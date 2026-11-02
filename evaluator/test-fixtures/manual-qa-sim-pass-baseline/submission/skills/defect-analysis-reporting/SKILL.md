---
name: defect-analysis-reporting
description: Use when manual test execution has produced failure evidence (screenshots, console logs, failed test results) and the failures must be analysed and written up as defect reports before they are logged; writes defect-analysis.md and bug-list.xlsx. Do NOT use to design or write test cases, or before any test has been executed.
---

# Defect Analysis and Reporting

Turns failure evidence into an analysis (facts, hypotheses, severity and priority with reasons) and a Bug List ready for the tracker.

## Inputs

- {failure_evidence}: screenshots, console logs and failed test results (for example the executed test case file with actual results). If missing, ask the user; never describe a failure that is not in the evidence.
- {environment}: build, browser and any other environment details, exactly as the user or the project documents give them. If an item is not given, write "Not provided" and list it as missing information; do not guess it.
- {tc_file}: the test case list with expected results, if available (default `{output_dir}/test-cases.xlsx`).
- {knowledge_dir}: the project's knowledge folder (requirements, screens, environment). If missing, ask the user.
- {output_dir}: the folder where the output files are written. If missing, ask the user.

## Process

1. List every evidence item with an ID (EV-01, EV-02, ...), its file name or source, and what it shows, word for word for messages and log lines.
2. Compare the actual result of each failure in the evidence with the expected result from {tc_file} or the requirement in {knowledge_dir}; mark the failure "Expected result not confirmed" if the expectation itself is an Assumption.
3. Group failures that show the same problem into one defect and give each defect a Bug ID (BUG-01, BUG-02, ...).
4. Write the facts of each defect (seen in evidence), the root cause hypotheses (labelled Hypothesis, with what would confirm them) and the missing information, keeping the three apart.
5. Assign severity and priority with `references/severity-priority-guide.md`, and write one reason for each.
6. Write `{output_dir}/defect-analysis.md` from `assets/defect-analysis-template.md`.
7. Write each Bug List row with `references/bug-report-rules.md`, filling Build and Browser only from {environment}, and tag notes with `../test-requirements-analysis/references/note-tags.md`.
8. Export by copying `assets/bug-list-template.xlsx` to `{output_dir}/bug-list.xlsx` and filling it, sorted by severity, keeping the sheet name, header row and column widths.
9. Verify that every bug has reproducible steps, one problem only, at least one evidence ID that exists in Step 1, and environment values that match {environment}.
10. Report to the user: the bug count by severity, the hypotheses that still need confirmation, the missing information; then stop, because a person confirms severity and priority, re-checks each bug and logs it.

## Exceptions

- Evidence cannot be opened or is unreadable: name the file, ask for a new copy; do not describe its content.
- Evidence and the requirement conflict, or the requirement is silent: report it as a question in the analysis; do not decide whether it is a bug.
- A failure cannot be explained from the evidence: write "Cause unknown" with the steps that would narrow it down; do not present a hypothesis as the cause.

## Output

- `{output_dir}/defect-analysis.md`: evidence reviewed, per defect facts / hypotheses / missing information, severity and priority with reasons.
- `{output_dir}/bug-list.xlsx`: one row per defect, in the layout of `assets/bug-list-template.xlsx`.

## Files

- `references/severity-priority-guide.md`: open at Step 5. Single source for severity and priority; any other skill that needs them links to this file.
- `assets/defect-analysis-template.md`: open at Step 6; copy it, never rebuild it.
- `references/bug-report-rules.md`: open at Steps 7 and 9.
- `../test-requirements-analysis/references/note-tags.md`: open at Step 7 (shared, single source).
- `assets/bug-list-template.xlsx`: open at Step 8; copy it, never rebuild it.
