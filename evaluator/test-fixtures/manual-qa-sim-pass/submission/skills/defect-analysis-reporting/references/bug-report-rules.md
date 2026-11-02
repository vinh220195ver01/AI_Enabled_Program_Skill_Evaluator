# Bug report writing rules

| Column | Rule |
|---|---|
| ID | BUG-01, BUG-02, ... continuous. |
| Summary | [Area] what is wrong + where/when, max about 15 words. No "not working". Example pattern: "[Form] valid value at the maximum length is rejected". |
| Description | 1-3 sentences: what happens, why it is wrong (cite the requirement or test case), and the impact. |
| Pre-Condition | State needed before step 1 (page open, data present, settings). |
| Steps to Reproduce | Numbered, one action per step, with the exact data used. Minimum steps that still reproduce. |
| Expected Result | From the requirement or the confirmed test case; name the source (for example "per AC-02 / TC-03-01"). If not confirmed, say "Not confirmed: ..." and tag Missing info. |
| Actual Result | Only what the evidence shows; quote messages exactly. |
| Evidence | Evidence IDs and file names (EV-01 screenshot-x.png). |
| Build | From the environment input only; else "Not provided". |
| Browser | From the environment input only; else "Not provided". |
| Severity | Critical / High / Medium / Low, per `severity-priority-guide.md`. |
| Priority | P1 / P2 / P3 / P4, per `severity-priority-guide.md`. |
| Status | New. |
| Notes | Related TC IDs, hypothesis reference, tagged notes. |

Rules:

- One problem per bug. Two symptoms with the same cause can share a bug only if fixing one fixes the other; say so in Notes.
- Neutral, factual tone; no blame, no guesses in Actual Result.
- Never add personal data from the evidence that is not needed to reproduce; mask it if present.
