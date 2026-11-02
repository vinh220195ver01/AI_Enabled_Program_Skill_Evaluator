# JSON Schemas

These schemas extend (and stay compatible with) skill-creator's `evals.json`, `grading.json`, and `benchmark.json` where noted, adding the layer dimension and the new L0/L3 concepts. If skill-creator's viewer/aggregator is present, layer-tagged files here are designed to still work with it — see `skill-creator-integration.md`.

---

## eval_plan.json

The pre-registration record from Step 1. Written before any run happens.

```json
{
  "skill_name": "example-skill",
  "skill_version": "v2",
  "created_at": "2026-09-19T10:00:00Z",
  "hypothesis": "v2's explicit error-handling instructions should raise correctness on malformed-input cases without materially increasing token cost.",
  "scope": {
    "layers": ["L0", "L1", "L2", "L3"],
    "has_refinement_step": true,
    "refinement_mechanism": "human feedback via eval-viewer, one revision pass",
    "primary_axes": ["correctness", "quality"],
    "n_repeats": 3,
    "quality_rubric": {
      "source": "agents/generic-quality-judge.md, written per Step 0.3's axis reasoning before any output was seen",
      "dimensions": {
        "clarity": {"1": "vague, could mean multiple things", "3": "mostly clear, one ambiguous phrase", "5": "no room for two readers to diverge"},
        "tone_fit": {"1": "wrong register for the audience", "3": "acceptable but generic", "5": "matches the requested tone precisely"}
      }
    }
  },
  "baseline": {
    "type": "previous_version",
    "reference": "v1"
  },
  "evals": [
    {
      "id": 1,
      "name": "malformed-csv-input",
      "prompt": "yo this csv export is busted again, 3rd time this week, can u just fix it",
      "files": ["exports/weekly_report.csv"],
      "assertions": [
        {"id": "a1", "text": "Output flags the malformed row instead of silently dropping it", "pre_registered": true},
        {"id": "a2", "text": "Output includes a corrected CSV file", "pre_registered": true}
      ],
      "exploratory_assertions": [
        {"id": "e1", "text": "Output also mentions which column had the bad value, not just the row", "added_after": "L1 run-2", "reason": "Noticed run-2's output already did this unprompted and it seemed genuinely useful — not evidence for the pre-registered hypothesis, but worth tracking for the next eval_plan.json revision."}
      ]
    }
  ]
}
```

**Fields:**
- `hypothesis`: free text, written before running anything
- `scope.layers`: which of L0/L1/L2/L3 apply to this evaluation — omit L2/L3 if there's no real refinement step
- `scope.has_refinement_step` / `refinement_mechanism`: forces an explicit statement of whether L2 is real or would be synthetic
- `scope.quality_rubric`: only present when quality is a primary axis and no fixed quality judge applies (i.e. `agents/generic-quality-judge.md` is in play, not `manual-tc-quality-judge.md` or a skill-creator judge) — the dimensions and score anchors, written before any L1 output exists, per that file's own rule against writing a rubric after seeing what it would grade
- `baseline.type` may be `assessment_baseline`, meaning the control is a fixed answer key (the exam's own `baseline.json`, passed with `--baseline`) rather than another configuration.
- `scope.assessment` (profile runs only): the frozen profile: `groups[]`, `criteria[]` (each `deduction` type with `max_points`, `penalty_per_error`, `details`, optional `na_when` and `advisory[]`), `pass_threshold`, `l0_override` (`mode: "replace"` swaps D1-D8 for one criteria group), plus `criteria_sha256` / `baseline_sha256` so a later edit to the profile is detectable. Optional `not_assessed[]` (`criterion`, `reason`) lists criteria the exam does not cover; they are removed from `criteria`, group totals shrink, and `pass_threshold` is scaled from `pass_threshold_original` / `full_total`. Written by `scripts/build_plan_from_profile.py`; see `references/assessment-profiles.md`. A profile run has no `scope.quality_rubric`.
- `scope.n_repeats`: N, fixed before running
- `baseline`: what L1 (and L2, if present) is compared against
- `evals[].assertions[]`: the pre-registered set — every entry has `pre_registered: true`. Never append a post-hoc assertion here, even with `pre_registered: false`; a mixed-flag array is exactly the kind of thing a future reader skims past without noticing which entries actually count as evidence.
- `evals[].exploratory_assertions[]`: a separate array (not a flag on `assertions[]`) for anything noticed mid-run worth checking going forward — `added_after` records when it was noticed, `reason` records why. These do not count toward `correctness.pass_rate` and are not evidence for the pre-registered hypothesis; they're raw material for the *next* `eval_plan.json`, per `references/scientific-method.md` rule 6 ("distinguish pre-registered findings from exploratory observations in the report").

---

## l0_scores.json

Output of the input-layer judge (Step 2): the 8-dimension, 1–5-per-dimension (40-point max) skill-quality rubric (`dimensions`) plus the three eval-design checks (`eval_design_checks`) from `agents/input-layer-judge.md`. Kept as separate top-level keys on purpose — `dimensions` scores whether the target skill's SKILL.md is well-designed (including D4's triggering quality); `eval_design_checks` scores three different things: whether this evaluation's own instructions-clarity read and prepared test prompts are trustworthy, *and* whether the description's claims are factually true (distinct from D4 — a description can trigger perfectly while overpromising). Mixing these into one 40+15-point total would hide which artifact a low score is actually about.

