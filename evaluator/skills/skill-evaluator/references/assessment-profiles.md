# Assessment Profiles

A profile is the seam for evaluating many trainees against **one fixed definition of "good"**. The course owner supplies two data files; the framework does the rest. Nothing in `SKILL.md`'s workflow changes per assessment, and no judge prompt has to be edited when criteria change.

**Status:** both profiles have criteria only and neither can be run yet. `manual-qa` v0.11 replaced the whole v0.3 profile with the weighted structure from the `Intermediate_Manual` sheet (see "manual-qa profile v0.11" below). The judge, the scripts and the sections from "The two files" through "Scoring model" still describe the v0.3 points model, which no longer matches any profile. `build_plan_from_profile.py` rejects a profile whose `scoring_model` is not `deduction`. `auto-qa` v0.17 likewise replaced v0.1 with the sheet `Intermediate_auto` (see "auto-qa profile v0.17" at the end). Group A is shared by both profiles (see "Shared criteria"). A new area is a new folder under `profiles/` with the same two files, plus a judge agent if the existing one doesn't fit.

## Shared criteria and course rules

Anything several profiles use is kept once under `profiles/_shared/`, so a change is made in one place. There are two kinds of shared file.

**Criteria fragments.** A fragment holds one group and its criteria (`fragment`, `version`, `group`, `criteria[]`). A profile pulls it in with a `$ref` entry in `groups`, by path relative to the profile folder:

```
"groups": [{"$ref": "../_shared/skill-standard.json"}, {"id": "B", ...}, {"id": "C", ...}]
```

| Fragment | Group | Used by |
|---|---|---|
| `_shared/skill-standard.json` | A Skill Standard (A1-A4, weight 0.2), from `Intermediate_Manual` | `manual-qa`, `auto-qa` |

Group A's `standard` points to `_shared/skill-standard.md` (the skill standard, template and naming convention that A1-A4 refer to, written for trainees, each rule tagged with the criterion that grades it) and `_shared/SKILL.template.md` (a SKILL.md to copy). The template is not named `SKILL.md`, so it is never taken for a skill. When a rule changes, edit `skill-standard.json` and `skill-standard.md` together and bump both versions; the JSON is what is graded.

**Course settings.** `_shared/course-rules.json` (`shared`, `version`, `settings{}`) holds course-wide settings: the default `pass_rule`, `scoring` and the `competency_catalog`. A profile pulls it in with a top-level `"extends": ["../_shared/course-rules.json"]`; each setting becomes a top-level key of the resolved profile, and `settings_from` names the file it came from. Both profiles extend it.

Rules:
- Scripts never read `criteria.json` directly. They call `scripts/profile_loader.py` `load_profile()`, which returns the profile with every `$ref` replaced: the group gets `shared_from` and `shared_version`, and its criteria come first in group order.
- A profile cannot override shared content. The loader refuses a profile that defines a fragment's group id or criterion ids, or a key that an `extends` file already sets. To change group A or the course rules, edit the shared file and bump its `version`; both profiles change together.
- The pre-registered plan records `criteria_sha256` and `shared_sources[]` (path, sha256, version of each shared file), so an edit to a fragment after grading started is detectable like an edit to the profile.
- Check what a profile resolves to with `python scripts/profile_loader.py profiles/manual-qa profiles/auto-qa`, or write the resolved profile with `--out`.

## Pass rules

The judge never decides a criterion's verdict. It reports, per condition, met or not met with evidence. `scripts/criterion_rules.py` turns those results into a verdict and a score using the criterion's `pass_rule`. A change of rule is therefore a data change: no judge prompt changes, and saved condition results can be re-evaluated under the new rule without grading again.

| Mode | Verdict | Score |
|---|---|---|
| `{"mode": "proportional", "min_ratio": 0.8}` (current course rule) | every condition has equal weight; pass when met / total >= 80% (4 of 5, 5 of 6, 8 of 10 pass; 3 of 4, 4 of 6, 5 of 7 fail) | met / total, kept even when the verdict is fail |
| `{"mode": "all"}` | pass only when every condition is met | 1 or 0 |
| `{"mode": "at_least", "min_met": 5}` or `"min_ratio": 0.8` | pass when at least that many / that share of conditions are met | 1 or 0 |

Optional on any mode: `conditions` (`pass_when_all`, the default, or `should_items`), `requires_pass_of` (criterion ids that must pass first, else fail with score 0), `text` (the rule in words).

