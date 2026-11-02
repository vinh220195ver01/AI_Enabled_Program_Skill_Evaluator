# Test design techniques: when and how

| Technique | Use when the TR has... | How to derive conditions |
|---|---|---|
| Equivalence Partitioning (EP) | An input or output with groups of values treated the same way (valid / invalid types, formats, options) | List the valid partitions and each invalid partition separately. One condition per partition. Invalid partitions are tested one at a time. |
| Boundary Value Analysis (BVA) | A numeric range, a length limit, a count limit, a date range | For each boundary: the value on it, just below and just above (3-value BVA). For a length limit N: N-1, N, N+1 characters; for a minimum M: M-1, M, M+1. Also empty (0) when the field is required. |
| Decision table | Several conditions that together decide the outcome (for example several required fields, or role + state) | List conditions and outcomes, build the rules, collapse rules that give the same outcome only when it is safe. One condition per remaining rule. |
| State transition | An object that changes state (created, pending, approved, rejected, deleted...) or a screen flow | Draw states and events; cover every valid transition once and the important invalid transitions (event not allowed in a state). |
| Error guessing | Inputs or actions where experience shows defects often appear | Leading/trailing spaces, only spaces, special and non-Latin characters, HTML or script text, very long text, double click on submit, browser back/reload after submit, pasted text, data remembered between visits, count or average shown after a change. |

Rules:

- Name the technique on every condition.
- Use the values from the sources. If the source gives no value, the condition still exists but carries a Missing info or Assumption note.
- Do not test two invalid partitions in one condition: the result would not show which one was rejected.