```json
{
  "skill_name": "example-skill",
  "skill_version": "v2",
  "pattern": "Tool",
  "knowledge_ratio": {
    "expert_pct": 65,
    "activation_pct": 25,
    "redundant_pct": 10
  },
  "eval_design_checks": {
    "instruction_clarity": {
      "score": 4,
      "max": 5,
      "notes": "Step 3 says 'handle malformed rows appropriately' with no criterion — the one ambiguous branch in an otherwise concrete workflow."
    },
    "test_prompt_realism": {
      "score": 5,
      "max": 5,
      "notes": "Eval prompt 2 reads like an actual user message ('yo this csv export is busted again'), not a cleaned-up spec."
    },
    "description_accuracy": {
      "score": 3,
      "max": 5,
      "notes": "Description claims 'automatic OCR fallback for scanned PDFs' — no OCR step found anywhere in SKILL.md or scripts/. Everything else checked out against actual content."
    }
  },
  "dimensions": {
    "d1_knowledge_payoff": {
      "score": 4,
      "max": 5,
      "notes": "Mostly expert-grade trade-offs, but the 'Setting Up Your Environment' section rehashes basic pip install steps the model already knows."
    },
    "d2_mindset_know_how": {
      "score": 4,
      "max": 5,
      "notes": "Includes a solid mental-model framework ('Before validating, ask...') plus a non-generic OOXML pack/unpack workflow."
    },
    "d3_gotchas_warnings": {
      "score": 3,
      "max": 5,
      "notes": "Has a NEVER list but only two of five items include the non-obvious WHY behind them."
    },
    "d4_description_quality": {
      "score": 4,
      "max": 5,
      "notes": "Description covers WHAT and WHEN with concrete trigger scenarios; missing a couple of discoverability keywords (file extensions)."
    },
    "d5_structure_layering": {
      "score": 4,
      "max": 5,
      "notes": "References directory exists with embedded MANDATORY loading triggers; SKILL.md is 340 lines, within the sweet spot."
    },
    "d6_freedom_fit": {
      "score": 3,
      "max": 5,
      "notes": "Correctly locks down the low-freedom file-format operations; one creative sub-task is over-scripted."
    },
    "d7_format_fit": {
      "score": 3,
      "max": 5,
      "notes": "Follows the Tool pattern well; decision tree for tool selection is present but not exhaustive."
    },
    "d8_real_world_usability": {
      "score": 4,
      "max": 5,
      "notes": "Strong fallback table for common failure modes; missing recovery guidance for encrypted-file edge case."
    }
  },
  "total_score": 29,
  "max_score": 40,
  "percentage": 72.5,
  "grade": "C",
  "verdict": "Adequate — genuine expert content throughout, but description keywords and gotcha rationale need tightening before this clears B.",
  "critical_issues": [
    "Step 3 says 'handle appropriately' with no further detail — candidate ambiguity."
  ],
  "top_improvements": [
    "Add non-obvious WHY to the remaining NEVER-list items in D3.",
    "Add missing file-extension keywords to the description for better discoverability.",
    "Cut the pip-install walkthrough in the setup section — the model already knows this."
  ]
}
```

