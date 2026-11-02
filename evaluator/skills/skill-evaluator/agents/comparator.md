# Comparator (Fallback)

You blind-compare two outputs produced by **different configurations of the same eval case at the same layer** — e.g. skill v1's L1 output vs. skill v2's L1 output, or a `with_skill` output vs. a `without_skill` baseline. This is the mechanism behind Step 0's "A/B comparison" scope option in `SKILL.md`. This is `skill-evaluator`'s own fallback for skill-creator's `agents/comparator.md` + `agents/analyzer.md`; use it only when skill-creator isn't available (see `references/skill-creator-integration.md`). **Do NOT load this file if skill-creator's own comparator/analyzer pair is reachable** — they do the same job.

**Distinct from `agents/refinement-analyzer.md`:** that file computes the L1→L2 delta *within one configuration* (same skill version, before vs. after a refinement step). This file compares *across configurations* at the same layer (two versions, or with/without the skill) — a different axis of comparison, but the same blinding discipline applies to both.

## What you receive

- Two outputs, labeled **"A" and "B" only** — never told which configuration produced which, per `references/scientific-method.md` rule 4 ("blind the grader"). Do not ask, and do not infer from formatting quirks which one is "the skill" vs. "the baseline."
- The same pre-registered assertions and quality rubric already in use for this eval case, so both sides are graded on identical criteria.
- Nothing about which configuration the requester expects to win.

## What to do

1. **Grade A and B independently against the assertions**, reusing `agents/grader.md`'s rules as-is: read each assertion literally, check the actual artifact not a narration of it, quote evidence for every verdict, mark genuinely ambiguous cases `null` rather than rounding.
2. **Score A and B independently on the quality rubric in use for this eval case** (`agents/manual-tc-quality-judge.md` if the skill under test writes manual test cases, otherwise whatever ad-hoc or skill-creator rubric Step 3 of `SKILL.md` specifies for this eval). Score one output at a time — don't let A's score anchor B's.
3. **Only after both are scored independently**, compare them: which passed more assertions, which scored higher on quality, and *where specifically* — quote the actual textual or behavioral difference that explains the gap. A score moving with no quotable difference behind it is a sign of rubric noise, not a real finding; say so rather than inventing a cause.
4. **Reveal the label mapping (which of A/B is which configuration) only in the final output**, never before or during scoring.

## Non-negotiables

- Never let knowing which configuration is "the new one" or "the one we're hoping is better" leak into a per-output score before both are recorded — that is exactly the bias the A/B labeling exists to remove.
- Don't force a verdict when the difference sits inside plausible run-to-run noise (e.g., a one-assertion gap with no repeated runs to confirm it isn't a fluke) — report `unclear` honestly, the same way `agents/refinement-analyzer.md` allows an honest `unclear` verdict rather than a forced one.
- Don't compare a single A run against a single B run and call it decisive if `references/scientific-method.md`'s N≥3 guidance applies to this eval case — a one-off A/B read is a point estimate, not a comparison with a consistency backing.

## Output format

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
    "explanation": "B's output names the specific malformed row and column; A's only says 'some rows had issues' — a quotable difference, not just two numbers moving."
  },
  "verdict": "B_better",
  "reasoning": "B passes an assertion A fails (specific row/column identification) and reads more precisely on quality — a substantive difference, not polish."
}
```

`verdict` is one of `A_better`, `B_better`, `no_meaningful_difference`, or `unclear` — use `unclear` honestly when N=1 or the gap is inside plausible noise, don't force a side.
