# Transcript 02: test-condition-design (run1)

Exported from the agent session log. Kept verbatim: the trainee's messages, the AI's replies, tool calls and tool results. Left out: harness reminders and private thinking. The harness prefix in front of follow-up messages is removed; the AI's final report is shown as an AI reply.

## Trainee (2026-10-21T04:01:44)

hey, next step. use my test design skill: evaluator/test-fixtures/manual-qa-sim-pass/submission/skills/test-condition-design/SKILL.md (read it and follow it).

input TR list: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-requirements.xlsx
clarification questions (no PO answers yet): evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/clarification-questions.md
knowledge folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/knowledge
output folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1

only use these files + the exam folder (evaluator/test-fixtures/manual-qa-sim-pass/exam), nothing else under test-fixtures. tell me what you wrote when done.

## AI (2026-10-21T04:01:46)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\skills\\test-condition-design\\SKILL.md"
}
```

## Tool (2026-10-21T04:01:46)

```
1	---
2	name: test-condition-design
3	description: Use when a reviewed Test Requirement Excel list already exists and test conditions must be derived from it with a named test design technique (equivalence partitioning, boundary value analysis, decision table, state transition, error guessing) before test cases are written; writes test-design.md. Do NOT use on a raw user story, to write step-by-step test cases or to produce test data sets.
4	---
5	
6	# Test Condition Design
7	
8	Turns each Test Requirement (TR) into test conditions, each derived with a named technique, so that test cases can be written from them.
9	
10	## Inputs
11	
12	- {tr_file}: the reviewed Test Requirement list (.xlsx written by the test-requirements-analysis skill). Default: `{output_dir}/test-requirements.xlsx`. If it is missing, ask the user; do not rebuild it from the user story.
13	- {answers}: answers to the clarification questions received so far, if any (file or pasted text). If the user has none, continue and keep the related notes as Missing info or Assumption.
14	- {knowledge_dir}: the project's knowledge folder (fields, limits, states, glossary). If missing, ask the user.
15	- {output_dir}: the folder where the output file is written. If missing, ask the user.
16	
17	## Process
18	
19	1. Open {tr_file} and list every TR ID with its AC ID and Notes. Stop and ask the user if a TR row has no TR ID or no text.
20	2. Read {answers} and the knowledge files that the index in {knowledge_dir} lists for test design, and write down each input field, value range, state and business rule you will use, marked Confirmed (with source) or Assumption.
21	3. Select one or more techniques for each TR with `references/test-design-techniques.md`, and note why the technique fits.
22	4. Derive the test conditions for each TR with the selected technique: partitions, boundary values, decision table rules, state transitions or error guesses. Give each condition an ID `TCD-<TR number>-<nn>` (for example TCD-03-02) and mark it Positive or Negative.
23	5. Check the scenario types in `references/coverage-checklist.md` and add missing conditions, or list the type under "Not covered" with a reason.
24	6. Tag notes on each condition with the tags in `../test-requirements-analysis/references/note-tags.md`; every condition built on an unconfirmed value gets an Assumption or Missing info note.
25	7. Write `{output_dir}/test-design.md` from `assets/test-design-template.md`.
26	8. Verify that every TR ID has at least one condition, that every boundary value is exact (on, just below, just above), and that no condition repeats another.
27	9. Report to the user: conditions per TR, the techniques used, the Assumption list and the "Not covered" list; then stop and wait for the user's approval before test cases are written.
28	
29	## Exceptions
30	
31	- A value range or rule needed for BVA or a decision table is not in any source: do not invent it; write the condition with a Missing info note, or with an Assumption note if the user agrees to proceed.
32	- {answers} contradicts {tr_file} or the knowledge files: list the conflict in the report and ask which source is authoritative; do not pick one.
33	- The xlsx cannot be read: show the error and ask the user for a re-saved copy or a CSV export; do not retype it from memory.
34	
35	## Output
36	
37	- `{output_dir}/test-design.md`: per TR, the technique(s), the test conditions with IDs, Positive/Negative, notes; plus the "Not covered" list and the assumption list.
38	
39	## Files
40	
41	- `references/test-design-techniques.md`: open at Steps 3 and 4.
42	- `references/coverage-checklist.md`: open at Step 5.
43	- `../test-requirements-analysis/references/note-tags.md`: open at Step 6 (shared, single source).
44	- `assets/test-design-template.md`: open at Step 7; copy it, never rebuild it.
45	
```

## AI (2026-10-21T04:01:47)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && find submission exam -type f | head -100",
  "description": "List files in submission and exam folders"
}
```

## Tool (2026-10-21T04:01:48)

```
submission/knowledge/environment.md
submission/knowledge/glossary.md
submission/knowledge/index.md
submission/knowledge/product-review-rules.md
submission/knowledge/screens-and-fields.md
submission/review/review-log.md
submission/runs/run-1/ai-original/clarification-questions.md
submission/runs/run-1/ai-original/test-requirements.xlsx
submission/runs/run-1/clarification-questions.md
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
exam/app/app.js
exam/app/index.html
exam/app/styles.css
exam/app-note.md
exam/mockup-1.png
exam/mockup-2.png
exam/User Story for My Shop.docx
exam/user-story.md
```

## AI (2026-10-21T04:01:51)

**Tool call `Bash`:**

```json
{
  "command": "for f in skills/test-condition-design/references/test-design-techniques.md skills/test-condition-design/references/coverage-checklist.md skills/test-requirements-analysis/references/note-tags.md skills/test-condition-design/assets/test-design-template.md knowledge/index.md runs/run-1/clarification-questions.md; do echo \"=== $f\"; cat \"$f\"; done",
  "description": "Read skill references, template, knowledge index, clarification questions"
}
```

## Tool (2026-10-21T04:01:53)