`overrides_applied[]` (optional, top level of `l0_scores.json`): one entry per profile override of type `anchors`, `{"dimension": "D3", "default_score": 3, "final_score": 4}`. `dimensions.<dN>.score` always holds the final score. Empty or absent when no override applies.

**Why this shape:** `dimensions[].notes` is required, not decorative — a bare `total_score` without a quote-backed note is unusable at Step 7, because there's nothing to tell the skill's author which specific line to fix. `critical_issues` and `top_improvements` are kept as two separate arrays rather than one prioritized list: a critical issue is a reason to fix before shipping, an improvement is a reason to fix before the next version — merging them loses that distinction the moment someone skims just one array.

---

## Layer-tagged run record

One file per run, extending skill-creator's `grading.json` with a `layer` field. Located at `<workspace>/<layer>/<eval-id>/run-<n>/result.json`.

```json
{
  "eval_id": 1,
  "eval_name": "malformed-csv-input",
  "layer": "L1",
  "configuration": "with_skill",
  "run_number": 1,
  "correctness": {
    "expectations": [
      {"text": "Output flags the malformed row instead of silently dropping it", "passed": true, "evidence": "..."},
      {"text": "Output includes a corrected CSV file", "passed": true, "evidence": "..."}
    ],
    "pass_rate": 1.0
  },
  "quality": {
    "rubric": {"clarity": 4, "completeness": 5},
    "overall_score": 4.5,
    "judge_notes": "Clear explanation of what was flagged and why."
  },
  "efficiency": {
    "tokens": 3800,
    "duration_seconds": 24.1,
    "tool_calls": 6
  },
  "grading_notes": []
}
```

`correctness` may also carry an optional `coverage` block (`scenarios` and `verification_points`, each with `covered`, `required`, `missed[]`), written by `agents/manual-qa-assessment-judge.md`. `scripts/aggregate_layered.py` ignores it; it is for the report.

`grading_notes` (from `agents/grader.md`) is a sibling of `correctness`, not nested inside it — it carries anything that should feed back into L0 (ambiguous wording, bundled assertions, assertions that turned out untestable). Leave it `[]` when there's nothing to report; don't manufacture notes to fill the field.

`layer` is one of `L0` (rare — L0 doesn't usually get per-run records), `L1`, `L2`. `configuration` follows skill-creator's convention (`with_skill` / `without_skill`, or version identifiers when comparing two versions).

**Why this shape:** `layer` and `configuration` are kept orthogonal on purpose — `layer` answers "which pass produced this" (L1 vs L2), `configuration` answers "which variant" (with/without skill, v1/v2). Collapsing them into one field would make it impossible to compare L1-with-skill against L2-with-skill without also dragging in the without-skill baseline. `correctness.expectations[].passed` is deliberately not a plain boolean — `agents/grader.md` can write `null` for a genuinely ambiguous assertion, so an under-specified assertion doesn't get silently counted as either a pass or a fail; it shows up instead as a gap to fix at the next L0 pass.

`correctness.pass_rate` itself can also be `null` — not just the per-assertion `passed` field — for the edge case where *every* assertion in a case graded `null` (a 0/0 denominator). `agents/grader.md` reports `pass_rate: null` rather than `0.0` in that case, because `0.0` would misleadingly read as "failed every check" when the real finding is "no check was gradeable." Anything that aggregates `pass_rate` (e.g. `scripts/aggregate_layered.py`) must treat `null` the same way it treats a missing field — excluded from the mean, not coerced to zero.

---

## refinement-analysis.json

Output of `agents/refinement-analyzer.md` (Step 5). One file per eval case, at `<workspace>/L3/<eval-id>/refinement-analysis.json`.

```json
{
  "eval_id": 1,
  "correctness_flips": {
    "fail_to_pass": ["Output flags the malformed row instead of silently dropping it"],
    "pass_to_fail": []
  },
  "quality_change": {
    "delta": 0.4,
    "explanation": "The corrected-row explanation became specific (named the row and column) rather than generic ('some rows had issues')."
  },
  "substance_vs_polish": "substantive",
  "cost": {"extra_tokens": 1400, "extra_seconds": 8.2},
  "verdict": "worth_it",
  "reasoning": "Fixed a real defect (silently dropped malformed row) at a 37% token cost — justified for a skill whose failure mode is silent data loss."
}
```

**Why this is a separate file from `l3_delta` in `benchmark.json`, not folded into it:** `l3_delta` is a *numeric* aggregate `scripts/aggregate_layered.py` computes independently across N repeats, straight from `result.json` files — it never reads this file. `refinement-analysis.json` is the *qualitative* companion for a single eval case: which specific assertions flipped, whether the change was substance or polish, and a worth-it verdict — judgments only a reader of the actual output text can make, not something a script can derive from means and stddevs. Step 6 reports both side by side, but neither is a substitute for the other.

---

## Layer-tagged benchmark.json

Extends skill-creator's `benchmark.json` (see that skill's `references/schemas.md` for the base shape) by adding `layer` alongside `configuration` in every run record and in `run_summary`, and adding an `l3_delta` section.

