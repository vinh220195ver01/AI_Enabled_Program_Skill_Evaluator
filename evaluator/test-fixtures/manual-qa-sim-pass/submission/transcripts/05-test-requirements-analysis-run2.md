# Transcript 05: test-requirements-analysis (run2)

Exported from the agent session log. Kept verbatim: the trainee's messages, the AI's replies, tool calls and tool results. Left out: harness reminders and private thinking. The harness prefix in front of follow-up messages is removed; the AI's final report is shown as an AI reply.

## Trainee (2026-10-21T04:29:41)

hi, I want to run my requirement analysis skill again to see if the output is consistent. skill: evaluator/test-fixtures/manual-qa-sim-pass/submission/skills/test-requirements-analysis/SKILL.md (read it and follow it).

user story: evaluator/test-fixtures/manual-qa-sim-pass/exam/user-story.md (mockups mockup-1.png, mockup-2.png in the same folder)
knowledge: evaluator/test-fixtures/manual-qa-sim-pass/submission/knowledge
output folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-2

still no PO answers. don't look at runs/run-1, I want an independent run. only the exam folder and my knowledge folder, nothing else under test-fixtures. tell me the files you wrote + number of TRs and questions.

## AI (2026-10-21T04:29:46)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\skills\\test-requirements-analysis\\SKILL.md"
}
```

## Tool (2026-10-21T04:29:46)

```
1	---
2	name: test-requirements-analysis
3	description: Use when reviewing a user story and its acceptance criteria (plus mockups, if any) before any test design starts, to find ambiguous points, raise clarification questions grouped as Must ask and Nice to confirm, and build the Test Requirement list; writes clarification-questions.md and test-requirements.xlsx. Do NOT use to choose test techniques, write test cases or report defects.
4	---
5	
6	# Test Requirements Analysis
7	
8	Turns one user story into (1) clarification questions for the product owner and (2) a traceable Test Requirement (TR) list. It does not design tests.
9	
10	## Inputs
11	
12	- {user_story}: the user story, its acceptance criteria and any mockups for this run, as attached files or pasted text. If missing, ask the user; do not guess.
13	- {knowledge_dir}: the project's knowledge folder (business rules, glossary, screens, environment). If missing, ask the user. If the user says there is none, continue and tag every rule you rely on as Assumption.
14	- {output_dir}: the folder where the output files are written. If missing, ask the user.
15	- Answers already received from the product owner, if any: given by the user. Never invent answers.
16	
17	## Process
18	
19	1. Read {user_story} and list every acceptance criterion in the given order with an AC ID (AC-01, AC-02, ...). Write the AC text word for word; do not rephrase it.
20	2. Read the index file in {knowledge_dir} and open only the files it lists for requirements analysis. Note each statement you use as Fact (stated in a source), Assumption or Open question, with its source file.
21	3. Identify the ambiguous points of each AC and of the story as a whole by walking through `references/ambiguity-checklist.md` item by item.
22	4. Classify each ambiguous point as Must ask or Nice to confirm with the rule in `references/ambiguity-checklist.md` (section "Must ask or Nice to confirm"), and write one specific question per point.
23	5. Write `{output_dir}/clarification-questions.md` from `assets/clarification-questions-template.md`, keeping both groups even if one is empty.
24	6. Derive the Test Requirements for each AC with `references/tr-writing-rules.md`, and tag each Notes entry with the tags in `references/note-tags.md`.
25	7. Check coverage: every AC ID has at least one TR; every Must ask question is linked to at least one TR through a "Missing info" note; no TR states a rule that is not in a source unless it is tagged Assumption.
26	8. Export the TR list by copying `assets/test-requirement-template.xlsx` to `{output_dir}/test-requirements.xlsx` and filling it, keeping the sheet name, header row and column widths.
27	9. Report to the user: the number of ACs, TRs and questions, the Must ask list, and every Assumption; then stop and wait for the user's review before any test design.
28	
29	## Exceptions
30	
31	- Input missing or unreadable (empty story, no AC, image cannot be opened): stop and ask the user for it; do not continue on a guess.
32	- Sources conflict (for example the story says one thing and a mockup or knowledge file another): write the conflict as a Must ask question quoting both sources; do not choose one.
33	- The template cannot be copied or the file cannot be written: show the error, retry once with a corrected path, then stop and ask the user.
34	
35	## Output
36	
37	- `{output_dir}/clarification-questions.md`: questions grouped as Must ask and Nice to confirm, each linked to an AC ID.
38	- `{output_dir}/test-requirements.xlsx`: one row per TR, in the layout of `assets/test-requirement-template.xlsx`.
39	
40	## Files
41	
42	- `references/ambiguity-checklist.md`: open at Steps 3 and 4.
43	- `references/tr-writing-rules.md`: open at Step 6.
44	- `references/note-tags.md`: open at Step 6. Other skills also use this file; edit it only here.
45	- `assets/clarification-questions-template.md`: open at Step 5; copy it, never rebuild it.
46	- `assets/test-requirement-template.xlsx`: open at Step 8; copy it, never rebuild it.
47	
```

## AI (2026-10-21T04:29:47)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && ls -la exam submission submission/knowledge submission/skills/test-requirements-analysis; ls submission/runs 2>/dev/null",
  "description": "List exam, knowledge, and skill folders"
}
```

