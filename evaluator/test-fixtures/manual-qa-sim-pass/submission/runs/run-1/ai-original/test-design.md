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
| TCD-02-03 | Error guessing | Moving the pointer over the stars without clicking, then moving it away, leaves the selected rating unchanged. | Negative | Assumption: a hover preview, if any, is not kept; no question raised yet, to be added to Q-16. |
| TCD-02-04 | Error guessing | The rating can be selected with the keyboard only (Tab to the stars, then arrow keys, Space or Enter), and the selection is shown. | Positive | Missing info: keyboard use is not stated in any source; new question needed. |

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
| TCD-06-02 | Error guessing | A review written on several lines is shown on the product page, after approval, with its line breaks kept. | Positive | Missing info: display of line breaks is not stated in any source; new question needed. |

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
| TCD-08-02 | Error guessing | Review text with accented letters (é, ü), non-Latin letters (日本語), digits, punctuation and an emoji: accepted and shown unchanged. | Positive | Assumption: no character restriction in "Your review"; no source restricts it, to be added to Q-15. |
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
| TCD-15-02 | State transition | Rejected review, then other pending reviews are approved: the rejected review is still not displayed. | Negative | Missing info: moderation workflow (Q-07).<br>Risk: rejected content shown publicly. |

### TR-16: Verify that the author sees their own pending review only in the way confirmed for Q-08 (marked as awaiting approval, or not at all).

Technique(s): Decision table - conditions "viewer = author / other visitor" and "state = Pending / Approved". Rule other + Pending is TCD-13-01; rule other + Approved is TCD-14-01; the two author rules are below.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-16-01 | Decision table | Rule: viewer = author, state = Pending: the author sees the review marked as awaiting approval, or does not see it, as confirmed for Q-08. | Positive | Missing info: author's view of a pending review not specified (Q-08). |
| TCD-16-02 | Decision table | Rule: viewer = author, state = Approved: the author sees the review like any other approved review, with no "awaiting approval" mark. | Positive | Missing info: whether a pending mark exists (Q-08). |

### TR-17: Verify that each displayed review shows the confirmed details (star rating, reviewer name, date, review text).

Technique(s): Equivalence Partitioning - every approved review belongs to one partition and must show the same set of details; one condition per detail group whose rule differs.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-17-01 | EP | Each approved review shows its star rating, reviewer name, date and review text. | Positive | Assumption: rating, reviewer name, date and review text are shown until Q-09 is answered. |
| TCD-17-02 | EP | The date shown with a review is the submit date, in an unambiguous format. | Positive | Assumption: submit date in any unambiguous format (Q-24). |
| TCD-17-03 | EP | The reviewer name is shown in the confirmed form (full name, first name only or initials). | Positive | Missing info: form of the name not specified (Q-09).<br>Risk: privacy of the reviewer's name. |

### TR-18: Verify that the star rating, name and review text of a displayed review match what the customer submitted.

Technique(s): Equivalence Partitioning - several reviews with different values must keep their own values. Error guessing - special characters are often encoded wrongly and long words often break the layout.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-18-01 | EP | Two reviews submitted one after the other with different rating, name and text: after approval each shows its own rating, name and text (no mix-up). | Positive | |
| TCD-18-02 | Error guessing | Name with accented letter, apostrophe and hyphen (for example "Zoë O'Brien-Lê"): shown exactly as entered, with no encoded characters such as `&#39;`. | Positive | Assumption: such names are accepted until Q-05 is answered. |
| TCD-18-03 | Error guessing | Review text with the characters `& < > " '` used as plain text (for example "5 > 3 & good"): shown exactly as entered, not as `&amp;` or `&gt;`. | Positive | Missing info: handling of HTML-like text (Q-15). |
| TCD-18-04 | Error guessing | Review of maximum length made of one long word with no spaces: shown in full without breaking the page layout. | Positive | Missing info: maximum length not stated (Q-04). |

### TR-19: Verify that the reviewer's email address is never displayed on the product page.

Technique(s): Error guessing - personal data often leaks through hidden places (tooltips, links, page source) as well as visible text.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-19-01 | Error guessing | After approval, the email entered does not appear anywhere in the visible product page (reviews list, reviewer name, rating summary). | Positive | Risk: personal data could be shown publicly. |
| TCD-19-02 | Error guessing | After approval, the email is not in hidden parts of the review: no tooltip, no "mailto" link on the name, not in the page source of the review. | Positive | Risk: personal data could be read by anyone viewing the page source. |

