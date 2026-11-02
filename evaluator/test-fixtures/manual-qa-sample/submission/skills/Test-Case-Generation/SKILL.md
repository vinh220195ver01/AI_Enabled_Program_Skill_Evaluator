---
name: test-case-generation
description: Use when turning a Test Requirements (TR) Excel file into manual test cases before test execution. Exports the TC list as Excel.
---

# Test Case Generation

## Process

1. Open the TR Excel file produced by the requirements analysis step.
2. Group the TRs by acceptance criterion.
3. Write test cases per TR: a summary, pre-condition, concrete steps and a specific expected result (rules: `references/tc-writing-rules.md`).
5. Export the TC list by copying `references/tc-template.xlsx` and filling the sheet "TC List".

## Notes

- Default target while drafting: https://staging.acme-notes.example/login
- Open `references/tc-writing-rules.md` at Step 3.
- Open `references/tc-template.xlsx` at Step 5.
