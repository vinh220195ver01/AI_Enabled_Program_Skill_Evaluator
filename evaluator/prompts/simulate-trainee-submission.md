# Prompt: simulate a trainee's complete submission

Builds a realistic, end-to-end trainee submission from the evaluator's own criteria, to use as a test fixture for the evaluator. The agent plays the trainee: it writes the skills, runs them for real, reviews and fixes the AI output, and hands in everything the evidence rules ask for.

Paste into a Claude Code session opened at the repo root. Replace the `<...>` values.

```
Act as a trainee of the AI-enabled QA course and produce one complete submission, end to end, graded by the evaluator's current criteria. The result is a test fixture for the evaluator.

Inputs
- Profile: <manual-qa | auto-qa>
- Exam folder: <path>/exam   (the task given to trainees: user story / requirements / manual test cases; for auto-qa also the test environment URL and test accounts)
- Competencies covered: <ids from competency_catalog, e.g. requirements-analysis, test-design, test-case-generation, test-data-generation>
- Sub-category (auto-qa only): <TCD | FWG | SCR | REV | EXE | RES | DEF>
- Target: <pass | planted>
- Planted defects (target planted only): <list of "criterion id: the condition to miss and how", or "none">
- Trainee persona: <name, QA experience, AI experience>
- Fixture folder: evaluator/test-fixtures/<fixture-name>/

Phase 0. Load the rules. Read them; do not rely on memory or on this prompt for their content.
1. Resolve the profile, then work only from the resolved file:
   python evaluator/skills/skill-evaluator/scripts/profile_loader.py evaluator/skills/skill-evaluator/profiles/<profile> --out <fixture>/design/resolved-criteria.json
   It holds groups A/B/C, the gate, the course pass_rule and scoring, competencies, and every criterion's clarifications and human_conditions.
2. Read evaluator/skills/skill-evaluator/profiles/_shared/skill-standard.md and SKILL.template.md (published to trainees).
3. auto-qa: read tech_stack, evidence_package and answer_key in the resolved file; for sub-category SCR also profiles/auto-qa/playwright-assessment.json.
4. Never open an answer key, a baseline, or any expected/ folder of other fixtures. A real trainee never sees them.

Phase 1. Design. Write <fixture>/design/plan.md before building anything:
- Evidence map: one row per condition of A1-A4, B1-B6, C1-C4 and the gate (auto-qa: the common conditions plus those of the chosen sub-category; SCR: plus the Playwright Assessment items). Columns: criterion, condition, the artefact that will show it, its path in the submission, and for target planted whether it will be missed and how the miss will show.
- Workflow map: the QA steps of the task, which ones use AI and why, control points, and where a human decides (B1, B5).
- Skill list: one skill per task, each with a distinct task and input (A3).

Phase 2. Build the submission in <fixture>/submission/ as the trainee would:
- skills/<skill-name>/: follow skill-standard.md. No project data anywhere in the skill folder (A4).
- knowledge/: the project's knowledge (business rules, glossary, screens), outside the skills, each file with a title, source and last-updated date (B2). auto-qa: produce these files from a skill step that explores the test environment with Playwright CLI, using test accounts and test data only.
- Run the skills for real. For every run, start a separate subagent that has only that skill and the run's input, and act as the trainee in that conversation. Save the complete, unedited transcript, including the skill invocation and tool calls, to transcripts/<nn>-<skill-name>-run<k>.md. Run each skill at least twice on similar input (B3). Never write or edit a transcript by hand.
- In those conversations, behave like a careful trainee: give the context the task needs, answer the skill's questions, stop and ask when input is missing, point to the exact AI mistake and the correct source when asking for a fix, rerun and re-check after fixing (B2, B4, C4).
- review-log.md: what was checked, against which source, what was fixed, and the re-check result (C4). For conditions listed in human_conditions, prepare the evidence a grader needs (e.g. notes explaining the code), but do not claim they are met.
- outputs/: the deliverables of each competency (manual-qa: clarification questions, TR, TC, test data; auto-qa: the deliverables B1 lists for the sub-category; SCR: a Playwright + TypeScript project with Page Objects, playwright.config, README, and run reports).
- auto-qa evidence (evidence_package): run logs (tsc, lint, npx playwright test, reports) under evidence/. Keep the trainee's project in its own git repository outside this repo, and export its history to evidence/git-log.txt; do not create a nested .git inside the fixture.
- README.md: how someone else runs the skills and the workflow (B6, C3).
- Gate: approved tools only, test accounts and test data only, no secrets anywhere.

Phase 3. Self-check. Do not run the evaluator's judge.
- For every condition in the evidence map, record met, not met (planted) or pending (a human condition), with the evidence path, in <fixture>/expected/conditions.json, in the format criterion_rules.py reads: {"<criterion id>": [{"met": true|false|null, "evidence": "<path[:line]>"}]}. Keep the condition order of each criterion: its own pass_when_all, then the sub-category's; should_items for a criterion whose rule counts them.
- Show the verdicts: python evaluator/skills/skill-evaluator/scripts/criterion_rules.py evaluator/skills/skill-evaluator/profiles/<profile> --results <fixture>/expected/conditions.json [--sub-category <X>]
- target pass: every verdict is pass or pending; fix the submission until it is. target planted: exactly the planted criteria fail.
- <fixture>/README.md: exam, persona, target, the planted defects and where each one shows, and every place where a rule is still undecided and which reading you followed.

Rules
- Do not change anything under evaluator/skills/.
- Use skill-standard.md as a trainee would. Do not paste criteria text into the skills or outputs.
- Where a rule is still undecided, follow the stricter reading and note it in the fixture README.
- Planted defects must look like natural trainee mistakes, not labelled errors. Nothing in submission/ may mention that a defect is planted.
- Keep the trainee's prompts realistic: short and informal, the way a trainee types.
- If the exam lacks something the task needs (e.g. a test environment or test accounts for auto-qa), stop and ask me.
```

