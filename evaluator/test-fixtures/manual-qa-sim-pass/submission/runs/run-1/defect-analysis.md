# Defect analysis: US-VP02 Submit a Product Review

Environment (as provided): Build demo-1.0, Browser Chrome (source: `exam/app-note.md`, `knowledge/environment.md`); browser version, operating system and screen size: Not provided · Date: 2026-10-21

Inputs used: `runs/run-1/test-execution.xlsx` (sheet Execution), `evidence/run-1/*.png`, `runs/run-1/test-cases.xlsx`, `runs/run-1/clarification-questions.md` (question IDs), `knowledge/`, `exam/` (user story, mockup, app note). The application source code was not used; all facts come from what was seen through the UI.

## Evidence reviewed

| EV ID | File or source | What it shows |
|---|---|---|
| EV-01 | `runs/run-1/test-execution.xlsx`, sheet Execution | 145 rows: 66 Pass, 9 Fail (TC-02-04, TC-03-01, TC-17-01, TC-17-03, TC-18-01, TC-18-02, TC-19-01, TC-19-02, TC-32-01), 22 Observed, 22 Blocked, 26 Not run. "Executed on" for every executed row: "demo-1.0 / Chrome (headless) / 2026-10-21". All 45 rows with an accepted submit record the message "Thank you! Your review has been submited and is awaiting approval." |
| EV-02 | `evidence/run-1/TC-02-04.png` | Focus box on the 1st star; 1 star filled, text "1 star"; form otherwise empty; "Pending approval: 0". |
| EV-03 | `evidence/run-1/TC-03-01.png` | Error box "Please select a rating." while the 1st star is filled and the text "1 star" is shown; Your review "Rating check: one star.", Name "Anna Smith", Email "anna.smith@example.com"; "Pending approval: 0"; approve button greyed out; "Reviews (3)". |
| EV-04 | `evidence/run-1/TC-12-01.png` | Message "Thank you! Your review has been submited and is awaiting approval."; newest review: 4 stars, "anna.smith@example.com", "October 21, 2026", text "<script>alert(1)</script>" as plain text; "1 review approved." |
| EV-05 | `evidence/run-1/TC-12-03.png` | Same message; newest review: "anna.smith@example.com", text "<b>bold</b> text check" as plain text. |
| EV-06 | `evidence/run-1/TC-12-04.png` | Same message; newest review: "anna.smith@example.com", text "Link check https://example.com" (not shown as a link). |
| EV-07 | `evidence/run-1/TC-12-05.png` | Same message; newest review: 4 stars, "anna.smith@example.com", text "Name script check."; no name shown. |
| EV-08 | `evidence/run-1/TC-16-01.png` | Message "Thank you! Your review has been submited and is awaiting approval."; "Pending approval: 1"; "Reviews (3)" (Mai T., David L., Anna K.); rating summary "3.0 out of 5 – based on 4 reviews". |
| EV-09 | `evidence/run-1/TC-16-02.png` | Same message; newest review: 4 stars, "anna.smith@example.com", "October 21, 2026", "Author view: approved check."; no "awaiting approval" mark. |
| EV-10 | `evidence/run-1/TC-17-01.png` | Same message; "Reviews (4)"; newest review: 4 stars, "anna.smith@example.com", "October 21, 2026", "Details check: all parts shown."; the name "Anna Smith" is not shown. Summary "4.0 out of 5 – based on 4 reviews". |
| EV-11 | `evidence/run-1/TC-17-03.png` | Same message; newest review: 4 stars, "anna.smith@example.com", "Name form check."; no name shown. |
| EV-12 | `evidence/run-1/TC-18-01.png` | Same message; "Reviews (5)"; 5 stars "chloe.diaz@example.com" "Second review: perfect fit."; 2 stars "ben.carter@example.com" "First review: too tight."; names "Chloe Diaz" and "Ben Carter" not shown; "2 reviews approved."; summary "3.8 out of 5 – based on 5 reviews". |
| EV-13 | `evidence/run-1/TC-18-02.png` | Same message; newest review: 4 stars, "anna.smith@example.com", "Special name check."; the name "Zoë O'Brien-Lê" is not shown. |
| EV-14 | `evidence/run-1/TC-18-03.png` | Same message; newest review: "anna.smith@example.com", text `5 > 3 & "good" isn't it` as typed. |
| EV-15 | `evidence/run-1/TC-19-01.png` | Same message; newest review: 4 stars, "unique.reviewer@example.com", "October 21, 2026", "Email privacy check: visible page."; the text above the form still says "Your email address will not be published." |
| EV-16 | `evidence/run-1/TC-19-02.png` | Same message; newest review: 4 stars, "unique.reviewer@example.com", "Email privacy check: hidden parts.". The screenshot shows the page only: no tooltip, no DevTools panel. |
| EV-17 | `evidence/run-1/TC-20-01.png` | Initial page: "Reviews (3)", top to bottom Mai T. (October 8, 2026, 3 stars), David L. (September 29, 2026, 4 stars), Anna K. (September 14, 2026, 5 stars); summary "4.0 out of 5 – based on 3 reviews"; empty form. |
| EV-18 | `evidence/run-1/TC-20-02.png` | Same message; "Order check: newly approved." at position 1 of 4, shown with "anna.smith@example.com". |
| EV-19 | `evidence/run-1/TC-23-01.png` | Error box "Please select a rating." with the 1st star filled and "1 star"; review "Summary check: approved 1 star."; "Pending approval: 0"; summary "4.0 out of 5 – based on 3 reviews". |
| EV-20 | `evidence/run-1/TC-23-02.png` | Error box "Please select a rating." with the 1st star filled and "1 star"; review "Summary check: pending 1 star."; "Pending approval: 0". |
| EV-21 | `evidence/run-1/TC-23-04.png` | Same message; "Reviews (4)"; summary "4.0 out of 5 – based on 4 reviews"; newest review "anna.smith@example.com", "Summary check: count.". |
| EV-22 | `evidence/run-1/TC-23-05.png` | Same message; newest review: 2 stars, "anna.smith@example.com", "Rounding check: two stars."; summary "3.5 out of 5 – based on 4 reviews". |
| EV-23 | `evidence/run-1/TC-29-04.png` | Byte-identical to EV-08 (TC-16-01.png): message "...submited...", "Pending approval: 1", form empty. Does not show the Name value entered for this case. |
| EV-24 | `evidence/run-1/TC-29-05.png` | Byte-identical to EV-08. |
| EV-25 | `evidence/run-1/TC-29-06.png` | Byte-identical to EV-08. |
| EV-26 | `evidence/run-1/TC-29-07.png` | Byte-identical to EV-08. |
| EV-27 | `evidence/run-1/TC-32-01.png` | Same message; newest review: 4 stars, "anna.smith@example.com", "Name trim check."; no name shown. The DevTools Elements panel is not in the screenshot. |
| EV-28 | `evidence/run-1/TC-36-02.png` | After reload: checkbox ticked, Name "Anna Smith", Email "anna.smith@example.com". |
| EV-29 | `evidence/run-1/TC-37-03.png` | Byte-identical to EV-17 (initial page, Name and Email empty). |
| EV-30 | `evidence/run-1/TC-37-06.png` | Byte-identical to EV-17. |
| EV-31 | `evidence/run-1/TC-38-01.png` | Byte-identical to EV-17. |
| EV-32 | `evidence/run-1/TC-38-02.png` | Byte-identical to EV-17. |
| EV-33 | Tester statement in chat, 2026-10-21 | "the console was empty in every case so no log files". No console log file exists. |

