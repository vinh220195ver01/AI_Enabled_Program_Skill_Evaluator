# TC writing rules

- One test case verifies one behaviour; split a TR when it has several.
- Steps contain concrete test data (e.g. `qa.tester@example.com`, a 20-character string), never "enter valid data".
- An Expected Result states at least one observable outcome: message text, displayed value, destination screen, field or button state, data saved or not saved.
- Vague phrases are not allowed on their own: "works correctly", "as expected", "displayed correctly", "no error", "success", "OK".
- A BLOCKED test case keeps its TR ID, uses `TBD —` at the start of Expected Result and `BLOCKED —` at the start of Notes.
- Every TR ID of the TR file appears at least once in the TR ID column.
