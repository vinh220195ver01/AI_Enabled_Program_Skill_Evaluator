#!/usr/bin/env python3
"""
Layered benchmark aggregator for skill-evaluator.

Reads per-run result.json files (schema: references/schemas.md, "Layer-tagged
run record") from a workspace directory structured as:

    <workspace>/<layer>/<eval_id>/run-<n>/result.json

and produces a layer-tagged benchmark.json (schema: references/schemas.md,
"Layer-tagged benchmark.json") with mean/stddev per layer x configuration x
axis, plus an L3 delta section if both L1 and L2 data are present.

It also reads any sibling ab-comparison.json files (schema: references/schemas.md,
"ab-comparison.json") at the same run-<n> level -- output from agents/comparator.md's
blind A/B grading pass -- and aggregates them into an `ab_comparison_summary` per
layer: mean/stddev of the correctness/quality deltas across repeats, plus a tally
of how many runs landed on each verdict (A_better/B_better/no_meaningful_difference/
unclear), since `verdict` is categorical and doesn't average.

This script is self-contained (stdlib only) and works whether or not
skill-creator is available in the environment. If skill-creator's
scripts/aggregate_benchmark.py IS available and you'd rather feed its
flat benchmark.json into an existing viewer per-layer, you can also just
call this script once per layer directory and keep the outputs separate --
see references/skill-creator-integration.md.

Usage:
    python -m scripts.aggregate_layered <workspace_dir> --skill-name <name>
"""

import argparse
import json
import statistics
from pathlib import Path
from typing import Any, Dict, List


def _is_unregistered(run_dir: Path) -> bool:
    """A run-<n> directory carrying PRE_REGISTRATION_STATUS.json was produced
    without a committed eval_plan.json (see SKILL.md Step 1's gate) -- never
    silently fold it into a statistical summary, even if a result.json shows
    up in it later."""
    return (run_dir / "PRE_REGISTRATION_STATUS.json").exists()


def load_runs(layer_dir: Path) -> List[Dict[str, Any]]:
    runs = []
    if not layer_dir.exists():
        return runs
    for eval_dir in sorted(layer_dir.iterdir()):
        if not eval_dir.is_dir():
            continue
        for run_dir in sorted(eval_dir.glob("run-*")):
            if _is_unregistered(run_dir):
                continue
            result_path = run_dir / "result.json"
            if result_path.exists():
                with open(result_path) as f:
                    runs.append(json.load(f))
    return runs


def load_ab_runs(layer_dir: Path) -> List[Dict[str, Any]]:
    """Same run-<n> layout as load_runs, but reads ab-comparison.json instead of result.json."""
    runs = []
    if not layer_dir.exists():
        return runs
    for eval_dir in sorted(layer_dir.iterdir()):
        if not eval_dir.is_dir():
            continue
        for run_dir in sorted(eval_dir.glob("run-*")):
            if _is_unregistered(run_dir):
                continue
            ab_path = run_dir / "ab-comparison.json"
            if ab_path.exists():
                with open(ab_path) as f:
                    runs.append(json.load(f))
    return runs


def mean_stddev(values: List[float]) -> Dict[str, float]:
    if not values:
        return {"mean": None, "stddev": None, "n": 0}
    if len(values) == 1:
        # `stddev: 0.0` here would read as "confirmed zero variance" to anyone skimming
        # benchmark.json, when it actually means "we don't know yet" -- references/
        # scientific-method.md rule 3: "N=1 gives you a point estimate with no idea
        # whether it's typical or a fluke." Use null, the same "not enough data" signal
        # mean/stddev already use for an empty list, plus an explicit flag so a reader
        # doesn't have to infer it from n==1 alone.
        return {"mean": values[0], "stddev": None, "n": 1, "insufficient_data_for_stddev": True}
    return {
        "mean": round(statistics.mean(values), 4),
        "stddev": round(statistics.stdev(values), 4),
        "n": len(values),
    }


