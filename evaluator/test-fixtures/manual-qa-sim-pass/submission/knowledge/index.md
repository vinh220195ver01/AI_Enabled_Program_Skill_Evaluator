# Project knowledge index: My Shop, US-VP02 Submit a Product Review

Source: exam folder (`exam/user-story.md`, `exam/mockup-1.png`, `exam/mockup-2.png`, `exam/app-note.md`, `exam/app/`)
Last updated: 2026-10-21

This folder is the project knowledge that the QA skills read through `{knowledge_dir}`. It is kept outside the skills on purpose. Each fact lives in one file only.

## Files and when to read them

| File | Content | Read by skill |
|---|---|---|
| `product-review-rules.md` | The user story, its acceptance criteria, what is confirmed, assumptions and open questions | test-requirements-analysis, test-condition-design, test-case-generation, defect-analysis-reporting |
| `screens-and-fields.md` | Screens, sections, field labels and controls seen in the mockup and the demo build | test-requirements-analysis (step on mockups), test-condition-design, test-case-generation, test-data-generation |
| `glossary.md` | Terms used in this project and their meaning | all skills, when a term is unclear |
| `environment.md` | Build, browser, how to open the demo build | test-case-generation (pre-conditions), defect-analysis-reporting (Build and Browser) |

## Source priority (when sources disagree)

1. Answers from the product owner, once received (record them in `product-review-rules.md` with date).
2. User story US-VP02 and its acceptance criteria (`exam/user-story.md`).
3. Mockup (`exam/mockup-1.png`) for labels, fields and layout.
4. `exam/app-note.md` for environment and how the demo build works.
5. The demo build (`exam/app/`) is the product under test. It is never a source of expected results; what it does is only "observed behaviour".

If two sources disagree, do not choose: record the conflict as an Open question and raise it as a Must ask question.

## Labels used in these files

- **Fact**: stated in a source; the source is named.
- **Observed**: seen in the demo build; not a requirement.
- **Assumption**: our working guess until confirmed.
- **Open question**: not stated anywhere; must be asked.

## Maintenance

- Update the "Last updated" line of a file whenever its content changes.
- When an Open question is answered, change it to Fact with the answer source and date, and remove any Assumption it replaces.
- No real personal data, accounts or passwords in this folder.