### TR-20: Verify that approved reviews are listed in the confirmed order.

Technique(s): Equivalence Partitioning - one partition "list of approved reviews with different dates and ratings". Error guessing - newly approved reviews and ties are common ordering defects.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-20-01 | EP | At least 3 approved reviews with different dates and ratings are listed in the confirmed order. | Positive | Missing info: list order not specified (Q-10). |
| TCD-20-02 | Error guessing | A review approved after the existing ones appears in the position the confirmed order requires. | Positive | Missing info: list order not specified (Q-10). |
| TCD-20-03 | Error guessing | Two approved reviews with the same date and the same rating keep a stable order when the page is opened again. | Positive | Edge case: tie in the sort key.<br>Missing info: list order not specified (Q-10). |

### TR-21: Verify that all approved reviews can be seen when a product has many reviews.

Technique(s): Equivalence Partitioning - "many reviews" partition. Boundary Value Analysis - page size, only if paging is confirmed.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-21-01 | EP | Product with a large number of approved reviews (for example 50): every approved review can be seen. | Positive | Edge case: large number of approved reviews.<br>Assumption: all approved reviews are shown on one page (Q-23). |
| TCD-21-02 | BVA | Approved reviews = page size - 1: all are on the first page and no paging control is shown. | Positive | Missing info: whether paging exists and the page size (Q-23). |
| TCD-21-03 | BVA | Approved reviews = page size: all are on the first page and no paging control is shown. | Positive | Edge case: count exactly at the page size.<br>Missing info: page size (Q-23). |
| TCD-21-04 | BVA | Approved reviews = page size + 1: the last review is reachable through the paging control or "Load more". | Positive | Edge case: one above the page size.<br>Missing info: page size (Q-23). |

### TR-22: Verify that a clear empty state is shown when the product has no approved reviews.

Technique(s): Boundary Value Analysis - approved review count 0 and the move from 0 to 1; Equivalence Partitioning - "only pending reviews" is part of the 0-approved partition.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-22-01 | BVA | 0 approved reviews: a short message says there are no reviews yet. | Positive | Edge case: product with no approved reviews.<br>Assumption: a short message saying there are no reviews yet (Q-25).<br>Missing info: demo-1.0 has one product that starts with approved reviews (app-note.md); a product with 0 approved reviews may not be available. |
| TCD-22-02 | EP | 0 approved reviews and 1 or more pending reviews: the empty-state message is still shown. | Positive | Edge case: only pending reviews.<br>Assumption: empty-state message (Q-25). |
| TCD-22-03 | BVA | From 0 to 1 approved review: the empty-state message disappears and the review is shown. | Positive | Assumption: empty-state message (Q-25). |

### TR-23: Verify that the average rating and review count on the product page, if shown, are calculated from approved reviews only.

Technique(s): Decision table - condition "state of the new review = Approved / Pending / Rejected", outcome "included in average and count: yes / no". Boundary Value Analysis - rounding boundary and zero reviews.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-23-01 | Decision table | Rule: new review Approved: the average rating and the review count include it. | Positive | Missing info: whether a summary is shown and how it is rounded (Q-11). |
| TCD-23-02 | Decision table | Rule: new review Pending: the average rating and the review count do not change. | Positive | Missing info: Q-11.<br>Risk: pending reviews could change the score shown to shoppers. |
| TCD-23-03 | Decision table | Rule: new review Rejected: the average rating and the review count do not change. | Positive | Missing info: Q-07, Q-11.<br>Risk: rejected reviews could change the score shown to shoppers. |
| TCD-23-04 | EP | The review count shown equals the number of approved reviews listed. | Positive | Missing info: whether a count is shown (Q-11). |
| TCD-23-05 | BVA | Ratings whose exact average falls on and next to the rounding step (for example 4 and 5 = 4.5; 4, 4 and 5 = 4.33...) are shown with the confirmed rounding. | Positive | Missing info: rounding rule not stated (Q-11); exact boundary values are set when Q-11 is answered. |
| TCD-23-06 | Error guessing | 0 approved reviews: the summary shows no average, or an empty state, and never a wrong value such as "NaN" or "0 stars". | Negative | Edge case: no approved reviews.<br>Missing info: Q-11, Q-25. |

