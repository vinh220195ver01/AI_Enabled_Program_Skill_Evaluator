# Transcript 03: test-case-generation (run1)

Exported from the agent session log. Kept verbatim: the trainee's messages, the AI's replies, tool calls and tool results. Left out: harness reminders and private thinking. The harness prefix in front of follow-up messages is removed; the AI's final report is shown as an AI reply.

## Trainee (2026-10-21T04:09:59)

hi, now the test cases. pls use my skill evaluator/test-fixtures/manual-qa-sim-pass/submission/skills/test-case-generation/SKILL.md (read and follow it).

inputs:
- TR list: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-requirements.xlsx
- test design: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-design.md
- clarification questions (no PO answers yet): evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/clarification-questions.md
- knowledge folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/knowledge
- output folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1

the build we test is demo-1.0 (see evaluator/test-fixtures/manual-qa-sim-pass/exam/app-note.md), I'll run the TCs manually in Chrome afterwards. only use these files and the exam folder, nothing else under test-fixtures. tell me what you wrote and anything I need to decide.

## AI (2026-10-21T04:10:02)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\skills\\test-case-generation\\SKILL.md"
}
```

## Tool (2026-10-21T04:10:02)

```
1	---
2	name: test-case-generation
3	description: Use when a reviewed Test Requirement Excel list and its approved test design (test conditions with techniques) already exist and manual test cases with steps and expected results must be written from them before test execution; exports test-cases.xlsx. Do NOT use to analyse a raw user story, to choose test techniques or to generate test data sets.
4	---
5	
6	# Test Case Generation
7	
8	Writes manual test cases, one behaviour each, traced to a TR and a test condition, with concrete steps and observable expected results.
9	
10	## Inputs
11	
12	- {tr_file}: the reviewed Test Requirement list (.xlsx). Default: `{output_dir}/test-requirements.xlsx`. If missing, ask the user.
13	- {design_file}: the approved test design (.md with condition IDs). Default: `{output_dir}/test-design.md`. If missing, ask the user; do not design conditions yourself.
14	- {knowledge_dir}: the project's knowledge folder (screens, field labels, messages, glossary, environment). If missing, ask the user.
15	- {output_dir}: the folder where the output file is written. If missing, ask the user.
16	
17	## Process
18	
19	1. Open {tr_file} and {design_file}, and list every TR ID with its condition IDs. Stop and ask the user if a condition points to a TR ID that is not in {tr_file}.
20	2. Read the screen, field and glossary files that the index in {knowledge_dir} lists for test cases, and use their labels and terms exactly.
21	3. Write one test case per test condition with `references/tc-writing-rules.md`: summary, pre-condition, numbered steps with the exact label of each control, and one observable expected result.
22	4. Take every expected result from a source (requirement, answer, knowledge file). Where no source states it, write the expected result as "To be confirmed: ..." and add a Missing info note with the question ID, using the tags in `../test-requirements-analysis/references/note-tags.md`.
23	5. Check traceability and quality: every TR ID and every condition ID has at least one test case, no two test cases verify the same thing, and each case passes the self-check in `references/tc-writing-rules.md`.
24	6. Export by copying `assets/test-case-template.xlsx` to `{output_dir}/test-cases.xlsx` and filling it, sorted by TR ID then TC ID, keeping the sheet name, header row and column widths.
25	7. Report to the user: the number of cases per TR, every "To be confirmed" expected result and every Assumption; then stop, because expected results must be confirmed by a person before execution.
26	
27	## Exceptions
28	
29	- A condition is too vague to write steps for: list it in the report and ask the user; do not invent behaviour.
30	- The design and the TR list disagree (missing TR, different wording of a rule): report the difference and ask which file is correct.
31	- The export fails: show the error, retry once with a corrected path, then stop and ask the user.
32	
33	## Output
34	
35	- `{output_dir}/test-cases.xlsx`: one row per test case, in the layout of `assets/test-case-template.xlsx`.
36	
37	## Files
38	
39	- `references/tc-writing-rules.md`: open at Steps 3 and 5.
40	- `../test-requirements-analysis/references/note-tags.md`: open at Step 4 (shared, single source).
41	- `assets/test-case-template.xlsx`: open at Step 6; copy it, never rebuild it.
42	
```

## AI (2026-10-21T04:10:03)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && find exam submission -type f | head -100",
  "description": "List exam and submission files"
}
```

## Tool (2026-10-21T04:10:05)

```
exam/app/app.js
exam/app/index.html
exam/app/styles.css
exam/app-note.md
exam/mockup-1.png
exam/mockup-2.png
exam/User Story for My Shop.docx
exam/user-story.md
submission/knowledge/environment.md
submission/knowledge/glossary.md
submission/knowledge/index.md
submission/knowledge/product-review-rules.md
submission/knowledge/screens-and-fields.md
submission/review/review-log.md
submission/runs/run-1/ai-original/clarification-questions.md
submission/runs/run-1/ai-original/test-design.md
submission/runs/run-1/ai-original/test-requirements.xlsx
submission/runs/run-1/clarification-questions.md
submission/runs/run-1/test-design.md
submission/runs/run-1/test-requirements.xlsx
submission/skills/defect-analysis-reporting/assets/bug-list-template.xlsx
submission/skills/defect-analysis-reporting/assets/defect-analysis-template.md
submission/skills/defect-analysis-reporting/references/bug-report-rules.md
submission/skills/defect-analysis-reporting/references/severity-priority-guide.md
submission/skills/defect-analysis-reporting/SKILL.md
submission/skills/test-case-generation/assets/test-case-template.xlsx
submission/skills/test-case-generation/references/tc-writing-rules.md
submission/skills/test-case-generation/SKILL.md
submission/skills/test-condition-design/assets/test-design-template.md
submission/skills/test-condition-design/references/coverage-checklist.md
submission/skills/test-condition-design/references/test-design-techniques.md
submission/skills/test-condition-design/SKILL.md
submission/skills/test-data-generation/assets/test-data-template.xlsx
submission/skills/test-data-generation/references/test-data-rules.md
submission/skills/test-data-generation/SKILL.md
submission/skills/test-requirements-analysis/assets/clarification-questions-template.md
submission/skills/test-requirements-analysis/assets/test-requirement-template.xlsx
submission/skills/test-requirements-analysis/references/ambiguity-checklist.md
submission/skills/test-requirements-analysis/references/note-tags.md
submission/skills/test-requirements-analysis/references/tr-writing-rules.md
submission/skills/test-requirements-analysis/SKILL.md
```

## AI (2026-10-21T04:10:08)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && cat submission/skills/test-case-generation/references/tc-writing-rules.md; echo ======; cat submission/skills/test-requirements-analysis/references/note-tags.md; echo ======; cat submission/knowledge/index.md; echo =====; cat exam/app-note.md",
  "description": "Read rules, note tags, knowledge index, app note"
}
```

## Tool (2026-10-21T04:10:10)

```
# Test case writing rules

## IDs

- TC ID: `TC-<TR number>-<nn>`, for example TC-03-01, TC-03-02 for TR-03. Numbers continuous per TR.
- Put the condition ID (TCD-xx-yy) in Notes as `Condition: TCD-xx-yy`.

## Columns

| Column | Rule |
|---|---|
| TR ID | Exactly as in the TR list. |
| TC ID | See IDs. |
| TC Summary | "Verify that ..." + one behaviour + the key condition, max about 15 words. |
| Pre-Condition | The state before step 1: page open, data that must already exist, settings. No actions that belong in the steps. |
| Steps | Numbered `1.` `2.` ... one action per step, naming the control by its exact label. Name the data by Data ID or concrete value (for example "Enter a 3-character value in Name"). |
| Expected Result | What the tester can see or check: the exact message, the element that appears or disappears, the value shown, the state of the record. One outcome per case (it may have several observable parts of that one outcome). |
| Notes | Condition ID, technique, and tagged notes (Assumption, Edge case, Missing info, Risk). |

## Do not write

- Vague results: "works normally", "works as expected", "error is shown", "system handles it correctly".
- Several behaviours in one case (for example valid submit and invalid submit together).
- Expected results copied from what the build currently does; the source is the requirement.

## Self-check per case

1. Can another tester run it without asking anything?
2. Is the expected result pass/fail on its own?
3. Does it trace to one TR and one condition?
4. Are unconfirmed expectations marked "To be confirmed" with a Missing info note?
======
# Note tags

Single source for the tags used in the Notes column of every QA output (TR list, test design, test cases, test data, bug list). Other skills link to this file; do not copy it.

Format: one note per line, `Tag: text`. A row can have several notes or none.

| Tag | Use when | Example |
|---|---|---|
| Assumption | We continue with a value or rule that no source states. Say what was assumed and which question would confirm it. | `Assumption: maximum length taken as N until Q-03 is answered.` |
| Edge case | The row covers a boundary, an unusual but valid input, or a rare sequence of actions. | `Edge case: value exactly at the maximum.` |
| Missing info | The source does not give enough to decide the expected behaviour. Link the question ID. | `Missing info: message text not specified (Q-05).` |
| Risk | Failure here would hurt users, data, privacy, security or the main flow. Say what could go wrong. | `Risk: personal data could be shown publicly.` |

Rules:

- An Assumption is never presented as fact elsewhere in the output.
- When a question is answered, replace the Assumption or Missing info note with the confirmed rule and its source.
======
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
=====
# Application under test: My Shop - Submit a Product Review

This is a small demo build of the "My Shop" product page that implements user story
US-VP02 "Submit a Product Review" (see `user-story.md` and the mockups in this folder).

The page shows one product with its approved customer reviews and an "Add a review"
form (star rating, review comment, name, email). Newly submitted reviews wait for
moderator approval before they are shown. To let you play the moderator, the page has a
"Moderator: approve pending reviews" button at the bottom that approves every review
that is waiting.

## How to open it

1. Open `exam/app/index.html` in Chrome (double-click the file, or drag it into a Chrome window).
2. No installation, server or internet connection is needed.
3. Reload the page to start again from the initial data. Only the "Save my name, email..."
   choice is kept between reloads.

## Environment

| Item    | Value    |
|---------|----------|
| Build   | demo-1.0 |
| Browser | Chrome   |
```

## AI (2026-10-21T04:10:12)

**Tool call `Bash`:**

```json
{
  "command": "cat knowledge/product-review-rules.md; echo =====; cat knowledge/screens-and-fields.md; echo =====; cat knowledge/glossary.md; echo =====; cat knowledge/environment.md",
  "description": "Read knowledge files"
}
```

## AI (2026-10-21T04:10:13)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1 && cat test-design.md; echo =====; cat clarification-questions.md",
  "description": "Read test design and clarification questions"
}
```

## Tool (2026-10-21T04:10:14)

```
<persisted-output>
Output too large (68.3KB). Full output saved to: C:\Users\vinh.the.nguyen\.claude\projects\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\tool-results\bs90bhh6g.txt

Preview (first 2KB):
# Test design: US-VP02 Submit a Product Review

Input: runs/run-1/test-requirements.xlsx (41 TRs, TR-01 to TR-41) · Answers used: none (runs/run-1/clarification-questions.md has questions Q-01 to Q-32, no product owner answers yet) · Date: 2026-10-21

Other sources read: knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md, knowledge/environment.md, exam/user-story.md, exam/mockup-1.png, exam/app-note.md. The demo build (exam/app/) is the product under test and is never used as a source of expected results; its "0 / 500" counter and its message texts are Observed only and are not used as values here.

## Values and rules used

| Item | Value | Status (Confirmed / Assumption) | Source |
|---|---|---|---|
| Form fields | "Your rating *", "Your review *", "Name *", "Email *", save checkbox, "Submit" | Confirmed | mockup-1.png (R1), screens-and-fields.md F1-F6 |
| Required fields | Rating, Review, Name and Email are required (marked *) | Confirmed | mockup-1.png (R2) |
| Info text | "Your email address will not be published. Required fields are marked *" | Confirmed | mockup-1.png |
| Heading | "ADD A REVIEW"; letter case not significant | Assumption | mockup-1.png; Q-32 |
| Number of stars | 5 star icons, none selected when the form opens | Confirmed | mockup-1.png (R6) |
| Rating values | Whole number 1 to 5, one per star; no half stars | Assumption | product-review-rules.md A1; Q-03 |
| Changing the rating | Clicking another star changes the rating; it cannot be cleared to "no rating" except by reloading the page | Assumption | Q-16 |
| "Your review" control | Multi-line text box | Confirmed | mockup-1.png (AC-02, F2) |
| "Your review" minimum and maximum length | Not stated in any source; no value used | Missing info | Q-04 (demo counter "0 / 500" is Observed only) |
| Text longer than the maximum | Typing and pasting stop at the maximum | Assumption | Q-18 |
...
</persisted-output>
```

## Tool (2026-10-21T04:10:15)

```
# Product review rules: US-VP02 Submit a Product Review

Source: `exam/user-story.md` (text of the Word file "User Story for My Shop"), `exam/mockup-1.png`, `exam/app-note.md`
Last updated: 2026-10-21

## User story (Fact, word for word)

- Application: My Shop
- ID and title: US-VP02 Submit a Product Review
- Story: As a customer, I want to submit a review for a product I purchased, so that I can share my experience with others.

## Acceptance criteria (Fact, word for word)

| AC ID | Acceptance criterion |
|---|---|
| AC-01 | Allow customers to enter a star rating |
| AC-02 | Provide a text box for review comments |
| AC-03 | Display approved reviews on the product page |

## Confirmed rules

| # | Rule | Label | Source |
|---|---|---|---|
| R1 | The review form has a star rating, a review text box, Name and Email. | Fact | mockup-1.png |
| R2 | Rating, Review, Name and Email are marked required (*). | Fact | mockup-1.png |
| R3 | The email address is not published. | Fact | mockup-1.png ("Your email address will not be published.") |
| R4 | Only approved reviews are displayed on the product page. | Fact | AC-03 |
| R5 | A newly submitted review waits for moderator approval before it is shown. | Fact (derived) | AC-03: only approved reviews are displayed |
| R6 | The star rating shows 5 stars. | Fact | mockup-1.png |

## Assumptions (working guesses, to be confirmed)

| # | Assumption | Related open question |
|---|---|---|
| A1 | The rating is a whole number from 1 to 5 (one per star). | OQ2 |
| A2 | A submitted review is shown with its rating, the reviewer's name, the date and the comment, and never the email. | OQ7 |

## Open questions (not stated in any source)

| # | Question area | Detail |
|---|---|---|
| OQ1 | Purchase check | The story says "a product I purchased". Must the system check the purchase? Can a non-buyer or a guest submit? Must the customer be signed in? |
| OQ2 | Rating values | Whole stars only or half stars? Is 0 / no rating allowed? |
| OQ3 | Review length | Minimum and maximum length of the review text. The demo build shows a "0 / 500" counter (Observed), but the story gives no limit. |
| OQ4 | Name and Email rules | Length limits, allowed characters, email format rule. |
| OQ5 | Messages | Wording and position of validation and success messages. |
| OQ6 | Moderation | Who approves, how, can a review be rejected, is the author told the result? What does the author see while the review is pending? |
| OQ7 | Display | Which details are shown per review (name or something else), date format, order, paging, what is shown when there are no reviews. |
| OQ8 | Rating summary | Does the product page show an average rating and review count, and is it based on approved reviews only? |
| OQ9 | Multiple reviews | Can one customer review the same product more than once? Edit or delete own review? |
| OQ10 | "Save my name, email, and website" | The checkbox mentions "website" but the mockup has no Website field. What is saved, where, and for how long? |
| OQ11 | Content rules | Are profanity, links or HTML in reviews filtered or blocked? |
| OQ12 | Scope | Supported browsers and devices beyond Chrome. |
=====
# Screens and fields: product page and "Add a review" form

Source: `exam/mockup-1.png` (form), `exam/mockup-2.png` (company logo only, no screen content), demo build `exam/app/index.html` (observed)
Last updated: 2026-10-21

Labels are written exactly as displayed. Use them in test steps.

## Product page (Observed in demo build; no mockup of this page exists)

| Section | What is displayed |
|---|---|
| Header | Shop logo text and navigation links (Home, Men, Women, Cart (0)) |
| Product | Product image area, product name, rating summary (stars + text), price, description |
| Reviews | Heading "Reviews (n)", list of reviews (stars, author, date, review text), and "There are no reviews yet." when the list is empty |
| Add a review | The form below |
| Moderator | Demo-only helper: "Pending approval: n" and button "Moderator: approve pending reviews" (see `environment.md`) |
| Footer | Copyright and build label |

Open question: the expected content and order of the Reviews section and the rating summary are not specified (see `product-review-rules.md` OQ7, OQ8).

## "Add a review" form

| # | Label (as shown) | Control | Required | Source | Notes |
|---|---|---|---|---|---|
| F0 | "Your email address will not be published. Required fields are marked *" | Info text | - | mockup-1 | Mockup heading is "ADD A REVIEW" (upper case); the build shows "Add a review" (Observed). Open question whether the case matters. |
| F1 | Your rating * | 5 star icons, click to select | Yes | mockup-1 | Build also shows the selected value as text, e.g. "3 stars" (Observed) |
| F2 | Your review * | Multi-line text box | Yes | mockup-1 | Build shows a character counter "n / 500" (Observed). Limit not in the story: Open question OQ3 |
| F3 | Name * | Single-line text box | Yes | mockup-1 | Rules: Open question OQ4 |
| F4 | Email * | Single-line text box | Yes | mockup-1 | Not published (R3). Format rule: Open question OQ4 |
| F5 | Save my name, email, and website in this browser for the next time I comment. | Checkbox, unchecked by default | No | mockup-1 | No Website field exists: Open question OQ10 |
| F6 | Submit | Button | - | mockup-1 | |

## Feedback areas (Observed in demo build)

- An error box appears above the form after a rejected submit.
- A success box appears above the form after an accepted submit.
- Expected wording of both: Open question OQ5.
=====
# Glossary: My Shop product reviews

Source: `exam/user-story.md`, `exam/mockup-1.png`, `exam/app-note.md`
Last updated: 2026-10-21

| Term | Meaning in this project | Label |
|---|---|---|
| Customer | A shopper of My Shop who writes a review. Whether they must be signed in or must have purchased the product is not stated. | Fact (user story) + Open question OQ1 |
| Product page | The page of one product, showing its details and its approved reviews. | Fact (AC-03) |
| Review | A customer's star rating plus review comment for one product, with name and email. | Fact (mockup-1) |
| Star rating | The score given by clicking one of 5 stars. | Fact (AC-01, mockup-1) |
| Review comment | The free text written in "Your review". | Fact (AC-02, mockup-1) |
| Pending review | A submitted review waiting for moderator approval; not shown on the product page. | Fact (app-note.md) |
| Approved review | A review accepted by a moderator; shown on the product page. | Fact (AC-03, app-note.md) |
| Moderator | The person who approves reviews. In the demo build this role is simulated with the "Moderator: approve pending reviews" button. Real moderation process is not described. | Fact (app-note.md) + Open question OQ6 |
| Rating summary | The stars and text near the product name. Its calculation is not specified. | Observed + Open question OQ8 |
| Build | The version label of the application under test. | Fact (app-note.md) |
=====
# Test environment: My Shop demo build

Source: `exam/app-note.md`
Last updated: 2026-10-21

## Environment (Fact)

| Item | Value |
|---|---|
| Build | demo-1.0 |
| Browser | Chrome |

Only these two items are given. Browser version, operating system and screen size are not provided: write "Not provided" in reports; do not guess.

## How to open the application (Fact)

1. Open `exam/app/index.html` in Chrome (double-click it or drag it into a Chrome window).
2. No installation, server or internet connection is needed.
3. Reload the page to start again from the initial data. Only the "Save my name, email..." choice is kept between reloads.

## Test helper (Fact)

- New reviews wait for moderator approval. The button "Moderator: approve pending reviews" at the bottom of the page approves every waiting review, so the tester can play the moderator.
- This helper is part of the demo build only. Assumption: it is not part of the feature under test; it is used only to move reviews to "approved".

## Test accounts and data

- No accounts are needed (no sign-in in the demo build, Observed).
- Use synthetic data only (reserved email domains such as example.com).
```

