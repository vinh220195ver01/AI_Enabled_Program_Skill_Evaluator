# Layers and Metrics

This is the object model the whole framework is built on. Read this before designing any eval — most eval-design mistakes come from scoring the wrong layer, or applying an axis where it doesn't make sense.

## Why layers, and why these four

A skill's output doesn't exist in isolation — it's the end of a chain: someone wrote instructions (L0) → the model followed them once (L1) → maybe someone or something reviewed and improved that (L2). If you only ever measure the final output, you can't tell *where* a problem originates. A bad final result could mean the instructions were ambiguous (L0), the model executed them poorly (L1), or the refinement step actually made things worse (L2 regressed relative to L1). Separating the layers is what lets you diagnose instead of just observe.

### L0 — Input Layer

**What it is:** The skill's own SKILL.md (description + instructions + bundled resources) and the test prompts you'll use to exercise it.

**What "good" looks like:**
- The description triggers on realistic should-trigger queries and stays silent on realistic should-not-trigger near-misses (see skill-creator's trigger-eval methodology if available — it's the rigorous version of this check).
- Instructions are unambiguous enough that independent runs converge on the same approach rather than diverging based on interpretation.
- Test prompts are realistic — the kind of thing an actual user types, messy phrasing and all, not a sanitized textbook example.

**Common failure mode this layer catches:** spending a full evaluation cycle on L1 only to discover every failure traces back to one ambiguous instruction ("process appropriately") that different runs interpreted three different ways. Cheaper to catch this before running N repeats of L1.

**Which axes apply:** Correctness (is the description factually accurate about what the skill does?) and Quality (rubric: clarity, triggering precision, prompt realism). Efficiency and Consistency don't really apply here — there's no "run" to time or repeat; L0 is evaluated once per skill version, not once per test case.

### L1 — Raw Output

**What it is:** What the model produces on a single, first pass through the skill given one L0 test prompt.

**What "good" looks like:** depends entirely on the skill — this is where skill-specific assertions live. A data-extraction skill's L1 output should have the extracted values correct; a writing skill's L1 output should read well and match the requested tone.

**Which axes apply:** All four.
- Correctness: assertion pass rate against the pre-registered checklist.
- Quality: blind rubric score for anything assertions can't capture.
- Efficiency: tokens, tool calls, wall-clock time for this single run.
- Consistency: only measurable across N≥3 repeats of the *same* prompt — a single run has no consistency score, only a point estimate.

**Baseline consideration:** L1 is usually where you'd run a baseline (no skill, or the previous skill version) alongside the "with skill" condition, because this is the layer where the skill's marginal contribution is most directly visible. Whether the baseline is worth the extra compute depends on Step 0 scoping — if you already have strong priors the skill helps (e.g. it wraps a hard file format), the baseline mainly confirms magnitude rather than direction, and you can economize by running it on a subset of test cases.

### L2 — Refined Output

**What it is:** What the model produces after L1 goes through the *actual* refinement mechanism the skill or workflow uses — a human-feedback-and-rerun loop, a self-critique step, an editor pass. This layer only exists if that mechanism genuinely exists in practice.

**Critical rule: do not invent a refinement step to get an L2 score.** If the skill has no real review/refine loop, skip L2 and L3 entirely and say so in the report. A synthetic "ask the model to improve its own output once, for the sake of having an L2" measures something, but it's not measuring the skill's actual refinement process — it's a different, weaker claim wearing the same L2 label, and this framework's Non-Negotiables treat it as a hard no, not a labeled-exploratory option: don't do it, full stop, not even flagged as exploratory. The risk isn't the first report that carefully labels it — it's the second one that quietly drops the label.

**Which axes apply:** Same four as L1, scored identically (same assertions, same rubric) so L1 and L2 numbers are directly comparable — that comparability is the entire point of this layer existing.

### L3 — Delta (computed, not measured)

**What it is:** L2 minus L1, per axis, per test case, then aggregated. Never measured directly — always derived from already-scored L1 and L2 data.

**What it answers:**
- Correctness delta: did refinement fix real defects, or leave the pass rate flat (or worse, regress it)?
- Quality delta: did it improve, and *where specifically* — cite the actual change, don't just report a number moving.
- Cost of refinement: extra tokens/time spent, set against the correctness/quality gain. A refinement step that costs 3x the tokens for a 2% correctness bump is a candidate for removal or simplification; report this trade-off explicitly rather than only reporting whether L2 "won."

**Failure mode this layer catches:** review/refinement loops that produce output that *reads* more polished (higher quality rubric score, more confident tone) without actually being more *correct* — polish and correctness are different axes and can move independently. Only tracking one gives a false sense of progress.

## Quick-reference grid

| | Correctness | Quality | Efficiency | Consistency |
|---|---|---|---|---|
| **L0 Input** | ✓ (accuracy of description) | ✓ (clarity, triggering) | — | — |
| **L1 Raw output** | ✓ | ✓ | ✓ | ✓ (needs N≥3) |
| **L2 Refined output** | ✓ | ✓ | ✓ | ✓ (needs N≥3) |
| **L3 Delta** | ✓ (derived) | ✓ (derived) | ✓ (cost of refining) | — (delta of a spread isn't meaningful the same way) |