All email addresses in the evidence use the reserved domain example.com (synthetic test data, `knowledge/environment.md`); no masking is needed.

## Defects

### BUG-01: [Reviews] Reviewer's email address is published in place of the name

- Related test cases: TC-19-01, TC-19-02, TC-17-01, TC-17-03, TC-18-01, TC-18-02, TC-32-01
- Evidence: EV-01, EV-15, EV-16, EV-10, EV-11, EV-12, EV-13, EV-27 (same symptom also visible in EV-04 to EV-07, EV-09, EV-14, EV-18, EV-21, EV-22)

**Facts (seen in evidence)**

- After Submit and approval, every new review shows the value typed in "Email *" in the reviewer-name position: "anna.smith@example.com" (EV-10, EV-11, EV-13, EV-27), "ben.carter@example.com" and "chloe.diaz@example.com" (EV-12), "unique.reviewer@example.com" (EV-15, EV-16).
- The value typed in "Name *" ("Anna Smith", "Ben Carter", "Chloe Diaz", "Zoë O'Brien-Lê") is not shown anywhere in the review (EV-10 to EV-13, EV-27).
- The form keeps saying "Your email address will not be published." on the same page where the email is shown (EV-15).
- TC-19-01: Ctrl+F "unique.reviewer" finds 1 match on the visible page, in the reviewer-name position of the new review; the "Email *" input is empty after Submit (EV-01).
- TC-19-02: no tooltip, no mailto link; the DevTools Elements search finds "unique.reviewer@example.com" inside the reviewer-name element of the "Reviews" section (EV-01; the screenshot EV-16 shows the page, not the DevTools panel).
- Rating, date and review text of the new reviews are correct and are not swapped between two reviews (EV-12, TC-18-01 in EV-01).
- The three reviews present at page load show short names ("Mai T.", "David L.", "Anna K."), not email addresses (EV-17).
- 7 of the 9 failed cases show this same symptom; the tester's notes in EV-01 link them all to TC-17-01.