```json
{
  "metadata": {
    "skill_name": "example-skill",
    "layers_evaluated": ["L1", "L2"],
    "n_repeats": 3
  },
  "run_summary": {
    "L1": {
      "with_skill": {
        "correctness": {"mean": 0.85, "stddev": 0.05},
        "quality": {"mean": 4.2, "stddev": 0.3},
        "efficiency_tokens": {"mean": 3800, "stddev": 400},
        "efficiency_seconds": {"mean": 24.1, "stddev": 3.2},
        "efficiency_tool_calls": {"mean": 6, "stddev": 1.0}
      }
    },
    "L2": {
      "with_skill": {
        "correctness": {"mean": 0.95, "stddev": 0.03},
        "quality": {"mean": 4.6, "stddev": 0.2},
        "efficiency_tokens": {"mean": 5200, "stddev": 500},
        "efficiency_seconds": {"mean": 31.5, "stddev": 4.0},
        "efficiency_tool_calls": {"mean": 8, "stddev": 1.2}
      }
    }
  },
  "l3_delta": {
    "correctness_delta": "+0.10",
    "quality_delta": "+0.4",
    "extra_cost_tokens": "+1400",
    "verdict": "Refinement meaningfully improved correctness and quality; extra token cost (37%) is justified given the correctness gain fixes a real defect class, not just wording polish.",
    "worth_it": true
  },
  "hypothesis_check": {
    "matched_expectation": true,
    "surprising": false,
    "rerun_completed": null,
    "note": "L2 correctness gain (+0.10) is in the direction and rough magnitude the pre-registered hypothesis predicted -- not a surprising result."
  },
  "notes": []
}
```

**Why `l3_delta` is a separate top-level section, not folded into `run_summary`:** it's derived, never independently measured — always L2 minus L1. Keeping it structurally apart from the measured `run_summary` blocks is a standing reminder that a surprising delta can't be sanity-checked against a run of its own; per `scientific-method.md`'s re-run rule, a suspicious `l3_delta` is a cue to re-check the L1/L2 inputs it was computed from, not a fact to report on its own.

**Why `hypothesis_check` is a required field, not an optional afterthought:** "was this surprising, and did you re-run before reporting it" is inherently a judgment call — no script can compare a numeric result against a free-text hypothesis and decide "surprising" for you, which is why this isn't listed as script-enforced the way the pre-registration gate is. Making it a required field instead of an optional note means Step 7 can't silently skip the question — `matched_expectation: false` or `surprising: true` with `rerun_completed: null` (not `true`) is a visible, checkable gap in the report, not a silent one. `rerun_completed` only applies when `surprising: true`; leave it `null` for an unsurprising result rather than `false`, since `false` would misleadingly suggest a re-run was skipped when none was needed.

---

## ab-comparison.json

