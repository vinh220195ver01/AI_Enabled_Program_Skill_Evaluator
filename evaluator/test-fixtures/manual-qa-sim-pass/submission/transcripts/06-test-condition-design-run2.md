# Transcript 06: test-condition-design (run2)

Exported from the agent session log. Kept verbatim: the trainee's messages, the AI's replies, tool calls and tool results. Left out: harness reminders and private thinking. The harness prefix in front of follow-up messages is removed; the AI's final report is shown as an AI reply.

## Trainee (2026-10-21T04:29:41)

hey, second run of my test design skill to check it's consistent. skill: evaluator/test-fixtures/manual-qa-sim-pass/submission/skills/test-condition-design/SKILL.md (read and follow it).

input TR list: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-requirements.xlsx
questions (no PO answers): evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/clarification-questions.md
knowledge: evaluator/test-fixtures/manual-qa-sim-pass/submission/knowledge
output folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-2

don't read runs/run-1/test-design.md, I want an independent run. only these files + the exam folder (evaluator/test-fixtures/manual-qa-sim-pass/exam), nothing else under test-fixtures. tell me what you wrote, number of conditions, techniques used.

## AI (2026-10-21T04:29:47)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\skills\\test-condition-design\\SKILL.md"
}
```

## Tool (2026-10-21T04:29:47)

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

## AI (2026-10-21T04:29:47)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && find submission/knowledge submission/skills exam submission/runs -type f | sort",
  "description": "List knowledge, skills, exam, and runs files"
}
```

## Tool (2026-10-21T04:29:49)

```
exam/User Story for My Shop.docx
exam/app-note.md
exam/app/app.js
exam/app/index.html
exam/app/styles.css
exam/mockup-1.png
exam/mockup-2.png
exam/user-story.md
submission/knowledge/environment.md
submission/knowledge/glossary.md
submission/knowledge/index.md
submission/knowledge/product-review-rules.md
submission/knowledge/screens-and-fields.md
submission/runs/run-1/ai-original/clarification-questions.md
submission/runs/run-1/ai-original/test-cases.xlsx
submission/runs/run-1/ai-original/test-data.xlsx
submission/runs/run-1/ai-original/test-design.md
submission/runs/run-1/ai-original/test-requirements.xlsx
submission/runs/run-1/clarification-questions.md
submission/runs/run-1/test-cases.xlsx
submission/runs/run-1/test-data.xlsx
submission/runs/run-1/test-design.md
submission/runs/run-1/test-requirements.xlsx
submission/skills/defect-analysis-reporting/SKILL.md
submission/skills/defect-analysis-reporting/assets/bug-list-template.xlsx
submission/skills/defect-analysis-reporting/assets/defect-analysis-template.md
submission/skills/defect-analysis-reporting/references/bug-report-rules.md
submission/skills/defect-analysis-reporting/references/severity-priority-guide.md
submission/skills/test-case-generation/SKILL.md
submission/skills/test-case-generation/assets/test-case-template.xlsx
submission/skills/test-case-generation/references/tc-writing-rules.md
submission/skills/test-condition-design/SKILL.md
submission/skills/test-condition-design/assets/test-design-template.md
submission/skills/test-condition-design/references/coverage-checklist.md
submission/skills/test-condition-design/references/test-design-techniques.md
submission/skills/test-data-generation/SKILL.md
submission/skills/test-data-generation/assets/test-data-template.xlsx
submission/skills/test-data-generation/references/test-data-rules.md
submission/skills/test-requirements-analysis/SKILL.md
submission/skills/test-requirements-analysis/assets/clarification-questions-template.md
submission/skills/test-requirements-analysis/assets/test-requirement-template.xlsx
submission/skills/test-requirements-analysis/references/ambiguity-checklist.md
submission/skills/test-requirements-analysis/references/note-tags.md
submission/skills/test-requirements-analysis/references/tr-writing-rules.md
```

## AI (2026-10-21T04:29:52)

**Tool call `Bash`:**

```json
{
  "command": "for f in skills/test-condition-design/references/test-design-techniques.md skills/test-condition-design/references/coverage-checklist.md skills/test-condition-design/assets/test-design-template.md skills/test-requirements-analysis/references/note-tags.md knowledge/index.md; do echo \"=== $f\"; cat \"$f\"; done",
  "description": "Read skill references, template, and knowledge index"
}
```

## Tool (2026-10-21T04:29:55)

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
```

## AI (2026-10-21T04:29:58)

**Tool call `Bash`:**

```json
{
  "command": "for f in knowledge/product-review-rules.md knowledge/screens-and-fields.md knowledge/glossary.md runs/run-1/clarification-questions.md; do echo \"=== $f\"; cat \"$f\"; done",
  "description": "Read knowledge files and clarification questions"
}
```

## Tool (2026-10-21T04:30:02)

```
=== knowledge/product-review-rules.md
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
=== knowledge/screens-and-fields.md
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
=== knowledge/glossary.md
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
| Q-33 | AC-GEN | Cancelled or refunded orders | If the customer's order of this product was cancelled or refunded, may they still submit a review? If not, should the form be hidden, disabled, or rejected on Submit with a message? | Same area as Q-01: changes who may review. Risk of reviews from customers who never received the product. |

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
| Q-34 | AC-GEN | Keyboard use | Must the star rating and the whole form (fields, checkbox, Submit) be usable with the keyboard alone, and in which focus order? | The rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen. |
| Q-35 | AC-03 | Line breaks in a displayed review | If "Your review" is written on several lines, should the line breaks be kept when the review is shown on the product page? | Line breaks are shown as entered. |
| Q-36 | AC-01 | Star hover preview | When the pointer moves over the stars without clicking, may the stars show a preview, and must the selected rating come back when the pointer leaves? | A hover preview, if any, is not kept; the selected rating is unchanged after the pointer leaves. |
| Q-37 | AC-02 | Characters allowed in "Your review" | Are all characters allowed in "Your review" (accented and non-Latin letters, digits, punctuation, emoji), or are some blocked? | No character restriction in "Your review". |
| Q-38 | AC-GEN | Values after a rejected submit | After Submit is rejected because of an error, should the values already entered stay in the form? | Entered values stay in the form after a rejected Submit. |

## Conflicts between sources

