# Scenario coverage checklist

For each type, either the design has at least one condition, or the type is listed under "Not covered" with a reason (not relevant, out of scope of the story, blocked by missing information, needs another environment).

| Type | Ask yourself |
|---|---|
| Positive | Is the main successful flow covered for every AC? |
| Negative | Is each way the action can be rejected covered? |
| Boundary | Is every limit (length, count, range) covered on, below and above? |
| Validation | Is every required field and format rule checked, with the message? |
| Error handling | What happens on failure (network, server, timeout, reload during action)? |
| Permissions | Who may and may not perform the action (signed out, other role, precondition not met)? |
| Integration | Does the result appear correctly in other places (lists, counts, summaries, other pages)? |
| UI | Labels, required markers, layout against the mockup, focus and keyboard use. |
| Compatibility | Which browsers and screen sizes are in scope? |
| Regression | Which existing behaviour on the same page must still work after the change? |
| Data and privacy | Is personal data stored, shown or hidden as expected? |

Priority of risk: data loss or exposure, security, main flow, payment or money values come first.
