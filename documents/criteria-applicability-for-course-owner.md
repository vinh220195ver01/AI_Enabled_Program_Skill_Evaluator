# C1, C2, B3: điều kiện không áp dụng được cho từng competency

Gửi: course owner · Nguồn: lần chấm đầu tiên `manual-qa-sim-pass` (`evaluator/evals/sim-pass-run-1/`, criteria `manual-qa` v0.11-draft) · Ngày: 2026-10-21

B và C được chấm **riêng cho từng competency** (M-13), nhưng nhiều điều kiện của C1, C2, B3 chỉ viết cho một loại output (danh sách câu hỏi, test case). Judge phải tự "đọc theo nghĩa" cho các competency còn lại. Mỗi chỗ đó là một quyết định của judge mà bạn chưa duyệt, và kết quả đổi theo cách đọc. Cần bạn chọn cách đọc chính thức. (Cập nhật 2026-10-23: tiêu chí chỉ còn điều kiện Pass và đạt khi thỏa ≥ 80% điều kiện; kết quả các bảng dưới đây không đổi.)

Ký hiệu: **✔** áp dụng đúng như viết · **~** không áp dụng được nguyên văn, judge tự suy ra (ghi cách đọc) · **✘** không có nghĩa với competency này.

Competency: RA = requirements-analysis, TD = test-design, TCG = test-case-generation, TDG = test-data-generation, DAR = defect-analysis-reporting.

## C1 Accuracy

| # | Điều kiện (nguyên văn) | RA | TD | TCG | TDG | DAR |
|---|---|---|---|---|---|---|
| 0 | Finds at least 70% of all ambiguous points | ✔ | ~ | ~ | ~ | ~ |
| 1 | Every Mandatory ambiguous point the trainee found is in the "Must ask" group, not in "Nice to confirm" | ✔ | ~ | ~ | ~ | ✘ |
| 2 | Both groups "Must ask" and "Nice to confirm" are present | ✔ | ~ | ~ | ~ | ✘ |

Cách judge đọc cho từng competency (kết quả đã chấm):

- **TD, TCG, TDG:** các competency này không tự tạo danh sách câu hỏi. Judge chấm theo các Q-ID mà output của chúng trích dẫn (ghi chú "Missing info / Assumption (Q-xx)"), và lấy nhóm Must/Nice từ `runs/run-1/clarification-questions.md` (sản phẩm của RA). Hệ quả: điều kiện 2 "đạt" chỉ vì file của RA có hai nhóm.
- **TDG:** nếu tính trên cả 12 điểm mơ hồ thì chỉ 5/12 (42%) liên quan tới dữ liệu. Judge tính các điểm làm đổi giá trị dữ liệu và chấm đạt.
- **DAR:** judge đổi "điểm mơ hồ" thành "bug cài sẵn" và dùng `baseline.thresholds.bug_found_pct = 60`: ghi nhận 3/5 bug = đúng 60% → đạt. Theo chữ "70%" của điều kiện thì **không đạt**. Điều kiện 1 và 2 judge đọc là "mức nghiêm trọng đúng" và "có tham chiếu cả hai nhóm câu hỏi".
- **Kết quả không nhất quán giữa competency cho cùng một nguyên nhân:** điểm mơ hồ bắt buộc AMB5 (khách thấy gì ngay sau khi gửi review) bị tách: trạng thái ban đầu ở Must ask (Q-08), thông báo xác nhận và form sau khi gửi ở Nice to confirm (Q-21, Q-22). Judge RA và TD chấm điều kiện 1 là đạt (đọc "phần chính"), judge TCG chấm không đạt. Run 2 của RA xếp cả AMB5 vào Must.

Câu hỏi cho bạn:

1. C1 chỉ áp dụng cho RA, còn các competency khác là N/A (loại khỏi trung bình, xem M-19)? Hay mỗi competency cần điều kiện C1 riêng (vd TD: "mọi điểm mơ hồ mà design gặp đều có Assumption/Missing info"; DAR: "% bug cài sẵn tìm thấy ≥ …")?
2. Nếu C1 áp dụng cho nhiều competency: mẫu số là tất cả điểm mơ hồ của đề, hay chỉ các điểm liên quan competency đó?
3. Điểm mơ hồ bắt buộc có nhiều phần (AMB5): cần cả các phần đều ở Must ask, hay phần chính là đủ?
4. 70% (điều kiện) hay 60% (`bug_found_pct` trong baseline) cho bug? Hai con số đang mâu thuẫn.

