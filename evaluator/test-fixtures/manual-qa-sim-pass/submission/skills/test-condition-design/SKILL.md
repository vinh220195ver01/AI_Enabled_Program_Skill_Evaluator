---
name: test-condition-design
description: Use when a reviewed Test Requirement Excel list already exists and test conditions must be derived from it with a named test design technique (equivalence partitioning, boundary value analysis, decision table, state transition, error guessing) before test cases are written; writes test-design.md. Do NOT use on a raw user story, to write step-by-step test cases or to produce test data sets.
---

# Test Condition Design

Turns each Test Requirement (TR) into test conditions, each derived with a named technique, so that test cases can be written from them.

## Inputs

- {tr_file}: the reviewed Test Requirement list (.xlsx written by the test-requirements-analysis skill). Default: `{output_dir}/test-requirements.xlsx`. If it is missing, ask the user; do not rebuild it from the user story.
- {answers}: answers to the clarification questions received so far, if any (file or pasted text). If the user has none, continue and keep the related notes as Missing info or Assumption.
- {knowledge_dir}: the project's knowledge folder (fields, limits, states, glossary). If missing, ask the user.
- {output_dir}: the folder where the output file is written. If missing, ask the user.

## Process

1. Open {tr_file} and list every TR ID with its AC ID and Notes. Stop and ask the user if a TR row has no TR ID or no text.
2. Read {answers} and the knowledge files that the index in {knowledge_dir} lists for test design, and write down each input field, value range, state and business rule you will use, marked Confirmed (with source) or Assumption.
3. Select one or more techniques for each TR with `references/test-design-techniques.md`, and note why the technique fits.
4. Derive the test conditions for each TR with the selected technique: partitions, boundary values, decision table rules, state transitions or error guesses. Give each condition an ID `TCD-<TR number>-<nn>` (for example TCD-03-02) and mark it Positive or Negative.
5. Check the scenario types in `references/coverage-checklist.md` and add missing conditions, or list the type under "Not covered" with a reason.
6. Tag notes on each condition with the tags in `../test-requirements-analysis/references/note-tags.md`; every condition built on an unconfirmed value gets an Assumption or Missing info note.
7. Write `{output_dir}/test-design.md` from `assets/test-design-template.md`.
8. Verify that every TR ID has at least one condition, that every boundary value is exact (on, just below, just above), and that no condition repeats another.
9. Report to the user: conditions per TR, the techniques used, the Assumption list and the "Not covered" list; then stop and wait for the user's approval before test cases are written.

## Exceptions

- A value range or rule needed for BVA or a decision table is not in any source: do not invent it; write the condition with a Missing info note, or with an Assumption note if the user agrees to proceed.
- {answers} contradicts {tr_file} or the knowledge files: list the conflict in the report and ask which source is authoritative; do not pick one.
- The xlsx cannot be read: show the error and ask the user for a re-saved copy or a CSV export; do not retype it from memory.

## Output

- `{output_dir}/test-design.md`: per TR, the technique(s), the test conditions with IDs, Positive/Negative, notes; plus the "Not covered" list and the assumption list.

## Files

- `references/test-design-techniques.md`: open at Steps 3 and 4.
- `references/coverage-checklist.md`: open at Step 5.
- `../test-requirements-analysis/references/note-tags.md`: open at Step 6 (shared, single source).
- `assets/test-design-template.md`: open at Step 7; copy it, never rebuild it.
