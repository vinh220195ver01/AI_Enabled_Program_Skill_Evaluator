# Transcript 08: test-data-generation (run2)

Exported from the agent session log. Kept verbatim: the trainee's messages, the AI's replies, tool calls and tool results. Left out: harness reminders and private thinking. The harness prefix in front of follow-up messages is removed; the AI's final report is shown as an AI reply.

## Trainee (2026-10-21T04:29:41)

hi, second run of my test data skill to check consistency. skill: evaluator/test-fixtures/manual-qa-sim-pass/submission/skills/test-data-generation/SKILL.md (read and follow it).

inputs:
- test cases: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-cases.xlsx
- test design (optional): evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-1/test-design.md
- knowledge: evaluator/test-fixtures/manual-qa-sim-pass/submission/knowledge
- output folder: evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-2

only data for the cases I can run (Notes not starting with BLOCKED or NOT RUN). synthetic only. don't read runs/run-1/test-data.xlsx, independent run. only these files + the exam folder (evaluator/test-fixtures/manual-qa-sim-pass/exam), nothing else under test-fixtures. tell me what you wrote.

## AI (2026-10-21T04:29:47)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\AI_Enabled_Program\\evaluator\\test-fixtures\\manual-qa-sim-pass\\submission\\skills\\test-data-generation\\SKILL.md"
}
```

## Tool (2026-10-21T04:29:47)

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

## AI (2026-10-21T04:29:48)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && find submission exam -type f | grep -v \"runs/run-1/test-data.xlsx\" | head -100",
  "description": "List submission and exam files"
}
```

## Tool (2026-10-21T04:29:50)

```
submission/knowledge/environment.md
submission/knowledge/glossary.md
submission/knowledge/index.md
submission/knowledge/product-review-rules.md
submission/knowledge/screens-and-fields.md
submission/review/review-log.md
submission/runs/run-1/ai-original/clarification-questions.md
submission/runs/run-1/ai-original/test-cases.xlsx
submission/runs/run-1/ai-original/test-data.xlsx
submission/runs/run-1/ai-original/test-design.md
submission/runs/run-1/ai-original/test-requirements.xlsx
submission/runs/run-1/clarification-questions.md
submission/runs/run-1/test-cases.xlsx
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
exam/app/app.js
exam/app/index.html
exam/app/styles.css
exam/app-note.md
exam/mockup-1.png
exam/mockup-2.png
exam/User Story for My Shop.docx
exam/user-story.md
```

## AI (2026-10-21T04:29:53)

**Tool call `Bash`:**

```json
{
  "command": "cat skills/test-data-generation/references/test-data-rules.md skills/test-requirements-analysis/references/note-tags.md; echo ======; cat runs/run-1/test-design.md",
  "description": "Read rules, note tags, and test design"
}
```

## Tool (2026-10-21T04:29:55)

```
<persisted-output>
Output too large (60.7KB). Full output saved to: C:\Users\vinh.the.nguyen\.claude\projects\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\tool-results\bwh616nem.txt

Preview (first 2KB):
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
- Names: fictional names are fine (for example "Anna Smith", "Test User 01") when they do not belong to a real customer, colleague or known person. Keep the names the test cases already use, so the data matches the steps.
- If masked data from production is required, stop and ask the user for an approved source.
# Note tags

Single source for the tags used in the Notes column of every QA output (TR list, test design, test cases, test data, bug list). Other skills link to this file; do not copy it.

Format: one note per line, `Tag: text`. A row can have several notes or none.

| Tag | Use when | Example |
|---|---|---|
...
</persisted-output>
```