- Precedence: `criterion.pass_rule` > `group.pass_rule` > the profile's (from `course-rules.json`). Today only auto-qa B6 overrides: `at_least` 2 of its 3 `should_items`, `requires_pass_of` B3 and B5.
- Counted conditions: the criterion's `pass_when_all`, then `by_sub_category[<sub>].pass_when_all` when it has variants (the sub-category being assessed must be given). Results are matched by position in that order.
- To change the course-wide pass line, change `settings.pass_rule` in `_shared/course-rules.json`, e.g. to `{"mode": "all"}` (every condition must be met). To change one criterion or group only, give it its own `pass_rule`.
- The loader validates every rule (known mode, the right thresholds, existing `requires_pass_of` ids, a non-empty condition list). Show the effective rule of each criterion with `python scripts/criterion_rules.py profiles/manual-qa profiles/auto-qa`, or evaluate saved results with `--results r.json [--sub-category SCR]`.
- Human-graded conditions: a criterion may list `human_conditions` (positions in its `pass_when_all`). The judge does not grade them and reports `{"met": null, "pending": "human"}`; the grader fills them in. While one is open the verdict is `pending` (score null), unless it is already decided, e.g. under mode `all` (or `proportional` once the 80% line can no longer be reached) another unmet condition already makes it a fail. A criterion that `requires_pass_of` a pending one is pending too. Today only auto-qa C4 has one: explaining the submitted code.
- Pass rules decide a criterion's verdict and score only. How scores roll up is the course `scoring` setting (see "Scoring (course-wide)").

## Scoring (course-wide)

`settings.scoring` in `_shared/course-rules.json` applies to both profiles. Course decisions so far:

| Item | Value |
|---|---|
| `option` | 2 (Option 1 was rejected). `formula` keeps the sheet's Option 2 text: per competency, `Competency Score = Skill Standard*0.2 + AI Application*0.5 + QA Output Quality*0.3`; pass when no competency scores below the line and the safety gate passes |
| `group_score` | `mean`: a group's score is the mean of its criteria scores, equal weights (e.g. B = mean of B1-B6) |
| `per_competency` | every group is scored separately for each competency the profile covers: B and C from the work done for that competency, A from the skills that belong to it |
| `skill_to_competency` | the judge decides which competency each submitted skill belongs to, with a reason; the final report lists the mapping; the trainer reviews it |
| `competency_catalog` | the course's 7 competencies (all "AI-assisted"): `requirements-analysis`, `test-design`, `test-case-generation`, `test-data-generation`, `automation-development`, `test-maintenance`, `defect-analysis-reporting`. A profile lists the ones its exam covers in `competencies`; the loader refuses an id that is not in the catalog |
| group weights | on each group (`weight`): A 0.2, B 0.5, C 0.3 |
| `group_points` | 5: each group A, B, C is worth 5 points, shared equally by its criteria (5 / n each) |
| `criterion_score` | a criterion earns its share x (conditions met / total); each unmet condition deducts an equal slice |
| `pass_threshold` | 3 (of 5): Competency Score = A\*0.2 + B\*0.5 + C\*0.3 with A, B, C in points; pass when >= 3 for every competency and the gate passes. |

`criterion_rules.score_groups()` computes group points and the competency score from `evaluate_all()` results; `python scripts/criterion_rules.py <profile> --results r.json` prints them when every criterion has results.

Decided 2026-10-21: the pass line 3 of 5 with weights 0.2/0.5/0.3, "a criterion passes at 80% or more of its conditions met, fails below" (2026-10-23; before that "fail at 20% unmet", under which 4 of 5 failed), and a Fail criterion keeps its partial points. Still undecided: rounding, and M-11 (group A per skill). Until M-11 is answered the report scores group A per skill and averages each A criterion's score over the skills mapped to the competency (a competency with no skill gets A = 0).

### Plan and report for weighted-pass-fail