### TR-24: Verify that a review is displayed only on the page of the product it was written for.

Technique(s): Equivalence Partitioning - partitions "page of the reviewed product" and "page of another product".

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-24-01 | EP | A review written and approved for product A appears on the page of product A. | Positive | Covered in demo-1.0 by TCD-14-01 (one product only). |
| TCD-24-02 | EP | The same review does not appear on the page of product B. | Negative | Risk: reviews shown on the wrong product mislead shoppers.<br>Missing info: demo-1.0 has one product only (app-note.md); needs a build with two products. |

### TR-25: Verify that the review form shows the heading, the info text, the fields, the save checkbox and the "Submit" button as in mockup-1.

Technique(s): Equivalence Partitioning - the form has one valid display state (mockup-1); one condition per element group. Error guessing - focus order and keyboard use.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-25-01 | EP | The heading reads "ADD A REVIEW". | Positive | Assumption: compared without regard to letter case (Q-32). |
| TCD-25-02 | EP | The info text reads "Your email address will not be published. Required fields are marked *". | Positive | |
| TCD-25-03 | EP | The labels "Your rating *", "Your review *", "Name *" and "Email *" are shown, each with the required marker *. | Positive | |
| TCD-25-04 | EP | The save checkbox reads "Save my name, email, and website in this browser for the next time I comment." | Positive | Missing info: final text of the save checkbox (Q-13). |
| TCD-25-05 | EP | A "Submit" button is shown below the save checkbox. | Positive | |
| TCD-25-06 | EP | The elements are in the mockup-1 order from top to bottom: heading, info text, rating, review, Name, Email, save checkbox, Submit. | Positive | |
| TCD-25-07 | Error guessing | Tab moves the focus through the form in the order shown, and Submit can be used with the keyboard. | Positive | Missing info: keyboard use is not stated in any source; new question needed. |

### TR-26: Verify that only a customer who is allowed to review (as confirmed for Q-01) can submit a review, and a customer who is not allowed cannot.

Technique(s): Decision table - conditions "signed in: yes / no" and "bought this product: yes / no"; outcome "may submit". The two "not signed in" rules are collapsed into one because the purchase cannot be linked to a guest without sign-in until Q-01 says otherwise. Error guessing - cancelled orders.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-26-01 | Decision table | Rule: signed in and bought the product: the customer can submit a review. | Positive | Missing info: sign-in and purchase check not specified (Q-01).<br>Missing info: demo-1.0 has no sign-in (environment.md). |
| TCD-26-02 | Decision table | Rule: signed in and did not buy the product: the form is hidden, disabled or rejected on Submit with a message, as confirmed for Q-01. | Negative | Missing info: Q-01.<br>Risk: non-buyers could post fake reviews. |
| TCD-26-03 | Decision table | Rule: not signed in (guest): the form is hidden, disabled or rejected on Submit with a message, as confirmed for Q-01. | Negative | Missing info: Q-01.<br>Risk: guests could post fake reviews. |
| TCD-26-04 | Error guessing | Signed in, the order of this product was cancelled or refunded: the customer may or may not review, as confirmed for Q-01. | Negative | Edge case: cancelled or refunded purchase.<br>Missing info: not covered by Q-01 yet; to be added to Q-01. |

### TR-27: Verify that Name and Email for a signed-in customer are handled as confirmed for Q-02 (prefilled, editable or not shown).

Technique(s): Equivalence Partitioning - the three possible answers to Q-02 (prefilled, editable, not shown) are the partitions; the applicable one is kept when Q-02 is answered.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-27-01 | EP | Signed-in customer opens the form: Name and Email are prefilled from the account, editable, or not shown, as confirmed for Q-02. | Positive | Missing info: conflict between the story and mockup-1 (Q-02). |
| TCD-27-02 | EP | If Name is prefilled and editable: the customer changes the Name, submits, and the displayed review shows the name as confirmed for Q-02 (edited or account name). | Positive | Missing info: Q-02. |

### TR-28: Verify that the review cannot be submitted when "Name" is empty.

Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-28-01 | EP | "Name" empty, rating, Review and Email valid, Submit: the review is not submitted and an error names "Name". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |

### TR-29: Verify that a Name within the allowed length and characters is accepted, and a Name outside them is rejected.

Technique(s): Equivalence Partitioning - character partitions (Latin letters, accented letters, hyphen/apostrophe, non-Latin script, digits, symbols only), one invalid partition per condition. Boundary Value Analysis - minimum (1 character, just above empty) and maximum length.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
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

