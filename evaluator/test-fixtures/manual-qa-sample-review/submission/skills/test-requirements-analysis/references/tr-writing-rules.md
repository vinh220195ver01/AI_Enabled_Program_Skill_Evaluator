# TR writing rules

- One Test Requirement states one verifiable behaviour, not a test step.
- Every AC gets at least one TR. A TR that traces to no AC gets `N/A` in AC ID.
- IDs run continuously (e.g. TR_001, TR_002, ...) with no gaps.
- Every Notes cell starts with its origin: `Fact`, `Assumption`, `Missing info`, `Edge case (...)` or `Risk (...)`.
- `Missing info` rows say `Must ask` when test design is blocked without the answer, otherwise `Nice to confirm`.
- Anything the source does not state is never written as a confirmed requirement: tag it `Assumption` or `Missing info`.
- Mockup content may be used as a source; say so in Notes.
