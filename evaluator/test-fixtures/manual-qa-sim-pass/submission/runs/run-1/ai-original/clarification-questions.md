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