## Tool (2026-10-21T04:29:48)

```
exam:
total 105
drwxr-xr-x 1 vinh.the.nguyen 1049089     0 Oct 21 10:46 .
drwxr-xr-x 1 vinh.the.nguyen 1049089     0 Oct 21 10:50 ..
-rw-r--r-- 1 vinh.the.nguyen 1049089 60243 Oct 21 10:45 User Story for My Shop.docx
drwxr-xr-x 1 vinh.the.nguyen 1049089     0 Oct 21 10:46 app
-rw-r--r-- 1 vinh.the.nguyen 1049089  1004 Oct 21 10:46 app-note.md
-rw-r--r-- 1 vinh.the.nguyen 1049089 26510 Oct 21 10:45 mockup-1.png
-rw-r--r-- 1 vinh.the.nguyen 1049089  5472 Oct 21 10:45 mockup-2.png
-rw-r--r-- 1 vinh.the.nguyen 1049089   486 Oct 21 10:45 user-story.md

submission:
total 8
drwxr-xr-x 1 vinh.the.nguyen 1049089 0 Oct 21 11:01 .
drwxr-xr-x 1 vinh.the.nguyen 1049089 0 Oct 21 10:50 ..
drwxr-xr-x 1 vinh.the.nguyen 1049089 0 Oct 21 10:53 knowledge
drwxr-xr-x 1 vinh.the.nguyen 1049089 0 Oct 21 11:01 review
drwxr-xr-x 1 vinh.the.nguyen 1049089 0 Oct 21 10:58 runs
drwxr-xr-x 1 vinh.the.nguyen 1049089 0 Oct 21 10:52 skills

submission/knowledge:
total 24
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 10:53 .
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 11:01 ..
-rw-r--r-- 1 vinh.the.nguyen 1049089 1172 Oct 21 10:53 environment.md
-rw-r--r-- 1 vinh.the.nguyen 1049089 1432 Oct 21 10:53 glossary.md
-rw-r--r-- 1 vinh.the.nguyen 1049089 2314 Oct 21 10:53 index.md
-rw-r--r-- 1 vinh.the.nguyen 1049089 3228 Oct 21 11:00 product-review-rules.md
-rw-r--r-- 1 vinh.the.nguyen 1049089 2377 Oct 21 10:53 screens-and-fields.md

submission/skills/test-requirements-analysis:
total 12
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 10:50 .
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 10:52 ..
-rw-r--r-- 1 vinh.the.nguyen 1049089 3901 Oct 21 10:54 SKILL.md
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 10:52 assets
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 10:50 references
run-1
```