## C2 Completeness & Coverage

| # | Điều kiện (nguyên văn, rút gọn) | RA | TD | TCG | TDG | DAR |
|---|---|---|---|---|---|---|
| 0 | Every requirement/AC in scope is covered by at least one output item | ✔ | ✔ | ✔ | ~ | ~ |
| 1 | Has all mandatory components of the template (objective, precondition, test data, steps, expected result...) | ✔ | ✔ | ~ | ✔ | ✔ |
| 2 | Has all relevant scenario types: positive, negative, boundary, validation, error handling, permissions, integration, UI, compatibility, regression | ~ | ✔ | ✔ | ~ | ~ |
| 3 | Misses no important risk in scope (payment, data, security, main flow) | ✔ | ✔ | ✔ | ~ | ~ |
| 4 | Missing or ambiguous points are raised as clarification questions or assumptions | ✔ | ✔ | ✔ | ✔ | ✔ |
| 5 | Parts not covered or excluded are stated with a reason | ✔ | ✔ | ✔ | ~ | ✔ |
| 6 | No serious omissions; minor omissions are within the allowed threshold | ✔ | ✔ | ✔ | ~ | ✘ |

Chỗ không áp dụng được nguyên văn:

- **Điều kiện 0 (TDG, DAR):** test data bám test case, không bám AC; bug report không "phủ" requirement. Judge đọc: TDG = mọi test case chạy được có dữ liệu; DAR = mọi dòng Fail trong `test-execution.xlsx` được xử lý (thành bug hoặc giải thích).
- **Điều kiện 1 (TCG):** danh sách thành phần có "test data", nhưng template test case thật (`test-case-template.xlsx`) không có cột test data (dữ liệu nằm trong Steps). Judge chấp nhận.
- **Điều kiện 2:** danh sách 10 loại kịch bản viết cho test case. RA đọc là "TR có loại nào", TDG là "loại dữ liệu (valid, invalid, boundary...)", DAR là "loại lỗi có trong bằng chứng". Ngoài ra "all relevant" không nói ai quyết định loại nào relevant: bản demo chỉ chạy Chrome nên compatibility bị loại, regression bị coi là không áp dụng.
- **Điều kiện 3 (TDG, DAR):** "payment" không có trong đề; "main flow" của bug report là gì? Với DAR judge đọc là "bug cài sẵn quan trọng": BUG-03 (số liệu tóm tắt đếm review đang chờ) **có** trong retest nhưng không vào bug list → không đạt.
- **Điều kiện 6:** "allowed threshold" chưa có giá trị (M-22). Với DAR không áp dụng được: judge dùng chung kết quả của điều kiện 3 (bug cài sẵn BUG-04, 500 ký tự bị từ chối, không bao giờ được tìm thấy). **Vấn đề công bằng:** BUG-04 không được tìm thấy vì các test case độ dài bị BLOCKED ở bước thực thi (bước do người làm, không dùng AI), nên DAR bị trừ vì lỗi của khâu khác.

Câu hỏi cho bạn:

5. Cho từng competency, danh sách "loại kịch bản" nào là bắt buộc (điều kiện 2)? Ai quyết định loại nào relevant (đề, judge, hay trainer)?
6. Điều kiện 0 và 6 của DAR: dựa vào cái gì để biết bug bị bỏ sót, khi bug cài sẵn phụ thuộc vào việc thực thi test (ngoài phạm vi skill)? Tính bug bỏ sót vào DAR hay vào khâu thực thi (không có competency)?
7. "Minor omissions within the allowed threshold": ngưỡng là bao nhiêu (M-22)?

## B3 Skill Execution & Repeatability

