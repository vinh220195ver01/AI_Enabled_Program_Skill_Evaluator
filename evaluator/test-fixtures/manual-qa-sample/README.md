# Manual QA sample assessment (test fixture)

A made-up trainee submission with **planted flaws**, to exercise `skill-evaluator`'s manual-QA profile end to end. Everything here is fictional.

| Path | What it is |
|---|---|
| `exam/user-story.md` | The exam the trainee received (login, 4 ACs, build and browser given, no OS) |
| `baseline.json` | The sample answer key (5 ambiguities, 3 edge cases, 5 planted bugs). It is the per-exam answer key and sits next to `exam/`, as a real one would. |
| `submission/skills/` | The trainee's final skill set (group A is graded on this) |
| `submission/chat-transcript.md` | The trainee's chat (group B provenance; its first outputs are L1) |
| `submission/outputs/` | The submitted `tr-list.xlsx`, `tc-list.xlsx`, `bug-list.xlsx` |
| `expected/assessment_result.json` | What a correct judge should find: the planted errors per criterion, plus the C6-severity flag |
| `expected/human_decisions.json` | The human decision on that flag (`fail`) |
| `build_xlsx.py` | Regenerates all `.xlsx` files (stdlib only) |

## Planted flaws (expected score)

- **A (32/40):** uppercase folder (A1), name/folder mismatch (A2), description with no trigger (A3), steps numbered 1,2,3,5 (A4), an orphan file (A5), an Excel template under `references/` (A6), a staging URL and a project rule in the skill (A7: 2 errors). A8 clean.
- **B (24/30):** TC file name differs from the one created in the chat, and TC-09 cites TR-11 which is not in the TR file (B3); bug analysis lacks the 5th section (B4).
- **C (17/30 before the human decision):** mandatory ambiguity AMB2 missed (C1), AC4 and AMB2 without TR (C2), TR-07 / edge case EC2 without TC, counted once (C3), two vague Expected Results (C4), BUG-003 without Observed Result and an invented OS (C6), three rules not in the story: the password length rule, the spaces-only email message and the disabled Login button (C7). C5 clean: 3 of 5 bugs found, including the Critical and the Major one.
- **Advisory flag:** BUG-002 is `Trivial` against `Major` in the key, 2 levels apart, so `C6-severity` is flagged. BUG-001 (`Major` vs `Critical`) is 1 level and is not.

Expected total: **73/100, PASS, provisional**. With the human decision `fail` on the flag: **72/100, PASS, final**.

## Run it

From `evaluator/skills/skill-evaluator/`:

```
python scripts/build_plan_from_profile.py profiles/manual-qa --baseline ../../test-fixtures/manual-qa-sample/baseline.json --skill-name sample-trainee --hypothesis "The sample scores about 74" --out <work>/eval_plan.json
python scripts/render_assessment_report.py --plan <work>/eval_plan.json --result ../../test-fixtures/manual-qa-sample/expected/assessment_result.json --submission-dir ../../test-fixtures/manual-qa-sample/submission --out-dir <work>/report
python scripts/render_assessment_report.py --plan <work>/eval_plan.json --result ../../test-fixtures/manual-qa-sample/expected/assessment_result.json --human ../../test-fixtures/manual-qa-sample/expected/human_decisions.json --out-dir <work>/report-final
```

Each run writes `assessment_scoring_sheet.xlsx` (the scoring table), `assessment_report.md` and `.json`. `--submission-dir` makes the script check that every evidence ref points at a real file. That checks the scoring. To test the **judge**, give `agents/manual-qa-assessment-judge.md` the files under `submission/` and the plan, let it write its own `assessment_result.json`, and compare it with `expected/assessment_result.json`.

Known limits of the sample: the Python code in the transcript is abridged, the screenshots and `console.log` are only named, and TC/TR cells are not styled like the real template.