```
=== skills/test-condition-design/references/test-design-techniques.md
# Test design techniques: when and how

| Technique | Use when the TR has... | How to derive conditions |
|---|---|---|
| Equivalence Partitioning (EP) | An input or output with groups of values treated the same way (valid / invalid types, formats, options) | List the valid partitions and each invalid partition separately. One condition per partition. Invalid partitions are tested one at a time. |
| Boundary Value Analysis (BVA) | A numeric range, a length limit, a count limit, a date range | For each boundary: the value on it, just below and just above (3-value BVA). For a length limit N: N-1, N, N+1 characters; for a minimum M: M-1, M, M+1. Also empty (0) when the field is required. |
| Decision table | Several conditions that together decide the outcome (for example several required fields, or role + state) | List conditions and outcomes, build the rules, collapse rules that give the same outcome only when it is safe. One condition per remaining rule. |
| State transition | An object that changes state (created, pending, approved, rejected, deleted...) or a screen flow | Draw states and events; cover every valid transition once and the important invalid transitions (event not allowed in a state). |
| Error guessing | Inputs or actions where experience shows defects often appear | Leading/trailing spaces, only spaces, special and non-Latin characters, HTML or script text, very long text, double click on submit, browser back/reload after submit, pasted text, data remembered between visits, count or average shown after a change. |

Rules:

- Name the technique on every condition.
- Use the values from the sources. If the source gives no value, the condition still exists but carries a Missing info or Assumption note.
- Do not test two invalid partitions in one condition: the result would not show which one was rejected.
=== skills/test-condition-design/references/coverage-checklist.md
# Scenario coverage checklist

For each type, either the design has at least one condition, or the type is listed under "Not covered" with a reason (not relevant, out of scope of the story, blocked by missing information, needs another environment).

| Type | Ask yourself |
|---|---|
| Positive | Is the main successful flow covered for every AC? |
| Negative | Is each way the action can be rejected covered? |
| Boundary | Is every limit (length, count, range) covered on, below and above? |
| Validation | Is every required field and format rule checked, with the message? |
| Error handling | What happens on failure (network, server, timeout, reload during action)? |
| Permissions | Who may and may not perform the action (signed out, other role, precondition not met)? |
| Integration | Does the result appear correctly in other places (lists, counts, summaries, other pages)? |
| UI | Labels, required markers, layout against the mockup, focus and keyboard use. |
| Compatibility | Which browsers and screen sizes are in scope? |
| Regression | Which existing behaviour on the same page must still work after the change? |
| Data and privacy | Is personal data stored, shown or hidden as expected? |

Priority of risk: data loss or exposure, security, main flow, payment or money values come first.
=== skills/test-requirements-analysis/references/note-tags.md
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
=== skills/test-condition-design/assets/test-design-template.md
# Test design: {story_id} {story_title}

Input: {tr_file} · Answers used: {answers or "none"} · Date: {date}

## Values and rules used

| Item | Value | Status (Confirmed / Assumption) | Source |
|---|---|---|---|
| | | | |

## Test conditions

### {TR ID}: {Test Requirement}

Technique(s): {technique} - {why it fits}

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-xx-01 | | | | |

## Coverage by scenario type

| Type | Covered by (condition IDs) |
|---|---|
| | |

## Not covered

| Type or area | Reason |
|---|---|
| | |

## Assumptions to confirm

| Condition ID | Assumption | Question ID |
|---|---|---|
| | | |
=== knowledge/index.md
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
=== runs/run-1/clarification-questions.md
# Clarification questions: US-VP02 Submit a Product Review

Sources reviewed: exam/user-story.md (text of "User Story for My Shop.docx"), exam/mockup-1.png, exam/mockup-2.png (company logo only, no screen content), knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md
Date: 2026-10-21

Acceptance criteria: AC-01 "Allow customers to enter a star rating"; AC-02 "Provide a text box for review comments"; AC-03 "Display approved reviews on the product page". AC-GEN = the story as a whole (not tied to one AC). No answers from the product owner have been received yet.

## Must ask

| Q ID | AC ID | Ambiguous point | Question | Why it matters |
|---|---|---|---|---|
| Q-01 | AC-GEN | Who may submit a review | The story says "a product I purchased". Must the customer be signed in to submit a review, and must the system check that they bought this product? If a guest or a customer who did not buy it opens the page, should the form be hidden, disabled, or rejected on Submit with a message? | Decides who can submit at all; without it, tests for guests and non-buyers have no Expected Result. Risk of fake reviews. |
| Q-02 | AC-GEN | Name and Email for a known customer (conflict) | mockup-1 asks the customer to type "Name *" and "Email *", while the story speaks of a customer who purchased the product and is therefore known to the shop. For a signed-in customer, should Name and Email be prefilled from the account, editable, or not shown at all? | Conflict between the story and the mockup; changes what is built. |
| Q-03 | AC-01 | Allowed rating values | Is the rating a whole number from 1 to 5 (one per star), or are half stars (for example 3.5) allowed? | Defines the valid values of "Your rating" and how the rating is displayed. |
| Q-04 | AC-02 | Length of "Your review" | What are the minimum and maximum number of characters for "Your review" (for example at least 1 and at most N), or is there no maximum? No source states a limit; the demo build shows a "0 / 500" counter, but that is observed behaviour, not a requirement. | Boundary tests need exact limits. |
| Q-05 | AC-GEN | Rules for "Name" | What are the maximum length and the allowed characters of "Name" (letters only, or also digits, spaces, hyphens, apostrophes, accented letters)? | Needed to decide which Name values are accepted or rejected. |
| Q-06 | AC-GEN | Email format rule | Which rule decides a valid "Email": a standard format check (text@domain.tld), or a different rule? Is there a maximum length? | Needed to decide which Email values are accepted or rejected. |
| Q-07 | AC-03 | Moderation workflow | Who approves reviews (which role), can that person also reject a review, and what happens to a rejected review (deleted, or kept hidden)? | Defines the states of a review and what "approved" in AC-03 means. |
| Q-08 | AC-03 | Author's view of a pending review | Right after Submit, should the author see their own review on the product page marked as awaiting approval, or should it be hidden from everyone, the author included, until it is approved? | Expected Result of the step right after Submit. |
| Q-09 | AC-03 | Details shown per review | Which details are shown for each approved review: star rating, reviewer name (full name, first name only or initials), date, review text? There is no mockup of the reviews list. | Display tests, and privacy of the reviewer's name. |
| Q-10 | AC-03 | Order of reviews | In which order are approved reviews listed: newest first, oldest first, highest rating first, or another order? | A test of the list order has no Expected Result without it. |
| Q-11 | AC-03 | Rating summary and review count | Should the product page show an average rating and the number of reviews? If yes, is it calculated from approved reviews only, and how is the average rounded (for example one decimal, or nearest half star)? | A calculation with no defined result; pending or rejected reviews must not change the score shown. |
| Q-12 | AC-GEN | Reviews per customer and product | Can one customer submit more than one review for the same product, or only one? If only one, what should happen on a second attempt? | Business rule (uniqueness) that changes what is built. |
| Q-13 | AC-GEN | "website" in the save checkbox (conflict) | The checkbox reads "Save my name, email, and website in this browser for the next time I comment." but mockup-1 has no Website field. Should a Website field be added, or should the text drop "website"? | Conflict inside mockup-1; changes what is built. |
| Q-14 | AC-GEN | What the save checkbox stores | When the checkbox is ticked, which data is saved in the browser (name, email, anything else), for how long, and how can the customer remove it? Is anything saved when it is not ticked? | Privacy of personal data stored on the device. |
| Q-15 | AC-02 | HTML, scripts and links in text | If "Your review" or "Name" contains HTML tags, script code or web links, should they be shown as plain text, removed, or should the review be rejected? | Security risk (script injection) and display of every review. |

## Nice to confirm

| Q ID | AC ID | Ambiguous point | Question | Assumption used until answered |
|---|---|---|---|---|
| Q-16 | AC-01 | Changing the rating | Can the customer change the selected rating by clicking another star before Submit, and can they clear it again? | Clicking another star changes the rating; the rating cannot be cleared back to "no rating" except by reloading the page. |
| Q-17 | AC-02 | Spaces in text fields | Should leading and trailing spaces in "Your review", "Name" and "Email" be removed, and is a field with only spaces treated as empty? | Spaces are trimmed; a field with only spaces counts as empty and is rejected. |
| Q-18 | AC-02 | Text longer than the maximum | If there is a maximum length, should extra characters be blocked while typing or pasting, or accepted in the box and rejected on Submit with a message? | Typing and pasting stop at the maximum. |
| Q-19 | AC-GEN | When fields are validated | Are fields checked on Submit only, or also when the customer leaves a field? | Checked on Submit only. |
| Q-20 | AC-GEN | Error message wording and position | What is the wording and position of error messages: one message next to each field, or one summary above the form? | Each error names the field concerned; wording is checked for meaning, not exact text. |
| Q-21 | AC-GEN | Success message | What message is shown after a successful submit? For example, that the review was received and will be shown after approval. | A confirmation says the review was received and waits for approval. |
| Q-22 | AC-GEN | Form after submit | After a successful submit, is the form cleared, and does the customer stay on the same product page? | The customer stays on the product page and the form is cleared (Name and Email stay filled only if the save checkbox was ticked). |
| Q-23 | AC-03 | Number of reviews shown | Are all approved reviews shown at once, or a fixed number per page with paging or "Load more"? If so, how many per page? | All approved reviews are shown on one page. |
| Q-24 | AC-03 | Date shown with a review | Which date is shown (submit date or approval date) and in which format (for example 21/10/2026 or October 21, 2026)? | Submit date, in any unambiguous format; the format is not checked. |
| Q-25 | AC-03 | Product with no approved reviews | What should the reviews section show when a product has no approved reviews: a message saying there are no reviews yet, or no section at all? | A short message saying there are no reviews yet. |
| Q-26 | AC-03 | Telling the author the result | Is the author told (for example by email) when their review is approved or rejected? | No notification; out of scope of this story. |
| Q-27 | AC-GEN | Edit or delete own review | Is editing or deleting one's own review in the scope of US-VP02? | Out of scope. |
| Q-28 | AC-GEN | Double submit | If Submit is clicked twice quickly, should only one review be created? | Only one review is created. |
| Q-29 | AC-GEN | Server or network error | What should the customer see if the review cannot be saved (server or network error, session expired)? | A message says the review was not submitted, and the entered data is kept. |
| Q-30 | AC-GEN | Offensive language | Is offensive language filtered automatically, or left to the moderator? | Left to the moderator; no automatic filter. |
| Q-31 | AC-GEN | Browsers, devices and language | Which browsers and devices must be supported (desktop Chrome only, or also other browsers and mobile), and in which language is the page? | Desktop Chrome, English. |
| Q-32 | AC-GEN | Heading text | mockup-1 shows the heading "ADD A REVIEW" in capitals. Are capitals required, or is it only a style (so "Add a review" is also correct)? | The heading text is compared without regard to letter case. |

## Conflicts between sources

| Q ID | Source A says | Source B says |
|---|---|---|
| Q-02 | exam/user-story.md: "As a customer, I want to submit a review for a product I purchased" (the reviewer is a known buyer) | exam/mockup-1.png: the form asks the reviewer to type "Name *" and "Email *" by hand, as for a guest |
| Q-13 | exam/mockup-1.png, checkbox: "Save my name, email, and website in this browser for the next time I comment." | exam/mockup-1.png, form: only "Your rating *", "Your review *", "Name *" and "Email *"; there is no Website field |
```

## AI (2026-10-21T04:01:56)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && for f in submission/knowledge/product-review-rules.md submission/knowledge/screens-and-fields.md submission/knowledge/glossary.md submission/knowledge/environment.md exam/user-story.md exam/app-note.md; do echo \"=== $f\"; cat \"$f\"; done",
  "description": "Read knowledge files and exam story"
}
```

## AI (2026-10-21T04:01:57)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1 && python -I -c \"\nimport openpyxl\nwb=openpyxl.load_workbook('test-requirements.xlsx')\nfor ws in wb:\n  print('###',ws.title,ws.dimensions)\n  for r in ws.iter_rows(values_only=True):\n    if any(c is not None for c in r): print(r)\n\"",
  "description": "Dump test requirements xlsx contents"
}
```

## Tool (2026-10-21T04:01:59)

```
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
=== exam/user-story.md
# Exam: Submit a Product Review (text of the Word file)

Application name: My Shop
US-VP02: Submit a Product Review
As a customer, I want to submit a review for a product I purchased, so that I can share my experience with others.
Acceptance Criteria:
- Allow customers to enter a star rating
- Provide a text box for review comments
- Display approved reviews on the product page

The Word file also holds two mockup images, saved here as `mockup-1.png` and `mockup-2.png`.
=== exam/app-note.md
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

## Tool (2026-10-21T04:02:00)

```
### Test Requirements A1:E42
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
```

## AI (2026-10-21T04:04:48)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\exam\\mockup-1.png"
}
```

## Tool (2026-10-21T04:04:48)

```
[image]
```

## AI (2026-10-21T04:04:51)

Now I'll write the test design file.

## AI (2026-10-21T04:07:37)