**Root cause hypotheses**

| # | Hypothesis | How to confirm |
|---|---|---|
| H1 | Hypothesis: when a new review is saved, its author value is taken from the "Email *" field instead of the "Name *" field (wrong field mapping at submit). The initial reviews are not affected because they do not go through the form. | Developer checks which form field fills the author of a new review. Tester: submit with Name "Name Only" and Email "email.only@example.com"; if "email.only@example.com" appears and "Name Only" appears nowhere, the mapping at submit is wrong. |
| H2 | Hypothesis: the name is saved correctly, but the review list shows the email property for reviews created through the form (wrong property used when rendering new reviews). | Developer checks which stored property the review list prints for new reviews; cannot be told apart from H1 through the UI alone. |

**Assumptions**

- Assumption: the name entered in "Name *" (in a form still to be confirmed: full name, first name or initials) is the value expected in the reviewer-name position, until Q-09 is answered. The defect does not depend on this assumption: showing the email at all contradicts R3 / mockup-1 ("Your email address will not be published.").

**Severity and priority**

| Item | Value | Reason |
|---|---|---|
| Severity | Critical | The email address of every reviewer is exposed to every visitor of the product page, against the form's own statement "Your email address will not be published." (R3); the guide puts personal data exposure under Critical. |
| Priority | P1 | It affects every review approved from now on and cannot be undone once published; it also blocks the verdict of TC-17-01, TC-17-03, TC-18-01, TC-18-02, TC-32-01 and TC-12-05, so it must be fixed before release and before the next test round. |

### BUG-02: [Rating] 1-star rating is rejected with "Please select a rating."

- Related test cases: TC-03-01 (also seen in TC-23-01 and TC-23-02, which are Observed and could not reach their intended state)
- Evidence: EV-03, EV-19, EV-20, EV-01

**Facts (seen in evidence)**

- With the 1st star clicked, the 1st star is filled and the text "1 star" is shown next to the stars (EV-03, EV-19, EV-20).
- With all other fields filled, Submit shows the error box "Please select a rating."; "Pending approval" stays 0; the approve button stays disabled; the review is not added (EV-03, EV-01).
- The tester repeated TC-03-01 twice in a fresh page with the same result (EV-01, Notes of TC-03-01).
- The same rejection happened in TC-23-01 ("Summary check: approved 1 star.", EV-19) and TC-23-02 ("Summary check: pending 1 star.", EV-20).
- Ratings 2, 3, 4 and 5 are accepted and shown correctly (TC-03-02 to TC-03-04, TC-04-05 in EV-01).
- TC-05-01 (no star selected) gives the same message "Please select a rating." (EV-01).

