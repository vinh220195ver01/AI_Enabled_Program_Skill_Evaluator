#!/usr/bin/env python3
"""
Builds an assessment's baseline.json from the trainer's baseline workbooks.

The trainer supplies the answer key as Excel files in the same layout trainees use:
  --tr   Test Requirement workbook  (sheet with headers: AC ID | Acceptance Criteria |
                                     TR ID | Test Requirements | Notes)
  --bug  Bug report workbook        (sheet with headers: ID | Summary | ... | Severity | ...)
  --tc   Test Case workbook, optional (kept as a reference file for the judge; its rows
                                     are not copied into baseline.json)

What is read, and where it comes from:
  acceptance_criteria  unique (AC ID, Acceptance Criteria) pairs, "N/A" rows skipped
  ambiguities          TR rows whose Notes start with "Missing info"; mandatory when the
                       Notes say "Must ask", not mandatory when they say "Nice to confirm"
  edge_cases           TR rows whose Notes start with "Edge case"; mandatory when the
                       sheet has a "Mandatory" column saying Yes/Y/True, otherwise the
                       default below applies and the row is listed in import_notes
  bugs                 one per bug row; severity from the Severity column. Without --bug
                       the exam has no bug-report competency: bugs is empty and B4, C5, C6
                       are listed under `not_assessed`
  severity_scale       the Severity dropdown of the bug sheet (its order = high to low),
                       else Critical, Major, Minor, Trivial

Nothing is invented silently: every default and every row that could not be classified is
written to `import_notes` in the output and printed. Source files are recorded with their
sha256 under `source_files`, so editing a workbook after import is detectable.

Usage:
    python scripts/import_baseline_xlsx.py --tr Test_Requirement.xlsx [--bug Bug_Report.xlsx] \
        [--tc Test_Case.xlsx] --assessment-id <id> --requirement-source <exam file> \
        [--build V --browser B --os O] [--edge-case-default mandatory|optional] \
        --out <assessment>/baseline.json
"""
import argparse
import hashlib
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
DEFAULT_SCALE = ["Critical", "Major", "Minor", "Trivial"]
DEFAULT_THRESHOLDS = {"ambiguity_found_pct": 70, "ambiguity_with_tr_pct": 70, "bug_found_pct": 60}


def col_of(ref):
    return re.match(r"[A-Z]+", ref).group(0)


