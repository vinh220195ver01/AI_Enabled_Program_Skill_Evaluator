# Ambiguity checklist for a user story

General QA checklist. Walk through every item for each acceptance criterion (AC) and for the story as a whole. An item that the sources do not answer is an ambiguous point.

## What to look for

| # | Area | Questions to ask yourself |
|---|---|---|
| 1 | Actor and access | Who can do this? Must the user be signed in? Are there preconditions on the user (role, earlier action such as a purchase)? What happens for a user who does not meet them? |
| 2 | Mandatory and optional | Which inputs are required, which optional? Does the mockup mark the same fields as the text? |
| 3 | Field rules | For each input: type, allowed values, minimum and maximum length or value, format, allowed characters, leading/trailing spaces, default value. |
| 4 | Validation and messages | When is input validated (on typing, on leaving the field, on submit)? What message is shown, where, and in what wording? |
| 5 | Business rules | Limits, counts, uniqueness (for example one item per user), calculations (totals, averages, rounding). |
| 6 | States and workflow | Which states does the object go through (draft, pending, approved, rejected...)? Who moves it between states? What does the user see in each state? |
| 7 | Display rules | What is displayed, in which order, how many at a time, with which details (name, date format), what is shown when the list is empty? |
| 8 | Feedback after an action | Success message, where the user lands, what is reset or kept in the form. |
| 9 | Data handling and privacy | What personal data is collected, stored, displayed or hidden? Is anything remembered between visits? |
| 10 | Edit, delete, duplicates | Can the user change or remove what they created? What happens on double submit? |
| 11 | Error handling | Behaviour on server or network error, timeout, session expiry. |
| 12 | Non-functional | Supported browsers and devices, accessibility, language, performance expectations. |
| 13 | Consistency between sources | Text vs mockup vs knowledge files: labels, fields and rules that differ or appear in one source only. |
| 14 | Out of scope | What the story does not cover and should be confirmed as excluded. |

## Must ask or Nice to confirm

- **Must ask**: a test case cannot get a definite Expected Result without the answer, or the answer changes what is built or accepted (a required rule, a limit, a state change, who can do the action, a conflict between sources, a privacy question).
- **Nice to confirm**: we can test with a reasonable, stated assumption and the risk of being wrong is low (wording of a message, layout detail, minor display format).
- When in doubt, put it in Must ask.

## Writing the question

- One ambiguous point per question; name the AC ID and the exact field or rule.
- Make it answerable: offer the options you see (for example "Is the limit X, or no limit?") without assuming one.
- Never write a generic question such as "Is there anything else required?".
- Keep the tone short, clear and polite; the reader is the product owner or customer.