**Root cause hypotheses**

| # | Hypothesis | How to confirm |
|---|---|---|
| H1 | Hypothesis: the "is a rating selected" check treats the value 1 as "no rating" (for example a check for a value greater than 1, or a zero-based star index where the 1st star is 0). | Tester: click star 3, then star 1, then Submit; an error again supports H1. Developer: check the rating condition in the Submit validation. |
| H2 | Hypothesis: clicking the 1st star updates the display only and does not store the value, so the form still holds "no rating". | Tester: click star 2, then star 1, then Submit. If the review is accepted and later shown with 2 stars, the value was not stored (H2); if the error appears, H1 is more likely. Also try selecting the 1st star with Tab and Space (keyboard path seen in TC-02-04). |

**Assumptions**

- Assumption: 1 is a valid rating (whole numbers 1 to 5, one per star, A1 in `knowledge/product-review-rules.md`) until Q-03 is answered. The 5-star control (R6, mockup-1) and AC-01 "Allow customers to enter a star rating" are facts. If the product owner decides that 1 star is not allowed, the defect remains in another form: the 1st star can be selected and the message "Please select a rating." is wrong for that state.

**Severity and priority**

| Item | Value | Reason |
|---|---|---|
| Severity | High | A valid input of the main function (AC-01) is rejected: customers cannot give the lowest rating, and choosing 2 stars instead is not a reasonable workaround because it changes the opinion and raises the product's average. |
| Priority | P2 | Fix in the current iteration: the review flow works for ratings 2 to 5, so it does not block other testing except TC-23-01 and TC-23-02, but it biases every rating summary. |

### BUG-03: [Confirmation] success message misspells "submitted" as "submited"

- Related test cases: TC-33-01, TC-33-02 (Pass, typo noted by the tester); visible in every accepted submit, for example TC-16-01
- Evidence: EV-08, EV-01 (also visible in EV-04 to EV-07, EV-09 to EV-16, EV-18, EV-21 to EV-27)

**Facts (seen in evidence)**

- After every accepted Submit, the message above the form reads "Thank you! Your review has been submited and is awaiting approval." (EV-08 and all success screenshots; recorded word for word in all 45 accepted-submit rows of EV-01).
- The tester noted the typo in TC-33-01 and TC-33-02: "Confirmation text contains the typo "submited" (should be "submitted"); wording not compared by this case." (EV-01).
- The message otherwise says the review was received and waits for approval, which matches the assumption of TC-33-01 (Q-21).

**Root cause hypotheses**

| # | Hypothesis | How to confirm |
|---|---|---|
| H1 | Hypothesis: the confirmation text is stored with the spelling "submited". | Developer searches the message text for "submited"; fixing the text and repeating TC-33-01 shows "submitted". |

**Assumptions**

- Assumption: correct English spelling is expected in user-facing text. The exact wording of the success message is not specified (Q-21, OQ5); this bug concerns the spelling only, not the wording.

**Severity and priority**

| Item | Value | Reason |
|---|---|---|
| Severity | Low | Spelling error with no functional impact; the review is accepted and the meaning is clear. |
| Priority | P3 | Every reviewer sees it after each successful submit, which looks careless, but it does not block use or testing; the fix is a one-word text change that should go in before release. |

## Missing information

