# Transcript 04: test-data-generation (run1)

Exported from the agent session log. Kept verbatim: the trainee's messages, the AI's replies, tool calls and tool results. Left out: harness reminders and private thinking. The harness prefix in front of follow-up messages is removed; the AI's final report is shown as an AI reply.

## Trainee (2026-10-21T04:23:21)

hi! test data now. pls use my skill evaluator/test-fixtures/manual-qa-sim-pass/submission/skills/test-data-generation/SKILL.md (read and follow it).

inputs:
- test cases: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-cases.xlsx
- test design (optional): evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-design.md
- knowledge folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/knowledge
- output folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1

only make data for the cases I can run (Notes not starting with BLOCKED or NOT RUN). synthetic data only. only use these files and the exam folder (evaluator/test-fixtures/manual-qa-sim-pass/exam), nothing else under test-fixtures. tell me what you wrote.

## AI (2026-10-21T04:23:24)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\skills\\test-data-generation\\SKILL.md"
}
```

## Tool (2026-10-21T04:23:24)

```
1	---
2	name: test-data-generation
3	description: Use when a manual test case Excel list already exists and the concrete input values for each test case (valid, invalid and boundary) must be prepared before test execution; exports a synthetic test data set as test-data.xlsx. Do NOT use to write test cases, design test conditions or analyse requirements.
4	---
5	
6	# Test Data Generation
7	
8	Produces the exact input values each test case needs, using synthetic data only.
9	
10	## Inputs
11	
12	- {tc_file}: the test case list (.xlsx written by the test-case-generation skill). Default: `{output_dir}/test-cases.xlsx`. If missing, ask the user.
13	- {design_file}: the test design with the value ranges used. Default: `{output_dir}/test-design.md`. Optional; if absent, take the ranges from {knowledge_dir}.
14	- {knowledge_dir}: the project's knowledge folder (fields and their rules). If missing, ask the user.
15	- {output_dir}: the folder where the output file is written. If missing, ask the user.
16	
17	## Process
18	
19	1. Open {tc_file} and list, for every TC ID, each field the steps fill in and the purpose of the value (valid, invalid or boundary).
20	2. Collect the rule of each field (type, length, range, format) from {design_file} or the field files in {knowledge_dir}, marked Confirmed (with source) or Assumption.
21	3. Generate one value per TC ID and field with `references/test-data-rules.md`, giving each value a Data ID.
22	4. Verify every boundary value by counting its length or comparing it with the limit, and verify that each invalid value breaks exactly one rule.
23	5. Check that the data set contains no real personal data, real accounts or secrets, following the privacy section of `references/test-data-rules.md`.
24	6. Export by copying `assets/test-data-template.xlsx` to `{output_dir}/test-data.xlsx` and filling it, keeping the sheet name, header row and column widths; tag notes with `../test-requirements-analysis/references/note-tags.md`.
25	7. Report to the user: the number of values per purpose, every value built on an Assumption, and any TC ID that has no data; then stop for review.
26	
27	## Exceptions
28	
29	- A field rule is unknown: generate the value only with an Assumption note that names the assumed rule, or ask the user; never present it as confirmed.
30	- A test case needs real or production data: do not create it; ask the user for an approved synthetic or masked set.
31	- A long value cannot be stored in one cell: state the generation rule in Value (for example a character repeated N times) and the exact length in Notes.
32	
33	## Output
34	
35	- `{output_dir}/test-data.xlsx`: one row per field value, in the layout of `assets/test-data-template.xlsx`.
36	
37	## Files
38	
39	- `references/test-data-rules.md`: open at Steps 3 and 5.
40	- `../test-requirements-analysis/references/note-tags.md`: open at Step 6 (shared, single source).
41	- `assets/test-data-template.xlsx`: open at Step 6; copy it, never rebuild it.
42	
```

## AI (2026-10-21T04:23:25)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && find submission/runs/run-1 submission/knowledge exam submission/skills/test-data-generation -type f | head -100",
  "description": "List relevant fixture files"
}
```

## Tool (2026-10-21T04:23:26)

```
submission/runs/run-1/ai-original/clarification-questions.md
submission/runs/run-1/ai-original/test-cases.xlsx
submission/runs/run-1/ai-original/test-design.md
submission/runs/run-1/ai-original/test-requirements.xlsx
submission/runs/run-1/clarification-questions.md
submission/runs/run-1/test-cases.xlsx
submission/runs/run-1/test-design.md
submission/runs/run-1/test-requirements.xlsx
submission/knowledge/environment.md
submission/knowledge/glossary.md
submission/knowledge/index.md
submission/knowledge/product-review-rules.md
submission/knowledge/screens-and-fields.md
exam/app/app.js
exam/app/index.html
exam/app/styles.css
exam/app-note.md
exam/mockup-1.png
exam/mockup-2.png
exam/User Story for My Shop.docx
exam/user-story.md
submission/skills/test-data-generation/assets/test-data-template.xlsx
submission/skills/test-data-generation/references/test-data-rules.md
submission/skills/test-data-generation/SKILL.md
```

## AI (2026-10-21T04:23:29)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && cat submission/skills/test-data-generation/references/test-data-rules.md; echo ======; ls submission/skills/; ls submission/skills/test-requirements-analysis/references 2>&1",
  "description": "Read data rules and list skills"
}
```

## AI (2026-10-21T04:23:30)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && for f in submission/knowledge/*.md; do echo \"=== $f\"; cat \"$f\"; done",
  "description": "Read knowledge folder files"
}
```

## Tool (2026-10-21T04:23:32)

```
# Test data rules

## IDs and columns

- Data ID: `D-<TC ID>-<nn>`, for example D-TC-03-01-01. One row per field value.
- Purpose: exactly one of `valid`, `invalid`, `boundary`.
- Value: the literal value to type. For long strings, give the generation rule and the length, for example `"a" x 120 (120 chars)`.
- Notes: the rule the value tests (for example "length = maximum"), plus tagged notes.

## How to build values

| Purpose | Rule |
|---|---|
| valid | A realistic, clearly fake value inside every rule of the field. |
| boundary | Exactly on, one below or one above a limit. Count characters, including spaces. |
| invalid | Breaks exactly one rule; everything else about the value is valid. |

Useful invalid and edge values (use when relevant): empty, spaces only, leading/trailing spaces, special characters, non-Latin and accented letters, emoji, HTML or script text (`<b>x</b>`), very long value, value with line breaks, wrong format for the type.

## Privacy

- Synthetic data only. Never real names of known people, real email addresses, phone numbers, addresses, card numbers, accounts or passwords.
- Email: use reserved domains only, `example.com`, `example.org` or `example.test`.
- Names: clearly fake, for example "Test User 01".
- If masked data from production is required, stop and ask the user for an approved source.
======
defect-analysis-reporting
test-case-generation
test-condition-design
test-data-generation
test-requirements-analysis
ambiguity-checklist.md
note-tags.md
tr-writing-rules.md
```

## Tool (2026-10-21T04:23:34)

```
=== submission/knowledge/environment.md
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
=== submission/knowledge/glossary.md
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
=== submission/knowledge/index.md
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
=== submission/knowledge/product-review-rules.md
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
=== submission/knowledge/screens-and-fields.md
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
```

## AI (2026-10-21T04:23:36)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && cat submission/skills/test-requirements-analysis/references/note-tags.md; echo =====; cat submission/runs/run-1/test-design.md",
  "description": "Read note tags and test design"
}
```

## AI (2026-10-21T04:23:38)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && python -I -c \"\nimport openpyxl,sys\nfor p in ['submission/runs/run-1/test-cases.xlsx','submission/skills/test-data-generation/assets/test-data-template.xlsx']:\n    wb=openpyxl.load_workbook(p)\n    for ws in wb:\n        print('=====',p,ws.title,ws.dimensions)\n        for c,d in ws.column_dimensions.items(): print('  width',c,d.width)\n        for row in ws.iter_rows(values_only=True):\n            print(row)\n\"",
  "description": "Dump test cases and template workbooks"
}
```

## Tool (2026-10-21T04:23:40)

```
<persisted-output>
Output too large (58.7KB). Full output saved to: C:\Users\vinh.the.nguyen\.claude\projects\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\tool-results\bvx3ht754.txt

Preview (first 2KB):
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
=====
# Test design: US-VP02 Submit a Product Review

Input: runs/run-1/test-requirements.xlsx (41 TRs, TR-01 to TR-41) · Answers used: none (runs/run-1/clarification-questions.md has questions Q-01 to Q-38 (Q-33 to Q-38 added after review), no product owner answers yet) · Date: 2026-10-21

Other sources read: knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md, knowledge/environment.md, exam/user-story.md, exam/mockup-1.png, exam/app-note.md. The demo build (exam/app/) is the product under test and is never used as a source of expected results; its "0 / 500" counter and its message texts are Observed only and are not used as values here.

## Values and rules used

| Item | Value | Status (Confirmed / Assumption) | Source |
|---|---|---|---|
...
</persisted-output>
```

## Tool (2026-10-21T04:23:42)

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 9, in <module>
    print(row)
    ~~~~~^^^^^
  File "C:\Python\Python314\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode characters in position 386-388: character maps to <undefined>
===== submission/runs/run-1/test-cases.xlsx Test Cases A1:G146
  width A 10.0
  width B 12.0
  width C 45.0
  width D 35.0
  width E 60.0
  width F 55.0
  width G 40.0
('TR ID', 'TC ID', 'TC Summary', 'Pre-Condition', 'Steps', 'Expected Result', 'Notes')
('TR-01', 'TC-01-01', 'Verify that "Your rating *" shows exactly 5 stars, none selected, when the form opens.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Scroll to the "Add a review" form.\n2. Look at the stars next to "Your rating *" without clicking them.', 'Exactly 5 star icons are shown next to "Your rating *" and none of them is shown as selected.', 'Condition: TCD-01-01\nTechnique: EP')
('TR-02', 'TC-02-01', 'Verify that clicking the 3rd star selects rating 3.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 3rd star of "Your rating *".\n2. Look at the 5 stars of "Your rating *".', 'Stars 1, 2 and 3 are shown as selected and stars 4 and 5 are shown as not selected.', 'Condition: TCD-02-01\nTechnique: EP\nAssumption: the rating is a whole number from 1 to 5 until Q-03 is answered.')
('TR-02', 'TC-02-02', 'Verify that clicking the left half of a star does not set a half-star rating.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the left half of the 3rd star of "Your rating *".\n2. Look at the stars of "Your rating *".\n3. Enter "Half star check." in "Your review *".\n4. Enter "Anna Smith" in "Name *".\n5. Enter "anna.smith@example.com" in "Email *".\n6. Click "Submit".\n7. Click "Moderator: approve pending reviews".\n8. Find the review "Half star check." in the "Reviews" list.', 'No half star is shown, neither in "Your rating *" after step 1 nor on the review "Half star check." in the "Reviews" list; the rating is a whole number of stars.', 'Condition: TCD-02-02\nTechnique: EP\nMissing info: whether half stars are allowed (Q-03).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nAssumption: the rating is a whole number from 1 to 5, one per star until Q-03 is answered.')
('TR-02', 'TC-02-03', 'Verify that moving the pointer over the stars without clicking keeps the selected rating.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 2nd star of "Your rating *".\n2. Move the pointer over the 5th star of "Your rating *" without clicking.\n3. Move the pointer away from the stars.\n4. Look at the 5 stars of "Your rating *".', 'Stars 1 and 2 are shown as selected and stars 3, 4 and 5 as not selected (rating still 2).', 'Condition: TCD-02-03\nTechnique: Error guessing\nAssumption: a hover preview, if any, is not kept until Q-36 is answered.\nMissing info: expected result not stated in any source (Q-36).')
('TR-02', 'TC-02-04', 'Verify that a rating can be selected with the keyboard only.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click on the info text "Your email address will not be published. Required fields are marked *" to place the focus before the form.\n2. Press Tab until a star of "Your rating *" has the focus.\n3. Use the arrow keys to move to the 4th star and press Space (if nothing changes, press Enter).\n4. Look at the 5 stars of "Your rating *".', 'Stars 1 to 4 are shown as selected and star 5 as not selected, without using the mouse after step 1.', 'Condition: TCD-02-04\nTechnique: Error guessing\nMissing info: keyboard use is not stated in any source (Q-34).\nAssumption: the rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen until Q-34 is answered.')
('TR-03', 'TC-03-01', 'Verify that a review with rating 1 is submitted and shown with 1 star.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Emai

... [8128 characters truncated] ...

ssing info: expected result not stated in any source (Q-09).\nAssumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.')
('TR-05', 'TC-05-01', 'Verify that the review is not submitted when no star rating is selected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n2. Enter "Anna Smith" in "Name *".\n3. Enter "anna.smith@example.com" in "Email *".\n4. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names the rating field ("Your rating").', 'Condition: TCD-05-01\nTechnique: EP / BVA\nEdge case: just below the minimum.\nAssumption: the error names the rating field; wording checked for meaning, not exact text until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).')
('TR-06', 'TC-06-01', 'Verify that pressing Enter in "Your review *" starts a new line without submitting.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click in "Your review *".\n2. Type "Line one".\n3. Press Enter.\n4. Type "Line two".', '"Line two" is shown on a new line below "Line one" inside "Your review *"; no confirmation or error message appears and "Pending approval" stays 0.', 'Condition: TCD-06-01\nTechnique: EP')
('TR-06', 'TC-06-02', 'Verify that a multi-line review keeps its line breaks on the product page.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and type "Line one", press Enter, type "Line two", press Enter, type "Line three".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review starting with "Line one" in the "Reviews" list.', 'The review shows "Line one", "Line two" and "Line three" on three separate lines.', 'Condition: TCD-06-02\nTechnique: Error guessing\nMissing info: display of line breaks is not stated in any source (Q-35).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nAssumption: line breaks in a review are shown as entered until Q-35 is answered.')
('TR-07', 'TC-07-01', 'Verify that the review is not submitted when "Your review *" is empty.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Leave "Your review *" empty.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".', 'Condition: TCD-07-01\nTechnique: EP\nAssumption: wording checked for meaning, not exact text until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).')
('TR-08', 'TC-08-01', 'Verify that a review text within the allowed length is saved and shown as entered.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Soft fabric, true to size. Would buy again." in the "Reviews" list.', 'The review appears in the "Reviews" list with the text "Soft fabric, true to size. Would buy again." exactly as entered (same words, punctuation and letter case).', 'Condition: TCD-08-01\nTechnique: EP\nMissing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered.\nAssumption: the text used (43 characters) is between the minimum and the maximum length until Q-04 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.')
```

## AI (2026-10-21T04:23:48)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && SP=\"/c/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\"; mkdir -p \"$SP\"; PYTHONIOENCODING=utf-8 python -I -c \"\nimport openpyxl\nfrom openpyxl.utils import get_column_letter\np='submission/skills/test-data-generation/assets/test-data-template.xlsx'\nwb=openpyxl.load_workbook(p)\nfor ws in wb:\n    print('=====',ws.title,ws.dimensions, ws.freeze_panes, ws.auto_filter.ref)\n    for c,d in ws.column_dimensions.items(): print('  width',c,d.width)\n    for row in ws.iter_rows():\n        for c in row:\n            if c.value is not None: print(c.coordinate, repr(c.value), c.font.b, c.fill.fgColor.rgb, c.alignment.wrap_text)\np='submission/runs/run-1/test-cases.xlsx'\nwb=openpyxl.load_workbook(p)\nws=wb.active\nwith open('$SP/tc.txt','w',encoding='utf-8') as f:\n  for row in ws.iter_rows(min_row=2,values_only=True):\n    f.write('### '+str(row[1])+' | '+str(row[0])+'\\nSUM: '+str(row[2])+'\\nSTEPS:\\n'+str(row[4])+'\\nEXP: '+str(row[5])+'\\nNOTES:\\n'+str(row[6])+'\\n\\n')\nprint(ws.max_row)\n\"; wc -c \"$SP/tc.txt\"",
  "description": "Inspect template and dump test cases to scratch"
}
```

## Tool (2026-10-21T04:23:50)

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 15, in <module>
    with open('/c/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt','w',encoding='utf-8') as f:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/c/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt'
===== Test Data A1:F1 A2 A1:F1
  width A 12.0
  width B 18.0
  width C 20.0
  width D 50.0
  width E 12.0
  width F 45.0
A1 'TC ID' True 001F4E78 True
B1 'Data ID' True 001F4E78 True
C1 'Field' True 001F4E78 True
D1 'Value' True 001F4E78 True
E1 'Purpose' True 001F4E78 True
F1 'Notes' True 001F4E78 True
wc: /c/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt: No such file or directory
```

## AI (2026-10-21T04:23:55)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && SP=\"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\"; mkdir -p \"$SP\"; PYTHONIOENCODING=utf-8 python -I -c \"\nimport openpyxl\np='submission/runs/run-1/test-cases.xlsx'\nwb=openpyxl.load_workbook(p)\nws=wb.active\nn=0\nwith open('$SP/tc.txt','w',encoding='utf-8') as f:\n  for row in ws.iter_rows(min_row=2,values_only=True):\n    n+=1\n    f.write('### '+str(row[1])+' | '+str(row[0])+'\\nSUM: '+str(row[2])+'\\nSTEPS:\\n'+str(row[4])+'\\nEXP: '+str(row[5])+'\\nNOTES:\\n'+str(row[6])+'\\n\\n')\nprint(n)\npre=set(r[3] for r in ws.iter_rows(min_row=2,values_only=True)); print(len(pre))\nfor x in pre: print(repr(x)[:300])\n\"; wc -c \"$SP/tc.txt\"",
  "description": "Dump test cases to scratch file"
}
```

## Tool (2026-10-21T04:23:57)

```
145
52
'A build with sign-in; signed in as a test customer; session expired before Submit (for example by signing out in another tab).'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). The rating summary next to the product name (average and count) and the ratings of all listed reviews are written d
'A build with a moderator reject action (moderation steps to be confirmed, Q-07); the product page open in Chrome.'
'A build with a server set up (by the test team) to return an error on saving a review; product page open in Chrome.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). Today\'s date is written down.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). The "Reviews" list shows exactly 3 approved reviews rated 5, 4 and 3 (initial data; check before step 1).'
'A build with sign-in; signed in as test customer "Anna Smith" (anna.smith@example.com); product page open.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of [minimum - 1] letters "a" followed by one space (value set when Q-04 is answered) is ready in the clipboa
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [minimum] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the clipb
'The product page open in Chrome with exactly 50 approved reviews (on demo-1.0: submit and approve 47 reviews in one session on top of the 3 initial ones, without reloading).'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). The text "Pasted review: comfy and soft." (copied from Notepad) is ready in the clipboard.'
'A build with sign-in and orders; signed in as a test customer with a delivered order of this product; product page open.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). An email of exactly [maximum] characters: letters "a" followed by "@example.com" (value set when Q-06 is answered) 
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of about [maximum x 10] characters (value set when Q-04 is answered) is ready in the clipboard.'
'A build with sign-in and orders; signed in as a test customer whose only order of this product was cancelled or refunded; product page open.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). An email of exactly [maximum - 1] characters: letters "a" followed by "@example.com" (value set when Q-06 is answer
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [minimum - 1] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the c
'The product page open in Chrome with exactly [page size - 1] approved reviews (page size set when Q-23 is answered).'
'A build with a moderator reject action (Q-07); the product page open in Chrome.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A name of exactly [maximum - 1] letters "a" (value set when Q-05 is answered) is ready in the clipboard.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [minimum + 1] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the c
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear 
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).'
'A build that keeps reviews; product page reached from another page (so Back is available); product page open in Chrome.'
'The customer (Name "Anna Smith", Email "anna.smith@example.com") already has [limit - 1] reviews for this product (limit set when Q-12 is answered); product page open.'
'A build that keeps submitted reviews after the page is closed; the product page open in Chrome; no moderator action during the test.'
'A build with sign-in; not signed in (guest); product page open.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). At least 3 approved reviews with different dates and ratings are listed (initial data of demo-1.0).'
'The customer (Name "Anna Smith", Email "anna.smith@example.com") already has [limit] reviews for this product (Q-12); product page open.'
'A build that stores reviews on a server; the product page open in Chrome session A and in a second session B (another Chrome profile).'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the clipb
'The product page open in Chrome with exactly [page size] approved reviews (page size set when Q-23 is answered).'
'A build with sign-in and orders; signed in as a test customer with no order of this product; product page open.'
'The customer already has [limit] reviews for this product (Q-12); product page open.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear 
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum + 1] characters (letter "a" repeated, last character "b"; value set when Q-04 is answere
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). Name "Anna Smith" and Email "anna.smith@example.com" are saved in this browser (they are filled on load).'
'The product page open in Chrome with exactly [page size + 1] approved reviews (page size set when Q-23 is answered).'
'A product with 0 approved reviews open in Chrome.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). An email of exactly [maximum + 1] characters: letters "a" followed by "@example.com" (value set when Q-06 is answer
'A build with sign-in where Name is prefilled and editable (Q-02); signed in as test customer "Anna Smith"; product page open.'
'A build with a moderator reject action (Q-07); the rating summary (average and count) written down.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). Name "Anna Smith" and Email "anna.smith@example.com" are saved in this browser (TC-37-01 done; they are filled on l
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum] letters "a" with no spaces (value set when Q-04 is answered) is ready in the clipboard.
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum - 1] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the c
'A build with two products A and B; the page of product A open in Chrome.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A name of exactly [maximum + 1] letters "a" (value set when Q-05 is answered) is ready in the clipboard.'
'A build with a server; product page open in Chrome with DevTools (F12) open on the Network tab.'
'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A name of exactly [maximum] letters "a" (value set when Q-05 is answered) is ready in the clipboard.'
'A build with two products; the customer already has [limit] reviews for product A (Q-12); page of product B open.'
'A build that keeps reviews after the page is closed; the product page open in Chrome.'
'A build that keeps reviews after reload; product page open in Chrome.'
116162 C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt
```

## AI (2026-10-21T04:24:02)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && PYTHONIOENCODING=utf-8 python -I -c \"\nimport openpyxl\nws=openpyxl.load_workbook('submission/runs/run-1/test-cases.xlsx').active\nfrom collections import Counter\nc=Counter()\nfor r in ws.iter_rows(min_row=2,values_only=True):\n    n=(r[6] or '')\n    first=n.split('\\n')[0]\n    k=first.split(':')[0]\n    c[k]+=1\n    if not first.startswith('Condition'): print(r[1], repr(first[:150]))\n    if 'BLOCKED' in n.upper() or 'NOT RUN' in n.upper(): print('  contains', r[1])\nprint(c)\n\"",
  "description": "Check Notes prefixes for BLOCKED/NOT RUN"
}
```

## Tool (2026-10-21T04:24:03)

```
TC-09-01 'BLOCKED � waiting for Q-04'
  contains TC-09-01
