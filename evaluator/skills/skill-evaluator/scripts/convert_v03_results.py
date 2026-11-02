#!/usr/bin/env python3
"""
Converts a result graded with the old v0.3 points model (error counts per criterion
A1-A8, B1-B4, C1-C7) into condition results of the current manual-qa criteria (T-04).

The two models do not line up one to one, so this is a partial conversion and says so:
  - profiles/manual-qa/v03-conversion.json maps each v0.3 criterion to the current
    conditions it checks (exact or approximate); a v0.3 error becomes an unmet condition
    with a location, and a mapped condition with no error becomes met.
  - A current condition that no v0.3 criterion checked stays pending ("no v0.3 equivalent").
    So does a competency the old exam did not cover: it is left out.
  - v0.3 criteria with no current equivalent (A5, A6, B1, the provenance part of B2-B4,
    the C6 severity flag) are listed, not converted.
  - The old result was graded for the whole submission, not per competency. Skills are
    mapped to competencies by folder name, and B and C errors by the file they point at
    (profile `competency` for C1-C6). Group A is converted per skill.
Because of the pending conditions the converted score is a RANGE: low counts every pending
condition as unmet, high counts it as met.

Outputs, next to --out-dir: assessment_result.v04.json (condition results, pending ones
`met: null`) and conversion_report.md.

Usage:
    python scripts/convert_v03_results.py --result old/assessment_result.json \
        --submission-dir path/to/submission --out-dir old/converted [--profile profiles/manual-qa]
"""
import argparse
import json
import re
import sys
from pathlib import Path

import criterion_rules as cr
from profile_loader import load_profile

HERE = Path(__file__).resolve().parent.parent
NONE_REASON = "no v0.3 equivalent"


def by_keyword(text, table):
    t = text.lower()
    for row in table:
        if row["keyword"] in t:
            return row["competency"]
    return None


