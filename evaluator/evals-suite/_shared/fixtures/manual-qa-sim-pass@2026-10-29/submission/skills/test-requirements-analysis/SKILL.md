---
name: test-requirements-analysis
description: Use when reviewing a user story and its acceptance criteria (plus mockups, if any) before any test design starts, to find ambiguous points, raise clarification questions grouped as Must ask and Nice to confirm, and build the Test Requirement list; writes clarification-questions.md and test-requirements.xlsx. Do NOT use to choose test techniques, write test cases or report defects.
---

# Test Requirements Analysis

Turns one user story into (1) clarification questions for the product owner and (2) a traceable Test Requirement (TR) list. It does not design tests.

## Inputs

- {user_story}: the user story, its acceptance criteria and any mockups for this run, as attached files or pasted text. If missing, ask the user; do not guess.
- {knowledge_dir}: the project's knowledge folder (business rules, glossary, screens, environment). If missing, ask the user. If the user says there is none, continue and tag every rule you rely on as Assumption.
- {output_dir}: the folder where the output files are written. If missing, ask the user.
- Answers already received from the product owner, if any: given by the user. Never invent answers.

## Process

1. Read {user_story} and list every acceptance criterion in the given order with an AC ID (AC-01, AC-02, ...). Write the AC text word for word; do not rephrase it.
2. Read the index file in {knowledge_dir} and open only the files it lists for requirements analysis. Note each statement you use as Fact (stated in a source), Assumption or Open question, with its source file.
3. Identify the ambiguous points of each AC and of the story as a whole by walking through `references/ambiguity-checklist.md` item by item.
4. Classify each ambiguous point as Must ask or Nice to confirm with the rule in `references/ambiguity-checklist.md` (section "Must ask or Nice to confirm"), and write one specific question per point.
5. Write `{output_dir}/clarification-questions.md` from `assets/clarification-questions-template.md`, keeping both groups even if one is empty.
6. Derive the Test Requirements for each AC with `references/tr-writing-rules.md`, and tag each Notes entry with the tags in `references/note-tags.md`.
7. Check coverage: every AC ID has at least one TR; every Must ask question is linked to at least one TR through a "Missing info" note; no TR states a rule that is not in a source unless it is tagged Assumption.
8. Export the TR list by copying `assets/test-requirement-template.xlsx` to `{output_dir}/test-requirements.xlsx` and filling it, keeping the sheet name, header row and column widths.
9. Report to the user: the number of ACs, TRs and questions, the Must ask list, and every Assumption; then stop and wait for the user's review before any test design.

## Exceptions

- Input missing or unreadable (empty story, no AC, image cannot be opened): stop and ask the user for it; do not continue on a guess.
- Sources conflict (for example the story says one thing and a mockup or knowledge file another): write the conflict as a Must ask question quoting both sources; do not choose one.
- The template cannot be copied or the file cannot be written: show the error, retry once with a corrected path, then stop and ask the user.

## Output

- `{output_dir}/clarification-questions.md`: questions grouped as Must ask and Nice to confirm, each linked to an AC ID.
- `{output_dir}/test-requirements.xlsx`: one row per TR, in the layout of `assets/test-requirement-template.xlsx`.

## Files

- `references/ambiguity-checklist.md`: open at Steps 3 and 4.
- `references/tr-writing-rules.md`: open at Step 6.
- `references/note-tags.md`: open at Step 6. Other skills also use this file; edit it only here.
- `assets/clarification-questions-template.md`: open at Step 5; copy it, never rebuild it.
- `assets/test-requirement-template.xlsx`: open at Step 8; copy it, never rebuild it.
