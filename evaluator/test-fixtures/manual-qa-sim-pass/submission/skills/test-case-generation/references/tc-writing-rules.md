# Test case writing rules

## IDs

- TC ID: `TC-<TR number>-<nn>`, for example TC-03-01, TC-03-02 for TR-03. Numbers continuous per TR.
- Put the condition ID (TCD-xx-yy) in Notes as `Condition: TCD-xx-yy`.

## Columns

| Column | Rule |
|---|---|
| TR ID | Exactly as in the TR list. |
| TC ID | See IDs. |
| TC Summary | "Verify that ..." + one behaviour + the key condition, max about 15 words. |
| Pre-Condition | The state before step 1: page open, data that must already exist, settings. No actions that belong in the steps. |
| Steps | Numbered `1.` `2.` ... one action per step, naming the control by its exact label. Name the data by Data ID or concrete value (for example "Enter a 3-character value in Name"). |
| Expected Result | What the tester can see or check: the exact message, the element that appears or disappears, the value shown, the state of the record. One outcome per case (it may have several observable parts of that one outcome). |
| Notes | Condition ID, technique, and tagged notes (Assumption, Edge case, Missing info, Risk). |

## Do not write

- Vague results: "works normally", "works as expected", "error is shown", "system handles it correctly".
- Several behaviours in one case (for example valid submit and invalid submit together).
- Expected results copied from what the build currently does; the source is the requirement.

## Self-check per case

1. Can another tester run it without asking anything?
2. Is the expected result pass/fail on its own?
3. Does it trace to one TR and one condition?
4. Are unconfirmed expectations marked "To be confirmed" with a Missing info note?