## AI (2026-10-21T04:10:17)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\runs\\run-1\\test-design.md"
}
```

## Tool (2026-10-21T04:10:17)

```
1	# Test design: US-VP02 Submit a Product Review
2	
3	Input: runs/run-1/test-requirements.xlsx (41 TRs, TR-01 to TR-41) · Answers used: none (runs/run-1/clarification-questions.md has questions Q-01 to Q-32, no product owner answers yet) · Date: 2026-10-21
4	
5	Other sources read: knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md, knowledge/environment.md, exam/user-story.md, exam/mockup-1.png, exam/app-note.md. The demo build (exam/app/) is the product under test and is never used as a source of expected results; its "0 / 500" counter and its message texts are Observed only and are not used as values here.
6	
7	## Values and rules used
8	
9	| Item | Value | Status (Confirmed / Assumption) | Source |
10	|---|---|---|---|
11	| Form fields | "Your rating *", "Your review *", "Name *", "Email *", save checkbox, "Submit" | Confirmed | mockup-1.png (R1), screens-and-fields.md F1-F6 |
12	| Required fields | Rating, Review, Name and Email are required (marked *) | Confirmed | mockup-1.png (R2) |
13	| Info text | "Your email address will not be published. Required fields are marked *" | Confirmed | mockup-1.png |
14	| Heading | "ADD A REVIEW"; letter case not significant | Assumption | mockup-1.png; Q-32 |
15	| Number of stars | 5 star icons, none selected when the form opens | Confirmed | mockup-1.png (R6) |
16	| Rating values | Whole number 1 to 5, one per star; no half stars | Assumption | product-review-rules.md A1; Q-03 |
17	| Changing the rating | Clicking another star changes the rating; it cannot be cleared to "no rating" except by reloading the page | Assumption | Q-16 |
18	| "Your review" control | Multi-line text box | Confirmed | mockup-1.png (AC-02, F2) |
19	| "Your review" minimum and maximum length | Not stated in any source; no value used | Missing info | Q-04 (demo counter "0 / 500" is Observed only) |
20	| Text longer than the maximum | Typing and pasting stop at the maximum | Assumption | Q-18 |
21	| Leading / trailing spaces | Trimmed in Review, Name and Email; a field of only spaces counts as empty | Assumption | Q-17 |
22	| Name length and allowed characters | Not stated; no value used | Missing info | Q-05 |
23	| Email format rule and maximum length | Standard format text@domain.tld taken as the working rule; maximum length not stated | Assumption (format), Missing info (length) | Q-06 |
24	| Email not published | The email is never shown on the product page | Confirmed | mockup-1.png (R3) |
25	| HTML, scripts and links in text | Shown as plain text, removed or rejected: not stated. Never executed in any case | Missing info (handling), Assumption (never executed) | Q-15 |
26	| Validation timing | Fields are checked on Submit only | Assumption | Q-19 |
27	| Error messages | Each error names the field concerned; wording checked for meaning, not exact text | Assumption | Q-20 |
28	| Success message | Says the review was received and waits for approval | Assumption | Q-21 |
29	| Form after success | Customer stays on the product page; form cleared; Name and Email stay only if the save checkbox was ticked | Assumption | Q-22 |
30	| Review states | Submitted review is Pending; only Approved reviews are displayed | Confirmed | AC-03 (R4, R5), app-note.md |
31	| Moderation (who approves, reject, what happens to a rejected review) | Not stated | Missing info | Q-07 |
32	| Moderator in demo-1.0 | "Moderator: approve pending reviews" approves every pending review; used only as a test helper | Confirmed (helper), Assumption (not part of the feature) | environment.md, app-note.md |
33	| Author's view of own pending review | Not stated | Missing info | Q-08 |
34	| Details per displayed review | Star rating, reviewer name, date, review text; never the email | Assumption | product-review-rules.md A2; Q-09 |
35	| Date shown | Submit date, any unambiguous format | Assumption | Q-24 |
36	| Order of reviews | Not stated | Missing info | Q-10 |
37	| Paging | All approved reviews shown on one page | Assumption | Q-23 |
38	| No approved reviews | A short message saying there are no reviews yet | Assumption | Q-25 |
39	| Rating summary and count | Whether shown and how rounded: not stated; if shown, approved reviews only | Missing info | Q-11 |
40	| Who may review | Sign-in and purchase check not stated | Missing info | Q-01 |
41	| Name / Email for a signed-in customer | Story vs mockup-1 conflict | Missing info | Q-02 |
42	| Reviews per customer and product | Not stated | Missing info | Q-12 |
43	| Save checkbox default | Unchecked | Confirmed | mockup-1.png (F5) |
44	| Save checkbox stores | Name and Email only, in this browser | Assumption | Q-13, Q-14 |
45	| What is kept when the checkbox is not ticked, how long data is kept, how it is removed | Not stated | Missing info | Q-14 |
46	| Double submit | Only one review is created | Assumption | Q-28 |
47	| Server / network error | A message says the review was not submitted; the entered data is kept | Assumption | Q-29 |
48	| Browser and environment | Build demo-1.0, Chrome; other browsers and devices not stated | Confirmed (Chrome), Assumption (desktop Chrome, English) | environment.md, app-note.md; Q-31 |
49	| Demo-1.0 data | One product; reload restores the initial data; no sign-in | Confirmed | app-note.md, environment.md |
50	
51	## Test conditions
52	
53	### TR-01: Verify that the "Your rating *" field shows 5 stars.
54	
55	Technique(s): Equivalence Partitioning - the rating control has one valid display state (as in mockup-1); one condition covers it.
56	
57	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
58	|---|---|---|---|---|
59	| TCD-01-01 | EP | When the form opens, "Your rating *" shows exactly 5 star icons and none of them is selected. | Positive | |
60	
61	### TR-02: Verify that the customer can select a rating by clicking a star, and the selected stars are shown as selected.
62	
63	Technique(s): Equivalence Partitioning - whole-star values 1 to 5 form one valid partition (a middle value represents it; the ends are in TR-03) and half-star values form one invalid partition. Error guessing - hover and keyboard use are common sources of rating defects.
64	
65	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
66	|---|---|---|---|---|
67	| TCD-02-01 | EP | From no rating, clicking the 3rd star selects rating 3: stars 1 to 3 are shown as selected and stars 4 and 5 as not selected. | Positive | Assumption: the rating is a whole number from 1 to 5 until Q-03 is answered. |
68	| TCD-02-02 | EP | Clicking on the left half of a star does not set a half-star value (for example 2.5); the rating shown and saved is a whole number. | Negative | Missing info: whether half stars are allowed (Q-03). |
69	| TCD-02-03 | Error guessing | Moving the pointer over the stars without clicking, then moving it away, leaves the selected rating unchanged. | Negative | Assumption: a hover preview, if any, is not kept until Q-36 is answered. |
70	| TCD-02-04 | Error guessing | The rating can be selected with the keyboard only (Tab to the stars, then arrow keys, Space or Enter), and the selection is shown. | Positive | Missing info: keyboard use is not stated in any source (Q-34). |
71	
72	### TR-03: Verify that both the lowest rating (1 star) and the highest rating (5 stars) can be selected and are saved with the review.
73	
74	Technique(s): Boundary Value Analysis - the rating is a range 1 to 5 (Assumption). Just below the minimum (0 = no rating) is TCD-05-01; just above the maximum (6) cannot be entered because only 5 stars exist (TCD-01-01), so no separate condition.
75	
76	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
77	|---|---|---|---|---|
78	| TCD-03-01 | BVA | Rating 1 (on the minimum): the review is submitted and, after approval, is shown with 1 star. | Positive | Edge case: value exactly at the minimum.<br>Assumption: rating range 1 to 5 until Q-03 is answered. |
79	| TCD-03-02 | BVA | Rating 2 (just above the minimum): the review is submitted and, after approval, is shown with 2 stars. | Positive | Assumption: rating range 1 to 5 until Q-03 is answered. |
80	| TCD-03-03 | BVA | Rating 4 (just below the maximum): the review is submitted and, after approval, is shown with 4 stars. | Positive | Assumption: rating range 1 to 5 until Q-03 is answered. |
81	| TCD-03-04 | BVA | Rating 5 (on the maximum): the review is submitted and, after approval, is shown with 5 stars. | Positive | Edge case: value exactly at the maximum.<br>Assumption: rating range 1 to 5 until Q-03 is answered. |
82	
83	### TR-04: Verify that the customer can change the selected rating before submitting, and only the last selected rating is saved.
84	
85	Technique(s): State transition - states "No rating" and "Rating n"; events "click star m", "click the selected star again", "reload page", "Submit". Each valid transition once, plus the transition that is not allowed (clearing to "No rating" by clicking).
86	
87	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
88	|---|---|---|---|---|
89	| TCD-04-01 | State transition | Rating 2, click the 5th star: the rating becomes 5 and stars 1 to 5 are shown as selected (increase). | Positive | Assumption: clicking another star changes the rating (Q-16). |
90	| TCD-04-02 | State transition | Rating 5, click the 2nd star: the rating becomes 2 and only stars 1 and 2 are shown as selected (decrease). | Positive | Assumption: clicking another star changes the rating (Q-16). |
91	| TCD-04-03 | State transition | Rating 3, click the 3rd star again: the rating stays 3; it does not go back to "No rating". | Negative | Assumption: the rating cannot be cleared by clicking (Q-16). |
92	| TCD-04-04 | State transition | Rating 3, reload the page: the form opens with "No rating". | Positive | Assumption: reloading is the only way back to "No rating" (Q-16). |
93	| TCD-04-05 | State transition | Rating changed several times (1, then 4, then 2, then 3) and then Submit: the saved and, after approval, displayed rating is 3. | Positive | |
94	
95	### TR-05: Verify that the review cannot be submitted when no star rating is selected.
96	
97	Technique(s): Equivalence Partitioning (invalid partition "no rating") with Boundary Value Analysis (0 is just below the minimum 1).
98	
99	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
100	|---|---|---|---|---|
101	| TCD-05-01 | EP / BVA | No star selected (0, just below the minimum), Review, Name and Email valid, Submit: the review is not submitted and an error names the rating field. | Negative | Edge case: just below the minimum.<br>Assumption: the error names the rating field; wording checked for meaning, not exact text (Q-20). |
102	
103	### TR-06: Verify that a multi-line text box "Your review *" is provided for the review comment.
104	
105	Technique(s): Equivalence Partitioning - multi-line input is one valid partition. Error guessing - line breaks are often lost when the text is displayed.
106	
107	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
108	|---|---|---|---|---|
109	| TCD-06-01 | EP | "Your review *" accepts text on several lines: pressing Enter starts a new line inside the box and does not submit the form. | Positive | |
110	| TCD-06-02 | Error guessing | A review written on several lines is shown on the product page, after approval, with its line breaks kept. | Positive | Missing info: display of line breaks is not stated in any source (Q-35). |
111	
112	### TR-07: Verify that the review cannot be submitted when "Your review" is empty.
113	
114	Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field (0 characters).
115	
116	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
117	|---|---|---|---|---|
118	| TCD-07-01 | EP | "Your review" empty (0 characters), rating, Name and Email valid, Submit: the review is not submitted and an error names "Your review". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |
119	
120	### TR-08: Verify that review text within the allowed length is accepted and saved as entered.
121	
122	Technique(s): Equivalence Partitioning - one valid length partition (between the minimum and the maximum) and valid character types. Error guessing - pasted text and non-Latin characters are frequent defect sources.
123	
124	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
125	|---|---|---|---|---|
126	| TCD-08-01 | EP | Review text with a length between the minimum and the maximum: the review is submitted and, after approval, the text is shown exactly as entered. | Positive | Missing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered. |
127	| TCD-08-02 | Error guessing | Review text with accented letters (é, ü), non-Latin letters (日本語), digits, punctuation and an emoji: accepted and shown unchanged. | Positive | Assumption: no character restriction in "Your review" until Q-37 is answered. |
128	| TCD-08-03 | Error guessing | Review text pasted from the clipboard is accepted and saved in the same way as typed text. | Positive | |
129	
130	### TR-09: Verify that review text of exactly the minimum length and exactly the maximum length is accepted.
131	
132	Technique(s): Boundary Value Analysis - the review has a length range (minimum and maximum). Values on and just inside each boundary are here; just outside are in TR-10. The exact numbers are not in any source.
133	
134	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
135	|---|---|---|---|---|
136	| TCD-09-01 | BVA | Review length = minimum: accepted. | Positive | Edge case: value exactly at the minimum.<br>Missing info: minimum length not stated (Q-04). |
137	| TCD-09-02 | BVA | Review length = minimum + 1: accepted. | Positive | Missing info: minimum length not stated (Q-04). |
138	| TCD-09-03 | BVA | Review length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-04). |
139	| TCD-09-04 | BVA | Review length = maximum: accepted and, after approval, shown in full (not cut). | Positive | Edge case: value exactly at the maximum.<br>Missing info: maximum length not stated (Q-04). |
140	
141	### TR-10: Verify that review text shorter than the minimum or longer than the maximum is not accepted.
142	
143	Technique(s): Boundary Value Analysis - values just outside each boundary, one invalid value per condition. Error guessing - very long pasted text.
144	
145	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
146	|---|---|---|---|---|
147	| TCD-10-01 | BVA | Review length = minimum - 1, Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: one character below the minimum.<br>Missing info: minimum length not stated (Q-04). If the minimum is 1, this is TCD-07-01 and is not repeated. |
148	| TCD-10-02 | BVA | Typing maximum + 1 characters: typing stops at the maximum and the box holds exactly maximum characters. | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: typing stops at the maximum (Q-18). |
149	| TCD-10-03 | BVA | Pasting text of maximum + 1 characters: the text in the box is cut at the maximum. | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |
150	| TCD-10-04 | Error guessing | Pasting very long text (about ten times the maximum): the box holds at most the maximum and the page stays responsive. | Negative | Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |
151	
152	### TR-11: Verify that review text made only of spaces is treated as empty and the review is not submitted.
153	
154	Technique(s): Error guessing - spaces-only and space-padded input; Boundary Value Analysis - trimmed length just below the minimum.
155	
156	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
157	|---|---|---|---|---|
158	| TCD-11-01 | Error guessing | "Your review" contains only spaces, Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
159	| TCD-11-02 | Error guessing | "Your review" contains only line breaks (Enter pressed several times), Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: line breaks are treated like spaces (Q-17). |
160	| TCD-11-03 | Error guessing | Valid review text with leading and trailing spaces: accepted and, after approval, shown without the leading and trailing spaces. | Positive | Assumption: spaces are trimmed (Q-17). |
161	| TCD-11-04 | BVA | Review of (minimum - 1) visible characters plus one trailing space (length = minimum only if the space is counted), Submit: the review is not submitted. | Negative | Edge case: length reaches the minimum only through a space.<br>Assumption: length is counted after trimming (Q-17).<br>Missing info: minimum length not stated (Q-04). |
162	
163	### TR-12: Verify that HTML tags, script code and links entered in "Your review" or "Name" are never run as code on the product page.
164	
165	Technique(s): Error guessing - script injection through free text is a known high-risk defect; each field and each injection form is tested separately so the result shows which one failed.
166	
167	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
168	|---|---|---|---|---|
169	| TCD-12-01 | Error guessing | "Your review" contains `<script>alert(1)</script>`: no script runs, on submit or on the product page after approval. | Negative | Missing info: shown as plain text, removed or rejected (Q-15).<br>Assumption: content is never executed (Q-15).<br>Risk: script injection would affect every visitor of the product page. |
170	| TCD-12-02 | Error guessing | "Your review" contains `<img src=x onerror=alert(1)>`: no script runs and no image element is added to the page. | Negative | Missing info: handling not stated (Q-15).<br>Risk: script injection through an HTML attribute. |
171	| TCD-12-03 | Error guessing | "Your review" contains harmless HTML `<b>bold</b>`: the text is not rendered as bold HTML; it is shown as plain text, removed or rejected as confirmed for Q-15. | Negative | Missing info: handling not stated (Q-15). |
172	| TCD-12-04 | Error guessing | "Your review" contains a web link (`https://example.com`): it is shown, removed or rejected as confirmed for Q-15, and is not turned into a clickable link unless Q-15 allows it. | Negative | Missing info: handling of links not stated (Q-15). |
173	| TCD-12-05 | Error guessing | "Name" contains `<script>alert(1)</script>`: no script runs where the name is shown. | Negative | Missing info: handling not stated (Q-05, Q-15).<br>Risk: script injection through the reviewer name. |
174	
175	### TR-13: Verify that a newly submitted review is not displayed on the product page while it waits for approval.
176	
177	Technique(s): State transition - Submit moves a review from "not existing" to "Pending"; in "Pending" the review must not be displayed to other visitors. (The author's own view is TR-16.)
178	
179	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
180	|---|---|---|---|---|
181	| TCD-13-01 | State transition | After a valid Submit (state Pending), the review does not appear in the reviews list for another visitor of the product page. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: demo-1.0 has no sign-in and keeps data only in the open page, so "another visitor" cannot be simulated there (environment.md); check in the author's page per TCD-16-01. |
182	| TCD-13-02 | State transition | A pending review is still not displayed after the product page is opened again later. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: in demo-1.0 a reload restores the initial data (environment.md), so this needs a build that keeps data. |
183	
184	### TR-14: Verify that a submitted review is displayed on the product page after it is approved.
185	
186	Technique(s): State transition - event "approve" moves Pending to Approved (valid transition); approving again or with nothing pending must not create entries (invalid transitions).
187	
188	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
189	|---|---|---|---|---|
190	| TCD-14-01 | State transition | Pending review, moderator approves: the review appears in the reviews list on the product page. | Positive | Missing info: who approves and how (Q-07).<br>Assumption: in demo-1.0 the "Moderator: approve pending reviews" helper plays the moderator (environment.md). |
191	| TCD-14-02 | State transition | Approved review, approve action used again: the review is shown once only (no duplicate). | Negative | Edge case: approve twice.<br>Missing info: moderation workflow (Q-07). |
192	| TCD-14-03 | State transition | No pending review, approve action used: no new or empty review appears. | Negative | Edge case: approve with nothing pending.<br>Missing info: moderation workflow (Q-07). |
193	
194	### TR-15: Verify that a rejected review is never displayed on the product page.
195	
196	Technique(s): State transition - event "reject" moves Pending to Rejected; Rejected must never lead to "displayed" through other events.
197	
198	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
199	|---|---|---|---|---|
200	| TCD-15-01 | State transition | Pending review, moderator rejects: the review does not appear on the product page. | Positive | Missing info: whether a review can be rejected and what happens to it (Q-07). Demo-1.0 has no reject action (environment.md). |
201	| TCD-15-02 | State transition | Rejected review, then other pending reviews are approved: the rejected review is still not displayed. | Negative | Missing info: moderation workflow (Q-07).<br>Risk: rejected content shown publicly. |
202	
203	### TR-16: Verify that the author sees their own pending review only in the way confirmed for Q-08 (marked as awaiting approval, or not at all).
204	
205	Technique(s): Decision table - conditions "viewer = author / other visitor" and "state = Pending / Approved". Rule other + Pending is TCD-13-01; rule other + Approved is TCD-14-01; the two author rules are below.
206	
207	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
208	|---|---|---|---|---|
209	| TCD-16-01 | Decision table | Rule: viewer = author, state = Pending: the author sees the review marked as awaiting approval, or does not see it, as confirmed for Q-08. | Positive | Missing info: author's view of a pending review not specified (Q-08). |
210	| TCD-16-02 | Decision table | Rule: viewer = author, state = Approved: the author sees the review like any other approved review, with no "awaiting approval" mark. | Positive | Missing info: whether a pending mark exists (Q-08). |
211	
212	### TR-17: Verify that each displayed review shows the confirmed details (star rating, reviewer name, date, review text).
213	
214	Technique(s): Equivalence Partitioning - every approved review belongs to one partition and must show the same set of details; one condition per detail group whose rule differs.
215	
216	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
217	|---|---|---|---|---|
218	| TCD-17-01 | EP | Each approved review shows its star rating, reviewer name, date and review text. | Positive | Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered. |
219	| TCD-17-02 | EP | The date shown with a review is the submit date, in an unambiguous format. | Positive | Assumption: submit date in any unambiguous format (Q-24). |
220	| TCD-17-03 | EP | The reviewer name is shown in the confirmed form (full name, first name only or initials). | Positive | Missing info: form of the name not specified (Q-09).<br>Risk: privacy of the reviewer's name. |
221	
222	### TR-18: Verify that the star rating, name and review text of a displayed review match what the customer submitted.
223	
224	Technique(s): Equivalence Partitioning - several reviews with different values must keep their own values. Error guessing - special characters are often encoded wrongly and long words often break the layout.
225	
226	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
227	|---|---|---|---|---|
228	| TCD-18-01 | EP | Two reviews submitted one after the other with different rating, name and text: after approval each shows its own rating, name and text (no mix-up). | Positive | |
229	| TCD-18-02 | Error guessing | Name with accented letter, apostrophe and hyphen (for example "Zoë O'Brien-Lê"): shown exactly as entered, with no encoded characters such as `&#39;`. | Positive | Assumption: such names are accepted until Q-05 is answered. |
230	| TCD-18-03 | Error guessing | Review text with the characters `& < > " '` used as plain text (for example "5 > 3 & good"): shown exactly as entered, not as `&amp;` or `&gt;`. | Positive | Missing info: handling of HTML-like text (Q-15). |
231	| TCD-18-04 | Error guessing | Review of maximum length made of one long word with no spaces: shown in full without breaking the page layout. | Positive | Missing info: maximum length not stated (Q-04). |
232	
233	### TR-19: Verify that the reviewer's email address is never displayed on the product page.
234	
235	Technique(s): Error guessing - personal data often leaks through hidden places (tooltips, links, page source) as well as visible text.
236	
237	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
238	|---|---|---|---|---|
239	| TCD-19-01 | Error guessing | After approval, the email entered does not appear anywhere in the visible product page (reviews list, reviewer name, rating summary). | Positive | Risk: personal data could be shown publicly. |
240	| TCD-19-02 | Error guessing | After approval, the email is not in hidden parts of the review: no tooltip, no "mailto" link on the name, not in the page source of the review. | Positive | Risk: personal data could be read by anyone viewing the page source. |
241	
242	### TR-20: Verify that approved reviews are listed in the confirmed order.
243	
244	Technique(s): Equivalence Partitioning - one partition "list of approved reviews with different dates and ratings". Error guessing - newly approved reviews and ties are common ordering defects.
245	
246	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
247	|---|---|---|---|---|
248	| TCD-20-01 | EP | At least 3 approved reviews with different dates and ratings are listed in the confirmed order. | Positive | Missing info: list order not specified (Q-10). |
249	| TCD-20-02 | Error guessing | A review approved after the existing ones appears in the position the confirmed order requires. | Positive | Missing info: list order not specified (Q-10). |
250	| TCD-20-03 | Error guessing | Two approved reviews with the same date and the same rating keep a stable order when the page is opened again. | Positive | Edge case: tie in the sort key.<br>Missing info: list order not specified (Q-10). |
251	
252	### TR-21: Verify that all approved reviews can be seen when a product has many reviews.
253	
254	Technique(s): Equivalence Partitioning - "many reviews" partition. Boundary Value Analysis - page size, only if paging is confirmed.
255	
256	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
257	|---|---|---|---|---|
258	| TCD-21-01 | EP | Product with a large number of approved reviews (for example 50): every approved review can be seen. | Positive | Edge case: large number of approved reviews.<br>Assumption: all approved reviews are shown on one page (Q-23). |
259	| TCD-21-02 | BVA | Approved reviews = page size - 1: all are on the first page and no paging control is shown. | Positive | Missing info: whether paging exists and the page size (Q-23). |
260	| TCD-21-03 | BVA | Approved reviews = page size: all are on the first page and no paging control is shown. | Positive | Edge case: count exactly at the page size.<br>Missing info: page size (Q-23). |
261	| TCD-21-04 | BVA | Approved reviews = page size + 1: the last review is reachable through the paging control or "Load more". | Positive | Edge case: one above the page size.<br>Missing info: page size (Q-23). |
262	
263	### TR-22: Verify that a clear empty state is shown when the product has no approved reviews.
264	
265	Technique(s): Boundary Value Analysis - approved review count 0 and the move from 0 to 1; Equivalence Partitioning - "only pending reviews" is part of the 0-approved partition.
266	
267	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
268	|---|---|---|---|---|
269	| TCD-22-01 | BVA | 0 approved reviews: a short message says there are no reviews yet. | Positive | Edge case: product with no approved reviews.<br>Assumption: a short message saying there are no reviews yet (Q-25).<br>Missing info: demo-1.0 has one product that starts with approved reviews (app-note.md); a product with 0 approved reviews may not be available. |
270	| TCD-22-02 | EP | 0 approved reviews and 1 or more pending reviews: the empty-state message is still shown. | Positive | Edge case: only pending reviews.<br>Assumption: empty-state message (Q-25). |
271	| TCD-22-03 | BVA | From 0 to 1 approved review: the empty-state message disappears and the review is shown. | Positive | Assumption: empty-state message (Q-25). |
272	
273	### TR-23: Verify that the average rating and review count on the product page, if shown, are calculated from approved reviews only.
274	
275	Technique(s): Decision table - condition "state of the new review = Approved / Pending / Rejected", outcome "included in average and count: yes / no". Boundary Value Analysis - rounding boundary and zero reviews.
276	
277	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
278	|---|---|---|---|---|
279	| TCD-23-01 | Decision table | Rule: new review Approved: the average rating and the review count include it. | Positive | Missing info: whether a summary is shown and how it is rounded (Q-11). |
280	| TCD-23-02 | Decision table | Rule: new review Pending: the average rating and the review count do not change. | Positive | Missing info: Q-11.<br>Risk: pending reviews could change the score shown to shoppers. |
281	| TCD-23-03 | Decision table | Rule: new review Rejected: the average rating and the review count do not change. | Positive | Missing info: Q-07, Q-11.<br>Risk: rejected reviews could change the score shown to shoppers. |
282	| TCD-23-04 | EP | The review count shown equals the number of approved reviews listed. | Positive | Missing info: whether a count is shown (Q-11). |
283	| TCD-23-05 | BVA | Ratings whose exact average falls on and next to the rounding step (for example 4 and 5 = 4.5; 4, 4 and 5 = 4.33...) are shown with the confirmed rounding. | Positive | Missing info: rounding rule not stated (Q-11); exact boundary values are set when Q-11 is answered. |
284	| TCD-23-06 | Error guessing | 0 approved reviews: the summary shows no average, or an empty state, and never a wrong value such as "NaN" or "0 stars". | Negative | Edge case: no approved reviews.<br>Missing info: Q-11, Q-25. |
285	
286	### TR-24: Verify that a review is displayed only on the page of the product it was written for.
287	
288	Technique(s): Equivalence Partitioning - partitions "page of the reviewed product" and "page of another product".
289	
290	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
291	|---|---|---|---|---|
292	| TCD-24-01 | EP | A review written and approved for product A appears on the page of product A. | Positive | Covered in demo-1.0 by TCD-14-01 (one product only). |
293	| TCD-24-02 | EP | The same review does not appear on the page of product B. | Negative | Risk: reviews shown on the wrong product mislead shoppers.<br>Missing info: demo-1.0 has one product only (app-note.md); needs a build with two products. |
294	
295	### TR-25: Verify that the review form shows the heading, the info text, the fields, the save checkbox and the "Submit" button as in mockup-1.
296	
297	Technique(s): Equivalence Partitioning - the form has one valid display state (mockup-1); one condition per element group. Error guessing - focus order and keyboard use.
298	
299	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
300	|---|---|---|---|---|
301	| TCD-25-01 | EP | The heading reads "ADD A REVIEW". | Positive | Assumption: compared without regard to letter case (Q-32). |
302	| TCD-25-02 | EP | The info text reads "Your email address will not be published. Required fields are marked *". | Positive | |
303	| TCD-25-03 | EP | The labels "Your rating *", "Your review *", "Name *" and "Email *" are shown, each with the required marker *. | Positive | |
304	| TCD-25-04 | EP | The save checkbox reads "Save my name, email, and website in this browser for the next time I comment." | Positive | Missing info: final text of the save checkbox (Q-13). |
305	| TCD-25-05 | EP | A "Submit" button is shown below the save checkbox. | Positive | |
306	| TCD-25-06 | EP | The elements are in the mockup-1 order from top to bottom: heading, info text, rating, review, Name, Email, save checkbox, Submit. | Positive | |
307	| TCD-25-07 | Error guessing | Tab moves the focus through the form in the order shown, and Submit can be used with the keyboard. | Positive | Missing info: keyboard use is not stated in any source (Q-34). |
308	
309	### TR-26: Verify that only a customer who is allowed to review (as confirmed for Q-01) can submit a review, and a customer who is not allowed cannot.
310	
311	Technique(s): Decision table - conditions "signed in: yes / no" and "bought this product: yes / no"; outcome "may submit". The two "not signed in" rules are collapsed into one because the purchase cannot be linked to a guest without sign-in until Q-01 says otherwise. Error guessing - cancelled orders.
312	
313	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
314	|---|---|---|---|---|
315	| TCD-26-01 | Decision table | Rule: signed in and bought the product: the customer can submit a review. | Positive | Missing info: sign-in and purchase check not specified (Q-01).<br>Missing info: demo-1.0 has no sign-in (environment.md). |
316	| TCD-26-02 | Decision table | Rule: signed in and did not buy the product: the form is hidden, disabled or rejected on Submit with a message, as confirmed for Q-01. | Negative | Missing info: Q-01.<br>Risk: non-buyers could post fake reviews. |
317	| TCD-26-03 | Decision table | Rule: not signed in (guest): the form is hidden, disabled or rejected on Submit with a message, as confirmed for Q-01. | Negative | Missing info: Q-01.<br>Risk: guests could post fake reviews. |
318	| TCD-26-04 | Error guessing | Signed in, the order of this product was cancelled or refunded: the customer may or may not review, as confirmed for Q-01. | Negative | Edge case: cancelled or refunded purchase.<br>Missing info: cancelled or refunded purchase not specified (Q-33). |
319	
320	### TR-27: Verify that Name and Email for a signed-in customer are handled as confirmed for Q-02 (prefilled, editable or not shown).
321	
322	Technique(s): Equivalence Partitioning - the three possible answers to Q-02 (prefilled, editable, not shown) are the partitions; the applicable one is kept when Q-02 is answered.
323	
324	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
325	|---|---|---|---|---|
326	| TCD-27-01 | EP | Signed-in customer opens the form: Name and Email are prefilled from the account, editable, or not shown, as confirmed for Q-02. | Positive | Missing info: conflict between the story and mockup-1 (Q-02). |
327	| TCD-27-02 | EP | If Name is prefilled and editable: the customer changes the Name, submits, and the displayed review shows the name as confirmed for Q-02 (edited or account name). | Positive | Missing info: Q-02. |
328	
329	### TR-28: Verify that the review cannot be submitted when "Name" is empty.
330	
331	Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field.
332	
333	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
334	|---|---|---|---|---|
335	| TCD-28-01 | EP | "Name" empty, rating, Review and Email valid, Submit: the review is not submitted and an error names "Name". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |
336	
337	### TR-29: Verify that a Name within the allowed length and characters is accepted, and a Name outside them is rejected.
338	
339	Technique(s): Equivalence Partitioning - character partitions (Latin letters, accented letters, hyphen/apostrophe, non-Latin script, digits, symbols only), one invalid partition per condition. Boundary Value Analysis - minimum (1 character, just above empty) and maximum length.
340	
341	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
342	|---|---|---|---|---|
343	| TCD-29-01 | EP | Name of Latin letters and a space (for example "Anna Smith"): accepted. | Positive | Assumption: letters and spaces are allowed until Q-05 is answered. |
344	| TCD-29-02 | EP | Name with accented letters (for example "Zoë Lê"): accepted. | Positive | Edge case: accented letters.<br>Assumption: accented letters are allowed until Q-05 is answered. |
345	| TCD-29-03 | EP | Name with a hyphen and an apostrophe (for example "Mary-Jane O'Neil"): accepted. | Positive | Edge case: hyphen and apostrophe.<br>Assumption: hyphens and apostrophes are allowed until Q-05 is answered. |
346	| TCD-29-04 | EP | Name in a non-Latin script (for example "李明"): accepted or rejected as confirmed for Q-05. | Positive | Missing info: allowed characters not stated (Q-05). |
347	| TCD-29-05 | EP | Name containing digits (for example "Anna2"): accepted or rejected with an error naming "Name", as confirmed for Q-05. | Negative | Missing info: whether digits are allowed (Q-05). |
348	| TCD-29-06 | EP | Name made only of symbols (for example "@#$%"): rejected with an error naming "Name", unless Q-05 allows it. | Negative | Missing info: allowed characters not stated (Q-05). |
349	| TCD-29-07 | BVA | Name of 1 character (just above empty): accepted. | Positive | Edge case: shortest non-empty name.<br>Missing info: minimum length not stated (Q-05). |
350	| TCD-29-08 | BVA | Name length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-05). |
351	| TCD-29-09 | BVA | Name length = maximum: accepted and shown in full. | Positive | Edge case: Name at the maximum length.<br>Missing info: maximum length not stated (Q-05). |
352	| TCD-29-10 | BVA | Name length = maximum + 1: input stops at the maximum, or the review is rejected with an error naming "Name". | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length and over-length behaviour not stated (Q-05, Q-18). |
353	
354	### TR-30: Verify that the review cannot be submitted when "Email" is empty.
355	
356	Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field.
357	
358	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
359	|---|---|---|---|---|
360	| TCD-30-01 | EP | "Email" empty, rating, Review and Name valid, Submit: the review is not submitted and an error names "Email". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |
361	
362	### TR-31: Verify that a correctly formatted email is accepted and an incorrectly formatted email is rejected.
363	
364	Technique(s): Equivalence Partitioning - valid format partitions and one invalid partition per format fault (one fault per condition). Boundary Value Analysis - maximum length. Error guessing - upper-case letters.
365	
366	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
367	|---|---|---|---|---|
368	| TCD-31-01 | EP | Email "anna.smith@example.com": accepted. | Positive | Assumption: standard format text@domain.tld until Q-06 is answered. |
369	| TCD-31-02 | EP | Email with a plus sign and a sub-domain ("anna+shop@mail.example.co.uk"): accepted. | Positive | Edge case: plus sign and sub-domain.<br>Assumption: standard format (Q-06). |
370	| TCD-31-03 | EP | Email without "@" ("anna.example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
371	| TCD-31-04 | EP | Email without the part before "@" ("@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
372	| TCD-31-05 | EP | Email without a domain ("anna@"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
373	| TCD-31-06 | EP | Email without a top-level domain ("anna@example"): rejected with an error naming "Email". | Negative | Assumption: a top-level domain is required (Q-06); some format rules accept this value. |
374	| TCD-31-07 | EP | Email with two "@" ("anna@@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
375	| TCD-31-08 | EP | Email with a space inside ("anna smith@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
376	| TCD-31-09 | Error guessing | Email in upper case ("ANNA@EXAMPLE.COM"): accepted. | Positive | Assumption: letter case does not matter (Q-06). |
377	| TCD-31-10 | BVA | Email length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-06). |
378	| TCD-31-11 | BVA | Email length = maximum: accepted. | Positive | Edge case: value exactly at the maximum.<br>Missing info: maximum length not stated (Q-06). |
379	| TCD-31-12 | BVA | Email length = maximum + 1: input stops at the maximum, or the review is rejected with an error naming "Email". | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length and over-length behaviour not stated (Q-06, Q-18). |
380	
381	### TR-32: Verify that leading and trailing spaces in Name and Email are removed, and a Name or Email made only of spaces counts as empty.
382	
383	Technique(s): Error guessing - space-padded and spaces-only input, one field per condition.
384	
385	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
386	|---|---|---|---|---|
387	| TCD-32-01 | Error guessing | Name with leading and trailing spaces ("  Anna Smith  "): accepted and, after approval, shown as "Anna Smith". | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
388	| TCD-32-02 | Error guessing | Name made only of spaces, Submit: the review is not submitted and an error names "Name". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
389	| TCD-32-03 | Error guessing | Email with leading and trailing spaces ("  anna@example.com  "): accepted as a valid email. | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
390	| TCD-32-04 | Error guessing | Email made only of spaces, Submit: the review is not submitted and an error names "Email". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
391	
392	### TR-33: Verify that when all required fields are valid, the review is submitted and a confirmation message is shown.
393	
394	Technique(s): Decision table - conditions "rating, review, name, email valid" and "save checkbox ticked: yes / no"; the all-valid rules give "submitted". The rules with one field invalid are listed under TR-34.
395	
396	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
397	|---|---|---|---|---|
398	| TCD-33-01 | Decision table | Rule: all four required fields valid, save checkbox not ticked, Submit: the review is submitted and a confirmation says it was received and waits for approval. | Positive | Assumption: confirmation says the review was received and waits for approval (Q-21). |
399	| TCD-33-02 | Decision table | Rule: all four required fields valid, save checkbox ticked, Submit: the review is submitted with the same confirmation. | Positive | Assumption: confirmation text (Q-21). |
400	
401	### TR-34: Verify that when a required field is empty or invalid, the review is not submitted and an error message names each field concerned.
402	
403	Technique(s): Decision table - conditions "rating / review / name / email valid: yes / no". Rules with exactly one invalid field are already covered: TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-31-03 to TCD-31-08. Rules with several invalid fields are collapsed into "all empty" and "two empty", which check that every field concerned is named. Equivalence Partitioning - validation timing.
404	
405	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
406	|---|---|---|---|---|
407	| TCD-34-01 | Decision table | Rule: all four required fields empty, Submit: the review is not submitted and errors name all four fields. | Negative | Assumption: each error names its field; wording checked for meaning (Q-20). |
408	| TCD-34-02 | Decision table | Rule: rating and review empty, Name and Email valid, Submit: errors name the rating and "Your review" only, not Name or Email. | Negative | Assumption: wording checked for meaning (Q-20). |
409	| TCD-34-03 | Decision table | After a rejected Submit, the values already entered stay in the form; the customer corrects the field, submits again and the review is submitted. | Positive | Assumption: entered values are kept after a rejected submit until Q-38 is answered. |
410	| TCD-34-04 | EP | Leaving a required field empty and moving to the next field shows no error until Submit is pressed. | Positive | Assumption: fields are checked on Submit only (Q-19). |
411	
412	### TR-35: Verify that after a successful submit the customer stays on the product page and the form is cleared.
413	
414	Technique(s): State transition - "form filled" to "form after success", with the save checkbox ticked or not as the deciding event.
415	
416	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
417	|---|---|---|---|---|
418	| TCD-35-01 | State transition | Successful Submit with the save checkbox not ticked: the customer stays on the product page and rating, review, Name and Email are all cleared. | Positive | Assumption: form cleared (Q-22). |
419	| TCD-35-02 | State transition | Successful Submit with the save checkbox ticked: the customer stays on the product page, rating and review are cleared, and Name and Email stay filled. | Positive | Assumption: Name and Email stay filled only if the checkbox was ticked (Q-22). |
420	
421	### TR-36: Verify that the "Save my name, email, and website..." checkbox is unchecked by default.
422	
423	Technique(s): Equivalence Partitioning - partitions "first visit (nothing saved)" and "visit after data was saved".
424	
425	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
426	|---|---|---|---|---|
427	| TCD-36-01 | EP | First visit with nothing saved in the browser: the save checkbox is not ticked. | Positive | |
428	| TCD-36-02 | EP | Visit after Name and Email were saved: the save checkbox is ticked or not ticked, as confirmed for Q-14. | Positive | Edge case: checkbox state on a return visit.<br>Missing info: not stated (Q-14). |
429	
430	### TR-37: Verify that when the save checkbox is ticked at submit, the name and email are filled in again on the next visit in the same browser.
431	
432	Technique(s): State transition - browser storage states "nothing saved" and "Name and Email saved"; events "Submit with box ticked", "Submit with box not ticked", "rejected Submit". Error guessing - other browser or private window.
433	
434	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
435	|---|---|---|---|---|
436	| TCD-37-01 | State transition | Nothing saved, valid Submit with the box ticked, next visit in the same browser: Name and Email are filled with the submitted values. | Positive | Assumption: only name and email are saved (Q-13, Q-14).<br>Risk: personal data stored on the device. |
437	| TCD-37-02 | State transition | Name and Email saved, valid Submit with a different Name and Email and the box ticked, next visit: the new values are filled. | Positive | Assumption: saved values are replaced (Q-14). |
438	| TCD-37-03 | State transition | Name and Email saved, valid Submit with the box not ticked, next visit: Name and Email are filled or empty as confirmed for Q-14. | Positive | Missing info: how saved data is removed (Q-14).<br>Risk: personal data left on a shared device. |
439	| TCD-37-04 | EP | After a ticked Submit, on the next visit only Name and Email are filled; rating and review are empty. | Positive | Assumption: only name and email are saved (Q-13, Q-14). |
440	| TCD-37-05 | Error guessing | After a ticked Submit, opening the page in another browser or a private window: Name and Email are empty. | Positive | Edge case: "in this browser" only. |
441	| TCD-37-06 | State transition | Nothing saved, box ticked but Submit rejected (for example "Your review" empty), next visit: Name and Email are empty. | Negative | Edge case: rejected submit with the box ticked.<br>Missing info: whether data is saved on a rejected submit (Q-14). |
442	
443	### TR-38: Verify that when the save checkbox is not ticked, no name or email is kept for the next visit.
444	
445	Technique(s): Equivalence Partitioning - partition "box not ticked, nothing saved before". Error guessing - data typed but not submitted.
446	
447	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
448	|---|---|---|---|---|
449	| TCD-38-01 | EP | Nothing saved, valid Submit with the box not ticked, next visit: Name and Email are empty. | Positive | Missing info: what is saved when the checkbox is not ticked (Q-14).<br>Risk: personal data left on a shared device. |
450	| TCD-38-02 | Error guessing | Name and Email typed but not submitted, page reloaded: Name and Email are empty (browser autofill switched off). | Positive | Missing info: Q-14.<br>Risk: personal data kept without consent. |
451	
452	### TR-39: Verify that a customer cannot submit more reviews for the same product than the confirmed limit.
453	
454	Technique(s): Boundary Value Analysis - count of reviews per customer and product (limit unknown). Error guessing - other product, changed identity.
455	
456	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
457	|---|---|---|---|---|
458	| TCD-39-01 | BVA | Customer has limit - 1 reviews for the product, submits another: accepted. | Positive | Missing info: number of reviews per customer and product not specified (Q-12). If the limit is 1, this is the first review (TCD-33-01) and is not repeated. |
459	| TCD-39-02 | BVA | Customer has exactly the limit, submits another (limit + 1): rejected with the message confirmed for Q-12. | Negative | Edge case: one above the limit.<br>Missing info: Q-12. |
460	| TCD-39-03 | Error guessing | Customer at the limit for product A submits a review for product B: accepted. | Positive | Missing info: Q-12; needs a build with two products. |
461	| TCD-39-04 | Error guessing | Customer at the limit submits again for the same product with a different Name and Email: still recognised and rejected. | Negative | Missing info: how the customer is identified (Q-01, Q-02, Q-12).<br>Risk: limit bypassed by changing name or email. |
462	
463	### TR-40: Verify that clicking Submit more than once quickly creates only one review.
464	
465	Technique(s): Error guessing - double click, repeated key presses, reload and browser back/forward after submit are known duplicate sources.
466	
467	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
468	|---|---|---|---|---|
469	| TCD-40-01 | Error guessing | Valid form, Submit double-clicked: one review is created (one pending, one shown after approval). | Negative | Edge case: rapid double click.<br>Assumption: only one review is created (Q-28).<br>Risk: duplicate reviews distort the rating. |
470	| TCD-40-02 | Error guessing | Valid form, Submit clicked and Enter pressed in a text field before the confirmation appears: one review is created. | Negative | Assumption: only one review is created (Q-28). |
471	| TCD-40-03 | Error guessing | Page reloaded right after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |
472	| TCD-40-04 | Error guessing | Browser Back and then Forward after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |
473	
474	### TR-41: Verify that when the review cannot be saved (server or network error), the customer is told and the entered data is kept.
475	
476	Technique(s): Error guessing - lost connection, server error and expired session are typical failure points of a submit.
477	
478	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
479	|---|---|---|---|---|
480	| TCD-41-01 | Error guessing | Network connection lost, Submit: a message says the review was not submitted and the entered data stays in the form. | Negative | Assumption: Q-29.<br>Missing info: demo-1.0 runs without a server or network (environment.md), so this cannot be produced there. |
481	| TCD-41-02 | Error guessing | Server returns an error on Submit: a message says the review was not submitted and the entered data stays in the form. | Negative | Assumption: Q-29. Not producible in demo-1.0. |
482	| TCD-41-03 | Error guessing | Session expired before Submit (signed-in customer): the customer is told and the entered data is not lost. | Negative | Assumption: Q-29.<br>Missing info: sign-in rules (Q-01); demo-1.0 has no sign-in. |
483	| TCD-41-04 | Error guessing | After a failed Submit, the connection returns and Submit is pressed again: exactly one review is created. | Positive | Assumption: Q-28, Q-29. |
484	
485	## Coverage by scenario type
486	
487	| Type | Covered by (condition IDs) |
488	|---|---|
489	| Positive | TCD-02-01, TCD-03-01 to TCD-03-04, TCD-04-01, TCD-04-02, TCD-04-05, TCD-06-01, TCD-08-01, TCD-09-01 to TCD-09-04, TCD-14-01, TCD-17-01, TCD-29-01, TCD-31-01, TCD-33-01, TCD-33-02, TCD-35-01, TCD-37-01 |
490	| Negative | TCD-02-02, TCD-04-03, TCD-05-01, TCD-07-01, TCD-10-01 to TCD-10-04, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-05, TCD-29-06, TCD-30-01, TCD-31-03 to TCD-31-08, TCD-34-01, TCD-34-02, TCD-39-02 |
491	| Boundary | TCD-03-01 to TCD-03-04, TCD-05-01, TCD-09-01 to TCD-09-04, TCD-10-01 to TCD-10-03, TCD-11-04, TCD-21-02 to TCD-21-04, TCD-22-01, TCD-22-03, TCD-23-05, TCD-29-07 to TCD-29-10, TCD-31-10 to TCD-31-12, TCD-39-01, TCD-39-02 |
492	| Validation | TCD-05-01, TCD-07-01, TCD-10-01, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-05, TCD-29-06, TCD-30-01, TCD-31-03 to TCD-31-08, TCD-32-02, TCD-32-04, TCD-34-01 to TCD-34-04 |
493	| Error handling | TCD-40-01 to TCD-40-04, TCD-41-01 to TCD-41-04 |
494	| Permissions | TCD-26-01 to TCD-26-04, TCD-27-01, TCD-27-02, TCD-13-01, TCD-16-01, TCD-16-02, TCD-39-02, TCD-39-04 |
495	| Integration | TCD-13-01, TCD-13-02, TCD-14-01 to TCD-14-03, TCD-15-01, TCD-15-02, TCD-17-01 to TCD-17-03, TCD-18-01, TCD-20-01 to TCD-20-03, TCD-21-01, TCD-22-01 to TCD-22-03, TCD-23-01 to TCD-23-06, TCD-24-01, TCD-24-02 |
496	| UI | TCD-01-01, TCD-02-03, TCD-02-04, TCD-06-01, TCD-06-02, TCD-18-04, TCD-25-01 to TCD-25-07 |
497	| Compatibility | None in this design; see "Not covered" |
498	| Regression | TCD-14-02, TCD-15-02, TCD-18-01, TCD-20-02, TCD-22-03, TCD-23-04 (existing approved reviews, the empty state and the rating summary still behave correctly after new reviews are added) |
499	| Data and privacy | TCD-12-01 to TCD-12-05, TCD-17-03, TCD-19-01, TCD-19-02, TCD-36-01, TCD-36-02, TCD-37-01 to TCD-37-06, TCD-38-01, TCD-38-02 |
500	
501	## Not covered
502	
503	| Type or area | Reason |
504	|---|---|
505	| Compatibility: browsers other than Chrome, mobile and tablet screen sizes | Only Chrome is given (environment.md, app-note.md); other browsers and devices are blocked by missing information (Q-31). Add conditions when Q-31 is answered. |
506	| Language and localisation | Page language not stated; English assumed (Q-31). |
507	| Moderator screens and workflow (approve / reject UI, who moderates) | Out of scope of US-VP02; only its effect on the product page is covered (TR-14, TR-15). The demo-1.0 helper button is a test tool, not the feature (environment.md). |
508	| Telling the author the moderation result (for example by email) | Assumed out of scope of this story (Q-26). |
509	| Editing or deleting one's own review | Assumed out of scope of this story (Q-27). |
510	| Automatic offensive-language filter | Assumed left to the moderator, no automatic filter (Q-30). |
511	| "Website" field | No Website field exists in mockup-1; nothing to test until Q-13 is answered (only the checkbox text is covered, TCD-25-04). |
512	| Accessibility beyond keyboard use (screen reader labels, colour contrast) | Not in any source; only keyboard use is covered (TCD-02-04, TCD-25-07). |
513	| Performance and load (many users submitting at once) | Not in the story; needs another environment. |
514	| Execution on demo-1.0 of TCD-13-01, TCD-13-02, TCD-15-01, TCD-15-02, TCD-23-03, TCD-24-02, TCD-26-01 to TCD-26-04, TCD-27-01, TCD-27-02, TCD-39-03, TCD-39-04, TCD-41-01 to TCD-41-03 | The conditions exist, but demo-1.0 has one product, no sign-in, no reject action, no server, and resets data on reload (app-note.md, environment.md); they need another build or environment. |
515	
516	## Assumptions to confirm
517	
518	| Condition ID | Assumption | Question ID |
519	|---|---|---|
520	| TCD-02-01, TCD-03-01 to TCD-03-04 | The rating is a whole number from 1 to 5, one per star. | Q-03 |
521	| TCD-02-03 | A hover preview, if any, is not kept after the pointer leaves. | Q-36 |
522	| TCD-04-01 to TCD-04-04 | Clicking another star changes the rating; it cannot be cleared except by reloading the page. | Q-16 |
523	| TCD-08-02 | "Your review" has no character restriction (accented, non-Latin, emoji allowed). | Q-37 |
524	| TCD-10-02 to TCD-10-04 | Typing and pasting stop at the maximum length. | Q-18 |
525	| TCD-11-01 to TCD-11-04, TCD-32-01 to TCD-32-04 | Spaces (and line breaks) are trimmed; a field of only spaces counts as empty; length is counted after trimming. | Q-17 |
526	| TCD-12-01 | HTML and script content is never executed, whatever the answer on how it is handled. | Q-15 |
527	| TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-34-01, TCD-34-02 | Each error names its field; wording is checked for meaning, not exact text. | Q-20 |
528	| TCD-34-03 | Entered values stay in the form after a rejected Submit. | Q-38 |
529	| TCD-34-04 | Fields are checked on Submit only. | Q-19 |
530	| TCD-14-01 | The demo-1.0 "Moderator: approve pending reviews" helper stands in for the moderator and is not part of the feature. | Q-07 |
531	| TCD-17-01 | Each displayed review shows star rating, reviewer name, date and review text. | Q-09 |
532	| TCD-17-02 | The date is the submit date, in any unambiguous format. | Q-24 |
533	| TCD-18-02, TCD-29-01 to TCD-29-03 | Names with letters, spaces, accented letters, hyphens and apostrophes are accepted. | Q-05 |
534	| TCD-21-01 | All approved reviews are shown on one page. | Q-23 |
535	| TCD-22-01 to TCD-22-03 | With no approved reviews, a short message says there are no reviews yet. | Q-25 |
536	| TCD-25-01 | The heading "ADD A REVIEW" is compared without regard to letter case. | Q-32 |
537	| TCD-31-01 to TCD-31-09 | A valid email has the standard format text@domain.tld (top-level domain required, letter case ignored). | Q-06 |
538	| TCD-33-01, TCD-33-02 | The confirmation says the review was received and waits for approval. | Q-21 |
539	| TCD-35-01, TCD-35-02 | After success the customer stays on the page; the form is cleared; Name and Email stay only if the checkbox was ticked. | Q-22 |
540	| TCD-37-01, TCD-37-02, TCD-37-04 | Only Name and Email are saved in this browser, and a new ticked submit replaces them. | Q-13, Q-14 |
541	| TCD-40-01 to TCD-40-04, TCD-41-04 | Only one review is created per submit action. | Q-28 |
542	| TCD-41-01 to TCD-41-04 | On a save failure a message says the review was not submitted and the entered data is kept. | Q-29 |
543	
```

## AI (2026-10-21T04:10:21)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1 && grep -n -E \"^#|Q-[0-9]+\" clarification-questions.md | head -80; wc -l clarification-questions.md",
  "description": "Scan clarification questions headings and IDs"
}
```

## Tool (2026-10-21T04:10:23)

```
1:# Clarification questions: US-VP02 Submit a Product Review
8:## Must ask
12:| Q-01 | AC-GEN | Who may submit a review | The story says "a product I purchased". Must the customer be signed in to submit a review, and must the system check that they bought this product? If a guest or a customer who did not buy it opens the page, should the form be hidden, disabled, or rejected on Submit with a message? | Decides who can submit at all; without it, tests for guests and non-buyers have no Expected Result. Risk of fake reviews. |
13:| Q-02 | AC-GEN | Name and Email for a known customer (conflict) | mockup-1 asks the customer to type "Name *" and "Email *", while the story speaks of a customer who purchased the product and is therefore known to the shop. For a signed-in customer, should Name and Email be prefilled from the account, editable, or not shown at all? | Conflict between the story and the mockup; changes what is built. |
14:| Q-03 | AC-01 | Allowed rating values | Is the rating a whole number from 1 to 5 (one per star), or are half stars (for example 3.5) allowed? | Defines the valid values of "Your rating" and how the rating is displayed. |
15:| Q-04 | AC-02 | Length of "Your review" | What are the minimum and maximum number of characters for "Your review" (for example at least 1 and at most N), or is there no maximum? No source states a limit; the demo build shows a "0 / 500" counter, but that is observed behaviour, not a requirement. | Boundary tests need exact limits. |
16:| Q-05 | AC-GEN | Rules for "Name" | What are the maximum length and the allowed characters of "Name" (letters only, or also digits, spaces, hyphens, apostrophes, accented letters)? | Needed to decide which Name values are accepted or rejected. |
17:| Q-06 | AC-GEN | Email format rule | Which rule decides a valid "Email": a standard format check (text@domain.tld), or a different rule? Is there a maximum length? | Needed to decide which Email values are accepted or rejected. |
18:| Q-07 | AC-03 | Moderation workflow | Who approves reviews (which role), can that person also reject a review, and what happens to a rejected review (deleted, or kept hidden)? | Defines the states of a review and what "approved" in AC-03 means. |
19:| Q-08 | AC-03 | Author's view of a pending review | Right after Submit, should the author see their own review on the product page marked as awaiting approval, or should it be hidden from everyone, the author included, until it is approved? | Expected Result of the step right after Submit. |
20:| Q-09 | AC-03 | Details shown per review | Which details are shown for each approved review: star rating, reviewer name (full name, first name only or initials), date, review text? There is no mockup of the reviews list. | Display tests, and privacy of the reviewer's name. |
21:| Q-10 | AC-03 | Order of reviews | In which order are approved reviews listed: newest first, oldest first, highest rating first, or another order? | A test of the list order has no Expected Result without it. |
22:| Q-11 | AC-03 | Rating summary and review count | Should the product page show an average rating and the number of reviews? If yes, is it calculated from approved reviews only, and how is the average rounded (for example one decimal, or nearest half star)? | A calculation with no defined result; pending or rejected reviews must not change the score shown. |
23:| Q-12 | AC-GEN | Reviews per customer and product | Can one customer submit more than one review for the same product, or only one? If only one, what should happen on a second attempt? | Business rule (uniqueness) that changes what is built. |
24:| Q-13 | AC-GEN | "website" in the save checkbox (conflict) | The checkbox reads "Save my name, email, and website in this browser for the next time I comment." but mockup-1 has no Website field. Should a Website field be added, or should the text drop "website"? | Conflict inside mockup-1; changes what is built. |
25:| Q-14 | AC-GEN | What the save checkbox stores | When the checkbox is ticked, which data is saved in the browser (name, email, anything else), for how long, and how can the customer remove it? Is anything saved when it is not ticked? | Privacy of personal data stored on the device. |
26:| Q-15 | AC-02 | HTML, scripts and links in text | If "Your review" or "Name" contains HTML tags, script code or web links, should they be shown as plain text, removed, or should the review be rejected? | Security risk (script injection) and display of every review. |
27:| Q-33 | AC-GEN | Cancelled or refunded orders | If the customer's order of this product was cancelled or refunded, may they still submit a review? If not, should the form be hidden, disabled, or rejected on Submit with a message? | Same area as Q-01: changes who may review. Risk of reviews from customers who never received the product. |
29:## Nice to confirm
33:| Q-16 | AC-01 | Changing the rating | Can the customer change the selected rating by clicking another star before Submit, and can they clear it again? | Clicking another star changes the rating; the rating cannot be cleared back to "no rating" except by reloading the page. |
34:| Q-17 | AC-02 | Spaces in text fields | Should leading and trailing spaces in "Your review", "Name" and "Email" be removed, and is a field with only spaces treated as empty? | Spaces are trimmed; a field with only spaces counts as empty and is rejected. |
35:| Q-18 | AC-02 | Text longer than the maximum | If there is a maximum length, should extra characters be blocked while typing or pasting, or accepted in the box and rejected on Submit with a message? | Typing and pasting stop at the maximum. |
36:| Q-19 | AC-GEN | When fields are validated | Are fields checked on Submit only, or also when the customer leaves a field? | Checked on Submit only. |
37:| Q-20 | AC-GEN | Error message wording and position | What is the wording and position of error messages: one message next to each field, or one summary above the form? | Each error names the field concerned; wording is checked for meaning, not exact text. |
38:| Q-21 | AC-GEN | Success message | What message is shown after a successful submit? For example, that the review was received and will be shown after approval. | A confirmation says the review was received and waits for approval. |
39:| Q-22 | AC-GEN | Form after submit | After a successful submit, is the form cleared, and does the customer stay on the same product page? | The customer stays on the product page and the form is cleared (Name and Email stay filled only if the save checkbox was ticked). |
40:| Q-23 | AC-03 | Number of reviews shown | Are all approved reviews shown at once, or a fixed number per page with paging or "Load more"? If so, how many per page? | All approved reviews are shown on one page. |
41:| Q-24 | AC-03 | Date shown with a review | Which date is shown (submit date or approval date) and in which format (for example 21/10/2026 or October 21, 2026)? | Submit date, in any unambiguous format; the format is not checked. |
42:| Q-25 | AC-03 | Product with no approved reviews | What should the reviews section show when a product has no approved reviews: a message saying there are no reviews yet, or no section at all? | A short message saying there are no reviews yet. |
43:| Q-26 | AC-03 | Telling the author the result | Is the author told (for example by email) when their review is approved or rejected? | No notification; out of scope of this story. |
44:| Q-27 | AC-GEN | Edit or delete own review | Is editing or deleting one's own review in the scope of US-VP02? | Out of scope. |
45:| Q-28 | AC-GEN | Double submit | If Submit is clicked twice quickly, should only one review be created? | Only one review is created. |
46:| Q-29 | AC-GEN | Server or network error | What should the customer see if the review cannot be saved (server or network error, session expired)? | A message says the review was not submitted, and the entered data is kept. |
47:| Q-30 | AC-GEN | Offensive language | Is offensive language filtered automatically, or left to the moderator? | Left to the moderator; no automatic filter. |
48:| Q-31 | AC-GEN | Browsers, devices and language | Which browsers and devices must be supported (desktop Chrome only, or also other browsers and mobile), and in which language is the page? | Desktop Chrome, English. |
49:| Q-32 | AC-GEN | Heading text | mockup-1 shows the heading "ADD A REVIEW" in capitals. Are capitals required, or is it only a style (so "Add a review" is also correct)? | The heading text is compared without regard to letter case. |
50:| Q-34 | AC-GEN | Keyboard use | Must the star rating and the whole form (fields, checkbox, Submit) be usable with the keyboard alone, and in which focus order? | The rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen. |
51:| Q-35 | AC-03 | Line breaks in a displayed review | If "Your review" is written on several lines, should the line breaks be kept when the review is shown on the product page? | Line breaks are shown as entered. |
52:| Q-36 | AC-01 | Star hover preview | When the pointer moves over the stars without clicking, may the stars show a preview, and must the selected rating come back when the pointer leaves? | A hover preview, if any, is not kept; the selected rating is unchanged after the pointer leaves. |
53:| Q-37 | AC-02 | Characters allowed in "Your review" | Are all characters allowed in "Your review" (accented and non-Latin letters, digits, punctuation, emoji), or are some blocked? | No character restriction in "Your review". |
54:| Q-38 | AC-GEN | Values after a rejected submit | After Submit is rejected because of an error, should the values already entered stay in the form? | Entered values stay in the form after a rejected Submit. |
56:## Conflicts between sources
60:| Q-02 | exam/user-story.md: "As a customer, I want to submit a review for a product I purchased" (the reviewer is a known buyer) | exam/mockup-1.png: the form asks the reviewer to type "Name *" and "Email *" by hand, as for a guest |
61:| Q-13 | exam/mockup-1.png, checkbox: "Save my name, email, and website in this browser for the next time I comment." | exam/mockup-1.png, form: only "Your rating *", "Your review *", "Name *" and "Email *"; there is no Website field |
61 clarification-questions.md
```

## AI (2026-10-21T04:10:27)

**Tool call `Bash`:**

```json
{
  "command": "sed -n 1,11p runs/run-1/clarification-questions.md; python -c \"\nimport openpyxl\nfor f in ['runs/run-1/test-requirements.xlsx','skills/test-case-generation/assets/test-case-template.xlsx']:\n    wb=openpyxl.load_workbook(f)\n    for ws in wb:\n        print('==',f,ws.title,ws.dimensions, ws.freeze_panes)\n        for c,d in ws.column_dimensions.items(): print(' col',c,d.width)\n        for r in ws.iter_rows(values_only=True):\n            print(r)\n\"",
  "description": "Dump TR list and TC template"
}
```

## Tool (2026-10-21T04:10:30)

```
# Clarification questions: US-VP02 Submit a Product Review

Sources reviewed: exam/user-story.md (text of "User Story for My Shop.docx"), exam/mockup-1.png, exam/mockup-2.png (company logo only, no screen content), knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md
Date: 2026-10-21

Acceptance criteria: AC-01 "Allow customers to enter a star rating"; AC-02 "Provide a text box for review comments"; AC-03 "Display approved reviews on the product page". AC-GEN = the story as a whole (not tied to one AC). No answers from the product owner have been received yet.

## Must ask

| Q ID | AC ID | Ambiguous point | Question | Why it matters |
|---|---|---|---|---|
== runs/run-1/test-requirements.xlsx Test Requirements A1:E42 A2
 col A 10.0
 col B 45.0
 col C 10.0
 col D 60.0
 col E 50.0
('AC ID', 'Acceptance Criteria', 'TR ID', 'Test Requirements', 'Notes')
('AC-01', 'Allow customers to enter a star rating', 'TR-01', 'Verify that the "Your rating *" field shows 5 stars.', None)
('AC-01', 'Allow customers to enter a star rating', 'TR-02', 'Verify that the customer can select a rating by clicking a star, and the selected stars are shown as selected.', 'Assumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.\nMissing info: whether half stars are allowed (Q-03).')
('AC-01', 'Allow customers to enter a star rating', 'TR-03', 'Verify that both the lowest rating (1 star) and the highest rating (5 stars) can be selected and are saved with the review.', 'Edge case: lowest and highest rating.\nAssumption: rating range 1 to 5 until Q-03 is answered.')
('AC-01', 'Allow customers to enter a star rating', 'TR-04', 'Verify that the customer can change the selected rating before submitting, and only the last selected rating is saved.', 'Assumption: clicking another star changes the rating; it cannot be cleared to no rating (Q-16).')
('AC-01', 'Allow customers to enter a star rating', 'TR-05', 'Verify that the review cannot be submitted when no star rating is selected.', 'Assumption: an error message names the rating field; wording checked for meaning, not exact text (Q-20).')
('AC-02', 'Provide a text box for review comments', 'TR-06', 'Verify that a multi-line text box "Your review *" is provided for the review comment.', None)
('AC-02', 'Provide a text box for review comments', 'TR-07', 'Verify that the review cannot be submitted when "Your review" is empty.', None)
('AC-02', 'Provide a text box for review comments', 'TR-08', 'Verify that review text within the allowed length is accepted and saved as entered.', 'Missing info: minimum and maximum length not stated (Q-04).')
('AC-02', 'Provide a text box for review comments', 'TR-09', 'Verify that review text of exactly the minimum length and exactly the maximum length is accepted.', 'Edge case: values exactly at the minimum and the maximum.\nMissing info: minimum and maximum length not stated (Q-04).')
('AC-02', 'Provide a text box for review comments', 'TR-10', 'Verify that review text shorter than the minimum or longer than the maximum is not accepted.', 'Edge case: one character below the minimum and one above the maximum.\nMissing info: minimum and maximum length not stated (Q-04).\nAssumption: typing and pasting stop at the maximum until Q-18 is answered.')
('AC-02', 'Provide a text box for review comments', 'TR-11', 'Verify that review text made only of spaces is treated as empty and the review is not submitted.', 'Edge case: whitespace-only input.\nAssumption: spaces are trimmed and a field with only spaces counts as empty (Q-17).')
('AC-02', 'Provide a text box for review comments', 'TR-12', 'Verify that HTML tags, script code and links entered in "Your review" or "Name" are never run as code on the product page.', 'Missing info: whether such content is shown as plain text, removed or rejected (Q-15).\nAssumption: content is never executed, whatever the answer to Q-15.\nRisk: script injection would affect every visitor of the product page.')
('AC-03', 'Display approved reviews on the product page', 'TR-13', 'Verify that a newly submitted review is not displayed on the product page while it waits for approval.', 'Missing info: whether the author sees their own pending review (Q-08).\nRisk: unmoderated content shown publicly.')
('AC-03', 'Display approved reviews on the product page', 'TR-14', 'Verify that a submitted review is displayed on the product page after it is approved.', 'Missing info: who approves and how (Q-07).')
('AC-03', 'Display approved reviews on the product page', 'TR-15', 'Verify that a rejected review is never displayed on the product page.', 'Missing info: whether a review can be rejected and what happens to it (Q-07).')
('AC-03', 'Display approved reviews on the product page', 'TR-16', 'Verify that the author sees their own pending review only in the way confirmed for Q-08 (marked as awaiting approval, or not at all).', "Missing info: author's view of a pending review not specified (Q-08).")
('AC-03', 'Display approved reviews on the product page', 'TR-17', 'Verify that each displayed review shows the confirmed details (star rating, reviewer name, date, review text).', 'Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered.\nMissing info: which details and which form of the name are shown; no mockup of the reviews list (Q-09).\nAssumption: submit date in any unambiguous format (Q-24).')
('AC-03', 'Display approved reviews on the product page', 'TR-18', 'Verify that the star rating, name and review text of a displayed review match what the customer submitted.', None)
('AC-03', 'Display approved reviews on the product page', 'TR-19', "Verify that the reviewer's email address is never displayed on the product page.", 'Risk: personal data could be shown publicly.')
('AC-03', 'Display approved reviews on the product page', 'TR-20', 'Verify that approved reviews are listed in the confirmed order.', 'Missing info: list order not specified (Q-10).')
('AC-03', 'Display approved reviews on the product page', 'TR-21', 'Verify that all approved reviews can be seen when a product has many reviews.', 'Edge case: large number of approved reviews.\nAssumption: all approved reviews are shown on one page (Q-23).')
('AC-03', 'Display approved reviews on the product page', 'TR-22', 'Verify that a clear empty state is shown when the product has no approved reviews.', 'Edge case: product with no approved reviews.\nAssumption: a short message saying there are no reviews yet (Q-25).')
('AC-03', 'Display approved reviews on the product page', 'TR-23', 'Verify that the average rating and review count on the product page, if shown, are calculated from approved reviews only.', 'Missing info: whether a summary is shown and how it is rounded (Q-11).\nRisk: pending or rejected reviews could change the score shown to shoppers.')
('AC-03', 'Display approved reviews on the product page', 'TR-24', 'Verify that a review is displayed only on the page of the product it was written for.', 'Risk: reviews shown on the wrong product mislead shoppers.')
('AC-GEN', 'General: form labels and layout shown in the mockup', 'TR-25', 'Verify that the review form shows the heading, the info text "Your email address will not be published. Required fields are marked *", the fields "Your rating *", "Your review *", "Name *", "Email *", the save checkbox and the "Submit" button as in mockup-1.', 'Assumption: the heading "ADD A REVIEW" is compared without regard to letter case (Q-32).\nMissing info: final text of the save checkbox (Q-13).')
('AC-GEN', 'General: who may review (story: "a product I purchased")', 'TR-26', 'Verify that only a customer who is allowed to review (as confirmed for Q-01) can submit a review, and a customer who is not allowed cannot.', 'Missing info: sign-in and purchase check not specified (Q-01).\nRisk: guests or non-buyers could post fake reviews.')
('AC-GEN', 'General: Name and Email for a known customer (story vs mockup)', 'TR-27', 'Verify that Name and Email for a signed-in customer are handled as confirmed for Q-02 (prefilled, editable or not shown).', 'Missing info: conflict between the story and mockup-1 (Q-02).')
('AC-GEN', 'General: form fields shown in the mockup', 'TR-28', 'Verify that the review cannot be submitted when "Name" is empty.', None)
('AC-GEN', 'General: form fields shown in the mockup', 'TR-29', 'Verify that a Name within the allowed length and characters is accepted, and a Name outside them is rejected.', 'Missing info: maximum length and allowed characters not stated (Q-05).\nEdge case: Name at the maximum length and with accented letters, hyphens or apostrophes.')
('AC-GEN', 'General: form fields shown in the mockup', 'TR-30', 'Verify that the review cannot be submitted when "Email" is empty.', None)
('AC-GEN', 'General: form fields shown in the mockup', 'TR-31', 'Verify that a correctly formatted email is accepted and an incorrectly formatted email is rejected.', 'Missing info: email format rule and maximum length not stated (Q-06).')
('AC-GEN', 'General: form fields shown in the mockup', 'TR-32', 'Verify that leading and trailing spaces in Name and Email are removed, and a Name or Email made only of spaces counts as empty.', 'Edge case: whitespace-only and space-padded input.\nAssumption: spaces are trimmed and a field with only spaces counts as empty (Q-17).')
('AC-GEN', 'General: submitting the review form', 'TR-33', 'Verify that when all required fields are valid, the review is submitted and a confirmation message is shown.', 'Assumption: the confirmation says the review was received and waits for approval (Q-21).')
('AC-GEN', 'General: submitting the review form', 'TR-34', 'Verify that when a required field is empty or invalid, the review is not submitted and an error message names each field concerned.', 'Assumption: fields are checked on Submit only (Q-19).\nAssumption: wording checked for meaning, not exact text (Q-20).')
('AC-GEN', 'General: submitting the review form', 'TR-35', 'Verify that after a successful submit the customer stays on the product page and the form is cleared.', 'Assumption: form cleared; Name and Email stay filled only if the save checkbox was ticked (Q-22).')
('AC-GEN', 'General: save checkbox shown in the mockup', 'TR-36', 'Verify that the "Save my name, email, and website..." checkbox is unchecked by default.', None)
('AC-GEN', 'General: save checkbox shown in the mockup', 'TR-37', 'Verify that when the save checkbox is ticked at submit, the name and email are filled in again on the next visit in the same browser.', 'Assumption: only name and email are saved until Q-13 and Q-14 are answered.\nMissing info: what is saved, where and for how long (Q-14); "website" with no Website field (Q-13).\nRisk: personal data stored on the device.')
('AC-GEN', 'General: save checkbox shown in the mockup', 'TR-38', 'Verify that when the save checkbox is not ticked, no name or email is kept for the next visit.', 'Missing info: what is saved when the checkbox is not ticked (Q-14).\nRisk: personal data left on a shared device.')
('AC-GEN', 'General: reviews per customer and product (story as a whole)', 'TR-39', 'Verify that a customer cannot submit more reviews for the same product than the confirmed limit.', 'Missing info: number of reviews per customer and product not specified (Q-12).')
('AC-GEN', 'General: submitting the review form', 'TR-40', 'Verify that clicking Submit more than once quickly creates only one review.', 'Edge case: rapid double click.\nAssumption: only one review is created (Q-28).\nRisk: duplicate reviews distort the rating.')
('AC-GEN', 'General: submitting the review form', 'TR-41', 'Verify that when the review cannot be saved (server or network error), the customer is told and the entered data is kept.', 'Assumption: an error message is shown and the entered data is kept (Q-29).')
== skills/test-case-generation/assets/test-case-template.xlsx Test Cases A1:G1 A2
 col A 10.0
 col B 12.0
 col C 45.0
 col D 35.0
 col E 60.0
 col F 55.0
 col G 40.0
('TR ID', 'TC ID', 'TC Summary', 'Pre-Condition', 'Steps', 'Expected Result', 'Notes')
```

## AI (2026-10-21T04:10:36)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/exam && cat user-story.md; echo ====; cat app/index.html; echo ====; wc -l app/app.js",
  "description": "Read user story and demo HTML"
}
```

## Tool (2026-10-21T04:10:37)

```
# Exam: Submit a Product Review (text of the Word file)

Application name: My Shop
US-VP02: Submit a Product Review
As a customer, I want to submit a review for a product I purchased, so that I can share my experience with others.
Acceptance Criteria:
- Allow customers to enter a star rating
- Provide a text box for review comments
- Display approved reviews on the product page

The Word file also holds two mockup images, saved here as `mockup-1.png` and `mockup-2.png`.
====
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Classic Cotton T-Shirt - My Shop</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header">
    <div class="container">
      <span class="logo">My Shop</span>
      <nav class="site-nav">
        <a href="#">Home</a>
        <a href="#">Men</a>
        <a href="#">Women</a>
        <a href="#">Cart (0)</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="product">
      <div class="product-image" aria-hidden="true">T-SHIRT</div>
      <div class="product-info">
        <h1>Classic Cotton T-Shirt</h1>
        <div class="rating-summary">
          <span class="stars-static" id="summary-stars" aria-hidden="true"></span>
          <span id="summary-text"></span>
        </div>
        <p class="price">$19.99</p>
        <p class="description">
          A soft, breathable everyday t-shirt made from 100% combed cotton.
          Regular fit, crew neck, available in five colours.
        </p>
      </div>
    </section>

    <section class="reviews">
      <h2 id="reviews-heading">Reviews</h2>
      <p id="no-reviews" class="muted" hidden>There are no reviews yet.</p>
      <ul id="review-list" class="review-list"></ul>
    </section>

    <section class="add-review">
      <h2 class="section-title">Add a review</h2>
      <p>Your email address will not be published. Required fields are marked <span class="req">*</span></p>

      <div id="form-errors" class="alert alert-error" role="alert" hidden></div>
      <div id="form-success" class="alert alert-success" role="status" hidden></div>

      <form id="review-form" novalidate>
        <div class="field field-inline">
          <span class="label" id="rating-label">Your rating <span class="req">*</span></span>
          <div class="star-input" id="star-input" role="radiogroup" aria-labelledby="rating-label">
            <button type="button" class="star" data-index="0" role="radio" aria-checked="false" aria-label="1 star" title="1 star">&#9733;</button>
            <button type="button" class="star" data-index="1" role="radio" aria-checked="false" aria-label="2 stars" title="2 stars">&#9733;</button>
            <button type="button" class="star" data-index="2" role="radio" aria-checked="false" aria-label="3 stars" title="3 stars">&#9733;</button>
            <button type="button" class="star" data-index="3" role="radio" aria-checked="false" aria-label="4 stars" title="4 stars">&#9733;</button>
            <button type="button" class="star" data-index="4" role="radio" aria-checked="false" aria-label="5 stars" title="5 stars">&#9733;</button>
          </div>
          <span id="rating-value" class="muted"></span>
        </div>

        <div class="field">
          <label for="comment">Your review <span class="req">*</span></label>
          <textarea id="comment" name="comment" rows="4" maxlength="500"></textarea>
          <div class="char-count"><span id="char-count">0</span> / 500</div>
        </div>

        <div class="field">
          <label for="name">Name <span class="req">*</span></label>
          <input type="text" id="name" name="name">
        </div>

        <div class="field">
          <label for="email">Email <span class="req">*</span></label>
          <input type="email" id="email" name="email">
        </div>

        <div class="field checkbox">
          <input type="checkbox" id="save-info" name="save-info">
          <label for="save-info">Save my name, email, and website in this browser for the next time I comment.</label>
        </div>

        <button type="submit" class="btn-primary">Submit</button>
      </form>
    </section>

    <section class="moderator">
      <h3>Moderator</h3>
      <p>Pending approval: <strong id="pending-count">0</strong></p>
      <button type="button" id="approve-btn" class="btn-secondary">Moderator: approve pending reviews</button>
      <p id="moderator-msg" class="muted" role="status"></p>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">&copy; 2026 My Shop. Build demo-1.0</div>
  </footer>

  <script src="app.js"></script>
</body>
</html>
====
318 app/app.js
```

## AI (2026-10-21T04:10:42)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/exam/app && sed -n 1,60p app.js",
  "description": "Read start of demo app script for seed data"
}
```

## Tool (2026-10-21T04:10:43)

```
(function () {
  'use strict';

  var MAX_REVIEW_LENGTH = 500;
  var STORAGE_KEY = 'myshop.commenter';
  var EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Reviews for this product. Status is "pending" until a moderator approves it.
  var reviews = [
    {
      id: 1,
      author: 'Anna K.',
      rating: 5,
      comment: 'Great fit and the fabric feels really soft. Washed it several times and it still looks new.',
      date: 'September 14, 2026',
      status: 'approved'
    },
    {
      id: 2,
      author: 'David L.',
      rating: 4,
      comment: 'Good quality for the price. The colour is slightly lighter than in the photo.',
      date: 'September 29, 2026',
      status: 'approved'
    },
    {
      id: 3,
      author: 'Mai T.',
      rating: 3,
      comment: 'Comfortable, but it runs a little small. I would order one size up next time.',
      date: 'October 8, 2026',
      status: 'approved'
    }
  ];
  var nextId = 4;

  var selectedStar = null; // index of the selected star button (0-4)

  var el = {
    form: document.getElementById('review-form'),
    stars: Array.prototype.slice.call(document.querySelectorAll('#star-input .star')),
    ratingValue: document.getElementById('rating-value'),
    comment: document.getElementById('comment'),
    charCount: document.getElementById('char-count'),
    name: document.getElementById('name'),
    email: document.getElementById('email'),
    saveInfo: document.getElementById('save-info'),
    errors: document.getElementById('form-errors'),
    success: document.getElementById('form-success'),
    list: document.getElementById('review-list'),
    noReviews: document.getElementById('no-reviews'),
    heading: document.getElementById('reviews-heading'),
    summaryStars: document.getElementById('summary-stars'),
    summaryText: document.getElementById('summary-text'),
    pendingCount: document.getElementById('pending-count'),
    approveBtn: document.getElementById('approve-btn'),
    moderatorMsg: document.getElementById('moderator-msg')
  };

  // ---------- helpers ----------
```

## AI (2026-10-21T04:13:52)

**Tool call `mcp__ccd_turn__update_plan`:**

```json
{
  "items": [
    {
      "content": "Read skill, rules, inputs and knowledge",
      "status": "completed"
    },
    {
      "content": "Write test cases per condition",
      "status": "in_progress"
    },
    {
      "content": "Export test-cases.xlsx from template",
      "status": "pending"
    },
    {
      "content": "Check traceability and self-check",
      "status": "pending"
    },
    {
      "content": "Report cases, TBCs and assumptions",
      "status": "pending"
    }
  ],
  "scope": "first_task"
}
```

## Tool (2026-10-21T04:13:52)

```
PreToolUse:mcp__ccd_turn__update_plan hook error: Not shown: you are a subagent, and the app shows only the main conversation's task list and wrap-up. Do not call update_plan or wrap_up again; carry on with your task and report your result as usual.
```

## AI (2026-10-21T04:16:56)

**Tool call `Write`:**

```json
{
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\gen_tc.py",
  "content": "import re, shutil, sys, collections\nimport openpyxl\nfrom openpyxl.styles import Alignment\n\nBASE = r\"C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\"\nRUN = BASE + r\"\\runs\\run-1\"\nTEMPLATE = BASE + r\"\\skills\\test-case-generation\\assets\\test-case-template.xlsx\"\nOUT = RUN + r\"\\test-cases.xlsx\"\n\n# ---------- read design conditions ----------\ndesign = open(RUN + r\"\\test-design.md\", encoding=\"utf-8\").read()\nconds = collections.OrderedDict()\nfor line in design.splitlines():\n    m = re.match(r\"\\|\\s*(TCD-(\\d\\d)-\\d\\d)\\s*\\|\\s*([^|]+?)\\s*\\|\\s*([^|]+?)\\s*\\|\\s*(Positive|Negative)\\s*\\|\\s*(.*?)\\s*\\|\\s*$\", line)\n    if m:\n        cid, trn, tech, text, pn, notes = m.groups()\n        conds[cid] = dict(tr=\"TR-\" + trn, tech=tech, text=text, pn=pn,\n                          notes=[n.strip() for n in notes.split(\"<br>\") if n.strip()])\n\nwb_tr = openpyxl.load_workbook(RUN + r\"\\test-requirements.xlsx\")\ntr_ids = [r[2] for r in wb_tr.active.iter_rows(min_row=2, values_only=True) if r[2]]\n\n# ---------- step helpers ----------\nORD = {1: \"1st\", 2: \"2nd\", 3: \"3rd\", 4: \"4th\", 5: \"5th\"}\nNAME, EMAIL = \"Anna Smith\", \"anna.smith@example.com\"\nTXT = \"Soft fabric, true to size. Would buy again.\"\nCB = '\"Save my name, email, and website in this browser for the next time I comment.\"'\n\ndef star(n): return f'Click the {ORD[n]} star of \"Your rating *\".'\ndef rev(t): return f'Enter \"{t}\" in \"Your review *\".'\ndef nm(v): return f'Enter \"{v}\" in \"Name *\".'\ndef em(v): return f'Enter \"{v}\" in \"Email *\".'\nSAVE = f\"Tick the checkbox {CB}\"\nSUB = 'Click \"Submit\".'\nAPP = 'Click \"Moderator: approve pending reviews\".'\ndef find(t): return f'Find the review \"{t}\" in the \"Reviews\" list.'\ndef fill(r=4, t=TXT, n=NAME, e=EMAIL):\n    s = []\n    if r: s.append(star(r))\n    if t is not None: s.append(rev(t))\n    if n is not None: s.append(nm(n))\n    if e is not None: s.append(em(e))\n    return s\n\nPRE = ('demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; '\n       '\"Pending approval: 0\"; nothing saved in this browser (Name * and Email * empty on load).')\nPRE_CLEAN = (PRE + ' If Name * or Email * is filled on load, clear the saved data first: '\n             'DevTools (F12) > Application > Storage > Clear site data, then reload.')\nPRE_CLIP = lambda what: PRE + f\" {what} is ready in the clipboard.\"\n\nOK = 'The review is submitted: a confirmation message appears above the form and \"Pending approval\" changes from 0 to 1.'\nNOT = 'The review is not submitted: no confirmation message appears and \"Pending approval\" stays 0.'\n\nVALID = \"Assumption: the valid data used (rating 4, review text, Name, Email) meets the unconfirmed length and format rules (Q-04, Q-05, Q-06).\"\ndef BLK(reason, q=None):\n    qq = f\" ({q})\" if q else \"\"\n    return f\"Missing info: cannot be run on demo-1.0 ({reason}){qq}; needs a build or environment that has it.\"\n\nTCS = []\ndef T(cid, summary, pre, steps, expected, extra=None, valid=False):\n    TCS.append(dict(cid=cid, summary=summary, pre=pre, steps=steps, expected=expected,\n                    extra=(extra or []) + ([VALID] if valid else [])))\n\n# ---------------- TR-01 ----------------\nT(\"TCD-01-01\", 'Verify that \"Your rating *\" shows exactly 5 stars, none selected, when the form opens.', PRE,\n  ['Scroll to the \"Add a review\" form.', 'Look at the stars next to \"Your rating *\" without clicking them.'],\n  'Exactly 5 star icons are shown next to \"Your rating *\" and none of them is shown as selected.')\n\n# ---------------- TR-02 ----------------\nT(\"TCD-02-01\", \"Verify that clicking the 3rd star selects rating 3.\", PRE,\n  [star(3), 'Look at the 5 stars of \"Your rating *\".'],\n  'Stars 1, 2 and 3 are shown as selected and stars 4 and 5 are shown as not selected.')\nT(\"TCD-02-02\", \"Verify that clicking the left half of a star does not set a half-star rating.\", PRE,\n  ['Click the left half of the 3rd star of \"Your rating *\".', 'Look at the stars of \"Your rating *\".',\n   rev(\"Half star check.\"), nm(NAME), em(EMAIL), SUB, APP, find(\"Half star check.\")],\n  'To be confirmed (Q-03): no half star is shown, neither in \"Your rating *\" after step 1 nor on the review \"Half star check.\" in the \"Reviews\" list; the rating is a whole number of stars.',\n  valid=True)\nT(\"TCD-02-03\", \"Verify that moving the pointer over the stars without clicking keeps the selected rating.\", PRE,\n  [star(2), 'Move the pointer over the 5th star of \"Your rating *\" without clicking.',\n   'Move the pointer away from the stars.', 'Look at the 5 stars of \"Your rating *\".'],\n  'To be confirmed (Q-36): stars 1 and 2 are shown as selected and stars 3, 4 and 5 as not selected (rating still 2).')\nT(\"TCD-02-04\", \"Verify that a rating can be selected with the keyboard only.\", PRE,\n  ['Click on the info text \"Your email address will not be published. Required fields are marked *\" to place the focus before the form.',\n   'Press Tab until a star of \"Your rating *\" has the focus.',\n   'Use the arrow keys to move to the 4th star and press Space (if nothing changes, press Enter).',\n   'Look at the 5 stars of \"Your rating *\".'],\n  'To be confirmed (Q-34): stars 1 to 4 are shown as selected and star 5 as not selected, without using the mouse after step 1.')\n\n# ---------------- TR-03 ----------------\nfor cid, n, word in [(\"TCD-03-01\", 1, \"one star\"), (\"TCD-03-02\", 2, \"two stars\"),\n                     (\"TCD-03-03\", 4, \"four stars\"), (\"TCD-03-04\", 5, \"five stars\")]:\n    t = f\"Rating check: {word}.\"\n    T(cid, f\"Verify that a review with rating {n} is submitted and shown with {n} star{'s' if n > 1 else ''}.\", PRE,\n      fill(n, t) + [SUB, APP, find(t)],\n      f'The review \"{t}\" appears in the \"Reviews\" list. To be confirmed (Q-03, Q-09): it is shown with {n} of 5 stars selected.',\n      valid=True)\n\n# ---------------- TR-04 ----------------\nT(\"TCD-04-01\", \"Verify that clicking the 5th star after the 2nd changes the rating to 5.\", PRE,\n  [star(2), star(5), 'Look at the 5 stars of \"Your rating *\".'],\n  'To be confirmed (Q-16): all 5 stars are shown as selected (rating 5).')\nT(\"TCD-04-02\", \"Verify that clicking the 2nd star after the 5th changes the rating to 2.\", PRE,\n  [star(5), star(2), 'Look at the 5 stars of \"Your rating *\".'],\n  'To be confirmed (Q-16): only stars 1 and 2 are shown as selected; stars 3, 4 and 5 are not selected (rating 2).')\nT(\"TCD-04-03\", \"Verify that clicking the selected 3rd star again does not clear the rating.\", PRE,\n  [star(3), star(3), 'Look at the 5 stars of \"Your rating *\".'],\n  'To be confirmed (Q-16): stars 1, 2 and 3 are still shown as selected (rating 3); the rating is not cleared to no rating.')\nT(\"TCD-04-04\", \"Verify that reloading the page resets a selected rating to no rating.\", PRE,\n  [star(3), \"Reload the page (F5).\", 'Look at the 5 stars of \"Your rating *\".'],\n  'None of the 5 stars is shown as selected.',\n  [\"Assumption: reloading is the only way back to no rating (Q-16); a reload restores the initial data (app-note.md).\"])\nt = \"Changed rating, final is three.\"\nT(\"TCD-04-05\", \"Verify that only the last selected rating is saved after several changes.\", PRE,\n  [star(1), star(4), star(2), star(3), rev(t), nm(NAME), em(EMAIL), SUB, APP, find(t)],\n  f'The review \"{t}\" appears in the \"Reviews\" list. To be confirmed (Q-09): it is shown with 3 of 5 stars selected (not 1, 4 or 2).',\n  valid=True)\n\n# ---------------- TR-05 ----------------\nT(\"TCD-05-01\", \"Verify that the review is not submitted when no star rating is selected.\", PRE,\n  fill(None) + [SUB],\n  NOT + ' To be confirmed (Q-20): an error message names the rating field (\"Your rating\").', valid=True)\n\n# ---------------- TR-06 ----------------\nT(\"TCD-06-01\", 'Verify that pressing Enter in \"Your review *\" starts a new line without submitting.', PRE,\n  ['Click in \"Your review *\".', 'Type \"Line one\".', \"Press Enter.\", 'Type \"Line two\".'],\n  '\"Line two\" is shown on a new line below \"Line one\" inside \"Your review *\"; no confirmation or error message appears and \"Pending approval\" stays 0.')\nT(\"TCD-06-02\", \"Verify that a multi-line review keeps its line breaks on the product page.\", PRE,\n  [star(4), 'Click in \"Your review *\" and type \"Line one\", press Enter, type \"Line two\", press Enter, type \"Line three\".',\n   nm(NAME), em(EMAIL), SUB, APP, 'Find the review starting with \"Line one\" in the \"Reviews\" list.'],\n  'To be confirmed (Q-35): the review shows \"Line one\", \"Line two\" and \"Line three\" on three separate lines.', valid=True)\n\n# ---------------- TR-07 ----------------\nT(\"TCD-07-01\", 'Verify that the review is not submitted when \"Your review *\" is empty.', PRE,\n  [star(4), 'Leave \"Your review *\" empty.', nm(NAME), em(EMAIL), SUB],\n  NOT + ' To be confirmed (Q-20): an error message names \"Your review\".', valid=True)\n\n# ---------------- TR-08 ----------------\nT(\"TCD-08-01\", \"Verify that a review text within the allowed length is saved and shown as entered.\", PRE,\n  fill(4, TXT) + [SUB, APP, find(TXT)],\n  f'The review appears in the \"Reviews\" list with the text \"{TXT}\" exactly as entered (same words, punctuation and letter case).',\n  [f\"Assumption: the text used ({len(TXT)} characters) is between the minimum and the maximum length until Q-04 is answered.\"],\n  valid=True)\nt = \"Très bien, Größe M passt! 日本語 OK 100% 👍\"\nT(\"TCD-08-02\", \"Verify that accented, non-Latin, digit, punctuation and emoji characters are saved unchanged.\", PRE,\n  fill(4, t) + [SUB, APP, find(t)],\n  f'To be confirmed (Q-37): the review is accepted and, in the \"Reviews\" list, its text is shown exactly as \"{t}\" (no \"?\", boxes or encoded characters).',\n  valid=True)\nt = \"Pasted review: comfy and soft.\"\nT(\"TCD-08-03\", \"Verify that a review text pasted from the clipboard is saved like typed text.\",\n  PRE_CLIP(f'The text \"{t}\" (copied from Notepad)'),\n  [star(4), 'Click in \"Your review *\" and press Ctrl+V.', nm(NAME), em(EMAIL), SUB, APP, find(t)],\n  f'The review appears in the \"Reviews\" list with the text \"{t}\" exactly as pasted.', valid=True)\n\n# ---------------- TR-09 ----------------\nfor cid, what, extra_exp in [(\"TCD-09-01\", \"[minimum]\", \"\"), (\"TCD-09-02\", \"[minimum + 1]\", \"\"),\n                             (\"TCD-09-03\", \"[maximum - 1]\", \"\"),\n                             (\"TCD-09-04\", \"[maximum]\", ' After step 6 the review appears in the \"Reviews\" list with its full text (no character cut off).')]:\n    steps = [star(4), 'Click in \"Your review *\" and press Ctrl+V.', nm(NAME), em(EMAIL), SUB]\n    if cid == \"TCD-09-04\":\n        steps += [APP, 'Find the new review in the \"Reviews\" list and compare its text with the clipboard text.']\n    T(cid, f\"Verify that a review text of exactly {what.strip('[]')} characters is accepted.\",\n      PRE_CLIP(f'A text of exactly {what} characters (letter \"a\" repeated; value set when Q-04 is answered)'),\n      steps, \"To be confirmed (Q-04): \" + OK + extra_exp)\n\n# ---------------- TR-10 ----------------\nT(\"TCD-10-01\", \"Verify that a review text of minimum - 1 characters is not submitted.\",\n  PRE_CLIP('A text of exactly [minimum - 1] characters (letter \"a\" repeated; value set when Q-04 is answered)'),\n  [star(4), 'Click in \"Your review *\" and press Ctrl+V.', nm(NAME), em(EMAIL), SUB],\n  'To be confirmed (Q-04, Q-20): ' + NOT + ' An error message names \"Your review\".')\nT(\"TCD-10-02\", \"Verify that typing stops at the maximum length in \\\"Your review *\\\".\",\n  PRE_CLIP('A text of exactly [maximum] characters (letter \"a\" repeated; value set when Q-04 is answered)'),\n  ['Click in \"Your review *\" and press Ctrl+V.', 'Press End, then type the letter \"b\" once.',\n   'Select all text in \"Your review *\" (Ctrl+A), copy it and count its characters (for example in a character counter tool).'],\n  'To be confirmed (Q-04, Q-18): \"Your review *\" holds exactly [maximum] characters and the typed \"b\" is not added.')\nT(\"TCD-10-03\", \"Verify that pasted text of maximum + 1 characters is cut at the maximum.\",\n  PRE_CLIP('A text of exactly [maximum + 1] characters (letter \"a\" repeated, last character \"b\"; value set when Q-04 is answered)'),\n  ['Click in \"Your review *\" and press Ctrl+V.',\n   'Select all text in \"Your review *\" (Ctrl+A), copy it and count its characters.'],\n  'To be confirmed (Q-04, Q-18): \"Your review *\" holds exactly [maximum] characters and the last character \"b\" is not in the box.')\nT(\"TCD-10-04\", \"Verify that pasting text ten times the maximum keeps the box at the maximum and the page usable.\",\n  PRE_CLIP('A text of about [maximum x 10] characters (value set when Q-04 is answered)'),\n  ['Click in \"Your review *\" and press Ctrl+V.', 'Click in \"Name *\" and type \"A\".',\n   'Select all text in \"Your review *\" (Ctrl+A), copy it and count its characters.'],\n  'To be confirmed (Q-04, Q-18): the page does not freeze (the \"A\" typed in step 2 appears in \"Name *\" at once) and \"Your review *\" holds at most [maximum] characters.')\n\n# ---------------- TR-11 ----------------\nT(\"TCD-11-01\", 'Verify that a review made only of spaces is not submitted.', PRE,\n  [star(4), 'Click in \"Your review *\" and press the Space bar 5 times.', nm(NAME), em(EMAIL), SUB],\n  'To be confirmed (Q-17, Q-20): ' + NOT + ' An error message names \"Your review\".', valid=True)\nT(\"TCD-11-02\", 'Verify that a review made only of line breaks is not submitted.', PRE,\n  [star(4), 'Click in \"Your review *\" and press Enter 3 times.', nm(NAME), em(EMAIL), SUB],\n  'To be confirmed (Q-17, Q-20): ' + NOT + ' An error message names \"Your review\".', valid=True)\nt = \"Space padded review.\"\nT(\"TCD-11-03\", \"Verify that leading and trailing spaces of a review are removed when shown.\", PRE,\n  [star(4), f'Enter \"   {t}   \" (3 spaces before and after) in \"Your review *\".', nm(NAME), em(EMAIL), SUB, APP,\n   find(t), 'Right-click the review text > Inspect, and read the text in the DevTools Elements panel.'],\n  f'To be confirmed (Q-17): the review text is \"{t}\" with no spaces before the first word or after the full stop.',\n  valid=True)\nT(\"TCD-11-04\", \"Verify that a review reaching the minimum length only through a trailing space is not submitted.\",\n  PRE_CLIP('A text of [minimum - 1] letters \"a\" followed by one space (value set when Q-04 is answered)'),\n  [star(4), 'Click in \"Your review *\" and press Ctrl+V.', nm(NAME), em(EMAIL), SUB],\n  'To be confirmed (Q-04, Q-17, Q-20): ' + NOT + ' An error message names \"Your review\".')\n\n# ---------------- TR-12 ----------------\ndef inj(cid, summary, review_val, name_val, exp):\n    T(cid, summary, PRE,\n      [star(4), rev(review_val), nm(name_val), em(EMAIL), SUB, APP, 'Look at the \"Reviews\" list.'], exp, valid=False)\ninj(\"TCD-12-01\", 'Verify that a script in \"Your review *\" is not run on submit or on the product page.',\n    \"<script>alert(1)</script>\", NAME,\n    'To be confirmed (Q-15): no alert dialog opens at any step; the review text is shown as plain text, removed, or the review is rejected, as confirmed for Q-15.')\ninj(\"TCD-12-02\", 'Verify that an HTML image tag with a script in \"Your review *\" is not run.',\n    \"<img src=x onerror=alert(1)>\", NAME,\n    'To be confirmed (Q-15): no alert dialog opens at any step and no image or broken-image icon appears in the \"Reviews\" list.')\ninj(\"TCD-12-03\", 'Verify that HTML formatting in \"Your review *\" is not rendered as HTML.',\n    \"<b>bold</b> text check\", NAME,\n    'To be confirmed (Q-15): the word \"bold\" is not shown in bold type; the text is shown as plain text \"<b>bold</b> text check\", with the tags removed, or the review is rejected, as confirmed for Q-15.')\ninj(\"TCD-12-04\", 'Verify that a web link in \"Your review *\" is not turned into a clickable link.',\n    \"Link check https://example.com\", NAME,\n    'To be confirmed (Q-15): in the \"Reviews\" list \"https://example.com\" is not a clickable link (the pointer does not change to a hand and clicking it opens nothing), or it is removed, or the review is rejected, as confirmed for Q-15.')\ninj(\"TCD-12-05\", 'Verify that a script in \"Name *\" is not run where the name is shown.',\n    \"Name script check.\", \"<script>alert(1)</script>\",\n    'To be confirmed (Q-05, Q-15): no alert dialog opens at any step; the name is shown as plain text, removed, or the review is rejected, as confirmed for Q-15.')\n\n# ---------------- TR-13 ----------------\nt = \"Pending check: other visitor.\"\nT(\"TCD-13-01\", \"Verify that a pending review is not shown to another visitor of the product page.\",\n  \"A build that stores reviews on a server; the product page open in Chrome session A and in a second session B (another Chrome profile).\",\n  [\"In session A: \" + star(4), \"In session A: \" + rev(t), \"In session A: \" + nm(NAME), \"In session A: \" + em(EMAIL),\n   \"In session A: \" + SUB, \"In session B: reload the product page.\", 'In session B: look at the \"Reviews\" list.'],\n  f'The review \"{t}\" is not in the \"Reviews\" list of session B.', valid=True)\nt = \"Pending check: page opened again.\"\nT(\"TCD-13-02\", \"Verify that a pending review is still not shown when the page is opened again later.\",\n  \"A build that keeps submitted reviews after the page is closed; the product page open in Chrome; no moderator action during the test.\",\n  fill(4, t) + [SUB, \"Close the browser tab.\", \"Open the product page again in a new tab.\", 'Look at the \"Reviews\" list.'],\n  f'The review \"{t}\" is not in the \"Reviews\" list.', valid=True)\n\n# ---------------- TR-14 ----------------\nt = \"Approval check: shown after approve.\"\nT(\"TCD-14-01\", \"Verify that a pending review appears on the product page after it is approved.\", PRE,\n  fill(4, t) + [SUB, APP, 'Look at the \"Reviews\" list.'],\n  f'The review \"{t}\" appears in the \"Reviews\" list.', valid=True)\nt = \"Approve twice check.\"\nT(\"TCD-14-02\", \"Verify that using the approve action twice shows an approved review only once.\", PRE,\n  fill(4, t) + [SUB, APP, APP, 'Count the reviews with the text \"' + t + '\" in the \"Reviews\" list.'],\n  f'The review \"{t}\" is shown exactly once in the \"Reviews\" list.', valid=True)\nT(\"TCD-14-03\", \"Verify that the approve action with no pending review adds no review.\", PRE,\n  ['Count the reviews in the \"Reviews\" list and write the number down.', APP,\n   'Count the reviews in the \"Reviews\" list again.'],\n  'The number of reviews in the \"Reviews\" list is the same as in step 1 and no new or empty review is shown.')\n\n# ---------------- TR-15 ----------------\nt = \"Reject check: must stay hidden.\"\nT(\"TCD-15-01\", \"Verify that a rejected review does not appear on the product page.\",\n  \"A build with a moderator reject action (moderation steps to be confirmed, Q-07); the product page open in Chrome.\",\n  fill(4, t) + [SUB, \"As moderator, reject the review in the moderation tool.\", \"Reload the product page.\",\n                'Look at the \"Reviews\" list.'],\n  f'The review \"{t}\" is not in the \"Reviews\" list.', valid=True)\nt1, t2 = \"Reject check: review A.\", \"Approve check: review B.\"\nT(\"TCD-15-02\", \"Verify that a rejected review stays hidden after other reviews are approved.\",\n  \"A build with a moderator reject action (Q-07); the product page open in Chrome.\",\n  fill(4, t1) + [SUB, f'As moderator, reject the review \"{t1}\".'] + fill(5, t2, \"Ben Carter\", \"ben.carter@example.com\")\n  + [SUB, f'As moderator, approve the review \"{t2}\".', \"Reload the product page.\", 'Look at the \"Reviews\" list.'],\n  f'The review \"{t1}\" is not in the \"Reviews\" list (the review \"{t2}\" is shown).', valid=True)\n\n# ---------------- TR-16 ----------------\nt = \"Author view: pending check.\"\nT(\"TCD-16-01\", \"Verify how the author sees their own pending review right after Submit.\", PRE,\n  fill(4, t) + [SUB, 'Look at the \"Reviews\" list.'],\n  f'To be confirmed (Q-08): either the review \"{t}\" is not in the \"Reviews\" list, or it is shown with a mark saying it awaits approval; it is never shown like an approved review without a mark.',\n  valid=True)\nt = \"Author view: approved check.\"\nT(\"TCD-16-02\", \"Verify that the author sees their approved review with no awaiting-approval mark.\", PRE,\n  fill(4, t) + [SUB, APP, find(t)],\n  f'To be confirmed (Q-08): the review \"{t}\" is shown like the other approved reviews, with no \"awaiting approval\" mark.',\n  valid=True)\n\n# ---------------- TR-17 ----------------\nt = \"Details check: all parts shown.\"\nT(\"TCD-17-01\", \"Verify that an approved review shows rating, reviewer name, date and text.\", PRE,\n  fill(4, t) + [SUB, APP, find(t)],\n  f'To be confirmed (Q-09): the review shows 4 of 5 stars, the name \"{NAME}\", a date and the text \"{t}\".', valid=True)\nt = \"Date check: submit date.\"\nT(\"TCD-17-02\", \"Verify that the date shown with a review is the submit date in an unambiguous format.\",\n  PRE + \" Today's date is written down.\",\n  fill(4, t) + [SUB, APP, find(t), \"Read the date shown with the review.\"],\n  \"To be confirmed (Q-24): the date shown is today's date (the submit date), written so that day and month cannot be mixed up (for example \\\"October 21, 2026\\\", not \\\"10/11/26\\\").\",\n  [\"Missing info: on demo-1.0 submit and approval happen on the same day, so submit date and approval date cannot be told apart (Q-24).\"],\n  valid=True)\nt = \"Name form check.\"\nT(\"TCD-17-03\", \"Verify that the reviewer name is shown in the confirmed form.\", PRE,\n  fill(4, t, \"Anna Smith\") + [SUB, APP, find(t), \"Read the reviewer name shown with the review.\"],\n  'To be confirmed (Q-09): the name is shown in the confirmed form: full name \"Anna Smith\", first name \"Anna\", or initials.',\n  valid=True)\n\n# ---------------- TR-18 ----------------\nt1, t2 = \"First review: too tight.\", \"Second review: perfect fit.\"\nT(\"TCD-18-01\", \"Verify that two reviews keep their own rating, name and text after approval.\", PRE,\n  fill(2, t1, \"Ben Carter\", \"ben.carter@example.com\") + [SUB,\n   'Clear \"Your review *\", \"Name *\" and \"Email *\" if they still contain text.']\n  + fill(5, t2, \"Chloe Diaz\", \"chloe.diaz@example.com\") + [SUB, APP, find(t1), find(t2)],\n  f'The review \"{t1}\" shows 2 stars and the name \"Ben Carter\"; the review \"{t2}\" shows 5 stars and the name \"Chloe Diaz\"; no value is swapped between them.',\n  [\"Assumption: the rating and the name are shown with each review (Q-09).\"], valid=True)\nt = \"Special name check.\"\nT(\"TCD-18-02\", \"Verify that a name with accent, apostrophe and hyphen is shown exactly as entered.\", PRE,\n  fill(4, t, \"Zoë O'Brien-Lê\") + [SUB, APP, find(t), \"Read the reviewer name shown with the review.\"],\n  \"To be confirmed (Q-05): the name is shown exactly as \\\"Zoë O'Brien-Lê\\\", with no encoded characters such as \\\"&#39;\\\" or \\\"&eacute;\\\".\",\n  valid=True)\nt = \"5 > 3 & \\\"good\\\" isn't it\"\nT(\"TCD-18-03\", \"Verify that the characters & < > \\\" ' in a review are shown exactly as typed.\", PRE,\n  fill(4, t) + [SUB, APP, 'Find the review starting with \"5 > 3\" in the \"Reviews\" list.'],\n  f\"To be confirmed (Q-15): the review text is shown exactly as {t!r}... \".replace(f\"{t!r}... \", f\"'{t}'\") + \", not as \\\"&gt;\\\", \\\"&amp;\\\", \\\"&quot;\\\" or \\\"&#39;\\\".\",\n  valid=True)\nT(\"TCD-18-04\", \"Verify that a maximum-length review of one long word does not break the layout.\",\n  PRE_CLIP('A text of exactly [maximum] letters \"a\" with no spaces (value set when Q-04 is answered)'),\n  [star(4), 'Click in \"Your review *\" and press Ctrl+V.', nm(NAME), em(EMAIL), SUB, APP,\n   'Find the new review in the \"Reviews\" list.'],\n  'To be confirmed (Q-04): the full text is shown, wrapped inside the \"Reviews\" section; the page has no horizontal scroll bar and the text does not overlap other elements.')\n\n# ---------------- TR-19 ----------------\nt = \"Email privacy check: visible page.\"\nT(\"TCD-19-01\", \"Verify that the reviewer's email is not shown anywhere on the visible product page.\", PRE,\n  fill(4, t, NAME, \"unique.reviewer@example.com\") + [SUB, APP,\n   'Press Ctrl+F and search for \"unique.reviewer\".', \"Check where each match is.\"],\n  'No match is in the \"Reviews\" list, the reviewer name or the rating summary (a match inside the \"Email *\" input itself, if the form keeps the value, does not count).',\n  [\"Risk: personal data could be shown publicly.\"], valid=True)\nt = \"Email privacy check: hidden parts.\"\nT(\"TCD-19-02\", \"Verify that the reviewer's email is not in hidden parts of the displayed review.\", PRE,\n  fill(4, t, NAME, \"unique.reviewer@example.com\") + [SUB, APP, find(t),\n   \"Hover over the reviewer name and wait 2 seconds.\", \"Right-click the reviewer name > Inspect.\",\n   'In the DevTools Elements panel press Ctrl+F and search for \"unique.reviewer\".'],\n  'No tooltip shows the email, the reviewer name is not a \"mailto:\" link, and the Elements search finds \"unique.reviewer\" only in the \"Email *\" input (if the form keeps the value), not in the \"Reviews\" section.',\n  valid=True)\n\n# ---------------- TR-20 ----------------\nPRE_LIST = PRE + ' At least 3 approved reviews with different dates and ratings are listed (initial data of demo-1.0).'\nT(\"TCD-20-01\", \"Verify that approved reviews are listed in the confirmed order.\", PRE_LIST,\n  ['Look at the \"Reviews\" list.', \"Write down the date and the rating of each review from top to bottom.\"],\n  \"To be confirmed (Q-10): the reviews are in the confirmed order (for example newest date first).\")\nt = \"Order check: newly approved.\"\nT(\"TCD-20-02\", \"Verify that a newly approved review appears in the position the order requires.\", PRE_LIST,\n  fill(4, t) + [SUB, APP, f'Note the position of the review \"{t}\" in the \"Reviews\" list.'],\n  f'To be confirmed (Q-10): the review \"{t}\" is in the position the confirmed order requires (for example first, if newest first).',\n  valid=True)\nt1, t2 = \"Tie check A.\", \"Tie check B.\"\nT(\"TCD-20-03\", \"Verify that two reviews with same date and rating keep a stable order on reopening.\",\n  \"A build that keeps reviews after the page is closed; the product page open in Chrome.\",\n  fill(4, t1) + [SUB, 'Clear \"Your review *\", \"Name *\" and \"Email *\" if they still contain text.']\n  + fill(4, t2, \"Ben Carter\", \"ben.carter@example.com\") + [SUB, APP,\n   f'Note the order of \"{t1}\" and \"{t2}\" in the \"Reviews\" list.', \"Close the tab and open the product page again.\",\n   f'Note the order of \"{t1}\" and \"{t2}\" again.'],\n  \"To be confirmed (Q-10): the two reviews are in the same order in steps 11 and 13, and that order follows the confirmed tie rule.\",\n  [BLK(\"a reload restores the initial data\")], valid=True)\n\n# ---------------- TR-21 ----------------\nT(\"TCD-21-01\", \"Verify that all 50 approved reviews of a product can be seen.\",\n  \"The product page open in Chrome with exactly 50 approved reviews (on demo-1.0: submit and approve 47 reviews in one session on top of the 3 initial ones, without reloading).\",\n  ['Scroll through the whole \"Reviews\" list.', \"Count the reviews shown.\"],\n  \"To be confirmed (Q-23): all 50 approved reviews are shown on the page (count = 50) with no paging control needed.\",\n  [\"Missing info: 50 reviews are entered by hand on demo-1.0; a test data set would help.\"])\nfor cid, cnt, exp in [\n    (\"TCD-21-02\", \"[page size - 1]\", 'all [page size - 1] reviews are on the first page and no paging control or \"Load more\" is shown.'),\n    (\"TCD-21-03\", \"[page size]\", 'all [page size] reviews are on the first page and no paging control or \"Load more\" is shown.'),\n    (\"TCD-21-04\", \"[page size + 1]\", 'the first page shows [page size] reviews and the last review is reached through the paging control or \"Load more\".')]:\n    T(cid, f\"Verify paging with exactly {cnt.strip('[]')} approved reviews.\",\n      f\"The product page open in Chrome with exactly {cnt} approved reviews (page size set when Q-23 is answered).\",\n      ['Look at the \"Reviews\" list and any paging control or \"Load more\" below it.', \"Count the reviews on the first page.\"],\n      f\"To be confirmed (Q-23): {exp}\",\n      [\"Missing info: if Q-23 confirms there is no paging, this case is dropped (covered by TCD-21-01).\"])\n\n# ---------------- TR-22 ----------------\nPRE0 = \"A product with 0 approved reviews open in Chrome.\"\nT(\"TCD-22-01\", \"Verify that a product with no approved reviews shows a no-reviews message.\", PRE0,\n  ['Look at the \"Reviews\" section.'],\n  \"To be confirmed (Q-25): a short message says there are no reviews yet, and no review is listed.\")\nt = \"Empty state check: pending only.\"\nT(\"TCD-22-02\", \"Verify that the no-reviews message stays while the only review is pending.\", PRE0,\n  fill(4, t) + [SUB, 'Look at the \"Reviews\" section.'],\n  \"To be confirmed (Q-25): the message saying there are no reviews yet is still shown and no review is listed.\",\n  valid=True)\nt = \"Empty state check: first approved.\"\nT(\"TCD-22-03\", \"Verify that the no-reviews message disappears when the first review is approved.\", PRE0,\n  fill(4, t) + [SUB, APP, 'Look at the \"Reviews\" section.'],\n  f'To be confirmed (Q-25): the no-reviews message is no longer shown and the review \"{t}\" is listed.', valid=True)\n\n# ---------------- TR-23 ----------------\nPRE_SUM = PRE + ' The rating summary next to the product name (average and count) and the ratings of all listed reviews are written down.'\nt = \"Summary check: approved 1 star.\"\nT(\"TCD-23-01\", \"Verify that an approved review is included in the average rating and review count.\", PRE_SUM,\n  fill(1, t) + [SUB, APP, \"Read the rating summary next to the product name.\"],\n  \"To be confirmed (Q-11): the review count is 1 higher than before, and the average equals the sum of all approved ratings (including the new 1) divided by the new count, rounded as confirmed.\",\n  valid=True)\nt = \"Summary check: pending 1 star.\"\nT(\"TCD-23-02\", \"Verify that a pending review does not change the average rating or review count.\", PRE_SUM,\n  fill(1, t) + [SUB, \"Read the rating summary next to the product name.\"],\n  \"To be confirmed (Q-11): the average rating and the review count are the same as written down before step 1.\",\n  valid=True)\nt = \"Summary check: rejected 1 star.\"\nT(\"TCD-23-03\", \"Verify that a rejected review does not change the average rating or review count.\",\n  \"A build with a moderator reject action (Q-07); the rating summary (average and count) written down.\",\n  fill(1, t) + [SUB, \"As moderator, reject the review.\", \"Reload the product page.\", \"Read the rating summary next to the product name.\"],\n  \"To be confirmed (Q-11): the average rating and the review count are the same as written down before step 1.\",\n  valid=True)\nt = \"Summary check: count.\"\nT(\"TCD-23-04\", \"Verify that the review count shown equals the number of approved reviews listed.\", PRE,\n  fill(4, t) + [SUB, APP, 'Count the reviews in the \"Reviews\" list.', \"Read the review count in the rating summary next to the product name.\"],\n  'To be confirmed (Q-11): the count in the rating summary equals the number of reviews counted in the \"Reviews\" list.',\n  valid=True)\nt = \"Rounding check: two stars.\"\nT(\"TCD-23-05\", \"Verify that an average falling exactly on a rounding step is shown with the confirmed rounding.\",\n  PRE + ' The \"Reviews\" list shows exactly 3 approved reviews rated 5, 4 and 3 (initial data; check before step 1).',\n  fill(2, t) + [SUB, APP, \"Read the average in the rating summary next to the product name.\"],\n  \"To be confirmed (Q-11): the approved ratings are 5, 4, 3 and 2 (exact average 3.5) and the average is shown as 3.5, or rounded as the confirmed rule says.\",\n  [\"Missing info: values next to the rounding step (for example 4.33) are added when Q-11 gives the rounding rule.\"],\n  valid=True)\nT(\"TCD-23-06\", \"Verify that the rating summary shows no wrong value when there are no approved reviews.\", PRE0,\n  [\"Read the rating summary next to the product name.\"],\n  'To be confirmed (Q-11, Q-25): the summary shows no average or an empty state; it never shows \"NaN\", \"0 stars\" or a number without reviews.')\n\n# ---------------- TR-24 ----------------\nPRE2 = \"A build with two products A and B; the page of product A open in Chrome.\"\nt = \"Product check: written for A.\"\nT(\"TCD-24-01\", \"Verify that a review approved for product A appears on product A's page.\", PRE2,\n  fill(4, t) + [SUB, \"As moderator, approve the review.\", \"Reload the page of product A.\", 'Look at the \"Reviews\" list.'],\n  f'The review \"{t}\" is in the \"Reviews\" list of product A.',\n  [\"Missing info: on demo-1.0 (one product) this is the same check as TC-14-01.\"], valid=True)\nt = \"Product check: not on B.\"\nT(\"TCD-24-02\", \"Verify that a review written for product A does not appear on product B's page.\", PRE2,\n  fill(4, t) + [SUB, \"As moderator, approve the review.\", \"Open the page of product B.\", 'Look at the \"Reviews\" list.'],\n  f'The review \"{t}\" is not in the \"Reviews\" list of product B.', valid=True)\n\n# ---------------- TR-25 ----------------\nT(\"TCD-25-01\", 'Verify that the form heading reads \"ADD A REVIEW\".', PRE,\n  ['Scroll to the review form.', \"Read the heading of the form.\"],\n  'The heading reads \"ADD A REVIEW\". To be confirmed (Q-32): the same words in other letter case (for example \"Add a review\") also pass.')\nT(\"TCD-25-02\", \"Verify that the info text above the form matches mockup-1.\", PRE,\n  ['Scroll to the review form.', \"Read the text under the form heading.\"],\n  'The text reads exactly \"Your email address will not be published. Required fields are marked *\".')\nT(\"TCD-25-03\", \"Verify that the four field labels are shown, each with the required marker *.\", PRE,\n  ['Scroll to the review form.', \"Read the label of each field.\"],\n  'The labels \"Your rating *\", \"Your review *\", \"Name *\" and \"Email *\" are shown, each ending with the required marker *.')\nT(\"TCD-25-04\", \"Verify that the save checkbox text matches mockup-1.\", PRE,\n  ['Scroll to the review form.', \"Read the text next to the checkbox.\"],\n  f'To be confirmed (Q-13): the text reads exactly {CB} (unless Q-13 removes \"website\").')\nT(\"TCD-25-05\", 'Verify that a \"Submit\" button is shown below the save checkbox.', PRE,\n  ['Scroll to the review form.', \"Look below the save checkbox.\"],\n  'A button labelled \"Submit\" is shown below the save checkbox.')\nT(\"TCD-25-06\", \"Verify that the form elements are in the mockup-1 order.\", PRE,\n  ['Scroll to the review form.', \"Write down the elements from top to bottom.\"],\n  'The order is: heading, info text, \"Your rating *\", \"Your review *\", \"Name *\", \"Email *\", save checkbox, \"Submit\".')\nT(\"TCD-25-07\", \"Verify that Tab moves through the form in screen order and Submit works by keyboard.\", PRE,\n  ['Click on the info text \"Your email address will not be published. Required fields are marked *\".',\n   \"Press Tab repeatedly and note which control gets the focus each time.\",\n   'When \"Submit\" has the focus, press Enter.'],\n  'To be confirmed (Q-34): the focus moves in this order: rating stars, \"Your review *\", \"Name *\", \"Email *\", save checkbox, \"Submit\"; pressing Enter on \"Submit\" submits the form (with empty fields: the form is checked and the review is not submitted).')\n\n# ---------------- TR-26 ----------------\nt = \"Permission check.\"\nT(\"TCD-26-01\", \"Verify that a signed-in customer who bought the product can submit a review.\",\n  \"A build with sign-in and orders; signed in as a test customer with a delivered order of this product; product page open.\",\n  fill(4, t) + [SUB],\n  \"To be confirmed (Q-01): \" + OK.replace(' and \"Pending approval\" changes from 0 to 1', \"\") + \" The review is waiting for approval.\",\n  [BLK(\"no sign-in or orders\", \"environment.md\")], valid=True)\nT(\"TCD-26-02\", \"Verify that a signed-in customer who did not buy the product cannot submit a review.\",\n  \"A build with sign-in and orders; signed in as a test customer with no order of this product; product page open.\",\n  ['Scroll to the review form.', \"If the form is shown and enabled: \" + \" \".join(fill(4, t)) + \" \" + SUB],\n  \"To be confirmed (Q-01): the form is hidden, or disabled, or Submit is rejected with a message; no review is created.\",\n  [BLK(\"no sign-in or orders\", \"environment.md\")], valid=True)\nT(\"TCD-26-03\", \"Verify that a guest (not signed in) cannot submit a review.\",\n  \"A build with sign-in; not signed in (guest); product page open.\",\n  ['Scroll to the review form.', \"If the form is shown and enabled: \" + \" \".join(fill(4, t)) + \" \" + SUB],\n  \"To be confirmed (Q-01): the form is hidden, or disabled, or Submit is rejected with a message; no review is created.\",\n  [\"Missing info: demo-1.0 has no sign-in, so every visitor is a guest; whether demo-1.0 should allow guests depends on Q-01.\"],\n  valid=True)\nT(\"TCD-26-04\", \"Verify review permission for a customer whose order was cancelled or refunded.\",\n  \"A build with sign-in and orders; signed in as a test customer whose only order of this product was cancelled or refunded; product page open.\",\n  ['Scroll to the review form.', \"If the form is shown and enabled: \" + \" \".join(fill(4, t)) + \" \" + SUB],\n  \"To be confirmed (Q-01, Q-33): the customer can or cannot submit, as confirmed; if not, the form is hidden, disabled or Submit is rejected with a message.\",\n  [BLK(\"no sign-in or orders\", \"environment.md\")], valid=True)\n\n# ---------------- TR-27 ----------------\nT(\"TCD-27-01\", \"Verify how Name and Email are handled for a signed-in customer.\",\n  'A build with sign-in; signed in as test customer \"Anna Smith\" (anna.smith@example.com); product page open.',\n  ['Scroll to the review form.', 'Look at \"Name *\" and \"Email *\".'],\n  \"To be confirmed (Q-02): Name and Email are prefilled from the account, or prefilled and editable, or not shown, as confirmed.\",\n  [BLK(\"no sign-in\", \"environment.md\")])\nt = \"Edited name check.\"\nT(\"TCD-27-02\", \"Verify which name is displayed when a signed-in customer edits a prefilled Name.\",\n  'A build with sign-in where Name is prefilled and editable (Q-02); signed in as test customer \"Anna Smith\"; product page open.',\n  [star(4), rev(t), 'Replace the text in \"Name *\" with \"Anna S.\"', SUB, \"As moderator, approve the review.\",\n   \"Reload the product page.\", find(t)],\n  'To be confirmed (Q-02): the review shows the name confirmed for Q-02 (\"Anna S.\" if the edited name is used, \"Anna Smith\" if the account name is used).',\n  [BLK(\"no sign-in\", \"environment.md\")])\n\n# ---------------- TR-28 ----------------\nT(\"TCD-28-01\", 'Verify that the review is not submitted when \"Name *\" is empty.', PRE,\n  [star(4), rev(TXT), 'Leave \"Name *\" empty.', em(EMAIL), SUB],\n  NOT + ' To be confirmed (Q-20): an error message names \"Name\".', valid=True)\n\n# ---------------- TR-29 ----------------\ndef name_case(cid, summary, value, exp, extra=None, pre=PRE, steps_name=None):\n    steps = [star(4), rev(f\"Name check {cid[-5:]}.\"), steps_name or nm(value), em(EMAIL), SUB]\n    T(cid, summary, pre, steps, exp, extra, valid=True)\nname_case(\"TCD-29-01\", 'Verify that a Name of Latin letters and a space is accepted.', \"Anna Smith\",\n          \"To be confirmed (Q-05): \" + OK)\nname_case(\"TCD-29-02\", 'Verify that a Name with accented letters is accepted.', \"Zoë Lê\",\n          \"To be confirmed (Q-05): \" + OK)\nname_case(\"TCD-29-03\", 'Verify that a Name with a hyphen and an apostrophe is accepted.', \"Mary-Jane O'Neil\",\n          \"To be confirmed (Q-05): \" + OK)\nname_case(\"TCD-29-04\", 'Verify whether a Name in a non-Latin script is accepted.', \"李明\",\n          'To be confirmed (Q-05): either the review is submitted (confirmation message, \"Pending approval\" 1) or it is rejected with an error naming \"Name\", as confirmed.')\nname_case(\"TCD-29-05\", 'Verify whether a Name containing digits is accepted.', \"Anna2\",\n          'To be confirmed (Q-05): either the review is submitted (confirmation message, \"Pending approval\" 1) or it is rejected with an error naming \"Name\", as confirmed.')\nname_case(\"TCD-29-06\", 'Verify that a Name made only of symbols is rejected.', \"@#$%\",\n          'To be confirmed (Q-05, Q-20): ' + NOT + ' An error message names \"Name\".')\nname_case(\"TCD-29-07\", 'Verify that a Name of 1 character is accepted.', \"A\",\n          \"To be confirmed (Q-05): \" + OK)\nfor cid, what, exp in [(\"TCD-29-08\", \"[maximum - 1]\", \"To be confirmed (Q-05): \" + OK),\n                       (\"TCD-29-09\", \"[maximum]\", \"To be confirmed (Q-05): \" + OK + ' After approval the full name is shown with the review.'),\n                       (\"TCD-29-10\", \"[maximum + 1]\", 'To be confirmed (Q-05, Q-18): either \"Name *\" stops at [maximum] characters, or the review is not submitted and an error message names \"Name\".')]:\n    T(cid, f\"Verify the Name length of exactly {what.strip('[]')} characters.\",\n      PRE_CLIP(f'A name of exactly {what} letters \"a\" (value set when Q-05 is answered)'),\n      [star(4), rev(f\"Name length check {cid[-5:]}.\"), 'Click in \"Name *\" and press Ctrl+V.', em(EMAIL), SUB]\n      + ([APP, 'Find the review \"Name length check 29-09.\" in the \"Reviews\" list.'] if cid == \"TCD-29-09\" else []),\n      exp, valid=True)\n\n# ---------------- TR-30 ----------------\nT(\"TCD-30-01\", 'Verify that the review is not submitted when \"Email *\" is empty.', PRE,\n  [star(4), rev(TXT), nm(NAME), 'Leave \"Email *\" empty.', SUB],\n  NOT + ' To be confirmed (Q-20): an error message names \"Email\".', valid=True)\n\n# ---------------- TR-31 ----------------\ndef email_case(cid, summary, value, good):\n    exp = (\"To be confirmed (Q-06): \" + OK) if good else ('To be confirmed (Q-06, Q-20): ' + NOT + ' An error message names \"Email\".')\n    T(cid, summary, PRE, [star(4), rev(f\"Email check {cid[-5:]}.\"), nm(NAME), em(value), SUB], exp, valid=True)\nemail_case(\"TCD-31-01\", 'Verify that the email \"anna.smith@example.com\" is accepted.', \"anna.smith@example.com\", True)\nemail_case(\"TCD-31-02\", 'Verify that an email with a plus sign and a sub-domain is accepted.', \"anna+shop@mail.example.co.uk\", True)\nemail_case(\"TCD-31-03\", 'Verify that an email without \"@\" is rejected.', \"anna.example.com\", False)\nemail_case(\"TCD-31-04\", 'Verify that an email with nothing before \"@\" is rejected.', \"@example.com\", False)\nemail_case(\"TCD-31-05\", 'Verify that an email with no domain after \"@\" is rejected.', \"anna@\", False)\nemail_case(\"TCD-31-06\", 'Verify that an email without a top-level domain is rejected.', \"anna@example\", False)\nemail_case(\"TCD-31-07\", 'Verify that an email with two \"@\" is rejected.', \"anna@@example.com\", False)\nemail_case(\"TCD-31-08\", 'Verify that an email with a space inside is rejected.', \"anna smith@example.com\", False)\nemail_case(\"TCD-31-09\", 'Verify that an email in upper case is accepted.', \"ANNA@EXAMPLE.COM\", True)\nfor cid, what, exp in [(\"TCD-31-10\", \"[maximum - 1]\", \"To be confirmed (Q-06): \" + OK),\n                       (\"TCD-31-11\", \"[maximum]\", \"To be confirmed (Q-06): \" + OK),\n                       (\"TCD-31-12\", \"[maximum + 1]\", 'To be confirmed (Q-06, Q-18): either \"Email *\" stops at [maximum] characters, or the review is not submitted and an error message names \"Email\".')]:\n    T(cid, f\"Verify the Email length of exactly {what.strip('[]')} characters.\",\n      PRE_CLIP(f'An email of exactly {what} characters: letters \"a\" followed by \"@example.com\" (value set when Q-06 is answered)'),\n      [star(4), rev(f\"Email length check {cid[-5:]}.\"), nm(NAME), 'Click in \"Email *\" and press Ctrl+V.', SUB],\n      exp, valid=True)\n\n# ---------------- TR-32 ----------------\nt = \"Name trim check.\"\nT(\"TCD-32-01\", \"Verify that leading and trailing spaces in Name are removed when shown.\", PRE,\n  [star(4), rev(t), 'Enter \"  Anna Smith  \" (2 spaces before and after) in \"Name *\".', em(EMAIL), SUB, APP, find(t),\n   'Right-click the reviewer name > Inspect, and read the name in the DevTools Elements panel.'],\n  'To be confirmed (Q-17): the review is accepted and the name is shown as \"Anna Smith\", with no spaces before or after it.',\n  valid=True)\nT(\"TCD-32-02\", \"Verify that a Name made only of spaces is treated as empty.\", PRE,\n  [star(4), rev(TXT), 'Click in \"Name *\" and press the Space bar 5 times.', em(EMAIL), SUB],\n  'To be confirmed (Q-17, Q-20): ' + NOT + ' An error message names \"Name\".', valid=True)\nT(\"TCD-32-03\", \"Verify that an Email with leading and trailing spaces is accepted.\", PRE,\n  [star(4), rev(\"Email trim check.\"), nm(NAME), 'Enter \"  anna@example.com  \" (2 spaces before and after) in \"Email *\".', SUB],\n  \"To be confirmed (Q-17): \" + OK, valid=True)\nT(\"TCD-32-04\", \"Verify that an Email made only of spaces is treated as empty.\", PRE,\n  [star(4), rev(TXT), nm(NAME), 'Click in \"Email *\" and press the Space bar 5 times.', SUB],\n  'To be confirmed (Q-17, Q-20): ' + NOT + ' An error message names \"Email\".', valid=True)\n\n# ---------------- TR-33 ----------------\nCONF = ' To be confirmed (Q-21): the message says the review was received and waits for approval.'\nT(\"TCD-33-01\", \"Verify that a valid review is submitted with the save checkbox not ticked.\", PRE_CLEAN,\n  fill(4, TXT) + [f\"Leave the checkbox {CB} not ticked.\", SUB],\n  OK + CONF, valid=True)\nT(\"TCD-33-02\", \"Verify that a valid review is submitted with the save checkbox ticked.\", PRE_CLEAN,\n  fill(4, TXT) + [SAVE, SUB],\n  OK + CONF, valid=True)\n\n# ---------------- TR-34 ----------------\nT(\"TCD-34-01\", \"Verify that submitting an empty form names all four required fields.\", PRE,\n  ['Leave \"Your rating *\", \"Your review *\", \"Name *\" and \"Email *\" empty.', SUB],\n  NOT + ' To be confirmed (Q-20): the error messages name all four fields: rating, \"Your review\", \"Name\" and \"Email\".')\nT(\"TCD-34-02\", \"Verify that only the empty rating and review are named when Name and Email are valid.\", PRE,\n  ['Leave \"Your rating *\" and \"Your review *\" empty.', nm(NAME), em(EMAIL), SUB],\n  NOT + ' To be confirmed (Q-20): the error messages name the rating and \"Your review\" only; \"Name\" and \"Email\" are not named.',\n  valid=True)\nT(\"TCD-34-03\", \"Verify that entered values are kept after a rejected Submit and correction submits.\", PRE,\n  [star(4), 'Leave \"Your review *\" empty.', nm(NAME), em(EMAIL), SUB,\n   'Check that the rating, \"Name *\" and \"Email *\" still hold the values entered.', rev(TXT), SUB],\n  'To be confirmed (Q-38): after step 5 the 4 stars, \"Anna Smith\" and \"anna.smith@example.com\" are still in the form, and after step 7 ' + OK[0].lower() + OK[1:],\n  valid=True)\nT(\"TCD-34-04\", \"Verify that leaving a required field empty shows no error until Submit.\", PRE,\n  ['Click in \"Name *\".', \"Press Tab to move to \\\"Email *\\\" without typing.\", 'Look at the form and the area above it.'],\n  'To be confirmed (Q-19): no error message is shown for \"Name\" (or any field) before \"Submit\" is clicked.')\n\n# ---------------- TR-35 ----------------\nT(\"TCD-35-01\", \"Verify that the form is fully cleared after a successful Submit without saving.\", PRE_CLEAN,\n  fill(4, TXT) + [f\"Leave the checkbox {CB} not ticked.\", SUB, \"Look at the page and the form.\"],\n  'To be confirmed (Q-22): the product page stays open (product name and \"Reviews\" still shown, no new page), no star is selected, and \"Your review *\", \"Name *\" and \"Email *\" are empty.',\n  valid=True)\nT(\"TCD-35-02\", \"Verify that Name and Email stay filled after a successful Submit with saving ticked.\", PRE_CLEAN,\n  fill(4, TXT) + [SAVE, SUB, \"Look at the page and the form.\"],\n  'To be confirmed (Q-22): the product page stays open, no star is selected, \"Your review *\" is empty, and \"Name *\" and \"Email *\" still show \"Anna Smith\" and \"anna.smith@example.com\".',\n  valid=True)\n\n# ---------------- TR-36 ----------------\nT(\"TCD-36-01\", \"Verify that the save checkbox is not ticked on a first visit.\", PRE_CLEAN,\n  ['Scroll to the review form.', f\"Look at the checkbox {CB}\"],\n  \"The checkbox is not ticked.\")\nT(\"TCD-36-02\", \"Verify the save checkbox state on a return visit after Name and Email were saved.\", PRE_CLEAN,\n  fill(4, \"Return visit check.\") + [SAVE, SUB, \"Reload the page (F5).\", f\"Look at the checkbox {CB}\"],\n  \"To be confirmed (Q-14): the checkbox is ticked or not ticked, as confirmed.\", valid=True)\n\n# ---------------- TR-37 ----------------\nT(\"TCD-37-01\", \"Verify that ticked saving refills Name and Email on the next visit.\", PRE_CLEAN,\n  fill(4, \"Save check: first visit.\") + [SAVE, SUB, \"Close the tab and open exam/app/index.html again in the same Chrome window.\",\n                                         'Look at \"Name *\" and \"Email *\".'],\n  '\"Name *\" shows \"Anna Smith\" and \"Email *\" shows \"anna.smith@example.com\".', valid=True)\nT(\"TCD-37-02\", \"Verify that a new ticked Submit replaces the saved Name and Email.\",\n  PRE + ' Name \"Anna Smith\" and Email \"anna.smith@example.com\" are saved in this browser (TC-37-01 done; they are filled on load).',\n  [star(4), rev(\"Save check: replace.\"), 'Replace the text in \"Name *\" with \"Ben Carter\".',\n   'Replace the text in \"Email *\" with \"ben.carter@example.com\".', SAVE + \" (tick it if it is not ticked)\", SUB,\n   \"Reload the page (F5).\", 'Look at \"Name *\" and \"Email *\".'],\n  'To be confirmed (Q-14): \"Name *\" shows \"Ben Carter\" and \"Email *\" shows \"ben.carter@example.com\".', valid=True)\nT(\"TCD-37-03\", \"Verify what happens to saved data after a Submit with the box not ticked.\",\n  PRE + ' Name \"Anna Smith\" and Email \"anna.smith@example.com\" are saved in this browser (they are filled on load).',\n  [star(4), rev(\"Save check: untick.\"), f\"Untick the checkbox {CB} if it is ticked.\", SUB, \"Reload the page (F5).\",\n   'Look at \"Name *\" and \"Email *\".'],\n  'To be confirmed (Q-14): \"Name *\" and \"Email *\" are filled or empty, as confirmed for Q-14.', valid=True)\nT(\"TCD-37-04\", \"Verify that only Name and Email are refilled, not rating or review.\", PRE_CLEAN,\n  fill(4, \"Save check: only name and email.\") + [SAVE, SUB, \"Reload the page (F5).\", \"Look at the whole form.\"],\n  'To be confirmed (Q-13, Q-14): only \"Name *\" and \"Email *\" are filled; no star is selected and \"Your review *\" is empty.',\n  valid=True)\nT(\"TCD-37-05\", \"Verify that saved Name and Email are not filled in a private window.\", PRE_CLEAN,\n  fill(4, \"Save check: private window.\") + [SAVE, SUB, \"Open a Chrome Incognito window (Ctrl+Shift+N).\",\n   \"Open exam/app/index.html in the Incognito window.\", 'Look at \"Name *\" and \"Email *\".'],\n  '\"Name *\" and \"Email *\" are empty in the Incognito window.', valid=True)\nT(\"TCD-37-06\", \"Verify that nothing is saved when Submit is rejected with the box ticked.\", PRE_CLEAN,\n  [star(4), 'Leave \"Your review *\" empty.', nm(NAME), em(EMAIL), SAVE, SUB, \"Reload the page (F5).\",\n   'Look at \"Name *\" and \"Email *\".'],\n  'To be confirmed (Q-14): \"Name *\" and \"Email *\" are empty.', valid=True)\n\n# ---------------- TR-38 ----------------\nT(\"TCD-38-01\", \"Verify that Name and Email are not kept when the box is not ticked.\", PRE_CLEAN,\n  fill(4, \"No save check.\") + [f\"Leave the checkbox {CB} not ticked.\", SUB, \"Reload the page (F5).\",\n   'Look at \"Name *\" and \"Email *\".'],\n  'To be confirmed (Q-14): \"Name *\" and \"Email *\" are empty.', valid=True)\nT(\"TCD-38-02\", \"Verify that typed but unsubmitted Name and Email are not kept after reload.\",\n  PRE_CLEAN + \" Chrome autofill of addresses is switched off (Settings > Autofill and passwords > Addresses and more).\",\n  [nm(NAME), em(EMAIL), \"Reload the page (F5) without clicking \\\"Submit\\\".\", 'Look at \"Name *\" and \"Email *\".'],\n  'To be confirmed (Q-14): \"Name *\" and \"Email *\" are empty.')\n\n# ---------------- TR-39 ----------------\nT(\"TCD-39-01\", \"Verify that a customer below the review limit can submit another review.\",\n  \"The customer (Name \\\"Anna Smith\\\", Email \\\"anna.smith@example.com\\\") already has [limit - 1] reviews for this product (limit set when Q-12 is answered); product page open.\",\n  fill(4, \"Limit check: below limit.\") + [SUB],\n  \"To be confirmed (Q-12): \" + OK.replace(\"changes from 0 to 1\", \"increases by 1\"),\n  [\"Missing info: if the limit is 1, this is the first review (TC-33-01) and the case is dropped.\"], valid=True)\nT(\"TCD-39-02\", \"Verify that a customer at the review limit cannot submit one more review.\",\n  \"The customer (Name \\\"Anna Smith\\\", Email \\\"anna.smith@example.com\\\") already has [limit] reviews for this product (Q-12); product page open.\",\n  fill(4, \"Limit check: above limit.\") + [SUB],\n  \"To be confirmed (Q-12): the review is not submitted (\\\"Pending approval\\\" does not increase) and the message confirmed for Q-12 is shown.\",\n  valid=True)\nT(\"TCD-39-03\", \"Verify that a customer at the limit for product A can review product B.\",\n  \"A build with two products; the customer already has [limit] reviews for product A (Q-12); page of product B open.\",\n  fill(4, \"Limit check: other product.\") + [SUB],\n  \"To be confirmed (Q-12): the review is submitted: a confirmation message appears and the review waits for approval.\",\n  valid=True)\nT(\"TCD-39-04\", \"Verify that the review limit cannot be bypassed by changing Name and Email.\",\n  \"The customer already has [limit] reviews for this product (Q-12); product page open.\",\n  fill(4, \"Limit check: other identity.\", \"Ben Carter\", \"ben.carter@example.com\") + [SUB],\n  \"To be confirmed (Q-01, Q-02, Q-12): the customer is still recognised and the review is not submitted; the message confirmed for Q-12 is shown.\",\n  valid=True)\n\n# ---------------- TR-40 ----------------\nt = \"Double click check.\"\nT(\"TCD-40-01\", \"Verify that double-clicking Submit creates only one review.\", PRE,\n  fill(4, t) + ['Double-click \"Submit\" quickly.', 'Read \"Pending approval\".', APP, f'Count the reviews \"{t}\" in the \"Reviews\" list.'],\n  f'To be confirmed (Q-28): \"Pending approval\" shows 1 (not 2) and the review \"{t}\" appears exactly once after approval.',\n  valid=True)\nt = \"Click and Enter check.\"\nT(\"TCD-40-02\", \"Verify that clicking Submit then pressing Enter quickly creates only one review.\", PRE,\n  fill(4, t) + [SUB + ' Immediately click in \"Name *\" and press Enter.', 'Read \"Pending approval\".', APP,\n                f'Count the reviews \"{t}\" in the \"Reviews\" list.'],\n  f'To be confirmed (Q-28): \"Pending approval\" shows 1 and the review \"{t}\" appears exactly once after approval.',\n  valid=True)\nt = \"Reload after submit check.\"\nT(\"TCD-40-03\", \"Verify that reloading right after a successful Submit creates no second review.\",\n  \"A build that keeps reviews after reload; product page open in Chrome.\",\n  fill(4, t) + [SUB, \"As soon as the confirmation appears, reload the page (F5); if Chrome asks to resend the form, click Continue.\",\n                \"As moderator, approve pending reviews.\", f'Count the reviews \"{t}\" in the \"Reviews\" list.'],\n  f'To be confirmed (Q-28): the review \"{t}\" appears exactly once.',\n  [\"Missing info: on demo-1.0 a reload restores the initial data, so this check is not meaningful there; run it on a build that keeps data.\"],\n  valid=True)\nt = \"Back and forward check.\"\nT(\"TCD-40-04\", \"Verify that browser Back then Forward after Submit creates no second review.\",\n  \"A build that keeps reviews; product page reached from another page (so Back is available); product page open in Chrome.\",\n  fill(4, t) + [SUB, \"Click the browser Back button.\", \"Click the browser Forward button.\",\n                \"As moderator, approve pending reviews.\", f'Count the reviews \"{t}\" in the \"Reviews\" list.'],\n  f'To be confirmed (Q-28): the review \"{t}\" appears exactly once.',\n  [\"Missing info: on demo-1.0 Back/Forward reloads the page and restores the initial data; run it on a build that keeps data.\"],\n  valid=True)\n\n# ---------------- TR-41 ----------------\nKEEP = 'a message says the review was not submitted, and the rating (4 stars), \"Your review *\", \"Name *\" and \"Email *\" still hold the entered values.'\nT(\"TCD-41-01\", \"Verify that a lost network connection on Submit is reported and data is kept.\",\n  \"A build with a server; product page open in Chrome with DevTools (F12) open on the Network tab.\",\n  fill(4, \"Network loss check.\") + ['In DevTools > Network set throttling to \"Offline\".', SUB],\n  \"To be confirmed (Q-29): \" + KEEP, valid=True)\nT(\"TCD-41-02\", \"Verify that a server error on Submit is reported and data is kept.\",\n  \"A build with a server set up (by the test team) to return an error on saving a review; product page open in Chrome.\",\n  fill(4, \"Server error check.\") + [SUB],\n  \"To be confirmed (Q-29): \" + KEEP, [BLK(\"no server\")], valid=True)\nT(\"TCD-41-03\", \"Verify that an expired session on Submit is reported and data is not lost.\",\n  \"A build with sign-in; signed in as a test customer; session expired before Submit (for example by signing out in another tab).\",\n  fill(4, \"Session expiry check.\") + [SUB],\n  \"To be confirmed (Q-29): the customer is told the session expired and the entered rating, review, Name and Email are not lost.\",\n  valid=True)\nt = \"Retry after failure check.\"\nT(\"TCD-41-04\", \"Verify that resubmitting after a failed Submit creates exactly one review.\",\n  \"A build with a server; product page open in Chrome with DevTools (F12) open on the Network tab.\",\n  fill(4, t) + ['In DevTools > Network set throttling to \"Offline\".', SUB,\n                'Set throttling back to \"No throttling\".', SUB, \"As moderator, approve pending reviews.\",\n                f'Count the reviews \"{t}\" in the \"Reviews\" list.'],\n  f'To be confirmed (Q-28, Q-29): the review \"{t}\" appears exactly once.',\n  [BLK(\"no server or network\")], valid=True)\n\n# ---------- build rows ----------\nby_cid = {}\nfor tc in TCS:\n    assert tc[\"cid\"] not in by_cid, tc[\"cid\"]\n    by_cid[tc[\"cid\"]] = tc\nmissing = [c for c in conds if c not in by_cid]\nextra = [c for c in by_cid if c not in conds]\nassert not missing and not extra, (missing, extra)\nbad_tr = [c for c, d in conds.items() if d[\"tr\"] not in tr_ids]\nassert not bad_tr, bad_tr\n\nQRE = re.compile(r\"To be confirmed \\(([^)]*)\\)\")\nrows = []\ncounter = collections.Counter()\nfor cid, d in conds.items():\n    tc = by_cid[cid]\n    tr = d[\"tr\"]\n    counter[tr] += 1\n    tcid = f\"TC-{tr[3:]}-{counter[tr]:02d}\"\n    tc[\"tcid\"] = tcid\n    notes = [f\"Condition: {cid}\", f\"Technique: {d['tech']}\"] + d[\"notes\"] + tc[\"extra\"]\n    # Every TBC needs a Missing info note naming its question IDs\n    m = QRE.search(tc[\"expected\"])\n    if m:\n        qs = [q.strip() for q in m.group(1).split(\",\")]\n        mi = \" \".join(n for n in notes if n.startswith(\"Missing info\"))\n        lacking = [q for q in qs if q not in mi]\n        if lacking:\n            notes.append(f\"Missing info: expected result not stated in any source ({', '.join(lacking)}).\")\n        tc[\"tbc\"] = qs\n    else:\n        tc[\"tbc\"] = []\n    # de-duplicate notes, keep order\n    seen = set(); notes = [n for n in notes if not (n in seen or seen.add(n))]\n    tc[\"notes\"] = notes\n    steps = \"\\n\".join(f\"{i}. {s}\" for i, s in enumerate(tc[\"steps\"], 1))\n    rows.append((tr, tcid, tc[\"summary\"], tc[\"pre\"], steps, tc[\"expected\"], \"\\n\".join(notes)))\n\nrows.sort(key=lambda r: (r[0], r[1]))\n\n# ---------- export ----------\nshutil.copyfile(TEMPLATE, OUT)\nwb = openpyxl.load_workbook(OUT)\nws = wb[\"Test Cases\"]\nal = Alignment(wrap_text=True, vertical=\"top\")\nfor r in rows:\n    ws.append(r)\nfor row in ws.iter_rows(min_row=2):\n    for c in row:\n        c.alignment = al\nwb.save(OUT)\n\n# ---------- report data ----------\nimport json\nrep = dict(per_tr=collections.Counter(r[0] for r in rows), total=len(rows),\n           tbc=collections.defaultdict(list), assumptions=collections.defaultdict(list),\n           vague=[], long_summary=[])\nfor tc in TCS:\n    for q in tc[\"tbc\"]:\n        rep[\"tbc\"][q].append(tc[\"tcid\"])\n    for n in tc[\"notes\"]:\n        if n.startswith(\"Assumption\"):\n            rep[\"assumptions\"][n].append(tc[\"tcid\"])\n    if len(tc[\"summary\"].split()) > 16:\n        rep[\"long_summary\"].append((tc[\"tcid\"], len(tc[\"summary\"].split())))\n    for bad in [\"works normally\", \"as expected\", \"error is shown\", \"handles it correctly\"]:\n        if bad in tc[\"expected\"]:\n            rep[\"vague\"].append(tc[\"tcid\"])\nprint(json.dumps(rep, indent=1, ensure_ascii=False, default=list))\n"
}
```

## Tool (2026-10-21T04:16:56)

```
File created successfully at: C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\gen_tc.py (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:17:02)

**Tool call `Edit`:**

```json
{
  "replace_all": false,
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\gen_tc.py",
  "old_string": "  f\"To be confirmed (Q-15): the review text is shown exactly as {t!r}... \".replace(f\"{t!r}... \", f\"'{t}'\") + \", not as \\\"&gt;\\\", \\\"&amp;\\\", \\\"&quot;\\\" or \\\"&#39;\\\".\",",
  "new_string": "  \"To be confirmed (Q-15): the review text is shown exactly as typed in step 2, with no \\\"&gt;\\\", \\\"&amp;\\\", \\\"&quot;\\\" or \\\"&#39;\\\" in place of the characters.\","
}
```

## Tool (2026-10-21T04:17:02)

```
The file C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\gen_tc.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:17:04)

**Tool call `Bash`:**

```json
{
  "command": "cd \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\" && PYTHONIOENCODING=utf-8 python -I gen_tc.py",
  "description": "Generate test cases and export xlsx"
}
```

## Tool (2026-10-21T04:17:06)

```
{
 "per_tr": {
  "TR-01": 1,
  "TR-02": 4,
  "TR-03": 4,
  "TR-04": 5,
  "TR-05": 1,
  "TR-06": 2,
  "TR-07": 1,
  "TR-08": 3,
  "TR-09": 4,
  "TR-10": 4,
  "TR-11": 4,
  "TR-12": 5,
  "TR-13": 2,
  "TR-14": 3,
  "TR-15": 2,
  "TR-16": 2,
  "TR-17": 3,
  "TR-18": 4,
  "TR-19": 2,
  "TR-20": 3,
  "TR-21": 4,
  "TR-22": 3,
  "TR-23": 6,
  "TR-24": 2,
  "TR-25": 7,
  "TR-26": 4,
  "TR-27": 2,
  "TR-28": 1,
  "TR-29": 10,
  "TR-30": 1,
  "TR-31": 12,
  "TR-32": 4,
  "TR-33": 2,
  "TR-34": 4,
  "TR-35": 2,
  "TR-36": 2,
  "TR-37": 6,
  "TR-38": 2,
  "TR-39": 4,
  "TR-40": 4,
  "TR-41": 4
 },
 "total": 145,
 "tbc": {
  "Q-03": [
   "TC-02-02",
   "TC-03-01",
   "TC-03-02",
   "TC-03-03",
   "TC-03-04"
  ],
  "Q-36": [
   "TC-02-03"
  ],
  "Q-34": [
   "TC-02-04",
   "TC-25-07"
  ],
  "Q-09": [
   "TC-03-01",
   "TC-03-02",
   "TC-03-03",
   "TC-03-04",
   "TC-04-05",
   "TC-17-01",
   "TC-17-03"
  ],
  "Q-16": [
   "TC-04-01",
   "TC-04-02",
   "TC-04-03"
  ],
  "Q-20": [
   "TC-05-01",
   "TC-07-01",
   "TC-10-01",
   "TC-11-01",
   "TC-11-02",
   "TC-11-04",
   "TC-28-01",
   "TC-29-06",
   "TC-30-01",
   "TC-31-03",
   "TC-31-04",
   "TC-31-05",
   "TC-31-06",
   "TC-31-07",
   "TC-31-08",
   "TC-32-02",
   "TC-32-04",
   "TC-34-01",
   "TC-34-02"
  ],
  "Q-35": [
   "TC-06-02"
  ],
  "Q-37": [
   "TC-08-02"
  ],
  "Q-04": [
   "TC-09-01",
   "TC-09-02",
   "TC-09-03",
   "TC-09-04",
   "TC-10-01",
   "TC-10-02",
   "TC-10-03",
   "TC-10-04",
   "TC-11-04",
   "TC-18-04"
  ],
  "Q-18": [
   "TC-10-02",
   "TC-10-03",
   "TC-10-04",
   "TC-29-10",
   "TC-31-12"
  ],
  "Q-17": [
   "TC-11-01",
   "TC-11-02",
   "TC-11-03",
   "TC-11-04",
   "TC-32-01",
   "TC-32-02",
   "TC-32-03",
   "TC-32-04"
  ],
  "Q-15": [
   "TC-12-01",
   "TC-12-02",
   "TC-12-03",
   "TC-12-04",
   "TC-12-05",
   "TC-18-03"
  ],
  "Q-05": [
   "TC-12-05",
   "TC-18-02",
   "TC-29-01",
   "TC-29-02",
   "TC-29-03",
   "TC-29-04",
   "TC-29-05",
   "TC-29-06",
   "TC-29-07",
   "TC-29-08",
   "TC-29-09",
   "TC-29-10"
  ],
  "Q-08": [
   "TC-16-01",
   "TC-16-02"
  ],
  "Q-24": [
   "TC-17-02"
  ],
  "Q-10": [
   "TC-20-01",
   "TC-20-02",
   "TC-20-03"
  ],
  "Q-23": [
   "TC-21-01",
   "TC-21-02",
   "TC-21-03",
   "TC-21-04"
  ],
  "Q-25": [
   "TC-22-01",
   "TC-22-02",
   "TC-22-03",
   "TC-23-06"
  ],
  "Q-11": [
   "TC-23-01",
   "TC-23-02",
   "TC-23-03",
   "TC-23-04",
   "TC-23-05",
   "TC-23-06"
  ],
  "Q-32": [
   "TC-25-01"
  ],
  "Q-13": [
   "TC-25-04",
   "TC-37-04"
  ],
  "Q-01": [
   "TC-26-01",
   "TC-26-02",
   "TC-26-03",
   "TC-26-04",
   "TC-39-04"
  ],
  "Q-33": [
   "TC-26-04"
  ],
  "Q-02": [
   "TC-27-01",
   "TC-27-02",
   "TC-39-04"
  ],
  "Q-06": [
   "TC-31-01",
   "TC-31-02",
   "TC-31-03",
   "TC-31-04",
   "TC-31-05",
   "TC-31-06",
   "TC-31-07",
   "TC-31-08",
   "TC-31-09",
   "TC-31-10",
   "TC-31-11",
   "TC-31-12"
  ],
  "Q-21": [
   "TC-33-01",
   "TC-33-02"
  ],
  "Q-38": [
   "TC-34-03"
  ],
  "Q-19": [
   "TC-34-04"
  ],
  "Q-22": [
   "TC-35-01",
   "TC-35-02"
  ],
  "Q-14": [
   "TC-36-02",
   "TC-37-02",
   "TC-37-03",
   "TC-37-04",
   "TC-37-06",
   "TC-38-01",
   "TC-38-02"
  ],
  "Q-12": [
   "TC-39-01",
   "TC-39-02",
   "TC-39-03",
   "TC-39-04"
  ],
  "Q-28": [
   "TC-40-01",
   "TC-40-02",
   "TC-40-03",
   "TC-40-04",
   "TC-41-04"
  ],
  "Q-29": [
   "TC-41-01",
   "TC-41-02",
   "TC-41-03",
   "TC-41-04"
  ]
 },
 "assumptions": {
  "Assumption: the rating is a whole number from 1 to 5 until Q-03 is answered.": [
   "TC-02-01"
  ],
  "Assumption: the valid data used (rating 4, review text, Name, Email) meets the unconfirmed length and format rules (Q-04, Q-05, Q-06).": [
   "TC-02-02",
   "TC-03-01",
   "TC-03-02",
   "TC-03-03",
   "TC-03-04",
   "TC-04-05",
   "TC-05-01",
   "TC-06-02",
   "TC-07-01",
   "TC-08-01",
   "TC-08-02",
   "TC-08-03",
   "TC-11-01",
   "TC-11-02",
   "TC-11-03",
   "TC-13-01",
   "TC-13-02",
   "TC-14-01",
   "TC-14-02",
   "TC-15-01",
   "TC-15-02",
   "TC-16-01",
   "TC-16-02",
   "TC-17-01",
   "TC-17-02",
   "TC-17-03",
   "TC-18-01",
   "TC-18-02",
   "TC-18-03",
   "TC-19-01",
   "TC-19-02",
   "TC-20-02",
   "TC-20-03",
   "TC-22-02",
   "TC-22-03",
   "TC-23-01",
   "TC-23-02",
   "TC-23-03",
   "TC-23-04",
   "TC-23-05",
   "TC-24-01",
   "TC-24-02",
   "TC-26-01",
   "TC-26-02",
   "TC-26-03",
   "TC-26-04",
   "TC-28-01",
   "TC-29-01",
   "TC-29-02",
   "TC-29-03",
   "TC-29-04",
   "TC-29-05",
   "TC-29-06",
   "TC-29-07",
   "TC-29-08",
   "TC-29-09",
   "TC-29-10",
   "TC-30-01",
   "TC-31-01",
   "TC-31-02",
   "TC-31-03",
   "TC-31-04",
   "TC-31-05",
   "TC-31-06",
   "TC-31-07",
   "TC-31-08",
   "TC-31-09",
   "TC-31-10",
   "TC-31-11",
   "TC-31-12",
   "TC-32-01",
   "TC-32-02",
   "TC-32-03",
   "TC-32-04",
   "TC-33-01",
   "TC-33-02",
   "TC-34-02",
   "TC-34-03",
   "TC-35-01",
   "TC-35-02",
   "TC-36-02",
   "TC-37-01",
   "TC-37-02",
   "TC-37-03",
   "TC-37-04",
   "TC-37-05",
   "TC-37-06",
   "TC-38-01",
   "TC-39-01",
   "TC-39-02",
   "TC-39-03",
   "TC-39-04",
   "TC-40-01",
   "TC-40-02",
   "TC-40-03",
   "TC-40-04",
   "TC-41-01",
   "TC-41-02",
   "TC-41-03",
   "TC-41-04"
  ],
  "Assumption: a hover preview, if any, is not kept until Q-36 is answered.": [
   "TC-02-03"
  ],
  "Assumption: rating range 1 to 5 until Q-03 is answered.": [
   "TC-03-01",
   "TC-03-02",
   "TC-03-03",
   "TC-03-04"
  ],
  "Assumption: clicking another star changes the rating (Q-16).": [
   "TC-04-01",
   "TC-04-02"
  ],
  "Assumption: the rating cannot be cleared by clicking (Q-16).": [
   "TC-04-03"
  ],
  "Assumption: reloading is the only way back to \"No rating\" (Q-16).": [
   "TC-04-04"
  ],
  "Assumption: reloading is the only way back to no rating (Q-16); a reload restores the initial data (app-note.md).": [
   "TC-04-04"
  ],
  "Assumption: the error names the rating field; wording checked for meaning, not exact text (Q-20).": [
   "TC-05-01"
  ],
  "Assumption: wording checked for meaning, not exact text (Q-20).": [
   "TC-07-01",
   "TC-28-01",
   "TC-30-01"
  ],
  "Assumption: the text used (43 characters) is between the minimum and the maximum length until Q-04 is answered.": [
   "TC-08-01"
  ],
  "Assumption: no character restriction in \"Your review\" until Q-37 is answered.": [
   "TC-08-02"
  ],
  "Assumption: typing stops at the maximum (Q-18).": [
   "TC-10-02"
  ],
  "Assumption: pasting stops at the maximum (Q-18).": [
   "TC-10-03",
   "TC-10-04"
  ],
  "Assumption: a field of only spaces counts as empty (Q-17).": [
   "TC-11-01",
   "TC-32-02",
   "TC-32-04"
  ],
  "Assumption: line breaks are treated like spaces (Q-17).": [
   "TC-11-02"
  ],
  "Assumption: spaces are trimmed (Q-17).": [
   "TC-11-03",
   "TC-32-01",
   "TC-32-03"
  ],
  "Assumption: length is counted after trimming (Q-17).": [
   "TC-11-04"
  ],
  "Assumption: content is never executed (Q-15).": [
   "TC-12-01"
  ],
  "Assumption: in demo-1.0 the \"Moderator: approve pending reviews\" helper plays the moderator (environment.md).": [
   "TC-14-01"
  ],
  "Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered.": [
   "TC-17-01"
  ],
  "Assumption: submit date in any unambiguous format (Q-24).": [
   "TC-17-02"
  ],
  "Assumption: the rating and the name are shown with each review (Q-09).": [
   "TC-18-01"
  ],
  "Assumption: such names are accepted until Q-05 is answered.": [
   "TC-18-02"
  ],
  "Assumption: all approved reviews are shown on one page (Q-23).": [
   "TC-21-01"
  ],
  "Assumption: a short message saying there are no reviews yet (Q-25).": [
   "TC-22-01"
  ],
  "Assumption: empty-state message (Q-25).": [
   "TC-22-02",
   "TC-22-03"
  ],
  "Assumption: compared without regard to letter case (Q-32).": [
   "TC-25-01"
  ],
  "Assumption: letters and spaces are allowed until Q-05 is answered.": [
   "TC-29-01"
  ],
  "Assumption: accented letters are allowed until Q-05 is answered.": [
   "TC-29-02"
  ],
  "Assumption: hyphens and apostrophes are allowed until Q-05 is answered.": [
   "TC-29-03"
  ],
  "Assumption: standard format text@domain.tld until Q-06 is answered.": [
   "TC-31-01"
  ],
  "Assumption: standard format (Q-06).": [
   "TC-31-02",
   "TC-31-03",
   "TC-31-04",
   "TC-31-05",
   "TC-31-07",
   "TC-31-08"
  ],
  "Assumption: a top-level domain is required (Q-06); some format rules accept this value.": [
   "TC-31-06"
  ],
  "Assumption: letter case does not matter (Q-06).": [
   "TC-31-09"
  ],
  "Assumption: confirmation says the review was received and waits for approval (Q-21).": [
   "TC-33-01"
  ],
  "Assumption: confirmation text (Q-21).": [
   "TC-33-02"
  ],
  "Assumption: each error names its field; wording checked for meaning (Q-20).": [
   "TC-34-01"
  ],
  "Assumption: wording checked for meaning (Q-20).": [
   "TC-34-02"
  ],
  "Assumption: entered values are kept after a rejected submit until Q-38 is answered.": [
   "TC-34-03"
  ],
  "Assumption: fields are checked on Submit only (Q-19).": [
   "TC-34-04"
  ],
  "Assumption: form cleared (Q-22).": [
   "TC-35-01"
  ],
  "Assumption: Name and Email stay filled only if the checkbox was ticked (Q-22).": [
   "TC-35-02"
  ],
  "Assumption: only name and email are saved (Q-13, Q-14).": [
   "TC-37-01",
   "TC-37-04"
  ],
  "Assumption: saved values are replaced (Q-14).": [
   "TC-37-02"
  ],
  "Assumption: only one review is created (Q-28).": [
   "TC-40-01",
   "TC-40-02",
   "TC-40-03",
   "TC-40-04"
  ],
  "Assumption: Q-29.": [
   "TC-41-01",
   "TC-41-03"
  ],
  "Assumption: Q-29. Not producible in demo-1.0.": [
   "TC-41-02"
  ],
  "Assumption: Q-28, Q-29.": [
   "TC-41-04"
  ]
 },
 "vague": [],
 "long_summary": [
  [
   "TC-10-04",
   18
  ],
  [
   "TC-12-01",
   18
  ],
  [
   "TC-18-03",
   17
  ]
 ]
}
```

## AI (2026-10-21T04:17:25)

**Tool call `Bash`:**

```json
{
  "command": "cd \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\" && python - <<'EOF'\np='gen_tc.py'; s=open(p,encoding='utf-8').read()\nrep=[\n('''  'None of the 5 stars is shown as selected.',\n  [\"Assumption: reloading is the only way back to no rating (Q-16); a reload restores the initial data (app-note.md).\"])''',\n '''  'None of the 5 stars is shown as selected.')'''),\n('VALID = \"Assumption: the valid data used (rating 4, review text, Name, Email) meets the unconfirmed length and format rules (Q-04, Q-05, Q-06).\"',\n 'VALID = \"Assumption: the other values entered are valid under the unconfirmed length and format rules (Q-04, Q-05, Q-06).\"'),\n('\"Verify that pasting text ten times the maximum keeps the box at the maximum and the page usable.\"',\n '\"Verify that pasting ten times the maximum text keeps the page usable.\"'),\n(\"\"\"'Verify that a script in \"Your review *\" is not run on submit or on the product page.'\"\"\",\n \"\"\"'Verify that a script in \"Your review *\" is never run.'\"\"\"),\n('''\"Verify that the characters & < > \\\\\" ' in a review are shown exactly as typed.\"''',\n '''\"Verify that the characters & < > \\\\\" ' in a review are shown as typed.\"'''),\n('''  \"To be confirmed (Q-25): the message saying there are no reviews yet is still shown and no review is listed.\",\n  valid=True)''',\n '''  \"To be confirmed (Q-25): the message saying there are no reviews yet is still shown and no review is listed.\",\n  [BLK(\"the product starts with approved reviews\", \"app-note.md\")], valid=True)'''),\n('''  f'To be confirmed (Q-25): the no-reviews message is no longer shown and the review \"{t}\" is listed.', valid=True)''',\n '''  f'To be confirmed (Q-25): the no-reviews message is no longer shown and the review \"{t}\" is listed.',\n  [BLK(\"the product starts with approved reviews\", \"app-note.md\")], valid=True)'''),\n('''  \"To be confirmed (Q-11): the average rating and the review count are the same as written down before step 1.\",\n  valid=True)\nt = \"Summary check: count.\"''',\n '''  \"To be confirmed (Q-11): the average rating and the review count are the same as written down before step 1.\",\n  [BLK(\"no reject action\", \"environment.md\")], valid=True)\nt = \"Summary check: count.\"'''),\n('''  'To be confirmed (Q-11, Q-25): the summary shows no average or an empty state; it never shows \"NaN\", \"0 stars\" or a number without reviews.')''',\n '''  'To be confirmed (Q-11, Q-25): the summary shows no average or an empty state; it never shows \"NaN\", \"0 stars\" or a number without reviews.',\n  [BLK(\"the product starts with approved reviews\", \"app-note.md\")])'''),\n]\nfor a,b in rep:\n    assert s.count(a)==1, a[:60]\n    s=s.replace(a,b)\nopen(p,'w',encoding='utf-8').write(s)\nEOF\nPYTHONIOENCODING=utf-8 python -I gen_tc.py | python -c \"import json,sys; d=json.load(sys.stdin); print(d['total'], d['long_summary'], d['vague'])\"",
  "description": "Apply fixes and regenerate workbook"
}
```

## Tool (2026-10-21T04:17:27)

```
145 [] []
```

## AI (2026-10-21T04:17:30)

Let me spot-check a few rows in the exported workbook.

## AI (2026-10-21T04:17:32)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1 && PYTHONIOENCODING=utf-8 python -c \"\nimport openpyxl\nwb=openpyxl.load_workbook('test-cases.xlsx'); ws=wb.active\nprint(ws.title, ws.max_row, [ws.column_dimensions[c].width for c in 'ABCDEFG'])\nrows=list(ws.iter_rows(values_only=True))\nprint(rows[0])\nfor r in rows[1:]:\n    if r[1] in ('TC-05-01','TC-12-01','TC-18-03','TC-26-01','TC-37-01','TC-23-05'):\n        print('-----'); [print(f'[{h}]',v) for h,v in zip(rows[0],r)]\nids=[r[1] for r in rows[1:]]; print(len(ids), len(set(ids)))\n\"",
  "description": "Spot-check exported test cases"
}
```

## Tool (2026-10-21T04:17:34)

```
Test Cases 146 [10.0, 12.0, 45.0, 35.0, 60.0, 55.0, 40.0]
('TR ID', 'TC ID', 'TC Summary', 'Pre-Condition', 'Steps', 'Expected Result', 'Notes')
-----
[TR ID] TR-05
[TC ID] TC-05-01
[TC Summary] Verify that the review is not submitted when no star rating is selected.
[Pre-Condition] demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).
[Steps] 1. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
2. Enter "Anna Smith" in "Name *".
3. Enter "anna.smith@example.com" in "Email *".
4. Click "Submit".
[Expected Result] The review is not submitted: no confirmation message appears and "Pending approval" stays 0. To be confirmed (Q-20): an error message names the rating field ("Your rating").
[Notes] Condition: TCD-05-01
Technique: EP / BVA
Edge case: just below the minimum.
Assumption: the error names the rating field; wording checked for meaning, not exact text (Q-20).
Assumption: the other values entered are valid under the unconfirmed length and format rules (Q-04, Q-05, Q-06).
Missing info: expected result not stated in any source (Q-20).
-----
[TR ID] TR-12
[TC ID] TC-12-01
[TC Summary] Verify that a script in "Your review *" is never run.
[Pre-Condition] demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).
[Steps] 1. Click the 4th star of "Your rating *".
2. Enter "<script>alert(1)</script>" in "Your review *".
3. Enter "Anna Smith" in "Name *".
4. Enter "anna.smith@example.com" in "Email *".
5. Click "Submit".
6. Click "Moderator: approve pending reviews".
7. Look at the "Reviews" list.
[Expected Result] To be confirmed (Q-15): no alert dialog opens at any step; the review text is shown as plain text, removed, or the review is rejected, as confirmed for Q-15.
[Notes] Condition: TCD-12-01
Technique: Error guessing
Missing info: shown as plain text, removed or rejected (Q-15).
Assumption: content is never executed (Q-15).
Risk: script injection would affect every visitor of the product page.
-----
[TR ID] TR-18
[TC ID] TC-18-03
[TC Summary] Verify that the characters & < > " ' in a review are shown as typed.
[Pre-Condition] demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).
[Steps] 1. Click the 4th star of "Your rating *".
2. Enter "5 > 3 & "good" isn't it" in "Your review *".
3. Enter "Anna Smith" in "Name *".
4. Enter "anna.smith@example.com" in "Email *".
5. Click "Submit".
6. Click "Moderator: approve pending reviews".
7. Find the review starting with "5 > 3" in the "Reviews" list.
[Expected Result] To be confirmed (Q-15): the review text is shown exactly as typed in step 2, with no "&gt;", "&amp;", "&quot;" or "&#39;" in place of the characters.
[Notes] Condition: TCD-18-03
Technique: Error guessing
Missing info: handling of HTML-like text (Q-15).
Assumption: the other values entered are valid under the unconfirmed length and format rules (Q-04, Q-05, Q-06).
-----
[TR ID] TR-23
[TC ID] TC-23-05
[TC Summary] Verify that an average falling exactly on a rounding step is shown with the confirmed rounding.
[Pre-Condition] demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). The "Reviews" list shows exactly 3 approved reviews rated 5, 4 and 3 (initial data; check before step 1).
[Steps] 1. Click the 2nd star of "Your rating *".
2. Enter "Rounding check: two stars." in "Your review *".
3. Enter "Anna Smith" in "Name *".
4. Enter "anna.smith@example.com" in "Email *".
5. Click "Submit".
6. Click "Moderator: approve pending reviews".
7. Read the average in the rating summary next to the product name.
[Expected Result] To be confirmed (Q-11): the approved ratings are 5, 4, 3 and 2 (exact average 3.5) and the average is shown as 3.5, or rounded as the confirmed rule says.
[Notes] Condition: TCD-23-05
Technique: BVA
Missing info: rounding rule not stated (Q-11); exact boundary values are set when Q-11 is answered.
Missing info: values next to the rounding step (for example 4.33) are added when Q-11 gives the rounding rule.
Assumption: the other values entered are valid under the unconfirmed length and format rules (Q-04, Q-05, Q-06).
-----
[TR ID] TR-26
[TC ID] TC-26-01
[TC Summary] Verify that a signed-in customer who bought the product can submit a review.
[Pre-Condition] A build with sign-in and orders; signed in as a test customer with a delivered order of this product; product page open.
[Steps] 1. Click the 4th star of "Your rating *".
2. Enter "Permission check." in "Your review *".
3. Enter "Anna Smith" in "Name *".
4. Enter "anna.smith@example.com" in "Email *".
5. Click "Submit".
[Expected Result] To be confirmed (Q-01): The review is submitted: a confirmation message appears above the form. The review is waiting for approval.
[Notes] Condition: TCD-26-01
Technique: Decision table
Missing info: sign-in and purchase check not specified (Q-01).
Missing info: demo-1.0 has no sign-in (environment.md).
Missing info: cannot be run on demo-1.0 (no sign-in or orders) (environment.md); needs a build or environment that has it.
Assumption: the other values entered are valid under the unconfirmed length and format rules (Q-04, Q-05, Q-06).
-----
[TR ID] TR-37
[TC ID] TC-37-01
[TC Summary] Verify that ticked saving refills Name and Email on the next visit.
[Pre-Condition] demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
[Steps] 1. Click the 4th star of "Your rating *".
2. Enter "Save check: first visit." in "Your review *".
3. Enter "Anna Smith" in "Name *".
4. Enter "anna.smith@example.com" in "Email *".
5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."
6. Click "Submit".
7. Close the tab and open exam/app/index.html again in the same Chrome window.
8. Look at "Name *" and "Email *".
[Expected Result] "Name *" shows "Anna Smith" and "Email *" shows "anna.smith@example.com".
[Notes] Condition: TCD-37-01
Technique: State transition
Assumption: only name and email are saved (Q-13, Q-14).
Risk: personal data stored on the device.
Assumption: the other values entered are valid under the unconfirmed length and format rules (Q-04, Q-05, Q-06).
145 145
```

## AI (2026-10-21T04:17:44)

**Tool call `Bash`:**

```json
{
  "command": "cd \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\" && python - <<'EOF'\np='gen_tc.py'; s=open(p,encoding='utf-8').read()\na='''  \"To be confirmed (Q-01): \" + OK.replace(' and \"Pending approval\" changes from 0 to 1', \"\") + \" The review is waiting for approval.\",\n  [BLK(\"no sign-in or orders\", \"environment.md\")], valid=True)'''\nb='''  \"To be confirmed (Q-01): the review is submitted: a confirmation message appears above the form and the review waits for approval.\",\n  valid=True)'''\nassert s.count(a)==1; s=s.replace(a,b)\na='''  fill(4, t) + [SUB, APP, 'Find the review starting with \"5 > 3\" in the \"Reviews\" list.'],'''\nb='''  [star(4), f'Enter this text in \"Your review *\" (everything after the colon): {t}', nm(NAME), em(EMAIL), SUB, APP,\n   'Find the review starting with \"5 > 3\" in the \"Reviews\" list.'],'''\nassert s.count(a)==1; s=s.replace(a,b)\nopen(p,'w',encoding='utf-8').write(s)\nEOF\nPYTHONIOENCODING=utf-8 python -I gen_tc.py > report.json && python -c \"import json; d=json.load(open('report.json',encoding='utf-8')); print(d['total'])\"; ls -la /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/",
  "description": "Apply final fixes and regenerate"
}
```

## Tool (2026-10-21T04:17:47)

```
145
total 120
drwxr-xr-x 1 vinh.the.nguyen 1049089     0 Oct 21 11:17 .
drwxr-xr-x 1 vinh.the.nguyen 1049089     0 Oct 21 10:58 ..
drwxr-xr-x 1 vinh.the.nguyen 1049089     0 Oct 21 11:08 ai-original
-rw-r--r-- 1 vinh.the.nguyen 1049089 11045 Oct 21 11:09 clarification-questions.md
-rw-r--r-- 1 vinh.the.nguyen 1049089 25563 Oct 21 11:17 test-cases.xlsx
-rw-r--r-- 1 vinh.the.nguyen 1049089 58871 Oct 21 11:09 test-design.md
-rw-r--r-- 1 vinh.the.nguyen 1049089  9065 Oct 21 11:00 test-requirements.xlsx
```

## AI (2026-10-21T04:17:52)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1 && PYTHONIOENCODING=utf-8 python -c \"\nimport openpyxl\nws=openpyxl.load_workbook('test-cases.xlsx').active\nrows=list(ws.iter_rows(min_row=2,values_only=True))\ntbc=[r[1] for r in rows if 'To be confirmed' in r[5]]\nprint('TBC',len(tbc)); print('no TBC',[r[1] for r in rows if r[1] not in tbc])\nblk=[r[1] for r in rows if not r[3].startswith('demo-1.0') or 'cannot be run on demo-1.0' in r[6] or 'not meaningful' in r[6] or 'restores the initial data' in r[6]]\nprint('not on demo',len(blk),blk)\n\"",
  "description": "Count confirmed vs TBC and blocked cases"
}
```

