#!/usr/bin/env python3
"""
Validates the judges' condition results against the plan and merges them into one
assessment_result.json for render_assessment_report.py (weighted-pass-fail plans).

Each judge file holds a part of the result (agents/manual-qa-assessment-judge.md):
    skills, skill_results            group A, per skill
    competency_results               groups B and C, per competency
    gate, notes                      optional
A condition with met false also needs `locations` (see the judge file, rule 3a): Excel cells
as {file, sheet, cell, quote}, text lines as {file, line, quote}, missing things as
{file, absent, kind} (kind "file": the file/folder itself is missing; "content": it exists but lacks the thing).
With --submission-dir every file, sheet, cell and verbatim quote is checked, and an `absent` claim is checked against the folder: a "file" claim about a file that exists is rejected.
Checks, per part:
  - the file is valid JSON
  - every skill has an entry for every group A criterion, every competency for every
    criterion of the other groups, with exactly as many results as the criterion has
    conditions (in the order of the plan)
  - each result is a bool, or an object with `met` (true/false/null) and, unless met is
    null, a non-empty `evidence`; a false result must say what is wrong
  - skills map to competencies of the plan; no competency or skill is reported twice
  - conditions at positions the criterion lists in `human_conditions` are reported null
Problems are listed per file so only the affected judge has to run again; nothing is
written while any problem remains.

Usage:
    python scripts/merge_judge_results.py --plan eval_plan.json --out assessment_result.json \n        --submission-dir path/to/submission judge/A.json judge/comp-*.json
"""
import argparse
import json
import re
import sys
from pathlib import Path

_cache = {}


def norm(t):
    return re.sub(r"\s+", " ", str(t)).strip()


def file_text(path):
    """Text of a file, or {"sheet": {"A1": "value"}} for a workbook; None when unreadable."""
    if path not in _cache:
        try:
            if path.suffix.lower() in (".xlsx", ".xlsm"):
                import openpyxl
                wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
                _cache[path] = {ws.title: {c.coordinate: c.value for row in ws.iter_rows() for c in row
                                           if c.value is not None} for ws in wb.worksheets}
            elif path.suffix.lower() in (".png", ".jpg", ".jpeg", ".docx", ".pdf"):
                _cache[path] = ""
            else:
                _cache[path] = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            _cache[path] = None
    return _cache[path]


def check_location(loc, root, where, problems):
    if not isinstance(loc, dict) or not loc.get("file"):
        problems.append(f"{where}: a location needs a `file` (path relative to the submission root)")
        return
    if "absent" in loc:
        if not str(loc["absent"]).strip():
            problems.append(f"{where}: `absent` is empty; say what is missing")
        kind = loc.get("kind")
        if kind not in (None, "file", "content"):
            problems.append(f"{where}: `kind` must be \"file\" (the file/folder itself is missing) or \"content\" (it exists but lacks the thing)")
        elif root is not None and loc.get("file"):
            exists = (root / loc["file"]).exists()
            if kind == "file" and exists:
                problems.append(f"{where}: {loc['file']} exists in the submission, so it is not absent (list the folder before claiming a file is missing)")
            elif kind == "content" and not exists:
                problems.append(f"{where}: {loc['file']} does not exist, so nothing can be missing inside it; use \"kind\": \"file\"")
            elif kind is None and exists:
                problems.append(f"{where}: {loc['file']} exists; add \"kind\": \"content\" if something is missing inside it (a row, a section, a sheet), or drop the claim if the file itself was thought missing")
        return
    if not (loc.get("quote") and (("sheet" in loc and "cell" in loc) or "line" in loc)):
        problems.append(f"{where}: needs a `quote` plus either sheet+cell (Excel) or line (text), or `absent`")
        return
    if root is None:
        return
    path = root / loc["file"]
    if not path.exists():
        problems.append(f"{where}: file not found: {loc['file']}")
        return
    body = file_text(path)
    if body is None:
        problems.append(f"{where}: cannot read {loc['file']}")
    elif isinstance(body, dict):
        sheet = body.get(loc.get("sheet"))
        if sheet is None:
            problems.append(f"{where}: sheet {loc.get('sheet')!r} not in {loc['file']} (sheets: {list(body)})")
        else:
            val = sheet.get(str(loc.get("cell", "")).upper())
            if val is None:
                problems.append(f"{where}: cell {loc.get('sheet')}!{loc.get('cell')} is empty or missing in {loc['file']}")
            elif norm(loc["quote"]) not in norm(val):
                problems.append(f"{where}: quote not found in {loc.get('sheet')}!{loc.get('cell')} of {loc['file']}; the cell holds {norm(val)[:80]!r}")
    elif body:
        if norm(loc["quote"]) not in norm(body):
            problems.append(f"{where}: quote not found verbatim in {loc['file']}: {norm(loc['quote'])[:80]!r}")
        else:
            lines = body.splitlines()
            n = loc.get("line")
            first = norm(str(loc["quote"]).splitlines()[0])[:60]
            if not (isinstance(n, int) and 1 <= n <= len(lines) and first in norm(lines[n - 1])):
                problems.append(f"{where}: line {n} of {loc['file']} does not hold the start of the quote ({first!r})")