### TR-30: Verify that the review cannot be submitted when "Email" is empty.

Technique(s): Equivalence Partitioning - "empty" is the invalid partition of a required field.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-30-01 | EP | "Email" empty, rating, Review and Name valid, Submit: the review is not submitted and an error names "Email". | Negative | Assumption: wording checked for meaning, not exact text (Q-20). |

### TR-31: Verify that a correctly formatted email is accepted and an incorrectly formatted email is rejected.

Technique(s): Equivalence Partitioning - valid format partitions and one invalid partition per format fault (one fault per condition). Boundary Value Analysis - maximum length. Error guessing - upper-case letters.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
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

### TR-32: Verify that leading and trailing spaces in Name and Email are removed, and a Name or Email made only of spaces counts as empty.

Technique(s): Error guessing - space-padded and spaces-only input, one field per condition.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-32-01 | Error guessing | Name with leading and trailing spaces ("  Anna Smith  "): accepted and, after approval, shown as "Anna Smith". | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
| TCD-32-02 | Error guessing | Name made only of spaces, Submit: the review is not submitted and an error names "Name". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |
| TCD-32-03 | Error guessing | Email with leading and trailing spaces ("  anna@example.com  "): accepted as a valid email. | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
| TCD-32-04 | Error guessing | Email made only of spaces, Submit: the review is not submitted and an error names "Email". | Negative | Edge case: whitespace-only input.<br>Assumption: a field of only spaces counts as empty (Q-17). |

### TR-33: Verify that when all required fields are valid, the review is submitted and a confirmation message is shown.

Technique(s): Decision table - conditions "rating, review, name, email valid" and "save checkbox ticked: yes / no"; the all-valid rules give "submitted". The rules with one field invalid are listed under TR-34.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-33-01 | Decision table | Rule: all four required fields valid, save checkbox not ticked, Submit: the review is submitted and a confirmation says it was received and waits for approval. | Positive | Assumption: confirmation says the review was received and waits for approval (Q-21). |
| TCD-33-02 | Decision table | Rule: all four required fields valid, save checkbox ticked, Submit: the review is submitted with the same confirmation. | Positive | Assumption: confirmation text (Q-21). |

### TR-34: Verify that when a required field is empty or invalid, the review is not submitted and an error message names each field concerned.

Technique(s): Decision table - conditions "rating / review / name / email valid: yes / no". Rules with exactly one invalid field are already covered: TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-31-03 to TCD-31-08. Rules with several invalid fields are collapsed into "all empty" and "two empty", which check that every field concerned is named. Equivalence Partitioning - validation timing.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-34-01 | Decision table | Rule: all four required fields empty, Submit: the review is not submitted and errors name all four fields. | Negative | Assumption: each error names its field; wording checked for meaning (Q-20). |
| TCD-34-02 | Decision table | Rule: rating and review empty, Name and Email valid, Submit: errors name the rating and "Your review" only, not Name or Email. | Negative | Assumption: wording checked for meaning (Q-20). |
| TCD-34-03 | Decision table | After a rejected Submit, the values already entered stay in the form; the customer corrects the field, submits again and the review is submitted. | Positive | Assumption: entered values are kept after a rejected submit; not stated, to be added to Q-19. |
| TCD-34-04 | EP | Leaving a required field empty and moving to the next field shows no error until Submit is pressed. | Positive | Assumption: fields are checked on Submit only (Q-19). |

### TR-35: Verify that after a successful submit the customer stays on the product page and the form is cleared.

Technique(s): State transition - "form filled" to "form after success", with the save checkbox ticked or not as the deciding event.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-35-01 | State transition | Successful Submit with the save checkbox not ticked: the customer stays on the product page and rating, review, Name and Email are all cleared. | Positive | Assumption: form cleared (Q-22). |
| TCD-35-02 | State transition | Successful Submit with the save checkbox ticked: the customer stays on the product page, rating and review are cleared, and Name and Email stay filled. | Positive | Assumption: Name and Email stay filled only if the checkbox was ticked (Q-22). |

### TR-36: Verify that the "Save my name, email, and website..." checkbox is unchecked by default.

