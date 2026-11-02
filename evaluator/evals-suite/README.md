# evals-suite

Bộ evals (test case) cho các thành phần của `evaluator/`. Ba nhóm:

| Nhóm | Kiểm | Trạng thái |
|---|---|---|
| `skill-evaluator/` | Hành vi của framework (quy trình, các điều cấm) | 8 ca, đã dựng |
| `profile-manual-qa/` | Pipeline chấm bài theo criteria manual-qa | chưa dựng |
| `profile-auto-qa/` | Pipeline chấm bài theo criteria auto-qa | chưa dựng |

`_shared/` chứa `place-files.common.sh` và `fixtures/` (bản chụp đóng băng, có sha256 trong `SNAPSHOT.json`).

## Cấu trúc một ca

`prompt.md` (lời người dùng, không lộ đáp án), `files/` (dữ liệu giả), `place-files.sh <sandbox>`
(copy vào sandbox của lượt chạy), `case.yaml` (`expected_outcome`: kết luận đúng, hành vi bắt buộc, điều KHÔNG được làm).

## Cách chạy một ca

1. `bash place-files.sh <sandbox-dir>`
2. Cho agent làm việc trong `<sandbox-dir>` với lời `prompt.md`, một lượt CÓ skill-evaluator, một lượt KHÔNG (đối chứng).
3. Đối chiếu kết quả với `expected_outcome`.

## Danh sách ca skill-evaluator

| Ca | Loại | Ý chính |
|---|---|---|
| main-ab-version-compare | chính | so hai phiên bản: chấm mù, pre-register, đánh đổi chi phí |
| main-l0-only-report | chính | chỉ báo cáo L0, không lan sang L1 |
| trap-no-refinement-step | bẫy | từ chối bịa L2/L3 |
| trap-single-run-surprise | bẫy | N=1 và lỗi chấm ở a3 |
| trap-weak-l0-checkpoint | bẫy | dừng ở checkpoint dù tổng điểm hạng C |
| trap-multi-run-noisy-judge | bẫy | fail nhất quán vs nhiễu, không có tổng điểm chính thức |
| trap-fabricated-evidence-quote | bẫy | quote bịa: chỉ chạy lại judge sai |
| no-trigger-skill-authoring | không kích hoạt | việc viết lại description là của skill-creator |