def check_cond(r, where, problems, human, root=None):
    if isinstance(r, bool):
        problems.append(f"{where}: a bare true/false has no evidence; give {{met, evidence}}")
        return
    if not isinstance(r, dict) or "met" not in r or r["met"] not in (True, False, None):
        problems.append(f"{where}: must be {{met: true|false|null, evidence}}")
        return
    if human and r["met"] is not None:
        problems.append(f"{where}: this condition is graded by a person; report met null")
    if not human and r["met"] is None:
        problems.append(f"{where}: met is null but the condition is not marked for a person")
    if r["met"] is not None and not str(r.get("evidence", "")).strip():
        problems.append(f"{where}: no evidence")
    if r["met"] is False:
        locs = r.get("locations")
        if not isinstance(locs, list) or not locs:
            problems.append(f"{where}: unmet condition needs `locations` (exact file/sheet/cell/line + verbatim quote)")
        else:
            for k, loc in enumerate(locs):
                check_location(loc, root, f"{where}.locations[{k}]", problems)


def check_set(results, criteria, where, problems, root=None):
    for c in criteria:
        got = results.get(c["id"])
        if got is None:
            problems.append(f"{where}: no results for {c['id']}")
            continue
        if not isinstance(got, list) or len(got) != len(c["conditions"]):
            problems.append(f"{where}/{c['id']}: {len(got) if isinstance(got, list) else 'not a list'} results for "
                            f"{len(c['conditions'])} conditions")
            continue
        human_pos = set(c.get("human_conditions", {}).get("pass_when_all", []))
        for i, r in enumerate(got):
            check_cond(r, f"{where}/{c['id']}[{i}]", problems, i in human_pos, root)
    extra = sorted(set(results) - {c["id"] for c in criteria})
    if extra:
        problems.append(f"{where}: unknown or out-of-scope criteria {extra}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--submission-dir", type=Path, help="submission root: locations are checked against the real files")
    ap.add_argument("parts", nargs="+", type=Path)
    a = ap.parse_args()
    root = a.submission_dir

    asm = json.loads(a.plan.read_text(encoding="utf-8"))["scope"]["assessment"]
    import profile_loader as pl
    profile_dir = Path(__file__).resolve().parent.parent / "profiles" / asm["profile"]
    stale = pl.check_plan_fresh(asm, profile_dir)
    if stale:
        print(f"error: {a.plan} is stale (profile {asm['profile']!r} changed since it was built):")
        for p in stale:
            print(f"  - {p}")
        print("rebuild it with build_plan_from_profile.py before merging judge results")
        return 1
    a_crit = [c for c in asm["criteria"] if c["group"] == "A"]
    rest = [c for c in asm["criteria"] if c["group"] != "A"]
    merged = {"skills": [], "skill_results": {}, "competency_results": {}, "gate": None, "notes": []}
    by_file = {}

    for path in a.parts:
        probs = by_file.setdefault(path.name, [])
        try:
            part = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            probs.append(f"cannot read as JSON: {e}")
            continue
        names = {s.get("name") for s in part.get("skills", [])}
        for s in part.get("skills", []):
            if s.get("competency") not in asm["competencies"]:
                probs.append(f"skill {s.get('name')!r}: competency {s.get('competency')!r} is not in {asm['competencies']}")
            if not str(s.get("reason", "")).strip():
                probs.append(f"skill {s.get('name')!r}: no reason for the competency")
            if any(s.get("name") == m["name"] for m in merged["skills"]):
                probs.append(f"skill {s.get('name')!r} is reported twice")
        for skill, res in part.get("skill_results", {}).items():
            if skill not in names:
                probs.append(f"skill_results for {skill!r}, which is not in `skills` of this file")
            check_set(res, a_crit, f"skill {skill}", probs, root)
        for skill in names - set(part.get("skill_results", {})):
            probs.append(f"skill {skill!r} has no skill_results")
        for comp, res in part.get("competency_results", {}).items():
            if comp not in asm["competencies"]:
                probs.append(f"competency {comp!r} is not in {asm['competencies']}")
            if comp in merged["competency_results"]:
                probs.append(f"competency {comp!r} is reported twice")
            check_set(res, rest, f"competency {comp}", probs, root)
        if not probs:
            merged["skills"] += part.get("skills", [])
            merged["skill_results"].update(part.get("skill_results", {}))
            merged["competency_results"].update(part.get("competency_results", {}))
            merged["notes"] += [f"[{path.name}] {n}" for n in part.get("notes", [])]
            if part.get("gate"):
                g = part["gate"]
                merged["gate"] = merged["gate"] or {"verdict": "pending", "note": ""}
                merged["gate"]["note"] += (" | " if merged["gate"]["note"] else "") + f"[{path.name}] {g.get('note', '')}"

    bad = {f: p for f, p in by_file.items() if p}
    missing = [c for c in asm["competencies"] if c not in merged["competency_results"]]
    if bad or missing:
        for f, p in bad.items():
            print(f"{f}: {len(p)} problem(s)")
            for x in p[:25]:
                print(f"  - {x}")
        if missing and not bad:
            print(f"no results yet for competencies {missing}")
        print("nothing written")
        return 1
    if merged["gate"] is None:
        merged["gate"] = {"verdict": "pending", "note": "no judge reported gate observations"}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {a.out}: {len(merged['skills'])} skills, {len(merged['competency_results'])} competencies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