Technique(s): Equivalence Partitioning - partitions "first visit (nothing saved)" and "visit after data was saved".

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-36-01 | EP | First visit with nothing saved in the browser: the save checkbox is not ticked. | Positive | |
| TCD-36-02 | EP | Visit after Name and Email were saved: the save checkbox is ticked or not ticked, as confirmed for Q-14. | Positive | Edge case: checkbox state on a return visit.<br>Missing info: not stated (Q-14). |

### TR-37: Verify that when the save checkbox is ticked at submit, the name and email are filled in again on the next visit in the same browser.

Technique(s): State transition - browser storage states "nothing saved" and "Name and Email saved"; events "Submit with box ticked", "Submit with box not ticked", "rejected Submit". Error guessing - other browser or private window.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-37-01 | State transition | Nothing saved, valid Submit with the box ticked, next visit in the same browser: Name and Email are filled with the submitted values. | Positive | Assumption: only name and email are saved (Q-13, Q-14).<br>Risk: personal data stored on the device. |
| TCD-37-02 | State transition | Name and Email saved, valid Submit with a different Name and Email and the box ticked, next visit: the new values are filled. | Positive | Assumption: saved values are replaced (Q-14). |
| TCD-37-03 | State transition | Name and Email saved, valid Submit with the box not ticked, next visit: Name and Email are filled or empty as confirmed for Q-14. | Positive | Missing info: how saved data is removed (Q-14).<br>Risk: personal data left on a shared device. |
| TCD-37-04 | EP | After a ticked Submit, on the next visit only Name and Email are filled; rating and review are empty. | Positive | Assumption: only name and email are saved (Q-13, Q-14). |
| TCD-37-05 | Error guessing | After a ticked Submit, opening the page in another browser or a private window: Name and Email are empty. | Positive | Edge case: "in this browser" only. |
| TCD-37-06 | State transition | Nothing saved, box ticked but Submit rejected (for example "Your review" empty), next visit: Name and Email are empty. | Negative | Edge case: rejected submit with the box ticked.<br>Missing info: whether data is saved on a rejected submit (Q-14). |

### TR-38: Verify that when the save checkbox is not ticked, no name or email is kept for the next visit.

Technique(s): Equivalence Partitioning - partition "box not ticked, nothing saved before". Error guessing - data typed but not submitted.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-38-01 | EP | Nothing saved, valid Submit with the box not ticked, next visit: Name and Email are empty. | Positive | Missing info: what is saved when the checkbox is not ticked (Q-14).<br>Risk: personal data left on a shared device. |
| TCD-38-02 | Error guessing | Name and Email typed but not submitted, page reloaded: Name and Email are empty (browser autofill switched off). | Positive | Missing info: Q-14.<br>Risk: personal data kept without consent. |

### TR-39: Verify that a customer cannot submit more reviews for the same product than the confirmed limit.

Technique(s): Boundary Value Analysis - count of reviews per customer and product (limit unknown). Error guessing - other product, changed identity.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-39-01 | BVA | Customer has limit - 1 reviews for the product, submits another: accepted. | Positive | Missing info: number of reviews per customer and product not specified (Q-12). If the limit is 1, this is the first review (TCD-33-01) and is not repeated. |
| TCD-39-02 | BVA | Customer has exactly the limit, submits another (limit + 1): rejected with the message confirmed for Q-12. | Negative | Edge case: one above the limit.<br>Missing info: Q-12. |
| TCD-39-03 | Error guessing | Customer at the limit for product A submits a review for product B: accepted. | Positive | Missing info: Q-12; needs a build with two products. |
| TCD-39-04 | Error guessing | Customer at the limit submits again for the same product with a different Name and Email: still recognised and rejected. | Negative | Missing info: how the customer is identified (Q-01, Q-02, Q-12).<br>Risk: limit bypassed by changing name or email. |

### TR-40: Verify that clicking Submit more than once quickly creates only one review.

Technique(s): Error guessing - double click, repeated key presses, reload and browser back/forward after submit are known duplicate sources.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-40-01 | Error guessing | Valid form, Submit double-clicked: one review is created (one pending, one shown after approval). | Negative | Edge case: rapid double click.<br>Assumption: only one review is created (Q-28).<br>Risk: duplicate reviews distort the rating. |
| TCD-40-02 | Error guessing | Valid form, Submit clicked and Enter pressed in a text field before the confirmation appears: one review is created. | Negative | Assumption: only one review is created (Q-28). |
| TCD-40-03 | Error guessing | Page reloaded right after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |
| TCD-40-04 | Error guessing | Browser Back and then Forward after a successful Submit: no second review is created. | Negative | Assumption: only one review is created (Q-28). |