| # | What is missing | Why it matters | Who can provide it |
|---|---|---|---|
| 1 | Browser version, operating system and screen size ("Not provided" in `exam/app-note.md`). EV-01 also records the runs as "Chrome (headless)". | Needed in the bug reports; it is not confirmed that the results are the same in a normal (headed) Chrome window. | Tester / test lead (record the Chrome version; re-check BUG-01 to BUG-03 once in headed Chrome) |
| 2 | Q-09: which form of the reviewer name is shown (full name, first name or initials). | Expected Result of BUG-01 for the name part (TC-17-01, TC-17-03). | Product owner |
| 3 | Q-03: allowed rating values (1 to 5 whole stars is Assumption A1). | Confirms the Expected Result of BUG-02. | Product owner |
| 4 | Q-21 / OQ5: exact wording of the success message. | BUG-03 only covers the spelling; the full wording is still open. | Product owner |
| 5 | Q-34: must the star rating be usable with the keyboard alone, and how (arrow keys or Tab)? | Decides whether TC-02-04 is a defect (see "Failures not raised as bugs"). | Product owner |
| 6 | Q-11 / OQ8: is the rating summary calculated from approved reviews only, and how? | Needed to judge the summary seen in EV-08 (see "Failures not raised as bugs"). | Product owner |
| 7 | Screenshots of the DevTools Elements panel for TC-19-02 and TC-32-01. | The "hidden parts" fact of BUG-01 is supported only by the execution record (EV-01), not by an image. | Tester |
| 8 | Case-specific screenshots for TC-29-04 to TC-29-07 (byte-identical to TC-16-01.png) and TC-37-03, TC-37-06, TC-38-01, TC-38-02 (byte-identical to TC-20-01.png). | These images cannot show the result of their own case (for example the Name entered in TC-29-04); they are not used as proof of any bug. | Tester |
| 9 | Retest results after the fixes: TC-32-01 (trimming of Name), TC-18-02 (special characters in Name), TC-12-05 (Name display), TC-23-01 and TC-23-02 (summary with a 1-star review). | These checks could not be judged because BUG-01 or BUG-02 hides the result. | Tester, after BUG-01 and BUG-02 are fixed |

## Failures not raised as bugs

| TC ID | Reason (for example expected result not confirmed, test data error) |
|---|---|
| TC-02-04 | Expected result not confirmed: the case checks Assumption Q-34 (keyboard use), not an acceptance criterion. Fact (EV-01, EV-02): after Tab the focus is on "1 star"; Arrow Right pressed 4 times leaves the focus on "1 star"; Space selects 1 star. Tester note: Tab moves focus star by star and Space selects, so a rating can be set by keyboard with Tab. Question for the product owner: must the arrow keys move between the stars (Q-34)? Raise as a bug only if the answer requires it. |
| TC-16-01 (observation in EV-08, also EV-23 to EV-26) | Requirement silent (Q-11 / OQ8). Fact: with "Reviews (3)" listed (3, 4 and 5 stars) and "Pending approval: 1", the summary reads "3.0 out of 5 – based on 4 reviews"; at page load it reads "4.0 out of 5 – based on 3 reviews" (EV-17); after approval it is correct for the listed reviews (EV-10: "4.0 out of 5 – based on 4 reviews"). The pending review appears to be counted before approval, and 3.0 does not match the listed ratings. Not recorded in the Actual Result of TC-16-01. Question for the product owner: should the summary use approved reviews only (Q-11)? If yes, this becomes a defect; re-run TC-23-02 with a 4-star review to confirm. |
| TC-23-01, TC-23-02 | Observed (no verdict until Q-11); the intended state could not be reached because a 1-star review is rejected (BUG-02). Retest after BUG-02 is fixed. |
| TC-18-02, TC-32-01, TC-12-05 (name parts) | The special-character, trimming and HTML checks of "Name" cannot be judged while the name is not shown at all (BUG-01). TC-18-02 and TC-32-01 are listed under BUG-01 for the symptom they show; their own checks must be retested after the fix. |
| Other Observed rows (TC-12-01, TC-12-03, TC-12-04, TC-16-02, TC-18-03, TC-20-01, TC-20-02, TC-23-04, TC-23-05, TC-29-04 to TC-29-07, TC-36-02, TC-37-03, TC-37-06, TC-38-01, TC-38-02) | Observe-only cases waiting for Q-05, Q-08, Q-10, Q-11, Q-14, Q-15 or Q-20; no failure decided. Their screenshots are used only for the BUG-01 and BUG-03 symptoms they also show. |
