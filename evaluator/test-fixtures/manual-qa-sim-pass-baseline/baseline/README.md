# Trainer answer key - manual-qa-sim-pass

This folder is the trainer's answer key for the `manual-qa-sim-pass` fixture. Trainees
receive only `exam/` (user story, Word file, mockups, `app-note.md` and the demo app in
`exam/app/`). Do not hand this folder to trainees.

- `baseline.json` - the manual-qa baseline (acceptance criteria, ambiguities and edge
  cases taken from `manual-qa-sample-review`, plus the planted bugs and the environment
  information given to trainees: build `demo-1.0`, browser `Chrome`, no OS).

The bugs in `exam/app` are **simulated**: they were planted in a small static demo so the
bug-finding and bug-report criteria can be exercised. They will be replaced by real bugs
of a real application later.

## Application facts used below

- Open `exam/app/index.html` in Chrome. Reload to reset the data (state is in memory).
- Seed data: 3 approved reviews - Anna K. (5 stars), David L. (4 stars), Mai T. (3 stars).
  Initial summary: "4.0 out of 5 - based on 3 reviews", heading "Reviews (3)".
- A valid submission = a star rating, a non-empty review, a Name and a valid Email.
- New reviews are "pending". The "Moderator: approve pending reviews" button approves all
  pending reviews.

## Planted bugs

### BUG-01 - A 1-star rating cannot be submitted (Major)

Location: Add a review form - Your rating (star input) / Submit validation.

Steps:
1. Open the page.
2. Click the first star (1 star). The first star turns yellow and "1 star" is shown.
3. Enter review "Too thin", Name "Tom", Email "tom@example.com".
4. Click Submit.

Expected: the review is accepted (success message, pending count becomes 1), as 1 star is
the lowest value of the 1-5 scale.
Actual: the error "Please select a rating." is shown and nothing is submitted, although a
star is selected. Repeating with 2, 3, 4 or 5 stars works.

### BUG-02 - Approved review shows the reviewer's email address publicly (Critical)

Location: Approved reviews list - reviewer name of a newly approved review.

Steps:
1. Open the page.
2. Select 5 stars, enter review "Love it", Name "Tom", Email "tom@example.com", click Submit.
3. Click "Moderator: approve pending reviews".
4. Look at the newest review at the top of the Reviews list.

Expected: the review is shown with the reviewer name "Tom"; the email is never published
("Your email address will not be published").
Actual: the review is shown with "tom@example.com" as the author. (The seeded reviews show
names correctly.)

### BUG-03 - Rating summary counts pending reviews (Major)

Location: Product rating summary under the product title (average rating and count).

Steps:
1. Open the page. Note the summary "4.0 out of 5 - based on 3 reviews" and "Reviews (3)".
2. Select 5 stars, enter review "Nice", Name "Tom", Email "tom@example.com", click Submit.
3. Do not approve. Look at the summary and the Reviews heading.

Expected: a pending review is not counted; the summary stays "4.0 out of 5 - based on 3
reviews", consistent with "Reviews (3)".
Actual: the summary shows "3.0 out of 5 - based on 4 reviews" (and 3 filled stars) while
the list still shows "Reviews (3)". The average is wrong because the approved ratings
(12) are divided by all reviews including the pending one (4). After approving, the
summary becomes correct ("4.3 out of 5 - based on 4 reviews").

### BUG-04 - A review of exactly 500 characters is rejected (Minor)

Location: Add a review form - Your review text box (length limit).

Steps:
1. Open the page.
2. Select 4 stars, enter Name "Tom", Email "tom@example.com".
3. Paste a review of exactly 500 non-space characters into "Your review". The counter
   shows "500 / 500" and the field accepts no more characters.
4. Click Submit.

Expected: the review is accepted, since the stated limit is 500 characters.
Actual: the error "Your review must be 500 characters or fewer." is shown. A review of
499 characters is accepted.

### BUG-05 - Spelling error in the success message (Trivial)

Location: Add a review form - confirmation message after Submit.

Steps:
1. Open the page.
2. Select 3 stars, enter review "OK", Name "Tom", Email "tom@example.com", click Submit.

Expected: "Thank you! Your review has been submitted and is awaiting approval."
Actual: "Thank you! Your review has been submited and is awaiting approval."