### TR-41: Verify that when the review cannot be saved (server or network error), the customer is told and the entered data is kept.

Technique(s): Error guessing - lost connection, server error and expired session are typical failure points of a submit.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-41-01 | Error guessing | Network connection lost, Submit: a message says the review was not submitted and the entered data stays in the form. | Negative | Assumption: Q-29.<br>Missing info: demo-1.0 runs without a server or network (environment.md), so this cannot be produced there. |
| TCD-41-02 | Error guessing | Server returns an error on Submit: a message says the review was not submitted and the entered data stays in the form. | Negative | Assumption: Q-29. Not producible in demo-1.0. |
| TCD-41-03 | Error guessing | Session expired before Submit (signed-in customer): the customer is told and the entered data is not lost. | Negative | Assumption: Q-29.<br>Missing info: sign-in rules (Q-01); demo-1.0 has no sign-in. |
| TCD-41-04 | Error guessing | After a failed Submit, the connection returns and Submit is pressed again: exactly one review is created. | Positive | Assumption: Q-28, Q-29. |

## Coverage by scenario type

| Type | Covered by (condition IDs) |
|---|---|
| Positive | TCD-02-01, TCD-03-01 to TCD-03-04, TCD-04-01, TCD-04-02, TCD-04-05, TCD-06-01, TCD-08-01, TCD-09-01 to TCD-09-04, TCD-14-01, TCD-17-01, TCD-29-01, TCD-31-01, TCD-33-01, TCD-33-02, TCD-35-01, TCD-37-01 |
| Negative | TCD-02-02, TCD-04-03, TCD-05-01, TCD-07-01, TCD-10-01 to TCD-10-04, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-05, TCD-29-06, TCD-30-01, TCD-31-03 to TCD-31-08, TCD-34-01, TCD-34-02, TCD-39-02 |
| Boundary | TCD-03-01 to TCD-03-04, TCD-05-01, TCD-09-01 to TCD-09-04, TCD-10-01 to TCD-10-03, TCD-11-04, TCD-21-02 to TCD-21-04, TCD-22-01, TCD-22-03, TCD-23-05, TCD-29-07 to TCD-29-10, TCD-31-10 to TCD-31-12, TCD-39-01, TCD-39-02 |
| Validation | TCD-05-01, TCD-07-01, TCD-10-01, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-05, TCD-29-06, TCD-30-01, TCD-31-03 to TCD-31-08, TCD-32-02, TCD-32-04, TCD-34-01 to TCD-34-04 |
| Error handling | TCD-40-01 to TCD-40-04, TCD-41-01 to TCD-41-04 |
| Permissions | TCD-26-01 to TCD-26-04, TCD-27-01, TCD-27-02, TCD-13-01, TCD-16-01, TCD-16-02, TCD-39-02, TCD-39-04 |
| Integration | TCD-13-01, TCD-13-02, TCD-14-01 to TCD-14-03, TCD-15-01, TCD-15-02, TCD-17-01 to TCD-17-03, TCD-18-01, TCD-20-01 to TCD-20-03, TCD-21-01, TCD-22-01 to TCD-22-03, TCD-23-01 to TCD-23-06, TCD-24-01, TCD-24-02 |
| UI | TCD-01-01, TCD-02-03, TCD-02-04, TCD-06-01, TCD-06-02, TCD-18-04, TCD-25-01 to TCD-25-07 |
| Compatibility | None in this design; see "Not covered" |
| Regression | TCD-14-02, TCD-15-02, TCD-18-01, TCD-20-02, TCD-22-03, TCD-23-04 (existing approved reviews, the empty state and the rating summary still behave correctly after new reviews are added) |
| Data and privacy | TCD-12-01 to TCD-12-05, TCD-17-03, TCD-19-01, TCD-19-02, TCD-36-01, TCD-36-02, TCD-37-01 to TCD-37-06, TCD-38-01, TCD-38-02 |

## Not covered

