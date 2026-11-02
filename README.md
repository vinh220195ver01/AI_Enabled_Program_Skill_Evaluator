# AI Enabled Program — Skill Evaluator

Phần đánh giá (skill-evaluator) tách ra từ repo `AI_Enabled_Program`.

| Thư mục | Nội dung |
|---|---|
| `evaluator/skills/skill-evaluator/` | Skill chính: `SKILL.md`, agents (judge), profiles `manual-qa` / `auto-qa` / `_shared`, references, scripts |
| `evaluator/evals-suite/` | Bộ eval cho framework và các profile (`skill-evaluator/`, `profile-manual-qa/`, `_shared/`) |
| `evaluator/test-fixtures/` | Bài nộp mẫu và kết quả kỳ vọng dùng để kiểm thử pipeline chấm |
| `evaluator/prompts/` | Prompt chạy chấm bài, mô phỏng bài nộp, viết test cho skill |
| `evaluator/.claude-plugin/` | Khai báo plugin |
| `documents/` | Rubric khóa học (bản chụp lịch sử) và ghi chú cho course owner |
| `work-log.md` | Nhật ký quyết định và bảng theo dõi câu hỏi clarify (M-xx, AU-xx) |

Giữ nguyên cấu trúc `evaluator/...` như repo gốc để các đường dẫn tương đối trong prompts và `place-files.sh` vẫn đúng.

`evaluator/evals/` (output các lượt chạy) không nằm trong repo; thư mục này bị `.gitignore`.
