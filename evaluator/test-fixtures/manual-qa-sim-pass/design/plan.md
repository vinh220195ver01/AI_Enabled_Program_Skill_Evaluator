# Plan: AI-enabled manual QA for US-VP02 "Submit a Product Review"

Author: trainee-sim-01 · Date: 2026-10-21 · Rules: `design/resolved-criteria.json` (profile manual-qa 0.11-draft), `_shared/skill-standard.md` v1.2

All paths below are relative to the fixture folder; `sub/` means `submission/`.

Planned layout:

```
sub/
├── skills/                  5 skills, generic (no project data)
├── knowledge/               project knowledge for My Shop / US-VP02 (outside the skills)
├── runs/run-1/, runs/run-2/ outputs of each skill run, one folder per run ({output_dir})
└── review/                  my human review log per step (what I checked, source, fix, re-check)
```

## 1. Evidence map

| Criterion | Condition (short) | Artefact that shows it | Planned path |
|---|---|---|---|
| A1 | Folder name kebab-case, max 64 chars | 5 skill folders | `sub/skills/*/` |
| A1 | Exactly one `SKILL.md` at each skill root | `SKILL.md` per skill | `sub/skills/*/SKILL.md` |
| A2 | `---` on line 1, closing `---`, YAML parses | Frontmatter of each SKILL.md | `sub/skills/*/SKILL.md` |
| A2 | `name` identical to folder | Frontmatter `name` | `sub/skills/*/SKILL.md` |
| A2 | Description non-empty, max 1024 chars, no `<` `>` | Frontmatter `description` | `sub/skills/*/SKILL.md` |
| A3 | Trigger clause "Use when..." | Frontmatter `description` | `sub/skills/*/SKILL.md` |
| A3 | Concrete activity + input | Frontmatter `description` | `sub/skills/*/SKILL.md` |
| A3 | No overlap between skill descriptions | Distinct input/task per skill + "Do NOT use" boundary | `sub/skills/*/SKILL.md`, section 3 below |
| A3 | Heading Process | `## Process` | `sub/skills/*/SKILL.md` |
| A3 | Steps numbered from 1, continuous, at least 3 | Numbered list under `## Process` | `sub/skills/*/SKILL.md` |
| A3 | Each step starts with an action verb | Numbered list under `## Process` | `sub/skills/*/SKILL.md` |
| A4 | No project-specific data in skill folders | All files in skill folders (checked by grep in Step 4) | `sub/skills/**` |
| A4 | Project info through input placeholders / "if missing, ask the user" | `## Inputs` with `{placeholders}` | `sub/skills/*/SKILL.md` |
| A4 | Single source for each content | Templates only in `assets/`, rules only in one `references/` file; shared files referenced by relative path | `sub/skills/*/assets/`, `sub/skills/*/references/` |
| B1 | One concrete QA task with goal, input, output | Workflow map (section 2) | `design/plan.md` |
| B1 | Subtasks cover input to output (analysis, design, review) | 5 skills + review steps | `design/plan.md`, `sub/skills/` |
| B1 | Each subtask one purpose, one checkable output | Output section of each skill | `sub/skills/*/SKILL.md` |
| B1 | Dependency order | Run order (section 3) | `design/plan.md` |
| B1 | Sized for AI (not crammed, not trivial) | One skill per competency task | `sub/skills/` |
| B1 | Human confirmation points marked | Control points in workflow map; "stop and wait" steps in skills | `design/plan.md`, `sub/skills/*/SKILL.md` |
| B2 | Right context for the task | Knowledge files + skill inputs | `sub/knowledge/`, `sub/skills/*/SKILL.md` |
| B2 | Instructions / project knowledge / run input separated | skills vs knowledge vs exam input | `sub/skills/`, `sub/knowledge/`, `exam/` |
| B2 | Structured, findable context | `knowledge/index.md` says which file to read for which skill | `sub/knowledge/index.md` |
| B2 | Fact vs assumption | "Assumption" / "Open question" labels in knowledge; Notes tags in TR list | `sub/knowledge/*.md`, `sub/runs/*/test-requirements.xlsx` |
| B2 | Source reliability (authoritative source named) | Source priority section | `sub/knowledge/index.md` |
| B2 | Context maintained (version/date, single source) | "Source:" and "Last updated:" lines; one fact in one file | `sub/knowledge/*.md` |
| B2 | Sensitive data protected | Synthetic-data rule in test data skill; no real accounts | `sub/skills/test-data-generation/references/test-data-rules.md` |
| B3 | Right skill for the situation | Run log naming skill + input per run | `sub/runs/run-1/run-log.md` |
| B3 | Required input provided, follow-ups answered | Run log | `sub/runs/run-*/run-log.md` |
| B3 | Mandatory steps and checkpoints followed | Run log + self-check output of each skill | `sub/runs/run-*/` |
| B3 | Output checked vs skill standard, rerun on deviation | Review log | `sub/review/review-log.md` |
| B3 | Similar runs consistent | Two runs with same input | `sub/runs/run-1/`, `sub/runs/run-2/` |
| B3 | How to run is recorded | Run order + how to launch (section 3) | `design/plan.md` |
| B4 | Detects exceptions from concrete signals | Stop rules in each skill; run log entries | `sub/skills/*/SKILL.md`, `sub/runs/*/run-log.md` |
| B4 | Responds per type (missing, conflict, bad output, failed step, unverifiable) | "Exceptions" section in each SKILL.md; review log | `sub/skills/*/SKILL.md`, `sub/review/review-log.md` |
| B4 | Controlled recovery (rerun from right point, re-check) | Review log | `sub/review/review-log.md` |
| B4 | Escalation criteria | Section 2 "Stop and escalate" | `design/plan.md` |
| B5 | QA steps mapped, AI use explained | Workflow map | `design/plan.md` |
| B5 | AI on at least 2 linked steps | 5 linked skills (output of one = input of next) | `sub/runs/run-1/` |
| B5 | Output passes without manual copying | Each skill reads the previous file from {output_dir} | `sub/skills/*/SKILL.md` |
| B5 | Control points at high-risk steps | CP1-CP5 in workflow map | `design/plan.md` |
| B5 | Humans in the right places | Human decision column | `design/plan.md` |
| B5 | Steps that should not use AI, with reason | Workflow map row "Execute tests" and "Send questions" | `design/plan.md` |
| B6 | Simple to launch | One-line launch per skill | `design/plan.md` section 3 |
| B6 | Context not re-provided each run | {knowledge_dir} read by the skill | `sub/knowledge/`, `sub/skills/*/SKILL.md` |
| B6 | Input not asked twice; output flows | {output_dir} shared by all skills | `sub/skills/*/SKILL.md` |
| B6 | Few manual actions | Skills write files directly, templates copied by the skill | `sub/runs/run-1/` |
| B6 | Human only at control points | Run log | `sub/runs/run-1/run-log.md` |
| B6 | New tester can run it first time | Inputs/Process/Output/Files in each SKILL.md + section 3 | `sub/skills/*/SKILL.md` |
| B6 | Effort lower than baseline | Effort estimate | `sub/review/effort-estimate.md` |
| C1 | Finds at least 70% of ambiguous points | Clarification questions | `sub/runs/run-1/clarification-questions.md` |
| C1 | Mandatory points in "Must ask" | Clarification questions | `sub/runs/run-1/clarification-questions.md` |
| C1 | Both groups present | Clarification questions | `sub/runs/run-1/clarification-questions.md` |
| C2 | Every AC covered | TR list (AC ID column), test cases (TR ID column) | `sub/runs/run-1/test-requirements.xlsx`, `test-cases.xlsx` |
| C2 | All mandatory template components | Test case template columns | `sub/runs/run-1/test-cases.xlsx` |
| C2 | All relevant scenario types | Test design technique per condition | `sub/runs/run-1/test-design.md` |
| C2 | No important risk missed | TR Notes tagged Risk | `sub/runs/run-1/test-requirements.xlsx` |
| C2 | Gaps raised as questions/assumptions | Clarification questions + Notes tags | `sub/runs/run-1/` |
| C2 | Excluded parts stated with reason | "Out of scope" section | `sub/runs/run-1/test-design.md` |
| C2 | No serious omissions | Coverage check step in each skill | `sub/runs/run-1/` |
| C3 | Matches template (columns, order, IDs) | xlsx outputs copied from `assets/` | `sub/runs/run-1/*.xlsx` |
| C3 | Consistent formatting and terms | Glossary used by all skills | `sub/knowledge/glossary.md` |
| C3 | Concrete steps, verifiable expected results | Test cases | `sub/runs/run-1/test-cases.xlsx` |
| C3 | Recipient understands without asking back | Bug list + questions | `sub/runs/run-1/bug-list.xlsx` |
| C3 | Each item one purpose | Test cases / bugs | `sub/runs/run-1/` |
| C3 | Usable immediately, no AI traces | Final outputs | `sub/runs/run-1/` |
| C3 | Organised (grouped, summary) | Grouping by AC / severity | `sub/runs/run-1/` |
| C3 | Tone suits recipient | Clarification questions, bug list | `sub/runs/run-1/` |
| C4 | Checks against trusted sources | Review log (source column) | `sub/review/review-log.md` |
| C4 | Systematic, high-risk first | Review log order | `sub/review/review-log.md` |
| C4 | Finds real problems | Review log findings | `sub/review/review-log.md` |
| C4 | Each finding handled with reason | Review log action column | `sub/review/review-log.md` |
| C4 | No guessing when source insufficient | Findings turned into questions/assumptions | `sub/review/review-log.md` |
| C4 | Fix and re-check | Review log re-check column | `sub/review/review-log.md` |
| C4 | Correct AI content not changed | Original AI output kept beside final | `sub/runs/run-1/ai-original/` |
| C4 | Unverified items marked | "Unverified" label in outputs | `sub/runs/run-1/` |
| C4 | Record kept | Review log | `sub/review/review-log.md` |
| SAFE | Gate conditions not defined yet; I plan to show: approved tool only, no real personal data (synthetic data only), human validates before use | Test data rules, knowledge file environment, review log | `sub/skills/test-data-generation/references/test-data-rules.md`, `sub/review/review-log.md` |