## Before you run it

- **Exam folder:** prepare it first, with only what trainees receive. For auto-qa it must include a test environment URL and test accounts. Exploration may use test data only, and the prompt stops if these are missing.
- **Competencies:** use ids from `competency_catalog` in `profiles/_shared/course-rules.json`. manual-qa covers the ids in its `competencies`. auto-qa has no list yet, because the sub-category to competency mapping is still open.
- **Answer key:** a manual-qa fixture still needs the trainer's answer key in `baseline/` for grading C1 and C2. This prompt does not produce it, because the trainee never sees it. Auto-qa has no answer key.
- **Cost:** the run is long. Every skill runs at least twice in its own subagent, and auto-qa also builds and runs a Playwright project.

## What you get

| Path | What it is |
|---|---|
| `design/resolved-criteria.json` | The criteria the submission was built against (the profile, with shared files resolved) |
| `design/plan.md` | Evidence map, workflow map, skill list |
| `submission/skills/` | The trainee's skills |
| `submission/knowledge/` | Project knowledge, outside the skills |
| `submission/transcripts/` | Unedited transcripts of every skill run (at least 2 per skill) |
| `submission/review-log.md` | The trainee's verification record |
| `submission/outputs/` | Deliverables per competency |
| `submission/evidence/` | auto-qa: run logs, reports, `git-log.txt` |
| `submission/README.md` | How to run the skills and the workflow |
| `expected/conditions.json` | Expected result per condition, readable by `criterion_rules.py` |
| `README.md` | Persona, target, planted defects, and undecided rules followed |

To test the evaluator, grade `submission/` blind, then compare the judge's per-condition results with `expected/conditions.json`. Scores above criterion level (group, competency, pass line) cannot be compared yet, because the course has not decided how a pass/fail result becomes a number.
