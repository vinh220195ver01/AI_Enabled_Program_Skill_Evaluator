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