def read_workbook(path):
    """Returns {sheet name: {"rows": {row number: {col: text}}, "validations": [(sqref, [options])]}}"""
    z = zipfile.ZipFile(path)
    ss = []
    if "xl/sharedStrings.xml" in z.namelist():
        ss = ["".join(t.text or "" for t in si.iter(M + "t")) for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(M + "si")]
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    out = {}
    for sh in ET.fromstring(z.read("xl/workbook.xml")).iter(M + "sheet"):
        target = rels[sh.get(R + "id")].lstrip("/")
        target = target if target.startswith("xl/") else "xl/" + target
        root = ET.fromstring(z.read(target))
        rows = {}
        for c in root.iter(M + "c"):
            t, v = c.get("t"), c.find(M + "v")
            if t == "inlineStr":
                val = "".join(x.text or "" for x in c.iter(M + "t"))
            elif v is None:
                continue
            else:
                val = ss[int(v.text)] if t == "s" else v.text
            if str(val).strip():
                rows.setdefault(int(re.search(r"\d+", c.get("r")).group(0)), {})[col_of(c.get("r"))] = str(val).strip()
        validations = []
        for dv in root.iter(M + "dataValidation"):
            f = dv.find(M + "formula1")
            if f is not None and f.text and f.text.startswith('"'):
                validations.append((dv.get("sqref", ""), [o.strip() for o in f.text.strip('"').split(",")]))
        out[sh.get("name")] = {"rows": rows, "validations": validations}
    return out


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def find_table(book, required):
    """First sheet and header row where every required header (prefix match) appears.
    Returns (sheet name, header row number, {header key: column letter}) or None."""
    for name, sh in book.items():
        for rn in sorted(sh["rows"])[:15]:
            cols = {norm(v): c for c, v in sh["rows"][rn].items()}
            found = {}
            for req in required:
                hit = next((c for h, c in cols.items() if h.startswith(req)), None)
                if hit is None:
                    break
                found[req] = hit
            else:
                for h, c in cols.items():
                    found.setdefault(h, c)
                return name, rn, found
    return None


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tr", required=True, type=Path)
    ap.add_argument("--bug", type=Path, help="omit when the exam has no bug-report competency")
    ap.add_argument("--tc", type=Path)
    ap.add_argument("--assessment-id", required=True)
    ap.add_argument("--requirement-source", required=True)
    ap.add_argument("--profile", default="manual-qa")
    ap.add_argument("--build")
    ap.add_argument("--browser")
    ap.add_argument("--os")
    ap.add_argument("--edge-case-default", choices=["mandatory", "optional"], default="mandatory",
                    help="used for edge cases when the sheet has no Mandatory column (default: mandatory)")
    ap.add_argument("--out", required=True, type=Path)
    a = ap.parse_args()

    for label, path in (("--tr", a.tr), ("--bug", a.bug), ("--tc", a.tc)):
        if path is None:
            continue
        if not path.is_file():
            print(f"error: {label} file not found: {path}", file=sys.stderr)
            return 1
        if not zipfile.is_zipfile(path):
            print(f"error: {label} {path.name} is not a valid .xlsx workbook", file=sys.stderr)
            return 1

    notes, problems = [], []

    # ---- TR workbook -------------------------------------------------------------------
    tr_book = read_workbook(a.tr)
    t = find_table(tr_book, ["ac id", "acceptance criteria", "tr id", "test requirements", "notes"])
    if not t:
        print(f"error: {a.tr.name}: no sheet with the headers AC ID | Acceptance Criteria | TR ID | Test Requirements | Notes", file=sys.stderr)
        return 1
    tr_sheet, hdr, c = t
    mand_col = next((col for h, col in c.items() if h.startswith("mandatory")), None)
    acs, ambs, edges, seen_ac = [], [], [], set()
    for rn in sorted(r for r in tr_book[tr_sheet]["rows"] if r > hdr):
        row = tr_book[tr_sheet]["rows"][rn]
        ac_id, ac_text = row.get(c["ac id"], ""), row.get(c["acceptance criteria"], "")
        tr_id, req, note = row.get(c["tr id"], ""), row.get(c["test requirements"], ""), row.get(c["notes"], "")
        ref = f"{a.tr.name}!{tr_sheet}!{c['test requirements']}{rn}"
        if ac_id and ac_id.upper() != "N/A" and ac_id not in seen_ac:
            seen_ac.add(ac_id)
            acs.append({"id": ac_id, "text": ac_text})
        n = norm(note)
        if n.startswith("missing info"):
            if "must ask" in n:
                mandatory = True
            elif "nice to confirm" in n:
                mandatory = False
            else:
                mandatory = None
                notes.append(f"{ref}: Missing info row has neither 'Must ask' nor 'Nice to confirm'; imported as not mandatory.")
            ambs.append({"id": f"AMB{len(ambs) + 1}", "description": req, "mandatory": bool(mandatory), "source_ref": ref, "tr_id": tr_id})
        elif n.startswith("edge case"):
            if mand_col and norm(row.get(mand_col, "")) in ("yes", "y", "true", "1"):
                mandatory = True
            elif mand_col and row.get(mand_col):
                mandatory = False
            else:
                mandatory = a.edge_case_default == "mandatory"
                notes.append(f"{ref}: no Mandatory value for edge case {tr_id}; defaulted to {'mandatory' if mandatory else 'optional'}.")
            edges.append({"id": f"EC{len(edges) + 1}", "description": req, "mandatory": mandatory, "source_ref": ref, "tr_id": tr_id})

    # ---- Bug workbook ------------------------------------------------------------------
    bugs, not_assessed, scale = [], [], DEFAULT_SCALE
    bug_book, bug_sheet, bhdr, bc = {}, None, 0, {}
    if a.bug is None:
        not_assessed = [{"criterion": cid, "reason": "the exam has no bug-report competency (no Bug Report baseline given)"}
                        for cid in ("B4", "C5", "C6")]
        notes.append("No Bug Report workbook given: B4, C5 and C6 are recorded as not_assessed; bugs is empty.")
    else:
        bug_book = read_workbook(a.bug)
        t = find_table(bug_book, ["id", "summary", "severity"])
        if not t:
            print(f"error: {a.bug.name}: no sheet with the headers ID | Summary | ... | Severity", file=sys.stderr)
            return 1
        bug_sheet, bhdr, bc = t
        scale = None
        for sqref, opts in bug_book[bug_sheet]["validations"]:
            if col_of(sqref.split(":")[0]) == bc["severity"]:
                scale = opts
        if scale is None:
            scale = DEFAULT_SCALE
            notes.append(f"{a.bug.name}: no Severity dropdown found; used the default scale {DEFAULT_SCALE} (highest first).")
    for rn in sorted(r for r in (bug_book[bug_sheet]["rows"] if bug_sheet else {}) if r > bhdr):
        row = bug_book[bug_sheet]["rows"][rn]
        summary, sev, raw_id = row.get(bc["summary"], ""), row.get(bc["severity"], ""), row.get(bc["id"], "")
        if not summary:
            continue
        ref = f"{a.bug.name}!{bug_sheet}!{bc['summary']}{rn}"
        if sev not in scale:
            problems.append(f"{ref}: severity {sev!r} is not in the scale {scale}")
        bid = f"BUG-{int(float(raw_id)):02d}" if re.fullmatch(r"\d+(\.0+)?", raw_id) else (raw_id or f"BUG-{len(bugs) + 1:02d}")
        location, _, symptom = summary.partition(":")
        bugs.append({"id": bid, "location": location.strip() if symptom else summary,
                     "symptom": summary, "severity": sev, "source_ref": ref})

    for label, items in (("acceptance_criteria", acs), ("ambiguities", ambs), ("edge_cases", edges), ("bugs", bugs)):
        if not items and not (label == "bugs" and a.bug is None):
            problems.append(f"nothing was imported for {label}; check the workbook layout")
    if problems:
        print("import_baseline_xlsx: problems, nothing written:\n", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    sources = {"test_requirement": a.tr, **({"bug_report": a.bug} if a.bug else {}), **({"test_case": a.tc} if a.tc else {})}
    if not a.tc:
        notes.append("No Test Case workbook given; the judge has no reference TC list.")
    for k, v in (("build", a.build), ("browser", a.browser), ("os", a.os)):
        if v is None and a.bug is not None:
            notes.append(f"environment_info_provided.{k} not given; left null (criterion C6 then treats any environment value the trainee fills in as invented).")
    baseline = {
        "profile": a.profile,
        "version": "imported",
        "assessment_id": a.assessment_id,
        "requirement_source": a.requirement_source,
        "severity_scale": scale,
        "thresholds": DEFAULT_THRESHOLDS,
        "acceptance_criteria": acs,
        "ambiguities": ambs,
        "edge_cases": edges,
        "bugs": bugs,
        "not_assessed": not_assessed,
        "environment_info_provided": {"build": a.build, "browser": a.browser, "os": a.os},
        "source_files": {k: {"file": v.name, "sha256": sha256(v)} for k, v in sources.items()},
        "import_notes": notes,
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(baseline, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {a.out}: {len(acs)} ACs, {len(ambs)} ambiguities "
          f"({sum(x['mandatory'] for x in ambs)} mandatory), {len(edges)} edge cases "
          f"({sum(x['mandatory'] for x in edges)} mandatory), {len(bugs)} bugs, scale {scale}")
    for n in notes:
        print(f"  note: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
