# Sample: Submit a Product Review, "perfect trainee" (test fixture)

A trainee whose outputs **are** the trainer's baseline, built from the trainer's own files. Use it to check that the prompt and `skill-evaluator` run end to end and that a flawless submission loses no points.

| Path | What it is |
|---|---|
| `exam/` | `User Story for My Shop.docx` (US-VP02), its text (`user-story.md`) and the two mockup images |
| `baseline/` | The trainer's workbooks `Test_Requirement.xlsx`, `Test_Case.xlsx`, and `baseline.json` produced from them by `import_baseline_xlsx.py` |
| `submission/skills/` | Two clean skills: `test-requirements-analysis`, `test-case-generation` |
| `submission/chat-transcript.md` | Chat with both skill invocations; the analysis and the Python code come from the baseline's own Appendix and `Python script` sheet |
| `submission/outputs/` | `Test_Requirement_US-VP02.xlsx`, `Test_Case_US-VP02.xlsx` (the baseline workbooks) |
| `expected/assessment_result.json` | The ideal grading: 0 errors on every assessed criterion |
| `build_fixture.py` | Rebuilds everything from the trainer's folder: `python build_fixture.py --source "<folder with exam/ and baseline/>"` |

## What is and is not assessed

No Bug Report baseline was given, so the exam has no bug-report competency: **B4, C5 and C6 are `not_assessed`** (recorded in `baseline.json`). The assessed total is 84 points and the pass line is scaled in the same proportion, **59/84** (70/100 rounded up). That scaling is an assumption of the framework, not a rule from the rubric; confirm it with the course owner.

Expected result: **84/84, PASS, final**. A real judge may still report a few errors. Each one needs an evidence ref; read them, they show where the criteria or the sample are loose.

## Defaults the importer applied (see `import_notes` in `baseline/baseline.json`)

- The 5 edge cases (TR_006, 007, 008, 014, 017) had no Mandatory value and defaulted to **mandatory**.
- The bug-report competency was left out, as above.

## Run it

From `evaluator/skills/skill-evaluator/`:

```
python scripts/build_plan_from_profile.py profiles/manual-qa --baseline ../../test-fixtures/manual-qa-sample-review/baseline/baseline.json --skill-name perfect-trainee --hypothesis "A trainee whose outputs equal the baseline loses no points" --out <work>/eval_plan.json
python scripts/render_assessment_report.py --plan <work>/eval_plan.json --result ../../test-fixtures/manual-qa-sample-review/expected/assessment_result.json --submission-dir ../../test-fixtures/manual-qa-sample-review/submission --out-dir <work>/report
```

To test the judge or the prompt in `evaluator/prompts/run-manual-qa-assessment.md`, point the assessment folder at this fixture (`exam/`, `baseline/`) and the submission root at `submission/`, then compare the judge's `assessment_result.json` with `expected/`.

Known limits: the submission has no bug competency; the baseline is not independent of the submission (they are the same files), so this sample can show a judge being too strict, but cannot show it missing a real defect. For that, use `../manual-qa-sample/` (planted flaws).