def summarize_configuration(runs: List[Dict[str, Any]]) -> Dict[str, Any]:
    # Every extraction below guards for key presence at both levels -- a run record
    # missing a field (e.g. no tool_calls captured, a quality axis skipped for this
    # skill) should be excluded from that mean, not raise a bare KeyError and abort
    # the whole aggregation over one incomplete run.
    # pass_rate can be present but `null` (agents/grader.md: every assertion in a case
    # graded `null` reports pass_rate: null, not 0.0) -- exclude None values the same way
    # a missing key is excluded, not feed them into statistics.mean() and crash.
    correctness = [r["correctness"]["pass_rate"] for r in runs if "correctness" in r and r["correctness"].get("pass_rate") is not None]
    quality = [r["quality"]["overall_score"] for r in runs if "quality" in r and "overall_score" in r["quality"]]
    tokens = [r["efficiency"]["tokens"] for r in runs if "efficiency" in r and "tokens" in r["efficiency"]]
    duration = [r["efficiency"]["duration_seconds"] for r in runs if "efficiency" in r and "duration_seconds" in r["efficiency"]]
    tool_calls = [r["efficiency"]["tool_calls"] for r in runs if "efficiency" in r and "tool_calls" in r["efficiency"]]

    return {
        "correctness": mean_stddev(correctness),
        "quality": mean_stddev(quality),
        "efficiency_tokens": mean_stddev(tokens),
        "efficiency_seconds": mean_stddev(duration),
        "efficiency_tool_calls": mean_stddev(tool_calls),
    }


_UNLABELED_CONFIG = "_missing_configuration"


def summarize_layer(runs: List[Dict[str, Any]]) -> Dict[str, Any]:
    # A run record missing `configuration` is NOT the same thing as one explicitly
    # labeled "with_skill" -- silently defaulting it there would fold an unlabeled run
    # into real with_skill statistics with no trace, the same silent-gap failure mode
    # the Non-Negotiables forbid for compute_l3_delta. Bucket it under a sentinel key
    # instead so main() can surface it as a note rather than eating it quietly.
    by_config: Dict[str, List[Dict[str, Any]]] = {}
    for r in runs:
        config = r.get("configuration", _UNLABELED_CONFIG)
        by_config.setdefault(config, []).append(r)
    return {config: summarize_configuration(rs) for config, rs in by_config.items()}