## AI (2026-10-21T04:29:58)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\Users\\vinh.the.nguyen\\.claude\\projects\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\tool-results\\bwh616nem.txt",
  "allow_large": true
}
```

## Tool (2026-10-21T04:29:58)

```
1	# Test data rules
2	
3	## IDs and columns
4	
5	- Data ID: `D-<TC ID>-<nn>`, for example D-TC-03-01-01. One row per field value.
6	- Purpose: exactly one of `valid`, `invalid`, `boundary`.
7	- Value: the literal value to type. For long strings, give the generation rule and the length, for example `"a" x 120 (120 chars)`.
8	- Notes: the rule the value tests (for example "length = maximum"), plus tagged notes.
9	
10	## How to build values
11	
12	| Purpose | Rule |
13	|---|---|
14	| valid | A realistic, clearly fake value inside every rule of the field. |
15	| boundary | Exactly on, one below or one above a limit. Count characters, including spaces. |
16	| invalid | Breaks exactly one rule; everything else about the value is valid. |
17	
18	Useful invalid and edge values (use when relevant): empty, spaces only, leading/trailing spaces, special characters, non-Latin and accented letters, emoji, HTML or script text (`<b>x</b>`), very long value, value with line breaks, wrong format for the type.
19	
20	## Privacy
21	
22	- Synthetic data only. Never real names of known people, real email addresses, phone numbers, addresses, card numbers, accounts or passwords.
23	- Email: use reserved domains only, `example.com`, `example.org` or `example.test`.
24	- Names: fictional names are fine (for example "Anna Smith", "Test User 01") when they do not belong to a real customer, colleague or known person. Keep the names the test cases already use, so the data matches the steps.
25	- If masked data from production is required, stop and ask the user for an approved source.
26	# Note tags
27	
28	Single source for the tags used in the Notes column of every QA output (TR list, test design, test cases, test data, bug list). Other skills link to this file; do not copy it.
29	
30	Format: one note per line, `Tag: text`. A row can have several notes or none.
31	
32	| Tag | Use when | Example |
33	|---|---|---|
34	| Assumption | We continue with a value or rule that no source states. Say what was assumed and which question would confirm it. | `Assumption: maximum length taken as N until Q-03 is answered.` |
35	| Edge case | The row covers a boundary, an unusual but valid input, or a rare sequence of actions. | `Edge case: value exactly at the maximum.` |
36	| Missing info | The source does not give enough to decide the expected behaviour. Link the question ID. | `Missing info: message text not specified (Q-05).` |
37	| Risk | Failure here would hurt users, data, privacy, security or the main flow. Say what could go wrong. | `Risk: personal data could be shown publicly.` |
38	
39	Rules:
40	
41	- An Assumption is never presented as fact elsewhere in the output.
42	- When a question is answered, replace the Assumption or Missing info note with the confirmed rule and its source.
43	======
44	# Test design: US-VP02 Submit a Product Review
45	
46	Input: runs/run-1/test-requirements.xlsx (41 TRs, TR-01 to TR-41) · Answers used: none (runs/run-1/clarification-questions.md has questions Q-01 to Q-38 (Q-33 to Q-38 added after review), no product owner answers yet) · Date: 2026-10-21
47	
48	Other sources read: knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md, knowledge/environment.md, exam/user-story.md, exam/mockup-1.png, exam/app-note.md. The demo build (exam/app/) is the product under test and is never used as a source of expected results; its "0 / 500" counter and its message texts are Observed only and are not used as values here.
49	
50	## Values and rules used
51	
52	| Item | Value | Status (Confirmed / Assumption) | Source |
53	|---|---|---|---|
54	| Form fields | "Your rating *", "Your review *", "Name *", "Email *", save checkbox, "Submit" | Confirmed | mockup-1.png (R1), screens-and-fields.md F1-F6 |
55	| Required fields | Rating, Review, Name and Email are required (marked *) | Confirmed | mockup-1.png (R2) |
56	| Info text | "Your email address will not be published. Required fields are marked *" | Confirmed | mockup-1.png |
57	| Heading | "ADD A REVIEW"; letter case not significant | Assumption | mockup-1.png; Q-32 |
58	| Number of stars | 5 star icons, none selected when the form opens | Confirmed | mockup-1.png (R6) |
59	| Rating values | Whole number 1 to 5, one per star; no half stars | Assumption | product-review-rules.md A1; Q-03 |
60	| Changing the rating | Clicking another star changes the rating; it cannot be cleared to "no rating" except by reloading the page | Assumption | Q-16 |
61	| "Your review" control | Multi-line text box | Confirmed | mockup-1.png (AC-02, F2) |
62	| "Your review" minimum and maximum length | Not stated in any source; no value used | Missing info | Q-04 (demo counter "0 / 500" is Observed only) |
63	| Text longer than the maximum | Typing and pasting stop at the maximum | Assumption | Q-18 |
64	| Leading / trailing spaces | Trimmed in Review, Name and Email; a field of only spaces counts as empty | Assumption | Q-17 |
65	| Name length and allowed characters | Not stated; no value used | Missing info | Q-05 |
66	| Email format rule and maximum length | Standard format text@domain.tld taken as the working rule; maximum length not stated | Assumption (format), Missing info (length) | Q-06 |
67	| Email not published | The email is never shown on the product page | Confirmed | mockup-1.png (R3) |
68	| HTML, scripts and links in text | Shown as plain text, removed or rejected: not stated. Never executed in any case | Missing info (handling), Assumption (never executed) | Q-15 |
69	| Validation timing | Fields are checked on Submit only | Assumption | Q-19 |
70	| Error messages | Each error names the field concerned; wording checked for meaning, not exact text | Assumption | Q-20 |
71	| Success message | Says the review was received and waits for approval | Assumption | Q-21 |
72	| Form after success | Customer stays on the product page; form cleared; Name and Email stay only if the save checkbox was ticked | Assumption | Q-22 |
73	| Review states | Submitted review is Pending; only Approved reviews are displayed | Confirmed | AC-03 (R4, R5), app-note.md |
74	| Moderation (who approves, reject, what happens to a rejected review) | Not stated | Missing info | Q-07 |
75	| Moderator in demo-1.0 | "Moderator: approve pending reviews" approves every pending review; used only as a test helper | Confirmed (helper), Assumption (not part of the feature) | environment.md, app-note.md |
76	| Author's view of own pending review | Not stated | Missing info | Q-08 |
77	| Details per displayed review | Star rating, reviewer name, date, review text; never the email | Assumption | product-review-rules.md A2; Q-09 |
78	| Date shown | Submit date, any unambiguous format | Assumption | Q-24 |
79	| Order of reviews | Not stated | Missing info | Q-10 |
80	| Paging | All approved reviews shown on one page | Assumption | Q-23 |
81	| No approved reviews | A short message saying there are no reviews yet | Assumption | Q-25 |
82	| Rating summary and count | Whether shown and how rounded: not stated; if shown, approved reviews only | Missing info | Q-11 |
83	| Who may review | Sign-in and purchase check not stated | Missing info | Q-01 |
84	| Name / Email for a signed-in customer | Story vs mockup-1 conflict | Missing info | Q-02 |
85	| Reviews per customer and product | Not stated | Missing info | Q-12 |
86	| Save checkbox default | Unchecked | Confirmed | mockup-1.png (F5) |
87	| Save checkbox stores | Name and Email only, in this browser | Assumption | Q-13, Q-14 |
88	| What is kept when the checkbox is not ticked, how long data is kept, how it is removed | Not stated | Missing info | Q-14 |
89	| Double submit | Only one review is created | Assumption | Q-28 |
90	| Server / network error | A message says the review was not submitted; the entered data is kept | Assumption | Q-29 |
91	| Browser and environment | Build demo-1.0, Chrome; other browsers and devices not stated | Confirmed (Chrome), Assumption (desktop Chrome, English) | environment.md, app-note.md; Q-31 |
92	| Demo-1.0 data | One product; reload restores the initial data; no sign-in | Confirmed | app-note.md, environment.md |
93	
94	## Test conditions
95	
96	### TR-01: Verify that the "Your rating *" field shows 5 stars.
97	
98	Technique(s): Equivalence Partitioning - the rating control has one valid display state (as in mockup-1); one condition covers it.
99	
100	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
101	|---|---|---|---|---|
102	| TCD-01-01 | EP | When the form opens, "Your rating *" shows exactly 5 star icons and none of them is selected. | Positive | |
103	
104	### TR-02: Verify that the customer can select a rating by clicking a star, and the selected stars are shown as selected.
105	
106	Technique(s): Equivalence Partitioning - whole-star values 1 to 5 form one valid partition (a middle value represents it; the ends are in TR-03) and half-star values form one invalid partition. Error guessing - hover and keyboard use are common sources of rating defects.
107	
108	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
109	|---|---|---|---|---|
110	| TCD-02-01 | EP | From no rating, clicking the 3rd star selects rating 3: stars 1 to 3 are shown as selected and stars 4 and 5 as not selected. | Positive | Assumption: the rating is a whole number from 1 to 5 until Q-03 is answered. |
111	| TCD-02-02 | EP | Clicking on the left half of a star does not set a half-star value (for example 2.5); the rating shown and saved is a whole number. | Negative | Missing info: whether half stars are allowed (Q-03). |
112	| TCD-02-03 | Error guessing | Moving the pointer over the stars without clicking, then moving it away, leaves the selected rating unchanged. | Negative | Assumption: a hover preview, if any, is not kept until Q-36 is answered. |
113	| TCD-02-04 | Error guessing | The rating can be selected with the keyboard only (Tab to the stars, then arrow keys, Space or Enter), and the selection is shown. | Positive | Missing info: keyboard use is not stated in any source (Q-34). |
114	
115	### TR-03: Verify that both the lowest rating (1 star) and the highest rating (5 stars) can be selected and are saved with the review.
116	
117	Technique(s): Boundary Value Analysis - the rating is a range 1 to 5 (Assumption). Just below the minimum (0 = no rating) is TCD-05-01; just above the maximum (6) cannot be entered because only 5 stars exist (TCD-01-01), so no separate condition.
118	
119	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
120	|---|---|---|---|---|
121	| TCD-03-01 | BVA | Rating 1 (on the minimum): the review is submitted and, after approval, is shown with 1 star. | Positive | Edge case: value exactly at the minimum.<br>Assumption: rating range 1 to 5 until Q-03 is answered. |
122	| TCD-03-02 | BVA | Rating 2 (just above the minimum): the review is submitted and, after approval, is shown with 2 stars. | Positive | Assumption: rating range 1 to 5 until Q-03 is answered. |
123	| TCD-03-03 | BVA | Rating 4 (just below the maximum): the review is submitted and, after approval, is shown with 4 stars. | Positive | Assumption: rating range 1 to 5 until Q-03 is answered. |
124	| TCD-03-04 | BVA | Rating 5 (on the maximum): the review is submitted and, after approval, is shown with 5 stars. | Positive | Edge case: value exactly at the maximum.<br>Assumption: rating range 1 to 5 until Q-03 is answered. |
125	
126	### TR-04: Verify that the customer can change the selected rating before submitting, and only the last selected rating is saved.
127	
128	Technique(s): State transition - states "No rating" and "Rating n"; events "click star m", "click the selected star again", "reload page", "Submit". Each valid transition once, plus the transition that is not allowed (clearing to "No rating" by clicking).
129	
130	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
131	|---|---|---|---|---|
132	| TCD-04-01 | State transition | Rating 2, click the 5th star: the rating becomes 5 and stars 1 to 5 are shown as selected (increase). | Positive | Assumption: clicking another star changes the rating (Q-16). |
133	| TCD-04-02 | State transition | Rating 5, click the 2nd star: the rating becomes 2 and only stars 1 and 2 are shown as selected (decrease). | Positive | Assumption: clicking another star changes the rating (Q-16). |
134	| TCD-04-03 | State transition | Rating 3, click the 3rd star again: the rating stays 3; it does not go back to "No rating". | Negative | Assumption: the rating cannot be cleared by clicking (Q-16). |
135	| TCD-04-04 | State transition | Rating 3, reload the page: the form opens with "No rating". | Positive | Assumption: reloading is the only way back to "No rating" (Q-16). |
136	| TCD-04-05 | State transition | Rating changed several times (1, then 4, then 2, then 3) and then Submit: the saved and, after approval, displayed rating is 3. | Positive | |
137	
138	### TR-05: Verify that the review cannot be submitted when no star rating is selected.
139	
140	Technique(s): Equivalence Partitioning (invalid partition "no rating") with Boundary Value Analysis (0 is just below the minimum 1).
141	
142	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
143	|---|---|---|---|---|
144	| TCD-05-01 | EP / BVA | No star selected (0, just below the minimum), Review, Name and Email valid, Submit: the review is not submitted and an error names the rating field. | Negative | Edge case: just below the minimum.<br>Assumption: the error names the rating field; wording checked for meaning, not exact text (Q-20). |
145	
146	### TR-06: Verify that a multi-line text box "Your review *" is provided for the review comment.
147	
148	Technique(s): Equivalence Partitioning - multi-line input is one valid partition. Error guessing - line breaks are often lost when the text is displayed.
149	
150	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
151	|---|---|---|---|---|
152	| TCD-06-01 | EP | "Your review *" accepts text on several lines: pressing Enter starts a new line inside the box and does not submit the form. | Positive | |
153	| TCD-06-02 | Error guessing | A review written on several lines is shown on the product page, after approval, with its line breaks kept. | Positive | Missing info: display of line breaks is not stated in any source (Q-35). |
154	
155	### TR-07: Verify that the review cannot be submitted when "Your review" is empty.
156	
157	Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field (0 characters).
158	
159	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
160	|---|---|---|---|---|
161	| TCD-07-01 | EP | "Your review" empty (0 characters), rating, Name and Email valid, Submit: the review is not submitted and an error names "Your review". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |
162	
163	### TR-08: Verify that review text within the allowed length is accepted and saved as entered.
164	
165	Technique(s): Equivalence Partitioning - one valid length partition (between the minimum and the maximum) and valid character types. Error guessing - pasted text and non-Latin characters are frequent defect sources.
166	
167	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
168	|---|---|---|---|---|
169	| TCD-08-01 | EP | Review text with a length between the minimum and the maximum: the review is submitted and, after approval, the text is shown exactly as entered. | Positive | Missing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered. |
170	| TCD-08-02 | Error guessing | Review text with accented letters (é, ü), non-Latin letters (日本語), digits, punctuation and an emoji: accepted and shown unchanged. | Positive | Assumption: no character restriction in "Your review" until Q-37 is answered. |
171	| TCD-08-03 | Error guessing | Review text pasted from the clipboard is accepted and saved in the same way as typed text. | Positive | |
172	
173	### TR-09: Verify that review text of exactly the minimum length and exactly the maximum length is accepted.
174	
175	Technique(s): Boundary Value Analysis - the review has a length range (minimum and maximum). Values on and just inside each boundary are here; just outside are in TR-10. The exact numbers are not in any source.
176	
177	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
178	|---|---|---|---|---|
179	| TCD-09-01 | BVA | Review length = minimum: accepted. | Positive | Edge case: value exactly at the minimum.<br>Missing info: minimum length not stated (Q-04). |
180	| TCD-09-02 | BVA | Review length = minimum + 1: accepted. | Positive | Missing info: minimum length not stated (Q-04). |
181	| TCD-09-03 | BVA | Review length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-04). |
182	| TCD-09-04 | BVA | Review length = maximum: accepted and, after approval, shown in full (not cut). | Positive | Edge case: value exactly at the maximum.<br>Missing info: maximum length not stated (Q-04). |
183	
184	### TR-10: Verify that review text shorter than the minimum or longer than the maximum is not accepted.
185	
186	Technique(s): Boundary Value Analysis - values just outside each boundary, one invalid value per condition. Error guessing - very long pasted text.
187	
188	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
189	|---|---|---|---|---|
190	| TCD-10-01 | BVA | Review length = minimum - 1, Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: one character below the minimum.<br>Missing info: minimum length not stated (Q-04). If the minimum is 1, this is TCD-07-01 and is not repeated. |
191	| TCD-10-02 | BVA | Typing maximum + 1 characters: typing stops at the maximum and the box holds exactly maximum characters. | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: typing stops at the maximum (Q-18). |
192	| TCD-10-03 | BVA | Pasting text of maximum + 1 characters: the text in the box is cut at the maximum. | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |
193	| TCD-10-04 | Error guessing | Pasting very long text (about ten times the maximum): the box holds at most the maximum and the page stays responsive. | Negative | Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |
194	
195	### TR-11: Verify that review text made only of spaces is treated as empty and the review is not submitted.
196	
197	Technique(s): Error guessing - spaces-only and space-padded input; Boundary Value Analysis - trimmed length just below the minimum.
198	
199	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
200	|---|---|---|---|---|
201	| TCD-11-01 | Error guessing | "Your review" contains only spaces, Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
202	| TCD-11-02 | Error guessing | "Your review" contains only line breaks (Enter pressed several times), Submit: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: line breaks are treated like spaces (Q-17). |
203	| TCD-11-03 | Error guessing | Valid review text with leading and trailing spaces: accepted and, after approval, shown without the leading and trailing spaces. | Positive | Assumption: spaces are trimmed (Q-17). |
204	| TCD-11-04 | BVA | Review of (minimum - 1) visible characters plus one trailing space (length = minimum only if the space is counted), Submit: the review is not submitted. | Negative | Edge case: length reaches the minimum only through a space.<br>Assumption: length is counted after trimming (Q-17).<br>Missing info: minimum length not stated (Q-04). |
205	
206	### TR-12: Verify that HTML tags, script code and links entered in "Your review" or "Name" are never run as code on the product page.
207	
208	Technique(s): Error guessing - script injection through free text is a known high-risk defect; each field and each injection form is tested separately so the result shows which one failed.
209	
210	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
211	|---|---|---|---|---|
212	| TCD-12-01 | Error guessing | "Your review" contains `<script>alert(1)</script>`: no script runs, on submit or on the product page after approval. | Negative | Missing info: shown as plain text, removed or rejected (Q-15).<br>Assumption: content is never executed (Q-15).<br>Risk: script injection would affect every visitor of the product page. |
213	| TCD-12-02 | Error guessing | "Your review" contains `<img src=x onerror=alert(1)>`: no script runs and no image element is added to the page. | Negative | Missing info: handling not stated (Q-15).<br>Risk: script injection through an HTML attribute. |
214	| TCD-12-03 | Error guessing | "Your review" contains harmless HTML `<b>bold</b>`: the text is not rendered as bold HTML; it is shown as plain text, removed or rejected as confirmed for Q-15. | Negative | Missing info: handling not stated (Q-15). |
215	| TCD-12-04 | Error guessing | "Your review" contains a web link (`https://example.com`): it is shown, removed or rejected as confirmed for Q-15, and is not turned into a clickable link unless Q-15 allows it. | Negative | Missing info: handling of links not stated (Q-15). |
216	| TCD-12-05 | Error guessing | "Name" contains `<script>alert(1)</script>`: no script runs where the name is shown. | Negative | Missing info: handling not stated (Q-05, Q-15).<br>Risk: script injection through the reviewer name. |
217	
218	### TR-13: Verify that a newly submitted review is not displayed on the product page while it waits for approval.
219	
220	Technique(s): State transition - Submit moves a review from "not existing" to "Pending"; in "Pending" the review must not be displayed to other visitors. (The author's own view is TR-16.)
221	
222	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
223	|---|---|---|---|---|
224	| TCD-13-01 | State transition | After a valid Submit (state Pending), the review does not appear in the reviews list for another visitor of the product page. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: demo-1.0 has no sign-in and keeps data only in the open page, so "another visitor" cannot be simulated there (environment.md); check in the author's page per TCD-16-01. |
225	| TCD-13-02 | State transition | A pending review is still not displayed after the product page is opened again later. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: in demo-1.0 a reload restores the initial data (environment.md), so this needs a build that keeps data. |
226	
227	### TR-14: Verify that a submitted review is displayed on the product page after it is approved.
228	
229	Technique(s): State transition - event "approve" moves Pending to Approved (valid transition); approving again or with nothing pending must not create entries (invalid transitions).
230	
231	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
232	|---|---|---|---|---|
233	| TCD-14-01 | State transition | Pending review, moderator approves: the review appears in the reviews list on the product page. | Positive | Missing info: who approves and how (Q-07).<br>Assumption: in demo-1.0 the "Moderator: approve pending reviews" helper plays the moderator (environment.md). |
234	| TCD-14-02 | State transition | Approved review, approve action used again: the review is shown once only (no duplicate). | Negative | Edge case: approve twice.<br>Missing info: moderation workflow (Q-07). |
235	| TCD-14-03 | State transition | No pending review, approve action used: no new or empty review appears. | Negative | Edge case: approve with nothing pending.<br>Missing info: moderation workflow (Q-07). |
236	
237	### TR-15: Verify that a rejected review is never displayed on the product page.
238	
239	Technique(s): State transition - event "reject" moves Pending to Rejected; Rejected must never lead to "displayed" through other events.
240	
241	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
242	|---|---|---|---|---|
243	| TCD-15-01 | State transition | Pending review, moderator rejects: the review does not appear on the product page. | Positive | Missing info: whether a review can be rejected and what happens to it (Q-07). Demo-1.0 has no reject action (environment.md). |
244	| TCD-15-02 | State transition | Rejected review, then other pending reviews are approved: the rejected review is still not displayed. | Negative | Missing info: moderation workflow (Q-07).<br>Risk: rejected content shown publicly. |
245	
246	### TR-16: Verify that the author sees their own pending review only in the way confirmed for Q-08 (marked as awaiting approval, or not at all).
247	
248	Technique(s): Decision table - conditions "viewer = author / other visitor" and "state = Pending / Approved". Rule other + Pending is TCD-13-01; rule other + Approved is TCD-14-01; the two author rules are below.
249	
250	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
251	|---|---|---|---|---|
252	| TCD-16-01 | Decision table | Rule: viewer = author, state = Pending: the author sees the review marked as awaiting approval, or does not see it, as confirmed for Q-08. | Positive | Missing info: author's view of a pending review not specified (Q-08). |
253	| TCD-16-02 | Decision table | Rule: viewer = author, state = Approved: the author sees the review like any other approved review, with no "awaiting approval" mark. | Positive | Missing info: whether a pending mark exists (Q-08). |
254	
255	### TR-17: Verify that each displayed review shows the confirmed details (star rating, reviewer name, date, review text).
256	
257	Technique(s): Equivalence Partitioning - every approved review belongs to one partition and must show the same set of details; one condition per detail group whose rule differs.
258	
259	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
260	|---|---|---|---|---|
261	| TCD-17-01 | EP | Each approved review shows its star rating, reviewer name, date and review text. | Positive | Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered. |
262	| TCD-17-02 | EP | The date shown with a review is the submit date, in an unambiguous format. | Positive | Assumption: submit date in any unambiguous format (Q-24). |
263	| TCD-17-03 | EP | The reviewer name is shown in the confirmed form (full name, first name only or initials). | Positive | Missing info: form of the name not specified (Q-09).<br>Risk: privacy of the reviewer's name. |
264	
265	### TR-18: Verify that the star rating, name and review text of a displayed review match what the customer submitted.
266	
267	Technique(s): Equivalence Partitioning - several reviews with different values must keep their own values. Error guessing - special characters are often encoded wrongly and long words often break the layout.
268	
269	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
270	|---|---|---|---|---|
271	| TCD-18-01 | EP | Two reviews submitted one after the other with different rating, name and text: after approval each shows its own rating, name and text (no mix-up). | Positive | |
272	| TCD-18-02 | Error guessing | Name with accented letter, apostrophe and hyphen (for example "Zoë O'Brien-Lê"): shown exactly as entered, with no encoded characters such as `&#39;`. | Positive | Assumption: such names are accepted until Q-05 is answered. |
273	| TCD-18-03 | Error guessing | Review text with the characters `& < > " '` used as plain text (for example "5 > 3 & good"): shown exactly as entered, not as `&amp;` or `&gt;`. | Positive | Missing info: handling of HTML-like text (Q-15). |
274	| TCD-18-04 | Error guessing | Review of maximum length made of one long word with no spaces: shown in full without breaking the page layout. | Positive | Missing info: maximum length not stated (Q-04). |
275	
276	### TR-19: Verify that the reviewer's email address is never displayed on the product page.
277	
278	Technique(s): Error guessing - personal data often leaks through hidden places (tooltips, links, page source) as well as visible text.
279	
280	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
281	|---|---|---|---|---|
282	| TCD-19-01 | Error guessing | After approval, the email entered does not appear anywhere in the visible product page (reviews list, reviewer name, rating summary). | Positive | Risk: personal data could be shown publicly. |
283	| TCD-19-02 | Error guessing | After approval, the email is not in hidden parts of the review: no tooltip, no "mailto" link on the name, not in the page source of the review. | Positive | Risk: personal data could be read by anyone viewing the page source. |
284	
285	### TR-20: Verify that approved reviews are listed in the confirmed order.
286	
287	Technique(s): Equivalence Partitioning - one partition "list of approved reviews with different dates and ratings". Error guessing - newly approved reviews and ties are common ordering defects.
288	
289	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
290	|---|---|---|---|---|
291	| TCD-20-01 | EP | At least 3 approved reviews with different dates and ratings are listed in the confirmed order. | Positive | Missing info: list order not specified (Q-10). |
292	| TCD-20-02 | Error guessing | A review approved after the existing ones appears in the position the confirmed order requires. | Positive | Missing info: list order not specified (Q-10). |
293	| TCD-20-03 | Error guessing | Two approved reviews with the same date and the same rating keep a stable order when the page is opened again. | Positive | Edge case: tie in the sort key.<br>Missing info: list order not specified (Q-10). |
294	
295	### TR-21: Verify that all approved reviews can be seen when a product has many reviews.
296	
297	Technique(s): Equivalence Partitioning - "many reviews" partition. Boundary Value Analysis - page size, only if paging is confirmed.
298	
299	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
300	|---|---|---|---|---|
301	| TCD-21-01 | EP | Product with a large number of approved reviews (for example 50): every approved review can be seen. | Positive | Edge case: large number of approved reviews.<br>Assumption: all approved reviews are shown on one page (Q-23). |
302	| TCD-21-02 | BVA | Approved reviews = page size - 1: all are on the first page and no paging control is shown. | Positive | Missing info: whether paging exists and the page size (Q-23). |
303	| TCD-21-03 | BVA | Approved reviews = page size: all are on the first page and no paging control is shown. | Positive | Edge case: count exactly at the page size.<br>Missing info: page size (Q-23). |
304	| TCD-21-04 | BVA | Approved reviews = page size + 1: the last review is reachable through the paging control or "Load more". | Positive | Edge case: one above the page size.<br>Missing info: page size (Q-23). |
305	
306	### TR-22: Verify that a clear empty state is shown when the product has no approved reviews.
307	
308	Technique(s): Boundary Value Analysis - approved review count 0 and the move from 0 to 1; Equivalence Partitioning - "only pending reviews" is part of the 0-approved partition.
309	
310	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
311	|---|---|---|---|---|
312	| TCD-22-01 | BVA | 0 approved reviews: a short message says there are no reviews yet. | Positive | Edge case: product with no approved reviews.<br>Assumption: a short message saying there are no reviews yet (Q-25).<br>Missing info: demo-1.0 has one product that starts with approved reviews (app-note.md); a product with 0 approved reviews may not be available. |
313	| TCD-22-02 | EP | 0 approved reviews and 1 or more pending reviews: the empty-state message is still shown. | Positive | Edge case: only pending reviews.<br>Assumption: empty-state message (Q-25). |
314	| TCD-22-03 | BVA | From 0 to 1 approved review: the empty-state message disappears and the review is shown. | Positive | Assumption: empty-state message (Q-25). |
315	
316	### TR-23: Verify that the average rating and review count on the product page, if shown, are calculated from approved reviews only.
317	
318	Technique(s): Decision table - condition "state of the new review = Approved / Pending / Rejected", outcome "included in average and count: yes / no". Boundary Value Analysis - rounding boundary and zero reviews.
319	
320	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
321	|---|---|---|---|---|
322	| TCD-23-01 | Decision table | Rule: new review Approved: the average rating and the review count include it. | Positive | Missing info: whether a summary is shown and how it is rounded (Q-11). |
323	| TCD-23-02 | Decision table | Rule: new review Pending: the average rating and the review count do not change. | Positive | Missing info: Q-11.<br>Risk: pending reviews could change the score shown to shoppers. |
324	| TCD-23-03 | Decision table | Rule: new review Rejected: the average rating and the review count do not change. | Positive | Missing info: Q-07, Q-11.<br>Risk: rejected reviews could change the score shown to shoppers. |
325	| TCD-23-04 | EP | The review count shown equals the number of approved reviews listed. | Positive | Missing info: whether a count is shown (Q-11). |
326	| TCD-23-05 | BVA | Ratings whose exact average falls on and next to the rounding step (for example 4 and 5 = 4.5; 4, 4 and 5 = 4.33...) are shown with the confirmed rounding. | Positive | Missing info: rounding rule not stated (Q-11); exact boundary values are set when Q-11 is answered. |
327	| TCD-23-06 | Error guessing | 0 approved reviews: the summary shows no average, or an empty state, and never a wrong value such as "NaN" or "0 stars". | Negative | Edge case: no approved reviews.<br>Missing info: Q-11, Q-25. |
328	
329	### TR-24: Verify that a review is displayed only on the page of the product it was written for.
330	
331	Technique(s): Equivalence Partitioning - partitions "page of the reviewed product" and "page of another product".
332	
333	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
334	|---|---|---|---|---|
335	| TCD-24-01 | EP | A review written and approved for product A appears on the page of product A. | Positive | Covered in demo-1.0 by TCD-14-01 (one product only). |
336	| TCD-24-02 | EP | The same review does not appear on the page of product B. | Negative | Risk: reviews shown on the wrong product mislead shoppers.<br>Missing info: demo-1.0 has one product only (app-note.md); needs a build with two products. |
337	
338	### TR-25: Verify that the review form shows the heading, the info text, the fields, the save checkbox and the "Submit" button as in mockup-1.
339	
340	Technique(s): Equivalence Partitioning - the form has one valid display state (mockup-1); one condition per element group. Error guessing - focus order and keyboard use.
341	
342	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
343	|---|---|---|---|---|
344	| TCD-25-01 | EP | The heading reads "ADD A REVIEW". | Positive | Assumption: compared without regard to letter case (Q-32). |
345	| TCD-25-02 | EP | The info text reads "Your email address will not be published. Required fields are marked *". | Positive | |
346	| TCD-25-03 | EP | The labels "Your rating *", "Your review *", "Name *" and "Email *" are shown, each with the required marker *. | Positive | |
347	| TCD-25-04 | EP | The save checkbox reads "Save my name, email, and website in this browser for the next time I comment." | Positive | Missing info: final text of the save checkbox (Q-13). |
348	| TCD-25-05 | EP | A "Submit" button is shown below the save checkbox. | Positive | |
349	| TCD-25-06 | EP | The elements are in the mockup-1 order from top to bottom: heading, info text, rating, review, Name, Email, save checkbox, Submit. | Positive | |
350	| TCD-25-07 | Error guessing | Tab moves the focus through the form in the order shown, and Submit can be used with the keyboard. | Positive | Missing info: keyboard use is not stated in any source (Q-34). |
351	
352	### TR-26: Verify that only a customer who is allowed to review (as confirmed for Q-01) can submit a review, and a customer who is not allowed cannot.
353	
354	Technique(s): Decision table - conditions "signed in: yes / no" and "bought this product: yes / no"; outcome "may submit". The two "not signed in" rules are collapsed into one because the purchase cannot be linked to a guest without sign-in until Q-01 says otherwise. Error guessing - cancelled orders.
355	
356	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
357	|---|---|---|---|---|
358	| TCD-26-01 | Decision table | Rule: signed in and bought the product: the customer can submit a review. | Positive | Missing info: sign-in and purchase check not specified (Q-01).<br>Missing info: demo-1.0 has no sign-in (environment.md). |
359	| TCD-26-02 | Decision table | Rule: signed in and did not buy the product: the form is hidden, disabled or rejected on Submit with a message, as confirmed for Q-01. | Negative | Missing info: Q-01.<br>Risk: non-buyers could post fake reviews. |
360	| TCD-26-03 | Decision table | Rule: not signed in (guest): the form is hidden, disabled or rejected on Submit with a message, as confirmed for Q-01. | Negative | Missing info: Q-01.<br>Risk: guests could post fake reviews. |
361	| TCD-26-04 | Error guessing | Signed in, the order of this product was cancelled or refunded: the customer may or may not review, as confirmed for Q-01. | Negative | Edge case: cancelled or refunded purchase.<br>Missing info: cancelled or refunded purchase not specified (Q-33). |
362	
363	### TR-27: Verify that Name and Email for a signed-in customer are handled as confirmed for Q-02 (prefilled, editable or not shown).
364	
365	Technique(s): Equivalence Partitioning - the three possible answers to Q-02 (prefilled, editable, not shown) are the partitions; the applicable one is kept when Q-02 is answered.
366	
367	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
368	|---|---|---|---|---|
369	| TCD-27-01 | EP | Signed-in customer opens the form: Name and Email are prefilled from the account, editable, or not shown, as confirmed for Q-02. | Positive | Missing info: conflict between the story and mockup-1 (Q-02). |
370	| TCD-27-02 | EP | If Name is prefilled and editable: the customer changes the Name, submits, and the displayed review shows the name as confirmed for Q-02 (edited or account name). | Positive | Missing info: Q-02. |
371	
372	### TR-28: Verify that the review cannot be submitted when "Name" is empty.
373	
374	Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field.
375	
376	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
377	|---|---|---|---|---|
378	| TCD-28-01 | EP | "Name" empty, rating, Review and Email valid, Submit: the review is not submitted and an error names "Name". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |
379	
380	### TR-29: Verify that a Name within the allowed length and characters is accepted, and a Name outside them is rejected.
381	
382	Technique(s): Equivalence Partitioning - character partitions (Latin letters, accented letters, hyphen/apostrophe, non-Latin script, digits, symbols only), one invalid partition per condition. Boundary Value Analysis - minimum (1 character, just above empty) and maximum length.
383	
384	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
385	|---|---|---|---|---|
386	| TCD-29-01 | EP | Name of Latin letters and a space (for example "Anna Smith"): accepted. | Positive | Assumption: letters and spaces are allowed until Q-05 is answered. |
387	| TCD-29-02 | EP | Name with accented letters (for example "Zoë Lê"): accepted. | Positive | Edge case: accented letters.<br>Assumption: accented letters are allowed until Q-05 is answered. |
388	| TCD-29-03 | EP | Name with a hyphen and an apostrophe (for example "Mary-Jane O'Neil"): accepted. | Positive | Edge case: hyphen and apostrophe.<br>Assumption: hyphens and apostrophes are allowed until Q-05 is answered. |
389	| TCD-29-04 | EP | Name in a non-Latin script (for example "李明"): accepted or rejected as confirmed for Q-05. | Positive | Missing info: allowed characters not stated (Q-05). |
390	| TCD-29-05 | EP | Name containing digits (for example "Anna2"): accepted or rejected with an error naming "Name", as confirmed for Q-05. | Negative | Missing info: whether digits are allowed (Q-05). |
391	| TCD-29-06 | EP | Name made only of symbols (for example "@#$%"): rejected with an error naming "Name", unless Q-05 allows it. | Negative | Missing info: allowed characters not stated (Q-05). |
392	| TCD-29-07 | BVA | Name of 1 character (just above empty): accepted. | Positive | Edge case: shortest non-empty name.<br>Missing info: minimum length not stated (Q-05). |
393	| TCD-29-08 | BVA | Name length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-05). |
394	| TCD-29-09 | BVA | Name length = maximum: accepted and shown in full. | Positive | Edge case: Name at the maximum length.<br>Missing info: maximum length not stated (Q-05). |
395	| TCD-29-10 | BVA | Name length = maximum + 1: input stops at the maximum, or the review is rejected with an error naming "Name". | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length and over-length behaviour not stated (Q-05, Q-18). |
396	
397	### TR-30: Verify that the review cannot be submitted when "Email" is empty.
398	
399	Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field.
400	
401	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
402	|---|---|---|---|---|
403	| TCD-30-01 | EP | "Email" empty, rating, Review and Name valid, Submit: the review is not submitted and an error names "Email". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |
404	
405	### TR-31: Verify that a correctly formatted email is accepted and an incorrectly formatted email is rejected.
406	
407	Technique(s): Equivalence Partitioning - valid format partitions and one invalid partition per format fault (one fault per condition). Boundary Value Analysis - maximum length. Error guessing - upper-case letters.
408	
409	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
410	|---|---|---|---|---|
411	| TCD-31-01 | EP | Email "anna.smith@example.com": accepted. | Positive | Assumption: standard format text@domain.tld until Q-06 is answered. |
412	| TCD-31-02 | EP | Email with a plus sign and a sub-domain ("anna+shop@mail.example.com"): accepted. | Positive | Edge case: plus sign and sub-domain.<br>Assumption: standard format (Q-06). |
413	| TCD-31-03 | EP | Email without "@" ("anna.example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
414	| TCD-31-04 | EP | Email without the part before "@" ("@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
415	| TCD-31-05 | EP | Email without a domain ("anna@"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
416	| TCD-31-06 | EP | Email without a top-level domain ("anna@example"): rejected with an error naming "Email". | Negative | Assumption: a top-level domain is required (Q-06); some format rules accept this value. |
417	| TCD-31-07 | EP | Email with two "@" ("anna@@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
418	| TCD-31-08 | EP | Email with a space inside ("anna smith@example.com"): rejected with an error naming "Email". | Negative | Assumption: standard format (Q-06). |
419	| TCD-31-09 | Error guessing | Email in upper case ("ANNA@EXAMPLE.COM"): accepted. | Positive | Assumption: letter case does not matter (Q-06). |
420	| TCD-31-10 | BVA | Email length = maximum - 1: accepted. | Positive | Missing info: maximum length not stated (Q-06). |
421	| TCD-31-11 | BVA | Email length = maximum: accepted. | Positive | Edge case: value exactly at the maximum.<br>Missing info: maximum length not stated (Q-06). |
422	| TCD-31-12 | BVA | Email length = maximum + 1: input stops at the maximum, or the review is rejected with an error naming "Email". | Negative | Edge case: one character above the maximum.<br>Missing info: maximum length and over-length behaviour not stated (Q-06, Q-18). |
423	
424	### TR-32: Verify that leading and trailing spaces in Name and Email are removed, and a Name or Email made only of spaces counts as empty.
425	
426	Technique(s): Error guessing - space-padded and spaces-only input, one field per condition.
427	
428	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
429	|---|---|---|---|---|
430	| TCD-32-01 | Error guessing | Name with leading and trailing spaces ("  Anna Smith  "): accepted and, after approval, shown as "Anna Smith". | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
431	| TCD-32-02 | Error guessing | Name made only of spaces, Submit: the review is not submitted and an error names "Name". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
432	| TCD-32-03 | Error guessing | Email with leading and trailing spaces ("  anna@example.com  "): accepted as a valid email. | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
433	| TCD-32-04 | Error guessing | Email made only of spaces, Submit: the review is not submitted and an error names "Email". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
434	
435	### TR-33: Verify that when all required fields are valid, the review is submitted and a confirmation message is shown.
436	
437	Technique(s): Decision table - conditions "rating, review, name, email valid" and "save checkbox ticked: yes / no"; the all-valid rules give "submitted". The rules with one field invalid are listed under TR-34.
438	
439	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
440	|---|---|---|---|---|
441	| TCD-33-01 | Decision table | Rule: all four required fields valid, save checkbox not ticked, Submit: the review is submitted and a confirmation says it was received and waits for approval. | Positive | Assumption: confirmation says the review was received and waits for approval (Q-21). |
442	| TCD-33-02 | Decision table | Rule: all four required fields valid, save checkbox ticked, Submit: the review is submitted with the same confirmation. | Positive | Assumption: confirmation text (Q-21). |
443	
444	### TR-34: Verify that when a required field is empty or invalid, the review is not submitted and an error message names each field concerned.
445	
446	Technique(s): Decision table - conditions "rating / review / name / email valid: yes / no". Rules with exactly one invalid field are already covered: TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-31-03 to TCD-31-08. Rules with several invalid fields are collapsed into "all empty" and "two empty", which check that every field concerned is named. Equivalence Partitioning - validation timing.
447	
448	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
449	|---|---|---|---|---|
450	| TCD-34-01 | Decision table | Rule: all four required fields empty, Submit: the review is not submitted and errors name all four fields. | Negative | Assumption: each error names its field; wording checked for meaning (Q-20). |
451	| TCD-34-02 | Decision table | Rule: rating and review empty, Name and Email valid, Submit: errors name the rating and "Your review" only, not Name or Email. | Negative | Assumption: wording checked for meaning (Q-20). |
452	| TCD-34-03 | Decision table | After a rejected Submit, the values already entered stay in the form; the customer corrects the field, submits again and the review is submitted. | Positive | Assumption: entered values are kept after a rejected submit until Q-38 is answered. |
453	| TCD-34-04 | EP | Leaving a required field empty and moving to the next field shows no error until Submit is pressed. | Positive | Assumption: fields are checked on Submit only (Q-19). |
454	
455	### TR-35: Verify that after a successful submit the customer stays on the product page and the form is cleared.
456	
457	Technique(s): State transition - "form filled" to "form after success", with the save checkbox ticked or not as the deciding event.
458	
459	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
460	|---|---|---|---|---|
461	| TCD-35-01 | State transition | Successful Submit with the save checkbox not ticked: the customer stays on the product page and rating, review, Name and Email are all cleared. | Positive | Assumption: form cleared (Q-22). |
462	| TCD-35-02 | State transition | Successful Submit with the save checkbox ticked: the customer stays on the product page, rating and review are cleared, and Name and Email stay filled. | Positive | Assumption: Name and Email stay filled only if the checkbox was ticked (Q-22). |
463	
464	### TR-36: Verify that the "Save my name, email, and website..." checkbox is unchecked by default.
465	
466	Technique(s): Equivalence Partitioning - partitions "first visit (nothing saved)" and "visit after data was saved".
467	
468	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
469	|---|---|---|---|---|
470	| TCD-36-01 | EP | First visit with nothing saved in the browser: the save checkbox is not ticked. | Positive | |
471	| TCD-36-02 | EP | Visit after Name and Email were saved: the save checkbox is ticked or not ticked, as confirmed for Q-14. | Positive | Edge case: checkbox state on a return visit.<br>Missing info: not stated (Q-14). |
472	
473	### TR-37: Verify that when the save checkbox is ticked at submit, the name and email are filled in again on the next visit in the same browser.
474	
475	Technique(s): State transition - browser storage states "nothing saved" and "Name and Email saved"; events "Submit with box ticked", "Submit with box not ticked", "rejected Submit". Error guessing - other browser or private window.
476	
477	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
478	|---|---|---|---|---|
479	| TCD-37-01 | State transition | Nothing saved, valid Submit with the box ticked, next visit in the same browser: Name and Email are filled with the submitted values. | Positive | Assumption: only name and email are saved (Q-13, Q-14).<br>Risk: personal data stored on the device. |
480	| TCD-37-02 | State transition | Name and Email saved, valid Submit with a different Name and Email and the box ticked, next visit: the new values are filled. | Positive | Assumption: saved values are replaced (Q-14). |
481	| TCD-37-03 | State transition | Name and Email saved, valid Submit with the box not ticked, next visit: Name and Email are filled or empty as confirmed for Q-14. | Positive | Missing info: how saved data is removed (Q-14).<br>Risk: personal data left on a shared device. |
482	| TCD-37-04 | EP | After a ticked Submit, on the next visit only Name and Email are filled; rating and review are empty. | Positive | Assumption: only name and email are saved (Q-13, Q-14). |
483	| TCD-37-05 | Error guessing | After a ticked Submit, opening the page in another browser or a private window: Name and Email are empty. | Positive | Edge case: "in this browser" only. |
484	| TCD-37-06 | State transition | Nothing saved, box ticked but Submit rejected (for example "Your review" empty), next visit: Name and Email are empty. | Negative | Edge case: rejected submit with the box ticked.<br>Missing info: whether data is saved on a rejected submit (Q-14). |
485	
486	### TR-38: Verify that when the save checkbox is not ticked, no name or email is kept for the next visit.
487	
488	Technique(s): Equivalence Partitioning - partition "box not ticked, nothing saved before". Error guessing - data typed but not submitted.
489	
490	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
491	|---|---|---|---|---|
492	| TCD-38-01 | EP | Nothing saved, valid Submit with the box not ticked, next visit: Name and Email are empty. | Positive | Missing info: what is saved when the checkbox is not ticked (Q-14).<br>Risk: personal data left on a shared device. |
493	| TCD-38-02 | Error guessing | Name and Email typed but not submitted, page reloaded: Name and Email are empty (browser autofill switched off). | Positive | Missing info: Q-14.<br>Risk: personal data kept without consent. |
494	
495	### TR-39: Verify that a customer cannot submit more reviews for the same product than the confirmed limit.
496	
497	Technique(s): Boundary Value Analysis - count of reviews per customer and product (limit unknown). Error guessing - other product, changed identity.
498	
499	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
500	|---|---|---|---|---|
501	| TCD-39-01 | BVA | Customer has limit - 1 reviews for the product, submits another: accepted. | Positive | Missing info: number of reviews per customer and product not specified (Q-12). If the limit is 1, this is the first review (TCD-33-01) and is not repeated. |
502	| TCD-39-02 | BVA | Customer has exactly the limit, submits another (limit + 1): rejected with the message confirmed for Q-12. | Negative | Edge case: one above the limit.<br>Missing info: Q-12. |
503	| TCD-39-03 | Error guessing | Customer at the limit for product A submits a review for product B: accepted. | Positive | Missing info: Q-12; needs a build with two products. |
504	| TCD-39-04 | Error guessing | Customer at the limit submits again for the same product with a different Name and Email: still recognised and rejected. | Negative | Missing info: how the customer is identified (Q-01, Q-02, Q-12).<br>Risk: limit bypassed by changing name or email. |
505	
506	### TR-40: Verify that clicking Submit more than once quickly creates only one review.
507	
508	Technique(s): Error guessing - double click, repeated key presses, reload and browser back/forward after submit are known duplicate sources.
509	
510	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
511	|---|---|---|---|---|
512	| TCD-40-01 | Error guessing | Valid form, Submit double-clicked: one review is created (one pending, one shown after approval). | Negative | Edge case: rapid double click.<br>Assumption: only one review is created (Q-28).<br>Risk: duplicate reviews distort the rating. |
513	| TCD-40-02 | Error guessing | Valid form, Submit clicked and Enter pressed in a text field before the confirmation appears: one review is created. | Negative | Assumption: only one review is created (Q-28). |
514	| TCD-40-03 | Error guessing | Page reloaded right after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |
515	| TCD-40-04 | Error guessing | Browser Back and then Forward after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |
516	
517	### TR-41: Verify that when the review cannot be saved (server or network error), the customer is told and the entered data is kept.
518	
519	Technique(s): Error guessing - lost connection, server error and expired session are typical failure points of a submit.
520	
521	| Condition ID | Technique | Test condition | Positive / Negative | Notes |
522	|---|---|---|---|---|
523	| TCD-41-01 | Error guessing | Network connection lost, Submit: a message says the review was not submitted and the entered data stays in the form. | Negative | Assumption: Q-29.<br>Missing info: demo-1.0 runs without a server or network (environment.md), so this cannot be produced there. |
524	| TCD-41-02 | Error guessing | Server returns an error on Submit: a message says the review was not submitted and the entered data stays in the form. | Negative | Assumption: Q-29. Not producible in demo-1.0. |
525	| TCD-41-03 | Error guessing | Session expired before Submit (signed-in customer): the customer is told and the entered data is not lost. | Negative | Assumption: Q-29.<br>Missing info: sign-in rules (Q-01); demo-1.0 has no sign-in. |
526	| TCD-41-04 | Error guessing | After a failed Submit, the connection returns and Submit is pressed again: exactly one review is created. | Positive | Assumption: Q-28, Q-29. |
527	
528	## Coverage by scenario type
529	
530	| Type | Covered by (condition IDs) |
531	|---|---|
532	| Positive | TCD-02-01, TCD-03-01 to TCD-03-04, TCD-04-01, TCD-04-02, TCD-04-05, TCD-06-01, TCD-08-01, TCD-09-01 to TCD-09-04, TCD-14-01, TCD-17-01, TCD-29-01, TCD-31-01, TCD-33-01, TCD-33-02, TCD-35-01, TCD-37-01 |
533	| Negative | TCD-02-02, TCD-04-03, TCD-05-01, TCD-07-01, TCD-10-01 to TCD-10-04, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-05, TCD-29-06, TCD-30-01, TCD-31-03 to TCD-31-08, TCD-34-01, TCD-34-02, TCD-39-02 |
534	| Boundary | TCD-03-01 to TCD-03-04, TCD-05-01, TCD-09-01 to TCD-09-04, TCD-10-01 to TCD-10-03, TCD-11-04, TCD-21-02 to TCD-21-04, TCD-22-01, TCD-22-03, TCD-23-05, TCD-29-07 to TCD-29-10, TCD-31-10 to TCD-31-12, TCD-39-01, TCD-39-02 |
535	| Validation | TCD-05-01, TCD-07-01, TCD-10-01, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-05, TCD-29-06, TCD-30-01, TCD-31-03 to TCD-31-08, TCD-32-02, TCD-32-04, TCD-34-01 to TCD-34-04 |
536	| Error handling | TCD-40-01 to TCD-40-04, TCD-41-01 to TCD-41-04 |
537	| Permissions | TCD-26-01 to TCD-26-04, TCD-27-01, TCD-27-02, TCD-13-01, TCD-16-01, TCD-16-02, TCD-39-02, TCD-39-04 |
538	| Integration | TCD-13-01, TCD-13-02, TCD-14-01 to TCD-14-03, TCD-15-01, TCD-15-02, TCD-17-01 to TCD-17-03, TCD-18-01, TCD-20-01 to TCD-20-03, TCD-21-01, TCD-22-01 to TCD-22-03, TCD-23-01 to TCD-23-06, TCD-24-01, TCD-24-02 |
539	| UI | TCD-01-01, TCD-02-03, TCD-02-04, TCD-06-01, TCD-06-02, TCD-18-04, TCD-25-01 to TCD-25-07 |
540	| Compatibility | None in this design; see "Not covered" |
541	| Regression | TCD-14-02, TCD-15-02, TCD-18-01, TCD-20-02, TCD-22-03, TCD-23-04 (existing approved reviews, the empty state and the rating summary still behave correctly after new reviews are added) |
542	| Data and privacy | TCD-12-01 to TCD-12-05, TCD-17-03, TCD-19-01, TCD-19-02, TCD-36-01, TCD-36-02, TCD-37-01 to TCD-37-06, TCD-38-01, TCD-38-02 |
543	
544	## Not covered
545	
546	| Type or area | Reason |
547	|---|---|
548	| Compatibility: browsers other than Chrome, mobile and tablet screen sizes | Only Chrome is given (environment.md, app-note.md); other browsers and devices are blocked by missing information (Q-31). Add conditions when Q-31 is answered. |
549	| Language and localisation | Page language not stated; English assumed (Q-31). |
550	| Moderator screens and workflow (approve / reject UI, who moderates) | Out of scope of US-VP02; only its effect on the product page is covered (TR-14, TR-15). The demo-1.0 helper button is a test tool, not the feature (environment.md). |
551	| Telling the author the moderation result (for example by email) | Assumed out of scope of this story (Q-26). |
552	| Editing or deleting one's own review | Assumed out of scope of this story (Q-27). |
553	| Automatic offensive-language filter | Assumed left to the moderator, no automatic filter (Q-30). |
554	| "Website" field | No Website field exists in mockup-1; nothing to test until Q-13 is answered (only the checkbox text is covered, TCD-25-04). |
555	| Accessibility beyond keyboard use (screen reader labels, colour contrast) | Not in any source; only keyboard use is covered (TCD-02-04, TCD-25-07). |
556	| Performance and load (many users submitting at once) | Not in the story; needs another environment. |
557	| Execution on demo-1.0 of TCD-13-01, TCD-13-02, TCD-15-01, TCD-15-02, TCD-23-03, TCD-24-02, TCD-26-01 to TCD-26-04, TCD-27-01, TCD-27-02, TCD-39-03, TCD-39-04, TCD-41-01 to TCD-41-03 | The conditions exist, but demo-1.0 has one product, no sign-in, no reject action, no server, and resets data on reload (app-note.md, environment.md); they need another build or environment. |
558	
559	## Assumptions to confirm
560	
561	| Condition ID | Assumption | Question ID |
562	|---|---|---|
563	| TCD-02-01, TCD-03-01 to TCD-03-04 | The rating is a whole number from 1 to 5, one per star. | Q-03 |
564	| TCD-02-03 | A hover preview, if any, is not kept after the pointer leaves. | Q-36 |
565	| TCD-04-01 to TCD-04-04 | Clicking another star changes the rating; it cannot be cleared except by reloading the page. | Q-16 |
566	| TCD-08-02 | "Your review" has no character restriction (accented, non-Latin, emoji allowed). | Q-37 |
567	| TCD-10-02 to TCD-10-04 | Typing and pasting stop at the maximum length. | Q-18 |
568	| TCD-11-01 to TCD-11-04, TCD-32-01 to TCD-32-04 | Spaces (and line breaks) are trimmed; a field of only spaces counts as empty; length is counted after trimming. | Q-17 |
569	| TCD-12-01 | HTML and script content is never executed, whatever the answer on how it is handled. | Q-15 |
570	| TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-34-01, TCD-34-02 | Each error names its field; wording is checked for meaning, not exact text. | Q-20 |
571	| TCD-34-03 | Entered values stay in the form after a rejected Submit. | Q-38 |
572	| TCD-34-04 | Fields are checked on Submit only. | Q-19 |
573	| TCD-14-01 | The demo-1.0 "Moderator: approve pending reviews" helper stands in for the moderator and is not part of the feature. | Q-07 |
574	| TCD-17-01 | Each displayed review shows star rating, reviewer name, date and review text. | Q-09 |
575	| TCD-17-02 | The date is the submit date, in any unambiguous format. | Q-24 |
576	| TCD-18-02, TCD-29-01 to TCD-29-03 | Names with letters, spaces, accented letters, hyphens and apostrophes are accepted. | Q-05 |
577	| TCD-21-01 | All approved reviews are shown on one page. | Q-23 |
578	| TCD-22-01 to TCD-22-03 | With no approved reviews, a short message says there are no reviews yet. | Q-25 |
579	| TCD-25-01 | The heading "ADD A REVIEW" is compared without regard to letter case. | Q-32 |
580	| TCD-31-01 to TCD-31-09 | A valid email has the standard format text@domain.tld (top-level domain required, letter case ignored). | Q-06 |
581	| TCD-33-01, TCD-33-02 | The confirmation says the review was received and waits for approval. | Q-21 |
582	| TCD-35-01, TCD-35-02 | After success the customer stays on the page; the form is cleared; Name and Email stay only if the checkbox was ticked. | Q-22 |
583	| TCD-37-01, TCD-37-02, TCD-37-04 | Only Name and Email are saved in this browser, and a new ticked submit replaces them. | Q-13, Q-14 |
584	| TCD-40-01 to TCD-40-04, TCD-41-04 | Only one review is created per submit action. | Q-28 |
585	| TCD-41-01 to TCD-41-04 | On a save failure a message says the review was not submitted and the entered data is kept. | Q-29 |
586	
```

## AI (2026-10-21T04:30:02)

**Tool call `Bash`:**

```json
{
  "command": "cat knowledge/*.md; python -c \"import openpyxl;print(openpyxl.__version__)\"",
  "description": "Read knowledge files and check openpyxl"
}
```

## Tool (2026-10-21T04:30:06)

```
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
3.1.5
```

## AI (2026-10-21T04:30:11)

**Tool call `Bash`:**

```json
{
  "command": "python -I -c \"\nimport openpyxl,sys\nfor f in ['runs/run-1/test-cases.xlsx','skills/test-data-generation/assets/test-data-template.xlsx']:\n    wb=openpyxl.load_workbook(f)\n    for ws in wb:\n        print('=== ',f,ws.title,ws.dimensions, {k:v.width for k,v in ws.column_dimensions.items()})\n        for r in ws.iter_rows(values_only=True):\n            if any(c is not None for c in r): print(r)\n\" > \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt\" 2>&1; wc -c \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt\"",
  "description": "Dump test cases and template to scratchpad"
}
```

## Tool (2026-10-21T04:30:15)

```
18136 C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt
```

## AI (2026-10-21T04:30:18)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\tc.txt"
}
```

## Tool (2026-10-21T04:30:18)

```
1	Traceback (most recent call last):
2	  File "<string>", line 8, in <module>
3	    if any(c is not None for c in r): print(r)
4	                                      ~~~~~^^^
5	  File "C:\Python\Python314\Lib\encodings\cp1252.py", line 19, in encode
6	    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
7	           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
8	UnicodeEncodeError: 'charmap' codec can't encode characters in position 386-388: character maps to <undefined>
9	===  runs/run-1/test-cases.xlsx Test Cases A1:G146 {'A': 10.0, 'B': 12.0, 'C': 45.0, 'D': 35.0, 'E': 60.0, 'F': 55.0, 'G': 40.0}
10	('TR ID', 'TC ID', 'TC Summary', 'Pre-Condition', 'Steps', 'Expected Result', 'Notes')
11	('TR-01', 'TC-01-01', 'Verify that "Your rating *" shows exactly 5 stars, none selected, when the form opens.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Scroll to the "Add a review" form.\n2. Look at the stars next to "Your rating *" without clicking them.', 'Exactly 5 star icons are shown next to "Your rating *" and none of them is shown as selected.', 'Condition: TCD-01-01\nTechnique: EP')
12	('TR-02', 'TC-02-01', 'Verify that clicking the 3rd star selects rating 3.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 3rd star of "Your rating *".\n2. Look at the 5 stars of "Your rating *".', 'Stars 1, 2 and 3 are shown as selected and stars 4 and 5 are shown as not selected.', 'Condition: TCD-02-01\nTechnique: EP\nAssumption: the rating is a whole number from 1 to 5 until Q-03 is answered.')
13	('TR-02', 'TC-02-02', 'Verify that clicking the left half of a star does not set a half-star rating.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the left half of the 3rd star of "Your rating *".\n2. Look at the stars of "Your rating *".\n3. Enter "Half star check." in "Your review *".\n4. Enter "Anna Smith" in "Name *".\n5. Enter "anna.smith@example.com" in "Email *".\n6. Click "Submit".\n7. Click "Moderator: approve pending reviews".\n8. Find the review "Half star check." in the "Reviews" list.', 'No half star is shown, neither in "Your rating *" after step 1 nor on the review "Half star check." in the "Reviews" list; the rating is a whole number of stars.', 'Condition: TCD-02-02\nTechnique: EP\nMissing info: whether half stars are allowed (Q-03).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nAssumption: the rating is a whole number from 1 to 5, one per star until Q-03 is answered.')
14	('TR-02', 'TC-02-03', 'Verify that moving the pointer over the stars without clicking keeps the selected rating.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 2nd star of "Your rating *".\n2. Move the pointer over the 5th star of "Your rating *" without clicking.\n3. Move the pointer away from the stars.\n4. Look at the 5 stars of "Your rating *".', 'Stars 1 and 2 are shown as selected and stars 3, 4 and 5 as not selected (rating still 2).', 'Condition: TCD-02-03\nTechnique: Error guessing\nAssumption: a hover preview, if any, is not kept until Q-36 is answered.\nMissing info: expected result not stated in any source (Q-36).')
15	('TR-02', 'TC-02-04', 'Verify that a rating can be selected with the keyboard only.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click on the info text "Your email address will not be published. Required fields are marked *" to place the focus before the form.\n2. Press Tab until a star of "Your rating *" has the focus.\n3. Use the arrow keys to move to the 4th star and press Space (if nothing changes, press Enter).\n4. Look at the 5 stars of "Your rating *".', 'Stars 1 to 4 are shown as selected and star 5 as not selected, without using the mouse after step 1.', 'Condition: TCD-02-04\nTechnique: Error guessing\nMissing info: keyboard use is not stated in any source (Q-34).\nAssumption: the rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen until Q-34 is answered.')
16	('TR-03', 'TC-03-01', 'Verify that a review with rating 1 is submitted and shown with 1 star.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 1st star of "Your rating *".\n2. Enter "Rating check: one star." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Rating check: one star." in the "Reviews" list.', 'The review "Rating check: one star." appears in the "Reviews" list. It is shown with 1 of 5 stars selected.', 'Condition: TCD-03-01\nTechnique: BVA\nEdge case: value exactly at the minimum.\nAssumption: rating range 1 to 5 until Q-03 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-03, Q-09).\nAssumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.')
17	('TR-03', 'TC-03-02', 'Verify that a review with rating 2 is submitted and shown with 2 stars.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 2nd star of "Your rating *".\n2. Enter "Rating check: two stars." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Rating check: two stars." in the "Reviews" list.', 'The review "Rating check: two stars." appears in the "Reviews" list. It is shown with 2 of 5 stars selected.', 'Condition: TCD-03-02\nTechnique: BVA\nAssumption: rating range 1 to 5 until Q-03 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-03, Q-09).\nAssumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.')
18	('TR-03', 'TC-03-03', 'Verify that a review with rating 4 is submitted and shown with 4 stars.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Rating check: four stars." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Rating check: four stars." in the "Reviews" list.', 'The review "Rating check: four stars." appears in the "Reviews" list. It is shown with 4 of 5 stars selected.', 'Condition: TCD-03-03\nTechnique: BVA\nAssumption: rating range 1 to 5 until Q-03 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-03, Q-09).\nAssumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.')
19	('TR-03', 'TC-03-04', 'Verify that a review with rating 5 is submitted and shown with 5 stars.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 5th star of "Your rating *".\n2. Enter "Rating check: five stars." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Rating check: five stars." in the "Reviews" list.', 'The review "Rating check: five stars." appears in the "Reviews" list. It is shown with 5 of 5 stars selected.', 'Condition: TCD-03-04\nTechnique: BVA\nEdge case: value exactly at the maximum.\nAssumption: rating range 1 to 5 until Q-03 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-03, Q-09).\nAssumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.')
20	('TR-04', 'TC-04-01', 'Verify that clicking the 5th star after the 2nd changes the rating to 5.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 2nd star of "Your rating *".\n2. Click the 5th star of "Your rating *".\n3. Look at the 5 stars of "Your rating *".', 'All 5 stars are shown as selected (rating 5).', 'Condition: TCD-04-01\nTechnique: State transition\nAssumption: clicking another star changes the rating until Q-16 is answered.\nMissing info: expected result not stated in any source (Q-16).')
21	('TR-04', 'TC-04-02', 'Verify that clicking the 2nd star after the 5th changes the rating to 2.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 5th star of "Your rating *".\n2. Click the 2nd star of "Your rating *".\n3. Look at the 5 stars of "Your rating *".', 'Only stars 1 and 2 are shown as selected; stars 3, 4 and 5 are not selected (rating 2).', 'Condition: TCD-04-02\nTechnique: State transition\nAssumption: clicking another star changes the rating until Q-16 is answered.\nMissing info: expected result not stated in any source (Q-16).')
22	('TR-04', 'TC-04-03', 'Verify that clicking the selected 3rd star again does not clear the rating.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 3rd star of "Your rating *".\n2. Click the 3rd star of "Your rating *".\n3. Look at the 5 stars of "Your rating *".', 'Stars 1, 2 and 3 are still shown as selected (rating 3); the rating is not cleared to no rating.', 'Condition: TCD-04-03\nTechnique: State transition\nAssumption: the rating cannot be cleared by clicking until Q-16 is answered.\nMissing info: expected result not stated in any source (Q-16).')
23	('TR-04', 'TC-04-04', 'Verify that reloading the page resets a selected rating to no rating.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 3rd star of "Your rating *".\n2. Reload the page (F5).\n3. Look at the 5 stars of "Your rating *".', 'None of the 5 stars is shown as selected.', 'Condition: TCD-04-04\nTechnique: State transition\nAssumption: reloading is the only way back to "No rating" until Q-16 is answered.')
24	('TR-04', 'TC-04-05', 'Verify that only the last selected rating is saved after several changes.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 1st star of "Your rating *".\n2. Click the 4th star of "Your rating *".\n3. Click the 2nd star of "Your rating *".\n4. Click the 3rd star of "Your rating *".\n5. Enter "Changed rating, final is three." in "Your review *".\n6. Enter "Anna Smith" in "Name *".\n7. Enter "anna.smith@example.com" in "Email *".\n8. Click "Submit".\n9. Click "Moderator: approve pending reviews".\n10. Find the review "Changed rating, final is three." in the "Reviews" list.', 'The review "Changed rating, final is three." appears in the "Reviews" list. It is shown with 3 of 5 stars selected (not 1, 4 or 2).', 'Condition: TCD-04-05\nTechnique: State transition\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-09).\nAssumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered.')
25	('TR-05', 'TC-05-01', 'Verify that the review is not submitted when no star rating is selected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n2. Enter "Anna Smith" in "Name *".\n3. Enter "anna.smith@example.com" in "Email *".\n4. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names the rating field ("Your rating").', 'Condition: TCD-05-01\nTechnique: EP / BVA\nEdge case: just below the minimum.\nAssumption: the error names the rating field; wording checked for meaning, not exact text until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).')
26	('TR-06', 'TC-06-01', 'Verify that pressing Enter in "Your review *" starts a new line without submitting.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click in "Your review *".\n2. Type "Line one".\n3. Press Enter.\n4. Type "Line two".', '"Line two" is shown on a new line below "Line one" inside "Your review *"; no confirmation or error message appears and "Pending approval" stays 0.', 'Condition: TCD-06-01\nTechnique: EP')
27	('TR-06', 'TC-06-02', 'Verify that a multi-line review keeps its line breaks on the product page.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and type "Line one", press Enter, type "Line two", press Enter, type "Line three".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review starting with "Line one" in the "Reviews" list.', 'The review shows "Line one", "Line two" and "Line three" on three separate lines.', 'Condition: TCD-06-02\nTechnique: Error guessing\nMissing info: display of line breaks is not stated in any source (Q-35).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nAssumption: line breaks in a review are shown as entered until Q-35 is answered.')
28	('TR-07', 'TC-07-01', 'Verify that the review is not submitted when "Your review *" is empty.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Leave "Your review *" empty.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".', 'Condition: TCD-07-01\nTechnique: EP\nAssumption: wording checked for meaning, not exact text until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).')
29	('TR-08', 'TC-08-01', 'Verify that a review text within the allowed length is saved and shown as entered.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Soft fabric, true to size. Would buy again." in the "Reviews" list.', 'The review appears in the "Reviews" list with the text "Soft fabric, true to size. Would buy again." exactly as entered (same words, punctuation and letter case).', 'Condition: TCD-08-01\nTechnique: EP\nMissing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered.\nAssumption: the text used (43 characters) is between the minimum and the maximum length until Q-04 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.')
30	
```

## AI (2026-10-21T04:30:24)

**Tool call `Bash`:**

```json
{
  "command": "PYTHONIOENCODING=utf-8 python -I -c \"\nimport openpyxl,sys\nfor f in ['runs/run-1/test-cases.xlsx','skills/test-data-generation/assets/test-data-template.xlsx']:\n    wb=openpyxl.load_workbook(f)\n    for ws in wb:\n        print('=== ',f,ws.title,ws.dimensions, {k:v.width for k,v in ws.column_dimensions.items()})\n        for r in ws.iter_rows(values_only=True):\n            if any(c is not None for c in r): print(r)\n\" > \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt\" 2>&1; wc -l \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt\"",
  "description": "Dump test cases with UTF-8 output"
}
```

## Tool (2026-10-21T04:30:26)

```
29 C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt
```

## AI (2026-10-21T04:30:30)

**Tool call `Bash`:**

```json
{
  "command": "cd \"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/\" && wc -c tc.txt; tail -c 3000 tc.txt",
  "description": "Check dump tail"
}
```

## Tool (2026-10-21T04:30:31)

```
18136 tc.txt
 saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and type "Line one", press Enter, type "Line two", press Enter, type "Line three".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review starting with "Line one" in the "Reviews" list.', 'The review shows "Line one", "Line two" and "Line three" on three separate lines.', 'Condition: TCD-06-02\nTechnique: Error guessing\nMissing info: display of line breaks is not stated in any source (Q-35).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nAssumption: line breaks in a review are shown as entered until Q-35 is answered.')
('TR-07', 'TC-07-01', 'Verify that the review is not submitted when "Your review *" is empty.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Leave "Your review *" empty.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".', 'Condition: TCD-07-01\nTechnique: EP\nAssumption: wording checked for meaning, not exact text until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).')
('TR-08', 'TC-08-01', 'Verify that a review text within the allowed length is saved and shown as entered.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Soft fabric, true to size. Would buy again." in the "Reviews" list.', 'The review appears in the "Reviews" list with the text "Soft fabric, true to size. Would buy again." exactly as entered (same words, punctuation and letter case).', 'Condition: TCD-08-01\nTechnique: EP\nMissing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered.\nAssumption: the text used (43 characters) is between the minimum and the maximum length until Q-04 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.')
```

## AI (2026-10-21T04:30:38)

**Tool call `Bash`:**

```json
{
  "command": "SP=\"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\" && python -I -c \"\nimport openpyxl,sys,io\nout=io.open(sys.argv[3],'w',encoding='utf-8')\nfor f in sys.argv[1:3]:\n    wb=openpyxl.load_workbook(f)\n    for ws in wb:\n        out.write('=== %s %s %s %s\\n'%(f,ws.title,ws.dimensions,{k:v.width for k,v in ws.column_dimensions.items()}))\n        for r in ws.iter_rows():\n            vals=[c.value for c in r]\n            if any(v is not None for v in vals): out.write(repr(vals)+'\\n')\nout.close()\nprint('ok')\n\" runs/run-1/test-cases.xlsx skills/test-data-generation/assets/test-data-template.xlsx \"$SP/tc.txt\"; wc -l \"$SP/tc.txt\"",
  "description": "Dump test cases to UTF-8 file"
}
```

## Tool (2026-10-21T04:30:40)

```
ok
149 C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad/tc.txt
```

## AI (2026-10-21T04:30:43)

**Tool call `Read`:**

```json
{
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\tc.txt",
  "offset": 20,
  "allow_large": true
}
```

## Tool (2026-10-21T04:30:44)

```
20	['TR-07', 'TC-07-01', 'Verify that the review is not submitted when "Your review *" is empty.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Leave "Your review *" empty.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".', 'Condition: TCD-07-01\nTechnique: EP\nAssumption: wording checked for meaning, not exact text until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).']
21	['TR-08', 'TC-08-01', 'Verify that a review text within the allowed length is saved and shown as entered.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Soft fabric, true to size. Would buy again." in the "Reviews" list.', 'The review appears in the "Reviews" list with the text "Soft fabric, true to size. Would buy again." exactly as entered (same words, punctuation and letter case).', 'Condition: TCD-08-01\nTechnique: EP\nMissing info: minimum and maximum length not stated; the exact length is chosen when Q-04 is answered.\nAssumption: the text used (43 characters) is between the minimum and the maximum length until Q-04 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
22	['TR-08', 'TC-08-02', 'Verify that accented, non-Latin, digit, punctuation and emoji characters are saved unchanged.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Très bien, Größe M passt! 日本語 OK 100% 👍" in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Très bien, Größe M passt! 日本語 OK 100% 👍" in the "Reviews" list.', 'The review is accepted and, in the "Reviews" list, its text is shown exactly as "Très bien, Größe M passt! 日本語 OK 100% 👍" (no "?", boxes or encoded characters).', 'Condition: TCD-08-02\nTechnique: Error guessing\nAssumption: no character restriction in "Your review" until Q-37 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-37).']
23	['TR-08', 'TC-08-03', 'Verify that a review text pasted from the clipboard is saved like typed text.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). The text "Pasted review: comfy and soft." (copied from Notepad) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Ctrl+V.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Pasted review: comfy and soft." in the "Reviews" list.', 'The review appears in the "Reviews" list with the text "Pasted review: comfy and soft." exactly as pasted.', 'Condition: TCD-08-03\nTechnique: Error guessing\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
24	['TR-09', 'TC-09-01', 'Verify that a review text of exactly minimum characters is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [minimum] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Ctrl+V.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'BLOCKED — waiting for Q-04\nCondition: TCD-09-01\nTechnique: BVA\nEdge case: value exactly at the minimum.\nMissing info: minimum length not stated (Q-04).']
25	['TR-09', 'TC-09-02', 'Verify that a review text of exactly minimum + 1 characters is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [minimum + 1] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Ctrl+V.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'BLOCKED — waiting for Q-04\nCondition: TCD-09-02\nTechnique: BVA\nMissing info: minimum length not stated (Q-04).']
26	['TR-09', 'TC-09-03', 'Verify that a review text of exactly maximum - 1 characters is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum - 1] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Ctrl+V.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'BLOCKED — waiting for Q-04\nCondition: TCD-09-03\nTechnique: BVA\nMissing info: maximum length not stated (Q-04).']
27	['TR-09', 'TC-09-04', 'Verify that a review text of exactly maximum characters is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Ctrl+V.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the new review in the "Reviews" list and compare its text with the clipboard text.', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1. After step 6 the review appears in the "Reviews" list with its full text (no character cut off).', 'BLOCKED — waiting for Q-04\nCondition: TCD-09-04\nTechnique: BVA\nEdge case: value exactly at the maximum.\nMissing info: maximum length not stated (Q-04).']
28	['TR-10', 'TC-10-01', 'Verify that a review text of minimum - 1 characters is not submitted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [minimum - 1] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Ctrl+V.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".', 'BLOCKED — waiting for Q-04\nCondition: TCD-10-01\nTechnique: BVA\nPossible duplicate of TC-07-01 if Q-04 = minimum length 1.\nEdge case: one character below the minimum.\nMissing info: minimum length not stated (Q-04). If the minimum is 1, this is TCD-07-01 and is not repeated.\nMissing info: expected result not stated in any source (Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
29	['TR-10', 'TC-10-02', 'Verify that typing stops at the maximum length in "Your review *".', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum] characters (letter "a" repeated; value set when Q-04 is answered) is ready in the clipboard.', '1. Click in "Your review *" and press Ctrl+V.\n2. Press End, then type the letter "b" once.\n3. Select all text in "Your review *" (Ctrl+A), copy it and count its characters (for example in a character counter tool).', '"Your review *" holds exactly [maximum] characters and the typed "b" is not added.', 'BLOCKED — waiting for Q-04\nCondition: TCD-10-02\nTechnique: BVA\nEdge case: one character above the maximum.\nMissing info: maximum length not stated (Q-04).\nAssumption: typing stops at the maximum until Q-18 is answered.\nMissing info: expected result not stated in any source (Q-18).']
30	['TR-10', 'TC-10-03', 'Verify that pasted text of maximum + 1 characters is cut at the maximum.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum + 1] characters (letter "a" repeated, last character "b"; value set when Q-04 is answered) is ready in the clipboard.', '1. Click in "Your review *" and press Ctrl+V.\n2. Select all text in "Your review *" (Ctrl+A), copy it and count its characters.', '"Your review *" holds exactly [maximum] characters and the last character "b" is not in the box.', 'BLOCKED — waiting for Q-04\nCondition: TCD-10-03\nTechnique: BVA\nEdge case: one character above the maximum.\nMissing info: maximum length not stated (Q-04).\nAssumption: pasting stops at the maximum until Q-18 is answered.\nMissing info: expected result not stated in any source (Q-18).']
31	['TR-10', 'TC-10-04', 'Verify that pasting ten times the maximum text keeps the page usable.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of about [maximum x 10] characters (value set when Q-04 is answered) is ready in the clipboard.', '1. Click in "Your review *" and press Ctrl+V.\n2. Click in "Name *" and type "A".\n3. Select all text in "Your review *" (Ctrl+A), copy it and count its characters.', 'The page does not freeze (the "A" typed in step 2 appears in "Name *" at once) and "Your review *" holds at most [maximum] characters.', 'BLOCKED — waiting for Q-04\nCondition: TCD-10-04\nTechnique: Error guessing\nMissing info: maximum length not stated (Q-04).\nAssumption: pasting stops at the maximum until Q-18 is answered.\nMissing info: expected result not stated in any source (Q-18).']
32	['TR-11', 'TC-11-01', 'Verify that a review made only of spaces is not submitted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press the Space bar 5 times.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".', 'Condition: TCD-11-01\nTechnique: Error guessing\nEdge case: whitespace-only input.\nAssumption: a field of only spaces counts as empty until Q-17 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-17, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
33	['TR-11', 'TC-11-02', 'Verify that a review made only of line breaks is not submitted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Enter 3 times.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".', 'Condition: TCD-11-02\nTechnique: Error guessing\nEdge case: whitespace-only input.\nAssumption: line breaks are treated like spaces until Q-17 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-17, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
34	['TR-11', 'TC-11-03', 'Verify that leading and trailing spaces of a review are removed when shown.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "   Space padded review.   " (3 spaces before and after) in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Space padded review." in the "Reviews" list.\n8. Right-click the review text > Inspect, and read the text in the DevTools Elements panel.', 'The review text is "Space padded review." with no spaces before the first word or after the full stop.', 'Condition: TCD-11-03\nTechnique: Error guessing\nAssumption: spaces are trimmed until Q-17 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-17).']
35	['TR-11', 'TC-11-04', 'Verify that a review reaching the minimum length only through a trailing space is not submitted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of [minimum - 1] letters "a" followed by one space (value set when Q-04 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Ctrl+V.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Your review".', 'BLOCKED — waiting for Q-04\nCondition: TCD-11-04\nTechnique: BVA\nEdge case: length reaches the minimum only through a space.\nAssumption: length is counted after trimming until Q-17 is answered.\nMissing info: minimum length not stated (Q-04).\nMissing info: expected result not stated in any source (Q-17, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
36	['TR-12', 'TC-12-01', 'Verify that a script in "Your review *" is never run.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "<script>alert(1)</script>" in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Look at the "Reviews" list.', 'No alert dialog opens at any step. To be confirmed (Q-15): the review text is shown as plain text, removed, or the review is rejected.', 'OBSERVE ONLY — no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict)\nCondition: TCD-12-01\nTechnique: Error guessing\nMissing info: shown as plain text, removed or rejected (Q-15).\nRisk: script injection would affect every visitor of the product page.']
37	['TR-12', 'TC-12-02', 'Verify that an HTML image tag with a script in "Your review *" is not run.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "<img src=x onerror=alert(1)>" in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Look at the "Reviews" list.', 'No alert dialog opens at any step and no image or broken-image icon appears in the "Reviews" list.', 'Condition: TCD-12-02\nTechnique: Error guessing\nMissing info: handling not stated (Q-15).\nRisk: script injection through an HTML attribute.']
38	['TR-12', 'TC-12-03', 'Verify that HTML formatting in "Your review *" is not rendered as HTML.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "<b>bold</b> text check" in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Look at the "Reviews" list.', 'To be confirmed (Q-15): the word "bold" is not shown in bold type; the text is shown as plain text "<b>bold</b> text check", with the tags removed, or the review is rejected, as confirmed for Q-15.', 'OBSERVE ONLY — no verdict until Q-15 is answered\nCondition: TCD-12-03\nTechnique: Error guessing\nMissing info: handling not stated (Q-15).']
39	['TR-12', 'TC-12-04', 'Verify that a web link in "Your review *" is not turned into a clickable link.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Link check https://example.com" in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Look at the "Reviews" list.', 'To be confirmed (Q-15): in the "Reviews" list "https://example.com" is not a clickable link (the pointer does not change to a hand and clicking it opens nothing), or it is removed, or the review is rejected, as confirmed for Q-15.', 'OBSERVE ONLY — no verdict until Q-15 is answered\nCondition: TCD-12-04\nTechnique: Error guessing\nMissing info: handling of links not stated (Q-15).']
40	['TR-12', 'TC-12-05', 'Verify that a script in "Name *" is not run where the name is shown.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name script check." in "Your review *".\n3. Enter "<script>alert(1)</script>" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Look at the "Reviews" list.', 'No alert dialog opens at any step. To be confirmed (Q-15): the name is shown as plain text, removed, or the review is rejected.', 'OBSERVE ONLY — no verdict until Q-15 is answered (only for how the text is shown; "No alert dialog opens" still gets a pass/fail verdict)\nCondition: TCD-12-05\nTechnique: Error guessing\nMissing info: handling not stated (Q-05, Q-15).\nRisk: script injection through the reviewer name.']
41	['TR-13', 'TC-13-01', 'Verify that a pending review is not shown to another visitor of the product page.', 'A build that stores reviews on a server; the product page open in Chrome session A and in a second session B (another Chrome profile).', '1. In session A: Click the 4th star of "Your rating *".\n2. In session A: Enter "Pending check: other visitor." in "Your review *".\n3. In session A: Enter "Anna Smith" in "Name *".\n4. In session A: Enter "anna.smith@example.com" in "Email *".\n5. In session A: Click "Submit".\n6. In session B: reload the product page.\n7. In session B: look at the "Reviews" list.', 'The review "Pending check: other visitor." is not in the "Reviews" list of session B.', 'NOT RUN on demo-1.0 — no second visitor session; reviews exist only in the open page\nCondition: TCD-13-01\nTechnique: State transition\nRisk: unmoderated content shown publicly.\nMissing info: demo-1.0 has no sign-in and keeps data only in the open page, so "another visitor" cannot be simulated there (environment.md); check in the author\'s page per TCD-16-01.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
42	['TR-13', 'TC-13-02', 'Verify that a pending review is still not shown when the page is opened again later.', 'A build that keeps submitted reviews after the page is closed; the product page open in Chrome; no moderator action during the test.', '1. Click the 4th star of "Your rating *".\n2. Enter "Pending check: page opened again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Close the browser tab.\n7. Open the product page again in a new tab.\n8. Look at the "Reviews" list.', 'The review "Pending check: page opened again." is not in the "Reviews" list.', 'NOT RUN on demo-1.0 — a reload restores the initial data, so a pending review cannot be kept\nCondition: TCD-13-02\nTechnique: State transition\nRisk: unmoderated content shown publicly.\nMissing info: in demo-1.0 a reload restores the initial data (environment.md), so this needs a build that keeps data.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
43	['TR-14', 'TC-14-01', 'Verify that a pending review appears on the product page after it is approved.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Approval check: shown after approve." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Look at the "Reviews" list.', 'The review "Approval check: shown after approve." appears in the "Reviews" list.', 'Condition: TCD-14-01\nTechnique: State transition\nMissing info: who approves and how (Q-07).\nAssumption: in demo-1.0 the "Moderator: approve pending reviews" helper plays the moderator (environment.md).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
44	['TR-14', 'TC-14-02', 'Verify that using the approve action twice shows an approved review only once.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Approve twice check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Click "Moderator: approve pending reviews".\n8. Count the reviews with the text "Approve twice check." in the "Reviews" list.', 'The review "Approve twice check." is shown exactly once in the "Reviews" list.', 'Condition: TCD-14-02\nTechnique: State transition\nEdge case: approve twice.\nMissing info: moderation workflow (Q-07).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
45	['TR-14', 'TC-14-03', 'Verify that the approve action with no pending review adds no review.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Count the reviews in the "Reviews" list and write the number down.\n2. Click "Moderator: approve pending reviews".\n3. Count the reviews in the "Reviews" list again.', 'The number of reviews in the "Reviews" list is the same as in step 1 and no new or empty review is shown.', 'Condition: TCD-14-03\nTechnique: State transition\nEdge case: approve with nothing pending.\nMissing info: moderation workflow (Q-07).']
46	['TR-15', 'TC-15-01', 'Verify that a rejected review does not appear on the product page.', 'A build with a moderator reject action (moderation steps to be confirmed, Q-07); the product page open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Reject check: must stay hidden." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. As moderator, reject the review in the moderation tool.\n7. Reload the product page.\n8. Look at the "Reviews" list.', 'The review "Reject check: must stay hidden." is not in the "Reviews" list.', 'NOT RUN on demo-1.0 — no reject action\nCondition: TCD-15-01\nTechnique: State transition\nMissing info: whether a review can be rejected and what happens to it (Q-07). Demo-1.0 has no reject action (environment.md).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
47	['TR-15', 'TC-15-02', 'Verify that a rejected review stays hidden after other reviews are approved.', 'A build with a moderator reject action (Q-07); the product page open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Reject check: review A." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. As moderator, reject the review "Reject check: review A.".\n7. Click the 5th star of "Your rating *".\n8. Enter "Approve check: review B." in "Your review *".\n9. Enter "Ben Carter" in "Name *".\n10. Enter "ben.carter@example.com" in "Email *".\n11. Click "Submit".\n12. As moderator, approve the review "Approve check: review B.".\n13. Reload the product page.\n14. Look at the "Reviews" list.', 'The review "Reject check: review A." is not in the "Reviews" list (the review "Approve check: review B." is shown).', 'NOT RUN on demo-1.0 — no reject action\nCondition: TCD-15-02\nTechnique: State transition\nMissing info: moderation workflow (Q-07).\nRisk: rejected content shown publicly.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
48	['TR-16', 'TC-16-01', 'Verify how the author sees their own pending review right after Submit.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Author view: pending check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Look at the "Reviews" list.', 'To be confirmed (Q-08): either the review "Author view: pending check." is not in the "Reviews" list, or it is shown with a mark saying it awaits approval; it is never shown like an approved review without a mark.', "OBSERVE ONLY — no verdict until Q-08 is answered\nCondition: TCD-16-01\nTechnique: Decision table\nMissing info: author's view of a pending review not specified (Q-08).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered."]
49	['TR-16', 'TC-16-02', 'Verify that the author sees their approved review with no awaiting-approval mark.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Author view: approved check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Author view: approved check." in the "Reviews" list.', 'To be confirmed (Q-08): the review "Author view: approved check." is shown like the other approved reviews, with no "awaiting approval" mark.', 'OBSERVE ONLY — no verdict until Q-08 is answered\nCondition: TCD-16-02\nTechnique: Decision table\nMissing info: whether a pending mark exists (Q-08).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
50	['TR-17', 'TC-17-01', 'Verify that an approved review shows rating, reviewer name, date and text.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Details check: all parts shown." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Details check: all parts shown." in the "Reviews" list.', 'The review shows 4 of 5 stars, the name "Anna Smith", a date and the text "Details check: all parts shown.".', 'Condition: TCD-17-01\nTechnique: EP\nAssumption: rating, reviewer name, date and review text are shown until Q-09 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-09).']
51	['TR-17', 'TC-17-02', 'Verify that the date shown with a review is the submit date in an unambiguous format.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). Today\'s date is written down.', '1. Click the 4th star of "Your rating *".\n2. Enter "Date check: submit date." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Date check: submit date." in the "Reviews" list.\n8. Read the date shown with the review.', 'The date shown is today\'s date (the submit date), written so that day and month cannot be mixed up (for example "October 21, 2026", not "10/11/26").', 'Condition: TCD-17-02\nTechnique: EP\nAssumption: submit date in any unambiguous format until Q-24 is answered.\nMissing info: on demo-1.0 submit and approval happen on the same day, so submit date and approval date cannot be told apart (Q-24).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
52	['TR-17', 'TC-17-03', 'Verify that the reviewer name is shown in the confirmed form.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name form check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Name form check." in the "Reviews" list.\n8. Read the reviewer name shown with the review.', 'The name is shown in the confirmed form: full name "Anna Smith", first name "Anna", or initials.', "Condition: TCD-17-03\nTechnique: EP\nMissing info: form of the name not specified (Q-09).\nRisk: privacy of the reviewer's name.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nAssumption: each displayed review shows its star rating, reviewer name, date and review text until Q-09 is answered."]
53	['TR-18', 'TC-18-01', 'Verify that two reviews keep their own rating, name and text after approval.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 2nd star of "Your rating *".\n2. Enter "First review: too tight." in "Your review *".\n3. Enter "Ben Carter" in "Name *".\n4. Enter "ben.carter@example.com" in "Email *".\n5. Click "Submit".\n6. Clear "Your review *", "Name *" and "Email *" if they still contain text.\n7. Click the 5th star of "Your rating *".\n8. Enter "Second review: perfect fit." in "Your review *".\n9. Enter "Chloe Diaz" in "Name *".\n10. Enter "chloe.diaz@example.com" in "Email *".\n11. Click "Submit".\n12. Click "Moderator: approve pending reviews".\n13. Find the review "First review: too tight." in the "Reviews" list.\n14. Find the review "Second review: perfect fit." in the "Reviews" list.', 'The review "First review: too tight." shows 2 stars and the name "Ben Carter"; the review "Second review: perfect fit." shows 5 stars and the name "Chloe Diaz"; no value is swapped between them.', 'Condition: TCD-18-01\nTechnique: EP\nAssumption: the rating and the name are shown with each review until Q-09 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
54	['TR-18', 'TC-18-02', 'Verify that a name with accent, apostrophe and hyphen is shown exactly as entered.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Special name check." in "Your review *".\n3. Enter "Zoë O\'Brien-Lê" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Special name check." in the "Reviews" list.\n8. Read the reviewer name shown with the review.', 'The name is shown exactly as "Zoë O\'Brien-Lê", with no encoded characters such as "&#39;" or "&eacute;".', 'Condition: TCD-18-02\nTechnique: Error guessing\nAssumption: such names are accepted until Q-05 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-05).']
55	['TR-18', 'TC-18-03', 'Verify that the characters & < > " \' in a review are shown as typed.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter this text in "Your review *" (everything after the colon): 5 > 3 & "good" isn\'t it\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review starting with "5 > 3" in the "Reviews" list.', 'To be confirmed (Q-15): the review text is shown exactly as typed in step 2, with no "&gt;", "&amp;", "&quot;" or "&#39;" in place of the characters.', 'OBSERVE ONLY — no verdict until Q-15 is answered\nCondition: TCD-18-03\nTechnique: Error guessing\nMissing info: handling of HTML-like text (Q-15).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
56	['TR-18', 'TC-18-04', 'Verify that a maximum-length review of one long word does not break the layout.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A text of exactly [maximum] letters "a" with no spaces (value set when Q-04 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Click in "Your review *" and press Ctrl+V.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the new review in the "Reviews" list.', 'The full text is shown, wrapped inside the "Reviews" section; the page has no horizontal scroll bar and the text does not overlap other elements.', 'BLOCKED — waiting for Q-04\nCondition: TCD-18-04\nTechnique: Error guessing\nMissing info: maximum length not stated (Q-04).']
57	['TR-19', 'TC-19-01', "Verify that the reviewer's email is not shown anywhere on the visible product page.", 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email privacy check: visible page." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "unique.reviewer@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Press Ctrl+F and search for "unique.reviewer".\n8. Check where each match is.', 'No match is in the "Reviews" list, the reviewer name or the rating summary (a match inside the "Email *" input itself, if the form keeps the value, does not count).', 'Condition: TCD-19-01\nTechnique: Error guessing\nRisk: personal data could be shown publicly.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
58	['TR-19', 'TC-19-02', "Verify that the reviewer's email is not in hidden parts of the displayed review.", 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email privacy check: hidden parts." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "unique.reviewer@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Email privacy check: hidden parts." in the "Reviews" list.\n8. Hover over the reviewer name and wait 2 seconds.\n9. Right-click the reviewer name > Inspect.\n10. In the DevTools Elements panel press Ctrl+F and search for "unique.reviewer".', 'No tooltip shows the email, the reviewer name is not a "mailto:" link, and the Elements search finds "unique.reviewer" only in the "Email *" input (if the form keeps the value), not in the "Reviews" section.', 'Condition: TCD-19-02\nTechnique: Error guessing\nRisk: personal data could be read by anyone viewing the page source.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
59	['TR-20', 'TC-20-01', 'Verify that approved reviews are listed in the confirmed order.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). At least 3 approved reviews with different dates and ratings are listed (initial data of demo-1.0).', '1. Look at the "Reviews" list.\n2. Write down the date and the rating of each review from top to bottom.', 'To be confirmed (Q-10): the reviews are in the confirmed order (for example newest date first).', 'OBSERVE ONLY — no verdict until Q-10 is answered\nCondition: TCD-20-01\nTechnique: EP\nMissing info: list order not specified (Q-10).']
60	['TR-20', 'TC-20-02', 'Verify that a newly approved review appears in the position the order requires.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). At least 3 approved reviews with different dates and ratings are listed (initial data of demo-1.0).', '1. Click the 4th star of "Your rating *".\n2. Enter "Order check: newly approved." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Note the position of the review "Order check: newly approved." in the "Reviews" list.', 'To be confirmed (Q-10): the review "Order check: newly approved." is in the position the confirmed order requires (for example first, if newest first).', 'OBSERVE ONLY — no verdict until Q-10 is answered\nCondition: TCD-20-02\nTechnique: Error guessing\nMissing info: list order not specified (Q-10).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
61	['TR-20', 'TC-20-03', 'Verify that two reviews with same date and rating keep a stable order on reopening.', 'A build that keeps reviews after the page is closed; the product page open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Tie check A." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Clear "Your review *", "Name *" and "Email *" if they still contain text.\n7. Click the 4th star of "Your rating *".\n8. Enter "Tie check B." in "Your review *".\n9. Enter "Ben Carter" in "Name *".\n10. Enter "ben.carter@example.com" in "Email *".\n11. Click "Submit".\n12. Click "Moderator: approve pending reviews".\n13. Note the order of "Tie check A." and "Tie check B." in the "Reviews" list.\n14. Close the tab and open the product page again.\n15. Note the order of "Tie check A." and "Tie check B." again.', 'To be confirmed (Q-10): the two reviews are in the same order in steps 11 and 13, and that order follows the confirmed tie rule.', 'NOT RUN on demo-1.0 — a reload restores the initial data\nCondition: TCD-20-03\nTechnique: Error guessing\nEdge case: tie in the sort key.\nMissing info: list order not specified (Q-10).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
62	['TR-21', 'TC-21-01', 'Verify that all 50 approved reviews of a product can be seen.', 'The product page open in Chrome with exactly 50 approved reviews (on demo-1.0: submit and approve 47 reviews in one session on top of the 3 initial ones, without reloading).', '1. Scroll through the whole "Reviews" list.\n2. Count the reviews shown.', 'All 50 approved reviews are shown on the page (count = 50) with no paging control needed.', 'NOT RUN on demo-1.0 — needs 50 approved reviews; creating 47 by hand is not done this round\nCondition: TCD-21-01\nTechnique: EP\nEdge case: large number of approved reviews.\nAssumption: all approved reviews are shown on one page until Q-23 is answered.\nMissing info: expected result not stated in any source (Q-23).']
63	['TR-21', 'TC-21-02', 'Verify paging with exactly page size - 1 approved reviews.', 'The product page open in Chrome with exactly [page size - 1] approved reviews (page size set when Q-23 is answered).', '1. Look at the "Reviews" list and any paging control or "Load more" below it.\n2. Count the reviews on the first page.', 'All [page size - 1] reviews are on the first page and no paging control or "Load more" is shown.', 'BLOCKED — waiting for Q-23\nCondition: TCD-21-02\nTechnique: BVA\nPossible duplicate of TC-21-01 if Q-23 = no paging (all reviews on one page).\nMissing info: whether paging exists and the page size (Q-23).\nAssumption: all approved reviews are shown on one page until Q-23 is answered.']
64	['TR-21', 'TC-21-03', 'Verify paging with exactly page size approved reviews.', 'The product page open in Chrome with exactly [page size] approved reviews (page size set when Q-23 is answered).', '1. Look at the "Reviews" list and any paging control or "Load more" below it.\n2. Count the reviews on the first page.', 'All [page size] reviews are on the first page and no paging control or "Load more" is shown.', 'BLOCKED — waiting for Q-23\nCondition: TCD-21-03\nTechnique: BVA\nPossible duplicate of TC-21-01 if Q-23 = no paging (all reviews on one page).\nEdge case: count exactly at the page size.\nMissing info: page size (Q-23).\nAssumption: all approved reviews are shown on one page until Q-23 is answered.']
65	['TR-21', 'TC-21-04', 'Verify paging with exactly page size + 1 approved reviews.', 'The product page open in Chrome with exactly [page size + 1] approved reviews (page size set when Q-23 is answered).', '1. Look at the "Reviews" list and any paging control or "Load more" below it.\n2. Count the reviews on the first page.', 'The first page shows [page size] reviews and the last review is reached through the paging control or "Load more".', 'BLOCKED — waiting for Q-23\nCondition: TCD-21-04\nTechnique: BVA\nPossible duplicate of TC-21-01 if Q-23 = no paging (all reviews on one page).\nEdge case: one above the page size.\nMissing info: page size (Q-23).\nAssumption: all approved reviews are shown on one page until Q-23 is answered.']
66	['TR-22', 'TC-22-01', 'Verify that a product with no approved reviews shows a no-reviews message.', 'A product with 0 approved reviews open in Chrome.', '1. Look at the "Reviews" section.', 'A short message says there are no reviews yet, and no review is listed.', 'NOT RUN on demo-1.0 — the only product starts with approved reviews\nCondition: TCD-22-01\nTechnique: BVA\nEdge case: product with no approved reviews.\nAssumption: a short message saying there are no reviews yet until Q-25 is answered.\nMissing info: demo-1.0 has one product that starts with approved reviews (app-note.md); a product with 0 approved reviews may not be available.\nMissing info: expected result not stated in any source (Q-25).']
67	['TR-22', 'TC-22-02', 'Verify that the no-reviews message stays while the only review is pending.', 'A product with 0 approved reviews open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Empty state check: pending only." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Look at the "Reviews" section.', 'The message saying there are no reviews yet is still shown and no review is listed.', 'NOT RUN on demo-1.0 — the only product starts with approved reviews\nCondition: TCD-22-02\nTechnique: EP\nEdge case: only pending reviews.\nAssumption: empty-state message until Q-25 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-25).']
68	['TR-22', 'TC-22-03', 'Verify that the no-reviews message disappears when the first review is approved.', 'A product with 0 approved reviews open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Empty state check: first approved." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Look at the "Reviews" section.', 'The no-reviews message is no longer shown and the review "Empty state check: first approved." is listed.', 'NOT RUN on demo-1.0 — the only product starts with approved reviews\nCondition: TCD-22-03\nTechnique: BVA\nAssumption: empty-state message until Q-25 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-25).']
69	['TR-23', 'TC-23-01', 'Verify that an approved review is included in the average rating and review count.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). The rating summary next to the product name (average and count) and the ratings of all listed reviews are written down.', '1. Click the 1st star of "Your rating *".\n2. Enter "Summary check: approved 1 star." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Read the rating summary next to the product name.', 'To be confirmed (Q-11): the review count is 1 higher than before, and the average equals the sum of all approved ratings (including the new 1) divided by the new count, rounded as confirmed.', 'OBSERVE ONLY — no verdict until Q-11 is answered\nCondition: TCD-23-01\nTechnique: Decision table\nMissing info: whether a summary is shown and how it is rounded (Q-11).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
70	['TR-23', 'TC-23-02', 'Verify that a pending review does not change the average rating or review count.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). The rating summary next to the product name (average and count) and the ratings of all listed reviews are written down.', '1. Click the 1st star of "Your rating *".\n2. Enter "Summary check: pending 1 star." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Read the rating summary next to the product name.', 'To be confirmed (Q-11): the average rating and the review count are the same as written down before step 1.', 'OBSERVE ONLY — no verdict until Q-11 is answered\nCondition: TCD-23-02\nTechnique: Decision table\nMissing info: Q-11.\nRisk: pending reviews could change the score shown to shoppers.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
71	['TR-23', 'TC-23-03', 'Verify that a rejected review does not change the average rating or review count.', 'A build with a moderator reject action (Q-07); the rating summary (average and count) written down.', '1. Click the 1st star of "Your rating *".\n2. Enter "Summary check: rejected 1 star." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. As moderator, reject the review.\n7. Reload the product page.\n8. Read the rating summary next to the product name.', 'To be confirmed (Q-11): the average rating and the review count are the same as written down before step 1.', 'NOT RUN on demo-1.0 — no reject action\nCondition: TCD-23-03\nTechnique: Decision table\nMissing info: Q-07, Q-11.\nRisk: rejected reviews could change the score shown to shoppers.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
72	['TR-23', 'TC-23-04', 'Verify that the review count shown equals the number of approved reviews listed.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Summary check: count." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Count the reviews in the "Reviews" list.\n8. Read the review count in the rating summary next to the product name.', 'To be confirmed (Q-11): the count in the rating summary equals the number of reviews counted in the "Reviews" list.', 'OBSERVE ONLY — no verdict until Q-11 is answered\nCondition: TCD-23-04\nTechnique: EP\nMissing info: whether a count is shown (Q-11).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
73	['TR-23', 'TC-23-05', 'Verify that an average falling exactly on a rounding step is shown with the confirmed rounding.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). The "Reviews" list shows exactly 3 approved reviews rated 5, 4 and 3 (initial data; check before step 1).', '1. Click the 2nd star of "Your rating *".\n2. Enter "Rounding check: two stars." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Read the average in the rating summary next to the product name.', 'To be confirmed (Q-11): the approved ratings are 5, 4, 3 and 2 (exact average 3.5) and the average is shown as 3.5, or rounded as the confirmed rule says.', 'OBSERVE ONLY — no verdict until Q-11 is answered\nCondition: TCD-23-05\nTechnique: BVA\nMissing info: rounding rule not stated (Q-11); exact boundary values are set when Q-11 is answered.\nMissing info: values next to the rounding step (for example 4.33) are added when Q-11 gives the rounding rule.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
74	['TR-23', 'TC-23-06', 'Verify that the rating summary shows no wrong value when there are no approved reviews.', 'A product with 0 approved reviews open in Chrome.', '1. Read the rating summary next to the product name.', 'To be confirmed (Q-11, Q-25): the summary shows no average or an empty state; it never shows "NaN", "0 stars" or a number without reviews.', 'NOT RUN on demo-1.0 — the only product starts with approved reviews\nCondition: TCD-23-06\nTechnique: Error guessing\nEdge case: no approved reviews.\nMissing info: Q-11, Q-25.']
75	['TR-24', 'TC-24-01', "Verify that a review approved for product A appears on product A's page.", 'A build with two products A and B; the page of product A open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Product check: written for A." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. As moderator, approve the review.\n7. Reload the page of product A.\n8. Look at the "Reviews" list.', 'The review "Product check: written for A." is in the "Reviews" list of product A.', 'NOT RUN on demo-1.0 — one product only\nCondition: TCD-24-01\nTechnique: EP\nPossible duplicate of TC-14-01 if the build under test has only one product.\nCovered in demo-1.0 by TCD-14-01 (one product only).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
76	['TR-24', 'TC-24-02', "Verify that a review written for product A does not appear on product B's page.", 'A build with two products A and B; the page of product A open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Product check: not on B." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. As moderator, approve the review.\n7. Open the page of product B.\n8. Look at the "Reviews" list.', 'The review "Product check: not on B." is not in the "Reviews" list of product B.', 'NOT RUN on demo-1.0 — one product only\nCondition: TCD-24-02\nTechnique: EP\nRisk: reviews shown on the wrong product mislead shoppers.\nMissing info: demo-1.0 has one product only (app-note.md); needs a build with two products.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
77	['TR-25', 'TC-25-01', 'Verify that the form heading reads "ADD A REVIEW".', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Scroll to the review form.\n2. Read the heading of the form.', 'The heading reads "ADD A REVIEW"; letter case is not compared (for example "Add a review" also passes).', 'Condition: TCD-25-01\nTechnique: EP\nMissing info: expected result not stated in any source (Q-32).\nAssumption: compared without letter case until Q-32 is answered.']
78	['TR-25', 'TC-25-02', 'Verify that the info text above the form matches mockup-1.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Scroll to the review form.\n2. Read the text under the form heading.', 'The text reads exactly "Your email address will not be published. Required fields are marked *".', 'Condition: TCD-25-02\nTechnique: EP']
79	['TR-25', 'TC-25-03', 'Verify that the four field labels are shown, each with the required marker *.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Scroll to the review form.\n2. Read the label of each field.', 'The labels "Your rating *", "Your review *", "Name *" and "Email *" are shown, each ending with the required marker *.', 'Condition: TCD-25-03\nTechnique: EP']
80	['TR-25', 'TC-25-04', 'Verify that the save checkbox text matches mockup-1.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Scroll to the review form.\n2. Read the text next to the checkbox.', 'The text reads exactly "Save my name, email, and website in this browser for the next time I comment."', 'Condition: TCD-25-04\nTechnique: EP\nMissing info: final text of the save checkbox (Q-13).']
81	['TR-25', 'TC-25-05', 'Verify that a "Submit" button is shown below the save checkbox.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Scroll to the review form.\n2. Look below the save checkbox.', 'A button labelled "Submit" is shown below the save checkbox.', 'Condition: TCD-25-05\nTechnique: EP']
82	['TR-25', 'TC-25-06', 'Verify that the form elements are in the mockup-1 order.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Scroll to the review form.\n2. Write down the elements from top to bottom.', 'The order is: heading, info text, "Your rating *", "Your review *", "Name *", "Email *", save checkbox, "Submit".', 'Condition: TCD-25-06\nTechnique: EP']
83	['TR-25', 'TC-25-07', 'Verify that Tab moves through the form in screen order and Submit works by keyboard.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click on the info text "Your email address will not be published. Required fields are marked *".\n2. Press Tab repeatedly and note which control gets the focus each time.\n3. When "Submit" has the focus, press Enter.', 'The focus moves in this order: rating stars, "Your review *", "Name *", "Email *", save checkbox, "Submit"; pressing Enter on "Submit" submits the form (with empty fields: the form is checked and the review is not submitted).', 'Condition: TCD-25-07\nTechnique: Error guessing\nMissing info: keyboard use is not stated in any source (Q-34).\nAssumption: the rating, fields, checkbox and Submit can be used with the keyboard alone, and Tab follows the order shown on screen until Q-34 is answered.']
84	['TR-26', 'TC-26-01', 'Verify that a signed-in customer who bought the product can submit a review.', 'A build with sign-in and orders; signed in as a test customer with a delivered order of this product; product page open.', '1. Click the 4th star of "Your rating *".\n2. Enter "Permission check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-01): the review is submitted: a confirmation message appears above the form and the review waits for approval.', 'NOT RUN on demo-1.0 — no sign-in or orders\nCondition: TCD-26-01\nTechnique: Decision table\nMissing info: sign-in and purchase check not specified (Q-01).\nMissing info: demo-1.0 has no sign-in (environment.md).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
85	['TR-26', 'TC-26-02', 'Verify that a signed-in customer who did not buy the product cannot submit a review.', 'A build with sign-in and orders; signed in as a test customer with no order of this product; product page open.', '1. Scroll to the review form.\n2. If the form is shown and enabled: Click the 4th star of "Your rating *". Enter "Permission check." in "Your review *". Enter "Anna Smith" in "Name *". Enter "anna.smith@example.com" in "Email *". Click "Submit".', 'To be confirmed (Q-01): the form is hidden, or disabled, or Submit is rejected with a message; no review is created.', 'NOT RUN on demo-1.0 — no sign-in or orders\nCondition: TCD-26-02\nTechnique: Decision table\nMissing info: Q-01.\nRisk: non-buyers could post fake reviews.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
86	['TR-26', 'TC-26-03', 'Verify that a guest (not signed in) cannot submit a review.', 'A build with sign-in; not signed in (guest); product page open.', '1. Scroll to the review form.\n2. If the form is shown and enabled: Click the 4th star of "Your rating *". Enter "Permission check." in "Your review *". Enter "Anna Smith" in "Name *". Enter "anna.smith@example.com" in "Email *". Click "Submit".', 'To be confirmed (Q-01): the form is hidden, or disabled, or Submit is rejected with a message; no review is created.', 'NOT RUN on demo-1.0 — no sign-in\nCondition: TCD-26-03\nTechnique: Decision table\nMissing info: Q-01.\nRisk: guests could post fake reviews.\nMissing info: demo-1.0 has no sign-in, so every visitor is a guest; whether demo-1.0 should allow guests depends on Q-01.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
87	['TR-26', 'TC-26-04', 'Verify review permission for a customer whose order was cancelled or refunded.', 'A build with sign-in and orders; signed in as a test customer whose only order of this product was cancelled or refunded; product page open.', '1. Scroll to the review form.\n2. If the form is shown and enabled: Click the 4th star of "Your rating *". Enter "Permission check." in "Your review *". Enter "Anna Smith" in "Name *". Enter "anna.smith@example.com" in "Email *". Click "Submit".', 'To be confirmed (Q-01, Q-33): the customer can or cannot submit, as confirmed; if not, the form is hidden, disabled or Submit is rejected with a message.', 'NOT RUN on demo-1.0 — no sign-in or orders\nCondition: TCD-26-04\nTechnique: Error guessing\nEdge case: cancelled or refunded purchase.\nMissing info: cancelled or refunded purchase not specified (Q-33).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-01).']
88	['TR-27', 'TC-27-01', 'Verify how Name and Email are handled for a signed-in customer.', 'A build with sign-in; signed in as test customer "Anna Smith" (anna.smith@example.com); product page open.', '1. Scroll to the review form.\n2. Look at "Name *" and "Email *".', 'To be confirmed (Q-02): Name and Email are prefilled from the account, or prefilled and editable, or not shown, as confirmed.', 'NOT RUN on demo-1.0 — no sign-in\nCondition: TCD-27-01\nTechnique: EP\nMissing info: conflict between the story and mockup-1 (Q-02).']
89	['TR-27', 'TC-27-02', 'Verify which name is displayed when a signed-in customer edits a prefilled Name.', 'A build with sign-in where Name is prefilled and editable (Q-02); signed in as test customer "Anna Smith"; product page open.', '1. Click the 4th star of "Your rating *".\n2. Enter "Edited name check." in "Your review *".\n3. Replace the text in "Name *" with "Anna S."\n4. Click "Submit".\n5. As moderator, approve the review.\n6. Reload the product page.\n7. Find the review "Edited name check." in the "Reviews" list.', 'To be confirmed (Q-02): the review shows the name confirmed for Q-02 ("Anna S." if the edited name is used, "Anna Smith" if the account name is used).', 'NOT RUN on demo-1.0 — no sign-in\nCondition: TCD-27-02\nTechnique: EP\nMissing info: Q-02.']
90	['TR-28', 'TC-28-01', 'Verify that the review is not submitted when "Name *" is empty.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Leave "Name *" empty.\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Name".', 'Condition: TCD-28-01\nTechnique: EP\nAssumption: wording checked for meaning, not exact text until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).']
91	['TR-29', 'TC-29-01', 'Verify that a Name of Latin letters and a space is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name check 29-01." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'Condition: TCD-29-01\nTechnique: EP\nAssumption: letters and spaces are allowed until Q-05 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-05).']
92	['TR-29', 'TC-29-02', 'Verify that a Name with accented letters is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name check 29-02." in "Your review *".\n3. Enter "Zoë Lê" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'Condition: TCD-29-02\nTechnique: EP\nEdge case: accented letters.\nAssumption: accented letters are allowed until Q-05 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-05).']
93	['TR-29', 'TC-29-03', 'Verify that a Name with a hyphen and an apostrophe is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name check 29-03." in "Your review *".\n3. Enter "Mary-Jane O\'Neil" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'Condition: TCD-29-03\nTechnique: EP\nEdge case: hyphen and apostrophe.\nAssumption: hyphens and apostrophes are allowed until Q-05 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-05).']
94	['TR-29', 'TC-29-04', 'Verify whether a Name in a non-Latin script is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name check 29-04." in "Your review *".\n3. Enter "李明" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-05): either the review is submitted (confirmation message, "Pending approval" 1) or it is rejected with an error naming "Name", as confirmed.', 'OBSERVE ONLY — no verdict until Q-05 is answered\nCondition: TCD-29-04\nTechnique: EP\nMissing info: allowed characters not stated (Q-05).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
95	['TR-29', 'TC-29-05', 'Verify whether a Name containing digits is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name check 29-05." in "Your review *".\n3. Enter "Anna2" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-05): either the review is submitted (confirmation message, "Pending approval" 1) or it is rejected with an error naming "Name", as confirmed.', 'OBSERVE ONLY — no verdict until Q-05 is answered\nCondition: TCD-29-05\nTechnique: EP\nMissing info: whether digits are allowed (Q-05).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
96	['TR-29', 'TC-29-06', 'Verify that a Name made only of symbols is rejected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name check 29-06." in "Your review *".\n3. Enter "@#$%" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-05, Q-20): The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Name".', 'OBSERVE ONLY — no verdict until Q-05 and Q-20 are answered\nCondition: TCD-29-06\nTechnique: EP\nMissing info: allowed characters not stated (Q-05).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).']
97	['TR-29', 'TC-29-07', 'Verify that a Name of 1 character is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name check 29-07." in "Your review *".\n3. Enter "A" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-05): The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'OBSERVE ONLY — no verdict until Q-05 is answered\nCondition: TCD-29-07\nTechnique: BVA\nEdge case: shortest non-empty name.\nMissing info: minimum length not stated (Q-05).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
98	['TR-29', 'TC-29-08', 'Verify the Name length of exactly maximum - 1 characters.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A name of exactly [maximum - 1] letters "a" (value set when Q-05 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Enter "Name length check 29-08." in "Your review *".\n3. Click in "Name *" and press Ctrl+V.\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'BLOCKED — waiting for Q-05\nCondition: TCD-29-08\nTechnique: BVA\nMissing info: maximum length not stated (Q-05).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
99	['TR-29', 'TC-29-09', 'Verify the Name length of exactly maximum characters.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A name of exactly [maximum] letters "a" (value set when Q-05 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Enter "Name length check 29-09." in "Your review *".\n3. Click in "Name *" and press Ctrl+V.\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Name length check 29-09." in the "Reviews" list.', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1. After approval the full name is shown with the review.', 'BLOCKED — waiting for Q-05\nCondition: TCD-29-09\nTechnique: BVA\nEdge case: Name at the maximum length.\nMissing info: maximum length not stated (Q-05).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
100	['TR-29', 'TC-29-10', 'Verify the Name length of exactly maximum + 1 characters.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). A name of exactly [maximum + 1] letters "a" (value set when Q-05 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Enter "Name length check 29-10." in "Your review *".\n3. Click in "Name *" and press Ctrl+V.\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', '"Name *" holds exactly [maximum] characters after the paste; the extra character is not added.', 'BLOCKED — waiting for Q-05\nCondition: TCD-29-10\nTechnique: BVA\nEdge case: one character above the maximum.\nMissing info: maximum length and over-length behaviour not stated (Q-05, Q-18).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nAssumption: typing and pasting stop at the maximum length until Q-18 is answered.']
101	['TR-30', 'TC-30-01', 'Verify that the review is not submitted when "Email *" is empty.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Leave "Email *" empty.\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".', 'Condition: TCD-30-01\nTechnique: EP\nAssumption: wording checked for meaning, not exact text until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).']
102	['TR-31', 'TC-31-01', 'Verify that the email "anna.smith@example.com" is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-01." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'Condition: TCD-31-01\nTechnique: EP\nAssumption: standard format text@domain.tld until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06).']
103	['TR-31', 'TC-31-02', 'Verify that an email with a plus sign and a sub-domain is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-02." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna+shop@mail.example.com" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'Condition: TCD-31-02\nTechnique: EP\nEdge case: plus sign and sub-domain.\nAssumption: standard format until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06).']
104	['TR-31', 'TC-31-03', 'Verify that an email without "@" is rejected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-03." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".', 'Condition: TCD-31-03\nTechnique: EP\nAssumption: standard format until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
105	['TR-31', 'TC-31-04', 'Verify that an email with nothing before "@" is rejected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-04." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".', 'Condition: TCD-31-04\nTechnique: EP\nAssumption: standard format until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
106	['TR-31', 'TC-31-05', 'Verify that an email with no domain after "@" is rejected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-05." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna@" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".', 'Condition: TCD-31-05\nTechnique: EP\nAssumption: standard format until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
107	['TR-31', 'TC-31-06', 'Verify that an email without a top-level domain is rejected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-06." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna@example" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".', 'Condition: TCD-31-06\nTechnique: EP\nAssumption: a top-level domain is required; some format rules accept this value until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
108	['TR-31', 'TC-31-07', 'Verify that an email with two "@" is rejected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-07." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna@@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".', 'Condition: TCD-31-07\nTechnique: EP\nAssumption: standard format until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
109	['TR-31', 'TC-31-08', 'Verify that an email with a space inside is rejected.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-08." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".', 'Condition: TCD-31-08\nTechnique: EP\nAssumption: standard format until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
110	['TR-31', 'TC-31-09', 'Verify that an email in upper case is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email check 31-09." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "ANNA@EXAMPLE.COM" in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'Condition: TCD-31-09\nTechnique: Error guessing\nAssumption: letter case does not matter until Q-06 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-06).']
111	['TR-31', 'TC-31-10', 'Verify the Email length of exactly maximum - 1 characters.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). An email of exactly [maximum - 1] characters: letters "a" followed by "@example.com" (value set when Q-06 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Enter "Email length check 31-10." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Click in "Email *" and press Ctrl+V.\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'BLOCKED — waiting for Q-06\nCondition: TCD-31-10\nTechnique: BVA\nMissing info: maximum length not stated (Q-06).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
112	['TR-31', 'TC-31-11', 'Verify the Email length of exactly maximum characters.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). An email of exactly [maximum] characters: letters "a" followed by "@example.com" (value set when Q-06 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Enter "Email length check 31-11." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Click in "Email *" and press Ctrl+V.\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'BLOCKED — waiting for Q-06\nCondition: TCD-31-11\nTechnique: BVA\nEdge case: value exactly at the maximum.\nMissing info: maximum length not stated (Q-06).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
113	['TR-31', 'TC-31-12', 'Verify the Email length of exactly maximum + 1 characters.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). An email of exactly [maximum + 1] characters: letters "a" followed by "@example.com" (value set when Q-06 is answered) is ready in the clipboard.', '1. Click the 4th star of "Your rating *".\n2. Enter "Email length check 31-12." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Click in "Email *" and press Ctrl+V.\n5. Click "Submit".', '"Email *" holds exactly [maximum] characters after the paste; the extra character is not added.', 'BLOCKED — waiting for Q-06\nCondition: TCD-31-12\nTechnique: BVA\nEdge case: one character above the maximum.\nMissing info: maximum length and over-length behaviour not stated (Q-06, Q-18).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nAssumption: typing and pasting stop at the maximum length until Q-18 is answered.']
114	['TR-32', 'TC-32-01', 'Verify that leading and trailing spaces in Name are removed when shown.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Name trim check." in "Your review *".\n3. Enter "  Anna Smith  " (2 spaces before and after) in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click "Moderator: approve pending reviews".\n7. Find the review "Name trim check." in the "Reviews" list.\n8. Right-click the reviewer name > Inspect, and read the name in the DevTools Elements panel.', 'The review is accepted and the name is shown as "Anna Smith", with no spaces before or after it.', 'Condition: TCD-32-01\nTechnique: Error guessing\nEdge case: space-padded input.\nAssumption: spaces are trimmed until Q-17 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-17).']
115	['TR-32', 'TC-32-02', 'Verify that a Name made only of spaces is treated as empty.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Click in "Name *" and press the Space bar 5 times.\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Name".', 'Condition: TCD-32-02\nTechnique: Error guessing\nEdge case: whitespace-only input.\nAssumption: a field of only spaces counts as empty until Q-17 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-17, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
116	['TR-32', 'TC-32-03', 'Verify that an Email with leading and trailing spaces is accepted.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Email trim check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "  anna@example.com  " (2 spaces before and after) in "Email *".\n5. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'Condition: TCD-32-03\nTechnique: Error guessing\nEdge case: space-padded input.\nAssumption: spaces are trimmed until Q-17 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-17).']
117	['TR-32', 'TC-32-04', 'Verify that an Email made only of spaces is treated as empty.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Click in "Email *" and press the Space bar 5 times.\n5. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. An error message names "Email".', 'Condition: TCD-32-04\nTechnique: Error guessing\nEdge case: whitespace-only input.\nAssumption: a field of only spaces counts as empty until Q-17 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-17, Q-20).\nAssumption: each error message names its field; wording is checked for meaning, not exact text until Q-20 is answered.']
118	['TR-33', 'TC-33-01', 'Verify that a valid review is submitted with the save checkbox not ticked.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Leave the checkbox "Save my name, email, and website in this browser for the next time I comment." not ticked.\n6. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1. The message says the review was received and waits for approval.', 'Condition: TCD-33-01\nTechnique: Decision table\nAssumption: confirmation says the review was received and waits for approval until Q-21 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-21).']
119	['TR-33', 'TC-33-02', 'Verify that a valid review is submitted with the save checkbox ticked.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."\n6. Click "Submit".', 'The review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1. The message says the review was received and waits for approval.', 'Condition: TCD-33-02\nTechnique: Decision table\nAssumption: confirmation text until Q-21 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-21).']
120	['TR-34', 'TC-34-01', 'Verify that submitting an empty form names all four required fields.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Leave "Your rating *", "Your review *", "Name *" and "Email *" empty.\n2. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. The error messages name all four fields: rating, "Your review", "Name" and "Email".', 'Condition: TCD-34-01\nTechnique: Decision table\nAssumption: each error names its field; wording checked for meaning until Q-20 is answered.\nMissing info: expected result not stated in any source (Q-20).']
121	['TR-34', 'TC-34-02', 'Verify that only the empty rating and review are named when Name and Email are valid.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Leave "Your rating *" and "Your review *" empty.\n2. Enter "Anna Smith" in "Name *".\n3. Enter "anna.smith@example.com" in "Email *".\n4. Click "Submit".', 'The review is not submitted: no confirmation message appears and "Pending approval" stays 0. The error messages name the rating and "Your review" only; "Name" and "Email" are not named.', 'Condition: TCD-34-02\nTechnique: Decision table\nAssumption: wording checked for meaning until Q-20 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-20).']
122	['TR-34', 'TC-34-03', 'Verify that entered values are kept after a rejected Submit and correction submits.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Leave "Your review *" empty.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Check that the rating, "Name *" and "Email *" still hold the values entered.\n7. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n8. Click "Submit".', 'After step 5 the 4 stars, "Anna Smith" and "anna.smith@example.com" are still in the form, and after step 7 the review is submitted: a confirmation message appears above the form and "Pending approval" changes from 0 to 1.', 'Condition: TCD-34-03\nTechnique: Decision table\nAssumption: entered values are kept after a rejected submit until Q-38 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-38).']
123	['TR-34', 'TC-34-04', 'Verify that leaving a required field empty shows no error until Submit.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click in "Name *".\n2. Press Tab to move to "Email *" without typing.\n3. Look at the form and the area above it.', 'No error message is shown for "Name" (or any field) before "Submit" is clicked.', 'Condition: TCD-34-04\nTechnique: EP\nAssumption: fields are checked on Submit only until Q-19 is answered.\nMissing info: expected result not stated in any source (Q-19).']
124	['TR-35', 'TC-35-01', 'Verify that the form is fully cleared after a successful Submit without saving.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Leave the checkbox "Save my name, email, and website in this browser for the next time I comment." not ticked.\n6. Click "Submit".\n7. Look at the page and the form.', 'The product page stays open (product name and "Reviews" still shown, no new page), no star is selected, and "Your review *", "Name *" and "Email *" are empty.', 'Condition: TCD-35-01\nTechnique: State transition\nAssumption: form cleared until Q-22 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-22).']
125	['TR-35', 'TC-35-02', 'Verify that Name and Email stay filled after a successful Submit with saving ticked.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "Soft fabric, true to size. Would buy again." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."\n6. Click "Submit".\n7. Look at the page and the form.', 'The product page stays open, no star is selected, "Your review *" is empty, and "Name *" and "Email *" still show "Anna Smith" and "anna.smith@example.com".', 'Condition: TCD-35-02\nTechnique: State transition\nAssumption: Name and Email stay filled only if the checkbox was ticked until Q-22 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-22).']
126	['TR-36', 'TC-36-01', 'Verify that the save checkbox is not ticked on a first visit.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Scroll to the review form.\n2. Look at the checkbox "Save my name, email, and website in this browser for the next time I comment."', 'The checkbox is not ticked.', 'Condition: TCD-36-01\nTechnique: EP']
127	['TR-36', 'TC-36-02', 'Verify the save checkbox state on a return visit after Name and Email were saved.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "Return visit check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."\n6. Click "Submit".\n7. Reload the page (F5).\n8. Look at the checkbox "Save my name, email, and website in this browser for the next time I comment."', 'To be confirmed (Q-14): the checkbox is ticked or not ticked, as confirmed.', 'OBSERVE ONLY — no verdict until Q-14 is answered\nCondition: TCD-36-02\nTechnique: EP\nEdge case: checkbox state on a return visit.\nMissing info: not stated (Q-14).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
128	['TR-37', 'TC-37-01', 'Verify that ticked saving refills Name and Email on the next visit.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "Save check: first visit." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."\n6. Click "Submit".\n7. Close the tab and open exam/app/index.html again in the same Chrome window.\n8. Look at "Name *" and "Email *".', '"Name *" shows "Anna Smith" and "Email *" shows "anna.smith@example.com".', 'Condition: TCD-37-01\nTechnique: State transition\nAssumption: only name and email are saved until Q-13 and Q-14 are answered.\nRisk: personal data stored on the device.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
129	['TR-37', 'TC-37-02', 'Verify that a new ticked Submit replaces the saved Name and Email.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). Name "Anna Smith" and Email "anna.smith@example.com" are saved in this browser (TC-37-01 done; they are filled on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Save check: replace." in "Your review *".\n3. Replace the text in "Name *" with "Ben Carter".\n4. Replace the text in "Email *" with "ben.carter@example.com".\n5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment." (tick it if it is not ticked)\n6. Click "Submit".\n7. Reload the page (F5).\n8. Look at "Name *" and "Email *".', '"Name *" shows "Ben Carter" and "Email *" shows "ben.carter@example.com".', 'Condition: TCD-37-02\nTechnique: State transition\nAssumption: saved values are replaced until Q-14 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-14).']
130	['TR-37', 'TC-37-03', 'Verify what happens to saved data after a Submit with the box not ticked.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). Name "Anna Smith" and Email "anna.smith@example.com" are saved in this browser (they are filled on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Save check: untick." in "Your review *".\n3. Untick the checkbox "Save my name, email, and website in this browser for the next time I comment." if it is ticked.\n4. Click "Submit".\n5. Reload the page (F5).\n6. Look at "Name *" and "Email *".', 'To be confirmed (Q-14): "Name *" and "Email *" are filled or empty, as confirmed for Q-14.', 'OBSERVE ONLY — no verdict until Q-14 is answered\nCondition: TCD-37-03\nTechnique: State transition\nMissing info: how saved data is removed (Q-14).\nRisk: personal data left on a shared device.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
131	['TR-37', 'TC-37-04', 'Verify that only Name and Email are refilled, not rating or review.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "Save check: only name and email." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."\n6. Click "Submit".\n7. Reload the page (F5).\n8. Look at the whole form.', 'Only "Name *" and "Email *" are filled; no star is selected and "Your review *" is empty.', 'Condition: TCD-37-04\nTechnique: EP\nAssumption: only name and email are saved until Q-13 and Q-14 are answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-13, Q-14).']
132	['TR-37', 'TC-37-05', 'Verify that saved Name and Email are not filled in a private window.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "Save check: private window." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."\n6. Click "Submit".\n7. Open a Chrome Incognito window (Ctrl+Shift+N).\n8. Open exam/app/index.html in the Incognito window.\n9. Look at "Name *" and "Email *".', '"Name *" and "Email *" are empty in the Incognito window.', 'Condition: TCD-37-05\nTechnique: Error guessing\nEdge case: "in this browser" only.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
133	['TR-37', 'TC-37-06', 'Verify that nothing is saved when Submit is rejected with the box ticked.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Leave "Your review *" empty.\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Tick the checkbox "Save my name, email, and website in this browser for the next time I comment."\n6. Click "Submit".\n7. Reload the page (F5).\n8. Look at "Name *" and "Email *".', 'To be confirmed (Q-14): "Name *" and "Email *" are empty.', 'OBSERVE ONLY — no verdict until Q-14 is answered\nCondition: TCD-37-06\nTechnique: State transition\nEdge case: rejected submit with the box ticked.\nMissing info: whether data is saved on a rejected submit (Q-14).\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
134	['TR-38', 'TC-38-01', 'Verify that Name and Email are not kept when the box is not ticked.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload.', '1. Click the 4th star of "Your rating *".\n2. Enter "No save check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Leave the checkbox "Save my name, email, and website in this browser for the next time I comment." not ticked.\n6. Click "Submit".\n7. Reload the page (F5).\n8. Look at "Name *" and "Email *".', 'To be confirmed (Q-14): "Name *" and "Email *" are empty.', 'OBSERVE ONLY — no verdict until Q-14 is answered\nCondition: TCD-38-01\nTechnique: EP\nMissing info: what is saved when the checkbox is not ticked (Q-14).\nRisk: personal data left on a shared device.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
135	['TR-38', 'TC-38-02', 'Verify that typed but unsubmitted Name and Email are not kept after reload.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load). If Name * or Email * is filled on load, clear the saved data first: DevTools (F12) > Application > Storage > Clear site data, then reload. Chrome autofill of addresses is switched off (Settings > Autofill and passwords > Addresses and more).', '1. Enter "Anna Smith" in "Name *".\n2. Enter "anna.smith@example.com" in "Email *".\n3. Reload the page (F5) without clicking "Submit".\n4. Look at "Name *" and "Email *".', 'To be confirmed (Q-14): "Name *" and "Email *" are empty.', 'OBSERVE ONLY — no verdict until Q-14 is answered\nCondition: TCD-38-02\nTechnique: Error guessing\nMissing info: Q-14.\nRisk: personal data kept without consent.']
136	['TR-39', 'TC-39-01', 'Verify that a customer below the review limit can submit another review.', 'The customer (Name "Anna Smith", Email "anna.smith@example.com") already has [limit - 1] reviews for this product (limit set when Q-12 is answered); product page open.', '1. Click the 4th star of "Your rating *".\n2. Enter "Limit check: below limit." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-12): The review is submitted: a confirmation message appears above the form and "Pending approval" increases by 1.', 'BLOCKED — waiting for Q-12\nCondition: TCD-39-01\nTechnique: BVA\nPossible duplicate of TC-33-01 if Q-12 = one review per customer and product.\nMissing info: number of reviews per customer and product not specified (Q-12). If the limit is 1, this is the first review (TCD-33-01) and is not repeated.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
137	['TR-39', 'TC-39-02', 'Verify that a customer at the review limit cannot submit one more review.', 'The customer (Name "Anna Smith", Email "anna.smith@example.com") already has [limit] reviews for this product (Q-12); product page open.', '1. Click the 4th star of "Your rating *".\n2. Enter "Limit check: above limit." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-12): the review is not submitted ("Pending approval" does not increase) and the message confirmed for Q-12 is shown.', 'BLOCKED — waiting for Q-12\nCondition: TCD-39-02\nTechnique: BVA\nEdge case: one above the limit.\nMissing info: Q-12.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
138	['TR-39', 'TC-39-03', 'Verify that a customer at the limit for product A can review product B.', 'A build with two products; the customer already has [limit] reviews for product A (Q-12); page of product B open.', '1. Click the 4th star of "Your rating *".\n2. Enter "Limit check: other product." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-12): the review is submitted: a confirmation message appears and the review waits for approval.', 'NOT RUN on demo-1.0 — one product only; also BLOCKED — waiting for Q-12\nCondition: TCD-39-03\nTechnique: Error guessing\nMissing info: Q-12; needs a build with two products.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
139	['TR-39', 'TC-39-04', 'Verify that the review limit cannot be bypassed by changing Name and Email.', 'The customer already has [limit] reviews for this product (Q-12); product page open.', '1. Click the 4th star of "Your rating *".\n2. Enter "Limit check: other identity." in "Your review *".\n3. Enter "Ben Carter" in "Name *".\n4. Enter "ben.carter@example.com" in "Email *".\n5. Click "Submit".', 'To be confirmed (Q-01, Q-02, Q-12): the customer is still recognised and the review is not submitted; the message confirmed for Q-12 is shown.', 'BLOCKED — waiting for Q-12 (and Q-01, Q-02 for how the customer is identified)\nCondition: TCD-39-04\nTechnique: Error guessing\nMissing info: how the customer is identified (Q-01, Q-02, Q-12).\nRisk: limit bypassed by changing name or email.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.']
140	['TR-40', 'TC-40-01', 'Verify that double-clicking Submit creates only one review.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Double click check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Double-click "Submit" quickly.\n6. Read "Pending approval".\n7. Click "Moderator: approve pending reviews".\n8. Count the reviews "Double click check." in the "Reviews" list.', '"Pending approval" shows 1 (not 2) and the review "Double click check." appears exactly once after approval.', 'Condition: TCD-40-01\nTechnique: Error guessing\nEdge case: rapid double click.\nAssumption: only one review is created until Q-28 is answered.\nRisk: duplicate reviews distort the rating.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-28).']
141	['TR-40', 'TC-40-02', 'Verify that clicking Submit then pressing Enter quickly creates only one review.', 'demo-1.0 (exam/app/index.html) open in Chrome and just reloaded, so the initial data is shown; "Pending approval: 0"; nothing saved in this browser (Name * and Email * empty on load).', '1. Click the 4th star of "Your rating *".\n2. Enter "Click and Enter check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit". Immediately click in "Name *" and press Enter.\n6. Read "Pending approval".\n7. Click "Moderator: approve pending reviews".\n8. Count the reviews "Click and Enter check." in the "Reviews" list.', '"Pending approval" shows 1 and the review "Click and Enter check." appears exactly once after approval.', 'Condition: TCD-40-02\nTechnique: Error guessing\nAssumption: only one review is created until Q-28 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-28).']
142	['TR-40', 'TC-40-03', 'Verify that reloading right after a successful Submit creates no second review.', 'A build that keeps reviews after reload; product page open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Reload after submit check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. As soon as the confirmation appears, reload the page (F5); if Chrome asks to resend the form, click Continue.\n7. As moderator, approve pending reviews.\n8. Count the reviews "Reload after submit check." in the "Reviews" list.', 'The review "Reload after submit check." appears exactly once.', 'NOT RUN on demo-1.0 — a reload restores the initial data\nCondition: TCD-40-03\nTechnique: Error guessing\nAssumption: only one review is created until Q-28 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-28).']
143	['TR-40', 'TC-40-04', 'Verify that browser Back then Forward after Submit creates no second review.', 'A build that keeps reviews; product page reached from another page (so Back is available); product page open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Back and forward check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".\n6. Click the browser Back button.\n7. Click the browser Forward button.\n8. As moderator, approve pending reviews.\n9. Count the reviews "Back and forward check." in the "Reviews" list.', 'The review "Back and forward check." appears exactly once.', 'NOT RUN on demo-1.0 — Back/Forward reloads the page and restores the initial data\nCondition: TCD-40-04\nTechnique: Error guessing\nAssumption: only one review is created until Q-28 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-28).']
144	['TR-41', 'TC-41-01', 'Verify that a lost network connection on Submit is reported and data is kept.', 'A build with a server; product page open in Chrome with DevTools (F12) open on the Network tab.', '1. Click the 4th star of "Your rating *".\n2. Enter "Network loss check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. In DevTools > Network set throttling to "Offline".\n6. Click "Submit".', 'A message says the review was not submitted, and the rating (4 stars), "Your review *", "Name *" and "Email *" still hold the entered values.', 'NOT RUN on demo-1.0 — no server or network\nCondition: TCD-41-01\nTechnique: Error guessing\nAssumption: on a save failure a message says the review was not submitted and the entered data is kept until Q-29 is answered.\nMissing info: demo-1.0 runs without a server or network (environment.md), so this cannot be produced there.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-29).']
145	['TR-41', 'TC-41-02', 'Verify that a server error on Submit is reported and data is kept.', 'A build with a server set up (by the test team) to return an error on saving a review; product page open in Chrome.', '1. Click the 4th star of "Your rating *".\n2. Enter "Server error check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'A message says the review was not submitted, and the rating (4 stars), "Your review *", "Name *" and "Email *" still hold the entered values.', 'NOT RUN on demo-1.0 — no server\nCondition: TCD-41-02\nTechnique: Error guessing\nAssumption: on a save failure a message says the review was not submitted and the entered data is kept until Q-29 is answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-29).']
146	['TR-41', 'TC-41-03', 'Verify that an expired session on Submit is reported and data is not lost.', 'A build with sign-in; signed in as a test customer; session expired before Submit (for example by signing out in another tab).', '1. Click the 4th star of "Your rating *".\n2. Enter "Session expiry check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. Click "Submit".', 'The customer is told the session expired and the entered rating, review, Name and Email are not lost.', 'NOT RUN on demo-1.0 — no sign-in\nCondition: TCD-41-03\nTechnique: Error guessing\nAssumption: on a save failure a message says the review was not submitted and the entered data is kept until Q-29 is answered.\nMissing info: sign-in rules (Q-01); demo-1.0 has no sign-in.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-29).']
147	['TR-41', 'TC-41-04', 'Verify that resubmitting after a failed Submit creates exactly one review.', 'A build with a server; product page open in Chrome with DevTools (F12) open on the Network tab.', '1. Click the 4th star of "Your rating *".\n2. Enter "Retry after failure check." in "Your review *".\n3. Enter "Anna Smith" in "Name *".\n4. Enter "anna.smith@example.com" in "Email *".\n5. In DevTools > Network set throttling to "Offline".\n6. Click "Submit".\n7. Set throttling back to "No throttling".\n8. Click "Submit".\n9. As moderator, approve pending reviews.\n10. Count the reviews "Retry after failure check." in the "Reviews" list.', 'The review "Retry after failure check." appears exactly once.', 'NOT RUN on demo-1.0 — no server or network\nCondition: TCD-41-04\nTechnique: Error guessing\nAssumption: only one review is created per submit action; on a save failure a message says the review was not submitted and the entered data is kept until Q-28 and Q-29 are answered.\nAssumption: the other values entered are valid under the unconfirmed length and format rules until Q-04, Q-05 and Q-06 are answered.\nMissing info: expected result not stated in any source (Q-28, Q-29).']
148	=== skills/test-data-generation/assets/test-data-template.xlsx Test Data A1:F1 {'A': 12.0, 'B': 18.0, 'C': 20.0, 'D': 50.0, 'E': 12.0, 'F': 45.0}
149	['TC ID', 'Data ID', 'Field', 'Value', 'Purpose', 'Notes']
150	
```

## AI (2026-10-21T04:32:14)

**Tool call `Bash`:**

```json
{
  "command": "cd /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass && ls submission/runs/; python -I -c \"\nimport openpyxl\nwb=openpyxl.load_workbook('submission/skills/test-data-generation/assets/test-data-template.xlsx')\nws=wb.active\nfor c in ws[1]: print(c.coordinate, c.font.b, c.fill.fgColor.rgb, c.alignment.wrap_text, c.alignment.vertical)\nprint(ws.freeze_panes, ws.auto_filter.ref, wb.sheetnames)\n\"",
  "description": "Inspect template styles and runs folder"
}
```

## Tool (2026-10-21T04:32:17)

```
run-1
run-2
A1 True 001F4E78 True center
B1 True 001F4E78 True center
C1 True 001F4E78 True center
D1 True 001F4E78 True center
E1 True 001F4E78 True center
F1 True 001F4E78 True center
A2 A1:F1 ['Test Data']
```

## AI (2026-10-21T04:32:19)

**Tool call `Bash`:**

```json
{
  "command": "ls -la /c/AI_Enabled_Program/evaluator/test-fixtures/manual-qa-sim-pass/submission/runs/run-2",
  "description": "List run-2 output folder"
}
```

## Tool (2026-10-21T04:32:20)

```
total 8
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 11:31 .
drwxr-xr-x 1 vinh.the.nguyen 1049089    0 Oct 21 11:31 ..
-rw-r--r-- 1 vinh.the.nguyen 1049089 7392 Oct 21 11:31 clarification-questions.md
```

## AI (2026-10-21T04:33:39)

**Tool call `Write`:**

```json
{
  "file_path": "C:\\Users\\VINHTH~1.NGU\\AppData\\Local\\Temp\\claude\\C--AI-Enabled-Program\\fe1617b2-e139-4ff0-b01c-9de934e75a43\\scratchpad\\gen_test_data.py",
  "content": "\"\"\"Generate run-2 test-data.xlsx from the test-data-generation skill rules.\n\nUsage: python -I gen_test_data.py <template.xlsx> <output.xlsx>\n\"\"\"\nimport shutil\nimport sys\nfrom collections import Counter, OrderedDict\n\nimport openpyxl\nfrom openpyxl.styles import Alignment\n\nTEMPLATE, OUT = sys.argv[1], sys.argv[2]\n\nR = 'Your rating *'\nV = 'Your review *'\nN = 'Name *'\nE = 'Email *'\nC = 'Save my name, email, and website... (checkbox)'\n\nA_RATING = 'Assumption: the rating is a whole number from 1 to 5, one per star, until Q-03 is answered.'\nA_REVIEW_LEN = 'Assumption: {n} characters is between the minimum and maximum review length until Q-04 is answered.'\nA_NAME = 'Assumption: letters and spaces are allowed and {n} characters is within the Name length limit until Q-05 is answered.'\nA_EMAIL = 'Assumption: standard format text@domain.tld is valid and {n} characters is within the unstated maximum length until Q-06 is answered.'\nA_TRIM = 'Assumption: leading and trailing spaces are trimmed and a field of only spaces counts as empty until Q-17 is answered.'\nM_Q15 = 'Missing info: whether HTML, scripts and links are shown as plain text, removed or rejected (Q-15).'\nA_Q15 = 'Assumption: the assumed rule broken is \"markup and scripts are never rendered or run\"; content is never executed whatever Q-15 says.'\n\nrows = []  # (tc, field, value, purpose, notes)\n\n\ndef add(tc, field, value, purpose, *notes):\n    assert purpose in ('valid', 'invalid', 'boundary')\n    rows.append((tc, field, value, purpose, '\\n'.join(notes)))\n\n\ndef rating(tc, n, field=R, extra=()):\n    add(tc, field, str(n), 'valid',\n        f'Tests: whole-star rating {n} inside 1 to 5 (5 stars, required: mockup-1 R2, R6).',\n        A_RATING, *extra)\n\n\ndef review(tc, text, field=V, purpose='valid', tests=None, extra=()):\n    n = len(text)\n    add(tc, field, text, purpose,\n        tests or f'Tests: required review text, {n} characters, ordinary letters and punctuation.',\n        A_REVIEW_LEN.format(n=n), *extra)\n\n\ndef name(tc, text='Anna Smith', field=N, extra=()):\n    n = len(text)\n    add(tc, field, text, 'valid',\n        f'Tests: required Name of Latin letters and a space, {n} characters.',\n        A_NAME.format(n=n), *extra)\n\n\ndef email(tc, text='anna.smith@example.com', field=E, extra=()):\n    n = len(text)\n    add(tc, field, text, 'valid',\n        f'Tests: required Email in format text@domain.tld on reserved domain example.com, {n} characters.',\n        A_EMAIL.format(n=n), *extra)\n\n\ndef box(tc, ticked):\n    if ticked:\n        add(tc, C, 'Ticked', 'valid',\n            'Tests: optional save checkbox ticked (changed from the unchecked default, mockup-1 F5).',\n            'Assumption: ticking saves only Name and Email in this browser until Q-13 and Q-14 are answered.',\n            'Risk: personal data stored on the device; use synthetic Name and Email only.')\n    else:\n        add(tc, C, 'Not ticked', 'valid',\n            'Tests: optional save checkbox left at its unchecked default (mockup-1 F5).')\n\n\ndef std(tc, stars, text, nm='Anna Smith', em='anna.smith@example.com'):\n    rating(tc, stars)\n    review(tc, text)\n    name(tc, nm)\n    email(tc, em)\n\n\nEMPTY_REQ = 'Tests: breaks one rule only: required field left empty (required: mockup-1 R2); all other fields valid.'\nSPACES = '\" \" x 5 (5 spaces)'\nSPACES_NOTE = 'Value is exactly 5 space characters and nothing else (Space bar pressed 5 times).'\n\n# ---------------- TR-02 ----------------\nrating('TC-02-01', 3)\nadd('TC-02-02', R, 'Left half of the 3rd star (attempted 2.5)', 'invalid',\n    'Tests: breaks one rule only: rating must be a whole number (half-star 2.5 attempted).',\n    'Missing info: whether half stars are allowed (Q-03).', A_RATING)\nreview('TC-02-02', 'Half star check.')\nname('TC-02-02')\nemail('TC-02-02')\nrating('TC-02-03', 2, extra=('Moving the pointer over the 5th star is an action in the steps, not a value.',))\nrating('TC-02-04', 4, extra=('Selected with the keyboard only (Tab, arrow keys, Space or Enter).',\n                             'Missing info: keyboard use is not stated in any source (Q-34).'))\n\n# ---------------- TR-03 ----------------\nfor tc, n, text, pos, edge in [\n    ('TC-03-01', 1, 'Rating check: one star.', 'on the minimum (1)', True),\n    ('TC-03-02', 2, 'Rating check: two stars.', 'one above the minimum (1)', False),\n    ('TC-03-03', 4, 'Rating check: four stars.', 'one below the maximum (5)', False),\n    ('TC-03-04', 5, 'Rating check: five stars.', 'on the maximum (5)', True),\n]:\n    notes = [f'Tests: rating {n} = {pos} of the range 1 to 5.']\n    if edge:\n        notes.append('Edge case: value exactly at the ' + ('minimum.' if n == 1 else 'maximum.'))\n    notes.append('Assumption: rating range 1 to 5 until Q-03 is answered.')\n    add(tc, R, str(n), 'boundary', *notes)\n    review(tc, text)\n    name(tc)\n    email(tc)\n\n# ---------------- TR-04 ----------------\nadd('TC-04-01', R, '2, then 5', 'valid', 'Tests: rating increased from 2 to 5; final rating 5.',\n    'Assumption: clicking another star changes the rating until Q-16 is answered.')\nadd('TC-04-02', R, '5, then 2', 'valid', 'Tests: rating decreased from 5 to 2; final rating 2.',\n    'Assumption: clicking another star changes the rating until Q-16 is answered.')\nadd('TC-04-03', R, '3, then 3 again', 'valid',\n    'Tests: clicking the selected star again keeps rating 3 (not cleared to no rating).',\n    'Assumption: the rating cannot be cleared by clicking until Q-16 is answered.')\nadd('TC-04-04', R, '3', 'valid', 'Tests: rating 3 selected, then the page is reloaded (step 2) and the rating resets.',\n    'Assumption: reloading is the only way back to no rating until Q-16 is answered.')\nadd('TC-04-05', R, '1, then 4, then 2, then 3', 'valid',\n    'Tests: several changes before Submit; only the final rating 3 is saved.',\n    'Assumption: clicking another star changes the rating until Q-16 is answered.', A_RATING)\nreview('TC-04-05', 'Changed rating, final is three.')\nname('TC-04-05')\nemail('TC-04-05')\n\n# ---------------- TR-05 ----------------\nadd('TC-05-01', R, '(no star selected)', 'boundary',\n    'Tests: rating 0 = one below the minimum 1; required field empty, all other fields valid.',\n    'Edge case: just below the minimum.', 'Assumption: rating range 1 to 5 until Q-03 is answered.')\nreview('TC-05-01', 'Soft fabric, true to size. Would buy again.')\nname('TC-05-01')\nemail('TC-05-01')\n\n# ---------------- TR-06 ----------------\nreview('TC-06-01', 'Line one\\nLine two',\n       tests='Tests: multi-line text, 2 lines typed with Enter between them (17 characters incl. 1 line break); no Submit.')\nrating('TC-06-02', 4)\nreview('TC-06-02', 'Line one\\nLine two\\nLine three',\n       tests='Tests: multi-line text, 3 lines typed with Enter between them (28 characters incl. 2 line breaks).',\n       extra=('Missing info: display of line breaks is not stated in any source (Q-35).',))\nname('TC-06-02')\nemail('TC-06-02')\n\n# ---------------- TR-07 ----------------\nrating('TC-07-01', 4)\nadd('TC-07-01', V, '(empty)', 'invalid', EMPTY_REQ, 'Value: 0 characters; leave the field untouched.')\nname('TC-07-01')\nemail('TC-07-01')\n\n# ---------------- TR-08 ----------------\nstd('TC-08-01', 4, 'Soft fabric, true to size. Would buy again.')\nrating('TC-08-02', 4)\ntxt = 'Très bien, Größe M passt! 日本語 OK 100% 👍'\nreview('TC-08-02', txt,\n       tests=f'Tests: accented letters (è, ö, ß), non-Latin letters (日本語), digits, punctuation and one emoji; {len(txt)} characters (Unicode code points; the emoji counts as 2 in a UTF-16 counter).',\n       extra=('Assumption: no character restriction in \"Your review\" until Q-37 is answered.',\n              'Edge case: non-Latin letters and emoji.'))\nname('TC-08-02')\nemail('TC-08-02')\nrating('TC-08-03', 4)\nreview('TC-08-03', 'Pasted review: comfy and soft.',\n       tests='Tests: text pasted with Ctrl+V instead of typed; 30 characters. Copy it from Notepad into the clipboard before the test.')\nname('TC-08-03')\nemail('TC-08-03')\n\n# ---------------- TR-11 ----------------\nrating('TC-11-01', 4)\nadd('TC-11-01', V, SPACES, 'invalid',\n    'Tests: breaks one rule only: required review has no visible text (spaces only).',\n    SPACES_NOTE, 'Edge case: whitespace-only input.', A_TRIM)\nname('TC-11-01')\nemail('TC-11-01')\nrating('TC-11-02', 4)\nadd('TC-11-02', V, '[Enter] x 3 (3 line breaks)', 'invalid',\n    'Tests: breaks one rule only: required review has no visible text (line breaks only).',\n    'Value is exactly 3 line breaks and nothing else (Enter pressed 3 times).',\n    'Edge case: whitespace-only input.',\n    'Assumption: line breaks are treated like spaces and the field counts as empty until Q-17 is answered.')\nname('TC-11-02')\nemail('TC-11-02')\nrating('TC-11-03', 4)\npad = '   Space padded review.   '\nassert len(pad) == 26\nadd('TC-11-03', V, pad, 'valid',\n    'Tests: valid text with 3 leading and 3 trailing spaces; 26 characters as typed, 20 after trimming (\"Space padded review.\").',\n    'Edge case: space-padded input.', A_TRIM, A_REVIEW_LEN.format(n=20))\nname('TC-11-03')\nemail('TC-11-03')\n\n# ---------------- TR-12 ----------------\nfor tc, txt, what, risk in [\n    ('TC-12-01', '<script>alert(1)</script>', 'script element', 'Risk: script injection would affect every visitor of the product page.'),\n    ('TC-12-02', '<img src=x onerror=alert(1)>', 'HTML image tag with an onerror script attribute', 'Risk: script injection through an HTML attribute.'),\n    ('TC-12-03', '<b>bold</b> text check', 'harmless HTML formatting tag', None),\n    ('TC-12-04', 'Link check https://example.com', 'web link (reserved domain example.com)', None),\n]:\n    rating(tc, 4)\n    notes = [f'Tests: breaks one rule only: review contains a {what}; length ({len(txt)} characters) and all other fields valid.',\n             M_Q15, A_Q15]\n    if tc == 'TC-12-04':\n        notes[2] = 'Assumption: the assumed rule broken is \"links are not turned into clickable links\" until Q-15 is answered.'\n    if risk:\n        notes.append(risk)\n    add(tc, V, txt, 'invalid', *notes)\n    name(tc)\n    email(tc)\nrating('TC-12-05', 4)\nreview('TC-12-05', 'Name script check.')\nadd('TC-12-05', N, '<script>alert(1)</script>', 'invalid',\n    'Tests: breaks one rule only: Name contains a script element; 25 characters; all other fields valid.',\n    'Missing info: Name characters and handling of markup not stated (Q-05, Q-15).', A_Q15,\n    'Risk: script injection through the reviewer name.')\nemail('TC-12-05')\n\n# ---------------- TR-14, TR-16, TR-17 ----------------\nstd('TC-14-01', 4, 'Approval check: shown after approve.')\nstd('TC-14-02', 4, 'Approve twice check.')\nstd('TC-16-01', 4, 'Author view: pending check.')\nstd('TC-16-02', 4, 'Author view: approved check.')\nstd('TC-17-01', 4, 'Details check: all parts shown.')\nstd('TC-17-02', 4, 'Date check: submit date.')\nstd('TC-17-03', 4, 'Name form check.')\n\n# ---------------- TR-18 ----------------\nrating('TC-18-01', 2, field=R + ' (review 1)')\nreview('TC-18-01', 'First review: too tight.', field=V + ' (review 1)')\nname('TC-18-01', 'Ben Carter', field=N + ' (review 1)')\nemail('TC-18-01', 'ben.carter@example.com', field=E + ' (review 1)')\nrating('TC-18-01', 5, field=R + ' (review 2)')\nreview('TC-18-01', 'Second review: perfect fit.', field=V + ' (review 2)')\nname('TC-18-01', 'Chloe Diaz', field=N + ' (review 2)')\nemail('TC-18-01', 'chloe.diaz@example.com', field=E + ' (review 2)',\n      extra=('Every value differs from review 1, so a mix-up is visible.',))\nrating('TC-18-02', 4)\nreview('TC-18-02', 'Special name check.')\nnm = \"Zoë O'Brien-Lê\"\nadd('TC-18-02', N, nm, 'valid',\n    f'Tests: Name with accented letters (ë, ê), an apostrophe and a hyphen; {len(nm)} characters.',\n    'Edge case: accented letters, apostrophe and hyphen.',\n    'Assumption: such names are accepted and the length is within the limit until Q-05 is answered.')\nemail('TC-18-02')\nrating('TC-18-03', 4)\ntxt = '5 > 3 & \"good\" isn\\'t it'\nreview('TC-18-03', txt,\n       tests=f'Tests: plain text containing the characters > & \" \\' (HTML-sensitive); {len(txt)} characters.',\n       extra=('Missing info: handling of HTML-like text (Q-15).',))\nname('TC-18-03')\nemail('TC-18-03')\n\n# ---------------- TR-19 ----------------\nfor tc, txt in [('TC-19-01', 'Email privacy check: visible page.'), ('TC-19-02', 'Email privacy check: hidden parts.')]:\n    rating(tc, 4)\n    review(tc, txt)\n    name(tc)\n    email(tc, 'unique.reviewer@example.com',\n          extra=('The local part \"unique.reviewer\" is the search marker used in the steps; it appears nowhere else in the data.',\n                 'Risk: personal data could be shown publicly.'))\n\n# ---------------- TR-20, TR-23 ----------------\nstd('TC-20-02', 4, 'Order check: newly approved.')\nstd('TC-23-01', 1, 'Summary check: approved 1 star.')\nstd('TC-23-02', 1, 'Summary check: pending 1 star.')\nstd('TC-23-04', 4, 'Summary check: count.')\nstd('TC-23-05', 2, 'Rounding check: two stars.')\nrows[-4] = rows[-4][:4] + (rows[-4][4] + '\\nWith the initial ratings 5, 4 and 3 (pre-condition, demo-1.0 data) the exact average becomes 14 / 4 = 3.5.\\nMissing info: rounding rule not stated (Q-11).',)\n\n# ---------------- TR-28 ----------------\nrating('TC-28-01', 4)\nreview('TC-28-01', 'Soft fabric, true to size. Would buy again.')\nadd('TC-28-01', N, '(empty)', 'invalid', EMPTY_REQ, 'Value: 0 characters; leave the field untouched.')\nemail('TC-28-01')\n\n# ---------------- TR-29 ----------------\ndef name_tc(tc, review_txt, name_val, purpose, *notes):\n    rating(tc, 4)\n    review(tc, review_txt)\n    add(tc, N, name_val, purpose, *notes)\n    email(tc)\n\n\nrows_before = len(rows)\nrating('TC-29-01', 4)\nreview('TC-29-01', 'Name check 29-01.')\nname('TC-29-01')\nemail('TC-29-01')\nname_tc('TC-29-02', 'Name check 29-02.', 'Zoë Lê', 'valid',\n        'Tests: Name with accented letters (ë, ê) and a space; 6 characters.',\n        'Edge case: accented letters.',\n        'Assumption: accented letters are allowed and the length is within the limit until Q-05 is answered.')\nname_tc('TC-29-03', 'Name check 29-03.', \"Mary-Jane O'Neil\", 'valid',\n        'Tests: Name with a hyphen, an apostrophe and a space; 16 characters.',\n        'Edge case: hyphen and apostrophe.',\n        'Assumption: hyphens and apostrophes are allowed and the length is within the limit until Q-05 is answered.')\nname_tc('TC-29-04', 'Name check 29-04.', '李明', 'valid',\n        'Tests: Name in a non-Latin script (Chinese), 2 characters, fictional.',\n        'Missing info: allowed characters not stated (Q-05).',\n        'Assumption: non-Latin letters are allowed until Q-05 is answered (OBSERVE ONLY test).')\nname_tc('TC-29-05', 'Name check 29-05.', 'Anna2', 'invalid',\n        'Tests: breaks one rule only: Name contains a digit (\"2\"); letters and length (5 characters) valid.',\n        'Missing info: whether digits are allowed (Q-05).',\n        'Assumption: the assumed rule broken is \"Name has letters, spaces, hyphens and apostrophes only\" until Q-05 is answered.')\nname_tc('TC-29-06', 'Name check 29-06.', '@#$%', 'invalid',\n        'Tests: breaks one rule only: Name has no letter, symbols only; length (4 characters) valid.',\n        'Missing info: allowed characters not stated (Q-05).',\n        'Assumption: the assumed rule broken is \"Name contains at least one letter\" until Q-05 is answered.')\nname_tc('TC-29-07', 'Name check 29-07.', 'A', 'boundary',\n        'Tests: Name length = 1 character, one above empty (shortest non-empty name).',\n        'Edge case: shortest non-empty name.',\n        'Assumption: the minimum Name length is 1 until Q-05 is answered.',\n        'Missing info: minimum length not stated (Q-05).')\n\n# ---------------- TR-30 ----------------\nrating('TC-30-01', 4)\nreview('TC-30-01', 'Soft fabric, true to size. Would buy again.')\nname('TC-30-01')\nadd('TC-30-01', E, '(empty)', 'invalid', EMPTY_REQ, 'Value: 0 characters; leave the field untouched.')\n\n# ---------------- TR-31 ----------------\nA_FMT = 'Assumption: standard format text@domain.tld until Q-06 is answered.'\nfor tc, rv, val, purpose, tests, extra in [\n    ('TC-31-01', 'Email check 31-01.', 'anna.smith@example.com', 'valid',\n     'Tests: standard format text@domain.tld with a dot in the local part; 22 characters.', ()),\n    ('TC-31-02', 'Email check 31-02.', 'anna+shop@mail.example.com', 'valid',\n     'Tests: plus sign in the local part and a sub-domain; 26 characters.', ('Edge case: plus sign and sub-domain.',)),\n    ('TC-31-03', 'Email check 31-03.', 'anna.example.com', 'invalid',\n     'Tests: breaks one rule only: no \"@\"; local part and domain otherwise valid.', ()),\n    ('TC-31-04', 'Email check 31-04.', '@example.com', 'invalid',\n     'Tests: breaks one rule only: nothing before \"@\"; domain valid.', ()),\n    ('TC-31-05', 'Email check 31-05.', 'anna@', 'invalid',\n     'Tests: breaks one rule only: no domain after \"@\"; local part valid.', ()),\n    ('TC-31-06', 'Email check 31-06.', 'anna@example', 'invalid',\n     'Tests: breaks one rule only: no top-level domain; local part and \"@\" valid.',\n     ('Assumption: a top-level domain is required until Q-06 is answered; some format rules accept this value.',)),\n    ('TC-31-07', 'Email check 31-07.', 'anna@@example.com', 'invalid',\n     'Tests: breaks one rule only: two \"@\"; local part and domain otherwise valid.', ()),\n    ('TC-31-08', 'Email check 31-08.', 'anna smith@example.com', 'invalid',\n     'Tests: breaks one rule only: a space inside the local part; everything else valid.', ()),\n    ('TC-31-09', 'Email check 31-09.', 'ANNA@EXAMPLE.COM', 'valid',\n     'Tests: valid format in upper case; 16 characters.',\n     ('Assumption: letter case does not matter until Q-06 is answered.',)),\n]:\n    rating(tc, 4)\n    review(tc, rv)\n    name(tc)\n    add(tc, E, val, purpose, tests, A_FMT, *extra)\n\n# ---------------- TR-32 ----------------\nrating('TC-32-01', 4)\nreview('TC-32-01', 'Name trim check.')\nadd('TC-32-01', N, '  Anna Smith  ', 'valid',\n    'Tests: valid Name with 2 leading and 2 trailing spaces; 14 characters as typed, 10 after trimming (\"Anna Smith\").',\n    'Edge case: space-padded input.', A_TRIM)\nemail('TC-32-01')\nrating('TC-32-02', 4)\nreview('TC-32-02', 'Soft fabric, true to size. Would buy again.')\nadd('TC-32-02', N, SPACES, 'invalid',\n    'Tests: breaks one rule only: required Name has no visible text (spaces only).',\n    SPACES_NOTE, 'Edge case: whitespace-only input.', A_TRIM)\nemail('TC-32-02')\nrating('TC-32-03', 4)\nreview('TC-32-03', 'Email trim check.')\nname('TC-32-03')\nadd('TC-32-03', E, '  anna@example.com  ', 'valid',\n    'Tests: valid Email with 2 leading and 2 trailing spaces; 20 characters as typed, 16 after trimming (\"anna@example.com\").',\n    'Edge case: space-padded input.', A_TRIM, A_FMT)\nrating('TC-32-04', 4)\nreview('TC-32-04', 'Soft fabric, true to size. Would buy again.')\nname('TC-32-04')\nadd('TC-32-04', E, SPACES, 'invalid',\n    'Tests: breaks one rule only: required Email has no visible text (spaces only).',\n    SPACES_NOTE, 'Edge case: whitespace-only input.', A_TRIM)\n\n# ---------------- TR-33 ----------------\nstd('TC-33-01', 4, 'Soft fabric, true to size. Would buy again.')\nbox('TC-33-01', False)\nstd('TC-33-02', 4, 'Soft fabric, true to size. Would buy again.')\nbox('TC-33-02', True)\n\n# ---------------- TR-34 ----------------\nadd('TC-34-01', R, '(no star selected)', 'invalid', 'Tests: required rating empty (one of 4 empty fields; decision-table rule \"all empty\").')\nadd('TC-34-01', V, '(empty)', 'invalid', 'Tests: required review empty (one of 4 empty fields).')\nadd('TC-34-01', N, '(empty)', 'invalid', 'Tests: required Name empty (one of 4 empty fields).')\nadd('TC-34-01', E, '(empty)', 'invalid', 'Tests: required Email empty (one of 4 empty fields).')\nadd('TC-34-02', R, '(no star selected)', 'invalid', 'Tests: required rating empty (one of 2 empty fields; Name and Email valid).')\nadd('TC-34-02', V, '(empty)', 'invalid', 'Tests: required review empty (one of 2 empty fields; Name and Email valid).')\nname('TC-34-02')\nemail('TC-34-02')\nrating('TC-34-03', 4)\nadd('TC-34-03', V + ' (1st Submit)', '(empty)', 'invalid', EMPTY_REQ, 'Used for the 1st Submit (step 5), which must be rejected.')\nreview('TC-34-03', 'Soft fabric, true to size. Would buy again.', field=V + ' (2nd Submit)',\n       extra=('Entered at step 7 to correct the form before the 2nd Submit.',\n              'Assumption: entered values are kept after a rejected Submit until Q-38 is answered.'))\nname('TC-34-03')\nemail('TC-34-03')\nadd('TC-34-04', N, '(empty)', 'invalid',\n    'Tests: required Name left empty and focus moved away with Tab; no Submit.',\n    'Assumption: fields are checked on Submit only until Q-19 is answered.')\n\n# ---------------- TR-35 to TR-38 ----------------\nstd('TC-35-01', 4, 'Soft fabric, true to size. Would buy again.')\nbox('TC-35-01', False)\nstd('TC-35-02', 4, 'Soft fabric, true to size. Would buy again.')\nbox('TC-35-02', True)\nstd('TC-36-02', 4, 'Return visit check.')\nbox('TC-36-02', True)\nstd('TC-37-01', 4, 'Save check: first visit.')\nbox('TC-37-01', True)\nrating('TC-37-02', 4)\nreview('TC-37-02', 'Save check: replace.')\nname('TC-37-02', 'Ben Carter', extra=('Replaces the saved Name \"Anna Smith\" (pre-condition from TC-37-01).',\n                                      'Assumption: saved values are replaced until Q-14 is answered.'))\nemail('TC-37-02', 'ben.carter@example.com', extra=('Replaces the saved Email \"anna.smith@example.com\" (pre-condition from TC-37-01).',))\nbox('TC-37-02', True)\nrating('TC-37-03', 4)\nreview('TC-37-03', 'Save check: untick.')\nname('TC-37-03', extra=('Not typed: filled on load from the saved data (pre-condition).',))\nemail('TC-37-03', extra=('Not typed: filled on load from the saved data (pre-condition).',))\nbox('TC-37-03', False)\nstd('TC-37-04', 4, 'Save check: only name and email.')\nbox('TC-37-04', True)\nstd('TC-37-05', 4, 'Save check: private window.')\nbox('TC-37-05', True)\nrating('TC-37-06', 4)\nadd('TC-37-06', V, '(empty)', 'invalid', EMPTY_REQ, 'Makes the Submit rejected while the save checkbox is ticked.',\n    'Missing info: whether data is saved on a rejected Submit (Q-14).')\nname('TC-37-06')\nemail('TC-37-06')\nbox('TC-37-06', True)\nstd('TC-38-01', 4, 'No save check.')\nbox('TC-38-01', False)\nname('TC-38-02', extra=('Typed but never submitted (page reloaded without Submit).',\n                        'Risk: personal data kept without consent.'))\nemail('TC-38-02', extra=('Typed but never submitted (page reloaded without Submit).',))\n\n# ---------------- TR-40 ----------------\nstd('TC-40-01', 4, 'Double click check.')\nstd('TC-40-02', 4, 'Click and Enter check.')\n\n# ---------------- checks ----------------\nREAL_DOMAINS_OK = ('example.com', 'example.org', 'example.test')\nfor tc, field, value, purpose, notes in rows:\n    if '@' in value and field.startswith(E) and purpose == 'valid':\n        dom = value.strip().split('@')[-1].lower()\n        assert dom == 'example.com' or dom.endswith('.example.com'), (tc, value)\n    if purpose == 'invalid':\n        assert notes.startswith('Tests:'), (tc, field)\n\n# order by TC ID (stable), assign Data IDs\norder = OrderedDict()\nfor r in rows:\n    order.setdefault(r[0], []).append(r)\ntc_ids = sorted(order, key=lambda t: tuple(int(x) for x in t[3:].split('-')))\n\nshutil.copyfile(TEMPLATE, OUT)\nwb = openpyxl.load_workbook(OUT)\nws = wb['Test Data']\nwrap = Alignment(wrap_text=True, vertical='top')\nr_i = 2\nfor tc in tc_ids:\n    for nn, (_, field, value, purpose, notes) in enumerate(order[tc], 1):\n        vals = [tc, f'D-{tc}-{nn:02d}', field, value, purpose, notes]\n        for c_i, v in enumerate(vals, 1):\n            cell = ws.cell(row=r_i, column=c_i, value=v)\n            cell.alignment = wrap\n        r_i += 1\nwb.save(OUT)\n\ncnt = Counter(r[3] for r in rows)\nprint('rows', len(rows), dict(cnt), 'tcs', len(tc_ids))\nprint(' '.join(tc_ids))\n"
}
```

## Tool (2026-10-21T04:33:39)

```
File created successfully at: C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\gen_test_data.py (file state is current in your context — no need to Read it back)
```

## AI (2026-10-21T04:33:45)

**Tool call `Bash`:**

```json
{
  "command": "SP=\"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\" && PYTHONIOENCODING=utf-8 python -I \"$SP/gen_test_data.py\" skills/test-data-generation/assets/test-data-template.xlsx runs/run-2/test-data.xlsx",
  "description": "Generate run-2 test-data.xlsx"
}
```

## Tool (2026-10-21T04:33:48)

```
rows 332 {'valid': 296, 'invalid': 30, 'boundary': 6} tcs 86
TC-02-01 TC-02-02 TC-02-03 TC-02-04 TC-03-01 TC-03-02 TC-03-03 TC-03-04 TC-04-01 TC-04-02 TC-04-03 TC-04-04 TC-04-05 TC-05-01 TC-06-01 TC-06-02 TC-07-01 TC-08-01 TC-08-02 TC-08-03 TC-11-01 TC-11-02 TC-11-03 TC-12-01 TC-12-02 TC-12-03 TC-12-04 TC-12-05 TC-14-01 TC-14-02 TC-16-01 TC-16-02 TC-17-01 TC-17-02 TC-17-03 TC-18-01 TC-18-02 TC-18-03 TC-19-01 TC-19-02 TC-20-02 TC-23-01 TC-23-02 TC-23-04 TC-23-05 TC-28-01 TC-29-01 TC-29-02 TC-29-03 TC-29-04 TC-29-05 TC-29-06 TC-29-07 TC-30-01 TC-31-01 TC-31-02 TC-31-03 TC-31-04 TC-31-05 TC-31-06 TC-31-07 TC-31-08 TC-31-09 TC-32-01 TC-32-02 TC-32-03 TC-32-04 TC-33-01 TC-33-02 TC-34-01 TC-34-02 TC-34-03 TC-34-04 TC-35-01 TC-35-02 TC-36-02 TC-37-01 TC-37-02 TC-37-03 TC-37-04 TC-37-05 TC-37-06 TC-38-01 TC-38-02 TC-40-01 TC-40-02
```

## AI (2026-10-21T04:33:59)

**Tool call `Bash`:**

```json
{
  "command": "PYTHONIOENCODING=utf-8 python -I -c \"\nimport openpyxl,re\ntc=openpyxl.load_workbook('runs/run-1/test-cases.xlsx').active\nrunnable={};allids=[]\nfor r in tc.iter_rows(min_row=2,values_only=True):\n    if not r[1]: continue\n    allids.append(r[1])\n    if not (r[6] or '').startswith(('BLOCKED','NOT RUN')): runnable[r[1]]=r\nd=openpyxl.load_workbook('runs/run-2/test-data.xlsx')\nprint(d.sheetnames,{k:v.width for k,v in d.active.column_dimensions.items()})\nws=d.active\nprint([c.value for c in ws[1]])\ndata={}\nfor r in ws.iter_rows(min_row=2,values_only=True): data.setdefault(r[0],[]).append(r)\nprint('runnable',len(runnable),'with data',len(data))\nprint('runnable without data:',[t for t in runnable if t not in data])\nprint('data for non-runnable:',[t for t in data if t not in runnable])\nskip=('(empty)','(no star selected)','Ticked','Not ticked','\\\" \\\" x 5 (5 spaces)','[Enter] x 3 (3 line breaks)')\nfor t,rs in data.items():\n    steps=runnable[t][3]+'\\n'+runnable[t][4]\n    for r in rs:\n        v=r[3]\n        if v in skip or r[2].startswith('Your rating'): continue\n        if v.replace('\\n','') and v not in steps and v.strip() not in steps:\n            if not all(line in steps for line in v.split('\\n')): print('NOT IN STEPS',t,r[2],repr(v))\n        m=re.search(r'(\\d+) characters',r[5])\n        if m and r[2].startswith(('Name','Email')) and 'as typed' not in r[5] and int(m.group(1))!=len(v): print('LEN MISMATCH',t,repr(v),m.group(1))\ndup=[r[1] for rs in data.values() for r in rs]; print('unique data ids',len(dup)==len(set(dup)),len(dup))\nprint(repr(ws['D2'].value))\nfor row in ws.iter_rows(min_row=2):\n    if row[0].value=='TC-11-03' and row[2].value.startswith('Your review'): print(repr(row[3].value),len(row[3].value))\n\"",
  "description": "Verify data coverage and values against test cases"
}
```

## Tool (2026-10-21T04:34:01)

```
['Test Data'] {'A': 12.0, 'B': 18.0, 'C': 20.0, 'D': 50.0, 'E': 12.0, 'F': 45.0}
['TC ID', 'Data ID', 'Field', 'Value', 'Purpose', 'Notes']
runnable 97 with data 86
runnable without data: ['TC-01-01', 'TC-14-03', 'TC-20-01', 'TC-25-01', 'TC-25-02', 'TC-25-03', 'TC-25-04', 'TC-25-05', 'TC-25-06', 'TC-25-07', 'TC-36-01']
data for non-runnable: []
unique data ids True 332
'3'
'   Space padded review.   ' 26
```

## AI (2026-10-21T04:34:07)

**Tool call `Bash`:**

```json
{
  "command": "PYTHONIOENCODING=utf-8 python -I -c \"\nfor s in ['Pasted review: comfy and soft.','<script>alert(1)</script>','Zoë Lê',\\\"Mary-Jane O'Neil\\\",'ANNA@EXAMPLE.COM','anna+shop@mail.example.com','anna.smith@example.com','Soft fabric, true to size. Would buy again.','  Anna Smith  ','  anna@example.com  ','Très bien, Größe M passt! 日本語 OK 100% 👍',\\\"Zoë O'Brien-Lê\\\"]: print(len(s),len(s.encode('utf-16-le'))//2,repr(s))\n\"",
  "description": "Verify character counts of stated values"
}
```

## Tool (2026-10-21T04:34:08)

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    for s in ['Pasted review: comfy and soft.','<script>alert(1)</script>','Zo� L�',"Mary-Jane O'Neil",'ANNA@EXAMPLE.COM','anna+shop@mail.example.com','anna.smith@example.com','Soft fabric, true to size. Would buy again.','  Anna Smith  ','  anna@example.com  ','Tr�s bien, Gr��e M passt! \u65e5\u672c\u8a9e OK 100% \U0001f44d',"Zo� O'Brien-L�"]: print(len(s),len(s.encode('utf-16-le'))//2,repr(s))
                                                                                                                                                                                                                                                                                                                                       ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python\Python314\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode characters in position 27-29: character maps to <undefined>
30 30 'Pasted review: comfy and soft.'
25 25 '<script>alert(1)</script>'
6 6 'Zo� L�'
16 16 "Mary-Jane O'Neil"
16 16 'ANNA@EXAMPLE.COM'
26 26 'anna+shop@mail.example.com'
22 22 'anna.smith@example.com'
43 43 'Soft fabric, true to size. Would buy again.'
14 14 '  Anna Smith  '
20 20 '  anna@example.com  '
39 40
```

## AI (2026-10-21T04:34:12)

**Tool call `Bash`:**

```json
{
  "command": "python -I -c \"\nimport openpyxl\nws=openpyxl.load_workbook('runs/run-2/test-data.xlsx').active\nfor r in ws.iter_rows(min_row=2,values_only=True):\n    if any(ord(ch)>127 for ch in r[3]): print(r[1], len(r[3]), len(r[3].encode('utf-16-le'))//2, ascii(r[3]), ascii(r[5].split(chr(10))[0]))\n\"",
  "description": "Check non-ASCII values and counts in output"
}
```

## Tool (2026-10-21T04:34:14)

```
D-TC-08-02-02 39 40 'Tr\xe8s bien, Gr\xf6\xdfe M passt! \u65e5\u672c\u8a9e OK 100% \U0001f44d' 'Tests: accented letters (\xe8, \xf6, \xdf), non-Latin letters (\u65e5\u672c\u8a9e), digits, punctuation and one emoji; 39 characters (Unicode code points; the emoji counts as 2 in a UTF-16 counter).'
D-TC-18-02-03 14 14 "Zo\xeb O'Brien-L\xea" 'Tests: Name with accented letters (\xeb, \xea), an apostrophe and a hyphen; 14 characters.'
D-TC-29-02-03 6 6 'Zo\xeb L\xea' 'Tests: Name with accented letters (\xeb, \xea) and a space; 6 characters.'
D-TC-29-04-03 2 2 '\u674e\u660e' 'Tests: Name in a non-Latin script (Chinese), 2 characters, fictional.'
```

## AI (2026-10-21T04:34:20)

**Tool call `Bash`:**

```json
{
  "command": "SP=\"C:/Users/VINHTH~1.NGU/AppData/Local/Temp/claude/C--AI-Enabled-Program/fe1617b2-e139-4ff0-b01c-9de934e75a43/scratchpad\" && sed -i 's/Tests: accented letters (è, ö, ß)/Tests: accented and special Latin letters (è, ö, ß)/' \"$SP/gen_test_data.py\" && grep -c \"special Latin\" \"$SP/gen_test_data.py\" && PYTHONIOENCODING=utf-8 python -I \"$SP/gen_test_data.py\" skills/test-data-generation/assets/test-data-template.xlsx runs/run-2/test-data.xlsx | head -1; git -C /c/AI_Enabled_Program status --short evaluator/test-fixtures/manual-qa-sim-pass/",
  "description": "Fix note wording and regenerate"
}
```

## Tool (2026-10-21T04:34:23)

```
1
rows 332 {'valid': 296, 'invalid': 30, 'boundary': 6} tcs 86
?? evaluator/test-fixtures/manual-qa-sim-pass/
```

## AI (2026-10-21T04:34:54)

I wrote run 2 of the test data, built on its own. It covers every test case you can run, apart from 11 that type nothing into the form. All values are synthetic.

**What I read:** the skill and its rules file, the note-tags file, the template, `runs/run-1/test-cases.xlsx`, `runs/run-1/test-design.md` and the 4 knowledge files. I did not open `runs/run-1/test-data.xlsx`, `ai-original/` or anything else under test-fixtures. I didn't need the exam folder either: the TCs, the design and the knowledge files gave every field rule.

**Output:** `C:\AI_Enabled_Program\evaluator\test-fixtures\manual-qa-sim-pass\submission\runs\run-2\test-data.xlsx`
- I copied the template and filled it, so the sheet name "Test Data", the header row and the column widths are unchanged. Data cells are set to wrap text.
- It has 332 rows across 86 test cases, one row per field value. Data IDs follow `D-<TC ID>-<nn>`.
- The `clarification-questions.md` that was already in run-2 was left as it was.

**Which cases are in:** 145 TCs in the list, 97 runnable. I left out the 48 whose Notes start with BLOCKED or NOT RUN. OBSERVE ONLY cases count as runnable, so they have data.

**Values per purpose:**

| Purpose | Rows | What they are |
|---|---|---|
| valid | 296 | Mostly the supporting rating, review, Name and Email values each TC needs, plus the save checkbox in 13 TCs |
| invalid | 30 | Each breaks one rule only (see below) |
| boundary | 6 | Ratings 1, 2, 4 and 5 (TC-03-01 to 03-04), no star selected = 0 (TC-05-01), and Name "A" (TC-29-07) |

The 30 invalid rows are:
- empty required fields: TC-07-01, 28-01, 30-01, 34-01 to 34-04, 37-06
- half star: TC-02-02
- spaces only or line breaks only: TC-11-01, 11-02, 32-02, 32-04
- HTML, script or link text: TC-12-01 to 12-05
- Name with a digit or only symbols: TC-29-05, 29-06
- the six bad email formats: TC-31-03 to 31-08

**Checks I ran with a script:**
- Every typed text value matches the literal in that TC's steps exactly.
- Every character count stated in Notes is right. Space-padded values say both lengths: TC-11-03 is 26 as typed and 20 after trimming. TC-08-02 is 39 code points, but the emoji counts as 2 in a browser counter, so 40.
- Each invalid value's Notes start with "Tests: breaks one rule only: …".
- Every Data ID is unique, and no data was written for a non-runnable TC.

**Privacy:** all emails are on example.com or mail.example.com. The deliberately broken ones, such as `anna@example`, can't be delivered. Names are the fictional ones the TCs already use: Anna Smith, Ben Carter, Chloe Diaz, Zoë O'Brien-Lê, Zoë Lê, Mary-Jane O'Neil, 李明. There are no real accounts or secrets, and nothing needed production data.

**Values built on an Assumption** (each is tagged in Notes with its question ID):
- **Ratings:** whole stars 1 to 5 (Q-03). The click sequences in TC-04-01 to 04-05 also assume clicking another star changes the rating and can't clear it (Q-16).
- **Review text:**
  - every valid review assumes its length is between the unknown minimum and maximum (Q-04)
  - TC-08-02 also assumes there is no character restriction (Q-37)
- **Names:** all valid names assume letters, spaces, accents, hyphens and apostrophes are allowed and the length is within the limit (Q-05).
  - TC-29-04 (李明) assumes non-Latin letters are allowed.
  - TC-29-05 and 29-06 assume digits and symbol-only names are not allowed.
  - TC-29-07 assumes the minimum length is 1.
- **Emails:** all assume the standard text@domain.tld format and a length within the unknown maximum (Q-06). TC-31-06 also assumes a top-level domain is required, and TC-31-09 that letter case doesn't matter.
- **Spaces:** trimming and "spaces only counts as empty" (Q-17) are behind TC-11-01 to 11-03 and TC-32-01 to 32-04. TC-11-02 also assumes line breaks count as spaces.
- **HTML and links:** TC-12-01 to 12-05 assume the rule broken is "markup is never rendered or run", and for TC-12-04 that "links are not made clickable". How Q-15 will be answered is still unknown.
- **Save checkbox:** every "Ticked" row assumes only Name and Email get saved (Q-13, Q-14).
- **Only confirmed rules, no Assumption:** the empty required fields (mockup-1 R2), "no star selected" in TC-34-01/02, and "Not ticked" for the checkbox (mockup-1 F5).

**Runnable TCs with no data:** TC-01-01, TC-14-03, TC-20-01, TC-25-01 to 25-07 and TC-36-01. Their steps only look, count, or Tab through an empty form. The demo's own starting data that TC-20-01 and TC-23-05 rely on (the initial ratings 5, 4 and 3) isn't generated; it's noted on the TC-23-05 rating row.

**Calls you may want to review:**
- I marked "no star" as boundary in TC-05-01, because the design treats it as just below the minimum. In TC-34-01/02 the same value is invalid, because there it's simply an empty field.
- TC-04-03 (clicking 3, then 3 again) is marked valid. The value itself breaks no rule; the test is negative only because of the action.
- TC-34-03 has two review rows, one for each Submit: empty first, then the corrected text.
- TC-37-02, 37-03 and 38-02 note in Notes where Name and Email come from saved data or are typed but never submitted.

The script that builds the file is `C:\Users\VINHTH~1.NGU\AppData\Local\Temp\claude\C--AI-Enabled-Program\fe1617b2-e139-4ff0-b01c-9de934e75a43\scratchpad\gen_test_data.py`. Nothing is committed. Per the skill, this stops here for your review.

## Tool (2026-10-21T04:34:55)

```
{"success":true,"message":"Report delivered to your caller."}
```
