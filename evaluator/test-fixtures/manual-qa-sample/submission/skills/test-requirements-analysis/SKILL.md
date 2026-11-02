---
name: test-requirements-analysis
description: Use when reviewing a user story and its acceptance criteria before designing test cases, to find ambiguities and derive a Test Requirements (TR) list. Exports the TR list as Excel.
---

# Test Requirements Analysis

## Process

1. Read the user story and list every acceptance criterion with its ID.
2. Identify ambiguous, missing or conflicting points in the story.
3. Write clarification questions, split into "Must ask" and "Nice to confirm".
4. Derive Test Requirements per acceptance criterion; mark edge cases and assumptions in Notes (rules: `references/tr-rules.md`).
5. Export the TR list by copying `assets/tr-template.xlsx` and filling the sheet "Test Requirement".

## Notes

- Open `references/tr-rules.md` at Step 4.
- Open `assets/tr-template.xlsx` at Step 5. Keep its title, styles and column widths.
- A TR that traces to no acceptance criterion gets `N/A` in AC ID and its origin in Notes (Edge case / Risk / Assumption / Missing info).