TC-09-02 'BLOCKED � waiting for Q-04'
  contains TC-09-02
TC-09-03 'BLOCKED � waiting for Q-04'
  contains TC-09-03
TC-09-04 'BLOCKED � waiting for Q-04'
  contains TC-09-04
TC-10-01 'BLOCKED � waiting for Q-04'
  contains TC-10-01
TC-10-02 'BLOCKED � waiting for Q-04'
  contains TC-10-02
TC-10-03 'BLOCKED � waiting for Q-04'
  contains TC-10-03
TC-10-04 'BLOCKED � waiting for Q-04'
  contains TC-10-04
TC-11-04 'BLOCKED � waiting for Q-04'
  contains TC-11-04
TC-12-01 'OBSERVE ONLY � no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict)'
TC-12-03 'OBSERVE ONLY � no verdict until Q-15 is answered'
TC-12-04 'OBSERVE ONLY � no verdict until Q-15 is answered'
TC-12-05 'OBSERVE ONLY � no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict)'
TC-13-01 'NOT RUN on demo-1.0 � no second visitor session; reviews exist only in the open page'
  contains TC-13-01
TC-13-02 'NOT RUN on demo-1.0 � a reload restores the initial data, so a pending review cannot be kept'
  contains TC-13-02
TC-15-01 'NOT RUN on demo-1.0 � no reject action'
  contains TC-15-01
TC-15-02 'NOT RUN on demo-1.0 � no reject action'
  contains TC-15-02
TC-16-01 'OBSERVE ONLY � no verdict until Q-08 is answered'
TC-16-02 'OBSERVE ONLY � no verdict until Q-08 is answered'
TC-18-03 'OBSERVE ONLY � no verdict until Q-15 is answered'
TC-18-04 'BLOCKED � waiting for Q-04'
  contains TC-18-04
TC-20-01 'OBSERVE ONLY � no verdict until Q-10 is answered'
TC-20-02 'OBSERVE ONLY � no verdict until Q-10 is answered'
TC-20-03 'NOT RUN on demo-1.0 � a reload restores the initial data'
  contains TC-20-03
TC-21-01 'NOT RUN on demo-1.0 � needs 50 approved reviews; creating 47 by hand is not done this round'
  contains TC-21-01
TC-21-02 'BLOCKED � waiting for Q-23'
  contains TC-21-02
TC-21-03 'BLOCKED � waiting for Q-23'
  contains TC-21-03
TC-21-04 'BLOCKED � waiting for Q-23'
  contains TC-21-04
TC-22-01 'NOT RUN on demo-1.0 � the only product starts with approved reviews'
  contains TC-22-01
TC-22-02 'NOT RUN on demo-1.0 � the only product starts with approved reviews'
  contains TC-22-02
TC-22-03 'NOT RUN on demo-1.0 � the only product starts with approved reviews'
  contains TC-22-03
TC-23-01 'OBSERVE ONLY � no verdict until Q-11 is answered'
TC-23-02 'OBSERVE ONLY � no verdict until Q-11 is answered'
TC-23-03 'NOT RUN on demo-1.0 � no reject action'
  contains TC-23-03
TC-23-04 'OBSERVE ONLY � no verdict until Q-11 is answered'
TC-23-05 'OBSERVE ONLY � no verdict until Q-11 is answered'
TC-23-06 'NOT RUN on demo-1.0 � the only product starts with approved reviews'
  contains TC-23-06
TC-24-01 'NOT RUN on demo-1.0 � one product only'
  contains TC-24-01
TC-24-02 'NOT RUN on demo-1.0 � one product only'
  contains TC-24-02
TC-26-01 'NOT RUN on demo-1.0 � no sign-in or orders'
  contains TC-26-01
TC-26-02 'NOT RUN on demo-1.0 � no sign-in or orders'
  contains TC-26-02
TC-26-03 'NOT RUN on demo-1.0 � no sign-in'
  contains TC-26-03
TC-26-04 'NOT RUN on demo-1.0 � no sign-in or orders'
  contains TC-26-04
TC-27-01 'NOT RUN on demo-1.0 � no sign-in'
  contains TC-27-01
TC-27-02 'NOT RUN on demo-1.0 � no sign-in'
  contains TC-27-02
TC-29-04 'OBSERVE ONLY � no verdict until Q-05 is answered'
TC-29-05 'OBSERVE ONLY � no verdict until Q-05 is answered'
TC-29-06 'OBSERVE ONLY � no verdict until Q-05 and Q-20 are answered'
TC-29-07 'OBSERVE ONLY � no verdict until Q-05 is answered'
TC-29-08 'BLOCKED � waiting for Q-05'
  contains TC-29-08
TC-29-09 'BLOCKED � waiting for Q-05'
  contains TC-29-09
TC-29-10 'BLOCKED � waiting for Q-05'
  contains TC-29-10
TC-31-10 'BLOCKED � waiting for Q-06'
  contains TC-31-10
TC-31-11 'BLOCKED � waiting for Q-06'
  contains TC-31-11
TC-31-12 'BLOCKED � waiting for Q-06'
  contains TC-31-12
TC-36-02 'OBSERVE ONLY � no verdict until Q-14 is answered'
TC-37-03 'OBSERVE ONLY � no verdict until Q-14 is answered'
TC-37-06 'OBSERVE ONLY � no verdict until Q-14 is answered'
TC-38-01 'OBSERVE ONLY � no verdict until Q-14 is answered'
TC-38-02 'OBSERVE ONLY � no verdict until Q-14 is answered'
TC-39-01 'BLOCKED � waiting for Q-12'
  contains TC-39-01
TC-39-02 'BLOCKED � waiting for Q-12'
  contains TC-39-02
TC-39-03 'NOT RUN on demo-1.0 � one product only; also BLOCKED � waiting for Q-12'
  contains TC-39-03
TC-39-04 'BLOCKED � waiting for Q-12 (and Q-01, Q-02 for how the customer is identified)'
  contains TC-39-04
TC-40-03 'NOT RUN on demo-1.0 � a reload restores the initial data'
  contains TC-40-03
TC-40-04 'NOT RUN on demo-1.0 � Back/Forward reloads the page and restores the initial data'
  contains TC-40-04
TC-41-01 'NOT RUN on demo-1.0 � no server or network'
  contains TC-41-01
TC-41-02 'NOT RUN on demo-1.0 � no server'
  contains TC-41-02
TC-41-03 'NOT RUN on demo-1.0 � no sign-in'
  contains TC-41-03
TC-41-04 'NOT RUN on demo-1.0 � no server or network'
  contains TC-41-04
Counter({'Condition': 75, 'BLOCKED � waiting for Q-04': 10, 'OBSERVE ONLY � no verdict until Q-14 is answered': 5, 'NOT RUN on demo-1.0 � the only product starts with approved reviews': 4, 'OBSERVE ONLY � no verdict until Q-11 is answered': 4, 'NOT RUN on demo-1.0 � no sign-in': 4, 'OBSERVE ONLY � no verdict until Q-15 is answered': 3, 'NOT RUN on demo-1.0 � no reject action': 3, 'BLOCKED � waiting for Q-23': 3, 'NOT RUN on demo-1.0 � no sign-in or orders': 3, 'OBSERVE ONLY � no verdict until Q-05 is answered': 3, 'BLOCKED � waiting for Q-05': 3, 'BLOCKED � waiting for Q-06': 3, 'OBSERVE ONLY � no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict)': 2, 'OBSERVE ONLY � no verdict until Q-08 is answered': 2, 'OBSERVE ONLY � no verdict until Q-10 is answered': 2, 'NOT RUN on demo-1.0 � a reload restores the initial data': 2, 'NOT RUN on demo-1.0 � one product only': 2, 'BLOCKED � waiting for Q-12': 2, 'NOT RUN on demo-1.0 � no server or network': 2, 'NOT RUN on demo-1.0 � no second visitor session; reviews exist only in the open page': 1, 'NOT RUN on demo-1.0 � a reload restores the initial data, so a pending review cannot be kept': 1, 'NOT RUN on demo-1.0 � needs 50 approved reviews; creating 47 by hand is not done this round': 1, 'OBSERVE ONLY � no verdict until Q-05 and Q-20 are answered': 1, 'NOT RUN on demo-1.0 � one product only; also BLOCKED � waiting for Q-12': 1, 'BLOCKED � waiting for Q-12 (and Q-01, Q-02 for how the customer is identified)': 1, 'NOT RUN on demo-1.0 � Back/Forward reloads the page and restores the initial data': 1, 'NOT RUN on demo-1.0 � no server': 1})
```

## AI (2026-10-21T04:24:09)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && sed -n '1,200p' submission/runs/run-1/test-design.md | head -c 30000",
  "description": "Read test design (first part)"
}
```

## Tool (2026-10-21T04:24:10)

```
# Test design: US-VP02 Submit a Product Review

Input: runs/run-1/test-requirements.xlsx (41 TRs, TR-01 to TR-41) · Answers used: none (runs/run-1/clarification-questions.md has questions Q-01 to Q-38 (Q-33 to Q-38 added after review), no product owner answers yet) · Date: 2026-10-21

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
| Leading / trailing spaces | Trimmed in Review, Name and Email; a field of only spaces counts as empty | Assumption | Q-17 |
| Name length and allowed characters | Not stated; no value used | Missing info | Q-05 |
| Email format rule and maximum length | Standard format text@domain.tld taken as the working rule; maximum length not stated | Assumption (format), Missing info (length) | Q-06 |
| Email not published | The email is never shown on the product page | Confirmed | mockup-1.png (R3) |
| HTML, scripts and links in text | Shown as plain text, removed or rejected: not stated. Never executed in any case | Missing info (handling), Assumption (never executed) | Q-15 |
| Validation timing | Fields are checked on Submit only | Assumption | Q-19 |
| Error messages | Each error names the field concerned; wording checked for meaning, not exact text | Assumption | Q-20 |
| Success message | Says the review was received and waits for approval | Assumption | Q-21 |
| Form after success | Customer stays on the product page; form cleared; Name and Email stay only if the save checkbox was ticked | Assumption | Q-22 |
| Review states | Submitted review is Pending; only Approved reviews are displayed | Confirmed | AC-03 (R4, R5), app-note.md |
| Moderation (who approves, reject, what happens to a rejected review) | Not stated | Missing info | Q-07 |
| Moderator in demo-1.0 | "Moderator: approve pending reviews" approves every pending review; used only as a test helper | Confirmed (helper), Assumption (not part of the feature) | environment.md, app-note.md |
| Author's view of own pending review | Not stated | Missing info | Q-08 |
| Details per displayed review | Star rating, reviewer name, date, review text; never the email | Assumption | product-review-rules.md A2; Q-09 |
| Date shown | Submit date, any unambiguous format | Assumption | Q-24 |
| Order of reviews | Not stated | Missing info | Q-10 |
| Paging | All approved reviews shown on one page | Assumption | Q-23 |
| No approved reviews | A short message saying there are no reviews yet | Assumption | Q-25 |
| Rating summary and count | Whether shown and how rounded: not stated; if shown, approved reviews only | Missing info | Q-11 |
| Who may review | Sign-in and purchase check not stated | Missing info | Q-01 |
| Name / Email for a signed-in customer | Story vs mockup-1 conflict | Missing info | Q-02 |
| Reviews per customer and product | Not stated | Missing info | Q-12 |
| Save checkbox default | Unchecked | Confirmed | mockup-1.png (F5) |
| Save checkbox stores | Name and Email only, in this browser | Assumption | Q-13, Q-14 |
| What is kept when the checkbox is not ticked, how long data is kept, how it is removed | Not stated | Missing info | Q-14 |
| Double submit | Only one review is created | Assumption | Q-28 |
| Server / network error | A message says the review was not submitted; the entered data is kept | Assumption | Q-29 |
| Browser and environment | Build demo-1.0, Chrome; other browsers and devices not stated | Confirmed (Chrome), Assumption (desktop Chrome, English) | environment.md, app-note.md; Q-31 |
| Demo-1.0 data | One product; reload restores the initial data; no sign-in | Confirmed | app-note.md, environment.md |

## Test conditions

### TR-01: Verify that the "Your rating *" field shows 5 stars.

Technique(s): Equivalence Partitioning - the rating control has one valid display state (as in mockup-1); one condition covers it.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-01-01 | EP | When the form opens, "Your rating *" shows exactly 5 star icons and none of them is selected. | Positive | |

### TR-02: Verify that the customer can select a rating by clicking a star, and the selected stars are shown as selected.

Technique(s): Equivalence Partitioning - whole-star values 1 to 5 form one valid partition (a middle value represents it; the ends are in TR-03) and half-star values form one invalid partition. Error guessing - hover and keyboard use are common sources of rating defects.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-02-01 | EP | From no rating, clicking the 3rd star selects rating 3: stars 1 to 3 are shown as selected and stars 4 and 5 as not selected. | Positive | Assumption: the rating is a whole number from 1 to 5 until Q-03 is answered. |
| TCD-02-02 | EP | Clicking on the left half of a star does not set a half-star value (for example 2.5); the rating shown and saved is a whole number. | Negative | Missing info: whether half stars are allowed (Q-03). |
| TCD-02-03 | Error guessing | Moving the pointer over the stars without clicking, then moving it away, leaves the selected rating unchanged. | Negative | Assumption: a hover preview, if any, is not kept until Q-36 is answered. |
| TCD-02-04 | Error guessing | The rating can be selected with the keyboard only (Tab to the stars, then arrow keys, Space or Enter), and the selection is shown. | Positive | Missing info: keyboard use is not stated in any source (Q-34). |

### TR-03: Verify that both the lowest rating (1 star) and the highest rating (5 stars) can be selected and are saved with the review.

Technique(s): Boundary Value Analysis - the rating is a range 1 to 5 (Assumption). Just below the minimum (0 = no rating) is TCD-05-01; just above the maximum (6) cannot be entered because only 5 stars exist (TCD-01-01), so no separate condition.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-03-01 | BVA | Rating 1 (on the minimum): the review is submitted and, after approval, is shown with 1 star. | Positive | Edge case: value exactly at the minimum.<br>Assumption: rating range 1 to 5 until Q-03 is answered. |
| TCD-03-02 | BVA | Rating 2 (just above the minimum): the review is submitted and, after approval, is shown with 2 stars. | Positive | Assumption: rating range 1 to 5 until Q-03 is answered. |
| TCD-03-03 | BVA | Rating 4 (just below the maximum): the review is submitted and, after approval, is shown with 4 stars. | Positive | Assumption: rating range 1 to 5 until Q-03 is answered. |
| TCD-03-04 | BVA | Rating 5 (on the maximum): the review is submitted and, after approval, is shown with 5 stars. | Positive | Edge case: value exactly at the maximum.<br>Assumption: rating range 1 to 5 until Q-03 is answered. |

### TR-04: Verify that the customer can change the selected rating before submitting, and only the last selected rating is saved.

Technique(s): State transition - states "No rating" and "Rating n"; events "click star m", "click the selected star again", "reload page", "Submit". Each valid transition once, plus the transition that is not allowed (clearing to "No rating" by clicking).

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-04-01 | State transition | Rating 2, click the 5th star: the rating becomes 5 and stars 1 to 5 are shown as selected (increase). | Positive | Assumption: clicking another star changes the rating (Q-16). |
| TCD-04-02 | State transition | Rating 5, click the 2nd star: the rating becomes 2 and only stars 1 and 2 are shown as selected (decrease). | Positive | Assumption: clicking another star changes the rating (Q-16). |
| TCD-04-03 | State transition | Rating 3, click the 3rd star again: the rating stays 3; it does not go back to "No rating". | Negative | Assumption: the rating cannot be cleared by clicking (Q-16). |
| TCD-04-04 | State transition | Rating 3, reload the page: the form opens with "No rating". | Positive | Assumption: reloading is the only way back to "No rating" (Q-16). |
| TCD-04-05 | State transition | Rating changed several times (1, then 4, then 2, then 3) and then Submit: the saved and, after approval, displayed rating is 3. | Positive | |

### TR-05: Verify that the review cannot be submitted when no star rating is selected.

Technique(s): Equivalence Partitioning (invalid partition "no rating") with Boundary Value Analysis (0 is just below the minimum 1).

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-05-01 | EP / BVA | No star selected (0, just below the minimum), Review, Name and Email valid, Submit: the review is not submitted and an error names the rating field. | Negative | Edge case: just below the minimum.<br>Assumption: the error names the rating field; wording checked for meaning, not exact text (Q-20). |

### TR-06: Verify that a multi-line text box "Your review *" is provided for the review comment.

Technique(s): Equivalence Partitioning - multi-line input is one valid partition. Error guessing - line breaks are often lost when the text is displayed.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-06-01 | EP | "Your review *" accepts text on several lines: pressing Enter starts a new line inside the box and does not submit the form. | Positive | |
| TCD-06-02 | Error guessing | A review written on several lines is shown on the product page, after approval, with its line breaks kept. | Positive | Missing info: display of line breaks is not stated in any source (Q-35). |

### TR-07: Verify that the review cannot be submitted when "Your review" is empty.

Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field (0 characters).

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-07-01 | EP | "Your review" empty (0 characters), rating, Name and Email valid, Submit: the review is not submitted and an error names "Your review". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |

### TR-08: Verify that review text within the allowed length is accepted and saved as entered.

Technique(s): Equivalence Partitioning - one valid length partition (between the minimum and the maximum) and valid character types. Error guessing - pasted text and non-Latin characters are frequent defect sources.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-08-01 | EP | Review text with a length between the minimum and the maximum: the review is submitted and, after approval, the text is shown exactly as entered. | Positive | Missing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered. |
| TCD-08-02 | Error guessing | Review text with accented letters (é, ü), non-Latin letters (日本語), digits, punctuation and an emoji: accepted and shown unchanged. | Positive | Assumption: no character restriction in "Your review" until Q-37 is answered. |
| TCD-08-03 | Error guessing | Review text pasted from the clipboard is accepted and saved in the same way as typed text. | Positive | |

### TR-09: Verify that review text of exactly the minimum length and exactly the maximum length is accepted.

Technique(s): Boundary Value Analysis - the review has a length range (minimum and maximum). Values on and just inside each boundary are here; just outside are in TR-10. The exact numbers are not in any source.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-09-01 | BVA | Review length = minimum: accepted. | Positive | Edge case: value exactly at the minimum.<br>Missing info: minimum length not stated (Q-04). |
| TCD-09-02 | BVA | Review length = minimum + 1: accepted. | Positive | Missing info: minimum length not stated (Q-04). |
| TCD-09-03 | BVA | Review length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-04). |
| TCD-09-04 | BVA | Review length = maximum: accepted and, after approval, shown in full (not cut). | Positive | Edge case: value exactly at the maximum.<br>Missing info: maximum length not stated (Q-04). |

### TR-10: Verify that review text shorter than the minimum or longer than the maximum is not accepted.

Technique(s): Boundary Value Analysis - values just outside each boundary, one invalid value per condition. Error guessing - very long pasted text.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-10-01 | BVA | Review length = minimum - 1, Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: one character below the minimum.<br>Missing info: minimum length not stated (Q-04). If the minimum is 1, this is TCD-07-01 and is not repeated. |
| TCD-10-02 | BVA | Typing maximum + 1 characters: typing stops at the maximum and the box holds exactly maximum characters. | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: typing stops at the maximum (Q-18). |
| TCD-10-03 | BVA | Pasting text of maximum + 1 characters: the text in the box is cut at the maximum. | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |
| TCD-10-04 | Error guessing | Pasting very long text (about ten times the maximum): the box holds at most the maximum and the page stays responsive. | Negative | Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |

### TR-11: Verify that review text made only of spaces is treated as empty and the review is not submitted.

Technique(s): Error guessing - spaces-only and space-padded input; Boundary Value Analysis - trimmed length just below the minimum.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-11-01 | Error guessing | "Your review" contains only spaces, Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
| TCD-11-02 | Error guessing | "Your review" contains only line breaks (Enter pressed several times), Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: line breaks are treated like spaces (Q-17). |
| TCD-11-03 | Error guessing | Valid review text with leading and trailing spaces: accepted and, after approval, shown without the leading and trailing spaces. | Positive | Assumption: spaces are trimmed (Q-17). |
| TCD-11-04 | BVA | Review of (minimum - 1) visible characters plus one trailing space (length = minimum only if the space is counted), Submit: the review is not submitted. | Negative | Edge case: length reaches the minimum only through a space.<br>Assumption: length is counted after trimming (Q-17).<br>Missing info: minimum length not stated (Q-04). |

### TR-12: Verify that HTML tags, script code and links entered in "Your review" or "Name" are never run as code on the product page.

Technique(s): Error guessing - script injection through free text is a known high-risk defect; each field and each injection form is tested separately so the result shows which one failed.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-12-01 | Error guessing | "Your review" contains `<script>alert(1)</script>`: no script runs, on submit or on the product page after approval. | Negative | Missing info: shown as plain text, removed or rejected (Q-15).<br>Assumption: content is never executed (Q-15).<br>Risk: script injection would affect every visitor of the product page. |
| TCD-12-02 | Error guessing | "Your review" contains `<img src=x onerror=alert(1)>`: no script runs and no image element is added to the page. | Negative | Missing info: handling not stated (Q-15).<br>Risk: script injection through an HTML attribute. |
| TCD-12-03 | Error guessing | "Your review" contains harmless HTML `<b>bold</b>`: the text is not rendered as bold HTML; it is shown as plain text, removed or rejected as confirmed for Q-15. | Negative | Missing info: handling not stated (Q-15). |
| TCD-12-04 | Error guessing | "Your review" contains a web link (`https://example.com`): it is shown, removed or rejected as confirmed for Q-15, and is not turned into a clickable link unless Q-15 allows it. | Negative | Missing info: handling of links not stated (Q-15). |
| TCD-12-05 | Error guessing | "Name" contains `<script>alert(1)</script>`: no script runs where the name is shown. | Negative | Missing info: handling not stated (Q-05, Q-15).<br>Risk: script injection through the reviewer name. |

