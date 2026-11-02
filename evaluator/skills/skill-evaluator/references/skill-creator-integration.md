# Integration with skill-creator

skill-evaluator is designed to sit alongside skill-creator, not duplicate it. If skill-creator is available in this environment — the path varies by deployment (`/mnt/skills/*/skill-creator/` on claude.ai, elsewhere on Claude Code or other hosts) — reuse the following directly:

| Need | Reuse from skill-creator | Notes |
|---|---|---|
| Assertion grading against a single output | `agents/grader.md` | Use as-is for L1 and L2 grading; the assertion format matches this skill's `eval_plan.json` |
| Statistical aggregation (mean/stddev/delta) | `scripts/aggregate_benchmark.py` | Works on skill-creator's flat `benchmark.json`. This skill's `scripts/aggregate_layered.py` wraps it to add the `layer` dimension — see that script's header comment for how it calls through |
| Side-by-side human review of outputs | `eval-viewer/generate_review.py` + `viewer.html` | Reads `benchmark.json` by the field names documented in skill-creator's `references/schemas.md`. This skill's layer-tagged benchmark file keeps those field names (`configuration`, `result.pass_rate`, etc.) inside each layer's block specifically so the existing viewer keeps working without modification — just point it at one layer's slice if it can't render the nested layer structure directly |
| Blind A/B comparison between two versions | `agents/comparator.md` + `agents/analyzer.md` | Directly applicable to comparing L1 vs L2 outputs blind, or two skill versions' L1 outputs blind — this is a good engine for the L3 delta analysis when you want more rigor than a single judge pass. **If skill-creator is absent**, this skill's own `agents/comparator.md` covers the version-vs-version case (L1→L2 within one version is already covered separately by `agents/refinement-analyzer.md`) |
| Trigger-description optimization (L0) | `scripts/run_loop.py`, "Description Optimization" section | This is the rigorous version of this skill's Step 2 description-quality check. Defer to it whenever available rather than relying only on `agents/input-layer-judge.md`'s lighter-weight rubric |
| Packaging the final skill | `scripts/package_skill.py` | Works on any skill folder, including this one or the one being evaluated |

## What skill-evaluator adds that skill-creator doesn't have

1. **The L0/L1/L2/L3 layer model itself** — skill-creator's loop is built around a single output layer (with a with-skill/without-skill or old/new-version split within that layer). It has no first-class concept of "the output after a refinement pass, scored comparably to before" — that's this skill's L2/L3 addition.
2. **Pre-registration discipline** — skill-creator drafts assertions "while runs are in progress" (i.e., after prompts are chosen but this skill pushes further back: hypothesis and assertions locked before *any* run, including the first one).
3. **Explicit axis separation** — skill-creator's `benchmark.json` mixes correctness (pass_rate) with efficiency (time, tokens) in one summary; this skill keeps quality as a distinct, separately-blinded axis rather than folding it into pass/fail.
4. **The metrics registry** — a first-class extensibility mechanism so new evaluation dimensions don't require touching the core workflow.

## When skill-creator isn't available

Everything in this skill still works standalone — `scripts/aggregate_layered.py` includes a self-contained aggregation path that doesn't call out to skill-creator's scripts, and `agents/grader.md`, `agents/input-layer-judge.md`, `agents/refinement-analyzer.md`, and `agents/comparator.md` are complete grading prompts on their own (`agents/grader.md` is the fallback for the "Assertion grading" row above; `agents/comparator.md` is the fallback for the "Blind A/B comparison" row — without it, Step 0's A/B-comparison scope option would have no engine to run on when skill-creator is absent). Present results directly in conversation (prompt + output + scores per test case) rather than via a browser viewer, following the same "no subagents, no browser" fallback pattern skill-creator itself uses on claude.ai.
