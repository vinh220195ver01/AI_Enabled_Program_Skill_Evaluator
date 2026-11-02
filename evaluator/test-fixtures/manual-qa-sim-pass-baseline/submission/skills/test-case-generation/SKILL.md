---
name: test-case-generation
description: Use when a reviewed Test Requirement Excel list and its approved test design (test conditions with techniques) already exist and manual test cases with steps and expected results must be written from them before test execution; exports test-cases.xlsx. Do NOT use to analyse a raw user story, to choose test techniques or to generate test data sets.
---

# Test Case Generation

Writes manual test cases, one behaviour each, traced to a TR and a test condition, with concrete steps and observable expected results.

## Inputs

- {tr_file}: the reviewed Test Requirement list (.xlsx). Default: `{output_dir}/test-requirements.xlsx`. If missing, ask the user.
- {design_file}: the approved test design (.md with condition IDs). Default: `{output_dir}/test-design.md`. If missing, ask the user; do not design conditions yourself.
- {knowledge_dir}: the project's knowledge folder (screens, field labels, messages, glossary, environment). If missing, ask the user.
- {output_dir}: the folder where the output file is written. If missing, ask the user.

## Process

1. Open {tr_file} and {design_file}, and list every TR ID with its condition IDs. Stop and ask the user if a condition points to a TR ID that is not in {tr_file}.
2. Read the screen, field and glossary files that the index in {knowledge_dir} lists for test cases, and use their labels and terms exactly.
3. Write one test case per test condition with `references/tc-writing-rules.md`: summary, pre-condition, numbered steps with the exact label of each control, and one observable expected result.
4. Take every expected result from a source (requirement, answer, knowledge file). Where no source states it, write the expected result as "To be confirmed: ..." and add a Missing info note with the question ID, using the tags in `../test-requirements-analysis/references/note-tags.md`.
5. Check traceability and quality: every TR ID and every condition ID has at least one test case, no two test cases verify the same thing, and each case passes the self-check in `references/tc-writing-rules.md`.
6. Export by copying `assets/test-case-template.xlsx` to `{output_dir}/test-cases.xlsx` and filling it, sorted by TR ID then TC ID, keeping the sheet name, header row and column widths.
7. Report to the user: the number of cases per TR, every "To be confirmed" expected result and every Assumption; then stop, because expected results must be confirmed by a person before execution.

## Exceptions

- A condition is too vague to write steps for: list it in the report and ask the user; do not invent behaviour.
- The design and the TR list disagree (missing TR, different wording of a rule): report the difference and ask which file is correct.
- The export fails: show the error, retry once with a corrected path, then stop and ask the user.

## Output

- `{output_dir}/test-cases.xlsx`: one row per test case, in the layout of `assets/test-case-template.xlsx`.

## Files

- `references/tc-writing-rules.md`: open at Steps 3 and 5.
- `../test-requirements-analysis/references/note-tags.md`: open at Step 4 (shared, single source).
- `assets/test-case-template.xlsx`: open at Step 6; copy it, never rebuild it.