## Tool (2026-10-21T04:17:54)

```
TBC 120
no TBC ['TC-01-01', 'TC-02-01', 'TC-04-04', 'TC-06-01', 'TC-08-01', 'TC-08-03', 'TC-13-01', 'TC-13-02', 'TC-14-01', 'TC-14-02', 'TC-14-03', 'TC-15-01', 'TC-15-02', 'TC-18-01', 'TC-19-01', 'TC-19-02', 'TC-24-01', 'TC-24-02', 'TC-25-02', 'TC-25-03', 'TC-25-05', 'TC-25-06', 'TC-36-01', 'TC-37-01', 'TC-37-05']
not on demo 32 ['TC-13-01', 'TC-13-02', 'TC-15-01', 'TC-15-02', 'TC-20-03', 'TC-21-01', 'TC-21-02', 'TC-21-03', 'TC-21-04', 'TC-22-01', 'TC-22-02', 'TC-22-03', 'TC-23-03', 'TC-23-06', 'TC-24-01', 'TC-24-02', 'TC-26-01', 'TC-26-02', 'TC-26-03', 'TC-26-04', 'TC-27-01', 'TC-27-02', 'TC-39-01', 'TC-39-02', 'TC-39-03', 'TC-39-04', 'TC-40-03', 'TC-40-04', 'TC-41-01', 'TC-41-02', 'TC-41-03', 'TC-41-04']
```

