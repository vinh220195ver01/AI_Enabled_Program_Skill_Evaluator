---
name: your-skill-name
description: Use when ACTIVITY on INPUT, before or after NEXT STEP; produces OUTPUT. Do NOT use for OUT-OF-SCOPE CASE.
---

# Skill Title

## Inputs

- {task_input}: the task specification for this run (e.g. user story and acceptance criteria), as attached files or pasted text. If missing, ask the user; do not guess.
- {knowledge_dir}: the project's knowledge folder (business rules, glossary, screens, environments). If missing, ask the user.
- {project_name}, {app_url}, test accounts: provided by the user at run time. Never write real values in this skill.

## Process

1. Read {task_input} and the files in {knowledge_dir} that this task needs, and list {the items to work on}.
2. Identify {what to analyse} (rules in `references/{rules-file}.md`).
3. Write {the output content}.
4. Check {the output} against {task_input} and the rules.
5. Export by copying `assets/{template-file}`, keeping its structure.

## Output

- {deliverable}: {format}.

## Files

- `references/{rules-file}.md`: open at Step 2.
- `assets/{template-file}`: open at Step 5; copy it, never rebuild it.

<!--
How to use this template (see skill-standard.md):
1. Copy this file to <your-skill-name>/SKILL.md. The file name must be exactly SKILL.md (A1).
2. Replace your-skill-name with the folder name, exactly (A2).
3. Replace the UPPERCASE words in description; keep "Use when", the activity and the input (A3). No < or > in description (A2).
4. Replace every {placeholder} in the body. Keep at least 3 numbered steps, each starting with a verb (A3).
5. Keep only general QA knowledge in references/. The task specification and the project's domain knowledge stay outside the skill folder and come in through Inputs (A4, section 4.1).
6. Delete the Inputs / Output / Files sections only if they do not apply; delete this comment.
-->
