---
name: changelog-writer
description: Turn a git log into a CHANGELOG section grouped by type (feat, fix, chore, docs).
---

# changelog-writer (v2)

1. Read the commit list.
2. Group commits by conventional-commit type: Features, Fixes, Chores, Docs.
3. Write one bullet per commit, imperative mood, no hashes.
4. Output a markdown section headed `## [Unreleased]`.

## Breaking changes (new in v2)

5. Scan every commit body for `BREAKING CHANGE:`. Put each one under `### Breaking changes` as the FIRST subsection,
   with the migration note copied from the body. Never omit a breaking change, even when the commit type is chore.
6. After writing, count breaking commits in the input and in the output; they must match.
