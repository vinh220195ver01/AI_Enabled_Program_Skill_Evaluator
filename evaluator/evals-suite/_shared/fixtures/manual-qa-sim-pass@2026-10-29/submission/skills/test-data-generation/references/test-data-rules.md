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
