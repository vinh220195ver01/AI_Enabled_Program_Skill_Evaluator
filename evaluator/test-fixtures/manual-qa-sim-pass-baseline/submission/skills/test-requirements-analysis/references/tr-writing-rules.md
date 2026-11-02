# Test Requirement writing rules

## IDs

- AC ID: `AC-01`, `AC-02`, ... in the order of the source.
- TR ID: `TR-01`, `TR-02`, ... numbered continuously across the whole list (not restarted per AC).
- Requirements implied by the story but not tied to one AC (for example access rules): use AC ID `AC-GEN`, and write a short origin in the Acceptance Criteria column, e.g. `General: form fields shown in the mockup`. No file paths. Notes keep the tags from `note-tags.md` only.

## One TR

- One TR = one testable behaviour, starting with "Verify that ..." (for example "Verify that the form cannot be submitted when a required field is empty").
- Write what must be true, not how to test it (no steps, no test data).
- Cover both sides where they exist: the accepted behaviour and the rejected behaviour.
- Do not add rules that no source states. If a TR needs one, keep the TR and tag the rule as Assumption in Notes.

## Columns

| Column | Content |
|---|---|
| AC ID | AC ID from Step 1 |
| Acceptance Criteria | The AC text, word for word (repeat it on every TR row of that AC) |
| TR ID | See IDs |
| Test Requirements | "Verify that ..." |
| Notes | Zero or more tagged notes, one per line, tags from `note-tags.md` |

## Self-check

- Every AC has at least one TR.
- No two TRs test the same behaviour.
- Each TR can later get a clear pass/fail result.