## AI (2026-10-21T04:18:27)

I wrote 145 test cases to `C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-1\test-cases.xlsx`, one per condition in your test design. 120 of them have an expected result marked "To be confirmed", because no product-owner answers exist yet. Per the skill, those expected results need a person to confirm them before you run anything.

The file is a copy of the skill's template, with the same sheet name, header row and column widths. Rows are sorted by TR ID, then TC ID. Every TR from TR-01 to TR-41 and every condition ID has a case, every TR ID in the design exists in the TR list, and no two cases share an ID. The generator script is at `C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\gen_tc.py` (temp folder, not in the repo). Nothing is committed.

**Cases per TR:** TR-01 1, TR-02 4, TR-03 4, TR-04 5, TR-05 1, TR-06 2, TR-07 1, TR-08 3, TR-09 4, TR-10 4, TR-11 4, TR-12 5, TR-13 2, TR-14 3, TR-15 2, TR-16 2, TR-17 3, TR-18 4, TR-19 2, TR-20 3, TR-21 4, TR-22 3, TR-23 6, TR-24 2, TR-25 7, TR-26 4, TR-27 2, TR-28 1, TR-29 10, TR-30 1, TR-31 12, TR-32 4, TR-33 2, TR-34 4, TR-35 2, TR-36 2, TR-37 6, TR-38 2, TR-39 4, TR-40 4, TR-41 4.

