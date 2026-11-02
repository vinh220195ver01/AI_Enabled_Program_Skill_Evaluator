# Run log: run-1

Trainee: trainee-sim-01 · Build under test: demo-1.0 (Chrome) · Date: 2026-10-21

Each skill ran in its own session. The transcript of every session is in `transcripts/`. The AI's first output of each skill is kept in `ai-original/` before any review change.

| Step | Skill / activity | Input | Output | Transcript | Review (see `review/review-log.md`) |
|---|---|---|---|---|---|
| 1 | test-requirements-analysis | exam/user-story.md, mockups, knowledge/ | clarification-questions.md, test-requirements.xlsx | 01-test-requirements-analysis-run1.md | #1, #2: fixed AC-GEN wording and the R5 source |
| 2 | test-condition-design | test-requirements.xlsx, clarification-questions.md | test-design.md (+ 6 new questions in clarification-questions.md) | 02-test-condition-design-run1.md | #3, #4: counts checked; CP2 decisions |
| 3 | test-case-generation | test-requirements.xlsx, test-design.md | test-cases.xlsx | 03-test-case-generation-run1.md | #5, #6: wording checked; CP3 decisions on unconfirmed expected results |
| 4 | test-data-generation | test-cases.xlsx | test-data.xlsx | 04-test-data-generation-run1.md | #7, #8: privacy and names |
| 5 | Test execution (no AI, by the tester) | test-cases.xlsx, test-data.xlsx, exam/app | test-execution.xlsx, evidence/run-1/ | none (manual step) | #9: failures sorted before bug analysis |
| 6 | Retest after review (no AI) | review findings | evidence/run-1/retest/ | none (manual step) | #10 |
| 7 | defect-analysis-reporting | test-execution.xlsx, evidence/run-1/, exam/app-note.md | defect-analysis.md, bug-list.xlsx | 09-defect-analysis-reporting-run1.md | #10, #11 |

Execution result (from `test-execution.xlsx`): 145 cases = 66 Pass, 9 Fail, 22 Observed (no verdict), 22 Blocked, 26 Not run.
