---
name: test-case-generation
description: Use when a Test Requirement (TR) Excel list already exists and manual test cases must be written from it, one or more per TR, before test execution; exports the TC list as Excel. Do NOT use to analyse a raw user story.
---

# Test Case Generation

## Process

1. Open the TR Excel file and list every TR ID with its Notes.
2. Split complex TRs into several test cases so that each test case verifies one behaviour (rules in `references/tc-writing-rules.md`).
3. Write specific steps with concrete test data and an observable Expected Result.
4. Mark each TR tagged `Missing info — Must ask` as BLOCKED: its Expected Result starts with `TBD —` and its Notes start with `BLOCKED —`.
5. Carry the TR Notes tags (Assumption, Edge case, Risk, Nice to confirm) into the TC Notes.
6. Check that every TR ID has at least one test case, and that every edge case has its own.
7. Export by copying `assets/Test_Case_Template.xlsx`, keeping its title, header, styles and column widths, and fill the sheet "TC List".

## Files

- `references/tc-writing-rules.md`: open at Step 2 and again at Step 3.
- `assets/Test_Case_Template.xlsx`: open at Step 7; copy it, never rebuild it.
