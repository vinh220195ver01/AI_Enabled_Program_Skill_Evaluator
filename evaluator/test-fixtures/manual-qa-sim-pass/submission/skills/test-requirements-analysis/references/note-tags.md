# Note tags

Single source for the tags used in the Notes column of every QA output (TR list, test design, test cases, test data, bug list). Other skills link to this file; do not copy it.

Format: one note per line, `Tag: text`. A row can have several notes or none.

| Tag | Use when | Example |
|---|---|---|
| Assumption | We continue with a value or rule that no source states. Say what was assumed and which question would confirm it. | `Assumption: maximum length taken as N until Q-03 is answered.` |
| Edge case | The row covers a boundary, an unusual but valid input, or a rare sequence of actions. | `Edge case: value exactly at the maximum.` |
| Missing info | The source does not give enough to decide the expected behaviour. Link the question ID. | `Missing info: message text not specified (Q-05).` |
| Risk | Failure here would hurt users, data, privacy, security or the main flow. Say what could go wrong. | `Risk: personal data could be shown publicly.` |

Rules:

- An Assumption is never presented as fact elsewhere in the output.
- When a question is answered, replace the Assumption or Missing info note with the confirmed rule and its source.
