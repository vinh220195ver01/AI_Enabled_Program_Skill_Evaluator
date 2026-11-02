# Prompt: assess one trainee's manual-QA submission

Paste into a Claude Code session opened at the repo root. Replace the `<...>` values.

```
Use skill-evaluator to assess one trainee's manual-QA submission with the manual-qa profile.

- Trainee: <trainee-id>
- Submission root: <path>/submission
- Assessment folder: <path>/assessment  (exam/ and baseline/, the trainer's answer-key workbooks for this exam only)
- Work folder: <path>/work/<trainee-id>  (never write into the submission folder)

Import the baseline workbooks into baseline.json first and show me the import notes. Grade with a separate subagent so grading is blind. Produce the scoring sheet with an evidence ref for every deduction. If any advisory flag is still pending a human decision, stop and ask me pass or fail for each before producing the final result.
```

## Before you run it

- `<assessment>/baseline/` holds the trainer's answer-key workbooks for that one exam (`Test_Requirement.xlsx`, `Bug_Report.xlsx`, optionally `Test_Case.xlsx`). The skill converts them to `baseline.json` with `scripts/import_baseline_xlsx.py`. Keep the folder out of the trainees' reach. If a `baseline.json` is already there, the skill uses it as is.
- Submission root layout: `skills/`, `chat-transcript.md`, `outputs/` (and `refined/` if the trainee submitted one, graded on group C only).

## What the skill already does without being told

Builds the plan from the profile criteria and this exam's baseline.json, replaces D1-D8 with group A, takes L1 from the first output in the chat transcript (one sample, no consistency claim), requires evidence refs as `path[:line] | path!Sheet!Cell | path#Heading`, and applies human decisions on advisory flags. See `evaluator/skills/skill-evaluator/references/assessment-profiles.md`.