### TR-13: Verify that a newly submitted review is not displayed on the product page while it waits for approval.

Technique(s): State transition - Submit moves a review from "not existing" to "Pending"; in "Pending" the review must not be displayed to other visitors. (The author's own view is TR-16.)

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-13-01 | State transition | After a valid Submit (state Pending), the review does not appear in the reviews list for another visitor of the product page. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: demo-1.0 has no sign-in and keeps data only in the open page, so "another visitor" cannot be simulated there (environment.md); check in the author's page per TCD-16-01. |
| TCD-13-02 | State transition | A pending review is still not displayed after the product page is opened again later. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: in demo-1.0 a reload restores the initial data (environment.md), so this needs a build that keeps data. |

### TR-14: Verify that a submitted review is displayed on the product page after it is approved.

Technique(s): State transition - event "approve" moves Pending to Approved (valid transition); approving again or with nothing pending must not create entries (invalid transitions).

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-14-01 | State transition | Pending review, moderator approves: the review appears in the reviews list on the product page. | Positive | Missing info: who approves and how (Q-07).<br>Assumption: in demo-1.0 the "Moderator: approve pending reviews" helper plays the moderator (environment.md). |
| TCD-14-02 | State transition | Approved review, approve action used again: the review is shown once only (no duplicate). | Negative | Edge case: approve twice.<br>Missing info: moderation workflow (Q-07). |
| TCD-14-03 | State transition | No pending review, approve action used: no new or empty review appears. | Negative | Edge case: approve with nothing pending.<br>Missing info: moderation workflow (Q-07). |

### TR-15: Verify that a rejected review is never displayed on the product page.

Technique(s): State transition - event "reject" moves Pending to Rejected; Rejected must never lead to "displayed" through other events.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-15-01 | State transition | Pending review, moderator rejects: the review does not appear on the product page. | Positive | Missing info: whether a review can be rejected and what happens to it (Q-07). Demo-1.0 has no reject action (environment.md). |
```

## AI (2026-10-21T04:24:16)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && PYTHONIOENCODING=utf-8 python -I -c \"\nimport openpyxl\nws=openpyxl.load_workbook('submission/runs/run-1/test-cases.xlsx').active\nstd='demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; \\\"Pending approval: 0\\\"; nothing saved in this browser (Name * and Email * empty on load).'\nk=0\nfor r in ws.iter_rows(min_row=2,values_only=True):\n    n=(r[6] or '')\n    if n.startswith('BLOCKED') or n.startswith('NOT RUN'): continue\n    k+=1\n    pre=r[3].replace(std,'[STD]')\n    notes='; '.join(l for l in n.split('\\n') if not l.startswith('Assumption: the other values') )\n    print('###',r[1],'|',r[2]); print('PRE:',pre); print(r[4]); print('NOTES:',notes); print()\nprint(k)\n\" > \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/run.txt\"; wc -c \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/run.txt\"",
  "description": "Extract runnable test cases to scratch"
}
```

## Tool (2026-10-21T04:24:18)

```
Traceback (most recent call last):
  File "<string>", line 12, in <module>
    print('###',r[1],'|',r[2]); print('PRE:',pre); print(r[4]); print('NOTES:',notes); print()
                                                   ~~~~~^^^^^^
  File "C:\Python\Python314\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode characters in position 79-81: character maps to <undefined>
10678 C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/run.txt
```

## AI (2026-10-21T04:24:25)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && python -I -c \"\nimport sys; sys.stdout.reconfigure(encoding='utf-8')\nimport openpyxl\nws=openpyxl.load_workbook('submission/runs/run-1/test-cases.xlsx').active\nstd='demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; \\\"Pending approval: 0\\\"; nothing saved in this browser (Name * and Email * empty on load).'\nk=0\nfor r in ws.iter_rows(min_row=2,values_only=True):\n    n=(r[6] or '')\n    if n.startswith('BLOCKED') or n.startswith('NOT RUN'): continue\n    k+=1\n    pre=r[3].replace(std,'[STD]')\n    notes='; '.join(l for l in n.split('\\n') if not l.startswith('Assumption: the other values') )\n    print('###',r[1],'|',r[2]); print('PRE:',pre); print(r[4]); print('NOTES:',notes); print()\nprint(k)\n\" > \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/run.txt\"; wc -c \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/run.txt\"",
  "description": "Extract runnable test cases with UTF-8 output"
}
```

## Tool (2026-10-21T04:24:28)

```
57204 C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/run.txt
```

## AI (2026-10-21T04:24:30)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\run.txt",
  "allow_large": true
}
```

## Tool (2026-10-21T04:24:31)

