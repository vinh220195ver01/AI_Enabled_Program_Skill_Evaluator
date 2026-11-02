# Test design: US-VP02 Submit a Product Review

Input: runs/run-1/test-requirements.xlsx (41 TRs, TR-01 to TR-41) · Answers used: none (runs/run-1/clarification-questions.md read for question IDs and working assumptions; no product owner answers received) · Date: 2026-10-21

Knowledge read: knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md; exam/user-story.md, exam/mockup-1.png, exam/app-note.md. The demo build is the product under test and is never used as a source of expected results.

Positive / Negative: Positive = a valid input or allowed flow that must succeed. Negative = an invalid input, a forbidden action, or an outcome that must not happen.

Placeholders used where no source gives the value (not invented): REVIEW_MIN, REVIEW_MAX (Q-04), NAME_MAX (Q-05), EMAIL_MAX (Q-06), LIMIT (Q-12), PAGE_SIZE (Q-23). Each condition that uses one carries a Missing info note.

## Values and rules used

| Item | Value | Status (Confirmed / Assumption) | Source |
|---|---|---|---|
| Number of stars in "Your rating *" | 5 | Confirmed | mockup-1.png (R6) |
| Rating values | Whole number 1 to 5, one per star; no half stars | Assumption | product-review-rules.md A1; Q-03 |
| Changing / clearing the rating | Clicking another star changes the rating; it cannot be cleared to no rating except by reloading | Assumption | Q-16 |
| Hover over stars | A hover preview, if any, is not kept | Assumption | Q-36 |
| Required fields | Your rating, Your review, Name, Email (marked *) | Confirmed | mockup-1.png (R2) |
| "Your review" control | Multi-line text box | Confirmed | mockup-1.png, AC-02 |
| "Your review" minimum and maximum length | Not stated (REVIEW_MIN, REVIEW_MAX). Demo build shows "0 / 500" counter: Observed only, not a requirement | Missing info | Q-04; screens-and-fields.md F2 |
| Text longer than the maximum | Typing and pasting stop at the maximum | Assumption | Q-18 |
| Characters allowed in "Your review" | No restriction (accented, non-Latin, digits, punctuation, emoji) | Assumption | Q-37 |
| Line breaks in a displayed review | Shown as entered | Assumption | Q-35 |
| Leading / trailing spaces, whitespace-only fields | Trimmed; a field with only spaces counts as empty | Assumption | Q-17 |
| "Name" length and allowed characters | Not stated (NAME_MAX); minimum length not stated and not asked by any question | Missing info | Q-05 |
| "Email" format rule and maximum length | Not stated (EMAIL_MAX) | Missing info | Q-06 |
| When fields are validated | On Submit only | Assumption | Q-19 |
| Error messages | Each error names the field concerned; wording checked for meaning, not exact text | Assumption | Q-20 |
| Values after a rejected Submit | Entered values stay in the form | Assumption | Q-38 |
| Success message | Says the review was received and waits for approval | Assumption | Q-21 |
| Form after a successful Submit | Customer stays on the product page; form cleared; Name and Email stay filled only if the save checkbox was ticked | Assumption | Q-22 |
| Double Submit | Only one review is created | Assumption | Q-28 |
| Save failure (server, network, session) | A message says the review was not submitted; entered data kept | Assumption | Q-29 |
| Email publication | The email address is not published | Confirmed | mockup-1.png (R3) |
| What is displayed on the product page | Only approved reviews | Confirmed | AC-03 (R4) |
| Review life cycle | New review is pending until approved | Confirmed (derived) | AC-03 (R5); app-note.md |
| Approval in the demo build | "Moderator: approve pending reviews" approves every pending review | Confirmed (test environment only) | app-note.md |
| Who approves, rejection possible | Not stated | Missing info | Q-07 |
| Author's view of a pending review | Not stated | Missing info | Q-08 |
| Details shown per review | Star rating, reviewer name, date, review text; never email | Assumption | product-review-rules.md A2; Q-09 |
| Date shown | Submit date, any unambiguous format | Assumption | Q-24 |
| Order of reviews | Not stated | Missing info | Q-10 |
| Number of reviews shown | All approved reviews on one page | Assumption | Q-23 |
| Product with no approved reviews | A short message saying there are no reviews yet | Assumption | Q-25 |
| Rating summary and review count | Whether shown, calculation and rounding not stated | Missing info | Q-11 |
| Who may submit | Sign-in and purchase check not stated; cancelled / refunded orders not stated | Missing info | Q-01, Q-33 |
| Name and Email for a signed-in customer | Conflict between story and mockup-1 | Missing info | Q-02 |
| Heading "ADD A REVIEW" | Compared without regard to letter case | Assumption | Q-32 |
| Save checkbox default | Unchecked | Confirmed | mockup-1.png (F5) |
| Save checkbox text | Mentions "website" but there is no Website field | Missing info | Q-13 |
| What the save checkbox stores | Only Name and Email; nothing when not ticked | Assumption | Q-13, Q-14 |
| Reviews per customer and product | Not stated (LIMIT) | Missing info | Q-12 |
| HTML, scripts, links in text | Display treatment not stated; content is never executed | Missing info (display) / Assumption (never executed) | Q-15; TR-12 |
| Keyboard use | Rating, fields, checkbox and Submit usable by keyboard; Tab follows screen order | Assumption | Q-34 |
| Browser and language | Desktop Chrome, English | Assumption (Chrome Confirmed for the demo environment) | Q-31; app-note.md |
| Demo build data | One product; reload restores initial data; only the save-checkbox choice is kept | Confirmed (test environment only) | app-note.md |

## Test conditions

### TR-01: Verify that the "Your rating *" field shows 5 stars.

Technique(s): Equivalence Partitioning - the control has one valid display state on first open (5 stars, none selected); the count limit itself is tested by BVA in TR-03.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-01-01 | EP | On first opening the product page, "Your rating *" shows exactly 5 star icons and none is selected. | Positive | |

### TR-02: Verify that the customer can select a rating by clicking a star, and the selected stars are shown as selected.