## AI (2026-10-21T04:29:52)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && cat exam/user-story.md; echo ----; cat submission/knowledge/index.md; echo ----; ls submission/skills/test-requirements-analysis/references submission/skills/test-requirements-analysis/assets; for f in submission/skills/test-requirements-analysis/references/*.md submission/skills/test-requirements-analysis/assets/*.md; do echo \"==== $f\"; cat \"$f\"; done",
  "description": "Read user story, knowledge index, and skill references"
}
```

## Tool (2026-10-21T04:29:56)

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
----
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
----
submission/skills/test-requirements-analysis/assets:
clarification-questions-template.md
test-requirement-template.xlsx

submission/skills/test-requirements-analysis/references:
ambiguity-checklist.md
note-tags.md
tr-writing-rules.md
==== submission/skills/test-requirements-analysis/references/ambiguity-checklist.md
# Ambiguity checklist for a user story

General QA checklist. Walk through every item for each acceptance criterion (AC) and for the story as a whole. An item that the sources do not answer is an ambiguous point.

## What to look for

| # | Area | Questions to ask yourself |
|---|---|---|
| 1 | Actor and access | Who can do this? Must the user be signed in? Are there preconditions on the user (role, earlier action such as a purchase)? What happens for a user who does not meet them? |
| 2 | Mandatory and optional | Which inputs are required, which optional? Does the mockup mark the same fields as the text? |
| 3 | Field rules | For each input: type, allowed values, minimum and maximum length or value, format, allowed characters, leading/trailing spaces, default value. |
| 4 | Validation and messages | When is input validated (on typing, on leaving the field, on submit)? What message is shown, where, and in what wording? |
| 5 | Business rules | Limits, counts, uniqueness (for example one item per user), calculations (totals, averages, rounding). |
| 6 | States and workflow | Which states does the object go through (draft, pending, approved, rejected...)? Who moves it between states? What does the user see in each state? |
| 7 | Display rules | What is displayed, in which order, how many at a time, with which details (name, date format), what is shown when the list is empty? |
| 8 | Feedback after an action | Success message, where the user lands, what is reset or kept in the form. |
| 9 | Data handling and privacy | What personal data is collected, stored, displayed or hidden? Is anything remembered between visits? |
| 10 | Edit, delete, duplicates | Can the user change or remove what they created? What happens on double submit? |
| 11 | Error handling | Behaviour on server or network error, timeout, session expiry. |
| 12 | Non-functional | Supported browsers and devices, accessibility, language, performance expectations. |
| 13 | Consistency between sources | Text vs mockup vs knowledge files: labels, fields and rules that differ or appear in one source only. |
| 14 | Out of scope | What the story does not cover and should be confirmed as excluded. |

## Must ask or Nice to confirm

- **Must ask**: a test case cannot get a definite Expected Result without the answer, or the answer changes what is built or accepted (a required rule, a limit, a state change, who can do the action, a conflict between sources, a privacy question).
- **Nice to confirm**: we can test with a reasonable, stated assumption and the risk of being wrong is low (wording of a message, layout detail, minor display format).
- When in doubt, put it in Must ask.

## Writing the question

- One ambiguous point per question; name the AC ID and the exact field or rule.
- Make it answerable: offer the options you see (for example "Is the limit X, or no limit?") without assuming one.
- Never write a generic question such as "Is there anything else required?".
- Keep the tone short, clear and polite; the reader is the product owner or customer.
==== submission/skills/test-requirements-analysis/references/note-tags.md
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
==== submission/skills/test-requirements-analysis/references/tr-writing-rules.md
# Test Requirement writing rules

## IDs

- AC ID: `AC-01`, `AC-02`, ... in the order of the source.
- TR ID: `TR-01`, `TR-02`, ... numbered continuously across the whole list (not restarted per AC).
- Requirements implied by the story but not tied to one AC (for example access rules): use AC ID `AC-GEN`, and write a short origin in the Acceptance Criteria column, e.g. `General: form fields shown in the mockup`. No file paths. Notes keep the tags from `note-tags.md` only.

## One TR

- One TR = one testable behaviour, starting with "Verify that ..." (for example "Verify that the form cannot be submitted when a required field is empty").
- Write what must be true, not how to test it (no steps, no test data).
- Cover both sides where they exist: the accepted behaviour and the rejected behaviour.
- Do not add rules that no source states. If a TR needs one, keep the TR and tag the rule as Assumption in Notes.

## Columns

| Column | Content |
|---|---|
| AC ID | AC ID from Step 1 |
| Acceptance Criteria | The AC text, word for word (repeat it on every TR row of that AC) |
| TR ID | See IDs |
| Test Requirements | "Verify that ..." |
| Notes | Zero or more tagged notes, one per line, tags from `note-tags.md` |

## Self-check

- Every AC has at least one TR.
- No two TRs test the same behaviour.
- Each TR can later get a clear pass/fail result.
==== submission/skills/test-requirements-analysis/assets/clarification-questions-template.md
# Clarification questions: {story_id} {story_title}

Sources reviewed: {list of source files}
Date: {date}

## Must ask

| Q ID | AC ID | Ambiguous point | Question | Why it matters |
|---|---|---|---|---|
| Q-01 | | | | |

## Nice to confirm

| Q ID | AC ID | Ambiguous point | Question | Assumption used until answered |
|---|---|---|---|---|
| Q-xx | | | | |

## Conflicts between sources

| Q ID | Source A says | Source B says |
|---|---|---|
| | | |
```

## AI (2026-10-21T04:29:59)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/knowledge && for f in product-review-rules.md screens-and-fields.md glossary.md; do echo \"==== $f\"; cat \"$f\"; done",
  "description": "Read knowledge files for requirements analysis"
}
```

## AI (2026-10-21T04:29:59)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\exam\\mockup-1.png"
}
```

## AI (2026-10-21T04:30:00)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\exam\\mockup-2.png"
}
```

## Tool (2026-10-21T04:30:04)

```
==== product-review-rules.md
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
==== screens-and-fields.md
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
==== glossary.md
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
```

## Tool (2026-10-21T04:30:04)

```
[image]
```

## Tool (2026-10-21T04:30:04)

```
[image]
```

## AI (2026-10-21T04:30:11)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/skills/test-requirements-analysis/assets && python -c \"\nimport openpyxl\nwb=openpyxl.load_workbook('test-requirement-template.xlsx')\nfor ws in wb:\n  print(ws.title, ws.dimensions, ws.freeze_panes)\n  for k,v in ws.column_dimensions.items(): print(k, v.width)\n  for r in ws.iter_rows(min_row=1,max_row=min(ws.max_row,5)):\n    for c in r:\n      if c.value is not None: print(c.coordinate, repr(c.value), c.font.b, c.fill.fgColor.rgb, c.alignment.wrap_text)\n\"",
  "description": "Inspect the TR xlsx template structure"
}
```

## Tool (2026-10-21T04:30:12)