**What I used:** the four files you named, the knowledge folder, and the exam folder. From the exam folder I took the labels in `exam/app/index.html` and the build's starting data in `app.js` (3 approved reviews rated 5, 4 and 3). That starting data is only used to set up TC-20-x and TC-23-05, and those cases tell you to check it before step 1. No expected result comes from what the build does.

**The 25 cases with fully sourced expected results:** TC-01-01, 02-01, 04-04, 06-01, 08-01, 08-03, 13-01, 13-02, 14-01, 14-02, 14-03, 15-01, 15-02, 18-01, 19-01, 19-02, 24-01, 24-02, 25-02, 25-03, 25-05, 25-06, 36-01, 37-01, 37-05. Of these, only 19 can run on demo-1.0; TC-13-01, 13-02, 15-01, 15-02, 24-01 and 24-02 need a build with persistent data, a reject action or two products.

**"To be confirmed" expected results, by question:**
- Q-01: TC-26-01 to 26-04, TC-39-04
- Q-02: TC-27-01, 27-02, 39-04
- Q-03: TC-02-02, 03-01 to 03-04
- Q-04: TC-09-01 to 09-04, 10-01 to 10-04, 11-04, 18-04
- Q-05: TC-12-05, 18-02, 29-01 to 29-10
- Q-06: TC-31-01 to 31-12
- Q-08: TC-16-01, 16-02
- Q-09: TC-03-01 to 03-04, 04-05, 17-01, 17-03
- Q-10: TC-20-01 to 20-03
- Q-11: TC-23-01 to 23-06
- Q-12: TC-39-01 to 39-04
- Q-13: TC-25-04, 37-04
- Q-14: TC-36-02, 37-02, 37-03, 37-04, 37-06, 38-01, 38-02
- Q-15: TC-12-01 to 12-05, 18-03
- Q-16: TC-04-01 to 04-03
- Q-17: TC-11-01 to 11-04, 32-01 to 32-04
- Q-18: TC-10-02 to 10-04, 29-10, 31-12
- Q-19: TC-34-04
- Q-20: TC-05-01, 07-01, 10-01, 11-01, 11-02, 11-04, 28-01, 29-06, 30-01, 31-03 to 31-08, 32-02, 32-04, 34-01, 34-02
- Q-21: TC-33-01, 33-02
- Q-22: TC-35-01, 35-02
- Q-23: TC-21-01 to 21-04
- Q-24: TC-17-02
- Q-25: TC-22-01 to 22-03, 23-06
- Q-28: TC-40-01 to 40-04, 41-04
- Q-29: TC-41-01 to 41-04
- Q-32: TC-25-01
- Q-33: TC-26-04
- Q-34: TC-02-04, 25-07
- Q-35: TC-06-02
- Q-36: TC-02-03
- Q-37: TC-08-02
- Q-38: TC-34-03