## 2. Workflow map

Task: from user story US-VP02 to a reviewed bug list. Goal: find what is unclear, test the feature with traceable cases, report defects clearly. Input: user story + AC + mockups + demo app. Output: clarification questions, TR list, test design, test cases, test data, bug list with analysis.

| # | QA step | AI? | Why | Output | Control point / human decision |
|---|---|---|---|---|---|
| 1 | Analyse requirements | Yes, skill `test-requirements-analysis` | AI is fast at listing gaps and edge cases in a short story; I review | `clarification-questions.md`, `test-requirements.xlsx` | CP1 (high risk): I check every question and TR against the story; I decide Must ask vs Nice to confirm |
| 2 | Send questions to PO / customer, record answers | No | Communication with the customer is a human job; AI must not send anything | Answers added to the knowledge files | Human only |
| 3 | Design test conditions | Yes, skill `test-condition-design` | Applying EP/BVA/decision table/state transition systematically is repeatable | `test-design.md` | CP2: I check boundaries and the technique choice; I approve before test cases |
| 4 | Write test cases | Yes, skill `test-case-generation` | Turning conditions into steps is mechanical; AI keeps the format | `test-cases.xlsx` | CP3 (high risk): I confirm every Expected Result against the story/knowledge; AI never finalises expected results |
| 5 | Prepare test data | Yes, skill `test-data-generation` | AI generates boundary and invalid values quickly; synthetic only | `test-data.xlsx` | CP4: I check boundary values and that no real personal data is used |
| 6 | Execute tests in the app, capture evidence | No | Observing real behaviour must be done by the tester; AI cannot be the source of actual results | Screenshots, console logs, results in the TC file | Human only |
| 7 | Analyse failures and write the bug list | Yes, skill `defect-analysis-reporting` | AI helps structure evidence, separate facts from guesses, and write clear reports | `defect-analysis.md`, `bug-list.xlsx` | CP5 (high risk): I confirm severity/priority and each bug is reproducible before logging; I submit the bugs |

