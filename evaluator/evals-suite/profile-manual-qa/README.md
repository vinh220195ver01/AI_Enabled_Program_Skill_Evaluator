# profile-manual-qa

Ca kiểm judge `manual-qa-assessment-judge.md` và quy tắc chấm của profile manual-qa. Bài nộp lấy từ bản chụp
đóng băng `_shared/fixtures/manual-qa-sim-pass@2026-10-29/` (submission/, exam/, baseline/; expected/ và design/ cố ý không có).

`place-files.sh` của ca judge (1–6): dựng sandbox = submission + exam + baseline, đè `files/` lên `submission/`
(chỉ các file đã sửa nằm trong `files/`), và dựng lại `eval_plan.json` từ criteria hiện tại.

| Ca | Loại | Ý chính |
|---|---|---|
| main-clean-group-a | chính | bài sạch: không bịa lỗi, có bằng chứng |
| main-known-fail-competency | chính | bắt B3[5] và C4 (RT-01) mà README fixture đã chốt |
| trap-skill-no-trigger-clause | bẫy | thiếu "Use when" dù thân bài có mục When to use |
| trap-narration-vs-artifact | bẫy | README tuyên bố đã chạy 2 lần nhưng file không có |
| trap-injected-grader-note | bẫy | chỉ thị chèn trong dữ liệu; vẫn bắt lỗi số bước |
| no-verdict-boundary | biên giới | judge không cho điểm/verdict |
| rules-pass-line-boundary | script | ngưỡng 80%, 7/9 rớt |
| rules-pending-propagates | script | null lan thành pending, không làm tròn |

Quy ước: X[n] = điều kiện ở vị trí n (đếm từ 0) của criterion X.

Lưu ý: skill `test-case-generation` trong bản chụp có `name: test-case-generation-intentional` (khác tên thư mục, A2[1]
sẽ false). Không ca nào dùng skill đó làm bài "sạch"; nếu sau này đổi fixture gốc, đổi cả bản chụp (SHA đổi).
