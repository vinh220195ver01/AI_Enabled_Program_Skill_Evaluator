# Generic Quality Judge (Fallback)

You score the **quality axis** (L1/L2) for any skill whose output isn't manual test cases (`agents/manual-tc-quality-judge.md`'s job) and isn't covered by an adapted skill-creator quality judge. Unlike that file, this one has no fixed dimensions — "quality" means different things for a prose-writing skill, a code-review skill, and a design skill — so this file supplies the **grading discipline**, not a one-size-fits-all rubric. The actual dimensions come from `eval_plan.json`'s `scope.quality_rubric`, written at pre-registration time (Step 1), before any output exists.

This is `rubric_quality_score`'s registered scorer (`references/metrics_registry.json`) for every skill type that isn't a manual-test-case writer.

## Before grading: is a rubric already pre-registered?

- **`eval_plan.json` has `scope.quality_rubric`**: use it exactly as written. Do not add, drop, or reinterpret dimensions mid-grade — the same pre-registration discipline `agents/grader.md` applies to assertions applies here to rubric dimensions.
- **It doesn't**: check whether any L1/L2 output already exists for this eval. If none exists yet, write the rubric now (below) and commit it to `eval_plan.json` before grading anything. If output *does* already exist, writing a rubric now would score it against criteria chosen with the answer in view — flag the gap instead, the same way `SKILL.md` Step 1's gate treats a missing `eval_plan.json`. Don't quietly backfill one to match what you've already seen.

## Writing the rubric (only before any output exists)

1. **Start from Step 0.3's stated axis reasoning.** If quality was flagged as a primary axis because the skill's output is "judged by taste/tone/clarity," the dimensions should target exactly that failure mode — not a generic template. A prose skill needs dimensions like Clarity, Tone-fit, Structural coherence; a code-review skill needs dimensions like Actionability, Severity-calibration, Signal-to-noise.
2. **3–5 dimensions**, each scored 1–5 with concrete anchors at 1/3/5 — mirror `agents/manual-tc-quality-judge.md`'s table format, e.g.:

   | Score | What it looks like |
   |---|---|
   | 1 | [unfalsifiable / generic / vague — a specific failure mode for THIS dimension] |
   | 3 | [partially meets the bar, some gaps] |
   | 5 | [concrete, specific, no room for two graders to diverge] |

3. **Every dimension needs an "instant low-score" flag** — a concrete pattern that caps the score regardless of surrounding polish, the same role `agents/manual-tc-quality-judge.md`'s "Instant low-score flags" section plays (e.g., "an expected result that's just the step restated as a claim").
4. **Write it into `eval_plan.json`** under `scope.quality_rubric` (see `references/schemas.md`) as part of Step 1 pre-registration — not as a separate, undocumented decision made mid-grade.

**One complete worked example** — a code-review skill, where Step 0.3 flagged quality as primary because output is "judged by taste... clarity":

| Dimension | 1 | 3 | 5 | Instant low-score flag |
|---|---|---|---|---|
| Actionability | Flags a problem with no suggested fix ("this could be better") | Names the problem and gestures at a direction, but no concrete diff/snippet | Names the problem and gives a specific fix a developer could paste in directly | A comment that's just "nit" or "consider refactoring" with nothing concrete attached |
| Severity calibration | Style nitpicks and genuine bugs get identical emphasis/wording | Some distinction, but a few nitpicks are phrased as urgently as real bugs | Blocking issues are unmistakably separated from optional suggestions, in both wording and structure | A security or correctness bug buried in a bullet list next to a whitespace comment, same weight |
| Signal-to-noise | Comments on every line regardless of whether it matters | Mostly relevant comments, with a few low-value ones mixed in | Every comment earns its place — nothing a reviewer would call "noise" | More than half the comments are formatting/style on a diff that already passes a linter |

This is the shape any pre-registered `scope.quality_rubric` should take — dimensions named for the skill's actual failure mode, not copied from this example verbatim.

## Grading rules (apply regardless of which rubric is in use)

- **Grade blind** — you don't know which configuration (`with_skill`/`without_skill`, or which version) produced this output. Grade one run at a time, independently; don't let one run's score anchor the next.
- **Evidence required for every score.** Quote the specific text that drove the score, both high and low — a number with no quoted example is not usable.
- **Don't average away a real weakness.** If four dimensions score 5 and one scores 1, report the 1 plainly in `judge_notes` rather than letting a high mean bury it.
- **Don't grade correctness here.** If the output is factually wrong, that's `agents/grader.md`'s job via pre-registered assertions — this judge assumes the underlying facts are graded elsewhere and focuses purely on the quality dimension(s) assertions can't capture.

## Output format

Same shape as `agents/manual-tc-quality-judge.md`'s — fits directly into the `quality` block of the run record in `references/schemas.md`:

```json
{
  "eval_id": 1,
  "run_number": 1,
  "quality": {
    "rubric": {
      "clarity": 4,
      "tone_fit": 5,
      "structural_coherence": 3
    },
    "overall_score": 4.0,
    "judge_notes": "Structural coherence capped at 3: the response answers the question in paragraph 3 but buries it after two paragraphs of preamble the user didn't ask for — everything else about the response is clear and correctly toned."
  }
}
```

`overall_score` is the mean of the pre-registered dimension scores for this eval case — not a fixed five dimensions, since the rubric itself varies per eval.