Each of these has a Missing info note naming the question.

**Assumptions:** All of the design's assumptions are carried into the Notes column unchanged. I added two of my own:
- About 100 cases carry the note "the other values entered are valid under the unconfirmed length and format rules (Q-04, Q-05, Q-06)". These are the standard values: rating 4, "Soft fabric, true to size. Would buy again.", "Anna Smith", anna.smith@example.com.
- TC-08-01 assumes its 43-character review text is within the allowed length (Q-04).

**Decisions for you:**
1. **Expected results before you run:** either get product-owner answers, or approve the design's assumptions as the working expected results for this run. If you approve them, the "To be confirmed" prefixes should be swapped for "Assumption" notes.
2. **Script injection (TR-12):** the design treats "no script ever runs" as an assumption, so those cases are marked to be confirmed. I'd treat it as a firm expected result; the open part of Q-15 is only whether such text is escaped, removed or rejected.
3. **Length limits:** 18 cases use placeholders like [minimum], [maximum] and [page size] (TC-09-x, 10-x, 11-04, 18-04, 21-02 to 21-04, 29-08 to 29-10, 31-10 to 31-12). They can't run until Q-04, Q-05, Q-06 and Q-23 are answered. The "0 / 500" counter in the build is observed behaviour only, so I didn't use 500. Using it anyway would be your call.
4. **Heading (Q-32):** the knowledge file records that the build shows "Add a review", while mockup-1 says "ADD A REVIEW". TC-25-01 only passes if Q-32 confirms letter case doesn't matter.
5. **Cases that can't run on demo-1.0 (25):** TC-13-01, 13-02, 15-01, 15-02, 20-03, 22-01 to 22-03, 23-03, 23-06, 24-01, 24-02, 26-01, 26-02, 26-04, 27-01, 27-02, 39-03, 40-03, 40-04, 41-01 to 41-04. The build has no sign-in, server, reject action, empty product or second product, and a reload resets the data. Each is noted in the file. Decide whether to mark them Blocked or Not run.
   - TC-21-01 can run, but means submitting and approving 47 reviews by hand in one session.
   - TC-26-03 (guest) depends on Q-01, because every visitor of demo-1.0 is a guest.
