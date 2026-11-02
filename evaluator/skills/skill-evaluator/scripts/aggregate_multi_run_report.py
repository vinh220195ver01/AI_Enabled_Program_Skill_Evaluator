#!/usr/bin/env python3
"""
Gộp N independent assessment_report.json files (N>=2 grading runs of the SAME plan and the
SAME trainee submission, e.g. consistency runs from Step 3's N-repeat guidance) into one
summary, averaged per competency: Markdown + Excel.

This does not re-grade anything. It reads each run's already-rendered
`report/assessment_report.json` (weighted-pass-fail model only, written by
render_assessment_report.py's render_weighted()) and reports, per competency:
  - group A/B/C points, averaged across runs
  - Competency Score, per run and averaged
  - which criteria Fail in ALL runs (consistent -- trust these first) vs only SOME runs
    (inconsistent -- judge noise at a borderline reading; flag for a person, don't average
    away by silently picking one run)

It does not compute a single official "total score": the course's `course-rules.json` only
defines a pass threshold per competency (>=3/5) plus the safety gate, not one combined number
across competencies. The report instead prints the per-competency breakdown (the thing that
actually gates a trainee's result) and, separately, an unweighted mean of the competency
scores labeled explicitly as a convenience indicator, not the course's pass rule.

Usage:
    python scripts/aggregate_multi_run_report.py \
        --reports evals/sim-pass-run-1/report/assessment_report.json \
                  evals/sim-pass-run-2/report/assessment_report.json \
        --label "trainee-sim-01 -- US-VP02" \
        --out-dir evals/sim-pass-summary/
"""
import argparse
import json
import sys
from pathlib import Path

from render_assessment_report import write_xlsx, S_CELL, S_HEAD, S_TITLE, S_SUB, S_NUM, S_EVID

HEADERS = ["Competency", "A (avg)", "B (avg)", "C (avg)",
           "Competency Score (per run)", "Avg Score", "Verdict", "Notes"]