```
Test Requirements A1:E1 A2
A 10.0
B 45.0
C 10.0
D 60.0
E 50.0
A1 'AC ID' True 001F4E78 True
B1 'Acceptance Criteria' True 001F4E78 True
C1 'TR ID' True 001F4E78 True
D1 'Test Requirements' True 001F4E78 True
E1 'Notes' True 001F4E78 True
```

## AI (2026-10-21T04:31:29)

**Tool call `Bash`:**

```json
{
  "command": "mkdir -p /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-2 && ls /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-2",
  "description": "Create run-2 output folder"
}
```

## Tool (2026-10-21T04:31:30)

```
(Bash completed with no output)
```

## AI (2026-10-21T04:31:54)

**Tool call `Write`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\runs\\run-2\\clarification-questions.md",
  "content": "# Clarification questions: US-VP02 Submit a Product Review\n\nSources reviewed: exam/user-story.md, exam/mockup-1.png, exam/mockup-2.png (company logo only, no screen content), knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md\nDate: 2026-10-21\n\n## Must ask\n\n| Q ID | AC ID | Ambiguous point | Question | Why it matters |\n|---|---|---|---|---|\n| Q-01 | AC-GEN | Purchase check (\"a product I purchased\") | Must the system allow only customers who bought this product to submit a review, or can anyone who opens the product page submit one? If a purchase check applies, what does a non-buyer see? | Decides who can perform the action; without it the access tests have no expected result. |\n| Q-02 | AC-GEN | Sign-in requirement | Must the customer be signed in to submit a review, or can a guest submit by typing Name and Email (as the mockup form suggests)? | The story speaks of a customer who purchased, while the form asks for Name and Email as for a guest; the expected access behaviour depends on the answer. |\n| Q-03 | AC-01 | Star rating values | Is the rating a whole number of stars from 1 to 5, or are half stars (for example 3.5) allowed? | Defines the valid and invalid rating values to test and how the rating is stored and shown. |\n| Q-04 | AC-02 | Review text length | What are the minimum and maximum lengths of \"Your review\" (for example 1 to 500 characters, another limit, or no limit)? What happens when the maximum is reached: typing is blocked, or an error is shown on submit? | Boundary tests need exact limits and the expected behaviour at and beyond them. |\n| Q-05 | AC-02 | Review text made of spaces only | Is a review that contains only spaces or line breaks treated as empty (rejected), and are leading and trailing spaces removed before saving? | Decides whether such input passes the required-field check. |\n| Q-06 | AC-GEN | Name field rules | What are the maximum length and the allowed characters of \"Name\" (letters only, digits, symbols, accented letters)? Is a Name of spaces only rejected? | Needed for valid and invalid Name tests; the story gives no rule. |\n| Q-07 | AC-GEN | Email field rules | Which email format is accepted (for example name@domain.tld), and is there a maximum length? | Needed to decide which Email values are valid or invalid. |\n| Q-08 | AC-03 | Moderation workflow | Who approves reviews, and can a review be rejected? If rejected, is it deleted or kept hidden, and is the author told? | AC-03 shows only approved reviews; the states and their effects must be known to test the display rule. |\n| Q-09 | AC-GEN | Feedback after a successful submit | After a successful submit, is the author told that the review is waiting for approval? Is the form cleared or are the entered values kept? | Defines the expected result of the main submit flow. |\n| Q-10 | AC-03 | Details shown per approved review | Which details are shown for each approved review: star rating, Name as entered, submission date, review text? Anything else? Please confirm that the email is never shown. | Defines the expected content of every displayed review and protects personal data. |\n| Q-11 | AC-03 | Order and paging of reviews | In which order are approved reviews shown (newest first, oldest first, highest rating first), and is there a limit per page or a \"load more\" control? | Without it the display tests have no definite expected result. |\n| Q-12 | AC-03 | Rating summary and review count | Does the product page show an average rating and a review count? If yes, are they calculated from approved reviews only, and how is the average rounded? | A calculation rule that changes the expected values on the product page. |\n| Q-13 | AC-GEN | More than one review per customer | Can the same customer submit more than one review for the same product? If not, what happens on the second attempt? | Uniqueness rule that changes what is accepted. |\n| Q-14 | AC-GEN | Checkbox mentions a Website field that does not exist | The checkbox says \"Save my name, email, and website in this browser for the next time I comment.\" but the form has no Website field. Should a Website field be added, or should the label read \"Save my name and email ...\"? | Conflict inside the mockup; we cannot decide which one is correct. |\n| Q-15 | AC-GEN | What the \"Save my name, email ...\" checkbox stores | When the checkbox is ticked, exactly what is saved, where (this browser only), and for how long? Are the saved values pre-filled on the next visit, and are they removed when the box is left unticked? | Privacy: personal data kept in the browser. |\n| Q-16 | AC-02 | Content rules for review text | Are HTML tags, links or offensive words in the review blocked, removed, or shown as plain text? | Security and content risk on a public page; the expected result differs for each option. |\n\n## Nice to confirm\n\n| Q ID | AC ID | Ambiguous point | Question | Assumption used until answered |\n|---|---|---|---|---|\n| Q-17 | AC-GEN | Validation timing and message wording | Is the form validated on submit only, or also while typing or when leaving a field? What are the exact wording and position of the error messages? | Validation is done on submit; a message identifies each missing or invalid field; the exact wording and position are not checked. |\n| Q-18 | AC-GEN | Success message wording | What is the exact text of the message shown after a successful submit? | Any clear confirmation message is accepted; the wording is not checked. |\n| Q-19 | AC-01 | Changing the rating before submit | Can the customer change the selected rating by clicking another star before submitting? | Clicking another star replaces the earlier selection, and the last selection is submitted. |\n| Q-20 | AC-02 | Allowed characters in review text | Are accented letters, emoji and line breaks allowed in \"Your review\"? | All printable characters and line breaks are allowed and are shown as entered. |\n| Q-21 | AC-03 | Date format of a displayed review | In which format is the review date shown (for example 21/10/2026 or October 21, 2026)? | Any unambiguous date format is accepted. |\n| Q-22 | AC-03 | Product page with no approved reviews | What is shown in the reviews area when a product has no approved reviews? | A short message saying there are no reviews yet is shown; the wording is not checked. |\n| Q-23 | AC-GEN | Double submit | If Submit is clicked twice quickly, should only one review be created? | Only one review is created. |\n| Q-24 | AC-GEN | Server or network error on submit | What should the customer see if the review cannot be saved because of a server or network error? | An error message is shown, no review is created, and the entered values are kept. |\n| Q-25 | AC-GEN | Edit or delete own review | Is editing or deleting a submitted review out of scope for US-VP02? | Out of scope; no tests are planned for it. |\n| Q-26 | AC-GEN | Supported browsers, devices and language | Which browsers, devices and languages must be supported? | Latest desktop Chrome, English user interface. |\n\n## Conflicts between sources\n\n| Q ID | Source A says | Source B says |\n|---|---|---|\n| Q-14 | mockup-1.png, checkbox label: \"Save my name, email, and website in this browser for the next time I comment.\" | mockup-1.png, form fields: only \"Your rating *\", \"Your review *\", \"Name *\" and \"Email *\"; there is no Website field. |\n"
}
```

## Tool (2026-10-21T04:31:54)

```
File created successfully at: C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-2\clarification-questions.md (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:32:28)