| Q ID | Source A says | Source B says |
|---|---|---|
| Q-02 | exam/user-story.md: "As a customer, I want to submit a review for a product I purchased" (the reviewer is a known buyer) | exam/mockup-1.png: the form asks the reviewer to type "Name *" and "Email *" by hand, as for a guest |
| Q-13 | exam/mockup-1.png, checkbox: "Save my name, email, and website in this browser for the next time I comment." | exam/mockup-1.png, form: only "Your rating *", "Your review *", "Name *" and "Email *"; there is no Website field |
```

## AI (2026-10-21T04:30:06)

**Tool call `Bash`:**

```json
{
  "command": "python -I -c \"\nimport openpyxl,sys\nwb=openpyxl.load_workbook('runs/run-1/test-requirements.xlsx',data_only=True)\nfor ws in wb:\n  print('### SHEET',ws.title,ws.dimensions)\n  for r in ws.iter_rows(values_only=True):\n    if any(c is not None for c in r): print(' | '.join('' if c is None else str(c) for c in r))\n\"",
  "description": "Dump test requirements workbook contents"
}
```

## Tool (2026-10-21T04:30:08)

```
### SHEET Test Requirements A1:E42
AC ID | Acceptance Criteria | TR ID | Test Requirements | Notes
AC-01 | Allow customers to enter a star rating | TR-01 | Verify that the "Your rating *" field shows 5 stars. | 
AC-01 | Allow customers to enter a star rating | TR-02 | Verify that the customer can select a rating by clicking a star, and the selected stars are shown as selected. | Assumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.
Missing info: whether half stars are allowed (Q-03).
AC-01 | Allow customers to enter a star rating | TR-03 | Verify that both the lowest rating (1 star) and the highest rating (5 stars) can be selected and are saved with the review. | Edge case: lowest and highest rating.
Assumption: rating range 1 to 5 until Q-03 is answered.
AC-01 | Allow customers to enter a star rating | TR-04 | Verify that the customer can change the selected rating before submitting, and only the last selected rating is saved. | Assumption: clicking another star changes the rating; it cannot be cleared to no rating (Q-16).
AC-01 | Allow customers to enter a star rating | TR-05 | Verify that the review cannot be submitted when no star rating is selected. | Assumption: an error message names the rating field; wording checked for meaning, not exact text (Q-20).
AC-02 | Provide a text box for review comments | TR-06 | Verify that a multi-line text box "Your review *" is provided for the review comment. | 
AC-02 | Provide a text box for review comments | TR-07 | Verify that the review cannot be submitted when "Your review" is empty. | 
AC-02 | Provide a text box for review comments | TR-08 | Verify that review text within the allowed length is accepted and saved as entered. | Missing info: minimum and maximum length not stated (Q-04).
AC-02 | Provide a text box for review comments | TR-09 | Verify that review text of exactly the minimum length and exactly the maximum length is accepted. | Edge case: values exactly at the minimum and the maximum.
Missing info: minimum and maximum length not stated (Q-04).
AC-02 | Provide a text box for review comments | TR-10 | Verify that review text shorter than the minimum or longer than the maximum is not accepted. | Edge case: one character below the minimum and one above the maximum.
Missing info: minimum and maximum length not stated (Q-04).
Assumption: typing and pasting stop at the maximum until Q-18 is answered.
AC-02 | Provide a text box for review comments | TR-11 | Verify that review text made only of spaces is treated as empty and the review is not submitted. | Edge case: whitespace-only input.
Assumption: spaces are trimmed and a field with only spaces counts as empty (Q-17).
AC-02 | Provide a text box for review comments | TR-12 | Verify that HTML tags, script code and links entered in "Your review" or "Name" are never run as code on the product page. | Missing info: whether such content is shown as plain text, removed or rejected (Q-15).
Assumption: content is never executed, whatever the answer to Q-15.
Risk: script injection would affect every visitor of the product page.
AC-03 | Display approved reviews on the product page | TR-13 | Verify that a newly submitted review is not displayed on the product page while it waits for approval. | Missing info: whether the author sees their own pending review (Q-08).
Risk: unmoderated content shown publicly.
AC-03 | Display approved reviews on the product page | TR-14 | Verify that a submitted review is displayed on the product page after it is approved. | Missing info: who approves and how (Q-07).
AC-03 | Display approved reviews on the product page | TR-15 | Verify that a rejected review is never displayed on the product page. | Missing info: whether a review can be rejected and what happens to it (Q-07).
AC-03 | Display approved reviews on the product page | TR-16 | Verify that the author sees their own pending review only in the way confirmed for Q-08 (marked as awaiting approval, or not at all). | Missing info: author's view of a pending review not specified (Q-08).
AC-03 | Display approved reviews on the product page | TR-17 | Verify that each displayed review shows the confirmed details (star rating, reviewer name, date, review text). | Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered.
Missing info: which details and which form of the name are shown; no mockup of the reviews list (Q-09).
Assumption: submit date in any unambiguous format (Q-24).
AC-03 | Display approved reviews on the product page | TR-18 | Verify that the star rating, name and review text of a displayed review match what the customer submitted. | 
AC-03 | Display approved reviews on the product page | TR-19 | Verify that the reviewer's email address is never displayed on the product page. | Risk: personal data could be shown publicly.
AC-03 | Display approved reviews on the product page | TR-20 | Verify that approved reviews are listed in the confirmed order. | Missing info: list order not specified (Q-10).
AC-03 | Display approved reviews on the product page | TR-21 | Verify that all approved reviews can be seen when a product has many reviews. | Edge case: large number of approved reviews.
Assumption: all approved reviews are shown on one page (Q-23).
AC-03 | Display approved reviews on the product page | TR-22 | Verify that a clear empty state is shown when the product has no approved reviews. | Edge case: product with no approved reviews.
Assumption: a short message saying there are no reviews yet (Q-25).
AC-03 | Display approved reviews on the product page | TR-23 | Verify that the average rating and review count on the product page, if shown, are calculated from approved reviews only. | Missing info: whether a summary is shown and how it is rounded (Q-11).
Risk: pending or rejected reviews could change the score shown to shoppers.
AC-03 | Display approved reviews on the product page | TR-24 | Verify that a review is displayed only on the page of the product it was written for. | Risk: reviews shown on the wrong product mislead shoppers.
AC-GEN | General: form labels and layout shown in the mockup | TR-25 | Verify that the review form shows the heading, the info text "Your email address will not be published. Required fields are marked *", the fields "Your rating *", "Your review *", "Name *", "Email *", the save checkbox and the "Submit" button as in mockup-1. | Assumption: the heading "ADD A REVIEW" is compared without regard to letter case (Q-32).
Missing info: final text of the save checkbox (Q-13).
AC-GEN | General: who may review (story: "a product I purchased") | TR-26 | Verify that only a customer who is allowed to review (as confirmed for Q-01) can submit a review, and a customer who is not allowed cannot. | Missing info: sign-in and purchase check not specified (Q-01).
Risk: guests or non-buyers could post fake reviews.
AC-GEN | General: Name and Email for a known customer (story vs mockup) | TR-27 | Verify that Name and Email for a signed-in customer are handled as confirmed for Q-02 (prefilled, editable or not shown). | Missing info: conflict between the story and mockup-1 (Q-02).
AC-GEN | General: form fields shown in the mockup | TR-28 | Verify that the review cannot be submitted when "Name" is empty. | 
AC-GEN | General: form fields shown in the mockup | TR-29 | Verify that a Name within the allowed length and characters is accepted, and a Name outside them is rejected. | Missing info: maximum length and allowed characters not stated (Q-05).
Edge case: Name at the maximum length and with accented letters, hyphens or apostrophes.
AC-GEN | General: form fields shown in the mockup | TR-30 | Verify that the review cannot be submitted when "Email" is empty. | 
AC-GEN | General: form fields shown in the mockup | TR-31 | Verify that a correctly formatted email is accepted and an incorrectly formatted email is rejected. | Missing info: email format rule and maximum length not stated (Q-06).
AC-GEN | General: form fields shown in the mockup | TR-32 | Verify that leading and trailing spaces in Name and Email are removed, and a Name or Email made only of spaces counts as empty. | Edge case: whitespace-only and space-padded input.
Assumption: spaces are trimmed and a field with only spaces counts as empty (Q-17).
AC-GEN | General: submitting the review form | TR-33 | Verify that when all required fields are valid, the review is submitted and a confirmation message is shown. | Assumption: the confirmation says the review was received and waits for approval (Q-21).
AC-GEN | General: submitting the review form | TR-34 | Verify that when a required field is empty or invalid, the review is not submitted and an error message names each field concerned. | Assumption: fields are checked on Submit only (Q-19).
Assumption: wording checked for meaning, not exact text (Q-20).
AC-GEN | General: submitting the review form | TR-35 | Verify that after a successful submit the customer stays on the product page and the form is cleared. | Assumption: form cleared; Name and Email stay filled only if the save checkbox was ticked (Q-22).
AC-GEN | General: save checkbox shown in the mockup | TR-36 | Verify that the "Save my name, email, and website..." checkbox is unchecked by default. | 
AC-GEN | General: save checkbox shown in the mockup | TR-37 | Verify that when the save checkbox is ticked at submit, the name and email are filled in again on the next visit in the same browser. | Assumption: only name and email are saved until Q-13 and Q-14 are answered.
Missing info: what is saved, where and for how long (Q-14); "website" with no Website field (Q-13).
Risk: personal data stored on the device.
AC-GEN | General: save checkbox shown in the mockup | TR-38 | Verify that when the save checkbox is not ticked, no name or email is kept for the next visit. | Missing info: what is saved when the checkbox is not ticked (Q-14).
Risk: personal data left on a shared device.
AC-GEN | General: reviews per customer and product (story as a whole) | TR-39 | Verify that a customer cannot submit more reviews for the same product than the confirmed limit. | Missing info: number of reviews per customer and product not specified (Q-12).
AC-GEN | General: submitting the review form | TR-40 | Verify that clicking Submit more than once quickly creates only one review. | Edge case: rapid double click.
Assumption: only one review is created (Q-28).
Risk: duplicate reviews distort the rating.
AC-GEN | General: submitting the review form | TR-41 | Verify that when the review cannot be saved (server or network error), the customer is told and the entered data is kept. | Assumption: an error message is shown and the entered data is kept (Q-29).
```

## AI (2026-10-21T04:30:12)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/exam && cat user-story.md; echo ======; cat app-note.md",
  "description": "Read exam user story and app note"
}
```

## Tool (2026-10-21T04:30:14)

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
======
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