def location(where, quote):
    where = where or ""
    if "!" in where:
        parts = where.split("!")
        if len(parts) >= 3:
            return {"file": parts[0], "sheet": parts[1], "cell": parts[2], "quote": quote}
        return {"file": parts[0], "sheet": parts[1], "absent": quote}
    m = re.match(r"^(.*?):(\d+)", where)
    if m:
        return {"file": m.group(1), "line": int(m.group(2)), "quote": quote}
    return {"file": where, "absent": quote}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--result", required=True, type=Path, help="v0.3 assessment_result.json")
    ap.add_argument("--submission-dir", required=True, type=Path, help="to read the skill folder names")
    ap.add_argument("--out-dir", required=True, type=Path)
    ap.add_argument("--profile", type=Path, default=HERE / "profiles" / "manual-qa")
    a = ap.parse_args()

    profile, _ = load_profile(a.profile)
    conv = json.loads((a.profile / "v03-conversion.json").read_text(encoding="utf-8"))
    old = json.loads(a.result.read_text(encoding="utf-8"))["criteria"]
    by_id = {c["id"]: c for c in profile["criteria"]}
    a_ids = [c["id"] for c in profile["criteria"] if c["group"] == "A"]
    rest_ids = [c["id"] for c in profile["criteria"] if c["group"] != "A"]
    size = {i: len(cr.conditions_for(c, cr.rule_for(profile, c)[0])) for i, c in by_id.items()}

    skills = {}
    for d in sorted((a.submission_dir / "skills").iterdir()):
        comp = by_keyword(d.name, conv["skill_competency_by_folder_keyword"])
        if d.is_dir() and comp:
            skills[d.name] = comp
    comps = sorted(set(skills.values()), key=profile["competencies"].index)

    # grid[(scope, crit)] = list of cond dicts; scope = skill name (A) or competency (B, C)
    grid = {}
    for s in skills:
        for i in a_ids:
            grid[(s, i)] = [{"met": None, "pending": NONE_REASON, "evidence": ""} for _ in range(size[i])]
    for c in comps:
        for i in rest_ids:
            grid[(c, i)] = [{"met": None, "pending": NONE_REASON, "evidence": ""} for _ in range(size[i])]
    log, unconverted = [], []

    def scopes(rule, where, text):
        """The grid scopes (skills or competencies) an old criterion / error refers to."""
        if rule["level"] == "skill":
            hit = [s for s in skills if s.lower() in (where or "").lower()]
            return hit or list(skills)
        comp = rule.get("competency") or by_keyword(where or "", conv["competency_by_file_keyword"])
        return [comp] if comp in comps else list(comps)

    for rule in conv["rules"]:
        oid = rule["old"]
        if oid not in old:
            log.append((oid, rule["name"], "not graded in this v0.3 result (not assessed)", []))
            continue
        errors = old[oid].get("errors", [])
        targets = rule["targets"]
        # a mapped condition with no error is met, for every scope the criterion covered
        covered = {(t["new"], t["cond"]) for t in targets if t["cond"] is not None}
        base_scopes = scopes(rule, "", "")
        if rule["level"] == "competency" and not rule.get("competency"):
            base_scopes = list(comps)
        for sc in base_scopes:
            for new, cond in covered:
                if (sc, new) in grid and grid[(sc, new)][cond]["met"] is None:
                    grid[(sc, new)][cond] = {"met": True, "evidence": f"v0.3 {oid} {rule['name']}: no error recorded ({rule['confidence']} match)"}
        if rule["confidence"] == "none" and not targets:
            for e in errors:
                unconverted.append((oid, e))
            log.append((oid, rule["name"], "no current equivalent", errors))
            continue
        placed = []
        for e in errors:
            text = f"{e.get('where', '')} {e.get('quote', '')}"
            pick = next((t for t in targets if t.get("match") and re.search(t["match"], text, re.I)), None)
            if pick is None and rule.get("default") is not None:
                pick = targets[rule["default"]]
            if pick is None or pick["cond"] is None:
                unconverted.append((oid, e))
                continue
            for sc in scopes(rule, e.get("where"), e.get("quote")):
                key = (sc, pick["new"])
                if key not in grid:
                    unconverted.append((oid, e))
                    continue
                cell = grid[key][pick["cond"]]
                if cell["met"] is False:
                    cell["locations"].append(location(e.get("where"), e.get("quote")))
                    cell["evidence"] += f"; v0.3 {oid}: {e.get('quote')}"
                else:
                    grid[key][pick["cond"]] = {"met": False, "evidence": f"v0.3 {oid} {rule['name']}: {e.get('quote')}",
                                               "locations": [location(e.get("where"), e.get("quote"))]}
                placed.append(f"{sc}/{pick['new']}[{pick['cond']}]")
        log.append((oid, rule["name"], f"{rule['confidence']}: {len(errors)} error(s) -> {', '.join(sorted(set(placed))) or 'none placed'}", errors))

    # --- score ranges ---------------------------------------------------------------
    def run(results, fill):
        flags = [r["met"] if r["met"] is not None else fill for r in results]
        return flags

    def outcomes_for(scope_results, ids, fill):
        return {i: cr.evaluate(cr.rule_for(profile, by_id[i])[0], run(scope_results[i], fill)) for i in ids}

    rows = []
    for c in comps:
        rng = {}
        for tag, fill in (("low", False), ("high", True)):
            merged = {}
            for i in a_ids:
                outs = [cr.evaluate(cr.rule_for(profile, by_id[i])[0], run(grid[(s, i)], fill)) for s, sc in skills.items() if sc == c]
                if not outs:
                    merged[i] = {"verdict": "fail", "score": 0.0}
                    continue
                merged[i] = {"verdict": "fail" if any(o["verdict"] == "fail" for o in outs) else "pass",
                             "score": sum(o["score"] for o in outs) / len(outs)}
            merged.update(outcomes_for({i: grid[(c, i)] for i in rest_ids}, rest_ids, fill))
            rng[tag] = cr.score_groups(profile, merged)
        rows.append((c, rng))

    # --- write -----------------------------------------------------------------------
    a.out_dir.mkdir(parents=True, exist_ok=True)
    result = {"converted_from": str(a.result), "profile_version": profile.get("version"),
              "skills": [{"name": s, "competency": sc, "reason": "mapped from the skill folder name"} for s, sc in skills.items()],
              "skill_results": {s: {i: grid[(s, i)] for i in a_ids} for s in skills},
              "competency_results": {c: {i: grid[(c, i)] for i in rest_ids} for c in comps},
              "gate": {"verdict": "pending", "note": "v0.3 had no gate; the current gate has no conditions yet"},
              "notes": ["Converted from a v0.3 result; conditions marked pending have no v0.3 equivalent."]}
    (a.out_dir / "assessment_result.v04.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    total = sum(len(v) for v in grid.values())
    known = sum(1 for v in grid.values() for r in v if r["met"] is not None)
    md = [f"# Quy đổi kết quả v0.3 sang criteria hiện tại", "",
          f"Nguồn: `{a.result}` · profile {profile.get('version')} · {known} / {total} điều kiện có dữ liệu từ v0.3, "
          f"{total - known} chưa có tương đương (pending).", "",
          "## Điểm competency (khoảng)", "",
          "Thấp = mọi điều kiện pending tính là không thỏa; cao = tính là thỏa. Ngưỡng đạt 3 / 5.", "",
          "| Competency | A (thấp–cao) | B | C | Điểm (thấp–cao) | Kết luận |", "|---|---|---|---|---|---|"]
    for c, rng in rows:
        lo, hi = rng["low"], rng["high"]
        def g(k):
            return f"{lo['groups'][k]['points']}–{hi['groups'][k]['points']}"
        verdict = ("đạt chắc chắn" if lo["competency_score"] >= 3 else "trượt chắc chắn" if hi["competency_score"] < 3 else "chưa kết luận được")
        md.append(f"| {c} | {g('A')} | {g('B')} | {g('C')} | {lo['competency_score']}–{hi['competency_score']} | {verdict} |")
    md += ["", "## Từng tiêu chí v0.3", "", "| Tiêu chí v0.3 | Kết quả quy đổi |", "|---|---|"]
    for oid, name, what, errs in log:
        md.append(f"| {oid} {name} ({len(errs)} lỗi) | {what} |")
    if unconverted:
        md += ["", "## Lỗi v0.3 không quy đổi được", ""]
        md += [f"- {oid}: `{e.get('where')}` — {e.get('quote')}" for oid, e in unconverted]
    md += ["", "## Không có tương đương ở criteria hiện tại", ""] + [f"- {x}" for x in conv["no_equivalent"]]
    md += ["", "## Điều kiện đã quy đổi thành không thỏa", ""]
    for (sc, i), conds in sorted(grid.items()):
        for k, r in enumerate(conds):
            if r["met"] is False:
                locs = "; ".join(f"{l['file']}" + (f" {l['sheet']}!{l['cell']}" if "cell" in l else f":{l['line']}" if "line" in l else "") for l in r["locations"])
                md.append(f"- **{sc} / {i}[{k}]**: {r['evidence']} ({locs})")
    (a.out_dir / "conversion_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{a.result}: {known}/{total} conditions converted; competencies {comps}")
    for c, rng in rows:
        print(f"  {c}: {rng['low']['competency_score']}-{rng['high']['competency_score']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
