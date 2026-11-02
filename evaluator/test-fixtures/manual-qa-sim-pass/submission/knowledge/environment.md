# Test environment: My Shop demo build

Source: `exam/app-note.md`
Last updated: 2026-10-21

## Environment (Fact)

| Item | Value |
|---|---|
| Build | demo-1.0 |
| Browser | Chrome |

Only these two items are given. Browser version, operating system and screen size are not provided: write "Not provided" in reports; do not guess.

## How to open the application (Fact)

1. Open `exam/app/index.html` in Chrome (double-click it or drag it into a Chrome window).
2. No installation, server or internet connection is needed.
3. Reload the page to start again from the initial data. Only the "Save my name, email..." choice is kept between reloads.

## Test helper (Fact)

- New reviews wait for moderator approval. The button "Moderator: approve pending reviews" at the bottom of the page approves every waiting review, so the tester can play the moderator.
- This helper is part of the demo build only. Assumption: it is not part of the feature under test; it is used only to move reviews to "approved".

## Test accounts and data

- No accounts are needed (no sign-in in the demo build, Observed).
- Use synthetic data only (reserved email domains such as example.com).
