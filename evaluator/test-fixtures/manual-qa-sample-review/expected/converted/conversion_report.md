# Quy đổi kết quả v0.3 sang criteria hiện tại

Nguồn: `..\..\test-fixtures\manual-qa-sample-review\expected\assessment_result.json` · profile 0.11-draft · 30 / 154 điều kiện có dữ liệu từ v0.3, 124 chưa có tương đương (pending).

## Điểm competency (khoảng)

Thấp = mọi điều kiện pending tính là không thỏa; cao = tính là thỏa. Ngưỡng đạt 3 / 5.

| Competency | A (thấp–cao) | B | C | Điểm (thấp–cao) | Kết luận |
|---|---|---|---|---|---|
| requirements-analysis | 3.75–5.0 | 0.0–5.0 | 1.7634–5.0 | 1.279–5.0 | chưa kết luận được |
| test-case-generation | 3.75–5.0 | 0.0–5.0 | 0.6696–5.0 | 0.9509–5.0 | chưa kết luận được |

## Từng tiêu chí v0.3

| Tiêu chí v0.3 | Kết quả quy đổi |
|---|---|
| A1 Structure (0 lỗi) | exact: 0 error(s) -> none placed |
| A2 Frontmatter (0 lỗi) | exact: 0 error(s) -> none placed |
| A3 Description (0 lỗi) | exact: 0 error(s) -> none placed |
| A4 Process (0 lỗi) | approximate: 0 error(s) -> none placed |
| A5 File-opening instructions (0 lỗi) | no current equivalent |
| A6 Files in the right place (0 lỗi) | no current equivalent |
| A7 No domain knowledge (0 lỗi) | exact: 0 error(s) -> none placed |
| A8 No overlap (0 lỗi) | exact: 0 error(s) -> none placed |
| B1 Clarification questions (provenance) (0 lỗi) | no current equivalent |
| B2 TR list (provenance) (0 lỗi) | approximate: 0 error(s) -> none placed |
| B3 TC list (provenance) (0 lỗi) | approximate: 0 error(s) -> none placed |
| B4 Bug report (provenance) (0 lỗi) | not graded in this v0.3 result (not assessed) |
| C1 Clarification questions (quality) (0 lỗi) | exact: 0 error(s) -> none placed |
| C2 TR list (quality) (0 lỗi) | approximate: 0 error(s) -> none placed |
| C3 TC coverage (0 lỗi) | approximate: 0 error(s) -> none placed |
| C4 TC quality (0 lỗi) | approximate: 0 error(s) -> none placed |
| C5 Bug finding (0 lỗi) | not graded in this v0.3 result (not assessed) |
| C6 Bug report quality (0 lỗi) | not graded in this v0.3 result (not assessed) |
| C7 No fabrication (0 lỗi) | approximate: 0 error(s) -> none placed |

## Không có tương đương ở criteria hiện tại

- advisory flag C6-severity
- A5 file references
- A6 files in the right place
- B1-B4 provenance of the output (transcript shows the skill produced it)
- C3-C7 conditions of v0.3 not listed above

## Điều kiện đã quy đổi thành không thỏa

