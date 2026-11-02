---
name: test-requirements-analysis
description: Use when a user story with acceptance criteria (and optional mockups) is given and a Test Requirement (TR) list is needed before any test case is written; finds ambiguities and clarification questions, then exports the TR list as Excel. Do NOT use to write test cases from an existing TR list.
---

# Test Requirements Analysis

## Process

1. Read the user story, its acceptance criteria (AC) and any mockup; give each AC an ID.
2. Separate facts, assumptions and missing information; never mix the three.
3. Identify ambiguous points, edge cases and risks per AC, tagging each with the origin tags in `references/tr-writing-rules.md`.
4. Draft clarification questions in two groups: "Must ask" (blocks test design) and "Nice to confirm".
5. Write the Test Requirements, one verifiable behaviour each, with an origin tag in Notes.
6. Export by copying `assets/Test_Requirement_Template.xlsx`, keeping its title, header, styles and column widths, and fill the sheet "Test Requirement".

## Files

- `references/tr-writing-rules.md`: open at Step 3 (origin tags) and again at Step 5 (wording rules).
- `assets/Test_Requirement_Template.xlsx`: open at Step 6; copy it, never rebuild it.