6. **Possible duplicates, to drop once answered:** TC-10-01 repeats TC-07-01 if the minimum is 1. TC-39-01 repeats TC-33-01 if the limit is 1. TC-24-01 repeats TC-14-01 on a one-product build. TC-21-02 to 21-04 go away if Q-23 says there's no paging.
7. **Design header out of date:** `test-design.md` says the questions run "Q-01 to Q-32", but it cites Q-33 to Q-38, which do exist in `clarification-questions.md`. I didn't edit the design; that line probably needs updating.

## Tool (2026-10-21T04:18:28)

```
{"success":true,"message":"Report delivered to your caller."}
```

## Trainee (2026-10-21T04:18:58)

thanks, checked a sample + scanned the Expected Result column, they're specific, good. my decisions (PO won't answer before the exam deadline):

1. yes, use the design's assumptions as the working expected results for this run. replace the "To be confirmed (Q-xx):" prefix in Expected Result with the plain expected result, and put "Assumption: ... until Q-xx is answered" in Notes (keep the Missing info note too).
2. TR-12: agree. "no script runs" is a firm expected result, no prefix. only how the text is shown (escaped/removed/rejected) stays open under Q-15.
3. length / page size placeholders (the 18 cases): don't use 500 from the build. keep the placeholders and start Notes with "BLOCKED — waiting for Q-04" (or Q-05/Q-06/Q-23, whichever applies).
4. heading TC-25-01: keep, note "Assumption: compared without letter case until Q-32 is answered".
5. the 25 that can't run on demo-1.0: start Notes with "NOT RUN on demo-1.0 — <reason>" (environment, not a requirement problem, so not BLOCKED). TC-21-01 too, I won't create 47 reviews by hand this round.
6. possible duplicates: keep them for now, just add a note "Possible duplicate of TC-xx if Q-yy = ...". 
7. design header: I'll fix test-design.md myself, don't touch it.

only change test-cases.xlsx. when done tell me how many cases are now runnable on demo-1.0 (no BLOCKED / NOT RUN) and list their TC IDs.

Address this before completing your current task.

## AI (2026-10-21T04:20:14)

**Tool call `Bash`:**

```json
{
  "command": "sed -n 29,32p clarification-questions.md | cut -c1-200; PYTHONIOENCODING=utf-8 python -c \"\nimport openpyxl\nws=openpyxl.load_workbook('test-cases.xlsx').active\nfor r in ws.iter_rows(min_row=2,values_only=True):\n    if 'To be confirmed' in r[5]: print(r[1],'|',r[5])\n\"",
  "description": "List all To-be-confirmed expected results"
}
```

## Tool (2026-10-21T04:20:16)

```
## Nice to confirm

| Q ID | AC ID | Ambiguous point | Question | Assumption used until answered |
|---|---|---|---|---|
TC-02-02 | To be confirmed (Q-03): no half star is shown, neither in "Your rating *" after step 1 nor on the review "Half star check." in the "Reviews" list; the rating is a whole number of stars.
TC-02-03 | To be confirmed (Q-36): stars 1 and 2 are shown as selected and stars 3, 4 and 5 as not selected (rating still 2).
TC-02-04 | To be confirmed (Q-34): stars 1 to 4 are shown as selected and star 5 as not selected, without using the mouse after step 1.
TC-03-01 | The review "Rating check: one star." appears in the "Reviews" list. To be confirmed (Q-03, Q-09): it is shown with 1 of 5 stars selected.
TC-03-02 | The review "Rating check: two stars." appears in the "Reviews" list. To be confirmed (Q-03, Q-09): it is shown with 2 of 5 stars selected.
TC-03-03 | The review "Rating check: four stars." appears in the "Reviews" list. To be confirmed (Q-03, Q-09): it is shown with 4 of 5 stars selected.
TC-03-04 | The review "Rating check: five stars." appears in the "Reviews" list. To be confirmed (Q-03, Q-09): it is shown with 5 of 5 stars selected.
TC-04-01 | To be confirmed (Q-16): all 5 stars are shown as selected (rating 5).
TC-04-02 | To be confirmed (Q-16): only stars 1 and 2 are shown as selected; stars 3, 4 and 5 are not selected (rating 2).
TC-04-03 | To be confirmed (Q-16): stars 1, 2 and 3 are still shown as selected (rating 3); the rating is not cleared to no rating.
TC-04-05 | The review "Changed rating, final is three." appears in the "Reviews" list. To be confirmed (Q-09): it is shown with 3 of 5 stars selected (not 1, 4 or 2).
TC-05-01 | The review is not submitted: no confirmation message appears and "Pending approval" stays 0. To be confirmed (Q-20): an error message names the rating field ("Your rating").
TC-06-02 | To be confirmed (Q-35): the review shows "Line one", "Line two" and "Line three" on three separate lines.
TC-07-01 | The review is not submitted: no confirmation message appears and "Pending approval" stays 0. To be confirmed (Q-20): an error message names "Your review".
TC-08-02 | To be confirmed (Q-37): the review is accepted and, in the "Reviews" list, its text is shown exactly as "Très bien, Größe M passt! 日本語 OK 100% 👍" (no "?", boxes or encoded characters).
TC-09-01 | To be confirmed (Q-04): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-09-02 | To be confirmed (Q-04): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-09-03 | To be confirmed (Q-04): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-09-04 | To be confirmed (Q-04): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1. After step 6 the review appears in the "Reviews" list with its full text (no character cut off).
TC-10-01 | To be confirmed (Q-04, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".
TC-10-02 | To be confirmed (Q-04, Q-18): "Your review *" holds exactly [maximum] characters and the typed "b" is not added.
TC-10-03 | To be confirmed (Q-04, Q-18): "Your review *" holds exactly [maximum] characters and the last character "b" is not in the box.
TC-10-04 | To be confirmed (Q-04, Q-18): the page does not freeze (the "A" typed in step 2 appears in "Name *" at once) and "Your review *" holds at most [maximum] characters.
TC-11-01 | To be confirmed (Q-17, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".
TC-11-02 | To be confirmed (Q-17, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".
TC-11-03 | To be confirmed (Q-17): the review text is "Space padded review." with no spaces before the first word or after the full stop.
TC-11-04 | To be confirmed (Q-04, Q-17, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".
TC-12-01 | To be confirmed (Q-15): no alert dialog opens at any step; the review text is shown as plain text, removed, or the review is rejected, as confirmed for Q-15.
TC-12-02 | To be confirmed (Q-15): no alert dialog opens at any step and no image or broken-image icon appears in the "Reviews" list.
TC-12-03 | To be confirmed (Q-15): the word "bold" is not shown in bold type; the text is shown as plain text "<b>bold</b> text check", with the tags removed, or the review is rejected, as confirmed for Q-15.
TC-12-04 | To be confirmed (Q-15): in the "Reviews" list "https://example.com" is not a clickable link (the pointer does not change to a hand and clicking it opens nothing), or it is removed, or the review is rejected, as confirmed for Q-15.
TC-12-05 | To be confirmed (Q-05, Q-15): no alert dialog opens at any step; the name is shown as plain text, removed, or the review is rejected, as confirmed for Q-15.
TC-16-01 | To be confirmed (Q-08): either the review "Author view: pending check." is not in the "Reviews" list, or it is shown with a mark saying it awaits approval; it is never shown like an approved review without a mark.
TC-16-02 | To be confirmed (Q-08): the review "Author view: approved check." is shown like the other approved reviews, with no "awaiting approval" mark.
TC-17-01 | To be confirmed (Q-09): the review shows 4 of 5 stars, the name "Anna Smith", a date and the text "Details check: all parts shown.".
TC-17-02 | To be confirmed (Q-24): the date shown is today's date (the submit date), written so that day and month cannot be mixed up (for example "October 21, 2026", not "10/11/26").
TC-17-03 | To be confirmed (Q-09): the name is shown in the confirmed form: full name "Anna Smith", first name "Anna", or initials.
TC-18-02 | To be confirmed (Q-05): the name is shown exactly as "Zoë O'Brien-Lê", with no encoded characters such as "&#39;" or "&eacute;".
TC-18-03 | To be confirmed (Q-15): the review text is shown exactly as typed in step 2, with no "&gt;", "&amp;", "&quot;" or "&#39;" in place of the characters.
TC-18-04 | To be confirmed (Q-04): the full text is shown, wrapped inside the "Reviews" section; the page has no horizontal scroll bar and the text does not overlap other elements.
TC-20-01 | To be confirmed (Q-10): the reviews are in the confirmed order (for example newest date first).
TC-20-02 | To be confirmed (Q-10): the review "Order check: newly approved." is in the position the confirmed order requires (for example first, if newest first).
TC-20-03 | To be confirmed (Q-10): the two reviews are in the same order in steps 11 and 13, and that order follows the confirmed tie rule.
TC-21-01 | To be confirmed (Q-23): all 50 approved reviews are shown on the page (count = 50) with no paging control needed.
TC-21-02 | To be confirmed (Q-23): all [page size - 1] reviews are on the first page and no paging control or "Load more" is shown.
TC-21-03 | To be confirmed (Q-23): all [page size] reviews are on the first page and no paging control or "Load more" is shown.
TC-21-04 | To be confirmed (Q-23): the first page shows [page size] reviews and the last review is reached through the paging control or "Load more".
TC-22-01 | To be confirmed (Q-25): a short message says there are no reviews yet, and no review is listed.
TC-22-02 | To be confirmed (Q-25): the message saying there are no reviews yet is still shown and no review is listed.
TC-22-03 | To be confirmed (Q-25): the no-reviews message is no longer shown and the review "Empty state check: first approved." is listed.
TC-23-01 | To be confirmed (Q-11): the review count is 1 higher than before, and the average equals the sum of all approved ratings (including the new 1) divided by the new count, rounded as confirmed.
TC-23-02 | To be confirmed (Q-11): the average rating and the review count are the same as written down before step 1.
TC-23-03 | To be confirmed (Q-11): the average rating and the review count are the same as written down before step 1.
TC-23-04 | To be confirmed (Q-11): the count in the rating summary equals the number of reviews counted in the "Reviews" list.
TC-23-05 | To be confirmed (Q-11): the approved ratings are 5, 4, 3 and 2 (exact average 3.5) and the average is shown as 3.5, or rounded as the confirmed rule says.
TC-23-06 | To be confirmed (Q-11, Q-25): the summary shows no average or an empty state; it never shows "NaN", "0 stars" or a number without reviews.
TC-25-01 | The heading reads "ADD A REVIEW". To be confirmed (Q-32): the same words in other letter case (for example "Add a review") also pass.
TC-25-04 | To be confirmed (Q-13): the text reads exactly "Save my name, email, and website in this browser for the next time I comment." (unless Q-13 removes "website").
TC-25-07 | To be confirmed (Q-34): the focus moves in this order: rating stars, "Your review *", "Name *", "Email *", save checkbox, "Submit"; pressing Enter on "Submit" submits the form (with empty fields: the form is checked and the review is not submitted).
TC-26-01 | To be confirmed (Q-01): the review is submitted: a confirmation message appears above the form and the review waits for approval.
TC-26-02 | To be confirmed (Q-01): the form is hidden, or disabled, or Submit is rejected with a message; no review is created.
TC-26-03 | To be confirmed (Q-01): the form is hidden, or disabled, or Submit is rejected with a message; no review is created.
TC-26-04 | To be confirmed (Q-01, Q-33): the customer can or cannot submit, as confirmed; if not, the form is hidden, disabled or Submit is rejected with a message.
TC-27-01 | To be confirmed (Q-02): Name and Email are prefilled from the account, or prefilled and editable, or not shown, as confirmed.
TC-27-02 | To be confirmed (Q-02): the review shows the name confirmed for Q-02 ("Anna S." if the edited name is used, "Anna Smith" if the account name is used).
TC-28-01 | The review is not submitted: no confirmation message appears and "Pending approval" stays 0. To be confirmed (Q-20): an error message names "Name".
TC-29-01 | To be confirmed (Q-05): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-29-02 | To be confirmed (Q-05): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-29-03 | To be confirmed (Q-05): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-29-04 | To be confirmed (Q-05): either the review is submitted (confirmation message, "Pending approval" 1) or it is rejected with an error naming "Name", as confirmed.
TC-29-05 | To be confirmed (Q-05): either the review is submitted (confirmation message, "Pending approval" 1) or it is rejected with an error naming "Name", as confirmed.
TC-29-06 | To be confirmed (Q-05, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Name".
TC-29-07 | To be confirmed (Q-05): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-29-08 | To be confirmed (Q-05): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-29-09 | To be confirmed (Q-05): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1. After approval the full name is shown with the review.
TC-29-10 | To be confirmed (Q-05, Q-18): either "Name *" stops at [maximum] characters, or the review is not submitted and an error message names "Name".
TC-30-01 | The review is not submitted: no confirmation message appears and "Pending approval" stays 0. To be confirmed (Q-20): an error message names "Email".
TC-31-01 | To be confirmed (Q-06): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-31-02 | To be confirmed (Q-06): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-31-03 | To be confirmed (Q-06, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".
TC-31-04 | To be confirmed (Q-06, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".
TC-31-05 | To be confirmed (Q-06, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".
TC-31-06 | To be confirmed (Q-06, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".
TC-31-07 | To be confirmed (Q-06, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".
TC-31-08 | To be confirmed (Q-06, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".
TC-31-09 | To be confirmed (Q-06): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-31-10 | To be confirmed (Q-06): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-31-11 | To be confirmed (Q-06): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-31-12 | To be confirmed (Q-06, Q-18): either "Email *" stops at [maximum] characters, or the review is not submitted and an error message names "Email".
TC-32-01 | To be confirmed (Q-17): the review is accepted and the name is shown as "Anna Smith", with no spaces before or after it.
TC-32-02 | To be confirmed (Q-17, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Name".
TC-32-03 | To be confirmed (Q-17): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-32-04 | To be confirmed (Q-17, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".
TC-33-01 | The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1. To be confirmed (Q-21): the message says the review was received and waits for approval.
TC-33-02 | The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1. To be confirmed (Q-21): the message says the review was received and waits for approval.
TC-34-01 | The review is not submitted: no confirmation message appears and "Pending approval" stays 0. To be confirmed (Q-20): the error messages name all four fields: rating, "Your review", "Name" and "Email".
TC-34-02 | The review is not submitted: no confirmation message appears and "Pending approval" stays 0. To be confirmed (Q-20): the error messages name the rating and "Your review" only; "Name" and "Email" are not named.
TC-34-03 | To be confirmed (Q-38): after step 5 the 4 stars, "Anna Smith" and "anna.smith@example.com" are still in the form, and after step 7 the review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.
TC-34-04 | To be confirmed (Q-19): no error message is shown for "Name" (or any field) before "Submit" is clicked.
TC-35-01 | To be confirmed (Q-22): the product page stays open (product name and "Reviews" still shown, no new page), no star is selected, and "Your review *", "Name *" and "Email *" are empty.
TC-35-02 | To be confirmed (Q-22): the product page stays open, no star is selected, "Your review *" is empty, and "Name *" and "Email *" still show "Anna Smith" and "anna.smith@example.com".
TC-36-02 | To be confirmed (Q-14): the checkbox is ticked or not ticked, as confirmed.
TC-37-02 | To be confirmed (Q-14): "Name *" shows "Ben Carter" and "Email *" shows "ben.carter@example.com".
TC-37-03 | To be confirmed (Q-14): "Name *" and "Email *" are filled or empty, as confirmed for Q-14.
TC-37-04 | To be confirmed (Q-13, Q-14): only "Name *" and "Email *" are filled; no star is selected and "Your review *" is empty.
TC-37-06 | To be confirmed (Q-14): "Name *" and "Email *" are empty.
TC-38-01 | To be confirmed (Q-14): "Name *" and "Email *" are empty.
TC-38-02 | To be confirmed (Q-14): "Name *" and "Email *" are empty.
TC-39-01 | To be confirmed (Q-12): The review is submitted: a confirmation message appears above the form and "Pending approval" increases by 1.
TC-39-02 | To be confirmed (Q-12): the review is not submitted ("Pending approval" does not increase) and the message confirmed for Q-12 is shown.
TC-39-03 | To be confirmed (Q-12): the review is submitted: a confirmation message appears and the review waits for approval.
TC-39-04 | To be confirmed (Q-01, Q-02, Q-12): the customer is still recognised and the review is not submitted; the message confirmed for Q-12 is shown.
TC-40-01 | To be confirmed (Q-28): "Pending approval" shows 1 (not 2) and the review "Double click check." appears exactly once after approval.
TC-40-02 | To be confirmed (Q-28): "Pending approval" shows 1 and the review "Click and Enter check." appears exactly once after approval.
TC-40-03 | To be confirmed (Q-28): the review "Reload after submit check." appears exactly once.
TC-40-04 | To be confirmed (Q-28): the review "Back and forward check." appears exactly once.
TC-41-01 | To be confirmed (Q-29): a message says the review was not submitted, and the rating (4 stars), "Your review *", "Name *" and "Email *" still hold the entered values.
TC-41-02 | To be confirmed (Q-29): a message says the review was not submitted, and the rating (4 stars), "Your review *", "Name *" and "Email *" still hold the entered values.
TC-41-03 | To be confirmed (Q-29): the customer is told the session expired and the entered rating, review, Name and Email are not lost.
TC-41-04 | To be confirmed (Q-28, Q-29): the review "Retry after failure check." appears exactly once.
```

## AI (2026-10-21T04:21:39)

**Tool call `Write`:**