**Tool call `Write`:**

```json
{
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\fill_trs.py",
  "content": "import shutil, sys, re\nimport openpyxl\nfrom openpyxl.styles import Alignment\n\ntpl, out = sys.argv[1], sys.argv[2]\nshutil.copyfile(tpl, out)\n\nAC = {\n    \"AC-01\": \"Allow customers to enter a star rating\",\n    \"AC-02\": \"Provide a text box for review comments\",\n    \"AC-03\": \"Display approved reviews on the product page\",\n}\nG_ACCESS = \"General: who can submit a review (user story)\"\nG_FORM = \"General: form fields shown in the mockup\"\nG_SUBMIT = \"General: submitting the form and the feedback shown\"\nG_SAVE = \"General: \\\"Save my name, email, and website\\\" checkbox in the mockup\"\nG_DUP = \"General: duplicate submits and error handling\"\n\nrows = [\n (\"AC-01\", None, \"Verify that the review form shows 5 star icons for \\\"Your rating *\\\".\", \"\"),\n (\"AC-01\", None, \"Verify that the customer can select a rating by clicking a star and the selected number of stars is shown as selected.\",\n  \"Assumption: rating is a whole number from 1 to 5, one per star, until Q-03 is answered.\\nMissing info: whether half stars are allowed (Q-03).\"),\n (\"AC-01\", None, \"Verify that the lowest and the highest rating values are accepted and saved with the review.\",\n  \"Edge case: 1 star and 5 stars.\\nAssumption: valid range is 1 to 5 whole stars until Q-03 is answered.\\nMissing info: valid rating values (Q-03).\"),\n (\"AC-01\", None, \"Verify that the review cannot be submitted when no star rating is selected.\",\n  \"Assumption: validation happens on submit and the message names the rating field; wording not checked until Q-17 is answered.\\nRisk: reviews without a rating would distort the product rating.\"),\n (\"AC-01\", None, \"Verify that the customer can change the selected rating before submitting and the last selected rating is the one saved.\",\n  \"Assumption: clicking another star replaces the earlier selection until Q-19 is answered.\\nEdge case: rating changed several times before submit.\"),\n\n (\"AC-02\", None, \"Verify that the review form shows a multi-line text box labelled \\\"Your review *\\\".\", \"\"),\n (\"AC-02\", None, \"Verify that the review cannot be submitted when the \\\"Your review\\\" text box is empty.\",\n  \"Assumption: validation happens on submit and the message names the review field; wording not checked until Q-17 is answered.\"),\n (\"AC-02\", None, \"Verify that a review text made only of spaces or line breaks is treated as empty and rejected.\",\n  \"Edge case: spaces only, line breaks only.\\nAssumption: whitespace-only text counts as empty until Q-05 is answered.\\nMissing info: trimming of leading and trailing spaces (Q-05).\"),\n (\"AC-02\", None, \"Verify that a review text within the allowed length is accepted and saved exactly as entered.\",\n  \"Missing info: minimum and maximum length of the review text (Q-04).\"),\n (\"AC-02\", None, \"Verify that a review text longer than the maximum length is not accepted (typing blocked or error on submit) and a text exactly at the maximum is accepted.\",\n  \"Edge case: length at the maximum and maximum + 1.\\nMissing info: maximum length and the behaviour when it is reached (Q-04).\"),\n (\"AC-02\", None, \"Verify that a review text shorter than the minimum length is rejected and a text exactly at the minimum is accepted.\",\n  \"Edge case: length at the minimum and minimum - 1 (a single character if there is no minimum).\\nMissing info: minimum length (Q-04).\"),\n (\"AC-02\", None, \"Verify that HTML or script code entered in the review is never executed on the product page.\",\n  \"Risk: script injection on a public page could affect every visitor.\\nAssumption: the code is either blocked or shown as plain text until Q-16 is answered.\\nMissing info: whether HTML is blocked, removed or shown as text (Q-16).\"),\n (\"AC-02\", None, \"Verify that links and offensive words in the review are handled according to the content rule.\",\n  \"Missing info: whether links and offensive words are blocked, removed or allowed (Q-16).\\nRisk: spam or offensive content shown publicly.\"),\n (\"AC-02\", None, \"Verify that a review text with accented letters, emoji and line breaks is accepted and displayed unchanged.\",\n  \"Assumption: all printable characters and line breaks are allowed until Q-20 is answered.\\nEdge case: mixed scripts and emoji.\"),\n\n (\"AC-03\", None, \"Verify that a newly submitted review is not displayed on the product page before it is approved.\",\n  \"Missing info: who approves and how (Q-08).\\nRisk: unmoderated content shown publicly.\"),\n (\"AC-03\", None, \"Verify that a review is displayed on the product page after it is approved.\",\n  \"Missing info: approval process (Q-08).\"),\n (\"AC-03\", None, \"Verify that a rejected review is never displayed on the product page.\",\n  \"Missing info: whether reviews can be rejected and what happens to them (Q-08).\"),\n (\"AC-03\", None, \"Verify that each displayed review shows the agreed details: star rating, Name, date and review text.\",\n  \"Assumption: details are rating, Name, date and review text until Q-10 is answered.\\nMissing info: exact list of details shown (Q-10).\"),\n (\"AC-03\", None, \"Verify that the reviewer's email address is never displayed with a review on the product page.\",\n  \"Risk: personal data could be shown publicly.\"),\n (\"AC-03\", None, \"Verify that the rating, Name and review text displayed match exactly what the customer submitted.\",\n  \"Edge case: 1-star review, very long review text.\"),\n (\"AC-03\", None, \"Verify that approved reviews are displayed in the agreed order and with the agreed number per page.\",\n  \"Missing info: sort order and paging (Q-11).\"),\n (\"AC-03\", None, \"Verify that the rating summary and review count on the product page are calculated from approved reviews only.\",\n  \"Missing info: whether a summary and count are shown, and the rounding of the average (Q-12).\\nRisk: pending or rejected reviews could change the shown rating.\"),\n (\"AC-03\", None, \"Verify that a message is shown in the reviews area when the product has no approved reviews.\",\n  \"Assumption: a short \\\"no reviews yet\\\" message is shown; wording not checked until Q-22 is answered.\\nEdge case: product with only pending reviews.\"),\n (\"AC-03\", None, \"Verify that the date of each displayed review is shown in the agreed format.\",\n  \"Assumption: any unambiguous date format is accepted until Q-21 is answered.\"),\n (\"AC-03\", None, \"Verify that an approved review is displayed only on the page of the product it was written for.\",\n  \"Risk: reviews shown on the wrong product would mislead customers.\"),\n\n (\"AC-GEN\", G_ACCESS, \"Verify that only customers who purchased the product can submit a review for it, and a non-buyer is blocked.\",\n  \"Missing info: whether a purchase check exists and what a non-buyer sees (Q-01).\\nRisk: fake reviews from non-buyers.\"),\n (\"AC-GEN\", G_ACCESS, \"Verify that the sign-in rule for submitting a review is applied (guest allowed or sign-in required).\",\n  \"Missing info: whether the customer must be signed in (Q-02).\"),\n (\"AC-GEN\", G_FORM, \"Verify that the form shows the fields \\\"Name *\\\" and \\\"Email *\\\", the checkbox, the Submit button and the text \\\"Your email address will not be published. Required fields are marked *\\\".\", \"\"),\n (\"AC-GEN\", G_FORM, \"Verify that the review cannot be submitted when Name is empty.\",\n  \"Assumption: validation happens on submit and the message names the field; wording not checked until Q-17 is answered.\"),\n (\"AC-GEN\", G_FORM, \"Verify that Name values outside the allowed length or characters, or made only of spaces, are rejected and valid values are accepted.\",\n  \"Missing info: Name length and allowed characters (Q-06).\\nEdge case: length at the maximum and maximum + 1, accented letters, spaces only.\"),\n (\"AC-GEN\", G_FORM, \"Verify that the review cannot be submitted when Email is empty.\",\n  \"Assumption: validation happens on submit and the message names the field; wording not checked until Q-17 is answered.\"),\n (\"AC-GEN\", G_FORM, \"Verify that an Email with an invalid format is rejected and an Email with a valid format is accepted.\",\n  \"Missing info: accepted email format and maximum length (Q-07).\\nEdge case: missing @, missing domain, length at the maximum.\"),\n (\"AC-GEN\", G_SUBMIT, \"Verify that a review with all required fields valid is submitted and a confirmation message is shown.\",\n  \"Missing info: whether the confirmation says the review awaits approval (Q-09).\\nAssumption: any clear confirmation is accepted; wording not checked until Q-18 is answered.\"),\n (\"AC-GEN\", G_SUBMIT, \"Verify that after a successful submit the form is cleared or keeps its values according to the agreed rule.\",\n  \"Missing info: form state after submit (Q-09).\"),\n (\"AC-GEN\", G_SUBMIT, \"Verify that when several required fields are missing or invalid, the review is not submitted and each problem field is identified.\",\n  \"Assumption: one message per missing or invalid field until Q-17 is answered.\\nEdge case: all fields empty.\"),\n (\"AC-GEN\", G_SAVE, \"Verify that the \\\"Save my name, email, and website in this browser for the next time I comment.\\\" checkbox is unticked by default.\", \"\"),\n (\"AC-GEN\", G_SAVE, \"Verify that when the checkbox is ticked, the saved Name and Email are pre-filled on the next visit in the same browser.\",\n  \"Missing info: what is saved, where and for how long (Q-15).\\nAssumption: Name and Email are pre-filled on the next visit until Q-15 is answered.\"),\n (\"AC-GEN\", G_SAVE, \"Verify that when the checkbox is left unticked, Name and Email are not remembered on the next visit.\",\n  \"Missing info: storage rule of the checkbox (Q-15).\\nRisk: personal data kept in a shared browser without consent.\"),\n (\"AC-GEN\", G_SAVE, \"Verify that the checkbox label and the data it saves match the fields present on the form.\",\n  \"Missing info: label mentions \\\"website\\\" but there is no Website field (Q-14).\"),\n (\"AC-GEN\", G_DUP, \"Verify that a customer cannot submit a second review for the same product unless the agreed rule allows it.\",\n  \"Missing info: whether more than one review per customer per product is allowed (Q-13).\"),\n (\"AC-GEN\", G_DUP, \"Verify that clicking Submit twice quickly creates only one review.\",\n  \"Assumption: only one review is created until Q-23 is answered.\\nEdge case: double click, Enter key pressed twice.\"),\n (\"AC-GEN\", G_DUP, \"Verify that when the review cannot be saved because of a server or network error, an error message is shown, no review is created and the entered values are kept.\",\n  \"Assumption: behaviour as described until Q-24 is answered.\\nRisk: the customer loses the written review.\"),\n]\n\nwb = openpyxl.load_workbook(out)\nws = wb[\"Test Requirements\"]\nalign = Alignment(wrap_text=True, vertical=\"top\")\nfor i, (ac, origin, tr, notes) in enumerate(rows, start=1):\n    r = i + 1\n    vals = [ac, origin if origin else AC[ac], f\"TR-{i:02d}\", tr, notes if notes else None]\n    for c, v in enumerate(vals, start=1):\n        cell = ws.cell(row=r, column=c, value=v)\n        cell.alignment = align\nwb.save(out)\n\n# self-checks\nassert all(t.startswith(\"Verify that \") for _, _, t, _ in rows)\nused = set()\nfor *_, n in rows:\n    used |= set(re.findall(r\"Missing info:.*?\\((Q-\\d+)\\)\", n))\nprint(\"TR count:\", len(rows))\nprint(\"ACs:\", sorted({r[0] for r in rows}))\nprint(\"Must ask linked via Missing info:\", sorted(used))\nprint(\"Missing Must ask links:\", [f\"Q-{i:02d}\" for i in range(1, 17) if f\"Q-{i:02d}\" not in used])\ntags = set()\nfor *_, n in rows:\n    for line in n.split(\"\\n\"):\n        if line: tags.add(line.split(\":\")[0])\nprint(\"Tags used:\", tags)\n"
}
```

