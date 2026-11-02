# Quy đổi kết quả v0.3 sang criteria hiện tại

Nguồn: `..\..\test-fixtures\manual-qa-sample\expected\assessment_result.json` · profile 0.11-draft · 44 / 231 điều kiện có dữ liệu từ v0.3, 187 chưa có tương đương (pending).

## Điểm competency (khoảng)

Thấp = mọi điều kiện pending tính là không thỏa; cao = tính là thỏa. Ngưỡng đạt 3 / 5.

| Competency | A (thấp–cao) | B | C | Điểm (thấp–cao) | Kết luận |
|---|---|---|---|---|---|
| requirements-analysis | 3.75–5.0 | 0.0–5.0 | 0.9896–4.2263 | 1.0469–4.7679 | chưa kết luận được |
| test-case-generation | 2.0834–3.3334 | 0.0–5.0 | 0.1562–4.4866 | 0.4635–4.5127 | chưa kết luận được |
| defect-analysis-reporting | 3.5416–4.7916 | 0.0–5.0 | 0.5134–4.8214 | 0.8623–4.9047 | chưa kết luận được |

## Từng tiêu chí v0.3

| Tiêu chí v0.3 | Kết quả quy đổi |
|---|---|
| A1 Structure (1 lỗi) | exact: 1 error(s) -> Test-Case-Generation/A1[0] |
| A2 Frontmatter (1 lỗi) | exact: 1 error(s) -> Test-Case-Generation/A2[1] |
| A3 Description (1 lỗi) | exact: 1 error(s) -> defect-analysis-reporting/A3[0] |
| A4 Process (1 lỗi) | approximate: 1 error(s) -> Test-Case-Generation/A3[4] |
| A5 File-opening instructions (1 lỗi) | no current equivalent |
| A6 Files in the right place (1 lỗi) | no current equivalent |
| A7 No domain knowledge (2 lỗi) | exact: 2 error(s) -> Test-Case-Generation/A4[0] |
| A8 No overlap (0 lỗi) | exact: 0 error(s) -> none placed |
| B1 Clarification questions (provenance) (0 lỗi) | no current equivalent |
| B2 TR list (provenance) (0 lỗi) | approximate: 0 error(s) -> none placed |
| B3 TC list (provenance) (2 lỗi) | approximate: 2 error(s) -> none placed |
| B4 Bug report (provenance) (1 lỗi) | approximate: 1 error(s) -> defect-analysis-reporting/C2[1] |
| C1 Clarification questions (quality) (2 lỗi) | exact: 2 error(s) -> requirements-analysis/C1[0] |
| C2 TR list (quality) (3 lỗi) | approximate: 3 error(s) -> requirements-analysis/C2[0], requirements-analysis/C2[4] |
| C3 TC coverage (1 lỗi) | approximate: 1 error(s) -> test-case-generation/C2[0] |
| C4 TC quality (2 lỗi) | approximate: 2 error(s) -> test-case-generation/C3[2] |
| C5 Bug finding (0 lỗi) | approximate: 0 error(s) -> none placed |
| C6 Bug report quality (2 lỗi) | approximate: 2 error(s) -> defect-analysis-reporting/C2[1] |
| C7 No fabrication (3 lỗi) | approximate: 3 error(s) -> test-case-generation/C2[4] |

## Lỗi v0.3 không quy đổi được

- A5: `skills/Test-Case-Generation/references/old-notes.md` — file is never mentioned in SKILL.md
- A6: `skills/Test-Case-Generation/references/tc-template.xlsx` — an Excel template sits in references/
- B3: `chat-transcript.md:56` — code saves tc-list-v1.xlsx but the submitted file is tc-list.xlsx
- B3: `outputs/tc-list.xlsx!TC List!A12` — TC-09 uses TR-11, which is not in tr-list.xlsx
- C6: `outputs/bug-list.xlsx!Bug List!N5` — OS 'Windows 11' is not provided by the exam

## Không có tương đương ở criteria hiện tại

- advisory flag C6-severity
- A5 file references
- A6 files in the right place
- B1-B4 provenance of the output (transcript shows the skill produced it)
- C3-C7 conditions of v0.3 not listed above

## Điều kiện đã quy đổi thành không thỏa

- **Test-Case-Generation / A1[0]**: v0.3 A1 Structure: folder name has uppercase letters (skills/Test-Case-Generation)
- **Test-Case-Generation / A2[1]**: v0.3 A2 Frontmatter: name 'test-case-generation' differs from folder 'Test-Case-Generation' (skills/Test-Case-Generation/SKILL.md:2)
- **Test-Case-Generation / A3[4]**: v0.3 A4 Process: steps are numbered 1, 2, 3, 5 (4 is skipped) (skills/Test-Case-Generation/SKILL.md:13)
- **Test-Case-Generation / A4[0]**: v0.3 A7 No domain knowledge: https://staging.acme-notes.example/login; v0.3 A7: the account locks after 5 failed attempts and stays locked for 15 minutes (skills/Test-Case-Generation/SKILL.md:17; skills/Test-Case-Generation/references/tc-writing-rules.md:5)
- **defect-analysis-reporting / A3[0]**: v0.3 A3 Description: description 'This skill writes bug reports.' has no trigger clause (skills/defect-analysis-reporting/SKILL.md:3)
- **defect-analysis-reporting / C2[1]**: v0.3 B4 Bug report (provenance): section 'Missing Information & Recommended Next Investigation' is missing; v0.3 C6: no Observed Result (chat-transcript.md:69; outputs/bug-list.xlsx Bug List!C6)
- **requirements-analysis / C1[0]**: v0.3 C1 Clarification questions (quality): only 1 of 2 mandatory and 3 of 5 ambiguities found (60%, below 70%); v0.3 C1: mandatory AMB2 (counter reset) is not asked (chat-transcript.md:20; chat-transcript.md:20)
- **requirements-analysis / C2[0]**: v0.3 C2 TR list (quality): AC4 has no TR row (outputs/tr-list.xlsx)
- **requirements-analysis / C2[4]**: v0.3 C2 TR list (quality): mandatory AMB2 has no TR row; v0.3 C2: 3 of 5 ambiguities (60%) have a TR row, below 70% (outputs/tr-list.xlsx; outputs/tr-list.xlsx)
- **test-case-generation / C2[0]**: v0.3 C3 TC coverage: TR-07 (correct password during the lock, mandatory edge case EC2) has no TC in outputs/tc-list.xlsx (outputs/tr-list.xlsx Test Requirement!C10)
- **test-case-generation / C2[4]**: v0.3 C7 No fabrication: 'Password must be 8-20 characters' is not in the user story and has no Assumption flag; v0.3 C7: spaces-only email shows 'Email is required' (the story only covers an empty email) and has no Assumption flag; v0.3 C7: 'the Login button is disabled' after the lock is not in the story and has no Assumption flag (outputs/tc-list.xlsx TC List!F10; outputs/tc-list.xlsx TC List!F8; outputs/tc-list.xlsx TC List!F9)
- **test-case-generation / C3[2]**: v0.3 C4 TC quality: Expected Result 'Error is displayed correctly'; v0.3 C4: Expected Result 'Success' (outputs/tc-list.xlsx TC List!F7; outputs/tc-list.xlsx TC List!F12)
