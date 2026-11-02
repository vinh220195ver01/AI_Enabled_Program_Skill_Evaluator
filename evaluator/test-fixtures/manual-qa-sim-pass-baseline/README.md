# Fixture: simulated trainee submission, manual-qa (US-VP02)

Built on 2026-10-21 with `evaluator/prompts/simulate-trainee-submission.md`: AI agents played the trainer, then the trainee. Use it to test the evaluator on a complete, realistic manual-QA submission.

| | |
|---|---|
| Profile | manual-qa (criteria v0.11-draft, group A from `_shared/skill-standard.json` v1.2) |
| Exam | US-VP02 "Submit a Product Review" for My Shop (copied from `manual-qa-sample-review/exam`), plus a static demo app `exam/app/` (build demo-1.0) |
| Competencies | requirements-analysis, test-design, test-case-generation, test-data-generation, defect-analysis-reporting |
| Persona | trainee-sim-01: manual QA, about 2 years, finished the Beginner AI course, first time writing skills; prompts in English |
| Target | pass. **Not reached: see "Self-check result"** |

## Layout

| Path | What it is | Who may read it |
|---|---|---|
| `exam/` | What the trainee receives: user story, mockups, `app-note.md`, the demo app | Trainee, grader |
| `baseline/` | Trainer's answer key: `baseline.json` (US-VP02 ACs, ambiguities, edge cases from `manual-qa-sample-review`, plus the planted bugs) and `README.md` | Grader only |
| `submission/` | The trainee's submission (see `submission/README.md`) | Grader |
| `design/` | The simulated trainee's plan (`plan.md`: evidence map, workflow map, skill list) and the criteria it was built against (`resolved-criteria.json`) | Fixture maintainers |
| `expected/conditions.json` | Expected result per condition, readable by `criterion_rules.py` | Fixture maintainers; never the judge |

## How it was built

1. **Trainer (one subagent):** built the demo app with planted bugs and wrote `baseline/`. Its reply listed only file paths, so the trainee side never saw the bugs.
2. **Trainee (subagents):** one subagent wrote the plan, the 5 skills and `knowledge/`. Each skill then ran in its own session, driven by short trainee prompts: skills 1–4 twice, skill 5 once. The trainee reviewed every output against the sources, gave specific feedback in the same session, and recorded everything in `submission/review/review-log.md`.
3. **Test execution:** done by a "tester" subagent driving Chrome through `playwright-core`, through the UI only. It did not read the app's source, the baseline or other fixtures. In a real exam a person does this by hand.
4. **Transcripts:** `submission/transcripts/` are exported from the session logs. The trainee's messages, AI replies, tool calls and results are kept verbatim. Harness reminders and private thinking are left out, and the harness prefix in front of follow-up messages is removed.

## Simulated bugs

The bugs in `exam/app/` are simulated: a static page with planted defects, written by an agent playing the trainer. **They are to be replaced with real bugs later** (work log task T-08).

## Self-check result (`expected/conditions.json`)

`python evaluator/skills/skill-evaluator/scripts/criterion_rules.py evaluator/skills/skill-evaluator/profiles/manual-qa --results evaluator/test-fixtures/manual-qa-sim-pass/expected/conditions.json`

| Verdict | Criteria |
|---|---|
| pass | A1, A2, A3, A4, B1, B2, B4, B5, B6, C2 |
| fail | B3 (defect-analysis-reporting ran only once), C4 (retest finding RT-01 not yet handled in the bug report) |
| pending | C1 (needs the answer key: share of ambiguities found, Mandatory ones), C3 (labelled placeholders in BLOCKED cases, see below) |

Both fails come from stopping the bug-report work early (the user's instruction on 2026-10-21). Two steps would close them: run `defect-analysis-reporting` a second time (run-2), and update `bug-list.xlsx` / `defect-analysis.md` with RT-01 and the narrowed hypotheses from `submission/evidence/run-1/retest/retest-log.md`.

## Undecided rules and the reading followed

- **Shared content between skills (A4, M-28):** kept once in one skill and referenced by relative path from the others. A grader who requires every skill to be self-contained could fail A4.
- **Placeholders vs no guessing (C3 vs C4):** 22 test cases keep labelled placeholders (`[minimum]`, `[maximum]`, `[page size]`) and are BLOCKED until the PO answers, instead of inventing limits. A strict "no placeholders" reading fails C3, so it is marked pending.
- **"Allowed threshold" for minor omissions (C2, M-22):** undefined. The one known omission (the rating-summary bug) is stated in `submission/README.md`.
- **Fail conditions (M-06):** `criterion_rules.py` grades only `pass_when_all`. B3's fail condition "only one run is available as evidence" was applied by hand, through B3's repeatability condition.
- **Severity scale:** the trainee's skill uses its own guide (Critical / High / Medium / Low). The baseline uses Critical / Major / Minor / Trivial.

## Known limits

- The execution and the retests were simulated with a scripted browser. The screenshots are real captures of the demo app.
- Skills 2–4 run-2 used run-1's reviewed input of the previous step, so their consistency check covers the skill run, not the whole chain.
- The demo app resets on reload and has no sign-in, server or second product, so 26 test cases are NOT RUN by design.
