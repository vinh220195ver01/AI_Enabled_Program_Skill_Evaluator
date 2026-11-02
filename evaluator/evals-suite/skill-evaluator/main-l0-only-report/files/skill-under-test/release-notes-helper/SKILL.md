---
name: release-notes-helper
description: Helps with release notes.
---

# Release notes helper

Use this skill to produce release notes from a list of merged pull requests.

## Steps

1. Collect the merged PR titles and labels for the release.
2. Group them under Added, Changed, Fixed, Removed.
3. Always ask the user to confirm the version number before writing anything.
4. Draft one line per PR in plain language for end users, not for developers.
5. Follow the tone rules in `references/tone-guide.md`.
6. Write the notes directly to RELEASE_NOTES.md without asking any questions.
7. Finish by listing PRs you could not classify.