## AI (2026-10-21T04:30:16)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\exam\\mockup-1.png"
}
```

## Tool (2026-10-21T04:30:17)

```
[image]
```

## AI (2026-10-21T04:32:37)

**Tool call `mcp__ccd_turn__update_plan`:**

```json
{
  "items": [
    {
      "content": "Read skill, references, TR list, questions, knowledge",
      "status": "completed"
    },
    {
      "content": "Derive conditions per TR with techniques",
      "status": "in_progress"
    },
    {
      "content": "Write run-2/test-design.md from template",
      "status": "pending"
    },
    {
      "content": "Verify coverage, IDs, duplicates",
      "status": "pending"
    }
  ],
  "scope": "first_task"
}
```

## Tool (2026-10-21T04:32:37)

```
PreToolUse:mcp__ccd_turn__update_plan hook error: Not shown: you are a subagent, and the app shows only the main conversation's task list and wrap-up. Do not call update_plan or wrap_up again; carry on with your task and report your result as usual.
```

## AI (2026-10-21T04:35:16)

**Tool call `Write`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\runs\\run-2\\test-design.md",
  "content": "# Test design: US-VP02 Submit a Product Review\n\nInput: runs/run-1/test-requirements.xlsx (41 TRs, TR-01 to TR-41) · Answers used: none (runs/run-1/clarification-questions.md read for question IDs and working assumptions; no product owner answers received) · Date: 2026-10-21\n\nKnowledge read: knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md; exam/user-story.md, exam/mockup-1.png, exam/app-note.md. The demo build is the product under test and is never used as a source of expected results.\n\nPositive / Negative: Positive = a valid input or allowed flow that must succeed. Negative = an invalid input, a forbidden action, or an outcome that must not happen.\n\nPlaceholders used where no source gives the value (not invented): REVIEW_MIN, REVIEW_MAX (Q-04), NAME_MAX (Q-05), EMAIL_MAX (Q-06), LIMIT (Q-12), PAGE_SIZE (Q-23). Each condition that uses one carries a Missing info note.\n\n## Values and rules used\n\n| Item | Value | Status (Confirmed / Assumption) | Source |\n|---|---|---|---|\n| Number of stars in \"Your rating *\" | 5 | Confirmed | mockup-1.png (R6) |\n| Rating values | Whole number 1 to 5, one per star; no half stars | Assumption | product-review-rules.md A1; Q-03 |\n| Changing / clearing the rating | Clicking another star changes the rating; it cannot be cleared to no rating except by reloading | Assumption | Q-16 |\n| Hover over stars | A hover preview, if any, is not kept | Assumption | Q-36 |\n| Required fields | Your rating, Your review, Name, Email (marked *) | Confirmed | mockup-1.png (R2) |\n| \"Your review\" control | Multi-line text box | Confirmed | mockup-1.png, AC-02 |\n| \"Your review\" minimum and maximum length | Not stated (REVIEW_MIN, REVIEW_MAX). Demo build shows \"0 / 500\" counter: Observed only, not a requirement | Missing info | Q-04; screens-and-fields.md F2 |\n| Text longer than the maximum | Typing and pasting stop at the maximum | Assumption | Q-18 |\n| Characters allowed in \"Your review\" | No restriction (accented, non-Latin, digits, punctuation, emoji) | Assumption | Q-37 |\n| Line breaks in a displayed review | Shown as entered | Assumption | Q-35 |\n| Leading / trailing spaces, whitespace-only fields | Trimmed; a field with only spaces counts as empty | Assumption | Q-17 |\n| \"Name\" length and allowed characters | Not stated (NAME_MAX); minimum length not stated and not asked by any question | Missing info | Q-05 |\n| \"Email\" format rule and maximum length | Not stated (EMAIL_MAX) | Missing info | Q-06 |\n| When fields are validated | On Submit only | Assumption | Q-19 |\n| Error messages | Each error names the field concerned; wording checked for meaning, not exact text | Assumption | Q-20 |\n| Values after a rejected Submit | Entered values stay in the form | Assumption | Q-38 |\n| Success message | Says the review was received and waits for approval | Assumption | Q-21 |\n| Form after a successful Submit | Customer stays on the product page; form cleared; Name and Email stay filled only if the save checkbox was ticked | Assumption | Q-22 |\n| Double Submit | Only one review is created | Assumption | Q-28 |\n| Save failure (server, network, session) | A message says the review was not submitted; entered data kept | Assumption | Q-29 |\n| Email publication | The email address is not published | Confirmed | mockup-1.png (R3) |\n| What is displayed on the product page | Only approved reviews | Confirmed | AC-03 (R4) |\n| Review life cycle | New review is pending until approved | Confirmed (derived) | AC-03 (R5); app-note.md |\n| Approval in the demo build | \"Moderator: approve pending reviews\" approves every pending review | Confirmed (test environment only) | app-note.md |\n| Who approves, rejection possible | Not stated | Missing info | Q-07 |\n| Author's view of a pending review | Not stated | Missing info | Q-08 |\n| Details shown per review | Star rating, reviewer name, date, review text; never email | Assumption | product-review-rules.md A2; Q-09 |\n| Date shown | Submit date, any unambiguous format | Assumption | Q-24 |\n| Order of reviews | Not stated | Missing info | Q-10 |\n| Number of reviews shown | All approved reviews on one page | Assumption | Q-23 |\n| Product with no approved reviews | A short message saying there are no reviews yet | Assumption | Q-25 |\n| Rating summary and review count | Whether shown, calculation and rounding not stated | Missing info | Q-11 |\n| Who may submit | Sign-in and purchase check not stated; cancelled / refunded orders not stated | Missing info | Q-01, Q-33 |\n| Name and Email for a signed-in customer | Conflict between story and mockup-1 | Missing info | Q-02 |\n| Heading \"ADD A REVIEW\" | Compared without regard to letter case | Assumption | Q-32 |\n| Save checkbox default | Unchecked | Confirmed | mockup-1.png (F5) |\n| Save checkbox text | Mentions \"website\" but there is no Website field | Missing info | Q-13 |\n| What the save checkbox stores | Only Name and Email; nothing when not ticked | Assumption | Q-13, Q-14 |\n| Reviews per customer and product | Not stated (LIMIT) | Missing info | Q-12 |\n| HTML, scripts, links in text | Display treatment not stated; content is never executed | Missing info (display) / Assumption (never executed) | Q-15; TR-12 |\n| Keyboard use | Rating, fields, checkbox and Submit usable by keyboard; Tab follows screen order | Assumption | Q-34 |\n| Browser and language | Desktop Chrome, English | Assumption (Chrome Confirmed for the demo environment) | Q-31; app-note.md |\n| Demo build data | One product; reload restores initial data; only the save-checkbox choice is kept | Confirmed (test environment only) | app-note.md |\n\n## Test conditions\n\n### TR-01: Verify that the \"Your rating *\" field shows 5 stars.\n\nTechnique(s): Equivalence Partitioning - the control has one valid display state on first open (5 stars, none selected); the count limit itself is tested by BVA in TR-03.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-01-01 | EP | On first opening the product page, \"Your rating *\" shows exactly 5 star icons and none is selected. | Positive | |\n\n### TR-02: Verify that the customer can select a rating by clicking a star, and the selected stars are shown as selected.\n\nTechnique(s): Equivalence Partitioning - whole-star values form one valid partition (one representative), half-star input is a separate partition; Error guessing - hover and keyboard use are common defect sources on star widgets.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-02-01 | EP | Clicking the 3rd star selects a rating of 3: stars 1 to 3 are shown as selected and stars 4 and 5 as not selected. | Positive | Assumption: whole number 1 to 5, one per star (Q-03). |\n| TCD-02-02 | EP | Clicking on the left half of a star selects a whole star only (no half-star value such as 2.5). | Negative | Missing info: whether half stars are allowed (Q-03). |\n| TCD-02-03 | Error guessing | Moving the pointer over the stars after a rating is selected, then away without clicking, leaves the selected rating unchanged. | Negative | Assumption: a hover preview is not kept (Q-36). |\n| TCD-02-04 | Error guessing | The rating can be selected with the keyboard only (Tab to the stars, then arrow keys / Enter / Space). | Positive | Assumption: rating usable with the keyboard (Q-34). |\n\n### TR-03: Verify that both the lowest rating (1 star) and the highest rating (5 stars) can be selected and are saved with the review.\n\nTechnique(s): Boundary Value Analysis - the rating is a range 1 to 5; 3-value BVA on both ends. The value just below the lower boundary (0 = no rating) is TCD-05-01.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-03-01 | BVA | Rating 1 (on the lower boundary) is selected, submitted, and shown as 1 star after approval. | Positive | Edge case: lowest rating.<br>Assumption: range 1 to 5 (Q-03). |\n| TCD-03-02 | BVA | Rating 2 (just above the lower boundary) is selected, submitted, and shown as 2 stars after approval. | Positive | Assumption: range 1 to 5 (Q-03). |\n| TCD-03-03 | BVA | Rating 4 (just below the upper boundary) is selected, submitted, and shown as 4 stars after approval. | Positive | Assumption: range 1 to 5 (Q-03). |\n| TCD-03-04 | BVA | Rating 5 (on the upper boundary) is selected, submitted, and shown as 5 stars after approval. | Positive | Edge case: highest rating.<br>Assumption: range 1 to 5 (Q-03). |\n| TCD-03-05 | BVA | A rating of 6 (just above the upper boundary) cannot be selected: with 5 stars selected, pressing the right arrow key or clicking just right of the 5th star keeps the rating at 5. | Negative | Edge case: value above the maximum.<br>Assumption: range 1 to 5 (Q-03). |\n\n### TR-04: Verify that the customer can change the selected rating before submitting, and only the last selected rating is saved.\n\nTechnique(s): State transition - the rating control moves between \"no rating\" and \"n stars\"; each valid change and the invalid \"clear by clicking again\" event are covered; Error guessing - reload as the only reset.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-04-01 | State transition | No rating -> 4 stars -> 2 stars (change to a lower value), then Submit: the saved review has rating 2. | Positive | |\n| TCD-04-02 | State transition | 2 stars -> 5 stars (change to a higher value), then Submit: the saved review has rating 5. | Positive | |\n| TCD-04-03 | State transition | Clicking the already selected star again does not clear the rating back to \"no rating\". | Negative | Assumption: the rating cannot be cleared by clicking (Q-16). |\n| TCD-04-04 | Error guessing | After selecting a rating, reloading the page returns the control to \"no rating\". | Positive | Assumption: reload is the only way to clear the rating (Q-16). |\n\n### TR-05: Verify that the review cannot be submitted when no star rating is selected.\n\nTechnique(s): Equivalence Partitioning - \"no rating\" is the invalid partition of a required field; it is also the value just below the lower boundary (0) of TR-03.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-05-01 | EP / BVA | No star selected (rating 0), all other fields valid: the review is not submitted and an error names the rating field. | Negative | Edge case: just below the lower boundary 1.<br>Assumption: error names the field; wording checked for meaning (Q-20). |\n\n### TR-06: Verify that a multi-line text box \"Your review *\" is provided for the review comment.\n\nTechnique(s): Equivalence Partitioning - single-line and multi-line text are separate input partitions; Error guessing - line breaks are often lost when text is displayed.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-06-01 | EP | Pressing Enter inside \"Your review\" adds a new line and does not submit the form. | Positive | |\n| TCD-06-02 | Error guessing | A review written on several lines keeps its line breaks when displayed on the product page after approval. | Positive | Assumption: line breaks shown as entered (Q-35). |\n\n### TR-07: Verify that the review cannot be submitted when \"Your review\" is empty.\n\nTechnique(s): Equivalence Partitioning - empty is the invalid partition of a required field.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-07-01 | EP | \"Your review\" empty (0 characters), all other fields valid: the review is not submitted and an error names \"Your review\". | Negative | Assumption: error names the field; wording checked for meaning (Q-20). |\n\n### TR-08: Verify that review text within the allowed length is accepted and saved as entered.\n\nTechnique(s): Equivalence Partitioning - one representative of the valid length partition and of the valid character partition; Error guessing - pasted text and padded text.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-08-01 | EP | A review of ordinary length (between REVIEW_MIN and REVIEW_MAX, for example one sentence) is accepted and saved exactly as entered. | Positive | Missing info: minimum and maximum length not stated (Q-04). |\n| TCD-08-02 | EP | A review containing accented and non-Latin letters, digits, punctuation and emoji is accepted and displayed exactly as entered. | Positive | Assumption: no character restriction (Q-37). |\n| TCD-08-03 | Error guessing | A review pasted from the clipboard (within the limit) is accepted the same way as typed text. | Positive | |\n| TCD-08-04 | Error guessing | A review with leading and trailing spaces is accepted and saved without those spaces. | Positive | Assumption: spaces are trimmed (Q-17). |\n\n### TR-09: Verify that review text of exactly the minimum length and exactly the maximum length is accepted.\n\nTechnique(s): Boundary Value Analysis - length limits; values on and just inside each boundary.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-09-01 | BVA | A review of exactly REVIEW_MIN characters is accepted. | Positive | Edge case: on the minimum.<br>Missing info: minimum length not stated (Q-04). |\n| TCD-09-02 | BVA | A review of REVIEW_MIN + 1 characters is accepted. | Positive | Missing info: minimum length not stated (Q-04). |\n| TCD-09-03 | BVA | A review of REVIEW_MAX - 1 characters is accepted. | Positive | Missing info: maximum length not stated (Q-04). |\n| TCD-09-04 | BVA | A review of exactly REVIEW_MAX characters is accepted and displayed in full after approval (not cut). | Positive | Edge case: on the maximum.<br>Missing info: maximum length not stated (Q-04). |\n\n### TR-10: Verify that review text shorter than the minimum or longer than the maximum is not accepted.\n\nTechnique(s): Boundary Value Analysis - values just outside each length limit; Error guessing - pasted and very long text.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-10-01 | BVA | A review of REVIEW_MIN - 1 characters is not accepted and an error names \"Your review\". | Negative | Edge case: just below the minimum.<br>Missing info: minimum length not stated (Q-04). If REVIEW_MIN is 1, this value is the empty case TCD-07-01 and this condition is dropped. |\n| TCD-10-02 | BVA | Typing REVIEW_MAX + 1 characters: the box stops at REVIEW_MAX characters. | Negative | Edge case: just above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: typing stops at the maximum (Q-18). |\n| TCD-10-03 | BVA | Pasting a text of REVIEW_MAX + 1 characters: the box keeps only REVIEW_MAX characters, or Submit is rejected with an error. | Negative | Edge case: just above the maximum by paste.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |\n| TCD-10-04 | Error guessing | Pasting a very long text (about 10 x REVIEW_MAX characters) does not freeze the page and is handled as in TCD-10-03. | Negative | Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |\n\n### TR-11: Verify that review text made only of spaces is treated as empty and the review is not submitted.\n\nTechnique(s): Equivalence Partitioning - whitespace-only text is an invalid partition separate from empty text; Error guessing - other whitespace characters.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-11-01 | EP | \"Your review\" containing only spaces is treated as empty: the review is not submitted and an error names \"Your review\". | Negative | Edge case: whitespace-only input.<br>Assumption: a field with only spaces counts as empty (Q-17). |\n| TCD-11-02 | Error guessing | \"Your review\" containing only line breaks (Enter pressed several times) is treated as empty and not submitted. | Negative | Edge case: whitespace-only input.<br>Assumption: line breaks are treated like spaces for this rule (Q-17). |\n\n### TR-12: Verify that HTML tags, script code and links entered in \"Your review\" or \"Name\" are never run as code on the product page.\n\nTechnique(s): Error guessing - script injection, HTML and link text are known defect sources wherever user text is displayed.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-12-01 | Error guessing | A review containing a script tag (for example `<script>alert(1)</script>`) does not run any script when the approved review is displayed. | Negative | Risk: script injection affects every visitor of the product page.<br>Missing info: shown as plain text, removed or rejected (Q-15). |\n| TCD-12-02 | Error guessing | A review containing an HTML event attribute (for example `<img src=x onerror=alert(1)>`) does not run any script when displayed. | Negative | Risk: script injection.<br>Missing info: display treatment (Q-15). |\n| TCD-12-03 | Error guessing | A Name containing script code does not run any script where the reviewer name is displayed. | Negative | Risk: script injection.<br>Missing info: display treatment (Q-15). |\n| TCD-12-04 | Error guessing | A review containing formatting tags (for example `<b>`, `<h1>`) does not change the layout or formatting of the product page. | Negative | Missing info: shown as plain text, removed or rejected (Q-15). |\n| TCD-12-05 | Error guessing | A review containing a web link (https://...) is handled as confirmed for Q-15 (plain text, removed or rejected). | Negative | Missing info: link handling not stated (Q-15). |\n\n### TR-13: Verify that a newly submitted review is not displayed on the product page while it waits for approval.\n\nTechnique(s): State transition - review life cycle (none -> Pending -> Approved / Rejected); covers the valid \"Submit\" transition and the invalid \"Pending -> displayed without approval\".\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-13-01 | State transition | Valid Submit moves the review to Pending: it is not added to the reviews list and the \"Reviews (n)\" count does not change. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: whether the author sees their own pending review (Q-08); this condition checks the public list. |\n| TCD-13-02 | State transition | Invalid transition Pending -> displayed without an approval event: after further actions on the page (another review submitted, page scrolled, form reused), the pending review is still not displayed. | Negative | Risk: unmoderated content shown publicly. |\n\n### TR-14: Verify that a submitted review is displayed on the product page after it is approved.\n\nTechnique(s): State transition - the \"Approve\" event from Pending to Approved, and the invalid repeat of that event.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-14-01 | State transition | Pending -> Approved: after approval, the review appears in the reviews list. | Positive | Missing info: who approves and how (Q-07); in the demo build approval is done with \"Moderator: approve pending reviews\" (app-note.md). |\n| TCD-14-02 | State transition | Two pending reviews approved together both appear, each exactly once. | Positive | Missing info: approval process (Q-07). |\n| TCD-14-03 | State transition | Invalid event: approving again when nothing is pending adds no review and does not duplicate already approved reviews. | Negative | Edge case: repeated approval. |\n\n### TR-15: Verify that a rejected review is never displayed on the product page.\n\nTechnique(s): State transition - the \"Reject\" event from Pending to Rejected, and the invalid transition Rejected -> displayed.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-15-01 | State transition | Pending -> Rejected: a rejected review is not displayed on the product page. | Negative | Missing info: whether a review can be rejected and what happens to it (Q-07). The demo build has no reject action. |\n| TCD-15-02 | State transition | Invalid transition Rejected -> Approved: a later approval of other pending reviews does not display the rejected review. | Negative | Missing info: rejection workflow (Q-07). |\n\n### TR-16: Verify that the author sees their own pending review only in the way confirmed for Q-08 (marked as awaiting approval, or not at all).\n\nTechnique(s): Equivalence Partitioning - two viewer partitions (the author, any other visitor) for a Pending review.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-16-01 | EP | Right after Submit, the author sees their own pending review as confirmed for Q-08 (marked as awaiting approval, or not shown). | Positive | Missing info: author's view of a pending review (Q-08). |\n| TCD-16-02 | EP | Another visitor (different browser or account) does not see the author's pending review, even if the author does. | Negative | Risk: unmoderated content shown publicly.<br>Missing info: author's view (Q-08). Needs an environment with shared stored data; the demo build keeps data per page load (app-note.md). |\n\n### TR-17: Verify that each displayed review shows the confirmed details (star rating, reviewer name, date, review text).\n\nTechnique(s): Equivalence Partitioning - one approved review is the valid partition; the name form is a partition decided by Q-09.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-17-01 | EP | An approved review shows its star rating, reviewer name, date and review text. | Positive | Assumption: these four details are shown (Q-09). |\n| TCD-17-02 | EP | The date shown for a review submitted today is today's date, in an unambiguous format. | Positive | Assumption: submit date, any unambiguous format (Q-24). |\n| TCD-17-03 | EP | The reviewer name is shown in the form confirmed for Q-09 (full name, first name only or initials). | Positive | Missing info: form of the name (Q-09). |\n\n### TR-18: Verify that the star rating, name and review text of a displayed review match what the customer submitted.\n\nTechnique(s): Equivalence Partitioning - one representative submitted review; Error guessing - special characters shown as codes and data mixed between reviews.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-18-01 | EP | After approval, the displayed rating, name and review text are identical to the submitted values (case, punctuation, spelling). | Positive | |\n| TCD-18-02 | Error guessing | A review and name containing `& < > \" '` are displayed with those characters, not as codes such as `&amp;`. | Positive | Edge case: characters that are often escaped twice. |\n| TCD-18-03 | Error guessing | Two reviews with different ratings, names and texts, submitted one after the other and approved together, each keep their own values (no mix-up). | Positive | |\n\n### TR-19: Verify that the reviewer's email address is never displayed on the product page.\n\nTechnique(s): Error guessing - places where personal data leaks unnoticed (visible text, page source, attributes).\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-19-01 | Error guessing | After approval, the reviewer's email address appears nowhere in the visible product page (review, author line, tooltips, success message area). | Negative | Risk: personal data shown publicly.<br>Confirmed: email not published (mockup-1.png). |\n| TCD-19-02 | Error guessing | The reviewer's email address is not present in the page source of the product page (hidden fields, attributes, links such as `mailto:`). | Negative | Risk: personal data exposed to anyone who views the source. |\n\n### TR-20: Verify that approved reviews are listed in the confirmed order.\n\nTechnique(s): Equivalence Partitioning - a set of reviews that differ in date and rating, so that any ordering rule gives a visible result; Error guessing - placement of a newly approved review.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-20-01 | EP | With at least 3 approved reviews that differ in date and rating, the list follows the order confirmed for Q-10. | Positive | Missing info: list order not specified (Q-10). |\n| TCD-20-02 | Error guessing | A newly approved review is placed in the correct position among the existing reviews (not always at the end). | Positive | Missing info: list order not specified (Q-10). |\n\n### TR-21: Verify that all approved reviews can be seen when a product has many reviews.\n\nTechnique(s): Equivalence Partitioning - \"many reviews\" partition; Boundary Value Analysis - page size, only if paging is confirmed.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-21-01 | EP | With many approved reviews (20 or more), every approved review is visible on the page and the \"Reviews (n)\" count equals the number listed. | Positive | Edge case: large number of reviews.<br>Assumption: all approved reviews on one page (Q-23). |\n| TCD-21-02 | BVA | If paging is confirmed: PAGE_SIZE reviews show on one page with no paging control; PAGE_SIZE + 1 reviews show paging or \"Load more\" and the extra review is reachable. | Positive | Missing info: page size, only if Q-23 confirms paging; dropped if all reviews are on one page. |\n\n### TR-22: Verify that a clear empty state is shown when the product has no approved reviews.\n\nTechnique(s): Boundary Value Analysis - approved review count 0 and 1; State transition - a pending review must not leave the empty state.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-22-01 | BVA | 0 approved reviews: a message says there are no reviews yet, and the count shows 0. | Positive | Edge case: no approved reviews.<br>Assumption: short \"no reviews yet\" message (Q-25). |\n| TCD-22-02 | BVA | 1 approved review (0 -> 1): the empty-state message is gone, one review is listed and the count shows 1. | Positive | Edge case: first approved review. |\n| TCD-22-03 | State transition | 0 approved and 1 pending review: the empty-state message is still shown and the count still shows 0. | Negative | Risk: pending content counted publicly. |\n\n### TR-23: Verify that the average rating and review count on the product page, if shown, are calculated from approved reviews only.\n\nTechnique(s): State transition - summary before and after the Pending -> Approved event; Error guessing - averages after a change, rounding and division by zero.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-23-01 | Error guessing | With approved ratings 5 and 4, the summary shows average 4.5 and count 2. | Positive | Missing info: whether a summary is shown and how it is rounded (Q-11). |\n| TCD-23-02 | State transition | A new 1-star review in Pending does not change the average or the count. | Negative | Risk: pending reviews change the score shown to shoppers.<br>Missing info: summary rule (Q-11). |\n| TCD-23-03 | State transition | After that review is approved, the average and count are recalculated to include it. | Positive | Missing info: summary rule (Q-11). |\n| TCD-23-04 | Error guessing | Approved ratings 5, 4, 4 (average 4.333...) are displayed with the confirmed rounding. | Positive | Edge case: repeating decimal.<br>Missing info: rounding not specified (Q-11). |\n| TCD-23-05 | Error guessing | With 0 approved reviews, the summary shows no rating / 0 reviews without an error value (for example \"NaN\"). | Negative | Edge case: average of zero reviews.<br>Missing info: summary rule (Q-11). |\n\n### TR-24: Verify that a review is displayed only on the page of the product it was written for.\n\nTechnique(s): Equivalence Partitioning - two product partitions (the reviewed product, any other product).\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-24-01 | EP | A review approved for product A is displayed on product A and not on product B. | Negative | Risk: reviews on the wrong product mislead shoppers.<br>Needs an environment with at least 2 products; the demo build has one product (app-note.md). |\n\n### TR-25: Verify that the review form shows the heading, the info text, the fields, the save checkbox and the \"Submit\" button as in mockup-1.\n\nTechnique(s): Equivalence Partitioning - the form on first open is one valid partition checked element by element against mockup-1; Error guessing - keyboard focus order.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-25-01 | EP | The heading reads \"ADD A REVIEW\". | Positive | Assumption: compared without regard to letter case (Q-32). |\n| TCD-25-02 | EP | The info text reads \"Your email address will not be published. Required fields are marked *\". | Positive | |\n| TCD-25-03 | EP | The labels \"Your rating *\", \"Your review *\", \"Name *\" and \"Email *\" are shown with the required marker, in the mockup-1 order. | Positive | |\n| TCD-25-04 | EP | The save checkbox text and the \"Submit\" button are shown below the fields as in mockup-1. | Positive | Missing info: final text of the save checkbox (Q-13). |\n| TCD-25-05 | Error guessing | Tab moves through stars, \"Your review\", \"Name\", \"Email\", checkbox and \"Submit\" in screen order, and every control can be used with the keyboard alone. | Positive | Assumption: keyboard use and focus order (Q-34). |\n\n### TR-26: Verify that only a customer who is allowed to review (as confirmed for Q-01) can submit a review, and a customer who is not allowed cannot.\n\nTechnique(s): Decision table - conditions: signed in (Y/N), bought the product (Y/N), order cancelled or refunded (Y/N); outcome: may submit / may not. Rules for a guest are collapsed into one (purchase cannot be checked without an account). Error guessing - bypassing a hidden form.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-26-01 | Decision table | Rule 1: signed in, bought the product, order not cancelled: the customer can submit a review. | Positive | Missing info: sign-in and purchase check (Q-01). |\n| TCD-26-02 | Decision table | Rule 2: signed in, did not buy the product: the form is hidden, disabled or Submit is rejected with a message, as confirmed for Q-01. | Negative | Risk: non-buyers post fake reviews.<br>Missing info: purchase check (Q-01). |\n| TCD-26-03 | Decision table | Rule 3: guest (not signed in): handled as confirmed for Q-01. | Negative | Risk: fake reviews.<br>Missing info: whether guests may review (Q-01). |\n| TCD-26-04 | Decision table | Rule 4: signed in, bought the product but the order was cancelled or refunded: handled as confirmed for Q-33. | Negative | Missing info: cancelled or refunded orders (Q-33). |\n| TCD-26-05 | Error guessing | A customer who is not allowed submits through a form left open in another tab (for example after signing out): Submit is rejected. | Negative | Risk: rule checked only on the screen, not on Submit.<br>Missing info: who may review (Q-01). |\n\n### TR-27: Verify that Name and Email for a signed-in customer are handled as confirmed for Q-02 (prefilled, editable or not shown).\n\nTechnique(s): Equivalence Partitioning - signed-in customer partition; the three possible behaviours of Q-02 decide the expected result.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-27-01 | EP | A signed-in customer opens the form: Name and Email are prefilled from the account, editable or not shown, as confirmed for Q-02. | Positive | Missing info: conflict between the story and mockup-1 (Q-02). |\n| TCD-27-02 | EP | If Name and Email are prefilled and editable, a signed-in customer who changes them gets the changed values used for the review as confirmed for Q-02. | Positive | Missing info: conflict between the story and mockup-1 (Q-02). |\n\n### TR-28: Verify that the review cannot be submitted when \"Name\" is empty.\n\nTechnique(s): Equivalence Partitioning - empty is the invalid partition of a required field.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-28-01 | EP | \"Name\" empty, all other fields valid: the review is not submitted and an error names \"Name\". | Negative | Assumption: error names the field; wording checked for meaning (Q-20). |\n\n### TR-29: Verify that a Name within the allowed length and characters is accepted, and a Name outside them is rejected.\n\nTechnique(s): Equivalence Partitioning - valid and invalid character partitions, one at a time; Boundary Value Analysis - Name length.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-29-01 | EP | A plain Latin name with a space (for example \"Anna Tran\") is accepted. | Positive | |\n| TCD-29-02 | EP | A name with accented letters, a hyphen and an apostrophe (for example \"Lê Thị-Ánh O'Neil\") is accepted as confirmed for Q-05. | Positive | Edge case: accented letters, hyphen, apostrophe.<br>Missing info: allowed characters (Q-05). |\n| TCD-29-03 | EP | A name made only of digits (for example \"12345\") is accepted or rejected as confirmed for Q-05. | Negative | Missing info: allowed characters (Q-05). |\n| TCD-29-04 | EP | A name made only of symbols (for example \"@#$%\") is accepted or rejected as confirmed for Q-05. | Negative | Missing info: allowed characters (Q-05). |\n| TCD-29-05 | BVA | A name of 1 character (just above empty) is accepted or rejected as confirmed. | Positive | Edge case: shortest name.<br>Missing info: minimum Name length not stated and not covered by any question (suggest adding to Q-05). |\n| TCD-29-06 | BVA | A name of NAME_MAX - 1 characters is accepted. | Positive | Missing info: maximum length (Q-05). |\n| TCD-29-07 | BVA | A name of exactly NAME_MAX characters is accepted and displayed in full. | Positive | Edge case: on the maximum.<br>Missing info: maximum length (Q-05). |\n| TCD-29-08 | BVA | A name of NAME_MAX + 1 characters is blocked while typing or rejected on Submit. | Negative | Edge case: just above the maximum.<br>Missing info: maximum length and over-length handling (Q-05). |\n\n### TR-30: Verify that the review cannot be submitted when \"Email\" is empty.\n\nTechnique(s): Equivalence Partitioning - empty is the invalid partition of a required field.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-30-01 | EP | \"Email\" empty, all other fields valid: the review is not submitted and an error names \"Email\". | Negative | Assumption: error names the field; wording checked for meaning (Q-20). |\n\n### TR-31: Verify that a correctly formatted email is accepted and an incorrectly formatted email is rejected.\n\nTechnique(s): Equivalence Partitioning - valid formats and one invalid partition per format fault, each tested alone; Boundary Value Analysis - Email length.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-31-01 | EP | A standard address (for example \"anna@example.com\") is accepted. | Positive | Missing info: email format rule (Q-06). |\n| TCD-31-02 | EP | An address with a dot and plus in the local part and a subdomain (for example \"anna.tran+shop@mail.example.co.uk\") is accepted. | Positive | Edge case: less common valid format.<br>Missing info: email format rule (Q-06). |\n| TCD-31-03 | EP | An address in upper case (for example \"Anna@Example.COM\") is accepted. | Positive | Missing info: email format rule (Q-06). |\n| TCD-31-04 | EP | An address without \"@\" (for example \"anna.example.com\") is rejected and an error names \"Email\". | Negative | Missing info: email format rule (Q-06). |\n| TCD-31-05 | EP | An address without a local part (for example \"@example.com\") is rejected. | Negative | Missing info: email format rule (Q-06). |\n| TCD-31-06 | EP | An address without a domain (for example \"anna@\") is rejected. | Negative | Missing info: email format rule (Q-06). |\n| TCD-31-07 | EP | An address without a top-level domain (for example \"anna@example\") is accepted or rejected as confirmed for Q-06. | Negative | Missing info: email format rule (Q-06). |\n| TCD-31-08 | EP | An address with a space inside (for example \"an na@example.com\") is rejected. | Negative | Missing info: email format rule (Q-06). |\n| TCD-31-09 | EP | An address with two \"@\" (for example \"anna@@example.com\") is rejected. | Negative | Missing info: email format rule (Q-06). |\n| TCD-31-10 | BVA | An address of EMAIL_MAX - 1 characters is accepted. | Positive | Missing info: maximum length (Q-06). |\n| TCD-31-11 | BVA | An address of exactly EMAIL_MAX characters is accepted. | Positive | Edge case: on the maximum.<br>Missing info: maximum length (Q-06). |\n| TCD-31-12 | BVA | An address of EMAIL_MAX + 1 characters is blocked or rejected. | Negative | Edge case: just above the maximum.<br>Missing info: maximum length (Q-06). |\n\n### TR-32: Verify that leading and trailing spaces in Name and Email are removed, and a Name or Email made only of spaces counts as empty.\n\nTechnique(s): Equivalence Partitioning - whitespace-only is an invalid partition per field; Error guessing - space-padded values.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-32-01 | Error guessing | A Name with leading and trailing spaces is accepted and displayed without them. | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |\n| TCD-32-02 | Error guessing | An Email with leading and trailing spaces is accepted (not rejected as a bad format). | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |\n| TCD-32-03 | EP | A Name made only of spaces counts as empty: not submitted, error names \"Name\". | Negative | Edge case: whitespace-only input.<br>Assumption: only spaces counts as empty (Q-17). |\n| TCD-32-04 | EP | An Email made only of spaces counts as empty: not submitted, error names \"Email\". | Negative | Edge case: whitespace-only input.<br>Assumption: only spaces counts as empty (Q-17). |\n\n### TR-33: Verify that when all required fields are valid, the review is submitted and a confirmation message is shown.\n\nTechnique(s): Decision table - the \"all four required fields valid\" rule, with the optional checkbox as an extra condition that must not change the outcome.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-33-01 | Decision table | Rating, review, Name and Email valid, checkbox not ticked: the review is submitted and a confirmation says it was received and waits for approval. | Positive | Assumption: confirmation wording (Q-21). |\n| TCD-33-02 | Decision table | Same valid data with the checkbox ticked: the review is submitted with the same confirmation. | Positive | Assumption: confirmation wording (Q-21). |\n\n### TR-34: Verify that when a required field is empty or invalid, the review is not submitted and an error message names each field concerned.\n\nTechnique(s): Decision table - 4 required fields give 16 rules; the \"all valid\" rule is TR-33, the four single-failure rules are TCD-05-01, TCD-07-01, TCD-28-01 and TCD-30-01 (invalid email: TCD-31-04); the remaining multi-failure rules give the same outcome and are collapsed into \"all fail\" and one two-failure rule, which check that every failing field is named. State transition - error shown -> corrected -> submitted. Error guessing - values kept, validation timing.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-34-01 | Decision table | All four required fields empty: not submitted, and an error names each of Rating, Your review, Name and Email. | Negative | Assumption: errors name each field; checked on Submit only (Q-19, Q-20). |\n| TCD-34-02 | Decision table | No rating and an invalid Email together (other fields valid): not submitted, and both fields are named. | Negative | Two failures on purpose, to check that all errors are reported together; each one alone is TCD-05-01 and TCD-31-04.<br>Assumption: errors name each field (Q-20). |\n| TCD-34-03 | Error guessing | After a rejected Submit, the rating, review text, Name and Email already entered are still in the form. | Positive | Assumption: values kept after a rejected Submit (Q-38). |\n| TCD-34-04 | State transition | Error shown -> the customer fixes the field -> Submit: the review is submitted and the error is no longer shown. | Positive | |\n| TCD-34-05 | Error guessing | Leaving a required field empty and moving to the next field shows no error until Submit is clicked. | Positive | Assumption: fields checked on Submit only (Q-19). |\n\n### TR-35: Verify that after a successful submit the customer stays on the product page and the form is cleared.\n\nTechnique(s): State transition - form state after the Submit event, with and without the save checkbox; Error guessing - reload/back after Submit and the rest of the page (regression).\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-35-01 | State transition | After a successful Submit with the checkbox not ticked: the customer stays on the product page and rating, review, Name and Email are all cleared. | Positive | Assumption: form cleared (Q-22). |\n| TCD-35-02 | State transition | After a successful Submit with the checkbox ticked: rating and review are cleared, Name and Email stay filled. | Positive | Assumption: Name and Email stay only if the checkbox was ticked (Q-22). |\n| TCD-35-03 | Error guessing | Using browser Back or Reload right after a successful Submit does not submit the review a second time. | Negative | Edge case: resubmit by browser navigation.<br>Risk: duplicate reviews distort the rating. |\n| TCD-35-04 | Error guessing | After Submit and after approval, the other parts of the product page (header links, Cart (0), product name, price, description) are unchanged and still work. | Positive | Regression check of the page that holds the form. |\n\n### TR-36: Verify that the \"Save my name, email, and website...\" checkbox is unchecked by default.\n\nTechnique(s): Equivalence Partitioning - first visit (nothing saved) and returning visit (data saved) are separate partitions for the default state.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-36-01 | EP | On a first visit with nothing saved, the save checkbox is not ticked. | Positive | Confirmed: unchecked in mockup-1.png. |\n| TCD-36-02 | EP | On a return visit after saving Name and Email, the checkbox state is as confirmed for Q-14. | Positive | Missing info: checkbox state when data is already saved (Q-14). |\n\n### TR-37: Verify that when the save checkbox is ticked at submit, the name and email are filled in again on the next visit in the same browser.\n\nTechnique(s): State transition - saved data state across visits (nothing saved -> saved -> updated -> removed); Error guessing - data remembered between visits.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-37-01 | State transition | Nothing saved -> tick the checkbox and Submit a valid review -> on the next visit, Name and Email are prefilled with the submitted values. | Positive | Risk: personal data stored on the device.<br>Assumption: only Name and Email are saved (Q-13, Q-14). |\n| TCD-37-02 | Error guessing | On the next visit after a saved Submit, the rating and review text are not prefilled. | Negative | Assumption: only Name and Email are saved (Q-14). |\n| TCD-37-03 | State transition | Saved -> Submit again with the checkbox ticked and a different Name and Email -> on the next visit the new values are prefilled. | Positive | Assumption: saved values are replaced (Q-14). |\n| TCD-37-04 | State transition | Saved -> Submit with the checkbox not ticked -> on the next visit Name and Email are no longer prefilled. | Negative | Risk: personal data left on a shared device.<br>Missing info: whether unticking removes saved data (Q-14). |\n| TCD-37-05 | Error guessing | Checkbox ticked but Submit rejected (for example empty review): nothing is saved, or data is saved as confirmed for Q-14. | Negative | Missing info: whether data is saved on a rejected Submit (Q-14). |\n\n### TR-38: Verify that when the save checkbox is not ticked, no name or email is kept for the next visit.\n\nTechnique(s): Equivalence Partitioning - \"not ticked\" partition; Error guessing - ticked then unticked before Submit.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-38-01 | EP | Checkbox not ticked, valid Submit, next visit: Name and Email are empty. | Negative | Risk: personal data left on a shared device.<br>Missing info: what is saved when not ticked (Q-14). |\n| TCD-38-02 | Error guessing | Checkbox ticked and then unticked before a valid Submit: on the next visit Name and Email are empty. | Negative | Edge case: changed mind before Submit.<br>Missing info: what is saved when not ticked (Q-14). |\n\n### TR-39: Verify that a customer cannot submit more reviews for the same product than the confirmed limit.\n\nTechnique(s): Boundary Value Analysis - count limit LIMIT per customer and product; Equivalence Partitioning - same product vs another product; Error guessing - pending reviews counted toward the limit.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-39-01 | BVA | The customer's review that reaches LIMIT for this product (for example the first review if LIMIT is 1) is accepted. | Positive | Missing info: number of reviews per customer and product (Q-12). |\n| TCD-39-02 | BVA | A review that would be number LIMIT + 1 for the same product is rejected as confirmed for Q-12. | Negative | Edge case: just above the limit.<br>Missing info: limit and message (Q-12); how the same customer is identified (account or email) also depends on Q-01. |\n| TCD-39-03 | EP | The same customer can review a different product even when the limit is reached on the first product. | Positive | Missing info: limit is per product (Q-12). Needs at least 2 products; the demo build has one (app-note.md). |\n| TCD-39-04 | Error guessing | A review still in Pending counts toward the limit (a second attempt while the first is pending is handled as in TCD-39-02). | Negative | Missing info: whether pending reviews count (Q-12). |\n\n### TR-40: Verify that clicking Submit more than once quickly creates only one review.\n\nTechnique(s): Error guessing - double click on Submit is a classic duplicate-record defect.\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-40-01 | Error guessing | Double-clicking Submit with valid data creates one pending review only (pending count +1; one review after approval). | Negative | Edge case: rapid double click.<br>Risk: duplicate reviews distort the rating.<br>Assumption: only one review is created (Q-28). |\n| TCD-40-02 | Error guessing | Clicking Submit and then pressing Enter immediately creates one pending review only. | Negative | Edge case: mixed mouse and keyboard submit.<br>Assumption: only one review is created (Q-28). |\n\n### TR-41: Verify that when the review cannot be saved (server or network error), the customer is told and the entered data is kept.\n\nTechnique(s): Error guessing - failure during Submit (network, server, session).\n\n| Condition ID | Technique | Test condition | Positive / Negative | Notes |\n|---|---|---|---|---|\n| TCD-41-01 | Error guessing | Network connection lost when Submit is clicked: a message says the review was not submitted and all entered values are kept. | Negative | Assumption: message shown and data kept (Q-29). Needs an environment with a server; the demo build runs without a server (app-note.md). |\n| TCD-41-02 | Error guessing | Server error or timeout on Submit: a message says the review was not submitted, all entered values are kept and no pending review is created. | Negative | Assumption: message shown and data kept (Q-29). Needs an environment with a server. |\n| TCD-41-03 | Error guessing | Session expired before Submit (signed-in customer): a message is shown and the entered values are kept. | Negative | Assumption: message shown and data kept (Q-29).<br>Missing info: sign-in rules (Q-01). |\n\n## Coverage by scenario type\n\n| Type | Covered by (condition IDs) |\n|---|---|\n| Positive | TCD-01-01, TCD-02-01, TCD-03-01 to TCD-03-04, TCD-04-01, TCD-04-02, TCD-06-01, TCD-08-01 to TCD-08-04, TCD-09-01 to TCD-09-04, TCD-14-01, TCD-14-02, TCD-17-01, TCD-18-01, TCD-26-01, TCD-29-01, TCD-31-01, TCD-33-01, TCD-33-02, TCD-35-01, TCD-37-01 |\n| Negative | TCD-02-02, TCD-03-05, TCD-04-03, TCD-05-01, TCD-07-01, TCD-10-01 to TCD-10-04, TCD-11-01, TCD-11-02, TCD-15-01, TCD-15-02, TCD-26-02 to TCD-26-05, TCD-28-01, TCD-29-03, TCD-29-04, TCD-29-08, TCD-30-01, TCD-31-04 to TCD-31-09, TCD-31-12, TCD-34-01, TCD-34-02 |\n| Boundary | Rating: TCD-03-01 to TCD-03-05, TCD-05-01. Review length: TCD-07-01, TCD-09-01 to TCD-09-04, TCD-10-01 to TCD-10-03. Name length: TCD-28-01, TCD-29-05 to TCD-29-08. Email length: TCD-31-10 to TCD-31-12. Review count: TCD-21-01, TCD-21-02, TCD-22-01, TCD-22-02, TCD-39-01, TCD-39-02 |\n| Validation | TCD-05-01, TCD-07-01, TCD-10-01, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-03, TCD-29-04, TCD-29-08, TCD-30-01, TCD-31-04 to TCD-31-09, TCD-31-12, TCD-32-03, TCD-32-04, TCD-34-01 to TCD-34-05 |\n| Error handling | TCD-35-03, TCD-40-01, TCD-40-02, TCD-41-01 to TCD-41-03 |\n| Permissions | TCD-26-01 to TCD-26-05, TCD-27-01, TCD-27-02, TCD-39-01 to TCD-39-04 |\n| Integration | TCD-13-01, TCD-14-01 to TCD-14-03, TCD-17-01 to TCD-17-03, TCD-18-01 to TCD-18-03, TCD-20-01, TCD-20-02, TCD-21-01, TCD-22-01 to TCD-22-03, TCD-23-01 to TCD-23-05, TCD-24-01 |\n| UI | TCD-01-01, TCD-02-01, TCD-02-03, TCD-02-04, TCD-06-01, TCD-25-01 to TCD-25-05, TCD-36-01 |\n| Compatibility | Not covered (see below) |\n| Regression | TCD-35-04 |\n| Data and privacy | TCD-12-01 to TCD-12-05, TCD-13-01, TCD-13-02, TCD-16-01, TCD-16-02, TCD-19-01, TCD-19-02, TCD-36-02, TCD-37-01 to TCD-37-05, TCD-38-01, TCD-38-02 |\n\n## Not covered\n\n| Type or area | Reason |\n|---|---|\n| Compatibility: browsers other than Chrome, mobile and tablet screen sizes, page language | Out of scope until Q-31 is answered; app-note.md names Chrome only for the build under test, and no TR covers other browsers or devices. |\n| Persistence of submitted and approved reviews after page reload or on another day | Needs another environment: the demo build restores its initial data on reload (app-note.md). No TR states persistence; it is implied by AC-03. |\n| Moderator screen (how a moderator finds, approves and rejects reviews) | Out of scope of the story; the demo build simulates approval with one button (app-note.md); process unknown (Q-07). Only the effect on the product page is designed (TR-13 to TR-15). |\n| Notification to the author when a review is approved or rejected | Out of scope of the story (Q-26 assumption: no notification); no TR. |\n| Edit or delete own review | Out of scope of the story (Q-27 assumption); no TR. |\n| Offensive language filtering | Q-30 assumption: left to the moderator, no automatic filter; no TR. |\n| Character counter \"n / 500\" under \"Your review\" | Observed in the demo build only; not in the story or mockup-1, so not a requirement. Its expected behaviour depends on Q-04. |\n| Visual styling against mockup-1 (colours, fonts, sizes, spacing) | Not specified as a requirement; TR-25 covers texts, labels, order and keyboard use only. |\n| Accessibility beyond keyboard use (screen reader names for the stars, contrast) | Not in any source and no TR; keyboard use is covered as an assumption (TCD-02-04, TCD-25-05). |\n| Performance and load (many visitors submitting at once) | Not in the story; no TR. |\n| Error handling conditions TCD-41-01 to TCD-41-03, multi-product conditions TCD-24-01 and TCD-39-03, and the second-viewer condition TCD-16-02 | Designed, but blocked in the demo build (no server, one product, data per page load); they need another environment. |\n\n## Assumptions to confirm\n\n| Condition ID | Assumption | Question ID |\n|---|---|---|\n| TCD-02-01, TCD-03-01 to TCD-03-05 | The rating is a whole number from 1 to 5, one per star. | Q-03 |\n| TCD-02-03 | A hover preview on the stars is not kept after the pointer leaves. | Q-36 |\n| TCD-02-04, TCD-25-05 | The rating and the whole form can be used by keyboard; Tab follows screen order. | Q-34 |\n| TCD-04-03, TCD-04-04 | Clicking the selected star again does not clear the rating; only a reload clears it. | Q-16 |\n| TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-34-01, TCD-34-02 | Each error names the field concerned; wording checked for meaning, not exact text. | Q-20 |\n| TCD-06-02 | Line breaks are shown as entered. | Q-35 |\n| TCD-08-02 | No character restriction in \"Your review\". | Q-37 |\n| TCD-08-04, TCD-11-01, TCD-11-02, TCD-32-01 to TCD-32-04 | Leading and trailing spaces are trimmed; a whitespace-only field counts as empty (line breaks treated like spaces). | Q-17 |\n| TCD-10-02 to TCD-10-04 | Typing and pasting stop at the maximum length. | Q-18 |\n| TCD-17-01 | Each displayed review shows star rating, reviewer name, date and review text. | Q-09 |\n| TCD-17-02 | The submit date is shown, in any unambiguous format. | Q-24 |\n| TCD-21-01 | All approved reviews are shown on one page. | Q-23 |\n| TCD-22-01 | A short message says there are no reviews yet. | Q-25 |\n| TCD-25-01 | The heading \"ADD A REVIEW\" is compared without regard to letter case. | Q-32 |\n| TCD-33-01, TCD-33-02 | The confirmation says the review was received and waits for approval. | Q-21 |\n| TCD-34-01, TCD-34-05 | Fields are checked on Submit only. | Q-19 |\n| TCD-34-03 | Entered values stay in the form after a rejected Submit. | Q-38 |\n| TCD-35-01, TCD-35-02 | After a successful Submit the customer stays on the page; the form is cleared, Name and Email stay only if the checkbox was ticked. | Q-22 |\n| TCD-37-01 to TCD-37-03 | Only Name and Email are saved, and a new ticked Submit replaces them. | Q-13, Q-14 |\n| TCD-40-01, TCD-40-02 | Only one review is created on a double Submit. | Q-28 |\n| TCD-41-01 to TCD-41-03 | On a save failure a message is shown and the entered data is kept. | Q-29 |\n| TCD-12-01 to TCD-12-05 | HTML, script and links are never executed, whatever the answer to Q-15. | Q-15 |\n"
}
```

## Tool (2026-10-21T04:35:16)

```
File created successfully at: C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-2\test-design.md (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:35:23)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-2 && python -I - <<'EOF'\nimport re,collections\nt=open('test-design.md',encoding='utf-8').read()\nrows=re.findall(r'^\\| (TCD-(\\d\\d)-\\d\\d) \\| ([^|]+) \\|[^|]+\\| (Positive|Negative) \\|',t,re.M)\nids=[r[0] for r in rows]\nprint('total',len(ids),'unique',len(set(ids)))\nper=collections.Counter(r[1] for r in rows)\nmissing=[f'{i:02d}' for i in range(1,42) if f'{i:02d}' not in per]\nprint('missing TRs',missing)\nprint('per TR',dict(sorted(per.items())))\ntech=collections.Counter(r[2].strip() for r in rows); print(tech)\npn=collections.Counter(r[3] for r in rows); print(pn)\nprint('TR headers',len(re.findall(r'^### TR-\\d\\d',t,re.M)))\nEOF",
  "description": "Verify condition IDs, coverage and technique counts"
}
```

## Tool (2026-10-21T04:35:24)

```
total 134 unique 134
missing TRs []
per TR {'01': 1, '02': 4, '03': 5, '04': 4, '05': 1, '06': 2, '07': 1, '08': 4, '09': 4, '10': 4, '11': 2, '12': 5, '13': 2, '14': 3, '15': 2, '16': 2, '17': 3, '18': 3, '19': 2, '20': 2, '21': 2, '22': 3, '23': 5, '24': 1, '25': 5, '26': 5, '27': 2, '28': 1, '29': 8, '30': 1, '31': 12, '32': 4, '33': 2, '34': 5, '35': 4, '36': 2, '37': 5, '38': 2, '39': 4, '40': 2, '41': 3}
Counter({'EP': 44, 'Error guessing': 38, 'BVA': 24, 'State transition': 19, 'Decision table': 8, 'EP / BVA': 1})
Counter({'Positive': 73, 'Negative': 61})
TR headers 41
```

## AI (2026-10-21T04:35:37)

Run 2 of the test-condition-design skill is finished. I followed its SKILL.md steps 1–9 and kept to the files you allowed. I did not open `runs/run-1/test-design.md` or the `run-1/ai-original/` folder, and I read nothing else under test-fixtures. From the exam folder I used `user-story.md`, `app-note.md` and `mockup-1.png`.

**What I wrote:** `C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-2\test-design.md`, built from `assets/test-design-template.md`. It has these sections:
- Values and rules used: 41 items, each marked Confirmed or Assumption with its source.
- Conditions for each TR, each with its technique(s) and the reason.
- Coverage by scenario type, a "Not covered" table and an "Assumptions to confirm" table linked to question IDs.

**Number of conditions:** 134 conditions for the 41 TRs (TR-01 to TR-41). A script check confirmed every TR has at least one condition and no ID repeats. 73 are Positive and 61 are Negative.
- Most conditions: TR-31 email format (12), TR-29 Name (8).
- Five each: TR-03, TR-12, TR-23, TR-25, TR-26, TR-34, TR-37.
- One each: TR-01, TR-05, TR-07, TR-24, TR-28, TR-30.

**Techniques used:**

| Technique | Conditions | Where |
|---|---|---|
| Equivalence partitioning | 44 | |
| Error guessing | 38 | |
| Boundary value analysis | 24 | Rating 1–5, review length, Name length, Email length, review count, per-customer limit |
| State transition | 19 | Review life cycle (pending, approved, rejected), the rating control, form state after submit, saved data across visits |
| Decision table | 8 | TR-26 who may review, TR-33/34 required-field rules |
| EP and BVA together | 1 | TCD-05-01, "no rating" |

**How I handled the missing values:** There are no product owner answers, so I did not invent any limits. Review min/max length, Name max length, Email max length, the per-customer review limit and the page size appear as named placeholders (REVIEW_MIN/MAX, NAME_MAX, EMAIL_MAX, LIMIT, PAGE_SIZE), each with a Missing info note pointing to its question. The "0 / 500" counter in the demo build is treated as observed behaviour only, not a requirement. Rating 1–5 stays an Assumption (Q-03).

**Not covered:**
- Other browsers and devices (Q-31).
- Reviews still being there after a reload, because the demo build resets its data on reload.
- The moderator screen.
- Telling the author the result.
- Editing or deleting your own review.
- Offensive-language filtering.
- The character counter.
- Visual styling.
- Accessibility beyond keyboard use.
- Performance.

Some conditions are written but can't be run on the demo build:
- Server and network errors (TCD-41-01 to 41-03).
- Two products needed (TCD-24-01, TCD-39-03).
- A second viewer needed (TCD-16-02).

**Things to raise:**
- **Name minimum length:** no clarification question asks for it. TCD-29-05 notes this, and I suggest adding it to Q-05.
- **Conflicts:** none between the answers and the sources, since there are no answers. The two conflicts already flagged in the TR list (Q-02 story vs mockup, Q-13 the "website" checkbox text) are kept as Missing info.

As the skill says, this stops here until you approve it; no test cases have been written.

## Tool (2026-10-21T04:35:38)

```
{"success":true,"message":"Report delivered to your caller."}
```