```json
{
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\post.py",
  "content": "import re, shutil, sys\nimport openpyxl\n\nOUT = r\"C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\runs\\run-1\\test-cases.xlsx\"\nBAK = sys.argv[1]  # untouched output of gen_tc.py\nshutil.copyfile(BAK, OUT)\n\n# Questions that have a working assumption (test design Values/Assumptions tables, or the\n# \"Assumption used until answered\" column of clarification-questions.md).\nAMAP = {\n    \"Q-03\": \"the rating is a whole number from 1 to 5, one per star\",\n    \"Q-05\": \"names with letters, spaces, accented letters, hyphens and apostrophes are accepted\",\n    \"Q-06\": \"a valid email has the standard format text@domain.tld (top-level domain required, letter case ignored)\",\n    \"Q-09\": \"each displayed review shows its star rating, reviewer name, date and review text\",\n    \"Q-13\": \"only Name and Email are saved in this browser\",\n    \"Q-14\": \"only Name and Email are saved in this browser, and a new ticked Submit replaces them\",\n    \"Q-16\": \"clicking another star changes the rating; it cannot be cleared except by reloading the page\",\n    \"Q-17\": \"leading and trailing spaces are trimmed, and a field of only spaces or line breaks counts as empty\",\n    \"Q-18\": \"typing and pasting stop at the maximum length\",\n    \"Q-19\": \"fields are checked on Submit only\",\n    \"Q-20\": \"each error message names its field; wording is checked for meaning, not exact text\",\n    \"Q-21\": \"the confirmation says the review was received and waits for approval\",\n    \"Q-22\": \"after success the customer stays on the page and the form is cleared; Name and Email stay only if the save checkbox was ticked\",\n    \"Q-23\": \"all approved reviews are shown on one page\",\n    \"Q-24\": \"the date shown is the submit date, in any unambiguous format\",\n    \"Q-25\": \"with no approved reviews, a short message says there are no reviews yet\",\n    \"Q-28\": \"only one review is created per submit action\",\n    \"Q-29\": \"on a save failure a message says the review was not submitted and the entered data is kept\",\n    \"Q-32\": \"the heading is compared without letter case\",\n    \"Q-34\": \"the rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen\",\n    \"Q-35\": \"line breaks in a review are shown as entered\",\n    \"Q-36\": \"a hover preview, if any, is not kept after the pointer leaves\",\n    \"Q-37\": \"\\\"Your review\\\" has no character restriction\",\n    \"Q-38\": \"entered values stay in the form after a rejected Submit\",\n}\n# Cases whose TBC question has an assumption only for some cases (Q-05, Q-14): restrict.\nQ05_OK = {\"TC-18-02\", \"TC-29-01\", \"TC-29-02\", \"TC-29-03\"}\nQ14_OK = {\"TC-37-02\", \"TC-37-04\"}\n\nBLOCKED = {}\nfor t in [\"TC-09-01\", \"TC-09-02\", \"TC-09-03\", \"TC-09-04\", \"TC-10-01\", \"TC-10-02\", \"TC-10-03\", \"TC-10-04\", \"TC-11-04\", \"TC-18-04\"]:\n    BLOCKED[t] = \"Q-04\"\nfor t in [\"TC-29-08\", \"TC-29-09\", \"TC-29-10\"]: BLOCKED[t] = \"Q-05\"\nfor t in [\"TC-31-10\", \"TC-31-11\", \"TC-31-12\"]: BLOCKED[t] = \"Q-06\"\nfor t in [\"TC-21-02\", \"TC-21-03\", \"TC-21-04\"]: BLOCKED[t] = \"Q-23\"\nfor t in [\"TC-39-01\", \"TC-39-02\"]: BLOCKED[t] = \"Q-12\"\nBLOCKED[\"TC-39-04\"] = \"Q-12 (and Q-01, Q-02 for how the customer is identified)\"\n\nNOTRUN = {\n    \"TC-13-01\": \"no second visitor session; reviews exist only in the open page\",\n    \"TC-13-02\": \"a reload restores the initial data, so a pending review cannot be kept\",\n    \"TC-15-01\": \"no reject action\", \"TC-15-02\": \"no reject action\", \"TC-23-03\": \"no reject action\",\n    \"TC-20-03\": \"a reload restores the initial data\",\n    \"TC-21-01\": \"needs 50 approved reviews; creating 47 by hand is not done this round\",\n    \"TC-22-01\": \"the only product starts with approved reviews\", \"TC-22-02\": \"the only product starts with approved reviews\",\n    \"TC-22-03\": \"the only product starts with approved reviews\", \"TC-23-06\": \"the only product starts with approved reviews\",\n    \"TC-24-01\": \"one product only\", \"TC-24-02\": \"one product only\",\n    \"TC-26-01\": \"no sign-in or orders\", \"TC-26-02\": \"no sign-in or orders\", \"TC-26-03\": \"no sign-in\", \"TC-26-04\": \"no sign-in or orders\",\n    \"TC-27-01\": \"no sign-in\", \"TC-27-02\": \"no sign-in\",\n    \"TC-39-03\": \"one product only; also BLOCKED — waiting for Q-12\",\n    \"TC-40-03\": \"a reload restores the initial data\", \"TC-40-04\": \"Back/Forward reloads the page and restores the initial data\",\n    \"TC-41-01\": \"no server or network\", \"TC-41-02\": \"no server\", \"TC-41-03\": \"no sign-in\", \"TC-41-04\": \"no server or network\",\n}\nDUP = {\n    \"TC-10-01\": \"Possible duplicate of TC-07-01 if Q-04 = minimum length 1.\",\n    \"TC-39-01\": \"Possible duplicate of TC-33-01 if Q-12 = one review per customer and product.\",\n    \"TC-24-01\": \"Possible duplicate of TC-14-01 if the build under test has only one product.\",\n    \"TC-21-02\": \"Possible duplicate of TC-21-01 if Q-23 = no paging (all reviews on one page).\",\n    \"TC-21-03\": \"Possible duplicate of TC-21-01 if Q-23 = no paging (all reviews on one page).\",\n    \"TC-21-04\": \"Possible duplicate of TC-21-01 if Q-23 = no paging (all reviews on one page).\",\n}\n# Expected results rewritten by hand (TR-12 firm part, open choices resolved by an assumption, sourced text)\nEXP = {\n    \"TC-12-01\": 'No alert dialog opens at any step. To be confirmed (Q-15): the review text is shown as plain text, removed, or the review is rejected.',\n    \"TC-12-02\": 'No alert dialog opens at any step and no image or broken-image icon appears in the \"Reviews\" list.',\n    \"TC-12-05\": 'No alert dialog opens at any step. To be confirmed (Q-15): the name is shown as plain text, removed, or the review is rejected.',\n    \"TC-25-01\": 'The heading reads \"ADD A REVIEW\"; letter case is not compared (for example \"Add a review\" also passes).',\n    \"TC-25-04\": 'The text reads exactly \"Save my name, email, and website in this browser for the next time I comment.\"',\n    \"TC-29-10\": '\"Name *\" holds exactly [maximum] characters after the paste; the extra character is not added.',\n    \"TC-31-12\": '\"Email *\" holds exactly [maximum] characters after the paste; the extra character is not added.',\n}\nREMOVE_NOTE_PREFIXES = (\n    \"Missing info: cannot be run on demo-1.0 (\",\n    \"Missing info: on demo-1.0 (one product) this is the same check as TC-14-01.\",\n    \"Missing info: if Q-23 confirms there is no paging\",\n    \"Missing info: if the limit is 1, this is the first review (TC-33-01)\",\n    \"Missing info: 50 reviews are entered by hand on demo-1.0\",\n    \"Missing info: on demo-1.0 a reload restores the initial data, so this check\",\n    \"Missing info: on demo-1.0 Back/Forward reloads\",\n    \"Assumption: content is never executed (Q-15).\",  # TR-12: now a firm expected result\n)\n\nTBC_RE = re.compile(r\"To be confirmed \\(([^)]*)\\):\\s*\")\nQID = re.compile(r\"Q-\\d\\d\")\n\ndef convertible(tc, qs):\n    for q in qs:\n        if q == \"Q-05\" and tc not in Q05_OK: return False\n        if q == \"Q-14\" and tc not in Q14_OK: return False\n        if q not in AMAP and q not in (\"Q-05\", \"Q-14\", \"Q-04\", \"Q-13\"): return False\n        if q == \"Q-04\" and tc not in BLOCKED: return False\n        if q == \"Q-13\" and tc not in (\"TC-25-04\", \"TC-37-04\"): return False\n    return True\n\ndef join_q(qs):\n    qs = list(dict.fromkeys(qs))\n    s = qs[0] if len(qs) == 1 else \", \".join(qs[:-1]) + \" and \" + qs[-1]\n    return s + (\" is answered\" if len(qs) == 1 else \" are answered\")\n\ndef norm_assumption(note):\n    if not note.startswith(\"Assumption:\") or \" until \" in note:\n        return note\n    qs = QID.findall(note)\n    if not qs:\n        return note\n    body = note[len(\"Assumption:\"):]\n    body = re.sub(r\"\\s*\\((?:[^()]*Q-\\d\\d[^()]*)\\)\", \"\", body).strip()\n    body = body.rstrip(\".\").strip()\n    if not body or body.startswith(\"Q-\") or body.startswith(\".\"):\n        body = \"; \".join(AMAP[q] for q in qs if q in AMAP)\n    return f\"Assumption: {body} until {join_q(qs)}.\"\n\nwb = openpyxl.load_workbook(OUT)\nws = wb[\"Test Cases\"]\nsummary = {\"converted\": [], \"still_tbc\": {}, \"blocked\": [], \"notrun\": [], \"runnable\": []}\nfor row in ws.iter_rows(min_row=2):\n    tc = row[1].value\n    exp = row[5].value\n    notes = row[6].value.split(\"\\n\")\n    new_assume = []\n    if tc in EXP:\n        exp = EXP[tc]\n        qs_conv = {\"TC-25-01\": [\"Q-32\"], \"TC-29-10\": [\"Q-18\"], \"TC-31-12\": [\"Q-18\"]}.get(tc, [])\n        for q in qs_conv: new_assume.append(q)\n    else:\n        m = TBC_RE.search(exp)\n        if m:\n            qs = [q.strip() for q in m.group(1).split(\",\")]\n            if convertible(tc, qs):\n                before, after = exp[:m.start()], exp[m.end():]\n                after = after[:1].upper() + after[1:]\n                exp = (before + after).strip()\n                new_assume += [q for q in qs if q in AMAP and not (q == \"Q-05\" and tc not in Q05_OK)\n                               and not (q == \"Q-14\" and tc not in Q14_OK)]\n                summary[\"converted\"].append(tc)\n    if \"To be confirmed\" in exp:\n        summary[\"still_tbc\"][tc] = TBC_RE.search(exp).group(1)\n    # notes\n    notes = [n for n in notes if not n.startswith(REMOVE_NOTE_PREFIXES)]\n    notes = [norm_assumption(n) for n in notes]\n    if tc == \"TC-25-01\":\n        notes = [n for n in notes if not (n.startswith(\"Assumption:\") and \"Q-32\" in n)]\n        notes.append(\"Assumption: compared without letter case until Q-32 is answered.\")\n    covered = set()\n    for n in notes:\n        if n.startswith(\"Assumption:\"):\n            covered.update(QID.findall(n))\n    for q in dict.fromkeys(new_assume):\n        if q not in covered:\n            notes.append(f\"Assumption: {AMAP[q]} until {q} is answered.\")\n    if tc in DUP:\n        notes.insert(2, DUP[tc])\n    if tc in NOTRUN:\n        notes.insert(0, f\"NOT RUN on demo-1.0 — {NOTRUN[tc]}\")\n        summary[\"notrun\"].append(tc)\n    elif tc in BLOCKED:\n        notes.insert(0, f\"BLOCKED — waiting for {BLOCKED[tc]}\")\n        summary[\"blocked\"].append(tc)\n    else:\n        summary[\"runnable\"].append(tc)\n    seen = set(); notes = [n for n in notes if not (n in seen or seen.add(n))]\n    row[5].value = exp\n    row[6].value = \"\\n\".join(notes)\nwb.save(OUT)\n\nfor k, v in summary.items():\n    print(k, len(v), v if k != \"converted\" else \"\")\n"
}
```

## Tool (2026-10-21T04:21:39)

```
File created successfully at: C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\post.py (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:21:49)

**Tool call `Bash`:**

```json
{
  "command": "cd \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\" && sed -i 's/Q05_OK = {\"TC-18-02\", \"TC-29-01\", \"TC-29-02\", \"TC-29-03\"}/Q05_OK = {\"TC-18-02\", \"TC-29-01\", \"TC-29-02\", \"TC-29-03\", \"TC-29-08\", \"TC-29-09\"}/' post.py && cp \"/c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-cases.xlsx\" tc_before_decisions.xlsx && PYTHONIOENCODING=utf-8 python -I post.py \"$(cygpath -w \"$PWD/tc_before_decisions.xlsx\")\"",
  "description": "Back up workbook and apply coordinator decisions"
}
```

## Tool (2026-10-21T04:21:53)

```
converted 80 
still_tbc 35 {'TC-12-01': 'Q-15', 'TC-12-03': 'Q-15', 'TC-12-04': 'Q-15', 'TC-12-05': 'Q-15', 'TC-16-01': 'Q-08', 'TC-16-02': 'Q-08', 'TC-18-03': 'Q-15', 'TC-20-01': 'Q-10', 'TC-20-02': 'Q-10', 'TC-20-03': 'Q-10', 'TC-23-01': 'Q-11', 'TC-23-02': 'Q-11', 'TC-23-03': 'Q-11', 'TC-23-04': 'Q-11', 'TC-23-05': 'Q-11', 'TC-23-06': 'Q-11, Q-25', 'TC-26-01': 'Q-01', 'TC-26-02': 'Q-01', 'TC-26-03': 'Q-01', 'TC-26-04': 'Q-01, Q-33', 'TC-27-01': 'Q-02', 'TC-27-02': 'Q-02', 'TC-29-04': 'Q-05', 'TC-29-05': 'Q-05', 'TC-29-06': 'Q-05, Q-20', 'TC-29-07': 'Q-05', 'TC-36-02': 'Q-14', 'TC-37-03': 'Q-14', 'TC-37-06': 'Q-14', 'TC-38-01': 'Q-14', 'TC-38-02': 'Q-14', 'TC-39-01': 'Q-12', 'TC-39-02': 'Q-12', 'TC-39-03': 'Q-12', 'TC-39-04': 'Q-01, Q-02, Q-12'}
blocked 22 ['TC-09-01', 'TC-09-02', 'TC-09-03', 'TC-09-04', 'TC-10-01', 'TC-10-02', 'TC-10-03', 'TC-10-04', 'TC-11-04', 'TC-18-04', 'TC-21-02', 'TC-21-03', 'TC-21-04', 'TC-29-08', 'TC-29-09', 'TC-29-10', 'TC-31-10', 'TC-31-11', 'TC-31-12', 'TC-39-01', 'TC-39-02', 'TC-39-04']
notrun 26 ['TC-13-01', 'TC-13-02', 'TC-15-01', 'TC-15-02', 'TC-20-03', 'TC-21-01', 'TC-22-01', 'TC-22-02', 'TC-22-03', 'TC-23-03', 'TC-23-06', 'TC-24-01', 'TC-24-02', 'TC-26-01', 'TC-26-02', 'TC-26-03', 'TC-26-04', 'TC-27-01', 'TC-27-02', 'TC-39-03', 'TC-40-03', 'TC-40-04', 'TC-41-01', 'TC-41-02', 'TC-41-03', 'TC-41-04']
runnable 97 ['TC-01-01', 'TC-02-01', 'TC-02-02', 'TC-02-03', 'TC-02-04', 'TC-03-01', 'TC-03-02', 'TC-03-03', 'TC-03-04', 'TC-04-01', 'TC-04-02', 'TC-04-03', 'TC-04-04', 'TC-04-05', 'TC-05-01', 'TC-06-01', 'TC-06-02', 'TC-07-01', 'TC-08-01', 'TC-08-02', 'TC-08-03', 'TC-11-01', 'TC-11-02', 'TC-11-03', 'TC-12-01', 'TC-12-02', 'TC-12-03', 'TC-12-04', 'TC-12-05', 'TC-14-01', 'TC-14-02', 'TC-14-03', 'TC-16-01', 'TC-16-02', 'TC-17-01', 'TC-17-02', 'TC-17-03', 'TC-18-01', 'TC-18-02', 'TC-18-03', 'TC-19-01', 'TC-19-02', 'TC-20-01', 'TC-20-02', 'TC-23-01', 'TC-23-02', 'TC-23-04', 'TC-23-05', 'TC-25-01', 'TC-25-02', 'TC-25-03', 'TC-25-04', 'TC-25-05', 'TC-25-06', 'TC-25-07', 'TC-28-01', 'TC-29-01', 'TC-29-02', 'TC-29-03', 'TC-29-04', 'TC-29-05', 'TC-29-06', 'TC-29-07', 'TC-30-01', 'TC-31-01', 'TC-31-02', 'TC-31-03', 'TC-31-04', 'TC-31-05', 'TC-31-06', 'TC-31-07', 'TC-31-08', 'TC-31-09', 'TC-32-01', 'TC-32-02', 'TC-32-03', 'TC-32-04', 'TC-33-01', 'TC-33-02', 'TC-34-01', 'TC-34-02', 'TC-34-03', 'TC-34-04', 'TC-35-01', 'TC-35-02', 'TC-36-01', 'TC-36-02', 'TC-37-01', 'TC-37-02', 'TC-37-03', 'TC-37-04', 'TC-37-05', 'TC-37-06', 'TC-38-01', 'TC-38-02', 'TC-40-01', 'TC-40-02']
```

## AI (2026-10-21T04:21:59)

**Tool call `Bash`:**

```json
{
  "command": "PYTHONIOENCODING=utf-8 python -c \"\nimport openpyxl\nws=openpyxl.load_workbook('test-cases.xlsx').active\nprint(ws.title, ws.max_row, [ws.column_dimensions[c].width for c in 'ABCDEFG'], [c.value for c in ws[1]])\nfor r in ws.iter_rows(min_row=2,values_only=True):\n    if r[1] in ('TC-05-01','TC-12-01','TC-25-01','TC-10-01','TC-39-03','TC-31-06','TC-41-04','TC-37-04','TC-03-01'):\n        print('=====',r[1]); print('EXP:',r[5]); print(r[6])\n\"; git -C /c/AI_Enabled_Program status --short evaluator/test-fixtures/manual-qa-sim-pass",
  "description": "Spot-check updated rows and git status"
}
```

## Tool (2026-10-21T04:22:01)

```
Test Cases 146 [10.0, 12.0, 45.0, 35.0, 60.0, 55.0, 40.0] ['TR ID', 'TC ID', 'TC Summary', 'Pre-Condition', 'Steps', 'Expected Result', 'Notes']
===== TC-03-01
EXP: The review "Rating check: one star." appears in the "Reviews" list. It is shown with 1 of 5 stars selected.
Condition: TCD-03-01
Technique: BVA
Edge case: value exactly at the minimum.
Assumption: rating range 1 to 5 until Q-03 is answered.
Assumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.
Missing info: expected result not stated in any source (Q-03, Q-09).
Assumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.
===== TC-05-01
EXP: The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names the rating field ("Your rating").
Condition: TCD-05-01
Technique: EP / BVA
Edge case: just below the minimum.
Assumption: the error names the rating field; wording checked for meaning, not exact text until Q-20 is answered.
Assumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.
Missing info: expected result not stated in any source (Q-20).
===== TC-10-01
EXP: The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".
BLOCKED — waiting for Q-04
Condition: TCD-10-01
Technique: BVA
Possible duplicate of TC-07-01 if Q-04 = minimum length 1.
Edge case: one character below the minimum.
Missing info: minimum length not stated (Q-04). If the minimum is 1, this is TCD-07-01 and is not repeated.
Missing info: expected result not stated in any source (Q-20).
Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
===== TC-12-01
EXP: No alert dialog opens at any step. To be confirmed (Q-15): the review text is shown as plain text, removed, or the review is rejected.
Condition: TCD-12-01
Technique: Error guessing
Missing info: shown as plain text, removed or rejected (Q-15).
Risk: script injection would affect every visitor of the product page.
===== TC-25-01
EXP: The heading reads "ADD A REVIEW"; letter case is not compared (for example "Add a review" also passes).
Condition: TCD-25-01
Technique: EP
Missing info: expected result not stated in any source (Q-32).
Assumption: compared without letter case until Q-32 is answered.
===== TC-31-06
EXP: The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".
Condition: TCD-31-06
Technique: EP
Assumption: a top-level domain is required; some format rules accept this value until Q-06 is answered.
Assumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.
Missing info: expected result not stated in any source (Q-06, Q-20).
Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
===== TC-37-04
EXP: Only "Name *" and "Email *" are filled; no star is selected and "Your review *" is empty.
Condition: TCD-37-04
Technique: EP
Assumption: only name and email are saved until Q-13 and Q-14 are answered.
Assumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.
Missing info: expected result not stated in any source (Q-13, Q-14).
===== TC-39-03
EXP: To be confirmed (Q-12): the review is submitted: a confirmation message appears and the review waits for approval.
NOT RUN on demo-1.0 — one product only; also BLOCKED — waiting for Q-12
Condition: TCD-39-03
Technique: Error guessing
Missing info: Q-12; needs a build with two products.
Assumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.
===== TC-41-04
EXP: The review "Retry after failure check." appears exactly once.
NOT RUN on demo-1.0 — no server or network
Condition: TCD-41-04
Technique: Error guessing
Assumption: only one review is created per submit action; on a save failure a message says the review was not submitted and the entered data is kept until Q-28 and Q-29 are answered.
Assumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.
Missing info: expected result not stated in any source (Q-28, Q-29).
?? evaluator/test-fixtures/manual-qa-sim-pass/
```

## AI (2026-10-21T04:22:19)

I applied your decisions to `test-cases.xlsx` (only that file changed; nothing committed). 97 of the 145 cases can now run on demo-1.0, but 15 of those 97 still have an open "To be confirmed" result, because neither the test design nor the clarification file has an assumption for them.

**Runnable on demo-1.0 (no BLOCKED / NOT RUN), 97 cases:**
TC-01-01, TC-02-01 to 02-04, TC-03-01 to 03-04, TC-04-01 to 04-05, TC-05-01, TC-06-01, TC-06-02, TC-07-01, TC-08-01 to 08-03, TC-11-01 to 11-03, TC-12-01 to 12-05, TC-14-01 to 14-03, TC-16-01, TC-16-02, TC-17-01 to 17-03, TC-18-01 to 18-03, TC-19-01, TC-19-02, TC-20-01, TC-20-02, TC-23-01, TC-23-02, TC-23-04, TC-23-05, TC-25-01 to 25-07, TC-28-01, TC-29-01 to 29-07, TC-30-01, TC-31-01 to 31-09, TC-32-01 to 32-04, TC-33-01, TC-33-02, TC-34-01 to 34-04, TC-35-01, TC-35-02, TC-36-01, TC-36-02, TC-37-01 to 37-06, TC-38-01, TC-38-02, TC-40-01, TC-40-02.

**What changed:**
- **Assumptions as expected results:** 80 cases lost the "To be confirmed (Q-xx):" prefix and now state the result plainly. Their Notes have "Assumption: … until Q-xx is answered", and the Missing info notes are kept. I also reworded the design's existing Assumption notes into the same "until Q-xx is answered" form.
- **Where the assumptions come from:** the design's own assumptions, plus the "Assumption used until answered" column in `clarification-questions.md`. That column is the only source for Q-34 (keyboard use) and Q-35 (line breaks).
- **TR-12:** "No alert dialog opens" is now a firm result in TC-12-01, 12-02 and 12-05. In TC-12-01 and 12-05, how the text is shown stays "To be confirmed (Q-15)". I removed the "content is never executed" Assumption note.
- **TC-25-01:** the result is "ADD A REVIEW", letter case not compared, with your Q-32 assumption note.
- **BLOCKED (22):** Notes start with "BLOCKED — waiting for Q-xx", and the placeholders are kept.
  - TC-09-01 to 09-04, TC-10-01 to 10-04, TC-11-04, TC-18-04 wait for Q-04.
  - TC-29-08 to 29-10 wait for Q-05.
  - TC-31-10 to 31-12 wait for Q-06.
  - TC-21-02 to 21-04 wait for Q-23.
  - Correction: that group is 19 cases, not the 18 I said before.
  - **I also added three you didn't name:** TC-39-01, 39-02 and 39-04 use a [limit] placeholder, so they wait for Q-12. TC-39-04 also waits for Q-01 and Q-02, which decide how a customer is recognised.
- **NOT RUN (26):** Notes start with "NOT RUN on demo-1.0 — <reason>". That is the 25 I listed before plus TC-21-01. TC-39-03 reads "one product only; also BLOCKED — waiting for Q-12". My earlier "cannot be run on demo-1.0" notes are removed because these lines replace them.
- **Duplicates:** notes added to TC-10-01 (TC-07-01 if Q-04 = minimum 1), TC-39-01 (TC-33-01 if Q-12 = one review), TC-24-01 (TC-14-01 if the build has one product) and TC-21-02 to 21-04 (TC-21-01 if Q-23 = no paging).

**Decision for you:** 35 cases still have a "To be confirmed" prefix because no source gives an assumption, so I didn't invent one. 15 of them are in the runnable list:
- TC-12-01, 12-03, 12-04, 12-05 and 18-03: how the text is shown (Q-15).
- TC-16-01 and 16-02: what the author sees while a review is pending (Q-08).
- TC-20-01 and 20-02: review order (Q-10).
- TC-23-01, 23-02, 23-04 and 23-05: the rating summary (Q-11).
- TC-29-04 to 29-07: name characters (Q-05).
- TC-36-02, 37-03, 37-06, 38-01 and 38-02: the save checkbox (Q-14).

You can give working assumptions for these, or run them and record what you observe without a pass/fail verdict.

The workbook before these changes is saved at `C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\tc_before_decisions.xlsx`. I didn't touch `test-design.md`.

## Tool (2026-10-21T04:22:19)

```
{"success":true,"message":"Report delivered to your caller."}
```

## Trainee (2026-10-21T04:22:27)

good that you didn't invent those. for the 15 runnable ones with "To be confirmed": I'll run them and record what I observe, no pass/fail. pls start their Notes with "OBSERVE ONLY — no verdict until Q-xx is answered" (keep the To be confirmed expected result as is). the other 20 non-runnable TBC ones stay as they are. only test-cases.xlsx. tell me the final counts: runnable with a verdict / observe only / BLOCKED / NOT RUN.

Address this before completing your current task.

## AI (2026-10-21T04:22:34)

**Tool call `Bash`:**

```json
{
  "command": "PYTHONIOENCODING=utf-8 python -I -c \"\nimport openpyxl,re\nf='test-cases.xlsx'\nwb=openpyxl.load_workbook(f); ws=wb['Test Cases']\nc={'verdict':[],'observe':[],'blocked':[],'notrun':[]}\nfor row in ws.iter_rows(min_row=2):\n    tc=row[1].value; exp=row[5].value; notes=row[6].value\n    if notes.startswith('BLOCKED'): c['blocked'].append(tc); continue\n    if notes.startswith('NOT RUN'): c['notrun'].append(tc); continue\n    if notes.startswith('OBSERVE ONLY'): c['observe'].append(tc); continue\n    m=re.search(r'To be confirmed \\(([^)]*)\\)',exp)\n    if m:\n        qs=[q.strip() for q in m.group(1).split(',')]\n        q=qs[0] if len(qs)==1 else ', '.join(qs[:-1])+' and '+qs[-1]\n        row[6].value=f'OBSERVE ONLY — no verdict until {q} '+('is' if len(qs)==1 else 'are')+' answered\\n'+notes\n        c['observe'].append(tc)\n    else: c['verdict'].append(tc)\nwb.save(f)\nfor k,v in c.items(): print(k,len(v),v if k=='observe' else '')\nws=openpyxl.load_workbook(f).active\nfor r in ws.iter_rows(min_row=2,values_only=True):\n    if r[1] in ('TC-12-01','TC-29-06'): print(r[1],'|',r[6].split(chr(10))[0])\n\"",
  "description": "Mark observe-only cases and count final statuses"
}
```

## Tool (2026-10-21T04:22:37)

```
verdict 75 
observe 22 ['TC-12-01', 'TC-12-03', 'TC-12-04', 'TC-12-05', 'TC-16-01', 'TC-16-02', 'TC-18-03', 'TC-20-01', 'TC-20-02', 'TC-23-01', 'TC-23-02', 'TC-23-04', 'TC-23-05', 'TC-29-04', 'TC-29-05', 'TC-29-06', 'TC-29-07', 'TC-36-02', 'TC-37-03', 'TC-37-06', 'TC-38-01', 'TC-38-02']
blocked 22 
notrun 26 
TC-12-01 | OBSERVE ONLY � no verdict until Q-15 is answered
TC-29-06 | OBSERVE ONLY � no verdict until Q-05 and Q-20 are answered
```

## AI (2026-10-21T04:22:46)

**Tool call `Bash`:**

```json
{
  "command": "PYTHONIOENCODING=utf-8 python -I -c \"\nimport openpyxl\nf='test-cases.xlsx'\nwb=openpyxl.load_workbook(f); ws=wb['Test Cases']\nold='OBSERVE ONLY — no verdict until Q-15 is answered'\nfor row in ws.iter_rows(min_row=2):\n    if row[1].value in ('TC-12-01','TC-12-05'):\n        assert row[6].value.startswith(old+'\\n')\n        row[6].value=row[6].value.replace(old, old+' (only for how the text is shown; \\\"No alert dialog opens\\\" still gets a pass/fail verdict)',1)\n        print(row[1].value, ascii(row[6].value.split(chr(10))[0]))\nwb.save(f)\n\"",
  "description": "Keep firm no-script verdict on TC-12-01 and 12-05"
}
```

## Tool (2026-10-21T04:22:48)

```
TC-12-01 'OBSERVE ONLY \u2014 no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict)'
TC-12-05 'OBSERVE ONLY \u2014 no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict)'
```

## AI (2026-10-21T04:22:58)

I've marked the observe-only cases in `test-cases.xlsx`. One correction first: the runnable "To be confirmed" group is 22 cases, not 15. The list I sent you had 22 IDs but I added it up wrong. So the non-runnable "To be confirmed" cases that I left untouched are 13, not 20. Only `test-cases.xlsx` changed, and nothing is committed.

**Final counts (145 cases):**

| Status | Cases |
|---|---|
| Runnable on demo-1.0 with a pass/fail verdict | 75 |
| OBSERVE ONLY (runnable, no verdict) | 22 |
| BLOCKED (waiting for answers) | 22 |
| NOT RUN on demo-1.0 | 26 |

**OBSERVE ONLY (22):** each one's Notes now start with "OBSERVE ONLY — no verdict until Q-xx is answered", and its "To be confirmed" expected result is unchanged.
- TC-12-01, 12-03, 12-04, 12-05, 18-03 (Q-15)
- TC-16-01, 16-02 (Q-08)
- TC-20-01, 20-02 (Q-10)
- TC-23-01, 23-02, 23-04, 23-05 (Q-11)
- TC-29-04, 29-05, 29-07 (Q-05)
- TC-29-06 (Q-05 and Q-20)
- TC-36-02, 37-03, 37-06, 38-01, 38-02 (Q-14)

**One change beyond what you asked:** on TC-12-01 and TC-12-05 I added a short tail after the required prefix. It says the hold applies only to how the text is shown, and that "No alert dialog opens" still gets a pass/fail verdict. That keeps your earlier decision that "no script runs" is a firm result. If you'd rather have the bare prefix there, it's a one-line change.

**Verdict cases (75):** everything runnable except the 22 above. That is TC-01-01, 02-01 to 02-04, 03-01 to 03-04, 04-01 to 04-05, 05-01, 06-01, 06-02, 07-01, 08-01 to 08-03, 11-01 to 11-03, 12-02, 14-01 to 14-03, 17-01 to 17-03, 18-01, 18-02, 19-01, 19-02, 25-01 to 25-07, 28-01, 29-01 to 29-03, 30-01, 31-01 to 31-09, 32-01 to 32-04, 33-01, 33-02, 34-01 to 34-04, 35-01, 35-02, 36-01, 37-01, 37-02, 37-04, 37-05, 40-01 and 40-02. Many of these verdicts rest on the design's working assumptions, which are noted in each case's Notes.

The BLOCKED and NOT RUN lists are the same as in my last report.

## Tool (2026-10-21T04:22:59)

```
{"success":true,"message":"Report delivered to your caller."}
```