## Tool (2026-10-21T04:32:28)

```
File created successfully at: C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\fill_trs.py (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:32:31)

**Tool call `Bash`:**

```json
{
  "command": "python \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/fill_trs.py\" skills/test-requirements-analysis/assets/test-requirement-template.xlsx runs/run-2/test-requirements.xlsx && python -c \"\nimport openpyxl\nws=openpyxl.load_workbook('runs/run-2/test-requirements.xlsx')['Test Requirements']\nprint(ws.title, ws.dimensions, ws.freeze_panes, [ (k,v.width) for k,v in ws.column_dimensions.items()], [c.value for c in ws[1]])\n\"; ls -la runs/run-2",
  "description": "Fill TR workbook from template and verify"
}
```

## Tool (2026-10-21T04:32:34)

```
TR count: 42
ACs: ['AC-01', 'AC-02', 'AC-03', 'AC-GEN']
Must ask linked via Missing info: ['Q-01', 'Q-02', 'Q-03', 'Q-04', 'Q-05', 'Q-06', 'Q-07', 'Q-08', 'Q-09', 'Q-10', 'Q-11', 'Q-12', 'Q-13', 'Q-14', 'Q-15', 'Q-16']
Missing Must ask links: []
Tags used: {'Edge case', 'Missing info', 'Assumption', 'Risk'}
Test Requirements A1:E43 A2 [('A', 10.0), ('B', 45.0), ('C', 10.0), ('D', 60.0), ('E', 50.0)] ['AC ID', 'Acceptance Criteria', 'TR ID', 'Test Requirements', 'Notes']
total 20
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 11:32 .
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 11:31 ..
-rw-r--r-- 1 vinh.the.nguyen 1049089 7392 Oct 21 11:31 clarification-questions.md
-rw-r--r-- 1 vinh.the.nguyen 1049089 9054 Oct 21 11:32 test-requirements.xlsx
```

## AI (2026-10-21T04:32:47)

I ran the test-requirements-analysis skill again on its own. I did not open runs/run-1. I read only the skill's own files, exam/user-story.md, the two mockups, and the knowledge files that knowledge/index.md lists for requirements analysis: product-review-rules.md, screens-and-fields.md and glossary.md. No product owner answers were used.

**Files written:**
- C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-2\clarification-questions.md
- C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-2\test-requirements.xlsx (copied from the skill's template; sheet name, header row and column widths are unchanged)

**Counts:**
- **Acceptance criteria:** 3, plus an AC-GEN group for requirements the story implies but no single criterion covers.
- **Test requirements:** 42 (TR-01 to TR-42).
  - AC-01 (star rating): 5
  - AC-02 (review text box): 9
  - AC-03 (approved reviews shown): 11
  - AC-GEN: 17
- **Questions:** 26 in total, 16 Must ask (Q-01 to Q-16) and 10 Nice to confirm (Q-17 to Q-26). One conflict between sources was recorded (Q-14).

**Must ask list:**
- Q-01: does the system check that the customer bought the product?
- Q-02: must the customer be signed in, or can a guest submit?
- Q-03: whole stars from 1 to 5, or half stars too?
- Q-04: minimum and maximum review length, and what happens at the limit.
- Q-05: is a review of only spaces treated as empty, and are spaces trimmed?
- Q-06: Name length and allowed characters.
- Q-07: Email format and maximum length.
- Q-08: who approves reviews, and can they be rejected?
- Q-09: after submitting, is the author told the review is pending, and is the form cleared?
- Q-10: which details each displayed review shows, with the email never shown.
- Q-11: order of reviews and how many per page.
- Q-12: average rating and review count, counted from approved reviews only?
- Q-13: can one customer post more than one review per product?
- Q-14: the checkbox label mentions "website" but the form has no Website field.
- Q-15: what the "save my details" checkbox stores, and for how long.
- Q-16: how HTML, links and offensive words in reviews are handled.

**Assumptions used (all tagged in the Notes column):**
- The rating is a whole number from 1 to 5 (Q-03).
- A review of only spaces counts as empty (Q-05).
- HTML or script in a review is never run on the page (Q-16).
- Each review shows rating, Name, date and text (Q-10).
- Validation happens on submit, and the exact message wording is not checked (Q-17).
- Any clear success message is accepted (Q-18).
- Clicking another star replaces the earlier choice (Q-19).
- All printable characters and line breaks are allowed (Q-20).
- Any clear date format is accepted (Q-21).
- A "no reviews yet" message appears when a product has none (Q-22).
- A double click on Submit creates only one review (Q-23).
- On a server or network error, a message is shown, nothing is saved and the entered values are kept (Q-24).
- Ticking the checkbox pre-fills Name and Email on the next visit (Q-15).
- Editing or deleting a review is out of scope (Q-25).
- Supported setup is latest desktop Chrome in English (Q-26).

**Coverage checks (all passed):**
- Every acceptance criterion has at least one test requirement.
- Every Must ask question is linked to at least one test requirement through a "Missing info" note.
- Only the four allowed note tags are used.
- Every test requirement starts with "Verify that".

mockup-2.png is only the company logo, so it added no requirements. The skill stops here and waits for your review before any test design.

## Tool (2026-10-21T04:32:48)

```
{"success":true,"message":"Report delivered to your caller."}
```