**Tool call `Write`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\runs\\run-1\\test-design.md",
  "content": "# Test design: US-VP02 Submit a Product Review\n\nInput: runs/run-1/test-requirements.xlsx (41 TRs, TR-01 to TR-41) · Answers used: none (runs/run-1/clarification-questions.md has questions Q-01 to Q-32, no product owner answers yet) · Date: 2026-10-21\n\nOther sources read: knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md, knowledge/environment.md, exam/user-story.md, exam/mockup-1.png, exam/app-note.md. The demo build (exam/app/) is the product under test and is never used as a source of expected results; its \"0 / 500\" counter and its message texts are Observed only and are not used as values here.\n\n## Values and rules used\n\n| Item | Value | Status (Confirmed / Assumption) | Source |\n|---|---|---|---|\n| Form fields | \"Your rating *\", \"Your review *\", \"Name *\", \"Email *\", save checkbox, \"Submit\" | Confirmed | mockup-1.png (R1), screens-and-fields.md F1-F6 |\n| Required fields | Rating, Review, Name and Email are required (marked *) | Confirmed | mockup-1.png (R2) |\n| Info text | \"Your email address will not be published. Required fields are marked *\" | Confirmed | mockup-1.png |\n| Heading | \"ADD A REVIEW\"; letter case not significant | Assumption | mockup-1.png; Q-32 |\n| Number of stars | 5 star icons, none selected when the form opens | Confirmed | mockup-1.png (R6) |\n| Rating values | Whole number 1 to 5, one per star; no half stars | Assumption | product-review-rules.md A1; Q-03 |\n| Changing the rating | Clicking another star changes the rating; it cannot be cleared to \"no rating\" except by reloading the page | Assumption | Q-16 |\n| \"Your review\" control | Multi-line text box | Confirmed | mockup-1.png (AC-02, F2) |\n| \"Your review\" minimum and maximum length | Not stated in any source; no value used | Missing info | Q-04 (demo counter \"0 / 500\" is Observed only) |\n| Text longer than the maximum | Typing and pasting stop at the maximum | Assumption | Q-18 |\n| Leading / trailing spaces | Trimmed in Review, Name and Email; a field of only spaces counts as empty | Assumption | Q-17 |\n| Name length and allowed characters | Not stated; no value used | Missing info | Q-05 |\n| Email format rule and maximum length | Standard format text@domain.tld taken as the working rule; maximum length not stated | Assumption (format), Missing info (length) | Q-06 |\n| Email not published | The email is never shown on the product page | Confirmed | mockup-1.png (R3) |\n| HTML, scripts and links in text | Shown as plain text, removed or rejected: not stated. Never executed in any case | Missing info (handling), Assumption (never executed) | Q-15 |\n| Validation timing | Fields are checked on Submit only | Assumption | Q-19 |\n| Error messages | Each error names the field concerned; wording checked for meaning, not exact text | Assumption | Q-20 |\n| Success message | Says the review was received and waits for approval | Assumption | Q-21 |\n| Form after success | Customer stays on the product page; form cleared; Name and Email stay only if the save checkbox was ticked | Assumption | Q-22 |\n| Review states | Submitted review is Pending; only Approved reviews are displayed | Confirmed | AC-03 (R4, R5), app-note.md |\n| Moderation (who approves, reject, what happens to a rejected review) | Not stated | Missing info | Q-07 |\n| Moderator in demo-1.0 | \"Moderator: approve pending reviews\" approves every pending review; used only as a test helper | Confirmed (helper), Assumption (not part of the feature) | environment.md, app-note.md |\n| Author's view of own pending review | Not stated | Missing info | Q-08 |\n| Details per displayed review | Star rating, reviewer name, date, review text; never the email | Assumption | product-review-rules.md A2; Q-09 |\n| Date shown | Submit date, any unambiguous format | Assumption | Q-24 |\n| Order of reviews | Not stated | Missing info | Q-10 |\n| Paging | All approved reviews shown on one page | Assumption | Q-23 |\n| No approved reviews | A short message saying there are no reviews yet | Assumption | Q-25 |\n| Rating summary and count | Whether shown and how rounded: not stated; if shown, approved reviews only | Missing info | Q-11 |\n| Who may review | Sign-in and purchase check not stated | Missing info | Q-01 |\n| Name / Email for a signed-in customer | Story vs mockup-1 conflict | Missing info | Q-02 |\n| Reviews per customer and product | Not stated | Missing info | Q-12 |\n| Save checkbox default | Unchecked | Confirmed | mockup-1.png (F5) |\n| Save checkbox stores | Name and Email only, in this browser | Assumption | Q-13, Q-14 |\n| What is kept when the checkbox is not ticked, how long data is kept, how it is removed | Not stated | Missing info | Q-14 |\n| Double submit | Only one review is created | Assumption | Q-28 |\n| Server / network error | A message says the review was not submitted; the entered data is kept | Assumption | Q-29 |\n| Browser and environment | Build demo-1.0, Chrome; other browsers and devices not stated | Confirmed (Chrome), Assumption (desktop Chrome, English) | environment.md, app-note.md; Q-31 |\n| Demo-1.0 data | One product; reload restores the initial data; no sign-in | Confirmed | app-note.md, environment.md |\n\n## Test conditions\n\n### TR-01: Verify that the \"Your rating *\" field shows 5 stars.\n\nTechnique(s): Equivalence Partitioning - the rating control has one valid display state (as in mockup-1); one condition covers it.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-01-01 | EP | When the form opens, \"Your rating *\" shows exactly 5 star icons and none of them is selected. | Positive | |\n\n### TR-02: Verify that the customer can select a rating by clicking a star, and the selected stars are shown as selected.\n\nTechnique(s): Equivalence Partitioning - whole-star values 1 to 5 form one valid partition (a middle value represents it; the ends are in TR-03) and half-star values form one invalid partition. Error guessing - hover and keyboard use are common sources of rating defects.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-02-01 | EP | From no rating, clicking the 3rd star selects rating 3: stars 1 to 3 are shown as selected and stars 4 and 5 as not selected. | Positive | Assumption: the rating is a whole number from 1 to 5 until Q-03 is answered. |\n| TCD-02-02 | EP | Clicking on the left half of a star does not set a half-star value (for example 2.5); the rating shown and saved is a whole number. | Negative | Missing info: whether half stars are allowed (Q-03). |\n| TCD-02-03 | Error guessing | Moving the pointer over the stars without clicking, then moving it away, leaves the selected rating unchanged. | Negative | Assumption: a hover preview, if any, is not kept; no question raised yet, to be added to Q-16. |\n| TCD-02-04 | Error guessing | The rating can be selected with the keyboard only (Tab to the stars, then arrow keys, Space or Enter), and the selection is shown. | Positive | Missing info: keyboard use is not stated in any source; new question needed. |\n\n### TR-03: Verify that both the lowest rating (1 star) and the highest rating (5 stars) can be selected and are saved with the review.\n\nTechnique(s): Boundary Value Analysis - the rating is a range 1 to 5 (Assumption). Just below the minimum (0 = no rating) is TCD-05-01; just above the maximum (6) cannot be entered because only 5 stars exist (TCD-01-01), so no separate condition.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-03-01 | BVA | Rating 1 (on the minimum): the review is submitted and, after approval, is shown with 1 star. | Positive | Edge case: value exactly at the minimum.<br>Assumption: rating range 1 to 5 until Q-03 is answered. |\n| TCD-03-02 | BVA | Rating 2 (just above the minimum): the review is submitted and, after approval, is shown with 2 stars. | Positive | Assumption: rating range 1 to 5 until Q-03 is answered. |\n| TCD-03-03 | BVA | Rating 4 (just below the maximum): the review is submitted and, after approval, is shown with 4 stars. | Positive | Assumption: rating range 1 to 5 until Q-03 is answered. |\n| TCD-03-04 | BVA | Rating 5 (on the maximum): the review is submitted and, after approval, is shown with 5 stars. | Positive | Edge case: value exactly at the maximum.<br>Assumption: rating range 1 to 5 until Q-03 is answered. |\n\n### TR-04: Verify that the customer can change the selected rating before submitting, and only the last selected rating is saved.\n\nTechnique(s): State transition - states \"No rating\" and \"Rating n\"; events \"click star m\", \"click the selected star again\", \"reload page\", \"Submit\". Each valid transition once, plus the transition that is not allowed (clearing to \"No rating\" by clicking).\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-04-01 | State transition | Rating 2, click the 5th star: the rating becomes 5 and stars 1 to 5 are shown as selected (increase). | Positive | Assumption: clicking another star changes the rating (Q-16). |\n| TCD-04-02 | State transition | Rating 5, click the 2nd star: the rating becomes 2 and only stars 1 and 2 are shown as selected (decrease). | Positive | Assumption: clicking another star changes the rating (Q-16). |\n| TCD-04-03 | State transition | Rating 3, click the 3rd star again: the rating stays 3; it does not go back to \"No rating\". | Negative | Assumption: the rating cannot be cleared by clicking (Q-16). |\n| TCD-04-04 | State transition | Rating 3, reload the page: the form opens with \"No rating\". | Positive | Assumption: reloading is the only way back to \"No rating\" (Q-16). |\n| TCD-04-05 | State transition | Rating changed several times (1, then 4, then 2, then 3) and then Submit: the saved and, after approval, displayed rating is 3. | Positive | |\n\n### TR-05: Verify that the review cannot be submitted when no star rating is selected.\n\nTechnique(s): Equivalence Partitioning (invalid partition \"no rating\") with Boundary Value Analysis (0 is just below the minimum 1).\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-05-01 | EP / BVA | No star selected (0, just below the minimum), Review, Name and Email valid, Submit: the review is not submitted and an error names the rating field. | Negative | Edge case: just below the minimum.<br>Assumption: the error names the rating field; wording checked for meaning, not exact text (Q-20). |\n\n### TR-06: Verify that a multi-line text box \"Your review *\" is provided for the review comment.\n\nTechnique(s): Equivalence Partitioning - multi-line input is one valid partition. Error guessing - line breaks are often lost when the text is displayed.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-06-01 | EP | \"Your review *\" accepts text on several lines: pressing Enter starts a new line inside the box and does not submit the form. | Positive | |\n| TCD-06-02 | Error guessing | A review written on several lines is shown on the product page, after approval, with its line breaks kept. | Positive | Missing info: display of line breaks is not stated in any source; new question needed. |\n\n### TR-07: Verify that the review cannot be submitted when \"Your review\" is empty.\n\nTechnique(s): Equivalence Partitioning - \"empty\" is the invalid partition of a required field (0 characters).\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-07-01 | EP | \"Your review\" empty (0 characters), rating, Name and Email valid, Submit: the review is not submitted and an error names \"Your review\". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |\n\n### TR-08: Verify that review text within the allowed length is accepted and saved as entered.\n\nTechnique(s): Equivalence Partitioning - one valid length partition (between the minimum and the maximum) and valid character types. Error guessing - pasted text and non-Latin characters are frequent defect sources.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-08-01 | EP | Review text with a length between the minimum and the maximum: the review is submitted and, after approval, the text is shown exactly as entered. | Positive | Missing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered. |\n| TCD-08-02 | Error guessing | Review text with accented letters (é, ü), non-Latin letters (日本語), digits, punctuation and an emoji: accepted and shown unchanged. | Positive | Assumption: no character restriction in \"Your review\"; no source restricts it, to be added to Q-15. |\n| TCD-08-03 | Error guessing | Review text pasted from the clipboard is accepted and saved in the same way as typed text. | Positive | |\n\n### TR-09: Verify that review text of exactly the minimum length and exactly the maximum length is accepted.\n\nTechnique(s): Boundary Value Analysis - the review has a length range (minimum and maximum). Values on and just inside each boundary are here; just outside are in TR-10. The exact numbers are not in any source.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-09-01 | BVA | Review length = minimum: accepted. | Positive | Edge case: value exactly at the minimum.<br>Missing info: minimum length not stated (Q-04). |\n| TCD-09-02 | BVA | Review length = minimum + 1: accepted. | Positive | Missing info: minimum length not stated (Q-04). |\n| TCD-09-03 | BVA | Review length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-04). |\n| TCD-09-04 | BVA | Review length = maximum: accepted and, after approval, shown in full (not cut). | Positive | Edge case: value exactly at the maximum.<br>Missing info: maximum length not stated (Q-04). |\n\n### TR-10: Verify that review text shorter than the minimum or longer than the maximum is not accepted.\n\nTechnique(s): Boundary Value Analysis - values just outside each boundary, one invalid value per condition. Error guessing - very long pasted text.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-10-01 | BVA | Review length = minimum - 1, Submit: the review is not submitted and an error names \"Your review\". | Negative | Edge case: one character below the minimum.<br>Missing info: minimum length not stated (Q-04). If the minimum is 1, this is TCD-07-01 and is not repeated. |\n| TCD-10-02 | BVA | Typing maximum + 1 characters: typing stops at the maximum and the box holds exactly maximum characters. | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: typing stops at the maximum (Q-18). |\n| TCD-10-03 | BVA | Pasting text of maximum + 1 characters: the text in the box is cut at the maximum. | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |\n| TCD-10-04 | Error guessing | Pasting very long text (about ten times the maximum): the box holds at most the maximum and the page stays responsive. | Negative | Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |\n\n### TR-11: Verify that review text made only of spaces is treated as empty and the review is not submitted.\n\nTechnique(s): Error guessing - spaces-only and space-padded input; Boundary Value Analysis - trimmed length just below the minimum.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-11-01 | Error guessing | \"Your review\" contains only spaces, Submit: the review is not submitted and an error names \"Your review\". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |\n| TCD-11-02 | Error guessing | \"Your review\" contains only line breaks (Enter pressed several times), Submit: the review is not submitted and an error names \"Your review\". | Negative | Edge case: whitespace-only input.<br>Assumption: line breaks are treated like spaces (Q-17). |\n| TCD-11-03 | Error guessing | Valid review text with leading and trailing spaces: accepted and, after approval, shown without the leading and trailing spaces. | Positive | Assumption: spaces are trimmed (Q-17). |\n| TCD-11-04 | BVA | Review of (minimum - 1) visible characters plus one trailing space (length = minimum only if the space is counted), Submit: the review is not submitted. | Negative | Edge case: length reaches the minimum only through a space.<br>Assumption: length is counted after trimming (Q-17).<br>Missing info: minimum length not stated (Q-04). |\n\n### TR-12: Verify that HTML tags, script code and links entered in \"Your review\" or \"Name\" are never run as code on the product page.\n\nTechnique(s): Error guessing - script injection through free text is a known high-risk defect; each field and each injection form is tested separately so the result shows which one failed.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-12-01 | Error guessing | \"Your review\" contains `<script>alert(1)</script>`: no script runs, on submit or on the product page after approval. | Negative | Missing info: shown as plain text, removed or rejected (Q-15).<br>Assumption: content is never executed (Q-15).<br>Risk: script injection would affect every visitor of the product page. |\n| TCD-12-02 | Error guessing | \"Your review\" contains `<img src=x onerror=alert(1)>`: no script runs and no image element is added to the page. | Negative | Missing info: handling not stated (Q-15).<br>Risk: script injection through an HTML attribute. |\n| TCD-12-03 | Error guessing | \"Your review\" contains harmless HTML `<b>bold</b>`: the text is not rendered as bold HTML; it is shown as plain text, removed or rejected as confirmed for Q-15. | Negative | Missing info: handling not stated (Q-15). |\n| TCD-12-04 | Error guessing | \"Your review\" contains a web link (`https://example.com`): it is shown, removed or rejected as confirmed for Q-15, and is not turned into a clickable link unless Q-15 allows it. | Negative | Missing info: handling of links not stated (Q-15). |\n| TCD-12-05 | Error guessing | \"Name\" contains `<script>alert(1)</script>`: no script runs where the name is shown. | Negative | Missing info: handling not stated (Q-05, Q-15).<br>Risk: script injection through the reviewer name. |\n\n### TR-13: Verify that a newly submitted review is not displayed on the product page while it waits for approval.\n\nTechnique(s): State transition - Submit moves a review from \"not existing\" to \"Pending\"; in \"Pending\" the review must not be displayed to other visitors. (The author's own view is TR-16.)\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-13-01 | State transition | After a valid Submit (state Pending), the review does not appear in the reviews list for another visitor of the product page. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: demo-1.0 has no sign-in and keeps data only in the open page, so \"another visitor\" cannot be simulated there (environment.md); check in the author's page per TCD-16-01. |\n| TCD-13-02 | State transition | A pending review is still not displayed after the product page is opened again later. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: in demo-1.0 a reload restores the initial data (environment.md), so this needs a build that keeps data. |\n\n### TR-14: Verify that a submitted review is displayed on the product page after it is approved.\n\nTechnique(s): State transition - event \"approve\" moves Pending to Approved (valid transition); approving again or with nothing pending must not create entries (invalid transitions).\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-14-01 | State transition | Pending review, moderator approves: the review appears in the reviews list on the product page. | Positive | Missing info: who approves and how (Q-07).<br>Assumption: in demo-1.0 the \"Moderator: approve pending reviews\" helper plays the moderator (environment.md). |\n| TCD-14-02 | State transition | Approved review, approve action used again: the review is shown once only (no duplicate). | Negative | Edge case: approve twice.<br>Missing info: moderation workflow (Q-07). |\n| TCD-14-03 | State transition | No pending review, approve action used: no new or empty review appears. | Negative | Edge case: approve with nothing pending.<br>Missing info: moderation workflow (Q-07). |\n\n### TR-15: Verify that a rejected review is never displayed on the product page.\n\nTechnique(s): State transition - event \"reject\" moves Pending to Rejected; Rejected must never lead to \"displayed\" through other events.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-15-01 | State transition | Pending review, moderator rejects: the review does not appear on the product page. | Positive | Missing info: whether a review can be rejected and what happens to it (Q-07). Demo-1.0 has no reject action (environment.md). |\n| TCD-15-02 | State transition | Rejected review, then other pending reviews are approved: the rejected review is still not displayed. | Negative | Missing info: moderation workflow (Q-07).<br>Risk: rejected content shown publicly. |\n\n### TR-16: Verify that the author sees their own pending review only in the way confirmed for Q-08 (marked as awaiting approval, or not at all).\n\nTechnique(s): Decision table - conditions \"viewer = author / other visitor\" and \"state = Pending / Approved\". Rule other + Pending is TCD-13-01; rule other + Approved is TCD-14-01; the two author rules are below.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-16-01 | Decision table | Rule: viewer = author, state = Pending: the author sees the review marked as awaiting approval, or does not see it, as confirmed for Q-08. | Positive | Missing info: author's view of a pending review not specified (Q-08). |\n| TCD-16-02 | Decision table | Rule: viewer = author, state = Approved: the author sees the review like any other approved review, with no \"awaiting approval\" mark. | Positive | Missing info: whether a pending mark exists (Q-08). |\n\n### TR-17: Verify that each displayed review shows the confirmed details (star rating, reviewer name, date, review text).\n\nTechnique(s): Equivalence Partitioning - every approved review belongs to one partition and must show the same set of details; one condition per detail group whose rule differs.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-17-01 | EP | Each approved review shows its star rating, reviewer name, date and review text. | Positive | Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered. |\n| TCD-17-02 | EP | The date shown with a review is the submit date, in an unambiguous format. | Positive | Assumption: submit date in any unambiguous format (Q-24). |\n| TCD-17-03 | EP | The reviewer name is shown in the confirmed form (full name, first name only or initials). | Positive | Missing info: form of the name not specified (Q-09).<br>Risk: privacy of the reviewer's name. |\n\n### TR-18: Verify that the star rating, name and review text of a displayed review match what the customer submitted.\n\nTechnique(s): Equivalence Partitioning - several reviews with different values must keep their own values. Error guessing - special characters are often encoded wrongly and long words often break the layout.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-18-01 | EP | Two reviews submitted one after the other with different rating, name and text: after approval each shows its own rating, name and text (no mix-up). | Positive | |\n| TCD-18-02 | Error guessing | Name with accented letter, apostrophe and hyphen (for example \"Zoë O'Brien-Lê\"): shown exactly as entered, with no encoded characters such as `&#39;`. | Positive | Assumption: such names are accepted until Q-05 is answered. |\n| TCD-18-03 | Error guessing | Review text with the characters `& < > \" '` used as plain text (for example \"5 > 3 & good\"): shown exactly as entered, not as `&amp;` or `&gt;`. | Positive | Missing info: handling of HTML-like text (Q-15). |\n| TCD-18-04 | Error guessing | Review of maximum length made of one long word with no spaces: shown in full without breaking the page layout. | Positive | Missing info: maximum length not stated (Q-04). |\n\n### TR-19: Verify that the reviewer's email address is never displayed on the product page.\n\nTechnique(s): Error guessing - personal data often leaks through hidden places (tooltips, links, page source) as well as visible text.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-19-01 | Error guessing | After approval, the email entered does not appear anywhere in the visible product page (reviews list, reviewer name, rating summary). | Positive | Risk: personal data could be shown publicly. |\n| TCD-19-02 | Error guessing | After approval, the email is not in hidden parts of the review: no tooltip, no \"mailto\" link on the name, not in the page source of the review. | Positive | Risk: personal data could be read by anyone viewing the page source. |\n\n### TR-20: Verify that approved reviews are listed in the confirmed order.\n\nTechnique(s): Equivalence Partitioning - one partition \"list of approved reviews with different dates and ratings\". Error guessing - newly approved reviews and ties are common ordering defects.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-20-01 | EP | At least 3 approved reviews with different dates and ratings are listed in the confirmed order. | Positive | Missing info: list order not specified (Q-10). |\n| TCD-20-02 | Error guessing | A review approved after the existing ones appears in the position the confirmed order requires. | Positive | Missing info: list order not specified (Q-10). |\n| TCD-20-03 | Error guessing | Two approved reviews with the same date and the same rating keep a stable order when the page is opened again. | Positive | Edge case: tie in the sort key.<br>Missing info: list order not specified (Q-10). |\n\n### TR-21: Verify that all approved reviews can be seen when a product has many reviews.\n\nTechnique(s): Equivalence Partitioning - \"many reviews\" partition. Boundary Value Analysis - page size, only if paging is confirmed.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-21-01 | EP | Product with a large number of approved reviews (for example 50): every approved review can be seen. | Positive | Edge case: large number of approved reviews.<br>Assumption: all approved reviews are shown on one page (Q-23). |\n| TCD-21-02 | BVA | Approved reviews = page size - 1: all are on the first page and no paging control is shown. | Positive | Missing info: whether paging exists and the page size (Q-23). |\n| TCD-21-03 | BVA | Approved reviews = page size: all are on the first page and no paging control is shown. | Positive | Edge case: count exactly at the page size.<br>Missing info: page size (Q-23). |\n| TCD-21-04 | BVA | Approved reviews = page size + 1: the last review is reachable through the paging control or \"Load more\". | Positive | Edge case: one above the page size.<br>Missing info: page size (Q-23). |\n\n### TR-22: Verify that a clear empty state is shown when the product has no approved reviews.\n\nTechnique(s): Boundary Value Analysis - approved review count 0 and the move from 0 to 1; Equivalence Partitioning - \"only pending reviews\" is part of the 0-approved partition.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-22-01 | BVA | 0 approved reviews: a short message says there are no reviews yet. | Positive | Edge case: product with no approved reviews.<br>Assumption: a short message saying there are no reviews yet (Q-25).<br>Missing info: demo-1.0 has one product that starts with approved reviews (app-note.md); a product with 0 approved reviews may not be available. |\n| TCD-22-02 | EP | 0 approved reviews and 1 or more pending reviews: the empty-state message is still shown. | Positive | Edge case: only pending reviews.<br>Assumption: empty-state message (Q-25). |\n| TCD-22-03 | BVA | From 0 to 1 approved review: the empty-state message disappears and the review is shown. | Positive | Assumption: empty-state message (Q-25). |\n\n### TR-23: Verify that the average rating and review count on the product page, if shown, are calculated from approved reviews only.\n\nTechnique(s): Decision table - condition \"state of the new review = Approved / Pending / Rejected\", outcome \"included in average and count: yes / no\". Boundary Value Analysis - rounding boundary and zero reviews.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-23-01 | Decision table | Rule: new review Approved: the average rating and the review count include it. | Positive | Missing info: whether a summary is shown and how it is rounded (Q-11). |\n| TCD-23-02 | Decision table | Rule: new review Pending: the average rating and the review count do not change. | Positive | Missing info: Q-11.<br>Risk: pending reviews could change the score shown to shoppers. |\n| TCD-23-03 | Decision table | Rule: new review Rejected: the average rating and the review count do not change. | Positive | Missing info: Q-07, Q-11.<br>Risk: rejected reviews could change the score shown to shoppers. |\n| TCD-23-04 | EP | The review count shown equals the number of approved reviews listed. | Positive | Missing info: whether a count is shown (Q-11). |\n| TCD-23-05 | BVA | Ratings whose exact average falls on and next to the rounding step (for example 4 and 5 = 4.5; 4, 4 and 5 = 4.33...) are shown with the confirmed rounding. | Positive | Missing info: rounding rule not stated (Q-11); exact boundary values are set when Q-11 is answered. |\n| TCD-23-06 | Error guessing | 0 approved reviews: the summary shows no average, or an empty state, and never a wrong value such as \"NaN\" or \"0 stars\". | Negative | Edge case: no approved reviews.<br>Missing info: Q-11, Q-25. |\n\n### TR-24: Verify that a review is displayed only on the page of the product it was written for.\n\nTechnique(s): Equivalence Partitioning - partitions \"page of the reviewed product\" and \"page of another product\".\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-24-01 | EP | A review written and approved for product A appears on the page of product A. | Positive | Covered in demo-1.0 by TCD-14-01 (one product only). |\n| TCD-24-02 | EP | The same review does not appear on the page of product B. | Negative | Risk: reviews shown on the wrong product mislead shoppers.<br>Missing info: demo-1.0 has one product only (app-note.md); needs a build with two products. |\n\n### TR-25: Verify that the review form shows the heading, the info text, the fields, the save checkbox and the \"Submit\" button as in mockup-1.\n\nTechnique(s): Equivalence Partitioning - the form has one valid display state (mockup-1); one condition per element group. Error guessing - focus order and keyboard use.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-25-01 | EP | The heading reads \"ADD A REVIEW\". | Positive | Assumption: compared without regard to letter case (Q-32). |\n| TCD-25-02 | EP | The info text reads \"Your email address will not be published. Required fields are marked *\". | Positive | |\n| TCD-25-03 | EP | The labels \"Your rating *\", \"Your review *\", \"Name *\" and \"Email *\" are shown, each with the required marker *. | Positive | |\n| TCD-25-04 | EP | The save checkbox reads \"Save my name, email, and website in this browser for the next time I comment.\" | Positive | Missing info: final text of the save checkbox (Q-13). |\n| TCD-25-05 | EP | A \"Submit\" button is shown below the save checkbox. | Positive | |\n| TCD-25-06 | EP | The elements are in the mockup-1 order from top to bottom: heading, info text, rating, review, Name, Email, save checkbox, Submit. | Positive | |\n| TCD-25-07 | Error guessing | Tab moves the focus through the form in the order shown, and Submit can be used with the keyboard. | Positive | Missing info: keyboard use is not stated in any source; new question needed. |\n\n### TR-26: Verify that only a customer who is allowed to review (as confirmed for Q-01) can submit a review, and a customer who is not allowed cannot.\n\nTechnique(s): Decision table - conditions \"signed in: yes / no\" and \"bought this product: yes / no\"; outcome \"may submit\". The two \"not signed in\" rules are collapsed into one because the purchase cannot be linked to a guest without sign-in until Q-01 says otherwise. Error guessing - cancelled orders.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-26-01 | Decision table | Rule: signed in and bought the product: the customer can submit a review. | Positive | Missing info: sign-in and purchase check not specified (Q-01).<br>Missing info: demo-1.0 has no sign-in (environment.md). |\n| TCD-26-02 | Decision table | Rule: signed in and did not buy the product: the form is hidden, disabled or rejected on Submit with a message, as confirmed for Q-01. | Negative | Missing info: Q-01.<br>Risk: non-buyers could post fake reviews. |\n| TCD-26-03 | Decision table | Rule: not signed in (guest): the form is hidden, disabled or rejected on Submit with a message, as confirmed for Q-01. | Negative | Missing info: Q-01.<br>Risk: guests could post fake reviews. |\n| TCD-26-04 | Error guessing | Signed in, the order of this product was cancelled or refunded: the customer may or may not review, as confirmed for Q-01. | Negative | Edge case: cancelled or refunded purchase.<br>Missing info: not covered by Q-01 yet; to be added to Q-01. |\n\n### TR-27: Verify that Name and Email for a signed-in customer are handled as confirmed for Q-02 (prefilled, editable or not shown).\n\nTechnique(s): Equivalence Partitioning - the three possible answers to Q-02 (prefilled, editable, not shown) are the partitions; the applicable one is kept when Q-02 is answered.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-27-01 | EP | Signed-in customer opens the form: Name and Email are prefilled from the account, editable, or not shown, as confirmed for Q-02. | Positive | Missing info: conflict between the story and mockup-1 (Q-02). |\n| TCD-27-02 | EP | If Name is prefilled and editable: the customer changes the Name, submits, and the displayed review shows the name as confirmed for Q-02 (edited or account name). | Positive | Missing info: Q-02. |\n\n### TR-28: Verify that the review cannot be submitted when \"Name\" is empty.\n\nTechnique(s): Equivalence Partitioning - \"empty\" is the invalid partition of a required field.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-28-01 | EP | \"Name\" empty, rating, Review and Email valid, Submit: the review is not submitted and an error names \"Name\". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |\n\n### TR-29: Verify that a Name within the allowed length and characters is accepted, and a Name outside them is rejected.\n\nTechnique(s): Equivalence Partitioning - character partitions (Latin letters, accented letters, hyphen/apostrophe, non-Latin script, digits, symbols only), one invalid partition per condition. Boundary Value Analysis - minimum (1 character, just above empty) and maximum length.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-29-01 | EP | Name of Latin letters and a space (for example \"Anna Smith\"): accepted. | Positive | Assumption: letters and spaces are allowed until Q-05 is answered. |\n| TCD-29-02 | EP | Name with accented letters (for example \"Zoë Lê\"): accepted. | Positive | Edge case: accented letters.<br>Assumption: accented letters are allowed until Q-05 is answered. |\n| TCD-29-03 | EP | Name with a hyphen and an apostrophe (for example \"Mary-Jane O'Neil\"): accepted. | Positive | Edge case: hyphen and apostrophe.<br>Assumption: hyphens and apostrophes are allowed until Q-05 is answered. |\n| TCD-29-04 | EP | Name in a non-Latin script (for example \"李明\"): accepted or rejected as confirmed for Q-05. | Positive | Missing info: allowed characters not stated (Q-05). |\n| TCD-29-05 | EP | Name containing digits (for example \"Anna2\"): accepted or rejected with an error naming \"Name\", as confirmed for Q-05. | Negative | Missing info: whether digits are allowed (Q-05). |\n| TCD-29-06 | EP | Name made only of symbols (for example \"@#$%\"): rejected with an error naming \"Name\", unless Q-05 allows it. | Negative | Missing info: allowed characters not stated (Q-05). |\n| TCD-29-07 | BVA | Name of 1 character (just above empty): accepted. | Positive | Edge case: shortest non-empty name.<br>Missing info: minimum length not stated (Q-05). |\n| TCD-29-08 | BVA | Name length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-05). |\n| TCD-29-09 | BVA | Name length = maximum: accepted and shown in full. | Positive | Edge case: Name at the maximum length.<br>Missing info: maximum length not stated (Q-05). |\n| TCD-29-10 | BVA | Name length = maximum + 1: input stops at the maximum, or the review is rejected with an error naming \"Name\". | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length and over-length behaviour not stated (Q-05, Q-18). |\n\n### TR-30: Verify that the review cannot be submitted when \"Email\" is empty.\n\nTechnique(s): Equivalence Partitioning - \"empty\" is the invalid partition of a required field.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-30-01 | EP | \"Email\" empty, rating, Review and Name valid, Submit: the review is not submitted and an error names \"Email\". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |\n\n### TR-31: Verify that a correctly formatted email is accepted and an incorrectly formatted email is rejected.\n\nTechnique(s): Equivalence Partitioning - valid format partitions and one invalid partition per format fault (one fault per condition). Boundary Value Analysis - maximum length. Error guessing - upper-case letters.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-31-01 | EP | Email \"anna.smith@example.com\": accepted. | Positive | Assumption: standard format text@domain.tld until Q-06 is answered. |\n| TCD-31-02 | EP | Email with a plus sign and a sub-domain (\"anna+shop@mail.example.co.uk\"): accepted. | Positive | Edge case: plus sign and sub-domain.<br>Assumption: standard format (Q-06). |\n| TCD-31-03 | EP | Email without \"@\" (\"anna.example.com\"): rejected with an error naming \"Email\". | Negative | Assumption: standard format (Q-06). |\n| TCD-31-04 | EP | Email without the part before \"@\" (\"@example.com\"): rejected with an error naming \"Email\". | Negative | Assumption: standard format (Q-06). |\n| TCD-31-05 | EP | Email without a domain (\"anna@\"): rejected with an error naming \"Email\". | Negative | Assumption: standard format (Q-06). |\n| TCD-31-06 | EP | Email without a top-level domain (\"anna@example\"): rejected with an error naming \"Email\". | Negative | Assumption: a top-level domain is required (Q-06); some format rules accept this value. |\n| TCD-31-07 | EP | Email with two \"@\" (\"anna@@example.com\"): rejected with an error naming \"Email\". | Negative | Assumption: standard format (Q-06). |\n| TCD-31-08 | EP | Email with a space inside (\"anna smith@example.com\"): rejected with an error naming \"Email\". | Negative | Assumption: standard format (Q-06). |\n| TCD-31-09 | Error guessing | Email in upper case (\"ANNA@EXAMPLE.COM\"): accepted. | Positive | Assumption: letter case does not matter (Q-06). |\n| TCD-31-10 | BVA | Email length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-06). |\n| TCD-31-11 | BVA | Email length = maximum: accepted. | Positive | Edge case: value exactly at the maximum.<br>Missing info: maximum length not stated (Q-06). |\n| TCD-31-12 | BVA | Email length = maximum + 1: input stops at the maximum, or the review is rejected with an error naming \"Email\". | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length and over-length behaviour not stated (Q-06, Q-18). |\n\n### TR-32: Verify that leading and trailing spaces in Name and Email are removed, and a Name or Email made only of spaces counts as empty.\n\nTechnique(s): Error guessing - space-padded and spaces-only input, one field per condition.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-32-01 | Error guessing | Name with leading and trailing spaces (\"  Anna Smith  \"): accepted and, after approval, shown as \"Anna Smith\". | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |\n| TCD-32-02 | Error guessing | Name made only of spaces, Submit: the review is not submitted and an error names \"Name\". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |\n| TCD-32-03 | Error guessing | Email with leading and trailing spaces (\"  anna@example.com  \"): accepted as a valid email. | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |\n| TCD-32-04 | Error guessing | Email made only of spaces, Submit: the review is not submitted and an error names \"Email\". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |\n\n### TR-33: Verify that when all required fields are valid, the review is submitted and a confirmation message is shown.\n\nTechnique(s): Decision table - conditions \"rating, review, name, email valid\" and \"save checkbox ticked: yes / no\"; the all-valid rules give \"submitted\". The rules with one field invalid are listed under TR-34.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-33-01 | Decision table | Rule: all four required fields valid, save checkbox not ticked, Submit: the review is submitted and a confirmation says it was received and waits for approval. | Positive | Assumption: confirmation says the review was received and waits for approval (Q-21). |\n| TCD-33-02 | Decision table | Rule: all four required fields valid, save checkbox ticked, Submit: the review is submitted with the same confirmation. | Positive | Assumption: confirmation text (Q-21). |\n\n### TR-34: Verify that when a required field is empty or invalid, the review is not submitted and an error message names each field concerned.\n\nTechnique(s): Decision table - conditions \"rating / review / name / email valid: yes / no\". Rules with exactly one invalid field are already covered: TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-31-03 to TCD-31-08. Rules with several invalid fields are collapsed into \"all empty\" and \"two empty\", which check that every field concerned is named. Equivalence Partitioning - validation timing.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-34-01 | Decision table | Rule: all four required fields empty, Submit: the review is not submitted and errors name all four fields. | Negative | Assumption: each error names its field; wording checked for meaning (Q-20). |\n| TCD-34-02 | Decision table | Rule: rating and review empty, Name and Email valid, Submit: errors name the rating and \"Your review\" only, not Name or Email. | Negative | Assumption: wording checked for meaning (Q-20). |\n| TCD-34-03 | Decision table | After a rejected Submit, the values already entered stay in the form; the customer corrects the field, submits again and the review is submitted. | Positive | Assumption: entered values are kept after a rejected submit; not stated, to be added to Q-19. |\n| TCD-34-04 | EP | Leaving a required field empty and moving to the next field shows no error until Submit is pressed. | Positive | Assumption: fields are checked on Submit only (Q-19). |\n\n### TR-35: Verify that after a successful submit the customer stays on the product page and the form is cleared.\n\nTechnique(s): State transition - \"form filled\" to \"form after success\", with the save checkbox ticked or not as the deciding event.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-35-01 | State transition | Successful Submit with the save checkbox not ticked: the customer stays on the product page and rating, review, Name and Email are all cleared. | Positive | Assumption: form cleared (Q-22). |\n| TCD-35-02 | State transition | Successful Submit with the save checkbox ticked: the customer stays on the product page, rating and review are cleared, and Name and Email stay filled. | Positive | Assumption: Name and Email stay filled only if the checkbox was ticked (Q-22). |\n\n### TR-36: Verify that the \"Save my name, email, and website...\" checkbox is unchecked by default.\n\nTechnique(s): Equivalence Partitioning - partitions \"first visit (nothing saved)\" and \"visit after data was saved\".\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-36-01 | EP | First visit with nothing saved in the browser: the save checkbox is not ticked. | Positive | |\n| TCD-36-02 | EP | Visit after Name and Email were saved: the save checkbox is ticked or not ticked, as confirmed for Q-14. | Positive | Edge case: checkbox state on a return visit.<br>Missing info: not stated (Q-14). |\n\n### TR-37: Verify that when the save checkbox is ticked at submit, the name and email are filled in again on the next visit in the same browser.\n\nTechnique(s): State transition - browser storage states \"nothing saved\" and \"Name and Email saved\"; events \"Submit with box ticked\", \"Submit with box not ticked\", \"rejected Submit\". Error guessing - other browser or private window.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-37-01 | State transition | Nothing saved, valid Submit with the box ticked, next visit in the same browser: Name and Email are filled with the submitted values. | Positive | Assumption: only name and email are saved (Q-13, Q-14).<br>Risk: personal data stored on the device. |\n| TCD-37-02 | State transition | Name and Email saved, valid Submit with a different Name and Email and the box ticked, next visit: the new values are filled. | Positive | Assumption: saved values are replaced (Q-14). |\n| TCD-37-03 | State transition | Name and Email saved, valid Submit with the box not ticked, next visit: Name and Email are filled or empty as confirmed for Q-14. | Positive | Missing info: how saved data is removed (Q-14).<br>Risk: personal data left on a shared device. |\n| TCD-37-04 | EP | After a ticked Submit, on the next visit only Name and Email are filled; rating and review are empty. | Positive | Assumption: only name and email are saved (Q-13, Q-14). |\n| TCD-37-05 | Error guessing | After a ticked Submit, opening the page in another browser or a private window: Name and Email are empty. | Positive | Edge case: \"in this browser\" only. |\n| TCD-37-06 | State transition | Nothing saved, box ticked but Submit rejected (for example \"Your review\" empty), next visit: Name and Email are empty. | Negative | Edge case: rejected submit with the box ticked.<br>Missing info: whether data is saved on a rejected submit (Q-14). |\n\n### TR-38: Verify that when the save checkbox is not ticked, no name or email is kept for the next visit.\n\nTechnique(s): Equivalence Partitioning - partition \"box not ticked, nothing saved before\". Error guessing - data typed but not submitted.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-38-01 | EP | Nothing saved, valid Submit with the box not ticked, next visit: Name and Email are empty. | Positive | Missing info: what is saved when the checkbox is not ticked (Q-14).<br>Risk: personal data left on a shared device. |\n| TCD-38-02 | Error guessing | Name and Email typed but not submitted, page reloaded: Name and Email are empty (browser autofill switched off). | Positive | Missing info: Q-14.<br>Risk: personal data kept without consent. |\n\n### TR-39: Verify that a customer cannot submit more reviews for the same product than the confirmed limit.\n\nTechnique(s): Boundary Value Analysis - count of reviews per customer and product (limit unknown). Error guessing - other product, changed identity.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-39-01 | BVA | Customer has limit - 1 reviews for the product, submits another: accepted. | Positive | Missing info: number of reviews per customer and product not specified (Q-12). If the limit is 1, this is the first review (TCD-33-01) and is not repeated. |\n| TCD-39-02 | BVA | Customer has exactly the limit, submits another (limit + 1): rejected with the message confirmed for Q-12. | Negative | Edge case: one above the limit.<br>Missing info: Q-12. |\n| TCD-39-03 | Error guessing | Customer at the limit for product A submits a review for product B: accepted. | Positive | Missing info: Q-12; needs a build with two products. |\n| TCD-39-04 | Error guessing | Customer at the limit submits again for the same product with a different Name and Email: still recognised and rejected. | Negative | Missing info: how the customer is identified (Q-01, Q-02, Q-12).<br>Risk: limit bypassed by changing name or email. |\n\n### TR-40: Verify that clicking Submit more than once quickly creates only one review.\n\nTechnique(s): Error guessing - double click, repeated key presses, reload and browser back/forward after submit are known duplicate sources.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-40-01 | Error guessing | Valid form, Submit double-clicked: one review is created (one pending, one shown after approval). | Negative | Edge case: rapid double click.<br>Assumption: only one review is created (Q-28).<br>Risk: duplicate reviews distort the rating. |\n| TCD-40-02 | Error guessing | Valid form, Submit clicked and Enter pressed in a text field before the confirmation appears: one review is created. | Negative | Assumption: only one review is created (Q-28). |\n| TCD-40-03 | Error guessing | Page reloaded right after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |\n| TCD-40-04 | Error guessing | Browser Back and then Forward after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |\n\n### TR-41: Verify that when the review cannot be saved (server or network error), the customer is told and the entered data is kept.\n\nTechnique(s): Error guessing - lost connection, server error and expired session are typical failure points of a submit.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-41-01 | Error guessing | Network connection lost, Submit: a message says the review was not submitted and the entered data stays in the form. | Negative | Assumption: Q-29.<br>Missing info: demo-1.0 runs without a server or network (environment.md), so this cannot be produced there. |\n| TCD-41-02 | Error guessing | Server returns an error on Submit: a message says the review was not submitted and the entered data stays in the form. | Negative | Assumption: Q-29. Not producible in demo-1.0. |\n| TCD-41-03 | Error guessing | Session expired before Submit (signed-in customer): the customer is told and the entered data is not lost. | Negative | Assumption: Q-29.<br>Missing info: sign-in rules (Q-01); demo-1.0 has no sign-in. |\n| TCD-41-04 | Error guessing | After a failed Submit, the connection returns and Submit is pressed again: exactly one review is created. | Positive | Assumption: Q-28, Q-29. |\n\n## Coverage by scenario type\n\n| Type | Covered by (condition IDs) |\n|---|---|\n| Positive | TCD-02-01, TCD-03-01 to TCD-03-04, TCD-04-01, TCD-04-02, TCD-04-05, TCD-06-01, TCD-08-01, TCD-09-01 to TCD-09-04, TCD-14-01, TCD-17-01, TCD-29-01, TCD-31-01, TCD-33-01, TCD-33-02, TCD-35-01, TCD-37-01 |\n| Negative | TCD-02-02, TCD-04-03, TCD-05-01, TCD-07-01, TCD-10-01 to TCD-10-04, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-05, TCD-29-06, TCD-30-01, TCD-31-03 to TCD-31-08, TCD-34-01, TCD-34-02, TCD-39-02 |\n| Boundary | TCD-03-01 to TCD-03-04, TCD-05-01, TCD-09-01 to TCD-09-04, TCD-10-01 to TCD-10-03, TCD-11-04, TCD-21-02 to TCD-21-04, TCD-22-01, TCD-22-03, TCD-23-05, TCD-29-07 to TCD-29-10, TCD-31-10 to TCD-31-12, TCD-39-01, TCD-39-02 |\n| Validation | TCD-05-01, TCD-07-01, TCD-10-01, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-05, TCD-29-06, TCD-30-01, TCD-31-03 to TCD-31-08, TCD-32-02, TCD-32-04, TCD-34-01 to TCD-34-04 |\n| Error handling | TCD-40-01 to TCD-40-04, TCD-41-01 to TCD-41-04 |\n| Permissions | TCD-26-01 to TCD-26-04, TCD-27-01, TCD-27-02, TCD-13-01, TCD-16-01, TCD-16-02, TCD-39-02, TCD-39-04 |\n| Integration | TCD-13-01, TCD-13-02, TCD-14-01 to TCD-14-03, TCD-15-01, TCD-15-02, TCD-17-01 to TCD-17-03, TCD-18-01, TCD-20-01 to TCD-20-03, TCD-21-01, TCD-22-01 to TCD-22-03, TCD-23-01 to TCD-23-06, TCD-24-01, TCD-24-02 |\n| UI | TCD-01-01, TCD-02-03, TCD-02-04, TCD-06-01, TCD-06-02, TCD-18-04, TCD-25-01 to TCD-25-07 |\n| Compatibility | None in this design; see \"Not covered\" |\n| Regression | TCD-14-02, TCD-15-02, TCD-18-01, TCD-20-02, TCD-22-03, TCD-23-04 (existing approved reviews, the empty state and the rating summary still behave correctly after new reviews are added) |\n| Data and privacy | TCD-12-01 to TCD-12-05, TCD-17-03, TCD-19-01, TCD-19-02, TCD-36-01, TCD-36-02, TCD-37-01 to TCD-37-06, TCD-38-01, TCD-38-02 |\n\n## Not covered\n\n| Type or area | Reason |\n|---|---|\n| Compatibility: browsers other than Chrome, mobile and tablet screen sizes | Only Chrome is given (environment.md, app-note.md); other browsers and devices are blocked by missing information (Q-31). Add conditions when Q-31 is answered. |\n| Language and localisation | Page language not stated; English assumed (Q-31). |\n| Moderator screens and workflow (approve / reject UI, who moderates) | Out of scope of US-VP02; only its effect on the product page is covered (TR-14, TR-15). The demo-1.0 helper button is a test tool, not the feature (environment.md). |\n| Telling the author the moderation result (for example by email) | Assumed out of scope of this story (Q-26). |\n| Editing or deleting one's own review | Assumed out of scope of this story (Q-27). |\n| Automatic offensive-language filter | Assumed left to the moderator, no automatic filter (Q-30). |\n| \"Website\" field | No Website field exists in mockup-1; nothing to test until Q-13 is answered (only the checkbox text is covered, TCD-25-04). |\n| Accessibility beyond keyboard use (screen reader labels, colour contrast) | Not in any source; only keyboard use is covered (TCD-02-04, TCD-25-07). |\n| Performance and load (many users submitting at once) | Not in the story; needs another environment. |\n| Execution on demo-1.0 of TCD-13-01, TCD-13-02, TCD-15-01, TCD-15-02, TCD-23-03, TCD-24-02, TCD-26-01 to TCD-26-04, TCD-27-01, TCD-27-02, TCD-39-03, TCD-39-04, TCD-41-01 to TCD-41-03 | The conditions exist, but demo-1.0 has one product, no sign-in, no reject action, no server, and resets data on reload (app-note.md, environment.md); they need another build or environment. |\n\n## Assumptions to confirm\n\n| Condition ID | Assumption | Question ID |\n|---|---|---|\n| TCD-02-01, TCD-03-01 to TCD-03-04 | The rating is a whole number from 1 to 5, one per star. | Q-03 |\n| TCD-02-03 | A hover preview, if any, is not kept after the pointer leaves. | New, to be added to Q-16 |\n| TCD-04-01 to TCD-04-04 | Clicking another star changes the rating; it cannot be cleared except by reloading the page. | Q-16 |\n| TCD-08-02 | \"Your review\" has no character restriction (accented, non-Latin, emoji allowed). | New, to be added to Q-15 |\n| TCD-10-02 to TCD-10-04 | Typing and pasting stop at the maximum length. | Q-18 |\n| TCD-11-01 to TCD-11-04, TCD-32-01 to TCD-32-04 | Spaces (and line breaks) are trimmed; a field of only spaces counts as empty; length is counted after trimming. | Q-17 |\n| TCD-12-01 | HTML and script content is never executed, whatever the answer on how it is handled. | Q-15 |\n| TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-34-01, TCD-34-02 | Each error names its field; wording is checked for meaning, not exact text. | Q-20 |\n| TCD-34-03 | Entered values stay in the form after a rejected Submit. | New, to be added to Q-19 |\n| TCD-34-04 | Fields are checked on Submit only. | Q-19 |\n| TCD-14-01 | The demo-1.0 \"Moderator: approve pending reviews\" helper stands in for the moderator and is not part of the feature. | Q-07 |\n| TCD-17-01 | Each displayed review shows star rating, reviewer name, date and review text. | Q-09 |\n| TCD-17-02 | The date is the submit date, in any unambiguous format. | Q-24 |\n| TCD-18-02, TCD-29-01 to TCD-29-03 | Names with letters, spaces, accented letters, hyphens and apostrophes are accepted. | Q-05 |\n| TCD-21-01 | All approved reviews are shown on one page. | Q-23 |\n| TCD-22-01 to TCD-22-03 | With no approved reviews, a short message says there are no reviews yet. | Q-25 |\n| TCD-25-01 | The heading \"ADD A REVIEW\" is compared without regard to letter case. | Q-32 |\n| TCD-31-01 to TCD-31-09 | A valid email has the standard format text@domain.tld (top-level domain required, letter case ignored). | Q-06 |\n| TCD-33-01, TCD-33-02 | The confirmation says the review was received and waits for approval. | Q-21 |\n| TCD-35-01, TCD-35-02 | After success the customer stays on the page; the form is cleared; Name and Email stay only if the checkbox was ticked. | Q-22 |\n| TCD-37-01, TCD-37-02, TCD-37-04 | Only Name and Email are saved in this browser, and a new ticked submit replaces them. | Q-13, Q-14 |\n| TCD-40-01 to TCD-40-04, TCD-41-04 | Only one review is created per submit action. | Q-28 |\n| TCD-41-01 to TCD-41-04 | On a save failure a message says the review was not submitted and the entered data is kept. | Q-29 |\n"
}
```

## Tool (2026-10-21T04:07:37)

```
File created successfully at: C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-1\test-design.md (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:07:43)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1 && python -I - <<'EOF'\nimport re,collections\nt=open('test-design.md',encoding='utf-8').read()\nids=re.findall(r'^\\| (TCD-\\d\\d-\\d\\d) \\|',t,re.M)\nprint(len(ids),'conditions; dups:',[i for i,c in collections.Counter(ids).items() if c>1])\nper=collections.Counter(i[4:6] for i in ids)\nprint('TRs with conditions:',len(per),'missing:',[f'{n:02d}' for n in range(1,42) if f'{n:02d}' not in per])\nprint(dict(sorted(per.items())))\nrows=re.findall(r'^\\| TCD-\\d\\d-\\d\\d \\| ([^|]+) \\|[^|]+\\| ([^|]+) \\|',t,re.M)\nprint(collections.Counter(r[0].strip() for r in rows)); print(collections.Counter(r[1].strip() for r in rows))\nrefs=set(re.findall(r'TCD-\\d\\d-\\d\\d',t)); print('dangling refs:',sorted(refs-set(ids)))\nEOF",
  "description": "Verify condition IDs, TR coverage and counts"
}
```

## Tool (2026-10-21T04:07:46)

```
155 conditions; dups: ['TCD-02-03', 'TCD-08-02', 'TCD-12-01', 'TCD-14-01', 'TCD-17-01', 'TCD-17-02', 'TCD-21-01', 'TCD-25-01', 'TCD-34-03', 'TCD-34-04']
TRs with conditions: 41 missing: []
{'01': 1, '02': 5, '03': 4, '04': 5, '05': 1, '06': 2, '07': 1, '08': 4, '09': 4, '10': 4, '11': 4, '12': 6, '13': 2, '14': 4, '15': 2, '16': 2, '17': 5, '18': 4, '19': 2, '20': 3, '21': 5, '22': 3, '23': 6, '24': 2, '25': 8, '26': 4, '27': 2, '28': 1, '29': 10, '30': 1, '31': 12, '32': 4, '33': 2, '34': 6, '35': 2, '36': 2, '37': 6, '38': 2, '39': 4, '40': 4, '41': 4}
Counter({'EP': 45, 'Error guessing': 41, 'BVA': 27, 'State transition': 18, 'Decision table': 13, 'EP / BVA': 1})
Counter({'Positive': 94, 'Negative': 51})
dangling refs: []
```

## AI (2026-10-21T04:08:01)

I ran the test-condition-design skill and wrote one file: `C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-1\test-design.md`. Nothing else was changed. It follows the skill's template, and many of its expected results stay open until the product owner answers Q-01 to Q-32.

**Sources I used:** the TR xlsx (41 TRs, TR-01 to TR-41, every row has an ID and text), `clarification-questions.md` (no answers yet), the knowledge folder (`index.md`, `product-review-rules.md`, `screens-and-fields.md`, `glossary.md`, `environment.md`) and the exam folder (`user-story.md`, `mockup-1.png`, `app-note.md`). Following the knowledge index, the demo build's "0 / 500" counter and its message texts are treated as observed only. I did not use them as expected values.

**What's in the file:**
- **Values and rules used:** about 40 items, each marked Confirmed or Assumption/Missing info, with its source and Q-ID.
- **Conditions:** 145 test conditions, IDs `TCD-<TR>-<nn>`. All 41 TRs have at least one, and no ID is reused. 94 are Positive and 51 Negative.
- **Techniques:** equivalence partitioning 45, error guessing 41, boundary value analysis 27, state transition 18, decision table 13, and one combined EP/BVA.
- **Coverage table:** maps each of the 11 scenario types to condition IDs. Compatibility has no conditions and is listed under "Not covered".

**Missing limits:** the minimum/maximum for the review text, Name and Email aren't in any source (Q-04, Q-05, Q-06). The same goes for the page size (Q-23), the per-customer review limit (Q-12) and the rounding of the average (Q-11). I did not invent numbers for these. Their boundary conditions are written in symbolic form (min-1, min, min+1, max-1, max, max+1) with a Missing info note. Where the minimum might be 1, the duplicate with the empty-field condition is noted rather than written twice.

**Assumptions:** 23 assumption rows, all taken from the TR notes, the "Nice to confirm" assumptions or the knowledge file. The main ones are:
- rating is a whole number from 1 to 5
- spaces are trimmed and a spaces-only field counts as empty
- typing and pasting stop at the maximum length
- standard email format
- confirmation, form-after-submit and empty-state behaviour
- only one review per submit
- the save checkbox stores only Name and Email

**Not covered (10 rows):**
- other browsers and mobile (Q-31)
- language and localisation
- moderator screens and workflow
- telling the author the moderation result (Q-26)
- editing or deleting one's own review (Q-27)
- offensive-language filter (Q-30)
- the Website field (Q-13)
- accessibility beyond keyboard use
- performance and load
- conditions that can't be run on demo-1.0: it has one product, no sign-in, no reject action and no server, and it resets data on reload. This affects 19 conditions, including the permission, rejection, other-product and network-error checks.

**New questions to add:** six conditions depend on things none of Q-01 to Q-32 ask about yet:
- keyboard use for the rating and the form (TCD-02-04, TCD-25-07)
- whether line breaks are kept when a review is displayed (TCD-06-02)
- hover preview on the stars (TCD-02-03)
- whether "Your review" restricts characters (TCD-08-02)
- whether entered values stay after a rejected submit (TCD-34-03)
- cancelled or refunded orders and permission to review (TCD-26-04)

**Conflicts:** none. With no PO answers there is nothing to contradict the TR file or the knowledge files.

The skill says to stop here and wait for your approval before test cases are written. Two decisions are yours: whether to proceed with the assumptions as they stand, and whether to add the six new questions to `clarification-questions.md`.

## Tool (2026-10-21T04:08:02)

```
{"success":true,"message":"Report delivered to your caller."}
```

## Trainee (2026-10-21T04:08:44)

ok I checked it. 145 conditions in the Test conditions section, matches what you said, and the similar-looking ones (TCD-03-01..04, TCD-21-02..04) are just BVA points so fine.

decisions:
1. go ahead with the assumptions as they are.
2. yes add the 6 new questions to runs/run-1/clarification-questions.md, continue numbering after the last Q. put "cancelled or refunded orders and permission to review" under Must ask (it changes who can review, same area as Q-01). the other 5 (keyboard use, line breaks in display, star hover preview, characters allowed in Your review, values kept after a rejected submit) under Nice to confirm, each with your working assumption like the others.
3. update the Q-IDs in the notes of those 6 conditions in test-design.md so they point to the new questions.

don't change anything else. tell me the new Q-IDs and which cells/lines you changed.

Address this before completing your current task.

## AI (2026-10-21T04:09:00)

**Tool call `Edit`:**

```json
{
  "replace_all": false,
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\runs\\run-1\\clarification-questions.md",
  "old_string": "| Security risk (script injection) and display of every review. |\n",
  "new_string": "| Security risk (script injection) and display of every review. |\n| Q-33 | AC-GEN | Cancelled or refunded orders | If the customer's order of this product was cancelled or refunded, may they still submit a review? If not, should the form be hidden, disabled, or rejected on Submit with a message? | Same area as Q-01: changes who may review. Risk of reviews from customers who never received the product. |\n"
}
```

## AI (2026-10-21T04:09:05)

**Tool call `Edit`:**

```json
{
  "replace_all": false,
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\runs\\run-1\\clarification-questions.md",
  "old_string": "| The heading text is compared without regard to letter case. |\n",
  "new_string": "| The heading text is compared without regard to letter case. |\n| Q-34 | AC-GEN | Keyboard use | Must the star rating and the whole form (fields, checkbox, Submit) be usable with the keyboard alone, and in which focus order? | The rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen. |\n| Q-35 | AC-03 | Line breaks in a displayed review | If \"Your review\" is written on several lines, should the line breaks be kept when the review is shown on the product page? | Line breaks are shown as entered. |\n| Q-36 | AC-01 | Star hover preview | When the pointer moves over the stars without clicking, may the stars show a preview, and must the selected rating come back when the pointer leaves? | A hover preview, if any, is not kept; the selected rating is unchanged after the pointer leaves. |\n| Q-37 | AC-02 | Characters allowed in \"Your review\" | Are all characters allowed in \"Your review\" (accented and non-Latin letters, digits, punctuation, emoji), or are some blocked? | No character restriction in \"Your review\". |\n| Q-38 | AC-GEN | Values after a rejected submit | After Submit is rejected because of an error, should the values already entered stay in the form? | Entered values stay in the form after a rejected Submit. |\n"
}
```

## Tool (2026-10-21T04:09:05)

```
The file C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-1\clarification-questions.md has been updated successfully.
```

## Tool (2026-10-21T04:09:05)

```
The file C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-1\clarification-questions.md has been updated successfully.
```

## AI (2026-10-21T04:09:06)

Now the condition notes in test-design.md.

## AI (2026-10-21T04:09:11)

**Tool call `Bash`:**

```json
{
  "command": "python -I - <<'EOF'\np='test-design.md'\nt=open(p,encoding='utf-8').read()\nreps=[\n(\"Assumption: a hover preview, if any, is not kept; no question raised yet, to be added to Q-16.\",\"Assumption: a hover preview, if any, is not kept until Q-36 is answered.\",1),\n(\"Missing info: keyboard use is not stated in any source; new question needed.\",\"Missing info: keyboard use is not stated in any source (Q-34).\",2),\n(\"Missing info: display of line breaks is not stated in any source; new question needed.\",\"Missing info: display of line breaks is not stated in any source (Q-35).\",1),\n('Assumption: no character restriction in \"Your review\"; no source restricts it, to be added to Q-15.','Assumption: no character restriction in \"Your review\" until Q-37 is answered.',1),\n(\"Missing info: not covered by Q-01 yet; to be added to Q-01.\",\"Missing info: cancelled or refunded purchase not specified (Q-33).\",1),\n(\"Assumption: entered values are kept after a rejected submit; not stated, to be added to Q-19.\",\"Assumption: entered values are kept after a rejected submit until Q-38 is answered.\",1),\n]\nfor a,b,n in reps:\n    c=t.count(a); assert c==n,(a,c); t=t.replace(a,b)\nopen(p,'w',encoding='utf-8',newline='').write(t)\nimport re\nfor l in t.splitlines():\n    if re.search(r'Q-3[3-8]',l): print(l[:60],'...',re.findall(r'Q-3[3-8]',l))\nEOF\ngrep -n \"New, to be added\" test-design.md",
  "description": "Update Q-IDs in condition notes and list remaining stale refs"
}
```

## Tool (2026-10-21T04:09:13)

```
| TCD-02-03 | Error guessing | Moving the pointer over the s ... ['Q-36']
| TCD-02-04 | Error guessing | The rating can be selected wi ... ['Q-34']
| TCD-06-02 | Error guessing | A review written on several l ... ['Q-35']
| TCD-08-02 | Error guessing | Review text with accented let ... ['Q-37']
| TCD-25-07 | Error guessing | Tab moves the focus through t ... ['Q-34']
| TCD-26-04 | Error guessing | Signed in, the order of this  ... ['Q-33']
| TCD-34-03 | Decision table | After a rejected Submit, the  ... ['Q-38']
521:| TCD-02-03 | A hover preview, if any, is not kept after the pointer leaves. | New, to be added to Q-16 |
523:| TCD-08-02 | "Your review" has no character restriction (accented, non-Latin, emoji allowed). | New, to be added to Q-15 |
528:| TCD-34-03 | Entered values stay in the form after a rejected Submit. | New, to be added to Q-19 |
```

## AI (2026-10-21T04:09:24)

I've added the 6 new questions to `clarification-questions.md` and pointed the condition notes in `test-design.md` at them. Three cells elsewhere in `test-design.md` now point to the wrong questions; I left them because you said not to change anything else.

**New Q-IDs**

| Q-ID | Section | Topic | AC ID |
|---|---|---|---|
| Q-33 | Must ask | Cancelled or refunded orders and permission to review | AC-GEN |
| Q-34 | Nice to confirm | Keyboard use | AC-GEN |
| Q-35 | Nice to confirm | Line breaks in a displayed review | AC-03 |
| Q-36 | Nice to confirm | Star hover preview | AC-01 |
| Q-37 | Nice to confirm | Characters allowed in "Your review" | AC-02 |
| Q-38 | Nice to confirm | Values after a rejected submit | AC-GEN |

The working assumptions for Q-34 to Q-38 are:
- **Q-34:** the rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the on-screen order.
- **Q-35:** line breaks are shown as entered.
- **Q-36:** a hover preview, if any, is not kept.
- **Q-37:** "Your review" has no character restriction.
- **Q-38:** entered values stay in the form after a rejected Submit.

**Changes in `runs/run-1/clarification-questions.md`**
- One row added at the end of the Must ask table, after Q-15: Q-33.
- Five rows added at the end of the Nice to confirm table, after Q-32: Q-34 to Q-38.

**Changes in `runs/run-1/test-design.md`**
Only the Notes cell of each row below was changed. There are 7 rows, not 6, because Q-34 covers two conditions:
- **TCD-02-03:** now reads "Assumption: a hover preview, if any, is not kept until Q-36 is answered." (was "to be added to Q-16")
- **TCD-02-04:** "new question needed" is now "(Q-34)".
- **TCD-06-02:** "new question needed" is now "(Q-35)".
- **TCD-08-02:** now reads "Assumption: no character restriction in "Your review" until Q-37 is answered." (was "to be added to Q-15")
- **TCD-25-07:** "new question needed" is now "(Q-34)".
- **TCD-26-04:** now reads "Missing info: cancelled or refunded purchase not specified (Q-33)." (was "to be added to Q-01")
- **TCD-34-03:** now reads "Assumption: entered values are kept after a rejected submit until Q-38 is answered." (was "to be added to Q-19")

**Cells now out of date**
In the "Assumptions to confirm" table at the end of `test-design.md`, the Question ID cell still says "New, to be added to Q-xx" on three lines:
- line 521, TCD-02-03: should be Q-36
- line 523, TCD-08-02: should be Q-37
- line 528, TCD-34-03: should be Q-38

Nothing else was changed.

## Tool (2026-10-21T04:09:25)

```
{"success":true,"message":"Report delivered to your caller."}
```

## Trainee (2026-10-21T04:09:30)

good catch, my "don't change anything else" was too strict. pls fix those 3 Question ID cells in the Assumptions to confirm table (lines 521, 523, 528 -> Q-36, Q-37, Q-38). then check there's no "to be added" or "new question needed" text left anywhere in test-design.md, and tell me the result.

Address this before completing your current task.

## AI (2026-10-21T04:09:34)

**Tool call `Bash`:**

```json
{
  "command": "python -I - <<'EOF'\np='test-design.md'\nt=open(p,encoding='utf-8').read()\nfor a,b in [(\"| New, to be added to Q-16 |\",\"| Q-36 |\"),(\"| New, to be added to Q-15 |\",\"| Q-37 |\"),(\"| New, to be added to Q-19 |\",\"| Q-38 |\")]:\n    assert t.count(a)==1,a; t=t.replace(a,b)\nopen(p,'w',encoding='utf-8',newline='').write(t)\nEOF\nsed -n '521p;523p;528p' test-design.md; echo ---; grep -n -i -E \"to be added|new question needed\" test-design.md; echo \"grep exit: $?\"",
  "description": "Fix 3 Question ID cells and check for leftover text"
}
```

## Tool (2026-10-21T04:09:37)

```
| TCD-02-03 | A hover preview, if any, is not kept after the pointer leaves. | Q-36 |
| TCD-08-02 | "Your review" has no character restriction (accented, non-Latin, emoji allowed). | Q-37 |
| TCD-34-03 | Entered values stay in the form after a rejected Submit. | Q-38 |
---
grep exit: 1
```

## AI (2026-10-21T04:09:41)

I fixed the 3 Question ID cells, and there is no "to be added" or "new question needed" text left anywhere in `runs/run-1/test-design.md`.

**What changed:** only the Question ID cell on each of these lines in the "Assumptions to confirm" table.
- Line 521, TCD-02-03: "New, to be added to Q-16" is now Q-36.
- Line 523, TCD-08-02: "New, to be added to Q-15" is now Q-37.
- Line 528, TCD-34-03: "New, to be added to Q-19" is now Q-38.

**Check:** a case-insensitive search of the whole file for "to be added" and "new question needed" found no matches.

The six new questions, Q-33 to Q-38, are in `clarification-questions.md`. `test-design.md` now points to them in the 7 condition notes and in these 3 table cells.

## Tool (2026-10-21T04:09:42)

```
{"success":true,"message":"Report delivered to your caller."}
```
