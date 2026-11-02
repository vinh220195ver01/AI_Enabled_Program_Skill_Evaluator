# Retest log - run-1 (demo-1.0, Chrome, 2026-10-21)

Browser UI only. Each retest used a fresh browser profile. No console messages, page errors or dialogs appeared in any retest.

| ID | Steps | Observed result | Evidence | Same as before / different |
|---|---|---|---|---|
| RT-01 | Fresh page; read summary and list; submit 4 stars, Ben Carter / ben.carter@example.com, "Summary check four stars."; read again before approve; approve; read again | Start: "4.0 out of 5 – based on 3 reviews", 3 reviews. After Submit (pending): "3.0 out of 5 – based on 4 reviews" while the list still shows 3 reviews, so the pending review is counted and the average drops to 3.0. After approve: "4.0 out of 5 – based on 4 reviews", 4 reviews (correct). Reviewer name shown as "ben.carter@example.com". | RT-01.png, RT-01.txt | Different (new finding): TC-23-02 could not show the pending-review effect because its 1-star submit was rejected. After approval it matches TC-23-04/TC-23-05 (summary correct). The name defect is the same as TC-17-01. |
| RT-02 | (a) Fresh page, star 2 then star 1, valid text/name/email, Submit. (b) Fresh page, star 1 only, Submit (as TC-03-01) | (a) 1 star shown as selected ("1 star"); Submit gives "Please select a rating.", Pending 0. (b) Same result: "Please select a rating.", Pending 0. | RT-02.png, RT-02.txt | Same as before (TC-03-01 Fail). It also fails when rating 1 is reached from 2. |
| RT-03 | Fresh page; 5 stars, Name "Zed Different", Email "other.person@example.com", "Name check."; Submit; approve | Reviewer name shown: "other.person@example.com". "Zed Different" is not shown anywhere in the review. 5 stars, date October 21, 2026, text "Name check.". | RT-03.png, RT-03-review.png, RT-03.txt | Same as before (TC-17-01): the name shown is always the Email value |
| RT-04 | TC-03-01 and TC-17-01 repeated in a visible (headless: false) Chrome window | TC-03-01: "Please select a rating.", Pending 0, not listed. TC-17-01: submitted, 4 stars, name "anna.smith@example.com". | RT-04-TC-03-01.png, RT-04-TC-17-01.png, RT-04.txt | Same as before (both Fail in headed and headless mode) |

## Evidence fixes in this round
- TC-29-04, TC-29-05, TC-29-06, TC-29-07, TC-37-03, TC-37-06, TC-38-01 and TC-38-02 were re-run. Each screenshot was replaced by a captioned, side-by-side image of that case's own states: for example, the typed name before Submit next to the result after Submit, or the form before reload next to the form after reload.
- Why the earlier files were identical: they matched TC-16-01.png / TC-20-01.png byte for byte because the final page states were the same. After a successful Submit the form is cleared, and after a reload the page returns to its initial state. They were taken in each case's own run, not copied, but they could not prove the case.
- The re-runs gave the same results: TC-29-04..07 were submitted (Pending 1); TC-37-03, TC-37-06, TC-38-01 and TC-38-02 show Name and Email empty after reload.
- TC-19-02-dom.txt and TC-32-01-dom.txt hold the outerHTML and text of the reviewer-name element of the review in question, taken from a re-run.