- `build_plan_from_profile.py <profile> --skill-name .. --hypothesis .. --out plan.json [--baseline b.json] [--sub-category X] [--competencies id1,id2]` (`--competencies`: weighted-pass-fail only; the exam covers just those competencies of the profile, the others are not assessed and not in the report; unknown ids are refused) writes the resolved criteria (with each one's effective rule and counted conditions), competencies, scoring and gates into the plan, with sha256 of `criteria.json` and shared files. It refuses a profile with missing `competencies`, weights not adding to 1, a pass line above `group_points`, or a criterion with variants and no `--sub-category`.
- `render_assessment_report.py --plan plan.json --result result.json [--human human.json] --out-dir report/` writes the scoring sheet (xlsx + md) and `assessment_report.json`. Result shape (the judge's output, T-01): `skills[{name, competency, reason}]`, `skill_results{skill: {A1: [cond..]}}`, `competency_results{competency: {B1: [cond..], .., C4: [..]}}`, `gate{verdict, note}`; `cond` is a bool or `{met, evidence}` (`met: null` = a person grades it). Human file: `conditions{"<competency>/<criterion>": {"<position>": bool}}` (A: `"<competency>/<skill>/A1"`), `gate`, `skill_to_competency` (trainer corrections), `mapping_reviewed`.
- Every unmet condition carries `locations` (rule 3a of the judge): Excel `{file, sheet, cell, quote}`, text `{file, line, quote}` (quote verbatim), missing `{file, absent, kind}` (`kind` "file": the file or folder is not there; "content": it exists but lacks the thing; the merge rejects a "file" claim about a file that exists, and an `absent` on an existing file without `kind`). `merge_judge_results.py --submission-dir` checks them against the real files; the report prints the absolute path, sheet and cell, or line and quote, and has a section "Failed conditions: where to look". When the check finds a quote or place that is not in the submission, `merge_judge_results.py` writes nothing; the only remedy is to re-run that judge. Do not correct the quote by hand, in the original file or in a copy, and do not build `assessment_result.json` another way: the result must be exactly what the judges reported and the script verified.
- Old v0.3 results: `scripts/convert_v03_results.py` + `profiles/manual-qa/v03-conversion.json` (T-04). It converts what has an equivalent (A1-A4, A7, A8, C1-C4, C6, C7 and template errors of B2-B4), leaves the rest pending, and reports a low-high score range.
- Overall verdict: FAIL if any competency scores below the line or the gate fails; PASS when all pass, the gate passes and nothing is pending; otherwise PENDING. Status is `final` only when the verdict is not PENDING and the trainer has reviewed the mapping.

## manual-qa profile v0.11 (criteria loaded, not yet runnable)

`profiles/manual-qa/criteria.json` (groups B and C; group A from `_shared/skill-standard.json`; `competencies`: requirements-analysis, test-design, test-case-generation, test-data-generation, defect-analysis-reporting) holds the criteria loaded from the sheet `Intermediate_Manual` of `AI-enabled QA Program.xlsx`, with the Description and Pass/Fail text translated from Vietnamese. Profile and fragment files hold criteria and scoring only, with no record of the source workbook, its cells or its open items; a reload from a new workbook version replaces the content. `"scoring_model": "weighted-pass-fail"`:

| Group | Section | Weight | Criteria |
|---|---|---|---|
| A Skill Standard | For Skills | 0.2 | A1 Naming Convention, A2 Structure Compliance, A3 Instruction Quality, A4 Reusability & Maintainability |
| B AI Application & Enablement | For Competence | 0.5 | B1 Task Decomposition, B2 Context & Knowledge Management, B3 Skill Execution & Repeatability, B4 Exception Handling & Recovery, B5 AI Integration & Workflow Coverage, B6 Usability & Execution Efficiency |
| C QA Output Quality | For Competence | 0.3 | C1 Accuracy, C2 Completeness & Coverage, C3 Usability & Format, C4 Human Validation & Improvement |
| SAFE AI Safety & Responsible Use (`gates[]`) | For Course | 0 | mandatory pass/fail gate, conditions not defined yet |

Each criterion has `description`, `pass_intro` + `pass_when_all[]` (the sheet's Pass conditions) (the sheet's Fail conditions were dropped on 2026-10-23: only pass conditions are graded). The sheet's "AI Assessor Need to Check" column is not loaded: it is not scored, and grading uses only the Pass/Fail conditions (course decision). Every criterion follows the course `pass_rule` (see "Pass rules"): today it passes only when all its conditions hold, with no partial pass. Scoring follows the course setting (see "Scoring (course-wide)"); the profile file has no `scoring` of its own.

What blocks a runnable pipeline:
- the scoring setting is incomplete: the number a pass/fail criterion counts as and the pass line that replaces "below 3" are undecided
- the safety gate has no pass/fail conditions
- C1 Accuracy: the description is about factual accuracy, but its Pass/Fail cells check clarification questions against the answer key's ambiguous points
- the answer key keeps the v0.3 shape (course decision): `profiles/manual-qa/baseline.template.json` is unchanged, with ACs, ambiguities, edge cases, planted bugs and `severity_scale`. Current criteria use the ambiguities (C1) and the ACs in scope (C2). The planted bugs and the `ambiguity_with_tr_pct` / `bug_found_pct` thresholds are kept for criteria that v0.4 dropped on purpose and will add back later. `import_baseline_xlsx.py` still writes this shape, but its `not_assessed` list names v0.3 criterion ids
- group B and C4 need evidence the sheet doesn't specify: transcripts, at least 2 similar runs (B3), a baseline effort (B6) and a verification record (C4)
- rebuilding the judge (`agents/manual-qa-assessment-judge.md`), `build_plan_from_profile.py`, `render_assessment_report.py` and `import_baseline_xlsx.py`; then converting the v0.3 results to the new scoring (course decision: convert, not drop): `test-fixtures/manual-qa-sample*/expected/` and `evals/sample-review-run-1`, `-2`

## The two files

| File | Holds | Filled from |
|---|---|---|
| `profiles/<name>/criteria.json` | Groups (A/B/C), the criteria in them, the pass threshold, and the L0 override | The course's rubric Excel (currently `QA_AI_Skills_Assessment_Rubric_MANUAL.xlsx`, in progress) |
| `<assessment>/baseline.json` (one per exam, passed with `--baseline`) | The answer key: acceptance criteria, ambiguities (mandatory or not), edge cases, planted bugs with severity, `severity_scale`, the percentage thresholds the criteria refer to, and the environment info the exam provided | The assessment author |

`criteria.json` is reused across assessments and lives in the profile. `baseline.json` belongs to **one assessment**: it is loaded together with that exam, kept next to it but never given to trainees, and passed to the script with `--baseline`. The profile only ships `baseline.template.json`, a skeleton full of `TODO` that shows the shape; copy it per exam and fill it in. `scripts/build_plan_from_profile.py` refuses to run while any `TODO` remains, and when the answer key's `profile` field names another profile. Both files carry a `version`.

## Answer key from the trainer's workbooks

The trainer supplies the answer key as Excel (the same layout trainees fill in), not as JSON. `scripts/import_baseline_xlsx.py` reads it and writes `<assessment>/baseline.json`:

```
python scripts/import_baseline_xlsx.py --tr Test_Requirement.xlsx --bug Bug_Report.xlsx [--tc Test_Case.xlsx]     --assessment-id <id> --requirement-source <exam file> [--build V --browser B --os O] --out <assessment>/baseline.json
```

| Baseline field | Read from |
|---|---|
| `acceptance_criteria` | unique AC ID + Acceptance Criteria pairs in the TR sheet (`N/A` rows skipped) |
| `ambiguities` | TR rows whose Notes start with `Missing info`; `Must ask` = mandatory, `Nice to confirm` = not |
| `edge_cases` | TR rows whose Notes start with `Edge case`; mandatory per an optional `Mandatory` column (Yes/No), else the `--edge-case-default` (mandatory) |
| `bugs`, `severity_scale` | Bug sheet rows; the scale is the Severity dropdown, highest first |
| `environment_info_provided` | not in the workbooks: pass `--build/--browser/--os`, otherwise null |

Rules of the importer: it never fabricates silently. Every default and every unclassifiable row goes into `import_notes` in the output and is printed, so read them before pre-registering. It fails with a plain message (nothing written) when a file is missing, is not an `.xlsx`, lacks the expected headers, or a bug severity is outside the dropdown. The Test Case workbook is only recorded as a reference file for the judge; its rows are not copied. Source workbooks are recorded with sha256 under `source_files`. `baseline.json` stays the single file passed to `build_plan_from_profile.py --baseline`, which hashes it into the plan.

**An exam without a bug-report competency:** omit `--bug`. The importer then lists `B4`, `C5`, `C6` under `not_assessed` in `baseline.json` (each with a reason) and leaves `bugs` empty. `build_plan_from_profile.py` drops those criteria from the plan, so the judge never grades them, and shrinks the totals accordingly. **The pass line is scaled in the same proportion and rounded up** (70 of 100 becomes 59 of 84 when 16 points are not assessed). That scaling is the framework's assumption, not a rule of the rubric; the plan keeps the original threshold next to the scaled one, and the report lists what was not assessed. Criteria that need the bug list say so with `needs: ["bugs"]` in `criteria.json`; an exam that does assess them must supply bugs.

Review `baseline.json` once after importing: the trainer, not the importer, decides which edge cases are mandatory.

## Scoring model

Every criterion is `deduction` type: `max_points`, `penalty_per_error`, and a `details` text that states what passes and what counts as an error.

- criterion points = `max_points` − `penalty_per_error` × errors, floored at 0
- the **judge reports error counts only**; `scripts/render_assessment_report.py` computes points, so grading is not bent by knowing the pass line
- group total = sum of its criteria; total = sum of groups; **PASS at `pass_threshold`** (70 of 100 for manual-qa)
- a criterion that meets its `na_when` condition scores full points and is flagged in the report. This is a choice: the trainee is not penalised for a criterion that does not apply. Change it in the script if the course wants N/A criteria dropped from the total instead.

## Groups and layers

| Group | Content | Layer |
|---|---|---|
| A | The trainee's skill set (A1–A8) | L0, **replaces D1–D8** |
| B | Workflow provenance from the chat transcript (B1–B4) | L1 |
| C | Output quality against the answer key (C1–C7) | L1 (L2 when scored) |

Trainee submission → layer: final skills → L0; chat prompts and transcript → evidence for L0 and B; **first manual-QA output in the chat log → L1**; refined version → L2; L3 = L2 − L1 via `agents/refinement-analyzer.md`. Each trainee is one sample (`n_repeats: 1`), so consistency is not measured and no consistency claim may be made.

Open point: the rubric scores a single output. Whether B (provenance) applies to L2, where hand edits are allowed, is not defined yet; until it is, score L2 on group C only.

## L0 override

`criteria.json` → `l0_override: {"mode": "replace", "group": "A", "reason": "..."}`. When present, group A **replaces** D1–D8: `agents/input-layer-judge.md` does not score them, and A1–A8 are graded by `agents/manual-qa-assessment-judge.md`. The override is copied into `eval_plan.json` at pre-registration. No override means D1–D8 apply as usual.

## Advisory flags and human decisions

A criterion may carry `advisory` entries (today, C6: `C6-severity`, severity more than one level from the key on `severity_scale`). For these the agent only **flags**, with the bug ID, the trainee's severity and the key's. A flag costs nothing and the report is `provisional` until a human decides. The human records:

```json
{"C6-severity:BUG-02": {"decision": "fail", "errors": 1}}
```

and passes it with `--human`. `fail` adds `errors` (default 1) to C6; `pass` adds nothing. Re-run the script after deciding; the status becomes `final` when no flag is pending.

## Wiring it into a run

1. Import the trainer's baseline workbooks into `<assessment>/baseline.json` (see "Answer key from the trainer's workbooks"), or copy `baseline.template.json` and fill it in by hand; revise `criteria.json` if the rubric changed (edit the JSON; the Excel import was a one-off).
2. Pre-register: `python scripts/build_plan_from_profile.py profiles/manual-qa --baseline <assessment>/baseline.json --skill-name <trainee> --hypothesis "<text>" [--has-refinement] --out evals/eval_plan.json`. The plan stores sha256 of both profile files, so a later edit is detectable.
3. Grade with `agents/manual-qa-assessment-judge.md` → `assessment_result.json`.
4. Report: `python scripts/render_assessment_report.py --plan evals/eval_plan.json --result <path> --out-dir report/ [--human decisions.json] [--submission-dir <submission root>]`. It writes `assessment_scoring_sheet.xlsx`, `assessment_report.md` and `assessment_report.json`.

## The scoring sheet

One row per criterion, laid out like the course's Excel scoring sheet:

| Column | Content |
|---|---|
| Category | The group (A Skill set, B Workflow coverage, C Output quality) |
| Sub-Category | Criterion id and name (e.g. `C4 TC quality`) |
| Evaluation Criteria | The criterion's `pass_when` |
| Max / Points / Errors | Points available, points earned, errors counted (human-decided flags included) |
| Evidence/Notes | One short line per deduction: an **evidence ref**, then a trimmed quote |
| Meets target? | `Yes` (no deduction), `No`, `N/A`, or `Pending human` |

Each group ends with a subtotal row, and the last row is the total against the pass threshold. Evidence refs use `path[:line]`, `path!Sheet!Cell` or `path#Heading`, relative to the submission root. With `--submission-dir` the script checks that each ref's file exists and marks it `(ref not found)` otherwise; a ref with no file path is marked `(no file ref)`. Both are also listed under Notes.

This sheet has no weight or skill/output 1-5 columns, because the manual-QA rubric scores by points and deductions. A profile with the weighted 1-5 model would need its own scoring model before it can use the same renderer.

## What the profile does not do

- It does not judge whether the criteria are good. That is the course owner's call.
- It does not match anything by string comparison. Whether a question covers an ambiguity, or a bug matches a BUG-xx, is a semantic judgment by the judge with a quoted `where`/`quote` for every error.
- Do not append post-hoc criteria to a generated plan. Anything noticed later goes in `exploratory_assertions[]`, or in `grading_notes` for the next profile version.

## auto-qa profile v0.17 (criteria loaded, not yet runnable)

`profiles/auto-qa/criteria.json` holds the criteria loaded from the sheet `Intermediate_auto` of `AI-enabled QA Program - automation side.xlsx`. It replaced the whole v0.1 profile, which held the maturity-levels model from `QA_AI_Skills_Assessment_Rubric_AUTO.xlsx`. It has the same groups, weights, gate structure and course scoring as manual-qa (`"scoring_model": "weighted-pass-fail"`). Group A is the shared `_shared/skill-standard.json`, identical to manual-qa; this sheet's own A1-A4 text is not used. B and C differ:

| Item | Content |
|---|---|
| Group B (B1-B5) | common conditions plus `by_sub_category` for the 7 sub-categories `TCD`, `FWG`, `SCR`, `REV`, `EXE`, `RES`, `DEF`: deliverables (B1), knowledge files (B2), trigger/assets/references/no project data (B3), `self_check` (B4), `trigger`/`handoff`/`delivered_to` (B5). B4 has a non-scoring `advisory_note` . B2 `clarifications`: the real application is explored with Playwright CLI, using only test accounts and test data of a test environment |
| B6 | `should_items[]` plus `pass_rule`: B3 and B5 must pass, and at least 2 of the 3 items must hold |
| Group C (C1-C4) | written for Playwright scripts (runs, locators, POM, rerun evidence). `clarifications` (course decisions): C1 locators: getByRole / getByTestId first, other user-facing locators (getByLabel, getByText, getByPlaceholder, getByAltText, getByTitle) accepted when reasonable and chosen by priority, taking each built-in locator's performance into account, CSS or XPath fails except XPath where built-in locators cannot target the element well (that XPath must be clean; CSS selectors have no exception); "serious errors" (C1) and "important AI errors" (C4) are exactly the ones in their parentheses; "minimal editing" (C3) means a short README / run guide. C4 `human_conditions`: explaining the submitted code is graded by the human grader |
| Gate `SAFE` | defined: only approved tools, no confidential data, AI output validated; a single violation fails. `clarifications`: "validating AI output" here means checking it for confidential/sensitive data only; using AI output without running, reviewing or refining it is graded by C4 and does not fail the gate; exploring the application through Playwright CLI with real (non-test) accounts or real data is a violation |
| `playwright-assessment.json` | the company's Playwright Assessment Level 1, the reference for grading the output of automation scripts (sub-category SCR); linked from group C as `output_reference`. 4 sections, 17 items: Interface (locators, page structure), Scripting and Debugging, Automation Test design, Configuration. Each item has a weight and a rating Poor 1 / Need to improve 2 / Meet 3 / Very Good 4 / Excellent 5; a section is Qualified at a weighted average of 3 or more; a comment is required below Meet. How it combines with C1-C4 and with the pass/fail model is undecided |
| `tech_stack` | Playwright + TypeScript, fixed by the course; no other stack is used |
| `evidence_package` | what a submission must include, unchanged from the earlier auto rubric: skills folder; full, unedited transcripts with the skill invocation; output files; run logs (`tsc`, lint, `npx playwright test`, CI/scheduler logs, test reports); git history / merge request / review records. Missing evidence means the condition fails; screenshots or pasted text without a transcript do not count |

Like manual-qa, it is blocked on the undecided parts of the course scoring. Auto assessments have no answer key (course decision; `answer_key.exists` is false), so auto-qa has no `baseline.template.json`. It has no judge or scripts yet, and `build_plan_from_profile.py` rejects it.
