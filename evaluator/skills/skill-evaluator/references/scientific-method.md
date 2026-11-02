# Scientific Method Scaffolding

These are the hygiene rules that make an evaluation's conclusions trustworthy rather than just a set of numbers someone can dispute later. The individual concepts (pre-registration, blinding, controls, sample size) are borrowed from comparative-experiment design generally — what's specific to *this* framework is where each one gets enforced mechanically rather than left as advice: a hard gate in `SKILL.md` Step 1 that blocks Step 2/3 without a committed `eval_plan.json`, a `PRE_REGISTRATION_STATUS.json` marker `scripts/aggregate_layered.py` checks before aggregating, A/B labels `agents/comparator.md` won't reveal until after scoring. Eval work skips these constantly because it's tempting to just "run it and see" — the rules below matter less as ideas (most people already agree with them) than as the specific procedural teeth that make skipping them harder than following them.

The "Enforced by:" line under each rule below is itself a claim that can go stale — a cited file can be renamed, a cited rule can be renumbered. `scripts/check_consistency.py` mechanically checks the parts of these citations a script can check (does the file exist, does the cited rule number still exist) every time this skill's own bundle changes — it can't verify the citation is *true*, only that it isn't obviously dangling.

## 1. Pre-register before observing

**Enforced by:** `SKILL.md` Step 1's hard gate ("do not proceed past this step without `evals/eval_plan.json` on disk") and `agents/grader.md`'s rule against editing an assertion mid-grade, even to fix wording — both exist specifically to make the underlying rule procedural rather than a matter of willpower.

Write your hypothesis and your correctness assertions **before** looking at any actual run output. State explicitly what you expect to change and why.

**Why this matters:** once you've seen an output, it's nearly impossible not to unconsciously write assertions that fit what you already saw — "well obviously it should check for X" said only after noticing the output has X. This isn't dishonesty, it's how pattern-matching minds work, which is exactly why the safeguard has to be procedural (write it down first) rather than relying on willpower.

**In practice:** `evals/eval_plan.json` gets written and timestamped in Step 1, before any L1/L2 run happens. If you think of a good assertion mid-run, add it to `evals[].exploratory_assertions[]` (see `references/schemas.md`) rather than back-dating it into the pre-registered set — both are useful, but they answer different questions ("did we predict this correctly" vs. "what did we learn"), and Step 6 reports them in separate subsections per rule 6 below.

## 2. Define controls deliberately

**Enforced by:** `references/schemas.md`'s `eval_plan.json` schema requires a `baseline` object (`{"type": ..., "reference": ...}`) as part of pre-registration — there's no way to write a valid eval plan that skips stating what the control is, short of leaving the field empty and having that omission visible in the committed plan itself.

A number without a comparison point is nearly meaningless ("85% correctness" — compared to what?). Decide explicitly what the control is:
- **New skill, no prior version:** baseline is "no skill at all" (same prompt, same model, skill unavailable).
- **Improving an existing skill:** baseline is the previous version, not "no skill" — you already know the skill helps *some*; the question is whether the change helped *more*.
- **L1 vs L2:** the control for L2 is its own L1 — this is a within-test-case, before/after comparison, not a between-skill one.

Don't skip the control to save compute unless you already have strong, stated priors about the answer — and if you skip it, say so in the report rather than presenting an uncontrolled number as if it were controlled.

## 3. Fix sample size (N) before running, based on what you need to detect

**Enforced by:** `scripts/aggregate_layered.py`'s `mean_stddev` — a single run gets back `stddev: null, insufficient_data_for_stddev: true`, not a `0.0` that could be misread as confirmed-stable. The script won't let N=1 masquerade as a consistency finding even if nobody reads this rule.

N=1 gives you a point estimate with no idea whether it's typical or a fluke — LLM outputs vary run to run even with identical prompts and settings. N=3 is a workable default that at least distinguishes "this is roughly stable" from "this varies wildly." Increase N (5–10) when:
- The skill is high-stakes (errors are costly)
- Early runs show high variance
- You need to detect a small effect size (a 5% correctness improvement needs more samples to distinguish from noise than a 40% one)

Report variance (stddev) alongside every mean — a mean without a spread hides exactly the information that tells you whether the number is reliable.

## 4. Blind the grader where subjective judgment is involved

**Enforced by:** `agents/comparator.md`, which literally never receives the configuration labels ("A"/"B" only) until after both sides are scored — the reveal step (`label_mapping`) is structurally the last thing that happens, not a discipline the grader has to remember to maintain.

When scoring Quality (rubric-based, not assertion-based), the grader should not know which version/condition produced the output it's looking at. Label outputs "A" and "B" (or similar) rather than "with skill" / "without skill" or "v1" / "v2" when handing them to a judge for scoring. Reveal the mapping only after scores are recorded.

**Why this matters:** knowing which one is "the new version we're hoping is better" measurably biases quality judgments, even in careful graders. This is the same reason clinical trials blind evaluators — it's not about distrust, it's about removing a known source of systematic error.

Correctness (assertion) grading doesn't need blinding in the same way, since a well-written assertion is checked mechanically against the text regardless of which version it came from — but it's cheap insurance to blind that too if you're running it manually rather than by script.

## 5. Separate "did it get better" from "was it worth it"

**Enforced by:** `agents/refinement-analyzer.md`'s output schema (`references/schemas.md`'s `refinement-analysis.json`) keeps `substance_vs_polish` and `verdict` as two distinct fields — there's no single "better/worse" field to collapse them into even if someone wanted to.

An improvement is not automatically worth adopting. If L2 raises correctness by 2 percentage points but costs 4x the tokens and triples the wall-clock time, that's a real trade-off to surface, not an automatic win. Report the axes separately and let the delta analysis (`agents/refinement-analyzer.md`) state the trade-off explicitly rather than collapsing everything into one "better/worse" verdict.

## 6. Distinguish pre-registered findings from exploratory observations in the report

**Enforced by:** `evals[].exploratory_assertions[]` is a schema-level separate array from `evals[].assertions[]` (`references/schemas.md`) — there's no shared field or flag to accidentally blend them, and `SKILL.md` Step 6 requires reporting them in their own labeled subsection.

When writing up results, keep two sections: what confirmed or disconfirmed the stated hypothesis (the pre-registered part), and anything else noticed along the way (exploratory — useful for generating the *next* hypothesis, but not evidence for the current one). Mixing these together is how a report ends up overclaiming.

## 7. Re-run before trusting a surprising result

**Enforced by:** `references/schemas.md`'s `benchmark.json` requires a `hypothesis_check` field (`matched_expectation`, `surprising`, `rerun_completed`) — not script-checkable the way the pre-registration gate is, since deciding "surprising" means comparing a number against free-text hypothesis intent, which no script can do. But it's a *required* field, not an optional note: Step 7 can't silently skip the question the way it could if this were left as pure advice. A surprising result reported with `rerun_completed: null` is a visible, checkable gap, not a silent one.

If a result strongly contradicts expectation (a skill you believed was correct suddenly scores 40% pass rate, or a refinement step you expected to help shows regression), the first move is to re-run rather than to write the surprising number into the report. Distinguish a real effect from a fluky run, a grading bug, or an ambiguous assertion before concluding anything.