Technique(s): Equivalence Partitioning - whole-star values form one valid partition (one representative), half-star input is a separate partition; Error guessing - hover and keyboard use are common defect sources on star widgets.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-02-01 | EP | Clicking the 3rd star selects a rating of 3: stars 1 to 3 are shown as selected and stars 4 and 5 as not selected. | Positive | Assumption: whole number 1 to 5, one per star (Q-03). |
| TCD-02-02 | EP | Clicking on the left half of a star selects a whole star only (no half-star value such as 2.5). | Negative | Missing info: whether half stars are allowed (Q-03). |
| TCD-02-03 | Error guessing | Moving the pointer over the stars after a rating is selected, then away without clicking, leaves the selected rating unchanged. | Negative | Assumption: a hover preview is not kept (Q-36). |
| TCD-02-04 | Error guessing | The rating can be selected with the keyboard only (Tab to the stars, then arrow keys / Enter / Space). | Positive | Assumption: rating usable with the keyboard (Q-34). |

### TR-03: Verify that both the lowest rating (1 star) and the highest rating (5 stars) can be selected and are saved with the review.

Technique(s): Boundary Value Analysis - the rating is a range 1 to 5; 3-value BVA on both ends. The value just below the lower boundary (0 = no rating) is TCD-05-01.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-03-01 | BVA | Rating 1 (on the lower boundary) is selected, submitted, and shown as 1 star after approval. | Positive | Edge case: lowest rating.<br>Assumption: range 1 to 5 (Q-03). |
| TCD-03-02 | BVA | Rating 2 (just above the lower boundary) is selected, submitted, and shown as 2 stars after approval. | Positive | Assumption: range 1 to 5 (Q-03). |
| TCD-03-03 | BVA | Rating 4 (just below the upper boundary) is selected, submitted, and shown as 4 stars after approval. | Positive | Assumption: range 1 to 5 (Q-03). |
| TCD-03-04 | BVA | Rating 5 (on the upper boundary) is selected, submitted, and shown as 5 stars after approval. | Positive | Edge case: highest rating.<br>Assumption: range 1 to 5 (Q-03). |
| TCD-03-05 | BVA | A rating of 6 (just above the upper boundary) cannot be selected: with 5 stars selected, pressing the right arrow key or clicking just right of the 5th star keeps the rating at 5. | Negative | Edge case: value above the maximum.<br>Assumption: range 1 to 5 (Q-03). |

### TR-04: Verify that the customer can change the selected rating before submitting, and only the last selected rating is saved.

Technique(s): State transition - the rating control moves between "no rating" and "n stars"; each valid change and the invalid "clear by clicking again" event are covered; Error guessing - reload as the only reset.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-04-01 | State transition | No rating -> 4 stars -> 2 stars (change to a lower value), then Submit: the saved review has rating 2. | Positive | |
| TCD-04-02 | State transition | 2 stars -> 5 stars (change to a higher value), then Submit: the saved review has rating 5. | Positive | |
| TCD-04-03 | State transition | Clicking the already selected star again does not clear the rating back to "no rating". | Negative | Assumption: the rating cannot be cleared by clicking (Q-16). |
| TCD-04-04 | Error guessing | After selecting a rating, reloading the page returns the control to "no rating". | Positive | Assumption: reload is the only way to clear the rating (Q-16). |

### TR-05: Verify that the review cannot be submitted when no star rating is selected.

Technique(s): Equivalence Partitioning - "no rating" is the invalid partition of a required field; it is also the value just below the lower boundary (0) of TR-03.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-05-01 | EP / BVA | No star selected (rating 0), all other fields valid: the review is not submitted and an error names the rating field. | Negative | Edge case: just below the lower boundary 1.<br>Assumption: error names the field; wording checked for meaning (Q-20). |

### TR-06: Verify that a multi-line text box "Your review *" is provided for the review comment.

Technique(s): Equivalence Partitioning - single-line and multi-line text are separate input partitions; Error guessing - line breaks are often lost when text is displayed.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-06-01 | EP | Pressing Enter inside "Your review" adds a new line and does not submit the form. | Positive | |
| TCD-06-02 | Error guessing | A review written on several lines keeps its line breaks when displayed on the product page after approval. | Positive | Assumption: line breaks shown as entered (Q-35). |

### TR-07: Verify that the review cannot be submitted when "Your review" is empty.

Technique(s): Equivalence Partitioning - empty is the invalid partition of a required field.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-07-01 | EP | "Your review" empty (0 characters), all other fields valid: the review is not submitted and an error names "Your review". | Negative | Assumption: error names the field; wording checked for meaning (Q-20). |

### TR-08: Verify that review text within the allowed length is accepted and saved as entered.

Technique(s): Equivalence Partitioning - one representative of the valid length partition and of the valid character partition; Error guessing - pasted text and padded text.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-08-01 | EP | A review of ordinary length (between REVIEW_MIN and REVIEW_MAX, for example one sentence) is accepted and saved exactly as entered. | Positive | Missing info: minimum and maximum length not stated (Q-04). |
| TCD-08-02 | EP | A review containing accented and non-Latin letters, digits, punctuation and emoji is accepted and displayed exactly as entered. | Positive | Assumption: no character restriction (Q-37). |
| TCD-08-03 | Error guessing | A review pasted from the clipboard (within the limit) is accepted the same way as typed text. | Positive | |
| TCD-08-04 | Error guessing | A review with leading and trailing spaces is accepted and saved without those spaces. | Positive | Assumption: spaces are trimmed (Q-17). |

### TR-09: Verify that review text of exactly the minimum length and exactly the maximum length is accepted.

Technique(s): Boundary Value Analysis - length limits; values on and just inside each boundary.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-09-01 | BVA | A review of exactly REVIEW_MIN characters is accepted. | Positive | Edge case: on the minimum.<br>Missing info: minimum length not stated (Q-04). |
| TCD-09-02 | BVA | A review of REVIEW_MIN + 1 characters is accepted. | Positive | Missing info: minimum length not stated (Q-04). |
| TCD-09-03 | BVA | A review of REVIEW_MAX - 1 characters is accepted. | Positive | Missing info: maximum length not stated (Q-04). |
| TCD-09-04 | BVA | A review of exactly REVIEW_MAX characters is accepted and displayed in full after approval (not cut). | Positive | Edge case: on the maximum.<br>Missing info: maximum length not stated (Q-04). |