Output of `agents/comparator.md` (Step 3's A/B-comparison branch). One file per repeat, at `<workspace>/<layer>/<eval-id>/run-<n>/ab-comparison.json` — the same `run-<n>` convention as `result.json` above, not a single flat file per eval case, so that N≥3 repeats of an A/B comparison can be aggregated into mean/stddev the same way every other metric in this framework is (a single A/B read is a point estimate, not a consistency claim, per the Non-Negotiables). It's a sibling of `result.json` rather than a replacement for it — kept in its own file because a blind A/B comparison covers *two* configurations and their delta at once, not one run's worth of fields.

```json
{
  "eval_id": 1,
  "comparison_type": "version_ab",
  "label_mapping": {"A": "v1", "B": "v2"},
  "A": {
    "correctness": {"pass_rate": 0.75, "expectations": [{"text": "...", "passed": true, "evidence": "..."}]},
    "quality": {"overall_score": 3.8, "judge_notes": "..."}
  },
  "B": {
    "correctness": {"pass_rate": 1.0, "expectations": [{"text": "...", "passed": true, "evidence": "..."}]},
    "quality": {"overall_score": 4.3, "judge_notes": "..."}
  },
  "delta": {
    "correctness_delta": "+0.25",
    "quality_delta": "+0.5",
    "explanation": "..."
  },
  "verdict": "B_better",
  "reasoning": "..."
}
```

**Why `label_mapping` is a separate field, not baked into `A`/`B`'s keys directly:** `agents/comparator.md` grades under "A"/"B" labels alone, blind to which configuration is which (per `scientific-method.md` rule 4) — `label_mapping` is filled in only *after* grading, as the reveal step. A reader who opens this file mid-grading (before `label_mapping` exists) should never be able to infer the mapping from the `A`/`B` blocks themselves. `scripts/aggregate_layered.py` parses this shape via `load_ab_runs`/`summarize_ab` and writes an `ab_comparison_summary` block into `benchmark.json` — mean/stddev of both deltas across repeats, plus a verdict tally (count of `A_better`/`B_better`/`no_meaningful_difference`/`unclear` across runs, since `verdict` is categorical and doesn't average).

---

## metrics_registry.json

The extensibility seam — see main SKILL.md "Extending this framework." **This file used to be illustrated here with real entries copied from the live registry (e.g. `assertion_pass_rate`, `run_variance`). That copy went stale four separate times** as the live file grew and its descriptions were corrected — most recently, this copy's `assertion_pass_rate.description` was still missing a "prefer skill-creator's grader when reachable" clause added to the live file rounds earlier. A disclaimer telling readers not to trust the copy didn't stop it from drifting again, so the copy itself is gone now, not just re-flagged.

Every entry in `references/metrics_registry.json` has exactly these fields — this is the shape, described abstractly, with no real entry values to go stale:

| Field | Type | Notes |
|---|---|---|
| `name` | string | unique metric identifier |
| `axis` | array of strings | one or more of `correctness`/`quality`/`efficiency`/`consistency` — always an array, even for one axis |
| `applies_to_layers` | array of strings | which of `L0`/`L1`/`L2`/`L3` this metric is meaningful for |
| `scorer_type` | string | one of `assertion` (script-checkable), `rubric` (needs a blind judge prompt), `derived` (computed from other metrics' already-recorded data) |
| `scorer_ref` | string | a pointer to the scoring logic (a script in `scripts/`, or a prompt in `agents/`) — not a place for routing-decision prose, which belongs in `description` instead |
| `description` | string | what the metric measures, plus any routing/disambiguation logic |

Read `references/metrics_registry.json` directly for the current, complete, real list — there is no substitute copy anywhere in this file to check it against, on purpose. To add a metric later (example: "hallucination_rate"): append an entry with these six fields to the live file, pointing to a new script or agent prompt. Nothing else in the framework needs to change.

**Why three `scorer_type`s and not just "script" vs "prompt":** `derived` is its own category because those metrics don't get their own grading pass at all — they're computed from `assertion`/`rubric` scores already recorded on other runs. Mislabeling a derived metric as `assertion` would send someone looking for a standalone scorer that was never meant to exist.