Linking: every skill reads the previous step's file from the same `{output_dir}`, so nothing is copied by hand.

Stop and escalate (to trainer / PO): the story is missing information that blocks expected results; two sources conflict (story vs demo build); a skill fails twice on the same step after a corrected input; an output cannot be verified from any source.

## 3. Skill list (run order)

Launch: "Use skill {name} with {inputs}; knowledge_dir = submission/knowledge; output_dir = submission/runs/run-N". Each skill asks for anything missing.

| Order | Folder | Competency | Input | Output files (in {output_dir}) |
|---|---|---|---|---|
| 1 | `test-requirements-analysis` | requirements-analysis | {user_story} (story + AC + mockups), {knowledge_dir} | `clarification-questions.md`, `test-requirements.xlsx` |
| 2 | `test-condition-design` | test-design | `test-requirements.xlsx` (reviewed), answers to questions if any | `test-design.md` |
| 3 | `test-case-generation` | test-case-generation | `test-requirements.xlsx` + `test-design.md` | `test-cases.xlsx` |
| 4 | `test-data-generation` | test-data-generation | `test-cases.xlsx` | `test-data.xlsx` |
| 5 | `defect-analysis-reporting` | defect-analysis-reporting | {failure_evidence} (screenshots, console logs, test results) + {environment} from the exam | `defect-analysis.md`, `bug-list.xlsx` |

Shared content (single source): note tags Assumption / Edge case / Missing info / Risk live in `test-requirements-analysis/references/note-tags.md`; skills 2-5 reference that file by relative path. Severity and priority scale lives only in `defect-analysis-reporting/references/severity-priority-guide.md`.