def _parse_delta(value: Any) -> Any:
    """delta fields in ab-comparison.json are strings like '+0.25', or null."""
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def summarize_ab(runs: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not runs:
        return {}

    correctness_deltas, quality_deltas = [], []
    verdict_counts: Dict[str, int] = {}
    for r in runs:
        delta = r.get("delta") or {}
        c = _parse_delta(delta.get("correctness_delta"))
        if c is not None:
            correctness_deltas.append(c)
        q = _parse_delta(delta.get("quality_delta"))
        if q is not None:
            quality_deltas.append(q)
        v = r.get("verdict", "unclear")
        verdict_counts[v] = verdict_counts.get(v, 0) + 1

    return {
        "n_runs": len(runs),
        "correctness_delta": mean_stddev(correctness_deltas),
        "quality_delta": mean_stddev(quality_deltas),
        "verdict_counts": verdict_counts,
        "note": "verdict is categorical and doesn't average -- verdict_counts is a tally "
        "across repeats, not a single verdict. A mixed tally (e.g. 2x B_better, 1x unclear) "
        "is itself a consistency finding, not noise to collapse into a majority vote.",
    }


def compute_l3_delta(l1_summary: Dict[str, Any], l2_summary: Dict[str, Any]) -> Dict[str, Any]:
    """Compare L1 vs L2 summaries for whichever `configuration` key both layers share.

    `configuration` isn't always "with_skill" -- references/schemas.md documents it as
    "with_skill / without_skill, or version identifiers when comparing two versions".
    L3 is specifically a within-configuration (before/after refinement) delta, so we need
    the one config key present in both layers, not a hardcoded guess -- silently returning
    {} when the workspace legitimately uses a different label (e.g. "v2") would make a real
    result vanish with no explanation, exactly the kind of silent gap the Non-Negotiables
    warn against.
    """
    shared_configs = sorted(set(l1_summary) & set(l2_summary))
    if not shared_configs:
        return {
            "note": f"No shared `configuration` key between L1 {sorted(l1_summary)} and "
            f"L2 {sorted(l2_summary)} -- nothing to delta. Check both layers used the "
            "same configuration label (e.g. both 'with_skill', or both the same version id)."
        }
    # "with_skill" is the conventional default when present; otherwise take the one shared
    # config deterministically (sorted) rather than guessing which the caller meant.
    config = "with_skill" if "with_skill" in shared_configs else shared_configs[0]
    other_shared = [c for c in shared_configs if c != config]
    l1 = l1_summary[config]
    l2 = l2_summary[config]

    def delta_str(a, b):
        if a.get("mean") is None or b.get("mean") is None:
            return None
        d = b["mean"] - a["mean"]
        return f"{'+' if d >= 0 else ''}{round(d, 4)}"

    correctness_delta = delta_str(l1["correctness"], l2["correctness"])
    quality_delta = delta_str(l1["quality"], l2["quality"])
    token_delta = delta_str(l1["efficiency_tokens"], l2["efficiency_tokens"])

    result = {
        "configuration": config,
        "correctness_delta": correctness_delta,
        "quality_delta": quality_delta,
        "extra_cost_tokens": token_delta,
        # Verdict is deliberately left for agents/refinement-analyzer.md to
        # judge with reasoning -- this script reports the numbers, not the
        # substance-vs-polish or worth-it call, which needs to read the
        # actual output text to be meaningful.
        "note": "See agents/refinement-analyzer.md output for substance-vs-polish "
        "and worth-it judgments -- this script only aggregates the numbers.",
    }
    if other_shared:
        # Don't silently drop other configs both layers happen to share -- flag them so
        # whoever reads this knows a choice was made, not that there was nothing else there.
        result["other_shared_configs_not_deltad"] = other_shared
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=Path)
    parser.add_argument("--skill-name", required=True)
    parser.add_argument("--n-repeats", type=int, default=None)
    args = parser.parse_args()

    layers_present = [
        layer for layer in ("L1", "L2") if (args.workspace / layer).exists()
    ]

    run_summary = {}
    unlabeled_counts: Dict[str, int] = {}
    for layer in layers_present:
        runs = load_runs(args.workspace / layer)
        # Count directly off the raw run list, not off any per-axis summary --
        # a run missing `configuration` AND missing e.g. `correctness` must still
        # be counted here, or the note below could undercount (or print 0 while
        # unlabeled runs actually exist).
        unlabeled_counts[layer] = sum(1 for r in runs if "configuration" not in r)
        run_summary[layer] = summarize_layer(runs)

    l3_delta = {}
    if "L1" in run_summary and "L2" in run_summary:
        l3_delta = compute_l3_delta(run_summary["L1"], run_summary["L2"])

    ab_comparison_summary = {}
    for layer in layers_present:
        ab_runs = load_ab_runs(args.workspace / layer)
        if ab_runs:
            ab_comparison_summary[layer] = summarize_ab(ab_runs)

    notes = []
    for layer, n in unlabeled_counts.items():
        if n:
            notes.append(
                f"{layer}: {n} run(s) had no `configuration` field and were NOT folded "
                "into with_skill -- fix the run records and re-aggregate rather than "
                "trusting this bucket's numbers."
            )

    benchmark = {
        "metadata": {
            "skill_name": args.skill_name,
            "layers_evaluated": layers_present,
            "n_repeats": args.n_repeats,
        },
        "run_summary": run_summary,
        "l3_delta": l3_delta,
        "ab_comparison_summary": ab_comparison_summary,
        # This script has no visibility into eval_plan.json's hypothesis text, so it
        # cannot decide "surprising" itself (references/scientific-method.md rule 7 --
        # that's a semantic judgment, not something to fake here). Stub it as
        # unfilled/null rather than a fake "false" default, so Step 6/7 in SKILL.md
        # can't mistake an unfilled stub for an actual "not surprising" judgment.
        "hypothesis_check": {
            "matched_expectation": None,
            "surprising": None,
            "rerun_completed": None,
            "note": "UNFILLED -- fill in per references/schemas.md before treating this report as final.",
        },
        "notes": notes,
    }

    out_path = args.workspace / "benchmark.json"
    with open(out_path, "w") as f:
        json.dump(benchmark, f, indent=2)

    print(f"Wrote {out_path}")
    print(json.dumps(benchmark, indent=2))


if __name__ == "__main__":
    main()
