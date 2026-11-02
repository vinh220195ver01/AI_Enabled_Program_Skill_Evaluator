# Submission: US-VP02 Submit a Product Review

Trainee: trainee-sim-01 · Course: AI-enabled QA, Intermediate (manual) · Date: 2026-10-21

## What is here

| Path | What it is |
|---|---|
| `skills/` | 5 skills, one per QA task (see the table below) |
| `knowledge/` | Project knowledge for My Shop / US-VP02: rules, screens and fields, glossary, environment. Kept outside the skills; each file has a source and a last-updated date. Start with `knowledge/index.md` |
| `runs/run-1/` | The deliverables I reviewed and used: questions, TR list, test design, test cases, test data, execution results, bug report. `ai-original/` keeps the AI's first output before my changes |
| `runs/run-2/` | A second, independent run of skills 1–4, to check the output is consistent |
| `transcripts/` | Every skill session, exported from the session log (see the note at the top of each file) |
| `evidence/run-1/` | Screenshots and DOM text from test execution; `retest/` has the retests after review |
| `review/` | `review-log.md` (what I checked, against which source, what I fixed, the re-check), `consistency.md` (run-1 vs run-2), `effort-estimate.md` |

## Skills

| Order | Skill | Use it for | Input | Output (in your output folder) |
|---|---|---|---|---|
| 1 | `test-requirements-analysis` | A user story before any test design | User story + AC + mockups | `clarification-questions.md`, `test-requirements.xlsx` |
| 2 | `test-condition-design` | Choosing test conditions and techniques | `test-requirements.xlsx` | `test-design.md` |
| 3 | `test-case-generation` | Writing test cases | `test-requirements.xlsx`, `test-design.md` | `test-cases.xlsx` |
| 4 | `test-data-generation` | Synthetic data for the runnable test cases | `test-cases.xlsx` | `test-data.xlsx` |
| 5 | `defect-analysis-reporting` | Turning failure evidence into a bug report | Screenshots / logs / execution results + the environment the exam gives | `defect-analysis.md`, `bug-list.xlsx` |

Every skill also asks for `{knowledge_dir}` (the project's knowledge folder) and `{output_dir}`. If either is missing, the skill asks; it never guesses.

## How to run it

1. Copy `skills/` to your Claude Code skills folder (or point Claude at the skill's `SKILL.md`), and put the project's knowledge in a folder like `knowledge/`.
2. Start a Claude Code session and ask for skill 1 with the user story, the knowledge folder and an output folder, for example: "use the test-requirements-analysis skill on <story file>, knowledge in <folder>, output to <folder>".
3. Review the output at the control point before the next skill (table below). Each skill stops and waits for your approval.
4. Run skills 2, 3 and 4 the same way. Each one reads the previous step's file from the same output folder, so nothing is copied by hand.
5. Execute the runnable test cases in the browser yourself and save screenshots of failures. This step does not use AI.
6. Run skill 5 on the evidence, then confirm each bug before logging it.

New project? Only the input and the knowledge folder change. The skills hold no project data.

## Workflow and control points

| # | QA step | AI? | Why | Control point / human decision |
|---|---|---|---|---|
| 1 | Analyse requirements | Yes (skill 1) | Fast at listing gaps and edge cases | CP1 (high risk): check every question and TR against the story; decide Must ask vs Nice to confirm |
| 2 | Send questions to the PO, record answers | No | Talking to the customer is a human job | Human only |
| 3 | Design test conditions | Yes (skill 2) | Systematic, repeatable technique choice | CP2: check boundaries and techniques; approve before test cases |
| 4 | Write test cases | Yes (skill 3) | Mechanical step, AI keeps the format | CP3 (high risk): confirm expected results against the story and knowledge; the AI never finalises them |
| 5 | Prepare test data | Yes (skill 4) | Quick boundary and invalid values | CP4: check boundaries; synthetic data only |
| 6 | Execute tests, capture evidence | No | Actual results must come from what the tester sees | Human only |
| 7 | Analyse failures, write bugs | Yes (skill 5) | Structures evidence, separates facts from guesses | CP5 (high risk): confirm severity, priority and reproducibility before logging |

Stop and escalate to the trainer / PO when: the story is missing information that blocks expected results; two sources conflict (e.g. story vs demo build); a skill fails twice on the same step after a corrected input; an output cannot be verified from any source.

## Status of this submission

- PO answers: none received. Expected results that depend on open questions are marked "Assumption … until Q-xx is answered", BLOCKED, or OBSERVE ONLY (see `runs/run-1/test-cases.xlsx`).
- Execution on demo-1.0: 66 Pass, 9 Fail, 22 Observed, 22 Blocked, 26 Not run (145 cases).
- Bug report: 3 bugs in `bug-list.xlsx`. The retest after review found one more problem (the rating summary counts a pending review, `evidence/run-1/retest/retest-log.md` RT-01). It is not in the bug report yet (review log #11).
- `defect-analysis-reporting` ran once; skills 1–4 ran twice.