```
1	### TC-01-01 | Verify that "Your rating *" shows exactly 5 stars, none selected, when the form opens.
2	PRE: [STD]
3	1. Scroll to the "Add a review" form.
4	2. Look at the stars next to "Your rating *" without clicking them.
5	NOTES: Condition: TCD-01-01; Technique: EP
6	
7	### TC-02-01 | Verify that clicking the 3rd star selects rating 3.
8	PRE: [STD]
9	1. Click the 3rd star of "Your rating *".
10	2. Look at the 5 stars of "Your rating *".
11	NOTES: Condition: TCD-02-01; Technique: EP; Assumption: the rating is a whole number from 1 to 5 until Q-03 is answered.
12	
13	### TC-02-02 | Verify that clicking the left half of a star does not set a half-star rating.
14	PRE: [STD]
15	1. Click the left half of the 3rd star of "Your rating *".
16	2. Look at the stars of "Your rating *".
17	3. Enter "Half star check." in "Your review *".
18	4. Enter "Anna Smith" in "Name *".
19	5. Enter "anna.smith@example.com" in "Email *".
20	6. Click "Submit".
21	7. Click "Moderator: approve pending reviews".
22	8. Find the review "Half star check." in the "Reviews" list.
23	NOTES: Condition: TCD-02-02; Technique: EP; Missing info: whether half stars are allowed (Q-03).; Assumption: the rating is a whole number from 1 to 5, one per star until Q-03 is answered.
24	
25	### TC-02-03 | Verify that moving the pointer over the stars without clicking keeps the selected rating.
26	PRE: [STD]
27	1. Click the 2nd star of "Your rating *".
28	2. Move the pointer over the 5th star of "Your rating *" without clicking.
29	3. Move the pointer away from the stars.
30	4. Look at the 5 stars of "Your rating *".
31	NOTES: Condition: TCD-02-03; Technique: Error guessing; Assumption: a hover preview, if any, is not kept until Q-36 is answered.; Missing info: expected result not stated in any source (Q-36).
32	
33	### TC-02-04 | Verify that a rating can be selected with the keyboard only.
34	PRE: [STD]
35	1. Click on the info text "Your email address will not be published. Required fields are marked *" to place the focus before the form.
36	2. Press Tab until a star of "Your rating *" has the focus.
37	3. Use the arrow keys to move to the 4th star and press Space (if nothing changes, press Enter).
38	4. Look at the 5 stars of "Your rating *".
39	NOTES: Condition: TCD-02-04; Technique: Error guessing; Missing info: keyboard use is not stated in any source (Q-34).; Assumption: the rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen until Q-34 is answered.
40	
41	### TC-03-01 | Verify that a review with rating 1 is submitted and shown with 1 star.
42	PRE: [STD]
43	1. Click the 1st star of "Your rating *".
44	2. Enter "Rating check: one star." in "Your review *".
45	3. Enter "Anna Smith" in "Name *".
46	4. Enter "anna.smith@example.com" in "Email *".
47	5. Click "Submit".
48	6. Click "Moderator: approve pending reviews".
49	7. Find the review "Rating check: one star." in the "Reviews" list.
50	NOTES: Condition: TCD-03-01; Technique: BVA; Edge case: value exactly at the minimum.; Assumption: rating range 1 to 5 until Q-03 is answered.; Missing info: expected result not stated in any source (Q-03, Q-09).; Assumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.
51	
52	### TC-03-02 | Verify that a review with rating 2 is submitted and shown with 2 stars.
53	PRE: [STD]
54	1. Click the 2nd star of "Your rating *".
55	2. Enter "Rating check: two stars." in "Your review *".
56	3. Enter "Anna Smith" in "Name *".
57	4. Enter "anna.smith@example.com" in "Email *".
58	5. Click "Submit".
59	6. Click "Moderator: approve pending reviews".
60	7. Find the review "Rating check: two stars." in the "Reviews" list.
61	NOTES: Condition: TCD-03-02; Technique: BVA; Assumption: rating range 1 to 5 until Q-03 is answered.; Missing info: expected result not stated in any source (Q-03, Q-09).; Assumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.
62	
63	### TC-03-03 | Verify that a review with rating 4 is submitted and shown with 4 stars.
64	PRE: [STD]
65	1. Click the 4th star of "Your rating *".
66	2. Enter "Rating check: four stars." in "Your review *".
67	3. Enter "Anna Smith" in "Name *".
68	4. Enter "anna.smith@example.com" in "Email *".
69	5. Click "Submit".
70	6. Click "Moderator: approve pending reviews".
71	7. Find the review "Rating check: four stars." in the "Reviews" list.
72	NOTES: Condition: TCD-03-03; Technique: BVA; Assumption: rating range 1 to 5 until Q-03 is answered.; Missing info: expected result not stated in any source (Q-03, Q-09).; Assumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.
73	
74	### TC-03-04 | Verify that a review with rating 5 is submitted and shown with 5 stars.
75	PRE: [STD]
76	1. Click the 5th star of "Your rating *".
77	2. Enter "Rating check: five stars." in "Your review *".
78	3. Enter "Anna Smith" in "Name *".
79	4. Enter "anna.smith@example.com" in "Email *".
80	5. Click "Submit".
81	6. Click "Moderator: approve pending reviews".
82	7. Find the review "Rating check: five stars." in the "Reviews" list.
83	NOTES: Condition: TCD-03-04; Technique: BVA; Edge case: value exactly at the maximum.; Assumption: rating range 1 to 5 until Q-03 is answered.; Missing info: expected result not stated in any source (Q-03, Q-09).; Assumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.
84	
85	### TC-04-01 | Verify that clicking the 5th star after the 2nd changes the rating to 5.
86	PRE: [STD]
87	1. Click the 2nd star of "Your rating *".
88	2. Click the 5th star of "Your rating *".
89	3. Look at the 5 stars of "Your rating *".
90	NOTES: Condition: TCD-04-01; Technique: State transition; Assumption: clicking another star changes the rating until Q-16 is answered.; Missing info: expected result not stated in any source (Q-16).
91	
92	### TC-04-02 | Verify that clicking the 2nd star after the 5th changes the rating to 2.
93	PRE: [STD]
94	1. Click the 5th star of "Your rating *".
95	2. Click the 2nd star of "Your rating *".
96	3. Look at the 5 stars of "Your rating *".
97	NOTES: Condition: TCD-04-02; Technique: State transition; Assumption: clicking another star changes the rating until Q-16 is answered.; Missing info: expected result not stated in any source (Q-16).
98	
99	### TC-04-03 | Verify that clicking the selected 3rd star again does not clear the rating.
100	PRE: [STD]
101	1. Click the 3rd star of "Your rating *".
102	2. Click the 3rd star of "Your rating *".
103	3. Look at the 5 stars of "Your rating *".
104	NOTES: Condition: TCD-04-03; Technique: State transition; Assumption: the rating cannot be cleared by clicking until Q-16 is answered.; Missing info: expected result not stated in any source (Q-16).
105	
106	### TC-04-04 | Verify that reloading the page resets a selected rating to no rating.
107	PRE: [STD]
108	1. Click the 3rd star of "Your rating *".
109	2. Reload the page (F5).
110	3. Look at the 5 stars of "Your rating *".
111	NOTES: Condition: TCD-04-04; Technique: State transition; Assumption: reloading is the only way back to "No rating" until Q-16 is answered.
112	
113	### TC-04-05 | Verify that only the last selected rating is saved after several changes.
114	PRE: [STD]
115	1. Click the 1st star of "Your rating *".
116	2. Click the 4th star of "Your rating *".
117	3. Click the 2nd star of "Your rating *".
118	4. Click the 3rd star of "Your rating *".
119	5. Enter "Changed rating, final is three." in "Your review *".
120	6. Enter "Anna Smith" in "Name *".
121	7. Enter "anna.smith@example.com" in "Email *".
122	8. Click "Submit".
123	9. Click "Moderator: approve pending reviews".
124	10. Find the review "Changed rating, final is three." in the "Reviews" list.
125	NOTES: Condition: TCD-04-05; Technique: State transition; Missing info: expected result not stated in any source (Q-09).; Assumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.
126	
127	### TC-05-01 | Verify that the review is not submitted when no star rating is selected.
128	PRE: [STD]
129	1. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
130	2. Enter "Anna Smith" in "Name *".
131	3. Enter "anna.smith@example.com" in "Email *".
132	4. Click "Submit".
133	NOTES: Condition: TCD-05-01; Technique: EP / BVA; Edge case: just below the minimum.; Assumption: the error names the rating field; wording checked for meaning, not exact text until Q-20 is answered.; Missing info: expected result not stated in any source (Q-20).
134	
135	### TC-06-01 | Verify that pressing Enter in "Your review *" starts a new line without submitting.
136	PRE: [STD]
137	1. Click in "Your review *".
138	2. Type "Line one".
139	3. Press Enter.
140	4. Type "Line two".
141	NOTES: Condition: TCD-06-01; Technique: EP
142	
143	### TC-06-02 | Verify that a multi-line review keeps its line breaks on the product page.
144	PRE: [STD]
145	1. Click the 4th star of "Your rating *".
146	2. Click in "Your review *" and type "Line one", press Enter, type "Line two", press Enter, type "Line three".
147	3. Enter "Anna Smith" in "Name *".
148	4. Enter "anna.smith@example.com" in "Email *".
149	5. Click "Submit".
150	6. Click "Moderator: approve pending reviews".
151	7. Find the review starting with "Line one" in the "Reviews" list.
152	NOTES: Condition: TCD-06-02; Technique: Error guessing; Missing info: display of line breaks is not stated in any source (Q-35).; Assumption: line breaks in a review are shown as entered until Q-35 is answered.
153	
154	### TC-07-01 | Verify that the review is not submitted when "Your review *" is empty.
155	PRE: [STD]
156	1. Click the 4th star of "Your rating *".
157	2. Leave "Your review *" empty.
158	3. Enter "Anna Smith" in "Name *".
159	4. Enter "anna.smith@example.com" in "Email *".
160	5. Click "Submit".
161	NOTES: Condition: TCD-07-01; Technique: EP; Assumption: wording checked for meaning, not exact text until Q-20 is answered.; Missing info: expected result not stated in any source (Q-20).
162	
163	### TC-08-01 | Verify that a review text within the allowed length is saved and shown as entered.
164	PRE: [STD]
165	1. Click the 4th star of "Your rating *".
166	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
167	3. Enter "Anna Smith" in "Name *".
168	4. Enter "anna.smith@example.com" in "Email *".
169	5. Click "Submit".
170	6. Click "Moderator: approve pending reviews".
171	7. Find the review "Soft fabric, true to size. Would buy again." in the "Reviews" list.
172	NOTES: Condition: TCD-08-01; Technique: EP; Missing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered.; Assumption: the text used (43 characters) is between the minimum and the maximum length until Q-04 is answered.
173	
174	### TC-08-02 | Verify that accented, non-Latin, digit, punctuation and emoji characters are saved unchanged.
175	PRE: [STD]
176	1. Click the 4th star of "Your rating *".
177	2. Enter "Très bien, Größe M passt! 日本語 OK 100% 👍" in "Your review *".
178	3. Enter "Anna Smith" in "Name *".
179	4. Enter "anna.smith@example.com" in "Email *".
180	5. Click "Submit".
181	6. Click "Moderator: approve pending reviews".
182	7. Find the review "Très bien, Größe M passt! 日本語 OK 100% 👍" in the "Reviews" list.
183	NOTES: Condition: TCD-08-02; Technique: Error guessing; Assumption: no character restriction in "Your review" until Q-37 is answered.; Missing info: expected result not stated in any source (Q-37).
184	
185	### TC-08-03 | Verify that a review text pasted from the clipboard is saved like typed text.
186	PRE: [STD] The text "Pasted review: comfy and soft." (copied from Notepad) is ready in the clipboard.
187	1. Click the 4th star of "Your rating *".
188	2. Click in "Your review *" and press Ctrl+V.
189	3. Enter "Anna Smith" in "Name *".
190	4. Enter "anna.smith@example.com" in "Email *".
191	5. Click "Submit".
192	6. Click "Moderator: approve pending reviews".
193	7. Find the review "Pasted review: comfy and soft." in the "Reviews" list.
194	NOTES: Condition: TCD-08-03; Technique: Error guessing
195	
196	### TC-11-01 | Verify that a review made only of spaces is not submitted.
197	PRE: [STD]
198	1. Click the 4th star of "Your rating *".
199	2. Click in "Your review *" and press the Space bar 5 times.
200	3. Enter "Anna Smith" in "Name *".
201	4. Enter "anna.smith@example.com" in "Email *".
202	5. Click "Submit".
203	NOTES: Condition: TCD-11-01; Technique: Error guessing; Edge case: whitespace-only input.; Assumption: a field of only spaces counts as empty until Q-17 is answered.; Missing info: expected result not stated in any source (Q-17, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
204	
205	### TC-11-02 | Verify that a review made only of line breaks is not submitted.
206	PRE: [STD]
207	1. Click the 4th star of "Your rating *".
208	2. Click in "Your review *" and press Enter 3 times.
209	3. Enter "Anna Smith" in "Name *".
210	4. Enter "anna.smith@example.com" in "Email *".
211	5. Click "Submit".
212	NOTES: Condition: TCD-11-02; Technique: Error guessing; Edge case: whitespace-only input.; Assumption: line breaks are treated like spaces until Q-17 is answered.; Missing info: expected result not stated in any source (Q-17, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
213	
214	### TC-11-03 | Verify that leading and trailing spaces of a review are removed when shown.
215	PRE: [STD]
216	1. Click the 4th star of "Your rating *".
217	2. Enter "   Space padded review.   " (3 spaces before and after) in "Your review *".
218	3. Enter "Anna Smith" in "Name *".
219	4. Enter "anna.smith@example.com" in "Email *".
220	5. Click "Submit".
221	6. Click "Moderator: approve pending reviews".
222	7. Find the review "Space padded review." in the "Reviews" list.
223	8. Right-click the review text > Inspect, and read the text in the DevTools Elements panel.
224	NOTES: Condition: TCD-11-03; Technique: Error guessing; Assumption: spaces are trimmed until Q-17 is answered.; Missing info: expected result not stated in any source (Q-17).
225	
226	### TC-12-01 | Verify that a script in "Your review *" is never run.
227	PRE: [STD]
228	1. Click the 4th star of "Your rating *".
229	2. Enter "<script>alert(1)</script>" in "Your review *".
230	3. Enter "Anna Smith" in "Name *".
231	4. Enter "anna.smith@example.com" in "Email *".
232	5. Click "Submit".
233	6. Click "Moderator: approve pending reviews".
234	7. Look at the "Reviews" list.
235	NOTES: OBSERVE ONLY — no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict); Condition: TCD-12-01; Technique: Error guessing; Missing info: shown as plain text, removed or rejected (Q-15).; Risk: script injection would affect every visitor of the product page.
236	
237	### TC-12-02 | Verify that an HTML image tag with a script in "Your review *" is not run.
238	PRE: [STD]
239	1. Click the 4th star of "Your rating *".
240	2. Enter "<img src=x onerror=alert(1)>" in "Your review *".
241	3. Enter "Anna Smith" in "Name *".
242	4. Enter "anna.smith@example.com" in "Email *".
243	5. Click "Submit".
244	6. Click "Moderator: approve pending reviews".
245	7. Look at the "Reviews" list.
246	NOTES: Condition: TCD-12-02; Technique: Error guessing; Missing info: handling not stated (Q-15).; Risk: script injection through an HTML attribute.
247	
248	### TC-12-03 | Verify that HTML formatting in "Your review *" is not rendered as HTML.
249	PRE: [STD]
250	1. Click the 4th star of "Your rating *".
251	2. Enter "<b>bold</b> text check" in "Your review *".
252	3. Enter "Anna Smith" in "Name *".
253	4. Enter "anna.smith@example.com" in "Email *".
254	5. Click "Submit".
255	6. Click "Moderator: approve pending reviews".
256	7. Look at the "Reviews" list.
257	NOTES: OBSERVE ONLY — no verdict until Q-15 is answered; Condition: TCD-12-03; Technique: Error guessing; Missing info: handling not stated (Q-15).
258	
259	### TC-12-04 | Verify that a web link in "Your review *" is not turned into a clickable link.
260	PRE: [STD]
261	1. Click the 4th star of "Your rating *".
262	2. Enter "Link check https://example.com" in "Your review *".
263	3. Enter "Anna Smith" in "Name *".
264	4. Enter "anna.smith@example.com" in "Email *".
265	5. Click "Submit".
266	6. Click "Moderator: approve pending reviews".
267	7. Look at the "Reviews" list.
268	NOTES: OBSERVE ONLY — no verdict until Q-15 is answered; Condition: TCD-12-04; Technique: Error guessing; Missing info: handling of links not stated (Q-15).
269	
270	### TC-12-05 | Verify that a script in "Name *" is not run where the name is shown.
271	PRE: [STD]
272	1. Click the 4th star of "Your rating *".
273	2. Enter "Name script check." in "Your review *".
274	3. Enter "<script>alert(1)</script>" in "Name *".
275	4. Enter "anna.smith@example.com" in "Email *".
276	5. Click "Submit".
277	6. Click "Moderator: approve pending reviews".
278	7. Look at the "Reviews" list.
279	NOTES: OBSERVE ONLY — no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict); Condition: TCD-12-05; Technique: Error guessing; Missing info: handling not stated (Q-05, Q-15).; Risk: script injection through the reviewer name.
280	
281	### TC-14-01 | Verify that a pending review appears on the product page after it is approved.
282	PRE: [STD]
283	1. Click the 4th star of "Your rating *".
284	2. Enter "Approval check: shown after approve." in "Your review *".
285	3. Enter "Anna Smith" in "Name *".
286	4. Enter "anna.smith@example.com" in "Email *".
287	5. Click "Submit".
288	6. Click "Moderator: approve pending reviews".
289	7. Look at the "Reviews" list.
290	NOTES: Condition: TCD-14-01; Technique: State transition; Missing info: who approves and how (Q-07).; Assumption: in demo-1.0 the "Moderator: approve pending reviews" helper plays the moderator (environment.md).
291	
292	### TC-14-02 | Verify that using the approve action twice shows an approved review only once.
293	PRE: [STD]
294	1. Click the 4th star of "Your rating *".
295	2. Enter "Approve twice check." in "Your review *".
296	3. Enter "Anna Smith" in "Name *".
297	4. Enter "anna.smith@example.com" in "Email *".
298	5. Click "Submit".
299	6. Click "Moderator: approve pending reviews".
300	7. Click "Moderator: approve pending reviews".
301	8. Count the reviews with the text "Approve twice check." in the "Reviews" list.
302	NOTES: Condition: TCD-14-02; Technique: State transition; Edge case: approve twice.; Missing info: moderation workflow (Q-07).
303	
304	### TC-14-03 | Verify that the approve action with no pending review adds no review.
305	PRE: [STD]
306	1. Count the reviews in the "Reviews" list and write the number down.
307	2. Click "Moderator: approve pending reviews".
308	3. Count the reviews in the "Reviews" list again.
309	NOTES: Condition: TCD-14-03; Technique: State transition; Edge case: approve with nothing pending.; Missing info: moderation workflow (Q-07).
310	
311	### TC-16-01 | Verify how the author sees their own pending review right after Submit.
312	PRE: [STD]
313	1. Click the 4th star of "Your rating *".
314	2. Enter "Author view: pending check." in "Your review *".
315	3. Enter "Anna Smith" in "Name *".
316	4. Enter "anna.smith@example.com" in "Email *".
317	5. Click "Submit".
318	6. Look at the "Reviews" list.
319	NOTES: OBSERVE ONLY — no verdict until Q-08 is answered; Condition: TCD-16-01; Technique: Decision table; Missing info: author's view of a pending review not specified (Q-08).
320	
321	### TC-16-02 | Verify that the author sees their approved review with no awaiting-approval mark.
322	PRE: [STD]
323	1. Click the 4th star of "Your rating *".
324	2. Enter "Author view: approved check." in "Your review *".
325	3. Enter "Anna Smith" in "Name *".
326	4. Enter "anna.smith@example.com" in "Email *".
327	5. Click "Submit".
328	6. Click "Moderator: approve pending reviews".
329	7. Find the review "Author view: approved check." in the "Reviews" list.
330	NOTES: OBSERVE ONLY — no verdict until Q-08 is answered; Condition: TCD-16-02; Technique: Decision table; Missing info: whether a pending mark exists (Q-08).
331	
332	### TC-17-01 | Verify that an approved review shows rating, reviewer name, date and text.
333	PRE: [STD]
334	1. Click the 4th star of "Your rating *".
335	2. Enter "Details check: all parts shown." in "Your review *".
336	3. Enter "Anna Smith" in "Name *".
337	4. Enter "anna.smith@example.com" in "Email *".
338	5. Click "Submit".
339	6. Click "Moderator: approve pending reviews".
340	7. Find the review "Details check: all parts shown." in the "Reviews" list.
341	NOTES: Condition: TCD-17-01; Technique: EP; Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered.; Missing info: expected result not stated in any source (Q-09).
342	
343	### TC-17-02 | Verify that the date shown with a review is the submit date in an unambiguous format.
344	PRE: [STD] Today's date is written down.
345	1. Click the 4th star of "Your rating *".
346	2. Enter "Date check: submit date." in "Your review *".
347	3. Enter "Anna Smith" in "Name *".
348	4. Enter "anna.smith@example.com" in "Email *".
349	5. Click "Submit".
350	6. Click "Moderator: approve pending reviews".
351	7. Find the review "Date check: submit date." in the "Reviews" list.
352	8. Read the date shown with the review.
353	NOTES: Condition: TCD-17-02; Technique: EP; Assumption: submit date in any unambiguous format until Q-24 is answered.; Missing info: on demo-1.0 submit and approval happen on the same day, so submit date and approval date cannot be told apart (Q-24).
354	
355	### TC-17-03 | Verify that the reviewer name is shown in the confirmed form.
356	PRE: [STD]
357	1. Click the 4th star of "Your rating *".
358	2. Enter "Name form check." in "Your review *".
359	3. Enter "Anna Smith" in "Name *".
360	4. Enter "anna.smith@example.com" in "Email *".
361	5. Click "Submit".
362	6. Click "Moderator: approve pending reviews".
363	7. Find the review "Name form check." in the "Reviews" list.
364	8. Read the reviewer name shown with the review.
365	NOTES: Condition: TCD-17-03; Technique: EP; Missing info: form of the name not specified (Q-09).; Risk: privacy of the reviewer's name.; Assumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.
366	
367	### TC-18-01 | Verify that two reviews keep their own rating, name and text after approval.
368	PRE: [STD]
369	1. Click the 2nd star of "Your rating *".
370	2. Enter "First review: too tight." in "Your review *".
371	3. Enter "Ben Carter" in "Name *".
372	4. Enter "ben.carter@example.com" in "Email *".
373	5. Click "Submit".
374	6. Clear "Your review *", "Name *" and "Email *" if they still contain text.
375	7. Click the 5th star of "Your rating *".
376	8. Enter "Second review: perfect fit." in "Your review *".
377	9. Enter "Chloe Diaz" in "Name *".
378	10. Enter "chloe.diaz@example.com" in "Email *".
379	11. Click "Submit".
380	12. Click "Moderator: approve pending reviews".
381	13. Find the review "First review: too tight." in the "Reviews" list.
382	14. Find the review "Second review: perfect fit." in the "Reviews" list.
383	NOTES: Condition: TCD-18-01; Technique: EP; Assumption: the rating and the name are shown with each review until Q-09 is answered.
384	
385	### TC-18-02 | Verify that a name with accent, apostrophe and hyphen is shown exactly as entered.
386	PRE: [STD]
387	1. Click the 4th star of "Your rating *".
388	2. Enter "Special name check." in "Your review *".
389	3. Enter "Zoë O'Brien-Lê" in "Name *".
390	4. Enter "anna.smith@example.com" in "Email *".
391	5. Click "Submit".
392	6. Click "Moderator: approve pending reviews".
393	7. Find the review "Special name check." in the "Reviews" list.
394	8. Read the reviewer name shown with the review.
395	NOTES: Condition: TCD-18-02; Technique: Error guessing; Assumption: such names are accepted until Q-05 is answered.; Missing info: expected result not stated in any source (Q-05).
396	
397	### TC-18-03 | Verify that the characters & < > " ' in a review are shown as typed.
398	PRE: [STD]
399	1. Click the 4th star of "Your rating *".
400	2. Enter this text in "Your review *" (everything after the colon): 5 > 3 & "good" isn't it
401	3. Enter "Anna Smith" in "Name *".
402	4. Enter "anna.smith@example.com" in "Email *".
403	5. Click "Submit".
404	6. Click "Moderator: approve pending reviews".
405	7. Find the review starting with "5 > 3" in the "Reviews" list.
406	NOTES: OBSERVE ONLY — no verdict until Q-15 is answered; Condition: TCD-18-03; Technique: Error guessing; Missing info: handling of HTML-like text (Q-15).
407	
408	### TC-19-01 | Verify that the reviewer's email is not shown anywhere on the visible product page.
409	PRE: [STD]
410	1. Click the 4th star of "Your rating *".
411	2. Enter "Email privacy check: visible page." in "Your review *".
412	3. Enter "Anna Smith" in "Name *".
413	4. Enter "unique.reviewer@example.com" in "Email *".
414	5. Click "Submit".
415	6. Click "Moderator: approve pending reviews".
416	7. Press Ctrl+F and search for "unique.reviewer".
417	8. Check where each match is.
418	NOTES: Condition: TCD-19-01; Technique: Error guessing; Risk: personal data could be shown publicly.
419	
420	### TC-19-02 | Verify that the reviewer's email is not in hidden parts of the displayed review.
421	PRE: [STD]
422	1. Click the 4th star of "Your rating *".
423	2. Enter "Email privacy check: hidden parts." in "Your review *".
424	3. Enter "Anna Smith" in "Name *".
425	4. Enter "unique.reviewer@example.com" in "Email *".
426	5. Click "Submit".
427	6. Click "Moderator: approve pending reviews".
428	7. Find the review "Email privacy check: hidden parts." in the "Reviews" list.
429	8. Hover over the reviewer name and wait 2 seconds.
430	9. Right-click the reviewer name > Inspect.
431	10. In the DevTools Elements panel press Ctrl+F and search for "unique.reviewer".
432	NOTES: Condition: TCD-19-02; Technique: Error guessing; Risk: personal data could be read by anyone viewing the page source.
433	
434	### TC-20-01 | Verify that approved reviews are listed in the confirmed order.
435	PRE: [STD] At least 3 approved reviews with different dates and ratings are listed (initial data of demo-1.0).
436	1. Look at the "Reviews" list.
437	2. Write down the date and the rating of each review from top to bottom.
438	NOTES: OBSERVE ONLY — no verdict until Q-10 is answered; Condition: TCD-20-01; Technique: EP; Missing info: list order not specified (Q-10).
439	
440	### TC-20-02 | Verify that a newly approved review appears in the position the order requires.
441	PRE: [STD] At least 3 approved reviews with different dates and ratings are listed (initial data of demo-1.0).
442	1. Click the 4th star of "Your rating *".
443	2. Enter "Order check: newly approved." in "Your review *".
444	3. Enter "Anna Smith" in "Name *".
445	4. Enter "anna.smith@example.com" in "Email *".
446	5. Click "Submit".
447	6. Click "Moderator: approve pending reviews".
448	7. Note the position of the review "Order check: newly approved." in the "Reviews" list.
449	NOTES: OBSERVE ONLY — no verdict until Q-10 is answered; Condition: TCD-20-02; Technique: Error guessing; Missing info: list order not specified (Q-10).
450	
451	### TC-23-01 | Verify that an approved review is included in the average rating and review count.
452	PRE: [STD] The rating summary next to the product name (average and count) and the ratings of all listed reviews are written down.
453	1. Click the 1st star of "Your rating *".
454	2. Enter "Summary check: approved 1 star." in "Your review *".
455	3. Enter "Anna Smith" in "Name *".
456	4. Enter "anna.smith@example.com" in "Email *".
457	5. Click "Submit".
458	6. Click "Moderator: approve pending reviews".
459	7. Read the rating summary next to the product name.
460	NOTES: OBSERVE ONLY — no verdict until Q-11 is answered; Condition: TCD-23-01; Technique: Decision table; Missing info: whether a summary is shown and how it is rounded (Q-11).
461	
462	### TC-23-02 | Verify that a pending review does not change the average rating or review count.
463	PRE: [STD] The rating summary next to the product name (average and count) and the ratings of all listed reviews are written down.
464	1. Click the 1st star of "Your rating *".
465	2. Enter "Summary check: pending 1 star." in "Your review *".
466	3. Enter "Anna Smith" in "Name *".
467	4. Enter "anna.smith@example.com" in "Email *".
468	5. Click "Submit".
469	6. Read the rating summary next to the product name.
470	NOTES: OBSERVE ONLY — no verdict until Q-11 is answered; Condition: TCD-23-02; Technique: Decision table; Missing info: Q-11.; Risk: pending reviews could change the score shown to shoppers.
471	
472	### TC-23-04 | Verify that the review count shown equals the number of approved reviews listed.
473	PRE: [STD]
474	1. Click the 4th star of "Your rating *".
475	2. Enter "Summary check: count." in "Your review *".
476	3. Enter "Anna Smith" in "Name *".
477	4. Enter "anna.smith@example.com" in "Email *".
478	5. Click "Submit".
479	6. Click "Moderator: approve pending reviews".
480	7. Count the reviews in the "Reviews" list.
481	8. Read the review count in the rating summary next to the product name.
482	NOTES: OBSERVE ONLY — no verdict until Q-11 is answered; Condition: TCD-23-04; Technique: EP; Missing info: whether a count is shown (Q-11).
483	
484	### TC-23-05 | Verify that an average falling exactly on a rounding step is shown with the confirmed rounding.
485	PRE: [STD] The "Reviews" list shows exactly 3 approved reviews rated 5, 4 and 3 (initial data; check before step 1).
486	1. Click the 2nd star of "Your rating *".
487	2. Enter "Rounding check: two stars." in "Your review *".
488	3. Enter "Anna Smith" in "Name *".
489	4. Enter "anna.smith@example.com" in "Email *".
490	5. Click "Submit".
491	6. Click "Moderator: approve pending reviews".
492	7. Read the average in the rating summary next to the product name.
493	NOTES: OBSERVE ONLY — no verdict until Q-11 is answered; Condition: TCD-23-05; Technique: BVA; Missing info: rounding rule not stated (Q-11); exact boundary values are set when Q-11 is answered.; Missing info: values next to the rounding step (for example 4.33) are added when Q-11 gives the rounding rule.
494	
495	### TC-25-01 | Verify that the form heading reads "ADD A REVIEW".
496	PRE: [STD]
497	1. Scroll to the review form.
498	2. Read the heading of the form.
499	NOTES: Condition: TCD-25-01; Technique: EP; Missing info: expected result not stated in any source (Q-32).; Assumption: compared without letter case until Q-32 is answered.
500	
501	### TC-25-02 | Verify that the info text above the form matches mockup-1.
502	PRE: [STD]
503	1. Scroll to the review form.
504	2. Read the text under the form heading.
505	NOTES: Condition: TCD-25-02; Technique: EP
506	
507	### TC-25-03 | Verify that the four field labels are shown, each with the required marker *.
508	PRE: [STD]
509	1. Scroll to the review form.
510	2. Read the label of each field.
511	NOTES: Condition: TCD-25-03; Technique: EP
512	
513	### TC-25-04 | Verify that the save checkbox text matches mockup-1.
514	PRE: [STD]
515	1. Scroll to the review form.
516	2. Read the text next to the checkbox.
517	NOTES: Condition: TCD-25-04; Technique: EP; Missing info: final text of the save checkbox (Q-13).
518	
519	### TC-25-05 | Verify that a "Submit" button is shown below the save checkbox.
520	PRE: [STD]
521	1. Scroll to the review form.
522	2. Look below the save checkbox.
523	NOTES: Condition: TCD-25-05; Technique: EP
524	
525	### TC-25-06 | Verify that the form elements are in the mockup-1 order.
526	PRE: [STD]
527	1. Scroll to the review form.
528	2. Write down the elements from top to bottom.
529	NOTES: Condition: TCD-25-06; Technique: EP
530	
531	### TC-25-07 | Verify that Tab moves through the form in screen order and Submit works by keyboard.
532	PRE: [STD]
533	1. Click on the info text "Your email address will not be published. Required fields are marked *".
534	2. Press Tab repeatedly and note which control gets the focus each time.
535	3. When "Submit" has the focus, press Enter.
536	NOTES: Condition: TCD-25-07; Technique: Error guessing; Missing info: keyboard use is not stated in any source (Q-34).; Assumption: the rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen until Q-34 is answered.
537	
538	### TC-28-01 | Verify that the review is not submitted when "Name *" is empty.
539	PRE: [STD]
540	1. Click the 4th star of "Your rating *".
541	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
542	3. Leave "Name *" empty.
543	4. Enter "anna.smith@example.com" in "Email *".
544	5. Click "Submit".
545	NOTES: Condition: TCD-28-01; Technique: EP; Assumption: wording checked for meaning, not exact text until Q-20 is answered.; Missing info: expected result not stated in any source (Q-20).
546	
547	### TC-29-01 | Verify that a Name of Latin letters and a space is accepted.
548	PRE: [STD]
549	1. Click the 4th star of "Your rating *".
550	2. Enter "Name check 29-01." in "Your review *".
551	3. Enter "Anna Smith" in "Name *".
552	4. Enter "anna.smith@example.com" in "Email *".
553	5. Click "Submit".
554	NOTES: Condition: TCD-29-01; Technique: EP; Assumption: letters and spaces are allowed until Q-05 is answered.; Missing info: expected result not stated in any source (Q-05).
555	
556	### TC-29-02 | Verify that a Name with accented letters is accepted.
557	PRE: [STD]
558	1. Click the 4th star of "Your rating *".
559	2. Enter "Name check 29-02." in "Your review *".
560	3. Enter "Zoë Lê" in "Name *".
561	4. Enter "anna.smith@example.com" in "Email *".
562	5. Click "Submit".
563	NOTES: Condition: TCD-29-02; Technique: EP; Edge case: accented letters.; Assumption: accented letters are allowed until Q-05 is answered.; Missing info: expected result not stated in any source (Q-05).
564	
565	### TC-29-03 | Verify that a Name with a hyphen and an apostrophe is accepted.
566	PRE: [STD]
567	1. Click the 4th star of "Your rating *".
568	2. Enter "Name check 29-03." in "Your review *".
569	3. Enter "Mary-Jane O'Neil" in "Name *".
570	4. Enter "anna.smith@example.com" in "Email *".
571	5. Click "Submit".
572	NOTES: Condition: TCD-29-03; Technique: EP; Edge case: hyphen and apostrophe.; Assumption: hyphens and apostrophes are allowed until Q-05 is answered.; Missing info: expected result not stated in any source (Q-05).
573	
574	### TC-29-04 | Verify whether a Name in a non-Latin script is accepted.
575	PRE: [STD]
576	1. Click the 4th star of "Your rating *".
577	2. Enter "Name check 29-04." in "Your review *".
578	3. Enter "李明" in "Name *".
579	4. Enter "anna.smith@example.com" in "Email *".
580	5. Click "Submit".
581	NOTES: OBSERVE ONLY — no verdict until Q-05 is answered; Condition: TCD-29-04; Technique: EP; Missing info: allowed characters not stated (Q-05).
582	
583	### TC-29-05 | Verify whether a Name containing digits is accepted.
584	PRE: [STD]
585	1. Click the 4th star of "Your rating *".
586	2. Enter "Name check 29-05." in "Your review *".
587	3. Enter "Anna2" in "Name *".
588	4. Enter "anna.smith@example.com" in "Email *".
589	5. Click "Submit".
590	NOTES: OBSERVE ONLY — no verdict until Q-05 is answered; Condition: TCD-29-05; Technique: EP; Missing info: whether digits are allowed (Q-05).
591	
592	### TC-29-06 | Verify that a Name made only of symbols is rejected.
593	PRE: [STD]
594	1. Click the 4th star of "Your rating *".
595	2. Enter "Name check 29-06." in "Your review *".
596	3. Enter "@#$%" in "Name *".
597	4. Enter "anna.smith@example.com" in "Email *".
598	5. Click "Submit".
599	NOTES: OBSERVE ONLY — no verdict until Q-05 and Q-20 are answered; Condition: TCD-29-06; Technique: EP; Missing info: allowed characters not stated (Q-05).; Missing info: expected result not stated in any source (Q-20).
600	
601	### TC-29-07 | Verify that a Name of 1 character is accepted.
602	PRE: [STD]
603	1. Click the 4th star of "Your rating *".
604	2. Enter "Name check 29-07." in "Your review *".
605	3. Enter "A" in "Name *".
606	4. Enter "anna.smith@example.com" in "Email *".
607	5. Click "Submit".
608	NOTES: OBSERVE ONLY — no verdict until Q-05 is answered; Condition: TCD-29-07; Technique: BVA; Edge case: shortest non-empty name.; Missing info: minimum length not stated (Q-05).
609	
610	### TC-30-01 | Verify that the review is not submitted when "Email *" is empty.
611	PRE: [STD]
612	1. Click the 4th star of "Your rating *".
613	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
614	3. Enter "Anna Smith" in "Name *".
615	4. Leave "Email *" empty.
616	5. Click "Submit".
617	NOTES: Condition: TCD-30-01; Technique: EP; Assumption: wording checked for meaning, not exact text until Q-20 is answered.; Missing info: expected result not stated in any source (Q-20).
618	
619	### TC-31-01 | Verify that the email "anna.smith@example.com" is accepted.
620	PRE: [STD]
621	1. Click the 4th star of "Your rating *".
622	2. Enter "Email check 31-01." in "Your review *".
623	3. Enter "Anna Smith" in "Name *".
624	4. Enter "anna.smith@example.com" in "Email *".
625	5. Click "Submit".
626	NOTES: Condition: TCD-31-01; Technique: EP; Assumption: standard format text@domain.tld until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06).
627	
628	### TC-31-02 | Verify that an email with a plus sign and a sub-domain is accepted.
629	PRE: [STD]
630	1. Click the 4th star of "Your rating *".
631	2. Enter "Email check 31-02." in "Your review *".
632	3. Enter "Anna Smith" in "Name *".
633	4. Enter "anna+shop@mail.example.co.uk" in "Email *".
634	5. Click "Submit".
635	NOTES: Condition: TCD-31-02; Technique: EP; Edge case: plus sign and sub-domain.; Assumption: standard format until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06).
636	
637	### TC-31-03 | Verify that an email without "@" is rejected.
638	PRE: [STD]
639	1. Click the 4th star of "Your rating *".
640	2. Enter "Email check 31-03." in "Your review *".
641	3. Enter "Anna Smith" in "Name *".
642	4. Enter "anna.example.com" in "Email *".
643	5. Click "Submit".
644	NOTES: Condition: TCD-31-03; Technique: EP; Assumption: standard format until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
645	
646	### TC-31-04 | Verify that an email with nothing before "@" is rejected.
647	PRE: [STD]
648	1. Click the 4th star of "Your rating *".
649	2. Enter "Email check 31-04." in "Your review *".
650	3. Enter "Anna Smith" in "Name *".
651	4. Enter "@example.com" in "Email *".
652	5. Click "Submit".
653	NOTES: Condition: TCD-31-04; Technique: EP; Assumption: standard format until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
654	
655	### TC-31-05 | Verify that an email with no domain after "@" is rejected.
656	PRE: [STD]
657	1. Click the 4th star of "Your rating *".
658	2. Enter "Email check 31-05." in "Your review *".
659	3. Enter "Anna Smith" in "Name *".
660	4. Enter "anna@" in "Email *".
661	5. Click "Submit".
662	NOTES: Condition: TCD-31-05; Technique: EP; Assumption: standard format until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
663	
664	### TC-31-06 | Verify that an email without a top-level domain is rejected.
665	PRE: [STD]
666	1. Click the 4th star of "Your rating *".
667	2. Enter "Email check 31-06." in "Your review *".
668	3. Enter "Anna Smith" in "Name *".
669	4. Enter "anna@example" in "Email *".
670	5. Click "Submit".
671	NOTES: Condition: TCD-31-06; Technique: EP; Assumption: a top-level domain is required; some format rules accept this value until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
672	
673	### TC-31-07 | Verify that an email with two "@" is rejected.
674	PRE: [STD]
675	1. Click the 4th star of "Your rating *".
676	2. Enter "Email check 31-07." in "Your review *".
677	3. Enter "Anna Smith" in "Name *".
678	4. Enter "anna@@example.com" in "Email *".
679	5. Click "Submit".
680	NOTES: Condition: TCD-31-07; Technique: EP; Assumption: standard format until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
681	
682	### TC-31-08 | Verify that an email with a space inside is rejected.
683	PRE: [STD]
684	1. Click the 4th star of "Your rating *".
685	2. Enter "Email check 31-08." in "Your review *".
686	3. Enter "Anna Smith" in "Name *".
687	4. Enter "anna smith@example.com" in "Email *".
688	5. Click "Submit".
689	NOTES: Condition: TCD-31-08; Technique: EP; Assumption: standard format until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
690	
691	### TC-31-09 | Verify that an email in upper case is accepted.
692	PRE: [STD]
693	1. Click the 4th star of "Your rating *".
694	2. Enter "Email check 31-09." in "Your review *".
695	3. Enter "Anna Smith" in "Name *".
696	4. Enter "ANNA@EXAMPLE.COM" in "Email *".
697	5. Click "Submit".
698	NOTES: Condition: TCD-31-09; Technique: Error guessing; Assumption: letter case does not matter until Q-06 is answered.; Missing info: expected result not stated in any source (Q-06).
699	
700	### TC-32-01 | Verify that leading and trailing spaces in Name are removed when shown.
701	PRE: [STD]
702	1. Click the 4th star of "Your rating *".
703	2. Enter "Name trim check." in "Your review *".
704	3. Enter "  Anna Smith  " (2 spaces before and after) in "Name *".
705	4. Enter "anna.smith@example.com" in "Email *".
706	5. Click "Submit".
707	6. Click "Moderator: approve pending reviews".
708	7. Find the review "Name trim check." in the "Reviews" list.
709	8. Right-click the reviewer name > Inspect, and read the name in the DevTools Elements panel.
710	NOTES: Condition: TCD-32-01; Technique: Error guessing; Edge case: space-padded input.; Assumption: spaces are trimmed until Q-17 is answered.; Missing info: expected result not stated in any source (Q-17).
711	
712	### TC-32-02 | Verify that a Name made only of spaces is treated as empty.
713	PRE: [STD]
714	1. Click the 4th star of "Your rating *".
715	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
716	3. Click in "Name *" and press the Space bar 5 times.
717	4. Enter "anna.smith@example.com" in "Email *".
718	5. Click "Submit".
719	NOTES: Condition: TCD-32-02; Technique: Error guessing; Edge case: whitespace-only input.; Assumption: a field of only spaces counts as empty until Q-17 is answered.; Missing info: expected result not stated in any source (Q-17, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
720	
721	### TC-32-03 | Verify that an Email with leading and trailing spaces is accepted.
722	PRE: [STD]
723	1. Click the 4th star of "Your rating *".
724	2. Enter "Email trim check." in "Your review *".
725	3. Enter "Anna Smith" in "Name *".
726	4. Enter "  anna@example.com  " (2 spaces before and after) in "Email *".
727	5. Click "Submit".
728	NOTES: Condition: TCD-32-03; Technique: Error guessing; Edge case: space-padded input.; Assumption: spaces are trimmed until Q-17 is answered.; Missing info: expected result not stated in any source (Q-17).
729	
730	### TC-32-04 | Verify that an Email made only of spaces is treated as empty.
731	PRE: [STD]
732	1. Click the 4th star of "Your rating *".
733	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
734	3. Enter "Anna Smith" in "Name *".
735	4. Click in "Email *" and press the Space bar 5 times.
736	5. Click "Submit".
737	NOTES: Condition: TCD-32-04; Technique: Error guessing; Edge case: whitespace-only input.; Assumption: a field of only spaces counts as empty until Q-17 is answered.; Missing info: expected result not stated in any source (Q-17, Q-20).; Assumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.
738	
739	### TC-33-01 | Verify that a valid review is submitted with the save checkbox not ticked.
740	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
741	1. Click the 4th star of "Your rating *".
742	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
743	3. Enter "Anna Smith" in "Name *".
744	4. Enter "anna.smith@example.com" in "Email *".
745	5. Leave the checkbox "Save my name, email, and website in this browser for the next time I comment." not ticked.
746	6. Click "Submit".
747	NOTES: Condition: TCD-33-01; Technique: Decision table; Assumption: confirmation says the review was received and waits for approval until Q-21 is answered.; Missing info: expected result not stated in any source (Q-21).
748	
749	### TC-33-02 | Verify that a valid review is submitted with the save checkbox ticked.
750	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
751	1. Click the 4th star of "Your rating *".
752	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
753	3. Enter "Anna Smith" in "Name *".
754	4. Enter "anna.smith@example.com" in "Email *".
755	5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."
756	6. Click "Submit".
757	NOTES: Condition: TCD-33-02; Technique: Decision table; Assumption: confirmation text until Q-21 is answered.; Missing info: expected result not stated in any source (Q-21).
758	
759	### TC-34-01 | Verify that submitting an empty form names all four required fields.
760	PRE: [STD]
761	1. Leave "Your rating *", "Your review *", "Name *" and "Email *" empty.
762	2. Click "Submit".
763	NOTES: Condition: TCD-34-01; Technique: Decision table; Assumption: each error names its field; wording checked for meaning until Q-20 is answered.; Missing info: expected result not stated in any source (Q-20).
764	
765	### TC-34-02 | Verify that only the empty rating and review are named when Name and Email are valid.
766	PRE: [STD]
767	1. Leave "Your rating *" and "Your review *" empty.
768	2. Enter "Anna Smith" in "Name *".
769	3. Enter "anna.smith@example.com" in "Email *".
770	4. Click "Submit".
771	NOTES: Condition: TCD-34-02; Technique: Decision table; Assumption: wording checked for meaning until Q-20 is answered.; Missing info: expected result not stated in any source (Q-20).
772	
773	### TC-34-03 | Verify that entered values are kept after a rejected Submit and correction submits.
774	PRE: [STD]
775	1. Click the 4th star of "Your rating *".
776	2. Leave "Your review *" empty.
777	3. Enter "Anna Smith" in "Name *".
778	4. Enter "anna.smith@example.com" in "Email *".
779	5. Click "Submit".
780	6. Check that the rating, "Name *" and "Email *" still hold the values entered.
781	7. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
782	8. Click "Submit".
783	NOTES: Condition: TCD-34-03; Technique: Decision table; Assumption: entered values are kept after a rejected submit until Q-38 is answered.; Missing info: expected result not stated in any source (Q-38).
784	
785	### TC-34-04 | Verify that leaving a required field empty shows no error until Submit.
786	PRE: [STD]
787	1. Click in "Name *".
788	2. Press Tab to move to "Email *" without typing.
789	3. Look at the form and the area above it.
790	NOTES: Condition: TCD-34-04; Technique: EP; Assumption: fields are checked on Submit only until Q-19 is answered.; Missing info: expected result not stated in any source (Q-19).
791	
792	### TC-35-01 | Verify that the form is fully cleared after a successful Submit without saving.
793	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
794	1. Click the 4th star of "Your rating *".
795	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
796	3. Enter "Anna Smith" in "Name *".
797	4. Enter "anna.smith@example.com" in "Email *".
798	5. Leave the checkbox "Save my name, email, and website in this browser for the next time I comment." not ticked.
799	6. Click "Submit".
800	7. Look at the page and the form.
801	NOTES: Condition: TCD-35-01; Technique: State transition; Assumption: form cleared until Q-22 is answered.; Missing info: expected result not stated in any source (Q-22).
802	
803	### TC-35-02 | Verify that Name and Email stay filled after a successful Submit with saving ticked.
804	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
805	1. Click the 4th star of "Your rating *".
806	2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".
807	3. Enter "Anna Smith" in "Name *".
808	4. Enter "anna.smith@example.com" in "Email *".
809	5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."
810	6. Click "Submit".
811	7. Look at the page and the form.
812	NOTES: Condition: TCD-35-02; Technique: State transition; Assumption: Name and Email stay filled only if the checkbox was ticked until Q-22 is answered.; Missing info: expected result not stated in any source (Q-22).
813	
814	### TC-36-01 | Verify that the save checkbox is not ticked on a first visit.
815	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
816	1. Scroll to the review form.
817	2. Look at the checkbox "Save my name, email, and website in this browser for the next time I comment."
818	NOTES: Condition: TCD-36-01; Technique: EP
819	
820	### TC-36-02 | Verify the save checkbox state on a return visit after Name and Email were saved.
821	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
822	1. Click the 4th star of "Your rating *".
823	2. Enter "Return visit check." in "Your review *".
824	3. Enter "Anna Smith" in "Name *".
825	4. Enter "anna.smith@example.com" in "Email *".
826	5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."
827	6. Click "Submit".
828	7. Reload the page (F5).
829	8. Look at the checkbox "Save my name, email, and website in this browser for the next time I comment."
830	NOTES: OBSERVE ONLY — no verdict until Q-14 is answered; Condition: TCD-36-02; Technique: EP; Edge case: checkbox state on a return visit.; Missing info: not stated (Q-14).
831	
832	### TC-37-01 | Verify that ticked saving refills Name and Email on the next visit.
833	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
834	1. Click the 4th star of "Your rating *".
835	2. Enter "Save check: first visit." in "Your review *".
836	3. Enter "Anna Smith" in "Name *".
837	4. Enter "anna.smith@example.com" in "Email *".
838	5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."
839	6. Click "Submit".
840	7. Close the tab and open exam/app/index.html again in the same Chrome window.
841	8. Look at "Name *" and "Email *".
842	NOTES: Condition: TCD-37-01; Technique: State transition; Assumption: only name and email are saved until Q-13 and Q-14 are answered.; Risk: personal data stored on the device.
843	
844	### TC-37-02 | Verify that a new ticked Submit replaces the saved Name and Email.
845	PRE: [STD] Name "Anna Smith" and Email "anna.smith@example.com" are saved in this browser (TC-37-01 done; they are filled on load).
846	1. Click the 4th star of "Your rating *".
847	2. Enter "Save check: replace." in "Your review *".
848	3. Replace the text in "Name *" with "Ben Carter".
849	4. Replace the text in "Email *" with "ben.carter@example.com".
850	5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment." (tick it if it is not ticked)
851	6. Click "Submit".
852	7. Reload the page (F5).
853	8. Look at "Name *" and "Email *".
854	NOTES: Condition: TCD-37-02; Technique: State transition; Assumption: saved values are replaced until Q-14 is answered.; Missing info: expected result not stated in any source (Q-14).
855	
856	### TC-37-03 | Verify what happens to saved data after a Submit with the box not ticked.
857	PRE: [STD] Name "Anna Smith" and Email "anna.smith@example.com" are saved in this browser (they are filled on load).
858	1. Click the 4th star of "Your rating *".
859	2. Enter "Save check: untick." in "Your review *".
860	3. Untick the checkbox "Save my name, email, and website in this browser for the next time I comment." if it is ticked.
861	4. Click "Submit".
862	5. Reload the page (F5).
863	6. Look at "Name *" and "Email *".
864	NOTES: OBSERVE ONLY — no verdict until Q-14 is answered; Condition: TCD-37-03; Technique: State transition; Missing info: how saved data is removed (Q-14).; Risk: personal data left on a shared device.
865	
866	### TC-37-04 | Verify that only Name and Email are refilled, not rating or review.
867	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
868	1. Click the 4th star of "Your rating *".
869	2. Enter "Save check: only name and email." in "Your review *".
870	3. Enter "Anna Smith" in "Name *".
871	4. Enter "anna.smith@example.com" in "Email *".
872	5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."
873	6. Click "Submit".
874	7. Reload the page (F5).
875	8. Look at the whole form.
876	NOTES: Condition: TCD-37-04; Technique: EP; Assumption: only name and email are saved until Q-13 and Q-14 are answered.; Missing info: expected result not stated in any source (Q-13, Q-14).
877	
878	### TC-37-05 | Verify that saved Name and Email are not filled in a private window.
879	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
880	1. Click the 4th star of "Your rating *".
881	2. Enter "Save check: private window." in "Your review *".
882	3. Enter "Anna Smith" in "Name *".
883	4. Enter "anna.smith@example.com" in "Email *".
884	5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."
885	6. Click "Submit".
886	7. Open a Chrome Incognito window (Ctrl+Shift+N).
887	8. Open exam/app/index.html in the Incognito window.
888	9. Look at "Name *" and "Email *".
889	NOTES: Condition: TCD-37-05; Technique: Error guessing; Edge case: "in this browser" only.
890	
891	### TC-37-06 | Verify that nothing is saved when Submit is rejected with the box ticked.
892	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
893	1. Click the 4th star of "Your rating *".
894	2. Leave "Your review *" empty.
895	3. Enter "Anna Smith" in "Name *".
896	4. Enter "anna.smith@example.com" in "Email *".
897	5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."
898	6. Click "Submit".
899	7. Reload the page (F5).
900	8. Look at "Name *" and "Email *".
901	NOTES: OBSERVE ONLY — no verdict until Q-14 is answered; Condition: TCD-37-06; Technique: State transition; Edge case: rejected submit with the box ticked.; Missing info: whether data is saved on a rejected submit (Q-14).
902	
903	### TC-38-01 | Verify that Name and Email are not kept when the box is not ticked.
904	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.
905	1. Click the 4th star of "Your rating *".
906	2. Enter "No save check." in "Your review *".
907	3. Enter "Anna Smith" in "Name *".
908	4. Enter "anna.smith@example.com" in "Email *".
909	5. Leave the checkbox "Save my name, email, and website in this browser for the next time I comment." not ticked.
910	6. Click "Submit".
911	7. Reload the page (F5).
912	8. Look at "Name *" and "Email *".
913	NOTES: OBSERVE ONLY — no verdict until Q-14 is answered; Condition: TCD-38-01; Technique: EP; Missing info: what is saved when the checkbox is not ticked (Q-14).; Risk: personal data left on a shared device.
914	
915	### TC-38-02 | Verify that typed but unsubmitted Name and Email are not kept after reload.
916	PRE: [STD] If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload. Chrome autofill of addresses is switched off (Settings > Autofill and passwords > Addresses and more).
917	1. Enter "Anna Smith" in "Name *".
918	2. Enter "anna.smith@example.com" in "Email *".
919	3. Reload the page (F5) without clicking "Submit".
920	4. Look at "Name *" and "Email *".
921	NOTES: OBSERVE ONLY — no verdict until Q-14 is answered; Condition: TCD-38-02; Technique: Error guessing; Missing info: Q-14.; Risk: personal data kept without consent.
922	
923	### TC-40-01 | Verify that double-clicking Submit creates only one review.
924	PRE: [STD]
925	1. Click the 4th star of "Your rating *".
926	2. Enter "Double click check." in "Your review *".
927	3. Enter "Anna Smith" in "Name *".
928	4. Enter "anna.smith@example.com" in "Email *".
929	5. Double-click "Submit" quickly.
930	6. Read "Pending approval".
931	7. Click "Moderator: approve pending reviews".
932	8. Count the reviews "Double click check." in the "Reviews" list.
933	NOTES: Condition: TCD-40-01; Technique: Error guessing; Edge case: rapid double click.; Assumption: only one review is created until Q-28 is answered.; Risk: duplicate reviews distort the rating.; Missing info: expected result not stated in any source (Q-28).
934	
935	### TC-40-02 | Verify that clicking Submit then pressing Enter quickly creates only one review.
936	PRE: [STD]
937	1. Click the 4th star of "Your rating *".
938	2. Enter "Click and Enter check." in "Your review *".
939	3. Enter "Anna Smith" in "Name *".
940	4. Enter "anna.smith@example.com" in "Email *".
941	5. Click "Submit". Immediately click in "Name *" and press Enter.
942	6. Read "Pending approval".
943	7. Click "Moderator: approve pending reviews".
944	8. Count the reviews "Click and Enter check." in the "Reviews" list.
945	NOTES: Condition: TCD-40-02; Technique: Error guessing; Assumption: only one review is created until Q-28 is answered.; Missing info: expected result not stated in any source (Q-28).
946	
947	97
948	
```

