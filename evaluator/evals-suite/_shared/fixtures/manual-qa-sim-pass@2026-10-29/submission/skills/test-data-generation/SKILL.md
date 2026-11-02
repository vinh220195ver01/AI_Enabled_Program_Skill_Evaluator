---
name: test-data-generation
description: Use when a manual test case Excel list already exists and the concrete input values for each test case (valid, invalid and boundary) must be prepared before test execution; exports a synthetic test data set as test-data.xlsx. Do NOT use to write test cases, design test conditions or analyse requirements.
---

# Test Data Generation

Produces the exact input values each test case needs, using synthetic data only.

## Inputs

- {tc_file}: the test case list (.xlsx written by the test-case-generation skill). Default: `{output_dir}/test-cases.xlsx`. If missing, ask the user.
- {design_file}: the test design with the value ranges used. Default: `{output_dir}/test-design.md`. Optional; if absent, take the ranges from {knowledge_dir}.
- {knowledge_dir}: the project's knowledge folder (fields and their rules). If missing, ask the user.
- {output_dir}: the folder where the output file is written. If missing, ask the user.

## Process

1. Open {tc_file} and list, for every TC ID, each field the steps fill in and the purpose of the value (valid, invalid or boundary).
2. Collect the rule of each field (type, length, range, format) from {design_file} or the field files in {knowledge_dir}, marked Confirmed (with source) or Assumption.
3. Generate one value per TC ID and field with `references/test-data-rules.md`, giving each value a Data ID.
4. Verify every boundary value by counting its length or comparing it with the limit, and verify that each invalid value breaks exactly one rule.
5. Check that the data set contains no real personal data, real accounts or secrets, following the privacy section of `references/test-data-rules.md`.
6. Export by copying `assets/test-data-template.xlsx` to `{output_dir}/test-data.xlsx` and filling it, keeping the sheet name, header row and column widths; tag notes with `../test-requirements-analysis/references/note-tags.md`.
7. Report to the user: the number of values per purpose, every value built on an Assumption, and any TC ID that has no data; then stop for review.

## Exceptions

- A field rule is unknown: generate the value only with an Assumption note that names the assumed rule, or ask the user; never present it as confirmed.
- A test case needs real or production data: do not create it; ask the user for an approved synthetic or masked set.
- A long value cannot be stored in one cell: state the generation rule in Value (for example a character repeated N times) and the exact length in Notes.

## Output

- `{output_dir}/test-data.xlsx`: one row per field value, in the layout of `assets/test-data-template.xlsx`.

## Files

- `references/test-data-rules.md`: open at Steps 3 and 5.
- `../test-requirements-analysis/references/note-tags.md`: open at Step 6 (shared, single source).
- `assets/test-data-template.xlsx`: open at Step 6; copy it, never rebuild it.
