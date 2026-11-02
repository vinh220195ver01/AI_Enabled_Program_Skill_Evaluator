# Severity and priority guide

Single source for severity and priority in all QA outputs. Severity = impact on the user or the system. Priority = how soon it should be fixed. Always give one reason for each.

## Severity

| Severity | Meaning | Typical signs |
|---|---|---|
| Critical | The main flow is blocked with no workaround, data is lost or corrupted, or security/privacy is broken. | Cannot complete the core action at all; personal data exposed; crash. |
| High | A main function gives a wrong result or a required rule is not enforced; a workaround may exist but is not reasonable for users. | Wrong values saved or displayed; valid input rejected; invalid input accepted for a required rule. |
| Medium | A secondary function is wrong, or the main function is wrong only in a less common case; a reasonable workaround exists. | Wrong count or summary in an edge case; wrong behaviour at one boundary. |
| Low | Cosmetic or wording problem with no functional impact. | Typo, alignment, label text differs from the mockup. |

## Priority

| Priority | Meaning |
|---|---|
| P1 - Urgent | Fix before the release can continue; blocks testing or users. |
| P2 - High | Fix in the current iteration. |
| P3 - Medium | Fix when capacity allows, before release if possible. |
| P4 - Low | Can wait for a later release. |

## Rules

- Severity does not decide priority alone: a Low-severity typo on a highly visible page can be P2; a High-severity problem in a rarely used path can be P3. Explain the choice.
- Privacy or security exposure of personal data is at least High severity.
- The final severity and priority are confirmed by a person; the AI proposal is a draft.