### TR-10: Verify that review text shorter than the minimum or longer than the maximum is not accepted.

Technique(s): Boundary Value Analysis - values just outside each length limit; Error guessing - pasted and very long text.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-10-01 | BVA | A review of REVIEW_MIN - 1 characters is not accepted and an error names "Your review". | Negative | Edge case: just below the minimum.<br>Missing info: minimum length not stated (Q-04). If REVIEW_MIN is 1, this value is the empty case TCD-07-01 and this condition is dropped. |
| TCD-10-02 | BVA | Typing REVIEW_MAX + 1 characters: the box stops at REVIEW_MAX characters. | Negative | Edge case: just above the maximum.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: typing stops at the maximum (Q-18). |
| TCD-10-03 | BVA | Pasting a text of REVIEW_MAX + 1 characters: the box keeps only REVIEW_MAX characters, or Submit is rejected with an error. | Negative | Edge case: just above the maximum by paste.<br>Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |
| TCD-10-04 | Error guessing | Pasting a very long text (about 10 x REVIEW_MAX characters) does not freeze the page and is handled as in TCD-10-03. | Negative | Missing info: maximum length not stated (Q-04).<br>Assumption: pasting stops at the maximum (Q-18). |

### TR-11: Verify that review text made only of spaces is treated as empty and the review is not submitted.

Technique(s): Equivalence Partitioning - whitespace-only text is an invalid partition separate from empty text; Error guessing - other whitespace characters.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-11-01 | EP | "Your review" containing only spaces is treated as empty: the review is not submitted and an error names "Your review". | Negative | Edge case: whitespace-only input.<br>Assumption: a field with only spaces counts as empty (Q-17). |
| TCD-11-02 | Error guessing | "Your review" containing only line breaks (Enter pressed several times) is treated as empty and not submitted. | Negative | Edge case: whitespace-only input.<br>Assumption: line breaks are treated like spaces for this rule (Q-17). |

### TR-12: Verify that HTML tags, script code and links entered in "Your review" or "Name" are never run as code on the product page.

