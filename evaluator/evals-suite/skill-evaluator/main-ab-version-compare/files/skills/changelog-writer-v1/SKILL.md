---
name: changelog-writer
description: Turn a git log into a CHANGELOG section grouped by type (feat, fix, chore, docs).
---

# changelog-writer (v1)

1. Read the commit list.
2. Group commits by conventional-commit type: Features, Fixes, Chores, Docs.
3. Write one bullet per commit, imperative mood, no hashes.
4. Output a markdown section headed `## [Unreleased]`.
