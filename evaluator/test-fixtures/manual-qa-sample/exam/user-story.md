# Exam: Login for Acme Notes (sample)

**User story:** As a registered user, I want to log in with my email and password so that I can access my notes.

## Acceptance criteria

- **AC1:** Given valid credentials, when the user submits the login form, then the user is redirected to `/notes`.
- **AC2:** Given invalid credentials, when the user submits the form, then an error message is shown and the user stays on the login page.
- **AC3:** The email field is required. When it is empty, the message "Email is required" is shown under the field.
- **AC4:** After 5 consecutive failed login attempts, the account is locked for 15 minutes.

## Environment information provided by the exam

- Build: v1.4.2
- Browser: Chrome 126
- (No operating system is given.)

## Material for defect analysis

The application under test is available to the trainee. Screenshots and a console log of the failures are uploaded to the chat during the exam.