## AI (2026-10-21T04:24:45)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/exam && cat app-note.md user-story.md",
  "description": "Read exam app note and user story"
}
```

## Tool (2026-10-21T04:24:47)

```
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
# Exam: Submit a Product Review (text of the Word file)

Application name: My Shop
US-VP02: Submit a Product Review
As a customer, I want to submit a review for a product I purchased, so that I can share my experience with others.
Acceptance Criteria:
- Allow customers to enter a star rating
- Provide a text box for review comments
- Display approved reviews on the product page

The Word file also holds two mockup images, saved here as `mockup-1.png` and `mockup-2.png`.
```

## AI (2026-10-21T04:25:10)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1 && grep -E '^\\| TCD-(02|08|11|12|17|18|29|31|32|34|37|38|40)-' test-design.md | cut -c1-400",
  "description": "Get design conditions for selected TRs"
}
```

## Tool (2026-10-21T04:25:10)

```
| TCD-02-01 | EP | From no rating, clicking the 3rd star selects rating 3: stars 1 to 3 are shown as selected and stars 4 and 5 as not selected. | Positive | Assumption: the rating is a whole number from 1 to 5 until Q-03 is answered. |
| TCD-02-02 | EP | Clicking on the left half of a star does not set a half-star value (for example 2.5); the rating shown and saved is a whole number. | Negative | Missing info: whether half stars are allowed (Q-03). |
| TCD-02-03 | Error guessing | Moving the pointer over the stars without clicking, then moving it away, leaves the selected rating unchanged. | Negative | Assumption: a hover preview, if any, is not kept until Q-36 is answered. |
| TCD-02-04 | Error guessing | The rating can be selected with the keyboard only (Tab to the stars, then arrow keys, Space or Enter), and the selection is shown. | Positive | Missing info: keyboard use is not stated in any source (Q-34). |
| TCD-08-01 | EP | Review text with a length between the minimum and the maximum: the review is submitted and, after approval, the text is shown exactly as entered. | Positive | Missing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered. |
| TCD-08-02 | Error guessing | Review text with accented letters (é, ü), non-Latin letters (日本語), digits, punctuation and an emoji: accepted and shown unchanged. | Positive | Assumption: no character restriction in "Your review" until Q-37 is answered. |
| TCD-08-03 | Error guessing | Review text pasted from the clipboard is accepted and saved in the same way as typed text. | Positive | |
| TCD-11-01 | Error guessing | "Your review" contains only spaces, Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
| TCD-11-02 | Error guessing | "Your review" contains only line breaks (Enter pressed several times), Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: line breaks are treated like spaces (Q-17). |
| TCD-11-03 | Error guessing | Valid review text with leading and trailing spaces: accepted and, after approval, shown without the leading and trailing spaces. | Positive | Assumption: spaces are trimmed (Q-17). |
| TCD-11-04 | BVA | Review of (minimum - 1) visible characters plus one trailing space (length = minimum only if the space is counted), Submit: the review is not submitted. | Negative | Edge case: length reaches the minimum only through a space.<br>Assumption: length is counted after trimming (Q-17).<br>Missing info: minimum length not stated (Q-04). |
| TCD-12-01 | Error guessing | "Your review" contains `<script>alert(1)</script>`: no script runs, on submit or on the product page after approval. | Negative | Missing info: shown as plain text, removed or rejected (Q-15).<br>Assumption: content is never executed (Q-15).<br>Risk: script injection would affect every visitor of the product page. |
| TCD-12-02 | Error guessing | "Your review" contains `<img src=x onerror=alert(1)>`: no script runs and no image element is added to the page. | Negative | Missing info: handling not stated (Q-15).<br>Risk: script injection through an HTML attribute. |
| TCD-12-03 | Error guessing | "Your review" contains harmless HTML `<b>bold</b>`: the text is not rendered as bold HTML; it is shown as plain text, removed or rejected as confirmed for Q-15. | Negative | Missing info: handling not stated (Q-15). |
| TCD-12-04 | Error guessing | "Your review" contains a web link (`https://example.com`): it is shown, removed or rejected as confirmed for Q-15, and is not turned into a clickable link unless Q-15 allows it. | Negative | Missing info: handling of links not stated (Q-15). |
| TCD-12-05 | Error guessing | "Name" contains `<script>alert(1)</script>`: no script runs where the name is shown. | Negative | Missing info: handling not stated (Q-05, Q-15).<br>Risk: script injection through the reviewer name. |
| TCD-17-01 | EP | Each approved review shows its star rating, reviewer name, date and review text. | Positive | Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered. |
| TCD-17-02 | EP | The date shown with a review is the submit date, in an unambiguous format. | Positive | Assumption: submit date in any unambiguous format (Q-24). |
| TCD-17-03 | EP | The reviewer name is shown in the confirmed form (full name, first name only or initials). | Positive | Missing info: form of the name not specified (Q-09).<br>Risk: privacy of the reviewer's name. |
| TCD-18-01 | EP | Two reviews submitted one after the other with different rating, name and text: after approval each shows its own rating, name and text (no mix-up). | Positive | |
| TCD-18-02 | Error guessing | Name with accented letter, apostrophe and hyphen (for example "Zoë O'Brien-Lê"): shown exactly as entered, with no encoded characters such as `&#39;`. | Positive | Assumption: such names are accepted until Q-05 is answered. |
| TCD-18-03 | Error guessing | Review text with the characters `& < > " '` used as plain text (for example "5 > 3 & good"): shown exactly as entered, not as `&amp;` or `&gt;`. | Positive | Missing info: handling of HTML-like text (Q-15). |
| TCD-18-04 | Error guessing | Review of maximum length made of one long word with no spaces: shown in full without breaking the page layout. | Positive | Missing info: maximum length not stated (Q-04). |
| TCD-29-01 | EP | Name of Latin letters and a space (for example "Anna Smith"): accepted. | Positive | Assumption: letters and spaces are allowed until Q-05 is answered. |
| TCD-29-02 | EP | Name with accented letters (for example "Zoë Lê"): accepted. | Positive | Edge case: accented letters.<br>Assumption: accented letters are allowed until Q-05 is answered. |
| TCD-29-03 | EP | Name with a hyphen and an apostrophe (for example "Mary-Jane O'Neil"): accepted. | Positive | Edge case: hyphen and apostrophe.<br>Assumption: hyphens and apostrophes are allowed until Q-05 is answered. |
| TCD-29-04 | EP | Name in a non-Latin script (for example "李明"): accepted or rejected as confirmed for Q-05. | Positive | Missing info: allowed characters not stated (Q-05). |
| TCD-29-05 | EP | Name containing digits (for example "Anna2"): accepted or rejected with an error naming "Name", as confirmed for Q-05. | Negative | Missing info: whether digits are allowed (Q-05). |
| TCD-29-06 | EP | Name made only of symbols (for example "@#$%"): rejected with an error naming "Name", unless Q-05 allows it. | Negative | Missing info: allowed characters not stated (Q-05). |
| TCD-29-07 | BVA | Name of 1 character (just above empty): accepted. | Positive | Edge case: shortest non-empty name.<br>Missing info: minimum length not stated (Q-05). |
| TCD-29-08 | BVA | Name length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-05). |
| TCD-29-09 | BVA | Name length = maximum: accepted and shown in full. | Positive | Edge case: Name at the maximum length.<br>Missing info: maximum length not stated (Q-05). |
| TCD-29-10 | BVA | Name length = maximum + 1: input stops at the maximum, or the review is rejected with an error naming "Name". | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length and over-length behaviour not stated (Q-05, Q-18). |
| TCD-31-01 | EP | Email "anna.smith@example.com": accepted. | Positive | Assumption: standard format text@domain.tld until Q-06 is answered. |
| TCD-31-02 | EP | Email with a plus sign and a sub-domain ("anna+shop@mail.example.co.uk"): accepted. | Positive | Edge case: plus sign and sub-domain.<br>Assumption: standard format (Q-06). |
| TCD-31-03 | EP | Email without "@" ("anna.example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
| TCD-31-04 | EP | Email without the part before "@" ("@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
| TCD-31-05 | EP | Email without a domain ("anna@"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
| TCD-31-06 | EP | Email without a top-level domain ("anna@example"): rejected with an error naming "Email". | Negative | Assumption: a top-level domain is required (Q-06); some format rules accept this value. |
| TCD-31-07 | EP | Email with two "@" ("anna@@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
| TCD-31-08 | EP | Email with a space inside ("anna smith@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
| TCD-31-09 | Error guessing | Email in upper case ("ANNA@EXAMPLE.COM"): accepted. | Positive | Assumption: letter case does not matter (Q-06). |
| TCD-31-10 | BVA | Email length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-06). |
| TCD-31-11 | BVA | Email length = maximum: accepted. | Positive | Edge case: value exactly at the maximum.<br>Missing info: maximum length not stated (Q-06). |
| TCD-31-12 | BVA | Email length = maximum + 1: input stops at the maximum, or the review is rejected with an error naming "Email". | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length and over-length behaviour not stated (Q-06, Q-18). |
| TCD-32-01 | Error guessing | Name with leading and trailing spaces ("  Anna Smith  "): accepted and, after approval, shown as "Anna Smith". | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
| TCD-32-02 | Error guessing | Name made only of spaces, Submit: the review is not submitted and an error names "Name". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
| TCD-32-03 | Error guessing | Email with leading and trailing spaces ("  anna@example.com  "): accepted as a valid email. | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
| TCD-32-04 | Error guessing | Email made only of spaces, Submit: the review is not submitted and an error names "Email". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
| TCD-34-01 | Decision table | Rule: all four required fields empty, Submit: the review is not submitted and errors name all four fields. | Negative | Assumption: each error names its field; wording checked for meaning (Q-20). |
| TCD-34-02 | Decision table | Rule: rating and review empty, Name and Email valid, Submit: errors name the rating and "Your review" only, not Name or Email. | Negative | Assumption: wording checked for meaning (Q-20). |
| TCD-34-03 | Decision table | After a rejected Submit, the values already entered stay in the form; the customer corrects the field, submits again and the review is submitted. | Positive | Assumption: entered values are kept after a rejected submit until Q-38 is answered. |
| TCD-34-04 | EP | Leaving a required field empty and moving to the next field shows no error until Submit is pressed. | Positive | Assumption: fields are checked on Submit only (Q-19). |
| TCD-37-01 | State transition | Nothing saved, valid Submit with the box ticked, next visit in the same browser: Name and Email are filled with the submitted values. | Positive | Assumption: only name and email are saved (Q-13, Q-14).<br>Risk: personal data stored on the device. |
| TCD-37-02 | State transition | Name and Email saved, valid Submit with a different Name and Email and the box ticked, next visit: the new values are filled. | Positive | Assumption: saved values are replaced (Q-14). |
| TCD-37-03 | State transition | Name and Email saved, valid Submit with the box not ticked, next visit: Name and Email are filled or empty as confirmed for Q-14. | Positive | Missing info: how saved data is removed (Q-14).<br>Risk: personal data left on a shared device. |
| TCD-37-04 | EP | After a ticked Submit, on the next visit only Name and Email are filled; rating and review are empty. | Positive | Assumption: only name and email are saved (Q-13, Q-14). |
| TCD-37-05 | Error guessing | After a ticked Submit, opening the page in another browser or a private window: Name and Email are empty. | Positive | Edge case: "in this browser" only. |
| TCD-37-06 | State transition | Nothing saved, box ticked but Submit rejected (for example "Your review" empty), next visit: Name and Email are empty. | Negative | Edge case: rejected submit with the box ticked.<br>Missing info: whether data is saved on a rejected submit (Q-14). |
| TCD-38-01 | EP | Nothing saved, valid Submit with the box not ticked, next visit: Name and Email are empty. | Positive | Missing info: what is saved when the checkbox is not ticked (Q-14).<br>Risk: personal data left on a shared device. |
| TCD-38-02 | Error guessing | Name and Email typed but not submitted, page reloaded: Name and Email are empty (browser autofill switched off). | Positive | Missing info: Q-14.<br>Risk: personal data kept without consent. |
| TCD-40-01 | Error guessing | Valid form, Submit double-clicked: one review is created (one pending, one shown after approval). | Negative | Edge case: rapid double click.<br>Assumption: only one review is created (Q-28).<br>Risk: duplicate reviews distort the rating. |
| TCD-40-02 | Error guessing | Valid form, Submit clicked and Enter pressed in a text field before the confirmation appears: one review is created. | Negative | Assumption: only one review is created (Q-28). |
| TCD-40-03 | Error guessing | Page reloaded right after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |
| TCD-40-04 | Error guessing | Browser Back and then Forward after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |
| TCD-02-01, TCD-03-01 to TCD-03-04 | The rating is a whole number from 1 to 5, one per star. | Q-03 |
| TCD-02-03 | A hover preview, if any, is not kept after the pointer leaves. | Q-36 |
| TCD-08-02 | "Your review" has no character restriction (accented, non-Latin, emoji allowed). | Q-37 |
| TCD-11-01 to TCD-11-04, TCD-32-01 to TCD-32-04 | Spaces (and line breaks) are trimmed; a field of only spaces counts as empty; length is counted after trimming. | Q-17 |
| TCD-12-01 | HTML and script content is never executed, whatever the answer on how it is handled. | Q-15 |
| TCD-34-03 | Entered values stay in the form after a rejected Submit. | Q-38 |
| TCD-34-04 | Fields are checked on Submit only. | Q-19 |
| TCD-17-01 | Each displayed review shows star rating, reviewer name, date and review text. | Q-09 |
| TCD-17-02 | The date is the submit date, in any unambiguous format. | Q-24 |
| TCD-18-02, TCD-29-01 to TCD-29-03 | Names with letters, spaces, accented letters, hyphens and apostrophes are accepted. | Q-05 |
| TCD-31-01 to TCD-31-09 | A valid email has the standard format text@domain.tld (top-level domain required, letter case ignored). | Q-06 |
| TCD-37-01, TCD-37-02, TCD-37-04 | Only Name and Email are saved in this browser, and a new ticked submit replaces them. | Q-13, Q-14 |
| TCD-40-01 to TCD-40-04, TCD-41-04 | Only one review is created per submit action. | Q-28 |
```

## AI (2026-10-21T04:27:28)

**Tool call `Write`:**

```json
{
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\build_test_data.py",
  "content": "\"\"\"Build test-data.xlsx for the runnable test cases (skill: test-data-generation).\"\"\"\nimport re\nimport shutil\nimport sys\nfrom collections import Counter, OrderedDict\n\nimport openpyxl\nfrom openpyxl.styles import Alignment\n\nsys.stdout.reconfigure(encoding=\"utf-8\")\n\nBASE = sys.argv[1]  # .../manual-qa-sim-pass/submission\nTEMPLATE = BASE + \"/skills/test-data-generation/assets/test-data-template.xlsx\"\nTC_FILE = BASE + \"/runs/run-1/test-cases.xlsx\"\nOUT = BASE + \"/runs/run-1/test-data.xlsx\"\n\n# ---------------------------------------------------------------- rules / notes\nA_RATING = \"Assumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.\"\nA_REVIEW_LEN = \"Assumption: a length of {n} characters is between the unconfirmed minimum and maximum until Q-04 is answered.\"\nA_REVIEW_CHARS = 'Assumption: no character restriction in \"Your review\" until Q-37 is answered.'\nA_NAME = \"Assumption: letters and spaces are allowed and the length is within the unconfirmed limit until Q-05 is answered.\"\nA_EMAIL = \"Assumption: standard format text@domain.tld (top-level domain required) and length within the unconfirmed maximum until Q-06 is answered.\"\nA_TRIM = \"Assumption: leading and trailing spaces are trimmed and a field of only spaces counts as empty until Q-17 is answered.\"\nREQ = \"required field (Confirmed: mockup-1, R2)\"\n\nrows = []  # (tc, field, value, purpose, notes)\n\n\ndef add(tc, field, value, purpose, notes, typed=None):\n    if typed is not None and field in (\"Your review\", \"Name\", \"Email\"):\n        notes = notes.replace(\"{n}\", str(len(typed)))\n        notes += f\"\\nLength check: {len(typed)} characters\" + (\n            \" (counted including spaces and line breaks).\" if typed.strip() != typed or \"\\n\" in typed else \".\"\n        )\n    rows.append((tc, field, value, purpose, notes))\n\n\ndef rating(tc, n, purpose=\"valid\", rule=None, extra=()):\n    rule = rule or f\"Valid: whole rating {n} of 5, inside the range 1 to 5 (5 stars: Confirmed, mockup-1 R6).\"\n    add(tc, \"Your rating\", f\"{n} (click the {['1st','2nd','3rd','4th','5th'][n-1]} star)\", purpose,\n        \"\\n\".join([rule, A_RATING, *extra]))\n\n\ndef review(tc, text, purpose=\"valid\", rule=None, extra=(), value=None):\n    rule = rule or f\"Valid: {REQ} filled with plain text.\"\n    add(tc, \"Your review\", value if value is not None else text, purpose,\n        \"\\n\".join([rule, A_REVIEW_LEN, *extra]), typed=text)\n\n\ndef name(tc, text=\"Anna Smith\", purpose=\"valid\", rule=None, extra=(), value=None, assume=True):\n    rule = rule or f\"Valid: {REQ} filled with Latin letters and one space.\"\n    parts = [rule] + ([A_NAME] if assume else []) + list(extra)\n    add(tc, \"Name\", value if value is not None else text, purpose, \"\\n\".join(parts), typed=text)\n\n\ndef email(tc, text=\"anna.smith@example.com\", purpose=\"valid\", rule=None, extra=(), value=None, assume=True):\n    rule = rule or f\"Valid: {REQ} filled in standard format with the reserved domain example.com.\"\n    parts = [rule] + ([A_EMAIL] if assume else []) + list(extra)\n    add(tc, \"Email\", value if value is not None else text, purpose, \"\\n\".join(parts), typed=text)\n\n\ndef checkbox(tc, ticked, extra=()):\n    val = \"Ticked\" if ticked else \"Not ticked (default)\"\n    rule = (\"Valid: optional checkbox ticked; unticked by default (Confirmed: mockup-1, F5).\"\n            if ticked else \"Valid: optional checkbox left in its default unticked state (Confirmed: mockup-1, F5).\")\n    add(tc, \"Save checkbox\", val, \"valid\", \"\\n\".join([rule, *extra]))\n\n\ndef std(tc, text, n=4, nm=\"Anna Smith\", em=\"anna.smith@example.com\"):\n    rating(tc, n)\n    review(tc, text)\n    name(tc, nm)\n    email(tc, em)\n\n\nEMPTY = \"(empty: 0 characters)\"\n\n# ---------------------------------------------------------------- TR-02\nrating(\"TC-02-01\", 3, extra=[\"Edge case: middle value representing the valid partition 1 to 5.\"])\nadd(\"TC-02-02\", \"Your rating\", \"Click the left half of the 3rd star (attempts 2.5)\", \"invalid\",\n    \"Invalid: half-star value 2.5; breaks only the whole-number rule (the value is otherwise inside 1 to 5).\\n\"\n    + A_RATING + \"\\nMissing info: whether half stars are allowed (Q-03).\")\nreview(\"TC-02-02\", \"Half star check.\")\nname(\"TC-02-02\"); email(\"TC-02-02\")\nadd(\"TC-02-03\", \"Your rating\", \"2 (click the 2nd star), then hover over the 5th star without clicking\", \"valid\",\n    \"Valid: selected rating 2; the hover over star 5 must not change it.\\n\" + A_RATING\n    + \"\\nAssumption: a hover preview, if any, is not kept until Q-36 is answered.\")\nadd(\"TC-02-04\", \"Your rating\", \"4 (select the 4th star with Tab, arrow keys and Space or Enter; no mouse)\", \"valid\",\n    \"Valid: whole rating 4 of 5, entered by keyboard only.\\n\" + A_RATING\n    + \"\\nMissing info: keyboard use is not stated in any source (Q-34).\")\n\n# ---------------------------------------------------------------- TR-03 (BVA on rating)\nfor tc, n, text, rule in [\n    (\"TC-03-01\", 1, \"Rating check: one star.\", \"Boundary: rating 1 = minimum.\"),\n    (\"TC-03-02\", 2, \"Rating check: two stars.\", \"Boundary: rating 2 = minimum + 1.\"),\n    (\"TC-03-03\", 4, \"Rating check: four stars.\", \"Boundary: rating 4 = maximum - 1.\"),\n    (\"TC-03-04\", 5, \"Rating check: five stars.\", \"Boundary: rating 5 = maximum.\"),\n]:\n    ex = [\"Edge case: value exactly at the minimum.\"] if n == 1 else (\n        [\"Edge case: value exactly at the maximum.\"] if n == 5 else [])\n    rating(tc, n, \"boundary\", rule + \" Verified: compared with the assumed range 1 to 5.\", ex)\n    review(tc, text); name(tc); email(tc)\n\n# ---------------------------------------------------------------- TR-04 (state transition)\nfor tc, val, rule in [\n    (\"TC-04-01\", \"2 then 5 (click the 2nd star, then the 5th star); final rating 5\",\n     \"Valid: rating increased from 2 to 5; final value 5 is inside 1 to 5.\"),\n    (\"TC-04-02\", \"5 then 2 (click the 5th star, then the 2nd star); final rating 2\",\n     \"Valid: rating decreased from 5 to 2; final value 2 is inside 1 to 5.\"),\n    (\"TC-04-03\", \"3 then 3 again (click the 3rd star twice); final rating 3\",\n     \"Valid: clicking the selected star again must not clear the rating.\"),\n    (\"TC-04-04\", \"3 (click the 3rd star), then reload the page (F5)\",\n     \"Valid: rating 3 selected before the reload; after the reload no rating is expected.\"),\n    (\"TC-04-05\", \"1, then 4, then 2, then 3 (click the stars in this order); final rating 3\",\n     \"Valid: several changes; only the final value 3 is saved.\"),\n]:\n    add(tc, \"Your rating\", val, \"valid\",\n        rule + \"\\n\" + A_RATING + \"\\nAssumption: clicking another star changes the rating and the rating cannot be cleared by clicking until Q-16 is answered.\")\nreview(\"TC-04-05\", \"Changed rating, final is three.\"); name(\"TC-04-05\"); email(\"TC-04-05\")\n\n# ---------------------------------------------------------------- TR-05 / TR-06 / TR-07\nadd(\"TC-05-01\", \"Your rating\", \"(no star selected)\", \"invalid\",\n    f\"Invalid: rating left empty; breaks only the {REQ} rule.\\n\"\n    \"Edge case: 0 stars is one below the minimum 1.\\n\" + A_RATING)\nreview(\"TC-05-01\", \"Soft fabric, true to size. Would buy again.\"); name(\"TC-05-01\"); email(\"TC-05-01\")\n\nadd(\"TC-06-01\", \"Your review\", \"Line one[Enter]Line two\", \"valid\",\n    \"Valid: text on two lines; [Enter] = press the Enter key once (1 line break).\\n\"\n    \"Edge case: value with a line break.\\n\" + A_REVIEW_LEN, typed=\"Line one\\nLine two\")\nrating(\"TC-06-02\", 4)\nadd(\"TC-06-02\", \"Your review\", \"Line one[Enter]Line two[Enter]Line three\", \"valid\",\n    \"Valid: text on three lines; [Enter] = press the Enter key (2 line breaks).\\n\"\n    \"Edge case: value with line breaks.\\n\" + A_REVIEW_LEN\n    + \"\\nAssumption: line breaks are shown as entered until Q-35 is answered.\", typed=\"Line one\\nLine two\\nLine three\")\nname(\"TC-06-02\"); email(\"TC-06-02\")\n\nrating(\"TC-07-01\", 4)\nadd(\"TC-07-01\", \"Your review\", EMPTY, \"invalid\", f\"Invalid: review left empty; breaks only the {REQ} rule.\")\nname(\"TC-07-01\"); email(\"TC-07-01\")\n\n# ---------------------------------------------------------------- TR-08\nrating(\"TC-08-01\", 4)\nreview(\"TC-08-01\", \"Soft fabric, true to size. Would buy again.\",\n       rule=f\"Valid: {REQ}; plain text inside the length range (equivalence partition).\",\n       extra=[\"Missing info: minimum and maximum length not stated (Q-04); this value does not test a limit.\"])\nname(\"TC-08-01\"); email(\"TC-08-01\")\nrating(\"TC-08-02\", 4)\nt = \"Très bien, Größe M passt! 日本語 OK 100% 👍\"\nreview(\"TC-08-02\", t, rule=\"Valid: accented letters (è, ö, ß), non-Latin letters (日本語), digits, punctuation and one emoji.\",\n       extra=[A_REVIEW_CHARS, \"Edge case: the emoji is 1 character but 2 UTF-16 code units; a counter may show \"\n              f\"{len(t.encode('utf-16-le')) // 2} instead of {len(t)}.\"])\nname(\"TC-08-02\"); email(\"TC-08-02\")\nrating(\"TC-08-03\", 4)\nreview(\"TC-08-03\", \"Pasted review: comfy and soft.\",\n       rule=\"Valid: plain text pasted from the clipboard (copy it from Notepad before step 1, per the pre-condition).\")\nname(\"TC-08-03\"); email(\"TC-08-03\")\n\n# ---------------------------------------------------------------- TR-11\nrating(\"TC-11-01\", 4)\nadd(\"TC-11-01\", \"Your review\", '\" \" x 5 (5 spaces, nothing else)', \"invalid\",\n    \"Invalid: spaces only; breaks only the required rule once trimmed (trimmed length 0).\\n\"\n    \"Edge case: whitespace-only input.\\n\" + A_TRIM, typed=\"     \")\nname(\"TC-11-01\"); email(\"TC-11-01\")\nrating(\"TC-11-02\", 4)\nadd(\"TC-11-02\", \"Your review\", \"[Enter] x 3 (3 line breaks, nothing else)\", \"invalid\",\n    \"Invalid: line breaks only; breaks only the required rule once trimmed (trimmed length 0).\\n\"\n    \"Edge case: whitespace-only input.\\n\" + A_TRIM\n    + \"\\nAssumption: line breaks are treated like spaces until Q-17 is answered.\", typed=\"\\n\\n\\n\")\nname(\"TC-11-02\"); email(\"TC-11-02\")\nrating(\"TC-11-03\", 4)\nadd(\"TC-11-03\", \"Your review\", '\"   Space padded review.   \" (3 spaces before and 3 after)', \"valid\",\n    \"Valid: 20-character text \\\"Space padded review.\\\" with leading and trailing spaces; expected shown trimmed.\\n\"\n    \"Edge case: leading and trailing spaces.\\n\" + A_TRIM + \"\\n\" + A_REVIEW_LEN, typed=\"   Space padded review.   \")\nname(\"TC-11-03\"); email(\"TC-11-03\")\n\n# ---------------------------------------------------------------- TR-12 (injection)\nA_Q15 = \"Assumption: HTML and script content is never executed until Q-15 is answered.\\nMissing info: whether it is shown as plain text, removed or rejected (Q-15).\"\nfor tc, txt, rule, risk in [\n    (\"TC-12-01\", \"<script>alert(1)</script>\", \"Invalid: script tag; breaks only the content rule (never executed). Non-empty and short, so the other rules hold.\",\n     \"Risk: script injection would affect every visitor of the product page.\"),\n    (\"TC-12-02\", \"<img src=x onerror=alert(1)>\", \"Invalid: HTML image tag with an event handler; breaks only the content rule (never executed).\",\n     \"Risk: script injection through an HTML attribute.\"),\n    (\"TC-12-03\", \"<b>bold</b> text check\", \"Invalid: harmless HTML formatting tag; breaks only the content rule (not rendered as HTML).\", None),\n    (\"TC-12-04\", \"Link check https://example.com\", \"Invalid: web link (reserved domain example.com); breaks only the content rule (not a clickable link unless Q-15 allows it).\", None),\n]:\n    rating(tc, 4)\n    review(tc, txt, \"invalid\", rule, [A_Q15] + ([risk] if risk else []))\n    name(tc); email(tc)\nrating(\"TC-12-05\", 4)\nreview(\"TC-12-05\", \"Name script check.\")\nname(\"TC-12-05\", \"<script>alert(1)</script>\", \"invalid\",\n     \"Invalid: script tag in the name; breaks only the content rule (never executed).\",\n     [A_Q15, \"Missing info: allowed name characters not stated (Q-05).\", \"Risk: script injection through the reviewer name.\"],\n     assume=False)\nemail(\"TC-12-05\")\n\n# ---------------------------------------------------------------- TR-14 / 16 / 17\nstd(\"TC-14-01\", \"Approval check: shown after approve.\")\nstd(\"TC-14-02\", \"Approve twice check.\")\nstd(\"TC-16-01\", \"Author view: pending check.\")\nstd(\"TC-16-02\", \"Author view: approved check.\")\nstd(\"TC-17-01\", \"Details check: all parts shown.\")\nstd(\"TC-17-02\", \"Date check: submit date.\")\nstd(\"TC-17-03\", \"Name form check.\")\n\n# ---------------------------------------------------------------- TR-18\nrating(\"TC-18-01\", 2, extra=[\"Review 1 of 2 (steps 1-5).\"])\nreview(\"TC-18-01\", \"First review: too tight.\", extra=[\"Review 1 of 2 (steps 1-5).\"])\nname(\"TC-18-01\", \"Ben Carter\", extra=[\"Review 1 of 2 (steps 1-5).\"])\nemail(\"TC-18-01\", \"ben.carter@example.com\", extra=[\"Review 1 of 2 (steps 1-5).\"])\nrating(\"TC-18-01\", 5, extra=[\"Review 2 of 2 (steps 7-11); differs from review 1 in every field.\"])\nreview(\"TC-18-01\", \"Second review: perfect fit.\", extra=[\"Review 2 of 2 (steps 7-11).\"])\nname(\"TC-18-01\", \"Chloe Diaz\", extra=[\"Review 2 of 2 (steps 7-11).\"])\nemail(\"TC-18-01\", \"chloe.diaz@example.com\", extra=[\"Review 2 of 2 (steps 7-11).\"])\nrating(\"TC-18-02\", 4)\nreview(\"TC-18-02\", \"Special name check.\")\nname(\"TC-18-02\", \"Zoë O'Brien-Lê\", rule=f\"Valid: {REQ} with accented letters (ë, ê), an apostrophe and a hyphen; must be shown with no encoded characters such as &#39;.\",\n     extra=[\"Assumption: accented letters, apostrophes and hyphens are allowed until Q-05 is answered.\",\n            \"Edge case: characters often HTML-encoded on display.\"])\nemail(\"TC-18-02\")\nrating(\"TC-18-03\", 4)\nreview(\"TC-18-03\", \"5 > 3 & \\\"good\\\" isn't it\",\n       rule=\"Valid: plain text containing the characters > & \\\" ' ; must be shown as typed, not as &gt; &amp; &quot; &#39;.\",\n       extra=[\"Missing info: handling of HTML-like text (Q-15).\", \"Edge case: special characters.\"])\nname(\"TC-18-03\"); email(\"TC-18-03\")\n\n# ---------------------------------------------------------------- TR-19 (email privacy)\nfor tc, txt in [(\"TC-19-01\", \"Email privacy check: visible page.\"), (\"TC-19-02\", \"Email privacy check: hidden parts.\")]:\n    rating(tc, 4); review(tc, txt); name(tc)\n    email(tc, \"unique.reviewer@example.com\",\n          rule=\"Valid: standard format, reserved domain example.com; the local part \\\"unique.reviewer\\\" is unique on the page so a search finds only this email.\",\n          extra=[\"Risk: personal data could be shown publicly (email must never be published, Confirmed R3).\"])\n\n# ---------------------------------------------------------------- TR-20 / TR-23\nstd(\"TC-20-02\", \"Order check: newly approved.\")\nrating(\"TC-23-01\", 1, extra=[\"Chosen to change the average visibly. If the initial reviews are 5, 4 and 3 (TC-23-05 pre-condition), the expected summary after approval is (5+4+3+1)/4 = 3.25 from 4 reviews.\",\n                             \"Missing info: whether a summary is shown and how it is rounded (Q-11).\"])\nreview(\"TC-23-01\", \"Summary check: approved 1 star.\"); name(\"TC-23-01\"); email(\"TC-23-01\")\nrating(\"TC-23-02\", 1, extra=[\"Chosen so that a wrong count would change the average visibly; while pending the summary must stay as written down (e.g. 4.0 from 3 reviews if the initial ratings are 5, 4, 3).\",\n                             \"Missing info: Q-11.\"])\nreview(\"TC-23-02\", \"Summary check: pending 1 star.\"); name(\"TC-23-02\"); email(\"TC-23-02\")\nstd(\"TC-23-04\", \"Summary check: count.\")\nrating(\"TC-23-05\", 2, \"boundary\",\n       \"Boundary: with the initial ratings 5, 4 and 3, adding 2 gives an average of exactly (5+4+3+2)/4 = 3.50, on a half-star rounding step.\",\n       [\"Missing info: rounding rule not stated (Q-11); values next to the step (for example 4.33) are added when Q-11 is answered.\",\n        \"Assumption: rounding steps fall on half stars until Q-11 is answered.\"])\nreview(\"TC-23-05\", \"Rounding check: two stars.\"); name(\"TC-23-05\"); email(\"TC-23-05\")\n\n# ---------------------------------------------------------------- TR-28 / 29 (Name)\nrating(\"TC-28-01\", 4); review(\"TC-28-01\", \"Soft fabric, true to size. Would buy again.\")\nadd(\"TC-28-01\", \"Name\", EMPTY, \"invalid\", f\"Invalid: name left empty; breaks only the {REQ} rule.\")\nemail(\"TC-28-01\")\nfor tc, nm, purpose, rule, extra in [\n    (\"TC-29-01\", \"Anna Smith\", \"valid\", f\"Valid: {REQ} with Latin letters and one space.\", []),\n    (\"TC-29-02\", \"Zoë Lê\", \"valid\", f\"Valid: {REQ} with accented letters (ë, ê).\",\n     [\"Edge case: accented letters.\", \"Assumption: accented letters are allowed until Q-05 is answered.\"]),\n    (\"TC-29-03\", \"Mary-Jane O'Neil\", \"valid\", f\"Valid: {REQ} with a hyphen and an apostrophe.\",\n     [\"Edge case: hyphen and apostrophe.\", \"Assumption: hyphens and apostrophes are allowed until Q-05 is answered.\"]),\n    (\"TC-29-04\", \"李明\", \"valid\", f\"Valid: {REQ} in a non-Latin script (2 CJK characters).\",\n     [\"Assumption: non-Latin letters are allowed until Q-05 is answered.\", \"Missing info: allowed characters not stated (Q-05).\"]),\n    (\"TC-29-05\", \"Anna2\", \"invalid\", \"Invalid: one digit added to a valid name; breaks only the letters-only rule.\",\n     [\"Assumption: digits are not allowed in a name until Q-05 is answered.\", \"Missing info: whether digits are allowed (Q-05).\"]),\n    (\"TC-29-06\", \"@#$%\", \"invalid\", \"Invalid: symbols only, no letters; breaks only the allowed-characters rule (non-empty, short).\",\n     [\"Assumption: a name must contain letters until Q-05 is answered.\", \"Missing info: allowed characters not stated (Q-05).\"]),\n    (\"TC-29-07\", \"A\", \"boundary\", \"Boundary: name length 1 = assumed minimum (shortest non-empty value). Verified: 1 character.\",\n     [\"Edge case: shortest non-empty name.\", \"Assumption: minimum name length is 1 until Q-05 is answered.\"]),\n]:\n    rating(tc, 4); review(tc, f\"Name check {tc[3:]}.\")\n    name(tc, nm, purpose, rule, extra, assume=(tc == \"TC-29-01\"))\n    email(tc)\n\n# ---------------------------------------------------------------- TR-30 / 31 (Email)\nrating(\"TC-30-01\", 4); review(\"TC-30-01\", \"Soft fabric, true to size. Would buy again.\"); name(\"TC-30-01\")\nadd(\"TC-30-01\", \"Email\", EMPTY, \"invalid\", f\"Invalid: email left empty; breaks only the {REQ} rule.\")\nfor tc, em, purpose, rule, extra in [\n    (\"TC-31-01\", \"anna.smith@example.com\", \"valid\", \"Valid: standard format local@domain.tld, reserved domain example.com.\", []),\n    (\"TC-31-02\", \"anna+shop@mail.example.com\", \"valid\",\n     \"Valid: plus sign in the local part and a sub-domain (mail.) of the reserved domain example.com.\",\n     [\"Edge case: plus sign and sub-domain.\",\n      \"Assumption: the test case and test design (TCD-31-02) give \\\"anna+shop@mail.example.co.uk\\\"; example.co.uk is not a reserved domain (test-data-rules.md Privacy), so the reserved sub-domain mail.example.com is used instead. Update TC-31-02 step 4 to this value.\"]),\n    (\"TC-31-03\", \"anna.example.com\", \"invalid\", \"Invalid: no \\\"@\\\"; breaks only the \\\"@ required\\\" rule (local part, domain and top-level domain otherwise present).\", []),\n    (\"TC-31-04\", \"@example.com\", \"invalid\", \"Invalid: nothing before \\\"@\\\"; breaks only the \\\"local part required\\\" rule.\", []),\n    (\"TC-31-05\", \"anna@\", \"invalid\", \"Invalid: nothing after \\\"@\\\"; breaks only the \\\"domain required\\\" rule.\", []),\n    (\"TC-31-06\", \"anna@example\", \"invalid\", \"Invalid: no top-level domain; breaks only the \\\"top-level domain required\\\" rule.\",\n     [\"Assumption: a top-level domain is required until Q-06 is answered; some format rules accept this value.\"]),\n    (\"TC-31-07\", \"anna@@example.com\", \"invalid\", \"Invalid: two \\\"@\\\"; breaks only the \\\"exactly one @\\\" rule.\", []),\n    (\"TC-31-08\", \"anna smith@example.com\", \"invalid\", \"Invalid: a space inside the local part; breaks only the \\\"no spaces\\\" rule.\", []),\n    (\"TC-31-09\", \"ANNA@EXAMPLE.COM\", \"valid\", \"Valid: standard format in upper case, reserved domain example.com.\",\n     [\"Assumption: letter case does not matter until Q-06 is answered.\"]),\n]:\n    rating(tc, 4); review(tc, f\"Email check {tc[3:]}.\"); name(tc)\n    email(tc, em, purpose, rule, extra)\n\n# ---------------------------------------------------------------- TR-32 (trimming)\nrating(\"TC-32-01\", 4); review(\"TC-32-01\", \"Name trim check.\")\nname(\"TC-32-01\", \"  Anna Smith  \", \"valid\",\n     \"Valid: \\\"Anna Smith\\\" (10 characters) with 2 spaces before and 2 after; expected shown trimmed.\",\n     [\"Edge case: space-padded input.\", A_TRIM], value='\"  Anna Smith  \" (2 spaces before and 2 after)')\nemail(\"TC-32-01\")\nrating(\"TC-32-02\", 4); review(\"TC-32-02\", \"Soft fabric, true to size. Would buy again.\")\nname(\"TC-32-02\", \"     \", \"invalid\", \"Invalid: spaces only; breaks only the required rule once trimmed (trimmed length 0).\",\n     [\"Edge case: whitespace-only input.\", A_TRIM], value='\" \" x 5 (5 spaces, nothing else)', assume=False)\nemail(\"TC-32-02\")\nrating(\"TC-32-03\", 4); review(\"TC-32-03\", \"Email trim check.\"); name(\"TC-32-03\")\nemail(\"TC-32-03\", \"  anna@example.com  \", \"valid\",\n      \"Valid: \\\"anna@example.com\\\" (16 characters) with 2 spaces before and 2 after; expected accepted as a valid email.\",\n      [\"Edge case: space-padded input.\", A_TRIM], value='\"  anna@example.com  \" (2 spaces before and 2 after)')\nrating(\"TC-32-04\", 4); review(\"TC-32-04\", \"Soft fabric, true to size. Would buy again.\"); name(\"TC-32-04\")\nemail(\"TC-32-04\", \"     \", \"invalid\", \"Invalid: spaces only; breaks only the required rule once trimmed (trimmed length 0).\",\n      [\"Edge case: whitespace-only input.\", A_TRIM], value='\" \" x 5 (5 spaces, nothing else)', assume=False)\n\n# ---------------------------------------------------------------- TR-33 / 34 / 35\nfor tc, tick in [(\"TC-33-01\", False), (\"TC-33-02\", True)]:\n    std(tc, \"Soft fabric, true to size. Would buy again.\")\n    checkbox(tc, tick)\nadd(\"TC-34-01\", \"Your rating\", \"(no star selected)\", \"invalid\", f\"Invalid: rating left empty; breaks only the {REQ} rule.\\nDecision table rule: all four required fields empty in one Submit.\")\nadd(\"TC-34-01\", \"Your review\", EMPTY, \"invalid\", f\"Invalid: review left empty; breaks only the {REQ} rule.\\nDecision table rule: all four required fields empty in one Submit.\")\nadd(\"TC-34-01\", \"Name\", EMPTY, \"invalid\", f\"Invalid: name left empty; breaks only the {REQ} rule.\\nDecision table rule: all four required fields empty in one Submit.\")\nadd(\"TC-34-01\", \"Email\", EMPTY, \"invalid\", f\"Invalid: email left empty; breaks only the {REQ} rule.\\nDecision table rule: all four required fields empty in one Submit.\")\nadd(\"TC-34-02\", \"Your rating\", \"(no star selected)\", \"invalid\", f\"Invalid: rating left empty; breaks only the {REQ} rule.\\nDecision table rule: rating and review empty, Name and Email valid.\")\nadd(\"TC-34-02\", \"Your review\", EMPTY, \"invalid\", f\"Invalid: review left empty; breaks only the {REQ} rule.\\nDecision table rule: rating and review empty, Name and Email valid.\")\nname(\"TC-34-02\"); email(\"TC-34-02\")\nrating(\"TC-34-03\", 4)\nadd(\"TC-34-03\", \"Your review\", EMPTY + \" at step 2\", \"invalid\", f\"Invalid: review left empty for the first Submit (step 5); breaks only the {REQ} rule.\")\nreview(\"TC-34-03\", \"Soft fabric, true to size. Would buy again.\",\n       rule=f\"Valid: correction typed at step 7 for the second Submit; {REQ} filled with plain text.\",\n       extra=[\"Assumption: entered values are kept after a rejected Submit until Q-38 is answered.\"])\nname(\"TC-34-03\"); email(\"TC-34-03\")\nadd(\"TC-34-04\", \"Name\", EMPTY + \" (click in, then Tab out without typing)\", \"invalid\",\n    f\"Invalid: name left empty; breaks only the {REQ} rule. No Submit in this test.\\n\"\n    \"Assumption: fields are checked on Submit only until Q-19 is answered.\")\nfor tc, tick in [(\"TC-35-01\", False), (\"TC-35-02\", True)]:\n    std(tc, \"Soft fabric, true to size. Would buy again.\")\n    checkbox(tc, tick, [\"Assumption: Name and Email stay filled only if the checkbox was ticked until Q-22 is answered.\"])\n\n# ---------------------------------------------------------------- TR-36 / 37 / 38 (save checkbox)\nA_SAVE = \"Assumption: only Name and Email are saved in this browser until Q-13 and Q-14 are answered.\"\nstd(\"TC-36-02\", \"Return visit check.\"); checkbox(\"TC-36-02\", True, [\"Missing info: checkbox state on a return visit (Q-14).\"])\nstd(\"TC-37-01\", \"Save check: first visit.\"); checkbox(\"TC-37-01\", True, [A_SAVE, \"Risk: personal data stored on the device.\"])\nrating(\"TC-37-02\", 4); review(\"TC-37-02\", \"Save check: replace.\")\nname(\"TC-37-02\", \"Ben Carter\", extra=[\"Replaces the saved name \\\"Anna Smith\\\" (pre-condition, from TC-37-01).\"])\nemail(\"TC-37-02\", \"ben.carter@example.com\", extra=[\"Replaces the saved email \\\"anna.smith@example.com\\\" (pre-condition, from TC-37-01).\"])\ncheckbox(\"TC-37-02\", True, [\"Assumption: saved values are replaced until Q-14 is answered.\"])\nrating(\"TC-37-03\", 4); review(\"TC-37-03\", \"Save check: untick.\")\nname(\"TC-37-03\", extra=[\"Pre-condition data: already saved in this browser and filled on load (run TC-37-01 first); not typed in the steps.\"])\nemail(\"TC-37-03\", extra=[\"Pre-condition data: already saved in this browser and filled on load (run TC-37-01 first); not typed in the steps.\"])\ncheckbox(\"TC-37-03\", False, [\"Missing info: how saved data is removed (Q-14).\", \"Risk: personal data left on a shared device.\"])\nstd(\"TC-37-04\", \"Save check: only name and email.\"); checkbox(\"TC-37-04\", True, [A_SAVE])\nstd(\"TC-37-05\", \"Save check: private window.\"); checkbox(\"TC-37-05\", True, [\"Edge case: \\\"in this browser\\\" only.\"])\nrating(\"TC-37-06\", 4)\nadd(\"TC-37-06\", \"Your review\", EMPTY, \"invalid\", f\"Invalid: review left empty so that Submit is rejected; breaks only the {REQ} rule.\")\nname(\"TC-37-06\"); email(\"TC-37-06\")\ncheckbox(\"TC-37-06\", True, [\"Missing info: whether data is saved on a rejected Submit (Q-14).\"])\nstd(\"TC-38-01\", \"No save check.\"); checkbox(\"TC-38-01\", False, [\"Missing info: what is saved when the checkbox is not ticked (Q-14).\", \"Risk: personal data left on a shared device.\"])\nname(\"TC-38-02\", extra=[\"Typed but not submitted (page reloaded without Submit).\"])\nemail(\"TC-38-02\", extra=[\"Typed but not submitted (page reloaded without Submit).\"])\n\n# ---------------------------------------------------------------- TR-40\nstd(\"TC-40-01\", \"Double click check.\")\nstd(\"TC-40-02\", \"Click and Enter check.\")\n\n# ---------------------------------------------------------------- verification\nwb_tc = openpyxl.load_workbook(TC_FILE)\nws_tc = wb_tc.active\ntc_order, runnable, skipped = [], set(), []\nfor r in ws_tc.iter_rows(min_row=2, values_only=True):\n    tcid, notes = r[1], (r[6] or \"\")\n    tc_order.append(tcid)\n    if notes.startswith(\"BLOCKED\") or notes.startswith(\"NOT RUN\"):\n        skipped.append(tcid)\n    else:\n        runnable.add(tcid)\n\nused = OrderedDict()\nfor row in rows:\n    assert row[0] in runnable, f\"data for non-runnable TC {row[0]}\"\n    assert row[3] in (\"valid\", \"invalid\", \"boundary\"), row\n    used.setdefault(row[0], 0)\n\n# privacy: every email-looking token must use a reserved domain\nfor row in rows:\n    for m in re.findall(r\"[\\w.+-]*@([\\w.-]+)\", row[2]):\n        assert re.search(r\"(^|\\.)example\\.(com|org|test)$\", m.lower()) or m.lower() == \"example\", (row, m)\n\n# order rows by the TC order of test-cases.xlsx (stable within a TC)\norder = {t: i for i, t in enumerate(tc_order)}\nrows.sort(key=lambda x: order[x[0]])\n\n# ---------------------------------------------------------------- export\nshutil.copyfile(TEMPLATE, OUT)\nwb = openpyxl.load_workbook(OUT)\nws = wb[\"Test Data\"]\ncounter = Counter()\nfor i, (tc, field, value, purpose, notes) in enumerate(rows, start=2):\n    counter[tc] += 1\n    did = f\"D-{tc}-{counter[tc]:02d}\"\n    for col, v in enumerate([tc, did, field, value, purpose, notes], start=1):\n        c = ws.cell(row=i, column=col, value=v)\n        c.alignment = Alignment(wrap_text=True, vertical=\"top\")\nwb.save(OUT)\n\nno_data = [t for t in tc_order if t in runnable and t not in used]\nprint(\"rows\", len(rows))\nprint(\"runnable TCs\", len(runnable), \"skipped\", len(skipped), \"with data\", len(used))\nprint(\"no data:\", no_data)\nprint(\"by purpose:\", Counter(r[3] for r in rows))\nprint(\"by field:\", Counter(r[1] for r in rows))\nprint(\"by purpose+field:\", sorted(Counter((r[1], r[3]) for r in rows).items()))\n"
}
```

## Tool (2026-10-21T04:27:28)

```
File created successfully at: C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\build_test_data.py (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:27:38)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program && python -I \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/build_test_data.py\" \"C:/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission\"",
  "description": "Generate test-data.xlsx from runnable test cases"
}
```

## Tool (2026-10-21T04:27:41)

```
rows 332
runnable TCs 97 skipped 48 with data 86
no data: ['TC-01-01', 'TC-14-03', 'TC-20-01', 'TC-25-01', 'TC-25-02', 'TC-25-03', 'TC-25-04', 'TC-25-05', 'TC-25-06', 'TC-25-07', 'TC-36-01']
by purpose: Counter({'valid': 295, 'invalid': 31, 'boundary': 6})
by field: Counter({'Your rating': 84, 'Your review': 79, 'Name': 79, 'Email': 78, 'Save checkbox': 12})
by purpose+field: [(('Email', 'invalid'), 9), (('Email', 'valid'), 69), (('Name', 'boundary'), 1), (('Name', 'invalid'), 7), (('Name', 'valid'), 71), (('Save checkbox', 'valid'), 12), (('Your rating', 'boundary'), 5), (('Your rating', 'invalid'), 4), (('Your rating', 'valid'), 75), (('Your review', 'invalid'), 11), (('Your review', 'valid'), 68)]
```

## AI (2026-10-21T04:27:47)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1 && python -I -c \"\nimport sys,re; sys.stdout.reconfigure(encoding='utf-8')\nimport openpyxl\nwb=openpyxl.load_workbook('test-data.xlsx'); ws=wb.active\nprint(wb.sheetnames, ws.max_row, [ws.column_dimensions[c].width for c in 'ABCDEF'], [c.value for c in ws[1]])\ndata={}\nfor r in ws.iter_rows(min_row=2,values_only=True): data.setdefault(r[0],[]).append(r)\ntc=openpyxl.load_workbook('test-cases.xlsx').active\nfor r in tc.iter_rows(min_row=2,values_only=True):\n    if r[1] not in data: continue\n    vals=' || '.join(str(x[3]) for x in data[r[1]])\n    for q in re.findall(r'(?:Enter|with) \\\"([^\\\"]+)\\\"', r[4]):\n        if q not in vals and q.strip() not in vals: print('MISSING',r[1],repr(q))\nfor row in list(ws.iter_rows(min_row=2,max_row=8,values_only=True))+[x for x in ws.iter_rows(values_only=True) if x[0] in ('TC-08-02','TC-31-02','TC-11-03')]:\n    print(row)\n\"",
  "description": "Verify output workbook against test case steps"
}
```

## Tool (2026-10-21T04:27:49)

```
['Test Data'] 333 [12.0, 18.0, 20.0, 50.0, 12.0, 45.0] ['TC ID', 'Data ID', 'Field', 'Value', 'Purpose', 'Notes']
MISSING TC-31-02 'anna+shop@mail.example.co.uk'
('TC-02-01', 'D-TC-02-01-01', 'Your rating', '3 (click the 3rd star)', 'valid', 'Valid: whole rating 3 of 5, inside the range 1 to 5 (5 stars: Confirmed, mockup-1 R6).\nAssumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.\nEdge case: middle value representing the valid partition 1 to 5.')
('TC-02-02', 'D-TC-02-02-01', 'Your rating', 'Click the left half of the 3rd star (attempts 2.5)', 'invalid', 'Invalid: half-star value 2.5; breaks only the whole-number rule (the value is otherwise inside 1 to 5).\nAssumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.\nMissing info: whether half stars are allowed (Q-03).')
('TC-02-02', 'D-TC-02-02-02', 'Your review', 'Half star check.', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled with plain text.\nAssumption: a length of 16 characters is between the unconfirmed minimum and maximum until Q-04 is answered.\nLength check: 16 characters.')
('TC-02-02', 'D-TC-02-02-03', 'Name', 'Anna Smith', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled with Latin letters and one space.\nAssumption: letters and spaces are allowed and the length is within the unconfirmed limit until Q-05 is answered.\nLength check: 10 characters.')
('TC-02-02', 'D-TC-02-02-04', 'Email', 'anna.smith@example.com', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled in standard format with the reserved domain example.com.\nAssumption: standard format text@domain.tld (top-level domain required) and length within the unconfirmed maximum until Q-06 is answered.\nLength check: 22 characters.')
('TC-02-03', 'D-TC-02-03-01', 'Your rating', '2 (click the 2nd star), then hover over the 5th star without clicking', 'valid', 'Valid: selected rating 2; the hover over star 5 must not change it.\nAssumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.\nAssumption: a hover preview, if any, is not kept until Q-36 is answered.')
('TC-02-04', 'D-TC-02-04-01', 'Your rating', '4 (select the 4th star with Tab, arrow keys and Space or Enter; no mouse)', 'valid', 'Valid: whole rating 4 of 5, entered by keyboard only.\nAssumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.\nMissing info: keyboard use is not stated in any source (Q-34).')
('TC-08-02', 'D-TC-08-02-01', 'Your rating', '4 (click the 4th star)', 'valid', 'Valid: whole rating 4 of 5, inside the range 1 to 5 (5 stars: Confirmed, mockup-1 R6).\nAssumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.')
('TC-08-02', 'D-TC-08-02-02', 'Your review', 'Très bien, Größe M passt! 日本語 OK 100% 👍', 'valid', 'Valid: accented letters (è, ö, ß), non-Latin letters (日本語), digits, punctuation and one emoji.\nAssumption: a length of 39 characters is between the unconfirmed minimum and maximum until Q-04 is answered.\nAssumption: no character restriction in "Your review" until Q-37 is answered.\nEdge case: the emoji is 1 character but 2 UTF-16 code units; a counter may show 40 instead of 39.\nLength check: 39 characters.')
('TC-08-02', 'D-TC-08-02-03', 'Name', 'Anna Smith', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled with Latin letters and one space.\nAssumption: letters and spaces are allowed and the length is within the unconfirmed limit until Q-05 is answered.\nLength check: 10 characters.')
('TC-08-02', 'D-TC-08-02-04', 'Email', 'anna.smith@example.com', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled in standard format with the reserved domain example.com.\nAssumption: standard format text@domain.tld (top-level domain required) and length within the unconfirmed maximum until Q-06 is answered.\nLength check: 22 characters.')
('TC-11-03', 'D-TC-11-03-01', 'Your rating', '4 (click the 4th star)', 'valid', 'Valid: whole rating 4 of 5, inside the range 1 to 5 (5 stars: Confirmed, mockup-1 R6).\nAssumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.')
('TC-11-03', 'D-TC-11-03-02', 'Your review', '"   Space padded review.   " (3 spaces before and 3 after)', 'valid', 'Valid: 20-character text "Space padded review." with leading and trailing spaces; expected shown trimmed.\nEdge case: leading and trailing spaces.\nAssumption: leading and trailing spaces are trimmed and a field of only spaces counts as empty until Q-17 is answered.\nAssumption: a length of 26 characters is between the unconfirmed minimum and maximum until Q-04 is answered.\nLength check: 26 characters (counted including spaces and line breaks).')
('TC-11-03', 'D-TC-11-03-03', 'Name', 'Anna Smith', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled with Latin letters and one space.\nAssumption: letters and spaces are allowed and the length is within the unconfirmed limit until Q-05 is answered.\nLength check: 10 characters.')
('TC-11-03', 'D-TC-11-03-04', 'Email', 'anna.smith@example.com', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled in standard format with the reserved domain example.com.\nAssumption: standard format text@domain.tld (top-level domain required) and length within the unconfirmed maximum until Q-06 is answered.\nLength check: 22 characters.')
('TC-31-02', 'D-TC-31-02-01', 'Your rating', '4 (click the 4th star)', 'valid', 'Valid: whole rating 4 of 5, inside the range 1 to 5 (5 stars: Confirmed, mockup-1 R6).\nAssumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.')
('TC-31-02', 'D-TC-31-02-02', 'Your review', 'Email check 31-02.', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled with plain text.\nAssumption: a length of 18 characters is between the unconfirmed minimum and maximum until Q-04 is answered.\nLength check: 18 characters.')
('TC-31-02', 'D-TC-31-02-03', 'Name', 'Anna Smith', 'valid', 'Valid: required field (Confirmed: mockup-1, R2) filled with Latin letters and one space.\nAssumption: letters and spaces are allowed and the length is within the unconfirmed limit until Q-05 is answered.\nLength check: 10 characters.')
('TC-31-02', 'D-TC-31-02-04', 'Email', 'anna+shop@mail.example.com', 'valid', 'Valid: plus sign in the local part and a sub-domain (mail.) of the reserved domain example.com.\nAssumption: standard format text@domain.tld (top-level domain required) and length within the unconfirmed maximum until Q-06 is answered.\nEdge case: plus sign and sub-domain.\nAssumption: the test case and test design (TCD-31-02) give "anna+shop@mail.example.co.uk"; example.co.uk is not a reserved domain (test-data-rules.md Privacy), so the reserved sub-domain mail.example.com is used instead. Update TC-31-02 step 4 to this value.\nLength check: 26 characters.')
```

## AI (2026-10-21T04:27:56)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program && S=\"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/build_test_data.py\"; sed -i 's|\"Assumption: the test case and test design (TCD-31-02) give|\"Risk: the test case and test design (TCD-31-02) give|' \"$S\" && grep -c 'Risk: the test case and test design' \"$S\" && python -I \"$S\" \"C:/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission\" && git -C /c/AI_Enabled_Program status --short evaluator/test-fixtures/manual-qa-sim-pass",
  "description": "Retag TC-31-02 note as Risk and regenerate"
}
```

## Tool (2026-10-21T04:27:59)

```
1
rows 332
runnable TCs 97 skipped 48 with data 86
no data: ['TC-01-01', 'TC-14-03', 'TC-20-01', 'TC-25-01', 'TC-25-02', 'TC-25-03', 'TC-25-04', 'TC-25-05', 'TC-25-06', 'TC-25-07', 'TC-36-01']
by purpose: Counter({'valid': 295, 'invalid': 31, 'boundary': 6})
by field: Counter({'Your rating': 84, 'Your review': 79, 'Name': 79, 'Email': 78, 'Save checkbox': 12})
by purpose+field: [(('Email', 'invalid'), 9), (('Email', 'valid'), 69), (('Name', 'boundary'), 1), (('Name', 'invalid'), 7), (('Name', 'valid'), 71), (('Save checkbox', 'valid'), 12), (('Your rating', 'boundary'), 5), (('Your rating', 'invalid'), 4), (('Your rating', 'valid'), 75), (('Your review', 'invalid'), 11), (('Your review', 'valid'), 68)]
?? evaluator/test-fixtures/manual-qa-sim-pass/
```

## AI (2026-10-21T04:28:17)

I wrote the test data file at `C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-1\test-data.xlsx`, following your test-data-generation skill. It has 332 rows, one per field value, with Data IDs in the form D-TC-xx-yy-nn. I made it by copying the template, so the sheet name, header row and column widths are unchanged. Nothing else was written or edited, and nothing was committed.

**Which cases got data**
- The test case file has 145 cases. 48 have Notes starting with BLOCKED or NOT RUN, so I skipped them.
- That leaves 97 runnable cases, including the 22 marked "OBSERVE ONLY".
- 86 of the 97 have data.
- 11 runnable cases have no data because their steps don't fill in any field: TC-01-01, TC-14-03, TC-20-01, TC-25-01 to TC-25-07, and TC-36-01.

**Values by purpose**

| Purpose | Rows | What they are |
|---|---|---|
| valid | 295 | Rating 75, review 68, name 71, email 69, save checkbox 12 |
| invalid | 31 | Rating 4, review 11, name 7, email 9 |
| boundary | 6 | Ratings 1, 2, 4 and 5 (TC-03-01 to TC-03-04), rating 2 in TC-23-05, and name "A" (TC-29-07) |

**Checks**
- **Values match the steps:** every value typed in the test case steps appears exactly in the data, with one exception (TC-31-02, below).
- **Lengths:** each text value has its length counted in Notes, spaces and line breaks included. In TC-08-02 the emoji counts as 1 character, but a character counter may show 40 instead of 39.
- **Invalid values:** each one breaks exactly one rule; Notes says which.
- **Privacy:** every email uses a reserved domain (example.com), and a script check confirmed this. There are no real accounts or secrets.

**Values built on assumptions.** Almost every value rests on an unanswered question; none is marked as confirmed. Only "required", "5 stars" and "checkbox unticked by default" come from the mockup. The assumptions are:
- the rating is a whole number from 1 to 5 (Q-03);
- review length is within limits nobody has stated (Q-04);
- allowed name characters and length (Q-05). This covers accented names, "李明" as valid, "Anna2" and "@#$%" as invalid, and a minimum of 1;
- the email format is text@domain.tld with a top-level domain required, and letter case ignored (Q-06);
- leading and trailing spaces are trimmed (Q-17);
- HTML and script text is never run (Q-15);
- what the save checkbox keeps (Q-13, Q-14, Q-22);
- entered values stay after a rejected Submit (Q-38);
- fields are checked on Submit only (Q-19);
- a half-star rounding step for TC-23-05 (Q-11).

**Decisions for you**
1. **TC-31-02 changed.** The step uses `anna+shop@mail.example.co.uk`, but example.co.uk is not a reserved domain, so it breaks the privacy rule. I used `anna+shop@mail.example.com` instead, which still has the plus sign and the sub-domain. TC-31-02 step 4 and TCD-31-02 in `test-design.md` should be updated to match.
2. **Realistic names kept.** I kept the names from the steps ("Anna Smith", "Ben Carter", "Chloe Diaz", "Mary-Jane O'Neil", "Zoë Lê", "Zoë O'Brien-Lê", "李明") so the data matches the test cases. They don't belong to known people. Your rules prefer clearly fake names like "Test User 01"; switching would mean changing both the test cases and the data.

**Other choices:**
- TC-34-03 has two review rows: empty for the first Submit, then the corrected text.
- TC-18-01 has two full sets of values, one per review.
- TC-37-03 lists the saved name and email from its pre-condition, marked as not typed in the steps.
- TC-23-01 and TC-23-05 notes give the expected average if the starting ratings are 5, 4 and 3: 3.25 and 3.50.

I used only the files you named and the exam folder (`exam/app-note.md`, `exam/user-story.md`). The build script is at `C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\build_test_data.py` if you want to regenerate the file.

## Tool (2026-10-21T04:28:18)

```
{"success":true,"message":"Report delivered to your caller."}
```