WIDTHS = [30, 10, 10, 10, 26, 10, 10, 60]


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def mean(xs):
    xs = [x for x in xs if x is not None]
    return round(sum(xs) / len(xs), 4) if xs else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reports", nargs="+", required=True, help=">=2 assessment_report.json paths, same plan/trainee")
    ap.add_argument("--run-labels", nargs="*", help="short label per report, same order (default: run-1, run-2, ...)")
    ap.add_argument("--label", default="", help="trainee / exam label for the title")
    ap.add_argument("--out-dir", required=True, type=Path)
    a = ap.parse_args()

    if len(a.reports) < 2:
        print("error: need at least 2 reports to aggregate (N=1 is not a consistency claim)", file=sys.stderr)
        return 1
    reports = [load(p) for p in a.reports]
    labels = a.run_labels or [f"run-{i+1}" for i in range(len(reports))]
    if len(labels) != len(reports):
        print("error: --run-labels must have as many entries as --reports", file=sys.stderr)
        return 1
    for p, r in zip(a.reports, reports):
        if r.get("scoring_model") != "weighted-pass-fail":
            print(f"error: {p} is not a weighted-pass-fail assessment_report.json", file=sys.stderr)
            return 1

    sha = {r["criteria_sha256"] for r in reports}
    if len(sha) > 1:
        print(f"warning: reports were graded against different criteria versions ({sha}); "
              f"scores may not be comparable", file=sys.stderr)

    comp_ids = reports[0]["competencies"]
    comp_order = [c["id"] for c in comp_ids]
    by_run_comp = [{c["id"]: c for c in r["competencies"]} for r in reports]
    for i, bc in enumerate(by_run_comp):
        missing = [c for c in comp_order if c not in bc]
        if missing:
            print(f"error: {a.reports[i]} is missing competencies {missing} present in the first report", file=sys.stderr)
            return 1

    comps_out = []
    for comp in comp_order:
        per_run = [bc[comp] for bc in by_run_comp]
        groups_avg = {g: mean([pr["groups"][g]["points"] for pr in per_run]) for g in "ABC"}
        scores = [pr["competency_score"] for pr in per_run]
        avg_score = mean(scores)
        verdicts = {pr["verdict"] for pr in per_run}
        verdict = "fail" if "fail" in verdicts else ("pending" if "pending" in verdicts or None in scores else "pass")

        fail_sets = [{cid for cid, c in pr["criteria"].items() if c["verdict"] == "fail"} for pr in per_run]
        consistent_fail = set.intersection(*fail_sets) if fail_sets else set()
        only_some_fail = set.union(*fail_sets) - consistent_fail

        note_parts = []
        if consistent_fail:
            note_parts.append("Fail in ALL runs: " + ", ".join(sorted(consistent_fail)))
        if only_some_fail:
            detail = ", ".join(f"{cid} ({sum(cid in fs for fs in fail_sets)}/{len(fail_sets)})" for cid in sorted(only_some_fail))
            note_parts.append("Fail in only some runs (judge noise, needs a person): " + detail)
        if not note_parts:
            note_parts.append("Clean (no Fail) in every run.")

        comps_out.append({
            "id": comp, "groups_avg": groups_avg, "scores": scores, "avg_score": avg_score,
            "verdict": verdict, "consistent_fail": sorted(consistent_fail), "only_some_fail": sorted(only_some_fail),
            "note": " / ".join(note_parts),
        })

    overall_mean = mean([c["avg_score"] for c in comps_out])
    pass_threshold = reports[0].get("pass_threshold", 3)
    gates = [r.get("gate", {}).get("verdict", "pending") for r in reports]
    gate_verdict = "fail" if "fail" in gates else ("pass" if all(g == "pass" for g in gates) else "pending")
    mapping_reviewed = all(r.get("mapping_reviewed") for r in reports)
    any_comp_fail = any(c["verdict"] == "fail" for c in comps_out)
    any_comp_pending = any(c["verdict"] != "pass" for c in comps_out)
    if any_comp_fail or gate_verdict == "fail":
        overall_verdict = "FAIL"
    elif any_comp_pending or gate_verdict != "pass" or not mapping_reviewed:
        overall_verdict = "PENDING"
    else:
        overall_verdict = "PASS"

    summary = {
        "label": a.label, "runs": [{"path": str(p), "label": l} for p, l in zip(a.reports, labels)],
        "n_runs": len(reports), "pass_threshold": pass_threshold, "gate_verdict": gate_verdict,
        "mapping_reviewed": mapping_reviewed, "overall_mean_competency_score": overall_mean,
        "overall_verdict": overall_verdict, "competencies": comps_out,
    }
    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / "aggregate_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    # --- Excel ---
    table = []
    for c in comps_out:
        scores_str = " / ".join("-" if s is None else f"{s:.3f}" for s in c["scores"])
        table.append([
            (c["id"], S_CELL),
            (fmt(c["groups_avg"]["A"]), S_NUM), (fmt(c["groups_avg"]["B"]), S_NUM), (fmt(c["groups_avg"]["C"]), S_NUM),
            (scores_str, S_CELL), (fmt(c["avg_score"]), S_NUM), (c["verdict"].capitalize(), S_NUM),
            (c["note"], S_EVID),
        ])
    table.append([("TOTAL", S_SUB), ("", S_SUB), ("", S_SUB), ("", S_SUB),
                  ("Unweighted mean across competencies", S_SUB), (fmt(overall_mean), S_SUB),
                  (overall_verdict, S_SUB),
                  (f"Gate: {gate_verdict}; mapping reviewed: {mapping_reviewed}", S_SUB)])
    title = f"Aggregate Summary{' - ' + a.label if a.label else ''}"
    subtitle = (f"{len(reports)} independent grading run(s): {', '.join(labels)}. "
                f"Competency Score averaged per run; pass at {pass_threshold}/5 per competency plus the safety gate. "
                f"'Avg Score' is NOT the course's official total (none is defined across competencies) -- "
                f"see Notes for which Fails are consistent across runs vs. single-run noise.")
    xlsx_path = a.out_dir / "aggregate_summary.xlsx"
    orig_headers_widths = _patch_headers(HEADERS, WIDTHS)
    try:
        write_xlsx(xlsx_path, title, subtitle, table)
    except PermissionError:
        xlsx_path = a.out_dir / "aggregate_summary.new.xlsx"
        write_xlsx(xlsx_path, title, subtitle, table)
        print(f"warning: aggregate_summary.xlsx is open elsewhere; wrote {xlsx_path.name} instead", file=sys.stderr)
    finally:
        _restore_headers(*orig_headers_widths)

    # --- Markdown ---
    def cellmd(t):
        return str(t).replace("|", "\\|").replace("\n", "<br>")
    md = [f"# Aggregate Summary{' - ' + a.label if a.label else ''}", "",
          f"**{overall_verdict}** -- {len(reports)} independent grading runs: " + ", ".join(labels), "",
          "## Competency scores (averaged across runs)", "",
          "| " + " | ".join(HEADERS) + " |", "|" + "---|" * len(HEADERS)]
    for row in table:
        md.append("| " + " | ".join(cellmd(v) for v, _ in row) + " |")
    md += ["", f"Gate AI Safety & Responsible Use: **{gate_verdict}**",
           f"Skill -> competency mapping reviewed by trainer: **{mapping_reviewed}**", "",
           "## Reading this report", "",
           "- **Avg Score** is the mean of this competency's Competency Score across all runs -- "
           "the course's pass rule is per-competency (>= " + str(pass_threshold) + "/5) plus the gate, "
           "there is no single official total across competencies.",
           "- **Fail in ALL runs**: trust these -- the same gap showed up independently every time.",
           "- **Fail in only some runs**: judge noise at a borderline reading (wording, scope-of-criterion "
           "ambiguity). Don't treat as a confirmed defect until a person reviews it, or until a majority "
           "forms across >=3 runs.", "",
           "## Source runs", ""]
    for p, l in zip(a.reports, labels):
        md.append(f"- **{l}**: `{p}`")
    (a.out_dir / "aggregate_summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"{overall_verdict}; overall mean competency score = {fmt(overall_mean)}; "
          + ", ".join(f"{c['id']}={fmt(c['avg_score'])}" for c in comps_out))
    return 0


def fmt(x):
    return "pending" if x is None else x


def _patch_headers(headers, widths):
    import render_assessment_report as rar
    orig = (rar.HEADERS, rar.WIDTHS)
    rar.HEADERS, rar.WIDTHS = headers, widths
    return orig


def _restore_headers(headers, widths):
    import render_assessment_report as rar
    rar.HEADERS, rar.WIDTHS = headers, widths


if __name__ == "__main__":
    sys.exit(main())
