# Clarification questions: US-VP02 Submit a Product Review

Sources reviewed: exam/user-story.md, exam/mockup-1.png, exam/mockup-2.png (company logo only, no screen content), knowledge/index.md, knowledge/product-review-rules.md, knowledge/screens-and-fields.md, knowledge/glossary.md
Date: 2026-10-21

## Must ask

| Q ID | AC ID | Ambiguous point | Question | Why it matters |
|---|---|---|---|---|
| Q-01 | AC-GEN | Purchase check ("a product I purchased") | Must the system allow only customers who bought this product to submit a review, or can anyone who opens the product page submit one? If a purchase check applies, what does a non-buyer see? | Decides who can perform the action; without it the access tests have no expected result. |
| Q-02 | AC-GEN | Sign-in requirement | Must the customer be signed in to submit a review, or can a guest submit by typing Name and Email (as the mockup form suggests)? | The story speaks of a customer who purchased, while the form asks for Name and Email as for a guest; the expected access behaviour depends on the answer. |
| Q-03 | AC-01 | Star rating values | Is the rating a whole number of stars from 1 to 5, or are half stars (for example 3.5) allowed? | Defines the valid and invalid rating values to test and how the rating is stored and shown. |
| Q-04 | AC-02 | Review text length | What are the minimum and maximum lengths of "Your review" (for example 1 to 500 characters, another limit, or no limit)? What happens when the maximum is reached: typing is blocked, or an error is shown on submit? | Boundary tests need exact limits and the expected behaviour at and beyond them. |
| Q-05 | AC-02 | Review text made of spaces only | Is a review that contains only spaces or line breaks treated as empty (rejected), and are leading and trailing spaces removed before saving? | Decides whether such input passes the required-field check. |
| Q-06 | AC-GEN | Name field rules | What are the maximum length and the allowed characters of "Name" (letters only, digits, symbols, accented letters)? Is a Name of spaces only rejected? | Needed for valid and invalid Name tests; the story gives no rule. |
| Q-07 | AC-GEN | Email field rules | Which email format is accepted (for example name@domain.tld), and is there a maximum length? | Needed to decide which Email values are valid or invalid. |
| Q-08 | AC-03 | Moderation workflow | Who approves reviews, and can a review be rejected? If rejected, is it deleted or kept hidden, and is the author told? | AC-03 shows only approved reviews; the states and their effects must be known to test the display rule. |
| Q-09 | AC-GEN | Feedback after a successful submit | After a successful submit, is the author told that the review is waiting for approval? Is the form cleared or are the entered values kept? | Defines the expected result of the main submit flow. |
| Q-10 | AC-03 | Details shown per approved review | Which details are shown for each approved review: star rating, Name as entered, submission date, review text? Anything else? Please confirm that the email is never shown. | Defines the expected content of every displayed review and protects personal data. |
| Q-11 | AC-03 | Order and paging of reviews | In which order are approved reviews shown (newest first, oldest first, highest rating first), and is there a limit per page or a "load more" control? | Without it the display tests have no definite expected result. |
| Q-12 | AC-03 | Rating summary and review count | Does the product page show an average rating and a review count? If yes, are they calculated from approved reviews only, and how is the average rounded? | A calculation rule that changes the expected values on the product page. |
| Q-13 | AC-GEN | More than one review per customer | Can the same customer submit more than one review for the same product? If not, what happens on the second attempt? | Uniqueness rule that changes what is accepted. |
| Q-14 | AC-GEN | Checkbox mentions a Website field that does not exist | The checkbox says "Save my name, email, and website in this browser for the next time I comment." but the form has no Website field. Should a Website field be added, or should the label read "Save my name and email ..."? | Conflict inside the mockup; we cannot decide which one is correct. |
| Q-15 | AC-GEN | What the "Save my name, email ..." checkbox stores | When the checkbox is ticked, exactly what is saved, where (this browser only), and for how long? Are the saved values pre-filled on the next visit, and are they removed when the box is left unticked? | Privacy: personal data kept in the browser. |
| Q-16 | AC-02 | Content rules for review text | Are HTML tags, links or offensive words in the review blocked, removed, or shown as plain text? | Security and content risk on a public page; the expected result differs for each option. |

## Nice to confirm

| Q ID | AC ID | Ambiguous point | Question | Assumption used until answered |
|---|---|---|---|---|
| Q-17 | AC-GEN | Validation timing and message wording | Is the form validated on submit only, or also while typing or when leaving a field? What are the exact wording and position of the error messages? | Validation is done on submit; a message identifies each missing or invalid field; the exact wording and position are not checked. |
| Q-18 | AC-GEN | Success message wording | What is the exact text of the message shown after a successful submit? | Any clear confirmation message is accepted; the wording is not checked. |
| Q-19 | AC-01 | Changing the rating before submit | Can the customer change the selected rating by clicking another star before submitting? | Clicking another star replaces the earlier selection, and the last selection is submitted. |
| Q-20 | AC-02 | Allowed characters in review text | Are accented letters, emoji and line breaks allowed in "Your review"? | All printable characters and line breaks are allowed and are shown as entered. |
| Q-21 | AC-03 | Date format of a displayed review | In which format is the review date shown (for example 21/10/2026 or October 21, 2026)? | Any unambiguous date format is accepted. |
| Q-22 | AC-03 | Product page with no approved reviews | What is shown in the reviews area when a product has no approved reviews? | A short message saying there are no reviews yet is shown; the wording is not checked. |
| Q-23 | AC-GEN | Double submit | If Submit is clicked twice quickly, should only one review be created? | Only one review is created. |
| Q-24 | AC-GEN | Server or network error on submit | What should the customer see if the review cannot be saved because of a server or network error? | An error message is shown, no review is created, and the entered values are kept. |
| Q-25 | AC-GEN | Edit or delete own review | Is editing or deleting a submitted review out of scope for US-VP02? | Out of scope; no tests are planned for it. |
| Q-26 | AC-GEN | Supported browsers, devices and language | Which browsers, devices and languages must be supported? | Latest desktop Chrome, English user interface. |

## Conflicts between sources

| Q ID | Source A says | Source B says |
|---|---|---|
| Q-14 | mockup-1.png, checkbox label: "Save my name, email, and website in this browser for the next time I comment." | mockup-1.png, form fields: only "Your rating *", "Your review *", "Name *" and "Email *"; there is no Website field. |
