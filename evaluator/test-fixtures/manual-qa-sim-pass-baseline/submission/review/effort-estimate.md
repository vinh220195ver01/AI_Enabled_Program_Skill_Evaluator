# Effort estimate: AI-assisted vs manual

Trainee: trainee-sim-01 · Story: US-VP02 · Date: 2026-10-21

The manual baseline is my estimate of doing the same work by hand, at the same depth, based on my usual pace. The AI-assisted figures are the session times from the transcripts, plus my estimate of my own review time.

| Step | Manual baseline (estimate) | AI-assisted: AI time (from the sessions) | AI-assisted: my review and decisions (estimate) |
|---|---|---|---|
| Requirements analysis: 32+6 questions, 41 TRs | 4 h | 6 min | 40 min |
| Test design: 145 conditions | 4 h | 8 min | 40 min |
| Test cases: 145 cases with steps and expected results | 12 h | 13 min | 1 h |
| Test data: 332 values | 2 h | 5 min | 20 min |
| Test execution: 97 runnable cases (no AI in both columns) | 5 h | – | 5 h |
| Bug analysis and report: 3 bugs + analysis | 1.5 h | 10 min | 40 min |
| **Total** | **28.5 h** | **about 45 min** | **about 8.5 h** |

AI-assisted total: about 9 h, against about 28.5 h by hand, so roughly a third. Most of the remaining time is test execution, which stays manual on purpose (actual results must come from what the tester sees), and reviewing the AI's output at the control points.

Limits of this estimate: the manual figures are not measured; the review times are my own estimate; the run-2 sessions (repeatability check) are not counted because they are not needed for the deliverables.