| Type or area | Reason |
|---|---|
| Compatibility: browsers other than Chrome, mobile and tablet screen sizes | Only Chrome is given (environment.md, app-note.md); other browsers and devices are blocked by missing information (Q-31). Add conditions when Q-31 is answered. |
| Language and localisation | Page language not stated; English assumed (Q-31). |
| Moderator screens and workflow (approve / reject UI, who moderates) | Out of scope of US-VP02; only its effect on the product page is covered (TR-14, TR-15). The demo-1.0 helper button is a test tool, not the feature (environment.md). |
| Telling the author the moderation result (for example by email) | Assumed out of scope of this story (Q-26). |
| Editing or deleting one's own review | Assumed out of scope of this story (Q-27). |
| Automatic offensive-language filter | Assumed left to the moderator, no automatic filter (Q-30). |
| "Website" field | No Website field exists in mockup-1; nothing to test until Q-13 is answered (only the checkbox text is covered, TCD-25-04). |
| Accessibility beyond keyboard use (screen reader labels, colour contrast) | Not in any source; only keyboard use is covered (TCD-02-04, TCD-25-07). |
| Performance and load (many users submitting at once) | Not in the story; needs another environment. |
| Execution on demo-1.0 of TCD-13-01, TCD-13-02, TCD-15-01, TCD-15-02, TCD-23-03, TCD-24-02, TCD-26-01 to TCD-26-04, TCD-27-01, TCD-27-02, TCD-39-03, TCD-39-04, TCD-41-01 to TCD-41-03 | The conditions exist, but demo-1.0 has one product, no sign-in, no reject action, no server, and resets data on reload (app-note.md, environment.md); they need another build or environment. |

## Assumptions to confirm

| Condition ID | Assumption | Question ID |
|---|---|---|
| TCD-02-01, TCD-03-01 to TCD-03-04 | The rating is a whole number from 1 to 5, one per star. | Q-03 |
| TCD-02-03 | A hover preview, if any, is not kept after the pointer leaves. | New, to be added to Q-16 |
| TCD-04-01 to TCD-04-04 | Clicking another star changes the rating; it cannot be cleared except by reloading the page. | Q-16 |
| TCD-08-02 | "Your review" has no character restriction (accented, non-Latin, emoji allowed). | New, to be added to Q-15 |
| TCD-10-02 to TCD-10-04 | Typing and pasting stop at the maximum length. | Q-18 |
| TCD-11-01 to TCD-11-04, TCD-32-01 to TCD-32-04 | Spaces (and line breaks) are trimmed; a field of only spaces counts as empty; length is counted after trimming. | Q-17 |
| TCD-12-01 | HTML and script content is never executed, whatever the answer on how it is handled. | Q-15 |
| TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-34-01, TCD-34-02 | Each error names its field; wording is checked for meaning, not exact text. | Q-20 |
| TCD-34-03 | Entered values stay in the form after a rejected Submit. | New, to be added to Q-19 |
| TCD-34-04 | Fields are checked on Submit only. | Q-19 |
| TCD-14-01 | The demo-1.0 "Moderator: approve pending reviews" helper stands in for the moderator and is not part of the feature. | Q-07 |
| TCD-17-01 | Each displayed review shows star rating, reviewer name, date and review text. | Q-09 |
| TCD-17-02 | The date is the submit date, in any unambiguous format. | Q-24 |
| TCD-18-02, TCD-29-01 to TCD-29-03 | Names with letters, spaces, accented letters, hyphens and apostrophes are accepted. | Q-05 |
| TCD-21-01 | All approved reviews are shown on one page. | Q-23 |
| TCD-22-01 to TCD-22-03 | With no approved reviews, a short message says there are no reviews yet. | Q-25 |
| TCD-25-01 | The heading "ADD A REVIEW" is compared without regard to letter case. | Q-32 |
| TCD-31-01 to TCD-31-09 | A valid email has the standard format text@domain.tld (top-level domain required, letter case ignored). | Q-06 |
| TCD-33-01, TCD-33-02 | The confirmation says the review was received and waits for approval. | Q-21 |
| TCD-35-01, TCD-35-02 | After success the customer stays on the page; the form is cleared; Name and Email stay only if the checkbox was ticked. | Q-22 |
| TCD-37-01, TCD-37-02, TCD-37-04 | Only Name and Email are saved in this browser, and a new ticked submit replaces them. | Q-13, Q-14 |
| TCD-40-01 to TCD-40-04, TCD-41-04 | Only one review is created per submit action. | Q-28 |
| TCD-41-01 to TCD-41-04 | On a save failure a message says the review was not submitted and the entered data is kept. | Q-29 |