| # | Điều kiện (nguyên văn) | RA | TD | TCG | TDG | DAR |
|---|---|---|---|---|---|---|
| 0 | Picks the right skill for the right situation | ✔ | ✔ | ✔ | ✔ | ✔ |
| 1 | Provides the input the skill requires and answers fully when the skill asks for more | ✔ | ✔ | ✔ | ✔ | ✔ |
| 2 | Follows the skill's mandatory steps and checkpoints | ✔ | ✔ | ✔ | ✔ | ✔ |
| 3 | Checks the output against the skill's standard, notices deviations, asks for a rerun | ✔ | ✔ | ✔ | ✔ | ✔ |
| 4 | Similar runs give consistent results in structure and level of detail | ✔ | ✔ | ✔ | ✔ | **✘ (1 run)** |
| 5 | Records, or can explain, how to run it, so someone else following it gets an equivalent result | ✔ | ✔ | **không đạt** | ✔ | ✔ |

- **Điều kiện 4 (DAR):** competency này chỉ có một lần chạy (người dùng dừng bước sửa bug report, README ghi "ran once"). Vì chỉ có một lần chạy nên không có gì để so sánh, điều kiện 4 không đạt (danh sách Fail cũ có dòng "Only one run is available as evidence"; danh sách Fail đã bỏ từ 2026-10-23, chỉ còn điều kiện Pass). Đề thi không bắt buộc chạy skill nào hai lần, nên không thể biết đây là lỗi của học viên hay do đề.
- **Điều kiện 5 (TCG):** các quyết định định hình kết quả (dùng assumption làm expected result làm việc, tiền tố BLOCKED / NOT RUN / OBSERVE ONLY) được nói trong chat, không nằm trong SKILL.md hay README. Làm theo README sẽ ra output khác: 120 expected result "To be confirmed" thay vì 35. Tương tự ở TDG: bộ lọc "chỉ test case chạy được" nằm trong prompt, không nằm trong skill. Điều kiện này có nghĩa với mọi skill, nhưng chỉ TCG bị chấm không đạt trong lần này.
- **Điều kiện 3 và C4:** cùng một nguyên nhân (review mỏng) dễ bị trừ ở B3.3 và C4.1; judge TD đã chỉ đếm một lần ở C4. Nên có quy tắc chung: đếm một nguyên nhân một lần cho mỗi competency.

Câu hỏi cho bạn:

8. Mỗi skill phải chạy tối thiểu mấy lần (cho điều kiện 4)? Nếu đề không yêu cầu, thì competency chỉ chạy một lần được tính N/A, không đạt, hay đạt?
9. Điều kiện 5: lệnh/quy tắc nằm trong chat nhưng không nằm trong skill có được coi là "ghi lại" không?

## Vấn đề chung (ảnh hưởng cả ba tiêu chí)

- **M-19 (N/A):** khi một điều kiện không áp dụng, loại điều kiện đó khỏi mẫu số hay cho đạt? Quy tắc 20% của `deduction` tính trên tổng số điều kiện, nên loại hay không loại thay đổi kết quả (vd C1 của DAR còn 1 điều kiện thì 1 lỗi = 100% Fail).
- **Bằng chứng dùng chung:** `README.md`, `review/review-log.md`, `knowledge/` chung cho mọi competency. Một lỗi (vd review mỏng) hiện bị tính ở nhiều competency (C4 của RA, TD, TCG, TDG đều không đạt điều kiện "systematic check"). Đây là cố ý (mỗi competency tính riêng) hay một lỗi chỉ tính một lần?
- **Competency không có skill nào:** nhóm A = 0 (đang là quy tắc tạm), nhưng B và C vẫn chấm. Có hợp lý không?
- **Kết quả không nhất quán** giữa các judge với cùng một bằng chứng (AMB5, mục C1 trên). Cần quy tắc: judge nào quyết định cách đọc, hay trainer quyết định sau khi xem bảng này.

## Đề xuất

1. Với điều kiện không áp dụng được cho một competency, đánh dấu `na_for: [competency...]` trong criteria; judge trả "N/A" thay vì tự đọc.
2. Viết lại C1 theo từng competency (RA giữ nguyên; competency khác dùng định nghĩa riêng), hoặc giới hạn C1 cho RA.
3. Thêm vào đề số lần chạy tối thiểu mỗi skill (hỗ trợ B3.4).
4. Quyết định M-19 trước khi bật N/A trong code.