Technique(s): Error guessing - script injection, HTML and link text are known defect sources wherever user text is displayed.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-12-01 | Error guessing | A review containing a script tag (for example `<script>alert(1)</script>`) does not run any script when the approved review is displayed. | Negative | Risk: script injection affects every visitor of the product page.<br>Missing info: shown as plain text, removed or rejected (Q-15). |
| TCD-12-02 | Error guessing | A review containing an HTML event attribute (for example `<img src=x onerror=alert(1)>`) does not run any script when displayed. | Negative | Risk: script injection.<br>Missing info: display treatment (Q-15). |
| TCD-12-03 | Error guessing | A Name containing script code does not run any script where the reviewer name is displayed. | Negative | Risk: script injection.<br>Missing info: display treatment (Q-15). |
| TCD-12-04 | Error guessing | A review containing formatting tags (for example `<b>`, `<h1>`) does not change the layout or formatting of the product page. | Negative | Missing info: shown as plain text, removed or rejected (Q-15). |
| TCD-12-05 | Error guessing | A review containing a web link (https://...) is handled as confirmed for Q-15 (plain text, removed or rejected). | Negative | Missing info: link handling not stated (Q-15). |

### TR-13: Verify that a newly submitted review is not displayed on the product page while it waits for approval.

Technique(s): State transition - review life cycle (none -> Pending -> Approved / Rejected); covers the valid "Submit" transition and the invalid "Pending -> displayed without approval".

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-13-01 | State transition | Valid Submit moves the review to Pending: it is not added to the reviews list and the "Reviews (n)" count does not change. | Positive | Risk: unmoderated content shown publicly.<br>Missing info: whether the author sees their own pending review (Q-08); this condition checks the public list. |
| TCD-13-02 | State transition | Invalid transition Pending -> displayed without an approval event: after further actions on the page (another review submitted, page scrolled, form reused), the pending review is still not displayed. | Negative | Risk: unmoderated content shown publicly. |

### TR-14: Verify that a submitted review is displayed on the product page after it is approved.

Technique(s): State transition - the "Approve" event from Pending to Approved, and the invalid repeat of that event.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-14-01 | State transition | Pending -> Approved: after approval, the review appears in the reviews list. | Positive | Missing info: who approves and how (Q-07); in the demo build approval is done with "Moderator: approve pending reviews" (app-note.md). |
| TCD-14-02 | State transition | Two pending reviews approved together both appear, each exactly once. | Positive | Missing info: approval process (Q-07). |
| TCD-14-03 | State transition | Invalid event: approving again when nothing is pending adds no review and does not duplicate already approved reviews. | Negative | Edge case: repeated approval. |

### TR-15: Verify that a rejected review is never displayed on the product page.

Technique(s): State transition - the "Reject" event from Pending to Rejected, and the invalid transition Rejected -> displayed.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-15-01 | State transition | Pending -> Rejected: a rejected review is not displayed on the product page. | Negative | Missing info: whether a review can be rejected and what happens to it (Q-07). The demo build has no reject action. |
| TCD-15-02 | State transition | Invalid transition Rejected -> Approved: a later approval of other pending reviews does not display the rejected review. | Negative | Missing info: rejection workflow (Q-07). |

### TR-16: Verify that the author sees their own pending review only in the way confirmed for Q-08 (marked as awaiting approval, or not at all).

Technique(s): Equivalence Partitioning - two viewer partitions (the author, any other visitor) for a Pending review.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-16-01 | EP | Right after Submit, the author sees their own pending review as confirmed for Q-08 (marked as awaiting approval, or not shown). | Positive | Missing info: author's view of a pending review (Q-08). |
| TCD-16-02 | EP | Another visitor (different browser or account) does not see the author's pending review, even if the author does. | Negative | Risk: unmoderated content shown publicly.<br>Missing info: author's view (Q-08). Needs an environment with shared stored data; the demo build keeps data per page load (app-note.md). |

### TR-17: Verify that each displayed review shows the confirmed details (star rating, reviewer name, date, review text).

Technique(s): Equivalence Partitioning - one approved review is the valid partition; the name form is a partition decided by Q-09.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-17-01 | EP | An approved review shows its star rating, reviewer name, date and review text. | Positive | Assumption: these four details are shown (Q-09). |
| TCD-17-02 | EP | The date shown for a review submitted today is today's date, in an unambiguous format. | Positive | Assumption: submit date, any unambiguous format (Q-24). |
| TCD-17-03 | EP | The reviewer name is shown in the form confirmed for Q-09 (full name, first name only or initials). | Positive | Missing info: form of the name (Q-09). |

### TR-18: Verify that the star rating, name and review text of a displayed review match what the customer submitted.

Technique(s): Equivalence Partitioning - one representative submitted review; Error guessing - special characters shown as codes and data mixed between reviews.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-18-01 | EP | After approval, the displayed rating, name and review text are identical to the submitted values (case, punctuation, spelling). | Positive | |
| TCD-18-02 | Error guessing | A review and name containing `& < > " '` are displayed with those characters, not as codes such as `&amp;`. | Positive | Edge case: characters that are often escaped twice. |
| TCD-18-03 | Error guessing | Two reviews with different ratings, names and texts, submitted one after the other and approved together, each keep their own values (no mix-up). | Positive | |

### TR-19: Verify that the reviewer's email address is never displayed on the product page.

Technique(s): Error guessing - places where personal data leaks unnoticed (visible text, page source, attributes).

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-19-01 | Error guessing | After approval, the reviewer's email address appears nowhere in the visible product page (review, author line, tooltips, success message area). | Negative | Risk: personal data shown publicly.<br>Confirmed: email not published (mockup-1.png). |
| TCD-19-02 | Error guessing | The reviewer's email address is not present in the page source of the product page (hidden fields, attributes, links such as `mailto:`). | Negative | Risk: personal data exposed to anyone who views the source. |

### TR-20: Verify that approved reviews are listed in the confirmed order.

Technique(s): Equivalence Partitioning - a set of reviews that differ in date and rating, so that any ordering rule gives a visible result; Error guessing - placement of a newly approved review.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-20-01 | EP | With at least 3 approved reviews that differ in date and rating, the list follows the order confirmed for Q-10. | Positive | Missing info: list order not specified (Q-10). |
| TCD-20-02 | Error guessing | A newly approved review is placed in the correct position among the existing reviews (not always at the end). | Positive | Missing info: list order not specified (Q-10). |

### TR-21: Verify that all approved reviews can be seen when a product has many reviews.

Technique(s): Equivalence Partitioning - "many reviews" partition; Boundary Value Analysis - page size, only if paging is confirmed.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-21-01 | EP | With many approved reviews (20 or more), every approved review is visible on the page and the "Reviews (n)" count equals the number listed. | Positive | Edge case: large number of reviews.<br>Assumption: all approved reviews on one page (Q-23). |
| TCD-21-02 | BVA | If paging is confirmed: PAGE_SIZE reviews show on one page with no paging control; PAGE_SIZE + 1 reviews show paging or "Load more" and the extra review is reachable. | Positive | Missing info: page size, only if Q-23 confirms paging; dropped if all reviews are on one page. |

### TR-22: Verify that a clear empty state is shown when the product has no approved reviews.

Technique(s): Boundary Value Analysis - approved review count 0 and 1; State transition - a pending review must not leave the empty state.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-22-01 | BVA | 0 approved reviews: a message says there are no reviews yet, and the count shows 0. | Positive | Edge case: no approved reviews.<br>Assumption: short "no reviews yet" message (Q-25). |
| TCD-22-02 | BVA | 1 approved review (0 -> 1): the empty-state message is gone, one review is listed and the count shows 1. | Positive | Edge case: first approved review. |
| TCD-22-03 | State transition | 0 approved and 1 pending review: the empty-state message is still shown and the count still shows 0. | Negative | Risk: pending content counted publicly. |

### TR-23: Verify that the average rating and review count on the product page, if shown, are calculated from approved reviews only.

Technique(s): State transition - summary before and after the Pending -> Approved event; Error guessing - averages after a change, rounding and division by zero.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-23-01 | Error guessing | With approved ratings 5 and 4, the summary shows average 4.5 and count 2. | Positive | Missing info: whether a summary is shown and how it is rounded (Q-11). |
| TCD-23-02 | State transition | A new 1-star review in Pending does not change the average or the count. | Negative | Risk: pending reviews change the score shown to shoppers.<br>Missing info: summary rule (Q-11). |
| TCD-23-03 | State transition | After that review is approved, the average and count are recalculated to include it. | Positive | Missing info: summary rule (Q-11). |
| TCD-23-04 | Error guessing | Approved ratings 5, 4, 4 (average 4.333...) are displayed with the confirmed rounding. | Positive | Edge case: repeating decimal.<br>Missing info: rounding not specified (Q-11). |
| TCD-23-05 | Error guessing | With 0 approved reviews, the summary shows no rating / 0 reviews without an error value (for example "NaN"). | Negative | Edge case: average of zero reviews.<br>Missing info: summary rule (Q-11). |

### TR-24: Verify that a review is displayed only on the page of the product it was written for.

Technique(s): Equivalence Partitioning - two product partitions (the reviewed product, any other product).

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-24-01 | EP | A review approved for product A is displayed on product A and not on product B. | Negative | Risk: reviews on the wrong product mislead shoppers.<br>Needs an environment with at least 2 products; the demo build has one product (app-note.md). |

### TR-25: Verify that the review form shows the heading, the info text, the fields, the save checkbox and the "Submit" button as in mockup-1.

Technique(s): Equivalence Partitioning - the form on first open is one valid partition checked element by element against mockup-1; Error guessing - keyboard focus order.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-25-01 | EP | The heading reads "ADD A REVIEW". | Positive | Assumption: compared without regard to letter case (Q-32). |
| TCD-25-02 | EP | The info text reads "Your email address will not be published. Required fields are marked *". | Positive | |
| TCD-25-03 | EP | The labels "Your rating *", "Your review *", "Name *" and "Email *" are shown with the required marker, in the mockup-1 order. | Positive | |
| TCD-25-04 | EP | The save checkbox text and the "Submit" button are shown below the fields as in mockup-1. | Positive | Missing info: final text of the save checkbox (Q-13). |
| TCD-25-05 | Error guessing | Tab moves through stars, "Your review", "Name", "Email", checkbox and "Submit" in screen order, and every control can be used with the keyboard alone. | Positive | Assumption: keyboard use and focus order (Q-34). |

### TR-26: Verify that only a customer who is allowed to review (as confirmed for Q-01) can submit a review, and a customer who is not allowed cannot.

Technique(s): Decision table - conditions: signed in (Y/N), bought the product (Y/N), order cancelled or refunded (Y/N); outcome: may submit / may not. Rules for a guest are collapsed into one (purchase cannot be checked without an account). Error guessing - bypassing a hidden form.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-26-01 | Decision table | Rule 1: signed in, bought the product, order not cancelled: the customer can submit a review. | Positive | Missing info: sign-in and purchase check (Q-01). |
| TCD-26-02 | Decision table | Rule 2: signed in, did not buy the product: the form is hidden, disabled or Submit is rejected with a message, as confirmed for Q-01. | Negative | Risk: non-buyers post fake reviews.<br>Missing info: purchase check (Q-01). |
| TCD-26-03 | Decision table | Rule 3: guest (not signed in): handled as confirmed for Q-01. | Negative | Risk: fake reviews.<br>Missing info: whether guests may review (Q-01). |
| TCD-26-04 | Decision table | Rule 4: signed in, bought the product but the order was cancelled or refunded: handled as confirmed for Q-33. | Negative | Missing info: cancelled or refunded orders (Q-33). |
| TCD-26-05 | Error guessing | A customer who is not allowed submits through a form left open in another tab (for example after signing out): Submit is rejected. | Negative | Risk: rule checked only on the screen, not on Submit.<br>Missing info: who may review (Q-01). |

### TR-27: Verify that Name and Email for a signed-in customer are handled as confirmed for Q-02 (prefilled, editable or not shown).

Technique(s): Equivalence Partitioning - signed-in customer partition; the three possible behaviours of Q-02 decide the expected result.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-27-01 | EP | A signed-in customer opens the form: Name and Email are prefilled from the account, editable or not shown, as confirmed for Q-02. | Positive | Missing info: conflict between the story and mockup-1 (Q-02). |
| TCD-27-02 | EP | If Name and Email are prefilled and editable, a signed-in customer who changes them gets the changed values used for the review as confirmed for Q-02. | Positive | Missing info: conflict between the story and mockup-1 (Q-02). |

### TR-28: Verify that the review cannot be submitted when "Name" is empty.

Technique(s): Equivalence Partitioning - empty is the invalid partition of a required field.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-28-01 | EP | "Name" empty, all other fields valid: the review is not submitted and an error names "Name". | Negative | Assumption: error names the field; wording checked for meaning (Q-20). |

### TR-29: Verify that a Name within the allowed length and characters is accepted, and a Name outside them is rejected.

Technique(s): Equivalence Partitioning - valid and invalid character partitions, one at a time; Boundary Value Analysis - Name length.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-29-01 | EP | A plain Latin name with a space (for example "Anna Tran") is accepted. | Positive | |
| TCD-29-02 | EP | A name with accented letters, a hyphen and an apostrophe (for example "Lê Thị-Ánh O'Neil") is accepted as confirmed for Q-05. | Positive | Edge case: accented letters, hyphen, apostrophe.<br>Missing info: allowed characters (Q-05). |
| TCD-29-03 | EP | A name made only of digits (for example "12345") is accepted or rejected as confirmed for Q-05. | Negative | Missing info: allowed characters (Q-05). |
| TCD-29-04 | EP | A name made only of symbols (for example "@#$%") is accepted or rejected as confirmed for Q-05. | Negative | Missing info: allowed characters (Q-05). |
| TCD-29-05 | BVA | A name of 1 character (just above empty) is accepted or rejected as confirmed. | Positive | Edge case: shortest name.<br>Missing info: minimum Name length not stated and not covered by any question (suggest adding to Q-05). |
| TCD-29-06 | BVA | A name of NAME_MAX - 1 characters is accepted. | Positive | Missing info: maximum length (Q-05). |
| TCD-29-07 | BVA | A name of exactly NAME_MAX characters is accepted and displayed in full. | Positive | Edge case: on the maximum.<br>Missing info: maximum length (Q-05). |
| TCD-29-08 | BVA | A name of NAME_MAX + 1 characters is blocked while typing or rejected on Submit. | Negative | Edge case: just above the maximum.<br>Missing info: maximum length and over-length handling (Q-05). |

### TR-30: Verify that the review cannot be submitted when "Email" is empty.

Technique(s): Equivalence Partitioning - empty is the invalid partition of a required field.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-30-01 | EP | "Email" empty, all other fields valid: the review is not submitted and an error names "Email". | Negative | Assumption: error names the field; wording checked for meaning (Q-20). |

### TR-31: Verify that a correctly formatted email is accepted and an incorrectly formatted email is rejected.

Technique(s): Equivalence Partitioning - valid formats and one invalid partition per format fault, each tested alone; Boundary Value Analysis - Email length.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-31-01 | EP | A standard address (for example "anna@example.com") is accepted. | Positive | Missing info: email format rule (Q-06). |
| TCD-31-02 | EP | An address with a dot and plus in the local part and a subdomain (for example "anna.tran+shop@mail.example.co.uk") is accepted. | Positive | Edge case: less common valid format.<br>Missing info: email format rule (Q-06). |
| TCD-31-03 | EP | An address in upper case (for example "Anna@Example.COM") is accepted. | Positive | Missing info: email format rule (Q-06). |
| TCD-31-04 | EP | An address without "@" (for example "anna.example.com") is rejected and an error names "Email". | Negative | Missing info: email format rule (Q-06). |
| TCD-31-05 | EP | An address without a local part (for example "@example.com") is rejected. | Negative | Missing info: email format rule (Q-06). |
| TCD-31-06 | EP | An address without a domain (for example "anna@") is rejected. | Negative | Missing info: email format rule (Q-06). |
| TCD-31-07 | EP | An address without a top-level domain (for example "anna@example") is accepted or rejected as confirmed for Q-06. | Negative | Missing info: email format rule (Q-06). |
| TCD-31-08 | EP | An address with a space inside (for example "an na@example.com") is rejected. | Negative | Missing info: email format rule (Q-06). |
| TCD-31-09 | EP | An address with two "@" (for example "anna@@example.com") is rejected. | Negative | Missing info: email format rule (Q-06). |
| TCD-31-10 | BVA | An address of EMAIL_MAX - 1 characters is accepted. | Positive | Missing info: maximum length (Q-06). |
| TCD-31-11 | BVA | An address of exactly EMAIL_MAX characters is accepted. | Positive | Edge case: on the maximum.<br>Missing info: maximum length (Q-06). |
| TCD-31-12 | BVA | An address of EMAIL_MAX + 1 characters is blocked or rejected. | Negative | Edge case: just above the maximum.<br>Missing info: maximum length (Q-06). |

### TR-32: Verify that leading and trailing spaces in Name and Email are removed, and a Name or Email made only of spaces counts as empty.

Technique(s): Equivalence Partitioning - whitespace-only is an invalid partition per field; Error guessing - space-padded values.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-32-01 | Error guessing | A Name with leading and trailing spaces is accepted and displayed without them. | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
| TCD-32-02 | Error guessing | An Email with leading and trailing spaces is accepted (not rejected as a bad format). | Positive | Edge case: space-padded input.<br>Assumption: spaces are trimmed (Q-17). |
| TCD-32-03 | EP | A Name made only of spaces counts as empty: not submitted, error names "Name". | Negative | Edge case: whitespace-only input.<br>Assumption: only spaces counts as empty (Q-17). |
| TCD-32-04 | EP | An Email made only of spaces counts as empty: not submitted, error names "Email". | Negative | Edge case: whitespace-only input.<br>Assumption: only spaces counts as empty (Q-17). |

### TR-33: Verify that when all required fields are valid, the review is submitted and a confirmation message is shown.

Technique(s): Decision table - the "all four required fields valid" rule, with the optional checkbox as an extra condition that must not change the outcome.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-33-01 | Decision table | Rating, review, Name and Email valid, checkbox not ticked: the review is submitted and a confirmation says it was received and waits for approval. | Positive | Assumption: confirmation wording (Q-21). |
| TCD-33-02 | Decision table | Same valid data with the checkbox ticked: the review is submitted with the same confirmation. | Positive | Assumption: confirmation wording (Q-21). |

### TR-34: Verify that when a required field is empty or invalid, the review is not submitted and an error message names each field concerned.

Technique(s): Decision table - 4 required fields give 16 rules; the "all valid" rule is TR-33, the four single-failure rules are TCD-05-01, TCD-07-01, TCD-28-01 and TCD-30-01 (invalid email: TCD-31-04); the remaining multi-failure rules give the same outcome and are collapsed into "all fail" and one two-failure rule, which check that every failing field is named. State transition - error shown -> corrected -> submitted. Error guessing - values kept, validation timing.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-34-01 | Decision table | All four required fields empty: not submitted, and an error names each of Rating, Your review, Name and Email. | Negative | Assumption: errors name each field; checked on Submit only (Q-19, Q-20). |
| TCD-34-02 | Decision table | No rating and an invalid Email together (other fields valid): not submitted, and both fields are named. | Negative | Two failures on purpose, to check that all errors are reported together; each one alone is TCD-05-01 and TCD-31-04.<br>Assumption: errors name each field (Q-20). |
| TCD-34-03 | Error guessing | After a rejected Submit, the rating, review text, Name and Email already entered are still in the form. | Positive | Assumption: values kept after a rejected Submit (Q-38). |
| TCD-34-04 | State transition | Error shown -> the customer fixes the field -> Submit: the review is submitted and the error is no longer shown. | Positive | |
| TCD-34-05 | Error guessing | Leaving a required field empty and moving to the next field shows no error until Submit is clicked. | Positive | Assumption: fields checked on Submit only (Q-19). |

### TR-35: Verify that after a successful submit the customer stays on the product page and the form is cleared.

Technique(s): State transition - form state after the Submit event, with and without the save checkbox; Error guessing - reload/back after Submit and the rest of the page (regression).

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-35-01 | State transition | After a successful Submit with the checkbox not ticked: the customer stays on the product page and rating, review, Name and Email are all cleared. | Positive | Assumption: form cleared (Q-22). |
| TCD-35-02 | State transition | After a successful Submit with the checkbox ticked: rating and review are cleared, Name and Email stay filled. | Positive | Assumption: Name and Email stay only if the checkbox was ticked (Q-22). |
| TCD-35-03 | Error guessing | Using browser Back or Reload right after a successful Submit does not submit the review a second time. | Negative | Edge case: resubmit by browser navigation.<br>Risk: duplicate reviews distort the rating. |
| TCD-35-04 | Error guessing | After Submit and after approval, the other parts of the product page (header links, Cart (0), product name, price, description) are unchanged and still work. | Positive | Regression check of the page that holds the form. |

### TR-36: Verify that the "Save my name, email, and website..." checkbox is unchecked by default.

Technique(s): Equivalence Partitioning - first visit (nothing saved) and returning visit (data saved) are separate partitions for the default state.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-36-01 | EP | On a first visit with nothing saved, the save checkbox is not ticked. | Positive | Confirmed: unchecked in mockup-1.png. |
| TCD-36-02 | EP | On a return visit after saving Name and Email, the checkbox state is as confirmed for Q-14. | Positive | Missing info: checkbox state when data is already saved (Q-14). |

### TR-37: Verify that when the save checkbox is ticked at submit, the name and email are filled in again on the next visit in the same browser.

Technique(s): State transition - saved data state across visits (nothing saved -> saved -> updated -> removed); Error guessing - data remembered between visits.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-37-01 | State transition | Nothing saved -> tick the checkbox and Submit a valid review -> on the next visit, Name and Email are prefilled with the submitted values. | Positive | Risk: personal data stored on the device.<br>Assumption: only Name and Email are saved (Q-13, Q-14). |
| TCD-37-02 | Error guessing | On the next visit after a saved Submit, the rating and review text are not prefilled. | Negative | Assumption: only Name and Email are saved (Q-14). |
| TCD-37-03 | State transition | Saved -> Submit again with the checkbox ticked and a different Name and Email -> on the next visit the new values are prefilled. | Positive | Assumption: saved values are replaced (Q-14). |
| TCD-37-04 | State transition | Saved -> Submit with the checkbox not ticked -> on the next visit Name and Email are no longer prefilled. | Negative | Risk: personal data left on a shared device.<br>Missing info: whether unticking removes saved data (Q-14). |
| TCD-37-05 | Error guessing | Checkbox ticked but Submit rejected (for example empty review): nothing is saved, or data is saved as confirmed for Q-14. | Negative | Missing info: whether data is saved on a rejected Submit (Q-14). |

### TR-38: Verify that when the save checkbox is not ticked, no name or email is kept for the next visit.

Technique(s): Equivalence Partitioning - "not ticked" partition; Error guessing - ticked then unticked before Submit.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-38-01 | EP | Checkbox not ticked, valid Submit, next visit: Name and Email are empty. | Negative | Risk: personal data left on a shared device.<br>Missing info: what is saved when not ticked (Q-14). |
| TCD-38-02 | Error guessing | Checkbox ticked and then unticked before a valid Submit: on the next visit Name and Email are empty. | Negative | Edge case: changed mind before Submit.<br>Missing info: what is saved when not ticked (Q-14). |

### TR-39: Verify that a customer cannot submit more reviews for the same product than the confirmed limit.

Technique(s): Boundary Value Analysis - count limit LIMIT per customer and product; Equivalence Partitioning - same product vs another product; Error guessing - pending reviews counted toward the limit.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-39-01 | BVA | The customer's review that reaches LIMIT for this product (for example the first review if LIMIT is 1) is accepted. | Positive | Missing info: number of reviews per customer and product (Q-12). |
| TCD-39-02 | BVA | A review that would be number LIMIT + 1 for the same product is rejected as confirmed for Q-12. | Negative | Edge case: just above the limit.<br>Missing info: limit and message (Q-12); how the same customer is identified (account or email) also depends on Q-01. |
| TCD-39-03 | EP | The same customer can review a different product even when the limit is reached on the first product. | Positive | Missing info: limit is per product (Q-12). Needs at least 2 products; the demo build has one (app-note.md). |
| TCD-39-04 | Error guessing | A review still in Pending counts toward the limit (a second attempt while the first is pending is handled as in TCD-39-02). | Negative | Missing info: whether pending reviews count (Q-12). |

### TR-40: Verify that clicking Submit more than once quickly creates only one review.

Technique(s): Error guessing - double click on Submit is a classic duplicate-record defect.

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-40-01 | Error guessing | Double-clicking Submit with valid data creates one pending review only (pending count +1; one review after approval). | Negative | Edge case: rapid double click.<br>Risk: duplicate reviews distort the rating.<br>Assumption: only one review is created (Q-28). |
| TCD-40-02 | Error guessing | Clicking Submit and then pressing Enter immediately creates one pending review only. | Negative | Edge case: mixed mouse and keyboard submit.<br>Assumption: only one review is created (Q-28). |

### TR-41: Verify that when the review cannot be saved (server or network error), the customer is told and the entered data is kept.

Technique(s): Error guessing - failure during Submit (network, server, session).

| Condition ID | Technique | Test condition | Positive / Negative | Notes |
|---|---|---|---|---|
| TCD-41-01 | Error guessing | Network connection lost when Submit is clicked: a message says the review was not submitted and all entered values are kept. | Negative | Assumption: message shown and data kept (Q-29). Needs an environment with a server; the demo build runs without a server (app-note.md). |
| TCD-41-02 | Error guessing | Server error or timeout on Submit: a message says the review was not submitted, all entered values are kept and no pending review is created. | Negative | Assumption: message shown and data kept (Q-29). Needs an environment with a server. |
| TCD-41-03 | Error guessing | Session expired before Submit (signed-in customer): a message is shown and the entered values are kept. | Negative | Assumption: message shown and data kept (Q-29).<br>Missing info: sign-in rules (Q-01). |

## Coverage by scenario type

| Type | Covered by (condition IDs) |
|---|---|
| Positive | TCD-01-01, TCD-02-01, TCD-03-01 to TCD-03-04, TCD-04-01, TCD-04-02, TCD-06-01, TCD-08-01 to TCD-08-04, TCD-09-01 to TCD-09-04, TCD-14-01, TCD-14-02, TCD-17-01, TCD-18-01, TCD-26-01, TCD-29-01, TCD-31-01, TCD-33-01, TCD-33-02, TCD-35-01, TCD-37-01 |
| Negative | TCD-02-02, TCD-03-05, TCD-04-03, TCD-05-01, TCD-07-01, TCD-10-01 to TCD-10-04, TCD-11-01, TCD-11-02, TCD-15-01, TCD-15-02, TCD-26-02 to TCD-26-05, TCD-28-01, TCD-29-03, TCD-29-04, TCD-29-08, TCD-30-01, TCD-31-04 to TCD-31-09, TCD-31-12, TCD-34-01, TCD-34-02 |
| Boundary | Rating: TCD-03-01 to TCD-03-05, TCD-05-01. Review length: TCD-07-01, TCD-09-01 to TCD-09-04, TCD-10-01 to TCD-10-03. Name length: TCD-28-01, TCD-29-05 to TCD-29-08. Email length: TCD-31-10 to TCD-31-12. Review count: TCD-21-01, TCD-21-02, TCD-22-01, TCD-22-02, TCD-39-01, TCD-39-02 |
| Validation | TCD-05-01, TCD-07-01, TCD-10-01, TCD-11-01, TCD-11-02, TCD-28-01, TCD-29-03, TCD-29-04, TCD-29-08, TCD-30-01, TCD-31-04 to TCD-31-09, TCD-31-12, TCD-32-03, TCD-32-04, TCD-34-01 to TCD-34-05 |
| Error handling | TCD-35-03, TCD-40-01, TCD-40-02, TCD-41-01 to TCD-41-03 |
| Permissions | TCD-26-01 to TCD-26-05, TCD-27-01, TCD-27-02, TCD-39-01 to TCD-39-04 |
| Integration | TCD-13-01, TCD-14-01 to TCD-14-03, TCD-17-01 to TCD-17-03, TCD-18-01 to TCD-18-03, TCD-20-01, TCD-20-02, TCD-21-01, TCD-22-01 to TCD-22-03, TCD-23-01 to TCD-23-05, TCD-24-01 |
| UI | TCD-01-01, TCD-02-01, TCD-02-03, TCD-02-04, TCD-06-01, TCD-25-01 to TCD-25-05, TCD-36-01 |
| Compatibility | Not covered (see below) |
| Regression | TCD-35-04 |
| Data and privacy | TCD-12-01 to TCD-12-05, TCD-13-01, TCD-13-02, TCD-16-01, TCD-16-02, TCD-19-01, TCD-19-02, TCD-36-02, TCD-37-01 to TCD-37-05, TCD-38-01, TCD-38-02 |

## Not covered

| Type or area | Reason |
|---|---|
| Compatibility: browsers other than Chrome, mobile and tablet screen sizes, page language | Out of scope until Q-31 is answered; app-note.md names Chrome only for the build under test, and no TR covers other browsers or devices. |
| Persistence of submitted and approved reviews after page reload or on another day | Needs another environment: the demo build restores its initial data on reload (app-note.md). No TR states persistence; it is implied by AC-03. |
| Moderator screen (how a moderator finds, approves and rejects reviews) | Out of scope of the story; the demo build simulates approval with one button (app-note.md); process unknown (Q-07). Only the effect on the product page is designed (TR-13 to TR-15). |
| Notification to the author when a review is approved or rejected | Out of scope of the story (Q-26 assumption: no notification); no TR. |
| Edit or delete own review | Out of scope of the story (Q-27 assumption); no TR. |
| Offensive language filtering | Q-30 assumption: left to the moderator, no automatic filter; no TR. |
| Character counter "n / 500" under "Your review" | Observed in the demo build only; not in the story or mockup-1, so not a requirement. Its expected behaviour depends on Q-04. |
| Visual styling against mockup-1 (colours, fonts, sizes, spacing) | Not specified as a requirement; TR-25 covers texts, labels, order and keyboard use only. |
| Accessibility beyond keyboard use (screen reader names for the stars, contrast) | Not in any source and no TR; keyboard use is covered as an assumption (TCD-02-04, TCD-25-05). |
| Performance and load (many visitors submitting at once) | Not in the story; no TR. |
| Error handling conditions TCD-41-01 to TCD-41-03, multi-product conditions TCD-24-01 and TCD-39-03, and the second-viewer condition TCD-16-02 | Designed, but blocked in the demo build (no server, one product, data per page load); they need another environment. |

## Assumptions to confirm

| Condition ID | Assumption | Question ID |
|---|---|---|
| TCD-02-01, TCD-03-01 to TCD-03-05 | The rating is a whole number from 1 to 5, one per star. | Q-03 |
| TCD-02-03 | A hover preview on the stars is not kept after the pointer leaves. | Q-36 |
| TCD-02-04, TCD-25-05 | The rating and the whole form can be used by keyboard; Tab follows screen order. | Q-34 |
| TCD-04-03, TCD-04-04 | Clicking the selected star again does not clear the rating; only a reload clears it. | Q-16 |
| TCD-05-01, TCD-07-01, TCD-28-01, TCD-30-01, TCD-34-01, TCD-34-02 | Each error names the field concerned; wording checked for meaning, not exact text. | Q-20 |
| TCD-06-02 | Line breaks are shown as entered. | Q-35 |
| TCD-08-02 | No character restriction in "Your review". | Q-37 |
| TCD-08-04, TCD-11-01, TCD-11-02, TCD-32-01 to TCD-32-04 | Leading and trailing spaces are trimmed; a whitespace-only field counts as empty (line breaks treated like spaces). | Q-17 |
| TCD-10-02 to TCD-10-04 | Typing and pasting stop at the maximum length. | Q-18 |
| TCD-17-01 | Each displayed review shows star rating, reviewer name, date and review text. | Q-09 |
| TCD-17-02 | The submit date is shown, in any unambiguous format. | Q-24 |
| TCD-21-01 | All approved reviews are shown on one page. | Q-23 |
| TCD-22-01 | A short message says there are no reviews yet. | Q-25 |
| TCD-25-01 | The heading "ADD A REVIEW" is compared without regard to letter case. | Q-32 |
| TCD-33-01, TCD-33-02 | The confirmation says the review was received and waits for approval. | Q-21 |
| TCD-34-01, TCD-34-05 | Fields are checked on Submit only. | Q-19 |
| TCD-34-03 | Entered values stay in the form after a rejected Submit. | Q-38 |
| TCD-35-01, TCD-35-02 | After a successful Submit the customer stays on the page; the form is cleared, Name and Email stay only if the checkbox was ticked. | Q-22 |
| TCD-37-01 to TCD-37-03 | Only Name and Email are saved, and a new ticked Submit replaces them. | Q-13, Q-14 |
| TCD-40-01, TCD-40-02 | Only one review is created on a double Submit. | Q-28 |
| TCD-41-01 to TCD-41-03 | On a save failure a message is shown and the entered data is kept. | Q-29 |
| TCD-12-01 to TCD-12-05 | HTML, script and links are never executed, whatever the answer to Q-15. | Q-15 |
