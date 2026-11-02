# Work log

## Theo dõi câu hỏi cần clarify

Mỗi câu hỏi có một ID cố định: `M-xx` cho manual, `AU-xx` cho auto. Nội dung đầy đủ của từng câu nằm ở các mục theo ngày bên dưới. **Trạng thái chỉ cập nhật ở bảng này.**

Trạng thái:
- `Mở`: chưa có câu trả lời.
- `Đã trả lời`: ghi câu trả lời hoặc quyết định vào cột "Câu trả lời / quyết định", kèm nguồn (ai trả lời, ở đâu) và ngày.
- `Không còn áp dụng`: câu hỏi không còn ý nghĩa vì một quyết định khác.
- `Gộp vào <ID>`: trùng với câu khác; theo dõi ở câu đó.

### Manual (`Intermediate_Manual`)

| ID | Câu hỏi (tóm tắt) | Trạng thái | Câu trả lời / quyết định | Nguồn | Ngày |
|---|---|---|---|---|---|
| M-01 | Thang 1–5 của `Intermediate_bk` còn hiệu lực không? | Đã trả lời | Không còn hiệu lực | Chat | 2026-10-19 |
| M-02 | Đạt/Không đạt của mỗi tiêu chí quy ra mấy điểm, và ngưỡng đạt mới thay cho "> 3" là bao nhiêu? | Đã trả lời | Mỗi nhóm A/B/C = 5 điểm, chia đều cho các tiêu chí; trong tiêu chí mỗi điều kiện cùng trọng số, mỗi điều kiện không thỏa bị trừ phần của nó; tiêu chí Fail khi ≥ 20% điều kiện không thỏa. **Xác nhận 2026-10-21:** Competency Score = A×0.2 + B×0.5 + C×0.3 (thang 0–5), đạt khi ≥ 3 (giữ ngưỡng "< 3" cũ); tiêu chí Fail vẫn giữ điểm một phần | Chat | 2026-10-21 |
| M-03 | Level 4–5 đạt được bằng cách nào? | Không còn áp dụng | Không còn thang 1–5 nên không có level 4–5 | Theo M-01 | 2026-10-19 |
| M-04 | Nếu Pass = 3 thì Option 1 ("> 3") không ai đạt; ý định là "> 3" hay "≥ 3"? | Gộp vào M-02 | Không còn thang 1–5 nên ngưỡng 3 phải định nghĩa lại; theo dõi ở M-02 | Theo M-01 | 2026-10-19 |
| M-05 | "Đạt khi" có nghĩa là phải thỏa tất cả điều kiện? | Đã trả lời | Có: phải thỏa tất cả điều kiện Pass mới Đạt, áp dụng cho mọi tiêu chí (cả manual và auto) | Chat | 2026-10-19 |
| M-06 | Thỏa hết Pass nhưng dính một điều Fail thì bên nào ưu tiên? | Không còn áp dụng | Danh sách Fail bị bỏ khỏi criteria (2026-10-23); chỉ chấm điều kiện Pass | Chat | 2026-10-23 | | | |
| M-07 | Có cho đạt một phần không? | Đã trả lời | (Thay đổi 2026-10-21: có, theo ngưỡng 20% của M-02.) Trước đó: không: một điều kiện không thỏa là Không đạt cả tiêu chí. Có thể đổi sau: chỉ cần sửa `pass_rule` trong `_shared/course-rules.json` (xem entry 2026-10-19 "Pass rule cấu hình được") | Chat | 2026-10-19 |
| M-08 | Cột F "AI Assessor Need to Check" có tính điểm không? | Đã trả lời | Không. Bỏ qua cột này; chỉ chấm theo điều kiện Pass/Fail. Đã xóa `assessor_checks` khỏi criteria | Chat | 2026-10-19 |
| M-09 | "Skill template / skill standard / naming convention" là tài liệu nào? (dùng chung cho nhóm A của manual và auto) | Đã trả lời | Tạo mới: `profiles/_shared/skill-standard.md` (chuẩn) + `profiles/_shared/SKILL.template.md` (mẫu). Đã duyệt, phát hành v1.0 | Chat | 2026-10-19 |
| M-10 | Các tiêu chí trong nhóm có trọng số bằng nhau? | Đã trả lời | Có. Điểm nhóm = trung bình cộng các tiêu chí trong nhóm (vd B = trung bình B1–B6) | Chat | 2026-10-19 |
| M-11 | Option 2: nhóm A chấm theo từng skill rồi lấy trung bình qua các skill của competency? A1 ghi "TẤT CẢ skill" có mâu thuẫn không? | Đã trả lời | Trong một skill, A1–A4 gộp bằng trung bình cộng (M-10). Khi một competency có nhiều skill: mỗi tiêu chí (A1, A2...) lấy **trung bình điểm các skill**; đạt (Pass) khi trung bình ≥ 3/5 (cùng ngưỡng competency score), không còn theo kiểu "1 skill fail là cả tiêu chí fail". Chỉ 1 skill thì giữ nguyên verdict gốc của tiêu chí đó (ngưỡng 80% điều kiện theo `course-rules.json`), không đổi | Chat | 2026-10-24 |
| M-12 | Option 1: bài thi gồm những competency nào? | Gộp vào M-13 | Option 1 bị loại; câu hỏi competency của bài thi chuyển sang M-13 (Option 2) | Theo M-14 | 2026-10-19 |
| M-13 | Option 2: bài thi gồm competency nào, skill nào thuộc competency nào, ai khai báo? Dòng "AI Application/QA Output Quality" còn bỏ dở | Đã trả lời | (1) B và C chấm riêng cho từng competency. (2) Khóa học có 7 competency: Requirements Analysis, Test Design, Test Case Generation, Test Data Generation, Automation Development, Test Maintenance, Defect Analysis & Reporting (đều "AI-assisted"). (3) Bài manual ứng với 4: Requirements Analysis, Test Design, Test Case Generation, Test Data Generation (thay đổi 2026-10-28: M-29 thêm Defect Analysis & Reporting; riêng đề Home Product Discovery chỉ chấm 3 competency requirements-analysis, test-case-generation, defect-analysis-reporting, loại test-design và test-data-generation, xem mục 2026-10-28). (4) AI agent phân loại skill nào thuộc competency nào, ghi rõ trong báo cáo chấm cuối; trainer review | Chat | 2026-10-19 |
| M-14 | Chọn Option 1 hay Option 2? | Đã trả lời | Option 2. Option 1 đã bị loại | Chat | 2026-10-19 |
| M-15 | Làm tròn điểm thế nào? Kết quả cuối chỉ PASS/FAIL hay kèm level? | Mở | | | |
| M-16 | Điều kiện Pass/Fail của gate AI Safety (manual) | Mở | | | |
| M-17 | Gate do AI chấm hay người quyết định? Gate Fail thì tổng là FAIL? | Mở | | | |
| M-18 | Gate có trùng với B2 (bảo vệ dữ liệu nhạy cảm) không? | Mở | | | |
| M-19 | Tiêu chí N/A tính thế nào? | Mở | | | |
| M-20 | Thiếu bằng chứng: tính Không đạt luôn hay xử lý riêng? | Mở | | | |
| M-21 | Bộ bằng chứng cần nộp cho nhóm B và C4 | Mở | | | |
| M-22 | Ngưỡng chưa định nghĩa (C2, B6, B3, A3) | Mở | Một phần (2026-10-19, chat): A3 so với các skill khác mà học viên nộp; mỗi skill làm một task khác nhau, không trùng lặp. Còn mở: C2, B6, B3 | | |
| M-23 | Tiêu chí nào cần người quyết định? Kết quả AI chính thức hay tạm thời? | Mở | | | |
| M-24 | C1 Accuracy: mô tả và điều kiện Pass/Fail không khớp | Mở | | | |
| M-25 | Answer key mỗi đề cần những gì? | Đã trả lời | Vẫn có baseline để đối chiếu, giữ cấu trúc như v0.3, gồm cả danh sách bug cài sẵn và severity. Đã khôi phục `baseline.template.json` | Chat | 2026-10-19 |
| M-26 | Các tiêu chí v0.3 không còn trong v0.4 là cố ý bỏ? | Đã trả lời | Cố ý bỏ; sẽ bổ sung sau | Chat | 2026-10-19 |
| M-27 | Bài đã chấm theo v0.3: quy đổi hay bỏ? | Đã trả lời | Quy đổi sang thang mới. Chưa làm được: chờ M-02 và judge mới (xem "Việc cần làm") | Chat | 2026-10-19 |
| M-28 | A4 "một nguồn duy nhất": nội dung dùng chung giữa nhiều skill đặt ở đâu? | Mở | | | |
| M-29 | Bài manual có bug report (và baseline có bug cài sẵn, M-25), nhưng "Defect Analysis & Reporting" không nằm trong 4 competency của manual. Phần bug report có được chấm không, và thuộc competency nào? | Đã trả lời | Có: bài manual chấm cả bug report. Đã thêm `defect-analysis-reporting` vào competency của manual (thành 5) | Chat | 2026-10-21 |
| M-30 | T-05's B1-B4 Provenance chỉ đối chiếu `ai-original/<file>` với transcript — nhưng transcript cũng là file học viên tự export rồi nộp. Nếu quy trình thật không bắt transcript bằng hệ thống độc lập (platform/LMS tự ghi log phiên chat, học viên không sửa được), học viên có thể giả cả `ai-original/` lẫn transcript cho khớp nhau, judge không có cách nào phát hiện. Quy trình thi thật hiện tại transcript được thu thập thế nào — có tamper-proof không? | Mở | | | |

### Auto (`Intermediate_auto`)

Các câu M-01…M-23 về scoring chung cũng áp dụng cho auto. Nhóm A của auto dùng y hệt manual (`_shared/skill-standard.json`), nên câu hỏi về nhóm A chỉ theo dõi ở phần manual (vd M-09).

| ID | Câu hỏi (tóm tắt) | Trạng thái | Câu trả lời / quyết định | Nguồn | Ngày |
|---|---|---|---|---|---|
| AU-01 | Quy đổi Pass/Fail sang thang 1–5 | Gộp vào M-02 | Thang 1–5 cũng bỏ cho auto (đã xóa `score_scale` khỏi `auto-qa/criteria.json`). Cách quy đổi Đạt/Không đạt ra điểm và ngưỡng đạt theo dõi chung ở M-02 | Chat | 2026-10-19 |
| AU-02 | Cột H "Assessment (Pass/Fail)" để trống: dùng để làm gì? | Đã trả lời | Không cần quan tâm cột này; không nạp vào criteria | Chat | 2026-10-19 |
| AU-08 | B3/B6 của auto chấm trùng với nhóm A dùng chung (A3 và B3 cùng chấm trigger clause "Use when…") | Mở | | | |
| AU-09 | Học viên được chấm trên bao nhiêu sub-category? Ai chọn? | Mở | | | |
| AU-10 | 7 sub-category ứng với competency nào? | Mở | Một phần (2026-10-19, theo M-13): đã có danh sách 7 competency của khóa học; manual dùng 4. Chưa rõ: bài auto gồm những competency nào (có phải 3 còn lại: Automation Development, Test Maintenance, Defect Analysis & Reporting?) và 7 sub-category (TCD, FWG, SCR, REV, EXE, RES, DEF) ứng với competency nào | | |
| AU-11 | Nhóm C chấm thế nào với sub-category không ra script? | Mở | | | |
| AU-12 | Số lần chạy tối thiểu cho mỗi sub-category | Mở | | | |
| AU-13 | Đề thi có cung cấp môi trường thật cho B2/B5 không? | Mở | | | |
| AU-14 | B5 (trigger tự động) có đúng là mức Intermediate? | Mở | | | |
| AU-15 | B6 phụ thuộc B3/B5: một lỗi bị phạt 2 lần có cố ý? | Mở | | | |
| AU-16 | B6 Fail bullet 3 mâu thuẫn với ghi chú B4; Pass và Fail cùng xảy ra thì sao? | Mở | | | |
| AU-17 | Ghi chú "không ảnh hưởng Pass/Fail" ở B4 có ghi nhận không? | Mở | | | |
| AU-18 | B4 bỏ các tình huống ngoại lệ trong description có cố ý? | Mở | | | |
| AU-19 | B2 "khám phá ứng dụng thật": công cụ gì, giới hạn dữ liệu nào? | Đã trả lời | Dùng **Playwright CLI** (sửa 2026-10-21; câu trả lời trước là Playwright MCP). Chỉ dùng tài khoản test, dữ liệu test của môi trường test (theo AU-32) | Chat | 2026-10-21 |
| AU-20 | Ngưỡng chưa định nghĩa ở nhóm C | Mở | Một phần (2026-10-19, chat): "chỉnh sửa tối thiểu" (C3) = có README / hướng dẫn chạy ngắn; "lỗi quan trọng" = các lỗi liệt kê trong ngoặc ngay cạnh (C1: test pass nhầm, assert sai, flaky rõ ràng; C4: locator sai, assert thiếu, flaky). Còn mở: "chạy ổn định" / "flaky thường xuyên" (C1); "phần đáng kể của scope" (C2, chờ xác nhận) | | |
| AU-21 | Answer key cho đề auto đã có chưa? | Đã trả lời | Không có answer key cho đề auto. Bỏ qua phần này: không làm baseline cho auto, không theo đuổi các câu hỏi phụ về đáp án | Chat | 2026-10-21 |
| AU-22 | Dùng locator khác getByRole/getByTestId có làm Fail không? | Đã trả lời | Có: dùng CSS/XPath làm Fail C1. Ngoại lệ (2026-10-21, AU-36): được dùng XPath khi locator có sẵn của Playwright không hỗ trợ tốt | Chat | 2026-10-21 |
| AU-23 | C4 "giải thích được code": bằng chứng là gì, AI hay người chấm? | Đã trả lời | Người chấm làm phần này; AI assessor không chấm điều kiện đó | Chat | 2026-10-19 |
| AU-24 | Danh sách AI tool được phê duyệt và chính sách dữ liệu là tài liệu nào? | Mở | | | |
| AU-25 | Gate trùng với C4 (dùng output AI mà không validate)? | Đã trả lời | Không trùng. "Dùng AI output mà không validate" của gate chỉ nói về thông tin mật, nhạy cảm. C4 nói về dùng output AI mà không refine. Một lỗi chất lượng output chỉ tính ở C4, không Fail gate | Chat | 2026-10-19 |
| AU-26 | Gate do AI chấm hay người quyết định cuối cùng? | Mở | | | |
| AU-30 | C1: các locator hướng người dùng khác của Playwright (getByLabel, getByText, getByPlaceholder, getByAltText, getByTitle) có được dùng không, hay chỉ getByRole/getByTestId? | Đã trả lời | Được chấp nhận, nhưng phải chọn tối ưu theo độ ưu tiên về hiệu suất của từng loại built-in locator (bổ sung 2026-10-21). CSS vẫn Fail; XPath chỉ khi locator có sẵn không hỗ trợ tốt (AU-36) | Chat | 2026-10-21 |
| AU-31 | C1: thứ tự ưu tiên locator cụ thể là gì? Khóa học cố định, hay theo quy ước code của học viên trong `references/` (B3 SCR)? | Mở | Một phần (2026-10-21): chọn theo độ ưu tiên về hiệu suất của từng loại built-in locator (AU-30). Chưa có thứ tự cụ thể | | |
| AU-32 | B2 cho dùng dữ liệu thật / tài khoản không giới hạn khi khám phá bằng Playwright MCP, nhưng gate Fail khi "đưa thông tin mật/nhạy cảm vào AI". Dùng tài khoản thật khi khám phá có tính là vi phạm gate không? | Đã trả lời | Chỉ được dùng tài khoản test, dữ liệu test của môi trường test. Dùng tài khoản / dữ liệu thật khi khám phá là vi phạm gate | Chat | 2026-10-20 |
| AU-33 | Playwright Assessment (17 mục) kết hợp với C1–C4 thế nào khi chấm script (SCR)? | Mở | | | |
| AU-34 | Playwright Assessment chấm từng mục theo thang 1–5 (Poor…Excellent), phần đạt khi trung bình ≥ 3; khóa học đã bỏ thang 1–5 (M-01). Quy đổi thế nào? | Mở | | | |
| AU-35 | Mục "Understand the locator in Playwright and use the correct one" không có trọng số (và không có công thức điểm), nên không được tính. Có cố ý không? | Mở | | | |
| AU-36 | Playwright Assessment cho dùng XPath ("xpath should be clean"), nhưng AU-22 chốt CSS/XPath là Fail C1. Với SCR, quy tắc nào áp dụng? | Đã trả lời | Nếu locator có sẵn của Playwright không hỗ trợ tốt trường hợp đó và phải dùng XPath thì không Fail; XPath đó phải gọn (PW-INT-3). Các trường hợp khác dùng CSS/XPath vẫn Fail. Ngoại lệ chỉ áp dụng cho XPath; CSS selector luôn Fail (chat, 2026-10-21) | Chat | 2026-10-21 |
| AU-27 | Bộ bằng chứng cần nộp cho auto | Đã trả lời | Dùng evidence package của rubric cũ (5 mục + "thiếu bằng chứng thì điều kiện Fail", "screenshot/text dán không có transcript thì không tính"). Đã đưa vào `auto-qa/criteria.json` | Chat | 2026-10-19 |
| AU-28 | Tech stack cố định Playwright + TypeScript? | Đã trả lời | Có. Khóa học cố định Playwright + TypeScript, không dùng stack khác | Chat | 2026-10-19 |
| AU-29 | Ngưỡng nào của mô hình cũ cần giữ lại? | Đã trả lời | Không giữ ngưỡng nào của mô hình cũ. (Điều kiện "pass 3 lần liên tiếp" ở B4 SCR vẫn còn, vì nó nằm trong sheet mới `Intermediate_auto`, không phải lấy từ mô hình cũ) | Chat | 2026-10-19 |

## Việc cần làm

Việc phát sinh từ các câu đã trả lời. Cập nhật trạng thái ở bảng này: `Chưa làm`, `Đang làm`, `Xong`.

| # | Việc | Từ câu | Chờ | Trạng thái |
|---|---|---|---|---|
| T-01 | (Xong 2026-10-21: `agents/manual-qa-assessment-judge.md` viết lại, `scripts/merge_judge_results.py` kiểm tra và gộp kết quả) Dựng lại judge: trả kết quả theo từng điều kiện (thỏa / không thỏa + bằng chứng), đúng thứ tự `pass_when_all` + điều kiện sub-category; đề xuất skill nào thuộc competency nào, kèm lý do; không chấm các điều kiện trong `human_conditions`, trả về "pending" | M-05, M-07, M-13, AU-23 | M-06 (vẫn mở: judge ghi fail_when_any không có điều kiện tương ứng vào notes) | Xong |
| T-02 | (Xong 2026-10-21, trừ judge T-01; **M-11 xong 2026-10-24**: `render_assessment_report.py` giờ dùng trung bình điểm + ngưỡng ≥3/5 khi một competency có nhiều skill, thay vì "1 skill fail là cả tiêu chí fail"; test lại run-4 kết quả không đổi vì fixture hiện tại mỗi competency chỉ có 1 skill) Dựng lại `build_plan_from_profile.py` và `render_assessment_report.py` cho mô hình `weighted-pass-fail` (pass rule, điểm nhóm = trung bình, Option 2, B và C chấm theo từng competency); báo cáo ghi rõ skill → competency để trainer review; liệt kê các điều kiện chờ người chấm và cho người chấm điền kết quả | M-10, M-13, M-14, AU-23 | | Xong |
| T-03 | Sửa `import_baseline_xlsx.py`: danh sách `not_assessed` đang dùng ID tiêu chí v0.3 (B4, C5, C6) | M-25, M-26 | Biết tiêu chí mới nào dùng danh sách bug | Chưa làm |
| T-04 | (Xong một phần 2026-10-21: `scripts/convert_v03_results.py`, kết quả ở thư mục `converted/` cạnh mỗi file; điều kiện không có tương đương vẫn pending) Quy đổi kết quả đã chấm theo v0.3 sang thang mới: `test-fixtures/manual-qa-sample/expected/`, `test-fixtures/manual-qa-sample-review/expected/`, `evals/sample-review-run-1`, `evals/sample-review-run-2` | M-27 | T-01, T-02, M-02 | Chưa làm |
| T-05 | (Xong một phần 2026-10-24: bản nháp đề xuất ở `documents/T-05-draft-additional-criteria.md`, dựa trên nội dung gốc v0.3 từng tiêu chí; A8 xác nhận đã có tương đương, không cần làm thêm. Ưu tiên đề xuất: C5 Bug Finding Rate > B1-B4 Provenance > C7 No fabrication > A5/A6/C3/C4/C6) Bổ sung lại các tiêu chí v0.3 đã cố ý bỏ (A5, A6, A8, B1–B4, C3–C7 cũ) | M-26 | Course owner duyệt bản nháp rồi mới đưa vào `criteria.json` | Chờ course owner duyệt |
| T-06 | Course owner duyệt `skill-standard.md` và `SKILL.template.md` | M-09 | | Xong (2026-10-19, v1.0) |
| T-07 | Gửi `skill-standard.md` và `SKILL.template.md` cho học viên | M-09 | | Chưa làm |
| T-08 | Thay bug giả lập trong fixture `manual-qa-sim-pass` bằng bug thật: hiện agent đóng vai trainer cài bug vào trang demo tĩnh của US-VP02 và ghi danh sách bug vào `baseline/` của fixture | M-29 | Người dùng tự làm | Chưa làm |
| T-09 | (Xong 2026-10-24: thêm `profile_loader.check_plan_fresh()`, gọi ở đầu `render_assessment_report.py` và `merge_judge_results.py`; test cả plan mới và plan cũ) `merge_judge_results.py`/`render_assessment_report.py` không đối chiếu `criteria_sha256`/`shared_sources[].sha256` của `eval_plan.json` với profile hiện tại trước khi chạy; plan cũ (rule model đã đổi) gây crash sâu (`KeyError: 'min_ratio'`) thay vì báo lỗi rõ "plan cũ hơn profile, hãy build lại" | Rà soát repo 2026-10-24 | | Xong |
| T-10 | `profiles/manual-qa/criteria.json`: trường `"status"` vẫn ghi "chưa chạy được, pass threshold còn undecided" — đã lỗi thời từ khi `course-rules.json` có `pass_threshold`/`group_points` và chạy được từ run-1. (Kiểm tra lại: `auto-qa/criteria.json` status "not runnable" vẫn đúng, vì thiếu field `competencies`, AU-10 còn mở — không sửa.) | Rà soát repo 2026-10-24 | | Xong (2026-10-24) |
| T-11 | (Xong 2026-10-24) `build_plan_from_profile.py` docstring dùng từ "deduction" để mô tả cơ chế `proportional` (trừ điểm theo tỷ lệ điều kiện không thỏa) — trùng tên với mô hình điểm `scoring_model: "deduction"` cũ đã bỏ (2026-10-23), dễ gây nhầm lẫn khi đọc | Rà soát repo 2026-10-24 | | Xong |
| T-12 | (Xong 2026-10-24) `SKILL.md` mục "Reference files" thiếu liệt kê `agents/generic-quality-judge.md` và `scripts/check_consistency.py` (cả hai đang tồn tại và được trỏ tới từ nơi khác) | Rà soát repo 2026-10-24 | | Xong |
| T-13 | (Xong một phần 2026-10-24: sửa `check_file_references()` bỏ qua ví dụ trong bảng Markdown và `(vd ...)`/`(e.g. ...)` inline — `check_consistency.py` giờ chạy sạch, 0 false-positive; đã ghi vào SKILL.md Reference files là "chạy tay sau khi sửa bundle") `scripts/check_consistency.py` không được gọi từ đâu cả (không trong SKILL.md Workflow, không hook/CI) dù tài liệu nói "chạy mỗi khi bundle thay đổi". Còn mở: chưa gắn vào quy trình thật (hook/CI) để không ai quên chạy | Rà soát repo 2026-10-24 | | Xong một phần |
| T-14 | (Xong 2026-10-24: thêm `documents/README.md` ghi rõ 2 file xlsx là snapshot lịch sử, nguồn sống là `profiles/manual-qa|auto-qa/criteria.json`) `documents/QA_AI_Skills_Assessment_Rubric_MANUAL.xlsx` và `_AUTO.xlsx` có thể đã lệch với `criteria.json` hiện tại (nhiều lần đổi model từ khi tạo); cần xác nhận còn là nguồn hay chỉ lưu lịch sử, và ghi chú rõ trong `documents/` | Rà soát repo 2026-10-24 | | Xong |
| T-15 | (Xong 2026-10-24: thêm `<cellStyles>` vào `STYLES`; verify bằng openpyxl không còn warning) `render_assessment_report.py`: `STYLES` (dùng chung cho `write_xlsx` và `write_summary_xlsx`) thiếu khai báo `<cellStyles>` mặc định trong stylesheet XML, khiến openpyxl cảnh báo "Workbook contains no default style" khi mở lại file xuất ra | Rà soát repo 2026-10-24 | | Xong |

## 2026-10-18 — Nạp criteria `Intermediate_Manual` vào profile manual-qa

### Đã làm (chưa commit)

- Nguồn: `AI-enabled QA Program.xlsx`, sheet `Intermediate_Manual` (bản lưu lúc 19:40; Excel đang mở file nên các sửa đổi chưa lưu không được đọc). sha256 `ea4ebce4f14679508a055a3c588c493360688cbeb214455dce08aa319d0a9e20`.
- Xóa toàn bộ profile manual-qa v0.3 (mô hình điểm trừ: A1–A8, B1–B4, C1–C7, pass 70/100) cùng `baseline.template.json`.
- `evaluator/skills/skill-evaluator/profiles/manual-qa/criteria.json` v0.4-draft (`scoring_model: weighted-pass-fail`):
  - Nhóm A Skill Standard (0.2): A1–A4
  - Nhóm B AI Application & Enablement (0.5): B1–B6
  - Nhóm C QA Output Quality (0.3): C1–C4
  - Gate AI Safety & Responsible Use (0, pass/fail)
  - Description và Pass/Fail được dịch sang tiếng Anh. Mỗi tiêu chí có `source_cells`. Đã kiểm tra số điều kiện Pass/Fail của cả 14 tiêu chí khớp với sheet.
- `build_plan_from_profile.py` giờ từ chối profile có `scoring_model` khác `deduction` và báo lỗi rõ ràng.
- `references/assessment-profiles.md`: thêm mục "manual-qa profile v0.4" và trạng thái.
- **Chưa chạy được:** judge (`agents/manual-qa-assessment-judge.md`), `build_plan_from_profile.py`, `render_assessment_report.py`, `import_baseline_xlsx.py` và expected result của các fixture `test-fixtures/manual-qa-sample*` vẫn theo mô hình v0.3. Các bước này chờ các quyết định dưới đây.

### Cần clarify: scoring rules

Bối cảnh: `Intermediate_Manual` chỉ có Pass/Fail cho từng tiêu chí (cột H "Assessment (Pass)", cột I "Assessment (Fail)"). Còn công thức tính điểm (A23:A24) lại dùng số và ngưỡng 3. Sheet ẩn `Intermediate_bk` có thang 1–5 (A22:C28) và mô tả level 1–5 cho từng tiêu chí (cột H–L). Sheet mới nhất đã bỏ thang này.

**1. Thang điểm và cách quy đổi Pass/Fail**

- **M-01.** Thang 1–5 trong `Intermediate_bk` (1 Not Demonstrated, 2 Below Expectation, 3 Meets Intermediate Expectations, 4 Exceeds Expectations, 5 Exceptional) còn hiệu lực không?
- **M-02.** *(Viết lại 2026-10-19, sau khi M-01 bỏ thang 1–5, M-10 chốt trung bình cộng trong nhóm, M-14 chốt Option 2.)* Công thức Option 2: `Competency Score = A × 0.2 + B × 0.5 + C × 0.3` cho từng competency, PASS khi không competency nào có điểm < 3 (và gate AI Safety Pass). Điểm nhóm A, B, C là trung bình cộng điểm các tiêu chí trong nhóm (M-10). Nhưng mỗi tiêu chí chỉ cho ra Đạt hoặc Không đạt, nên còn phải chốt 2 điều:
  1. Đạt và Không đạt quy ra mấy điểm?
  2. Ngưỡng mới thay cho "< 3" là bao nhiêu? Số 3 vốn thuộc thang 1–5, nay thang này đã bỏ.

  Ví dụ một competency của một học viên: nhóm A đạt 3/4 tiêu chí, nhóm B đạt 4/6, nhóm C đạt 3/4.

  | Cách quy đổi | Điểm A | Điểm B | Điểm C | Competency Score | Ngưỡng cần chốt |
  |---|---|---|---|---|---|
  | Đạt = 1, Không đạt = 0 (điểm nhóm = tỷ lệ đạt) | 0.75 | 0.67 | 0.75 | 0.71 (71%) | vd không competency nào < 70% |
  | Đạt = 5, Không đạt = 0 (giữ được số 3 trong công thức) | 3.75 | 3.33 | 3.75 | 3.54 | "không competency nào < 3", tương đương ≥ 60% |

  Hai cách cho cùng thứ hạng, chỉ khác đơn vị. Điều thực sự cần chốt là **mỗi competency phải đạt bao nhiêu phần trăm** (theo trọng số) thì PASS.
- **M-03.** Level 4–5 đạt được bằng cách nào? Pass/Fail chỉ cho ra 2 mức. Nếu dùng lại mô tả level ở `Intermediate_bk` thì A1–A3 và B1–B6 có đủ 5 level, còn A4 và C1–C4 chỉ có level 3 và 5 (thiếu 1, 2, 4).
- **M-04.** **Mâu thuẫn ngưỡng:** nếu Pass = 3 thì điểm tối đa là 3.
  - Option 1 ("Final Score > 3") không ai đạt được.
  - Option 2 ("No Competency Score < 3") thì đạt được.
  - Ý định là "> 3" hay "≥ 3"?

**2. Điều kiện Pass/Fail trong một tiêu chí**

- **M-05.** "Đạt khi" có nghĩa là phải thỏa TẤT CẢ điều kiện không? Chỉ A1, A4, B1, B2, C1 ghi rõ "TẤT CẢ". A2, A3, B3–B6, C2–C4 chỉ ghi "Đạt khi".
- **M-06.** Danh sách Pass và danh sách Fail không phải là mặt trái của nhau. Ví dụ B3 có Fail "chỉ có một lần chạy làm bằng chứng", nhưng Pass không có điều kiện tương ứng. Nếu bài thỏa hết Pass nhưng dính một điều Fail thì tính sao? Bên nào ưu tiên?
- **M-07.** Có cho đạt một phần không (vd thỏa 5/6 điều kiện), hay một điều kiện trượt là Fail cả tiêu chí?
- **M-08.** Cột F "AI Assessor Need to Check" có tính điểm không? Cột này chỉ có ở A1, A2 (và C1, nhưng chỉ chép lại Objective). Nội dung F lại rộng hơn H/I, ví dụ:
  - A1: tên phản ánh đúng chức năng, thuật ngữ nhất quán, tên quá chung chung
  - A2: section bắt buộc, thứ tự theo template

  Trong khi H/I chỉ kiểm tra regex tên thư mục và frontmatter.
- **M-09.** "Skill template / skill standard" mà A2 nhắc tới là tài liệu nào? Open item ở dòng 36 ghi "Pre-condition: skill standard definition".

**3. Gộp điểm từ tiêu chí lên nhóm và tổng**

- **M-10.** Trong mỗi nhóm, các tiêu chí có trọng số bằng nhau (trung bình cộng) không? Ví dụ "AI Application" = trung bình B1–B6?
- **M-11.** *(Viết lại 2026-10-19 theo Option 2.)* Option 2 ghi "Skill Standard = Average of all skills for one competency", còn A1 ghi "Đạt khi TẤT CẢ skill thỏa".
  - Nhóm A có chấm theo từng skill (A1–A4 cho mỗi skill, gộp bằng trung bình cộng theo M-10) rồi lấy trung bình qua các skill của competency không?
  - Nếu có, câu "TẤT CẢ skill" của A1 có còn đúng không? Hay A1 cũng chỉ xét từng skill một?
  - Ví dụ: competency có 2 skill. Skill 1 đạt A1–A4 (điểm A = 1.0), skill 2 trượt A1 (điểm A = 0.75), vậy Skill Standard = 0.875? Hay A1 trượt cho cả competency vì không phải tất cả skill đều đạt?
- **M-12.** Option 1 ghi "Average of all competencies". Vậy:
  - Một bài thi gồm những competency nào? (Capability Framework Intermediate có 9 competency.)
  - Bài manual-QA hiện tại (clarification questions, TR, TC, bug report) ứng với competency nào?
  - B và C được chấm riêng cho từng competency rồi mới lấy trung bình?
- **M-13.** Option 2 *(bổ sung 2026-10-19: gộp các ý của M-12, vì Option 1 bị loại)*:
  - Dòng "AI Application/QA Output Quality" bị bỏ dở, chưa có định nghĩa. Có phải B và C được chấm riêng cho từng competency?
  - Một bài thi gồm những competency nào? (Capability Framework Intermediate có 9 competency.) Bài manual-QA hiện tại (clarification questions, TR, TC, bug report) ứng với competency nào?
  - "Average of all skills for one competency" cần biết skill nào thuộc competency nào. Ai khai báo mapping này (học viên, đề thi, hay trainer)?
- **M-14.** Chọn Option 1 hay Option 2? (Open item dòng 37.)
- **M-15.** Làm tròn: Final/Competency Score có làm tròn trước khi so với 3 không? Làm tròn mấy chữ số? Kết quả cuối chỉ là PASS/FAIL hay có kèm level?

**4. Gate AI Safety & Responsible Use**

- **M-16.** Gate chưa có điều kiện Pass/Fail (H20 trống, I20 chỉ ghi "Mandatory Pass/Fail Gate"; open item dòng 38).
- **M-17.** Gate do AI chấm hay người quyết định? Gate Fail thì tổng là FAIL bất kể điểm, đúng không?
- **M-18.** Gate có trùng với B2 không? B2 có điều kiện "Bảo vệ thông tin: không đưa dữ liệu nhạy cảm vào AI". Một vi phạm có bị tính ở cả hai chỗ không?

**5. N/A, thiếu bằng chứng, ngưỡng chưa định nghĩa**

- **M-19.** Tiêu chí không áp dụng (N/A) thì tính sao: bỏ khỏi trung bình, hay cho điểm mặc định? Ví dụ:
  - chỉ có 1 skill nên điều kiện "không trùng skill khác" của A3 không áp dụng
  - bài thi không có phần bug report
  - (v0.3 cho trọn điểm khi N/A.)
- **M-20.** Thiếu bằng chứng (không có transcript, chỉ 1 lần chạy cho B3) thì tính là Không đạt luôn, hay xử lý riêng (vd ghi "thiếu bằng chứng" và cho học viên nộp bổ sung)? *(Sửa 2026-10-19: bỏ phần nhắc anchor "No required evidence" của thang 1–5 vì thang đã bỏ.)*
- **M-21.** Bộ bằng chứng (evidence package) cho nhóm B và C4 gồm những gì? Transcript đầy đủ? Bao nhiêu lần chạy? Log kiểm chứng của C4?
- **M-22.** Các ngưỡng được nhắc tới nhưng chưa có giá trị:
  - C2: "thiếu sót nhỏ nằm trong ngưỡng cho phép"
  - B6: "công sức thấp hơn baseline", baseline đo thế nào?
  - B3: "nhất quán", nhất quán đến mức nào?
  - A3: "không trùng với skill khác trong khóa học", so với skill của học viên hay của cả khóa học?
- **M-23.** Tiêu chí nào cần người quyết định thay vì AI (vd ước tính công sức ở B6, đánh giá "rủi ro cao" ở B5)? Kết quả của AI là chính thức hay tạm thời?

**6. Nội dung tiêu chí ảnh hưởng tới điểm**

- **M-24.** C1 Accuracy không khớp:
  - Description (G15) nói về độ chính xác của output: không bịa, logic đúng, không vi phạm business rule.
  - H15/I15 lại chỉ chấm câu hỏi làm rõ so với điểm mơ hồ trong đáp án (chép từ C1 của v0.3).
  - Nếu giữ như vậy thì độ chính xác của TR/TC/bug report không được chấm ở đâu. Ý định là gì?
- **M-25.** Đáp án (answer key) mỗi đề cần những gì? C1 cần danh sách điểm mơ hồ có đánh dấu Bắt buộc, C2 cần AC/requirement trong scope. Có còn cần danh sách bug cài sẵn và severity như v0.3 không?
- **M-26.** Các tiêu chí v0.3 không còn trong v0.4 là cố ý bỏ hay sẽ bổ sung lại?
  - A5 file references/assets phải được nhắc trong SKILL.md
  - A6 file đặt đúng thư mục
  - A8 không trùng lặp (một phần đã gộp vào A3)
  - B1–B4 bằng chứng skill tạo ra output
  - C3–C7 độ phủ TC, chất lượng expected result, tìm bug, chất lượng bug report, không bịa rule
- **M-27.** Các bài đã chấm theo v0.3 (`evaluator/evals/sample-review-run-1`, `-2`) và expected result trong fixtures có cần quy đổi sang thang mới không, hay bỏ?
- **M-28.** *(Thêm 2026-10-19, phát sinh khi viết `skill-standard.md`.)* A4 yêu cầu mỗi nội dung chỉ có một nguồn, và Fail nếu "nhiều skill dùng chung một nội dung nhưng mỗi skill giữ một bản copy". Nhưng mỗi skill là một thư mục độc lập. Vậy nội dung dùng chung (vd hướng dẫn severity dùng cho cả skill phân tích lỗi và skill viết bug report) nên đặt ở đâu?
  - Một skill giữ file, các skill khác tham chiếu bằng đường dẫn tương đối (vd `../defect-analysis-reporting/references/severity-guide.md`)?
  - Hay có một thư mục dùng chung riêng?
  - Nếu skill được copy sang máy khác hoặc dùng riêng lẻ thì đường dẫn tham chiếu có còn chạy không?
- **M-29.** *(Thêm 2026-10-19, phát sinh từ câu trả lời M-13.)* Bài manual ứng với 4 competency: Requirements Analysis, Test Design, Test Case Generation, Test Data Generation. Nhưng bài manual hiện tại có cả bug report (fixture `manual-qa-sample` có skill `defect-analysis-reporting`), và baseline vẫn giữ danh sách bug cài sẵn kèm severity (M-25).
  - Phần bug report của bài manual có được chấm không?
  - Nếu có, nó thuộc competency nào? Thêm "Defect Analysis & Reporting" vào bài manual, hay chấm ở bài auto?
  - Nếu không, skill bug report của học viên manual xử lý thế nào khi AI agent phân loại skill theo competency?

## 2026-10-18 — Nạp criteria `Intermediate_auto` vào profile auto-qa

### Đã làm (chưa commit)

- Nguồn: `AI-enabled QA Program - automation side.xlsx`, sheet `Intermediate_auto` (bản lưu lúc 22:45). sha256 `e9a7a9ee363cca022ebfe630856d5a13640a7a59f2eb4523e2b3da41188b1dbd`.
- Xóa toàn bộ profile auto-qa v0.1 (mô hình maturity level 1–5 theo 7 sub-category, 0.8 skill / 0.2 output, lấy từ `QA_AI_Skills_Assessment_Rubric_AUTO.xlsx`).
- `evaluator/skills/skill-evaluator/profiles/auto-qa/criteria.json` v0.2-draft (`scoring_model: weighted-pass-fail`):
  - Cùng nhóm, trọng số, gate và 2 option tính điểm như manual-qa v0.4.
  - Thêm `score_scale` 1–5 (sheet này có bảng A22:C28).
  - B1–B5 có điều kiện chung + `by_sub_category` cho 7 sub-category: TCD, FWG, SCR, REV, EXE, RES, DEF.
  - Đã kiểm tra số điều kiện Pass/Fail và đủ 7 sub-category của từng tiêu chí khớp với sheet.
- `references/assessment-profiles.md`: viết lại mục auto-qa.
- Không đụng tới `documents/`: thư mục này chỉ chứa file rubric gốc (xlsx) và bản đề xuất `AI_QA_Competency_Scoring_Matrix.md`, không phải criteria đã nạp vào evaluator.

### Cần clarify: auto-qa

Các câu hỏi chung về scoring ở phần manual (M-01…M-23: thang điểm, Pass/Fail, gộp điểm, Option 1/2, làm tròn, N/A, thiếu bằng chứng) cũng áp dụng cho auto. Dưới đây là các điểm riêng của sheet `Intermediate_auto`.

**1. Thang điểm và quy đổi**

- **AU-01.** Sheet có bảng 1–5 (A22:C28), nhưng tiêu chí chỉ có Pass/Fail. Quy đổi thế nào? Nếu Pass = 3 thì Option 1 ("Final Score > 3") không ai đạt được (giống manual).
- **AU-02.** Cột H "Assessment (Pass/Fail)" để trống ở mọi tiêu chí trừ gate. Cột này để assessor ghi kết quả, hay còn thiếu nội dung?

**2. Sub-category và competency**

- **AU-09.** Một học viên được chấm trên 1 sub-category, nhiều sub-category, hay cả 7? Ai chọn?
- **AU-10.** 7 sub-category ứng với competency nào trong Capability Framework (vd "AI-assisted Automation Development", "Test Maintenance")? Option 1 lấy "average of all competencies", Option 2 tính "per competency". Sub-category có phải là competency không?
- **AU-11.** Nhóm A, C và B6 không có biến thể theo sub-category. C1–C4 viết cho Playwright script (script chạy, locator, POM, rerun). Vậy với TCD (file thiết kế), REV (báo cáo review), EXE (kế hoạch chạy), RES (báo cáo kết quả), DEF (bug report) thì chấm C thế nào?
- **AU-12.** B1 "mỗi lần chạy giao đủ deliverable": cần bao nhiêu lần chạy? B3 cần 2 lần để so cấu trúc; B4 SCR cần pass 3 lần liên tiếp. Có phải tối thiểu 2 lần cho mọi sub-category?

**3. Nhóm B**

- **AU-08.** B3 và B6 của auto chấm trùng với nhóm A dùng chung:
  - B3: trigger clause, assets/references, không đưa dữ liệu project vào skill (A3 cũng chấm trigger clause "Use when…", A4 cũng chấm không gắn cứng dữ liệu project)
  - B6: đặt tên theo deliverable (A1 cũng chấm tên skill)

  Một lỗi có bị trừ ở cả A và B không?
- **AU-13.** B2 và B5 cần môi trường thật:
  - B2: ứng dụng thật, repo, báo cáo cũ, bug list
  - B5: trigger trong repo, CI, merge request, lịch chạy, bug tracker (ADO), kênh chat

  Đề thi có cung cấp các thứ này không? Nếu không, mọi học viên đều Fail B5, kéo theo Fail B6.
- **AU-14.** B5 (chạy tự động theo trigger, handoff không cần người) trong rubric cũ thuộc level 4–5 ("Supervised"/"Autonomous"). Có đúng là yêu cầu này nằm ở mức Intermediate?
- **AU-15.** B6 Pass yêu cầu B3 và B5 đều Pass. Như vậy một lỗi ở B3/B5 bị phạt 2 lần. Có cố ý không?
- **AU-16.** B6: Fail bullet 3 ("không có cảnh báo hoặc danh sách câu hỏi còn mở") mâu thuẫn với ghi chú ở B4 ("danh sách câu hỏi còn mở … không ảnh hưởng Pass/Fail"). Ngoài ra, nếu đạt 2/3 mục SHOULD nhưng dính một Fail bullet (vd bullet 1) thì kết quả là gì?
- **AU-17.** B4: "Lưu ý (không ảnh hưởng Pass/Fail)" có cần ghi nhận trong báo cáo không, hay bỏ qua?
- **AU-18.** B4 chỉ có self-check của agent. Các tình huống ngoại lệ trong description G12 (thiếu input, thông tin mâu thuẫn, kết quả không xác minh được) không còn được chấm. Có cố ý không?
- **AU-19.** B2 "khám phá ứng dụng thật": dùng công cụ gì (Playwright MCP, browser)? Có giới hạn nào về dữ liệu thật/tài khoản (liên quan gate) không?

**4. Nhóm C**

- **AU-20.** Các ngưỡng chưa định nghĩa:
  - "chạy ổn định", "flaky thường xuyên": bao nhiêu lần chạy, tỷ lệ fail bao nhiêu? Có dùng chung ngưỡng "pass 3 lần liên tiếp" của B4 SCR không?
  - "phần đáng kể của scope"
  - "chỉnh sửa tối thiểu"
  - "lỗi quan trọng"
- **AU-21.** C2 cần danh sách requirement/test case trong scope và edge case quan trọng, tức là cần đáp án cho từng đề. Rubric cũ ghi chưa có bài tập/đáp án cho auto. Hiện đã có chưa?
  - *(Bổ sung 2026-10-20.)* Hướng đang cân nhắc: auto không có đáp án sẵn. Nếu chốt như vậy thì cần quyết định:
    - C2 "mọi requirement / test case trong scope có ít nhất một Playwright test": scope lấy từ đâu? Có phải là danh sách requirement / manual test case mà đề đưa cho học viên (chấm bằng truy vết), không cần đáp án riêng?
    - C2 "edge case quan trọng", "risk quan trọng" và AU-20 "phần đáng kể của scope": không có đáp án thì AI assessor tự đánh giá rồi trainer review, hay bỏ các điều kiện này với auto?
    - `baseline.template.json` (M-25) chỉ dùng cho manual; auto không cần file đáp án.
  - *(2026-10-21.)* Đã chốt: không có answer key cho auto; bỏ qua phần này. Các câu hỏi phụ ở trên không theo đuổi nữa.
- **AU-22.** C1 "locator chính xác (ưu tiên getByRole/getByTestId)": dùng locator khác (CSS/XPath) có làm Fail không?
- **AU-23.** C4 "giải thích được code đã nộp": bằng chứng là gì (ghi chú, phỏng vấn)? AI assessor có chấm được không, hay cần người?
- **AU-30.** *(Thêm 2026-10-19, phát sinh từ câu trả lời AU-22.)* AU-22 chốt dùng CSS/XPath là Fail C1. Nhưng Playwright còn các locator hướng người dùng khác ngoài getByRole/getByTestId: `getByLabel`, `getByText`, `getByPlaceholder`, `getByAltText`, `getByTitle`. Các locator này có được chấp nhận không, hay mọi locator không phải getByRole/getByTestId đều Fail?
- **AU-31.** *(Thêm 2026-10-20, phát sinh từ AU-30.)* AU-30 cho dùng các locator hướng người dùng khác nếu "hợp lý và có độ ưu tiên". Thứ tự ưu tiên cụ thể là gì?
  - Khóa học cố định một thứ tự. Ví dụ thứ tự Playwright khuyến nghị: getByRole → getByLabel → getByPlaceholder → getByText → getByAltText → getByTitle → getByTestId. Nhưng sheet lại ghi "ưu tiên getByRole/getByTestId".
  - Hay theo quy ước code Playwright của học viên trong `references/`? (B3 của SCR yêu cầu `references/` có "thứ tự locator".)
- **AU-32.** *(Thêm 2026-10-20, phát sinh từ AU-19.)* AU-19: khám phá ứng dụng thật bằng Playwright MCP, không giới hạn dữ liệu thật / tài khoản. Nhưng gate AI Safety Fail khi "đưa thông tin mật/nhạy cảm vào AI", và Playwright MCP đưa nội dung trang, tài khoản đăng nhập vào AI.
  - Dùng tài khoản thật / dữ liệu thật khi khám phá có được miễn khỏi gate không?
  - Hay chỉ được dùng tài khoản test, dữ liệu test của môi trường test?
- **AU-33.** *(Thêm 2026-10-21, khi nạp `[Level 1] Playwright Assessment.xlsx`.)* Output của script tự động (SCR) chấm theo Playwright Assessment Level 1 của công ty. Nhưng nhóm C của auto đã có C1–C4. Hai bộ kết hợp thế nào?
  - (a) Dùng 17 mục làm điều kiện chi tiết của C1–C3 khi chấm SCR, giữ C4. Ánh xạ đề xuất:
    - C1 Accuracy: PW-INT-2 (hiểu và dùng đúng locator), PW-INT-3 (locator ổn định, hiệu năng tốt), PW-INT-4 (dynamic locator), PW-SD-2 (tránh sleep, hardcode), PW-DES-1 (checkpoint đúng, không pass/fail sai).
    - C2 Completeness: PW-SD-3 (chuẩn bị, dọn dẹp test data / môi trường).
    - C3 Usability & Format: PW-INT-1, PW-SD-1, PW-SD-4 (chạy song song), PW-SD-5, PW-SD-6, PW-SD-7, PW-DES-2, PW-DES-3 (dùng method của Page Object), PW-CFG-1, PW-CFG-2, PW-CFG-3.
    - C4 Human Validation: không có mục tương ứng.
  - (b) Với SCR, thay C1–C3 bằng 4 phần của Playwright Assessment, giữ C4.
  - (c) Giữ nguyên C1–C4, thêm Playwright Assessment như một điều kiện riêng: cả 4 phần đều Qualified.
- **AU-34.** Playwright Assessment chấm từng mục theo thang 1–5 (Poor 1, Need to improve 2, Meet 3, Very Good 4, Excellent 5), có trọng số. Điểm phần = trung bình có trọng số, Qualified khi ≥ 3. Mục dưới Meet phải có comment. Khóa học đã bỏ thang 1–5 (M-01) và chấm Đạt/Không đạt.
  - Quy đổi thế nào? Ví dụ mục "thỏa" khi đạt Meet trở lên, phần "thỏa" khi Qualified?
  - Hay giữ thang 1–5 riêng cho phần này?
  - Không có công thức tổng cho cả 4 phần: phải cả 4 phần Qualified mới đạt?
  - Ai chấm điểm từng mục: AI assessor rồi trainer review, hay trainer?
- **AU-35.** Mục PW-INT-2 "Understand the locator in Playwright and use the correct one" để trống trọng số và không có công thức điểm, nên công thức của sheet bỏ qua mục này. Có cố ý không, hay thiếu trọng số?
- **AU-36.** PW-INT-3 ghi "in case of using xpath, xpath should be clean", tức là cho dùng XPath. Nhưng AU-22 chốt dùng CSS/XPath là Fail C1. Khi chấm SCR, quy tắc nào được áp dụng? Có liên quan AU-31 (thứ tự ưu tiên locator).

**5. Gate AI Safety & Responsible Use**

- **AU-24.** Gate đã có điều kiện, nhưng danh sách "AI tool được phê duyệt" và "chính sách xử lý dữ liệu của công ty" là tài liệu nào? AI assessor kiểm tra bằng cách nào?
- **AU-25.** "Dùng AI output mà không validate" trùng với C4 ("dùng nguyên output AI mà không chạy/không review"). Một lỗi vừa Fail gate vừa Fail C4?
- **AU-26.** Gate do AI chấm hay người quyết định cuối cùng?

**6. Bằng chứng và phạm vi**

- **AU-27.** Bộ bằng chứng cần nộp là gì? (Rubric cũ có `evidence_package`: thư mục skill, transcript đầy đủ, file output, run log, git history/MR.) Sheet mới không nêu.
- **AU-28.** Tech stack cố định là Playwright + TypeScript? Học viên dùng stack khác thì sao?
- **AU-29.** Mô hình cũ (maturity level 1–5 theo skill/output, 0.8/0.2, target 3.0, các ngưỡng đề xuất: 3 lần pass liên tiếp, ≥5 lần chạy trước, ≥2 lần chạy bằng trigger, ≥90% của 10 mục) đã bỏ hẳn. Có ngưỡng nào cần giữ lại cho mô hình mới không?

## 2026-10-18 — Dùng chung nhóm A cho manual và auto

### Quyết định

Nhóm A (Skill Standard) của auto giống y hệt manual. Bản gốc là text của sheet `Intermediate_Manual`; text A1–A4 của sheet `Intermediate_auto` không dùng nữa.

### Kiến trúc (chưa commit)

- `profiles/_shared/skill-standard.json`: fragment chứa group A (weight 0.2) và A1–A4. Sửa nhóm A **chỉ ở đây** và tăng `version`.
- `profiles/manual-qa/criteria.json` (v0.5) và `profiles/auto-qa/criteria.json` (v0.3) không còn tự chứa A. Cả hai trỏ tới fragment bằng `{"$ref": "../_shared/skill-standard.json"}` trong `groups`.
- `scripts/profile_loader.py`:
  - `load_profile()` thay mỗi `$ref` bằng group và criteria của fragment.
  - Từ chối nếu fragment thiếu file hoặc thiếu field, hoặc nếu profile tự định nghĩa lại group/criterion của fragment (không cho override cục bộ).
  - Chạy `python scripts/profile_loader.py profiles/manual-qa profiles/auto-qa` để xem kết quả resolve.
- `build_plan_from_profile.py` đọc profile qua loader. Plan ghi thêm `shared_sources[]` (path, sha256, version của từng fragment), nên sửa fragment sau khi đã chấm cũng phát hiện được.
- Đã kiểm tra: hai profile resolve ra A1–A4 giống hệt nhau. Các lỗi (thiếu fragment, định nghĩa trùng group/criterion) đều bị chặn.
- Cập nhật `references/assessment-profiles.md` (mục "Shared criteria") và `SKILL.md`.

### Có thể dùng chung tiếp (chưa làm, chờ clarify)

- Gate AI Safety & Responsible Use: manual chưa có điều kiện, auto đã có. Nếu cùng một gate cho cả khóa thì tách thành fragment `_shared/` thứ hai.
- `scoring` (2 option) và `score_scale` 1–5: hiện chép ở cả hai profile. Khi chốt scoring rule thì nên đưa về một chỗ.

## 2026-10-18 — Bỏ thông tin nguồn Excel khỏi criteria.json

- Không script nào đọc các field này nên đã xóa khỏi `_shared/skill-standard.json`, `manual-qa/criteria.json` và `auto-qa/criteria.json`:
  - `source` (tên workbook, sheet, sha256, ghi chú dịch)
  - `source_cells` của từng group, criterion, gate, scoring, score_scale
  - `open_items` (open item chép từ sheet + điểm mơ hồ khi nạp)
- Các status còn nhắc ô Excel ("H20", "row 37") được viết lại, không còn tham chiếu sheet.
- Thông tin nguồn (workbook, sheet, sha256) và danh sách điểm mơ hồ giờ chỉ còn trong work log này. Các dòng "Mỗi tiêu chí có `source_cells`" ở các mục trên không còn đúng.
- Version các file không đổi, vì nội dung tiêu chí không đổi.

## 2026-10-18 — Thêm bảng theo dõi trạng thái câu hỏi

- Mỗi câu hỏi có ID cố định (M-01…M-27, AU-01…AU-29), thay cho số thứ tự cũ.
- Trạng thái chỉ ghi ở bảng "Theo dõi câu hỏi cần clarify" đầu file; các ghi chú "→ Đã giải quyết" trước đây nằm trong câu hỏi đã chuyển vào bảng.
- Hiện tại: manual 27 câu mở. Auto: 1 đã trả lời (AU-06), 3 không còn áp dụng (AU-03, AU-04, AU-07), 1 gộp vào M-09 (AU-05), 24 câu mở.

## 2026-10-18 — Bỏ câu hỏi về nhóm A của auto

- Auto dùng y hệt nhóm A của manual, nên đã bỏ AU-03…AU-07 (phần "Nhóm A (Skill Standard)" của auto và AU-03 ở phần thang điểm). Câu hỏi về nhóm A chỉ theo dõi ở manual (vd M-09). Các ID này không dùng lại.
- Giữ AU-08 (B3/B6 của auto chấm trùng với nhóm A dùng chung) và chuyển sang mục "Nhóm B" của auto, vì chuyện chấm trùng vẫn còn sau khi dùng chung nhóm A.
- Đánh lại số các mục của auto (1–6).
- Hiện tại: manual 27 câu mở; auto 24 câu mở.

## 2026-10-19 — Trả lời M-01

- M-01: thang 1–5 của `Intermediate_bk` **không còn hiệu lực**.
- Hệ quả:
  - M-03 (level 4–5) → Không còn áp dụng.
  - M-04 (ngưỡng "> 3" hay "≥ 3") → Gộp vào M-02, vì số 3 trong công thức phải định nghĩa lại.
  - M-02 được viết lại rõ hơn, có ví dụ tính điểm.
  - M-20 bỏ phần nhắc anchor của thang 1–5.
- Còn treo: sheet `Intermediate_auto` vẫn có bảng 1–5 (A22:C28), và `auto-qa/criteria.json` đang lưu nó trong `score_scale`. Chưa rõ quyết định M-01 có áp dụng cho auto không (liên quan AU-01).

## 2026-10-19 — Bỏ thang 1–5 cho auto

- Quyết định M-01 (bỏ thang 1–5) áp dụng cho cả auto.
- Đã xóa `score_scale` khỏi `auto-qa/criteria.json` và tăng version lên 0.4-draft. Không script nào đọc field này.
- `references/assessment-profiles.md`: bỏ dòng `score_scale` ở mục auto-qa và cập nhật version.
- AU-01 → Gộp vào M-02: cách quy đổi Đạt/Không đạt và ngưỡng đạt dùng chung cho manual và auto.
- Mục "Còn treo" ở entry "Trả lời M-01" đã xong.

## 2026-10-19 — Trả lời M-05

- M-05: phải thỏa **tất cả** điều kiện Pass mới Đạt. Áp dụng cho mọi tiêu chí của cả manual và auto, kể cả các tiêu chí sheet chỉ ghi "Đạt khi" (A2, A3, B3–B6, C2–C4).
- Hệ quả: M-07 (có cho đạt một phần không) → Đã trả lời: không, một điều kiện không thỏa là Không đạt cả tiêu chí.
- M-06 vẫn mở: thỏa hết điều kiện Pass nhưng dính một điều kiện Fail thì kết quả là gì?
- Đã thêm `pass_rule` (tất cả điều kiện phải thỏa, không có đạt một phần) vào `manual-qa/criteria.json` (v0.6-draft) và `auto-qa/criteria.json` (v0.5-draft). Ở auto, B6 vẫn dùng rule riêng (B3 và B5 Đạt + ít nhất 2/3 mục SHOULD).
- `references/assessment-profiles.md`: thêm mô tả `pass_rule`, cập nhật version.

## 2026-10-19 — Pass rule cấu hình được (M-07)

### Quyết định

M-07: hiện tại một điều kiện không thỏa là Không đạt cả tiêu chí. Nhưng kiến trúc phải cho phép đổi sang "đạt một phần" sau này mà không phải sửa nhiều chỗ.

### Kiến trúc (chưa commit)

- **Judge không tự quyết Đạt/Không đạt.** Judge chỉ báo từng điều kiện: thỏa hay không, kèm bằng chứng. Code (`scripts/criterion_rules.py`) tính verdict và điểm từ đó theo `pass_rule`. Đổi rule là đổi dữ liệu: không sửa prompt của judge, và kết quả đã chấm (theo từng điều kiện) tính lại được theo rule mới mà không phải chấm lại.
- **Rule mặc định của khóa học nằm ở một chỗ:** `profiles/_shared/course-rules.json` → `settings.pass_rule = {"mode": "all"}`. Cả hai profile kéo vào bằng `"extends": ["../_shared/course-rules.json"]` (manual v0.7-draft, auto v0.6-draft). Profile không được tự định nghĩa lại key đã có trong file dùng chung.
- **Các mode có sẵn:**
  - `{"mode": "all"}`: thỏa hết mới Đạt (đang dùng).
  - `{"mode": "at_least", "min_met": 5}` hoặc `{"mode": "at_least", "min_ratio": 0.8}`: đạt một phần, tính theo số lượng hoặc tỷ lệ điều kiện thỏa.
  - `{"mode": "proportional", "min_ratio": 0.6}`: chấm điểm một phần (điểm = số thỏa / tổng), Đạt khi ≥ ngưỡng.
  - Tùy chọn: `requires_pass_of` (phải Đạt tiêu chí khác trước), `conditions: "should_items"`.
- **Ghi đè theo phạm vi:** tiêu chí > nhóm > khóa học. Hiện chỉ B6 của auto có rule riêng (`at_least` 2/3 should_items, `requires_pass_of` B3 và B5), nên đổi rule chung không ảnh hưởng B6.
- **Muốn đổi sang đạt một phần cho cả khóa:** sửa đúng một dòng `settings.pass_rule` trong `course-rules.json` và tăng `version`. Loader sẽ kiểm tra rule hợp lệ (mode đúng, có ngưỡng, `requires_pass_of` trỏ đúng tiêu chí).
- **Xem rule đang áp dụng cho từng tiêu chí:** `python scripts/criterion_rules.py profiles/manual-qa profiles/auto-qa`.
- `profile_loader.py` hỗ trợ thêm `extends` và kiểm tra pass rule khi load. Plan ghi sha256 của `course-rules.json` như các file dùng chung khác.
- Đã kiểm tra bằng 21 test (chạy ngoài repo): đủ các mode; đổi `course-rules.json` sang `at_least` thì cả hai profile cùng đổi, còn B6 giữ rule riêng; B6 Không đạt khi B5 Không đạt; tiêu chí có sub-category bắt buộc phải nêu sub-category; các lỗi cấu hình đều bị chặn.
- Cập nhật `references/assessment-profiles.md` (mục "Shared criteria and course rules", mục mới "Pass rules") và `SKILL.md`.

### Chưa làm

- Judge (khi dựng lại) phải trả kết quả theo từng điều kiện, đúng thứ tự `pass_when_all` + điều kiện của sub-category.
- Pass rule chỉ quyết verdict và điểm của từng tiêu chí. Cách gộp lên nhóm và tổng vẫn chờ M-02, M-10, M-14.
- M-06 (dính điều kiện Fail thì sao) có thể thêm vào cùng chỗ (vd `fail_when_any` trong rule) khi có câu trả lời.

## 2026-10-19 — Trả lời M-08

- M-08: không cần quan tâm cột F "AI Assessor Need to Check". Cột này không tính điểm; chỉ chấm theo điều kiện Pass/Fail.
- Đã xóa `assessor_checks` (dữ liệu của cột F) khỏi criteria, để judge sau này không nhầm nó là điều kiện chấm:
  - `_shared/skill-standard.json` → v0.2-draft (A1, A2 có dữ liệu)
  - `manual-qa/criteria.json` → v0.8-draft
  - `auto-qa/criteria.json` → v0.7-draft
- `references/assessment-profiles.md`: ghi rõ cột F không được nạp, cập nhật version.

## 2026-10-19 — Trả lời M-10, M-14 (Option 2), cập nhật M-11, M-12

- M-10: các tiêu chí trong nhóm có trọng số bằng nhau. Điểm nhóm = trung bình cộng điểm các tiêu chí (vd B = trung bình B1–B6).
- M-14: **Option 1 đã bị loại, chỉ dùng Option 2** (chấm theo từng competency).
- M-11 vẫn mở, viết lại theo Option 2: Option 2 vẫn ghi "Average of all skills for one competency", nên vẫn cần chốt nhóm A có chấm theo từng skill không, và câu "TẤT CẢ skill" của A1 xử lý thế nào. Phần gộp A1–A4 trong một skill đã rõ nhờ M-10.
- M-12 (competency trong Option 1) → Gộp vào M-13; M-13 bổ sung các ý đó cho Option 2.
- M-02 viết lại theo công thức Option 2 (ngưỡng "không competency nào < 3").
- Criteria:
  - `scoring` chuyển từ hai profile vào `_shared/course-rules.json` (v0.2-draft), chỉ giữ Option 2: `option: 2`, `group_score: "mean"`, `criterion_score: null` và `pass_threshold: null` (chờ M-02).
  - `manual-qa/criteria.json` → v0.9-draft, `auto-qa/criteria.json` → v0.8-draft (bỏ `scoring` riêng, cập nhật `status`).
- `references/assessment-profiles.md`: thêm mục "Scoring (course-wide)", bỏ các chỗ nhắc 2 option.

## 2026-10-19 — Trả lời M-25, M-26, M-27

- M-25: vẫn có baseline (answer key) để đối chiếu, giữ cấu trúc như v0.3, gồm cả danh sách bug cài sẵn và severity.
  - Đã khôi phục `profiles/manual-qa/baseline.template.json` từ git, nội dung giữ nguyên bản v0.3.
  - Các file `baseline.json` trong `test-fixtures/` vẫn dùng được.
  - Tiêu chí hiện tại dùng: điểm mơ hồ (C1) và AC trong scope (C2). Danh sách bug và các ngưỡng `ambiguity_with_tr_pct`, `bug_found_pct` giữ lại cho các tiêu chí sẽ bổ sung sau (M-26).
- M-26: các tiêu chí v0.3 bị bỏ là **cố ý**, sẽ bổ sung sau → việc T-05.
- M-27: kết quả đã chấm theo v0.3 sẽ **quy đổi sang thang mới**, không bỏ. Chưa làm được ngay, vì cách quy đổi Đạt/Không đạt ra điểm (M-02) và judge mới (T-01) chưa có → việc T-04.
- Thêm bảng "Việc cần làm" (T-01…T-05) ở đầu file, để theo dõi việc phát sinh từ các câu đã trả lời, tách khỏi bảng câu hỏi.
- `references/assessment-profiles.md`: cập nhật mục blocker (baseline giữ cấu trúc v0.3; kết quả v0.3 sẽ được quy đổi).

## 2026-10-19 — Tạo skill standard cho nhóm A (M-09)

- M-09: chưa có tài liệu skill standard, nên đã tạo mới (bản nháp 0.1, chờ course owner duyệt → T-06):
  - `profiles/_shared/skill-standard.md`: chuẩn đặt tên, cấu trúc thư mục, cấu trúc SKILL.md (frontmatter, description, quy trình), tái sử dụng, checklist tự kiểm tra. Viết bằng tiếng Việt, kèm ví dụ Đạt / Không đạt.
  - `profiles/_shared/SKILL.template.md`: SKILL.md mẫu để copy. Không đặt tên `SKILL.md` để không vi phạm A1 và không bị nhầm là một skill.
- Mỗi quy tắc gắn nhãn **[Bắt buộc · Ax]** (được chấm ở A1–A4) hoặc **[Khuyến nghị]** (không chấm ở nhóm A). Tài liệu chỉ diễn giải đúng các điều kiện A1–A4 hiện có, không thêm điều kiện chấm mới. Các mục khuyến nghị được chấm ở nhóm khác thì ghi rõ (auto-qa B3, B6).
- `skill-standard.json` → v0.3-draft: group A có thêm `standard` trỏ tới hai file trên. File JSON vẫn là nguồn chấm chính thức; khi sửa quy tắc thì sửa cả hai file và tăng version.
- `references/assessment-profiles.md`: thêm mô tả hai file.
- Đã kiểm tra (script chạy ngoài repo):
  - Template sau khi copy vào thư mục `your-skill-name/` đạt các kiểm tra tự động của A1–A3 (tên, frontmatter, description, quy trình).
  - Thư mục tên sai (`Bad_Name`) bị bắt lỗi A1/A2.
  - Hai skill mẫu trong fixture cũng đạt.
  - Bảng ví dụ tên trong tài liệu khớp với regex.
  - A4 cần đánh giá ngữ nghĩa nên không kiểm tra tự động.
- Câu hỏi mới phát sinh: M-28 (nội dung dùng chung giữa các skill đặt ở đâu).

## 2026-10-19 — Phát hành skill standard v1.0

- Course owner duyệt skill standard → phát hành **v1.0**:
  - `profiles/_shared/skill-standard.md`: 0.1-draft → 1.0, trạng thái "đã duyệt".
  - `profiles/_shared/skill-standard.json` (tiêu chí A1–A4): 0.3-draft → 1.0, để hai file cùng version.
  - `SKILL.template.md` không có số version riêng; nó đi kèm `skill-standard.md`.
- Trước khi phát hành đã rà tham chiếu ô Excel:
  - `skill-standard.md`, `SKILL.template.md`, `skill-standard.json` không có tham chiếu ô nào. "dòng 1" trong tài liệu là dòng 1 của SKILL.md; các tên `.xlsx` là tên file template.
  - Đã bỏ các chỗ "column H / column I / Column F" trong `references/assessment-profiles.md`. Evaluator không còn tham chiếu ô Excel nào.
  - Work log này vẫn giữ tham chiếu ô (vd H15, A22:C28) vì cần cho việc clarify với course owner.
- T-06 → Xong. Thêm T-07: gửi tài liệu cho học viên.
- Mục "Câu hỏi còn mở" trong `skill-standard.md` vẫn giữ (M-28, M-22). Khi có câu trả lời thì cập nhật tài liệu và tăng version (vd 1.1).

## 2026-10-19 — skill-standard.md v1.0.1: ghi rõ A1–A4 là gì

- Câu hỏi: "1. Đặt tên (A1, A2)" trong `skill-standard.md` là gì? → A1–A4 là mã tiêu chí chấm của nhóm A, không phải ô Excel:
  - A1 Naming Convention
  - A2 Structure Compliance
  - A3 Instruction Quality
  - A4 Reusability & Maintainability
- `skill-standard.md` → v1.0.1 (chỉ sửa câu chữ, không đổi quy tắc chấm):
  - Thêm bảng A1–A4 ở mục "Cách đọc": tên tiêu chí, chấm điều gì, mục nào trong tài liệu nói về nó.
  - Các heading ghi cả mã lẫn tên tiêu chí, vd "1. Đặt tên (A1 Naming Convention, A2 Structure Compliance)".
  - Ghi quy ước version: đổi quy tắc chấm thì tăng version của cả hai file (1.0 → 1.1); chỉ sửa câu chữ thì chỉ tăng số cuối của tài liệu (1.0 → 1.0.1).
- `skill-standard.json` giữ v1.0, vì quy tắc chấm không đổi.
- Work log tiếp tục giữ các tham chiếu ô Excel (theo yêu cầu).

## 2026-10-19 — Trả lời một phần M-22 (A3 không trùng skill)

- M-22, phần A3: "không trùng với skill khác" nghĩa là **các skill mà học viên nộp phải có description cho các task khác nhau, không có hai skill trùng lặp**. So sánh với các skill khác của chính học viên, không so với mọi skill trong khóa học.
- M-22 vẫn mở cho C2 (ngưỡng thiếu sót nhỏ), B6 (baseline công sức), B3 (mức nhất quán).
- Đây là thay đổi nội dung điều kiện chấm, nên tăng version của cả hai file (theo quy ước):
  - `skill-standard.json` → v1.1: điều kiện A3 đổi từ "does not overlap with any other skill in the course" thành "does not overlap with any other skill the trainee submitted: each skill covers a different task, and no two skills do the same job".
  - `skill-standard.md` → v1.1:
    - Mục 3.2 ghi rõ phạm vi so sánh, kèm cách kiểm tra: lấy một yêu cầu điển hình của skill này, xem nó có khớp description của skill kia không. Nếu hai skill dùng cùng đầu vào thì nên nêu ranh giới.
    - Checklist mục 6 được cập nhật.
    - Bỏ câu hỏi này khỏi mục "Câu hỏi còn mở".
- Ghi chú cho M-19: nếu học viên chỉ nộp 1 skill thì không có skill nào khác để trùng, nên điều kiện này tự thỏa. Cách xử lý N/A nói chung vẫn chờ M-19.

## 2026-10-19 — Trả lời M-13 (competency)

- M-13 → Đã trả lời:
  - B và C được chấm riêng cho từng competency.
  - Khóa học có 7 competency (đều "AI-assisted"):
    - Requirements Analysis
    - Test Design
    - Test Case Generation
    - Test Data Generation
    - Automation Development
    - Test Maintenance
    - Defect Analysis & Reporting
    
    Capability Framework Intermediate có thêm "AI Output Evaluation & Validation" và "AI-assisted QA Decision Making", nhưng hai competency này không nằm trong danh sách bài thi.
  - Bài manual ứng với 4 competency: Requirements Analysis, Test Design, Test Case Generation, Test Data Generation.
  - Skill nào thuộc competency nào: AI agent phân loại, ghi rõ trong báo cáo chấm cuối, trainer review.
- Câu hỏi mới phát sinh: M-29 (bài manual có bug report nhưng "Defect Analysis & Reporting" không nằm trong 4 competency của manual).
- AU-10 cập nhật một phần: đã có danh sách competency; chưa rõ bài auto gồm competency nào và 7 sub-category ứng với competency nào.
- Criteria:
  - `_shared/course-rules.json` → v0.3-draft:
    - thêm `competency_catalog` (7 competency, có id);
    - `scoring.per_competency`: A, B, C chấm theo từng competency;
    - `scoring.skill_to_competency`: judge phân loại, báo cáo ghi rõ, trainer review.
  - `manual-qa/criteria.json` → v0.10-draft: thêm `competencies` (4 id).
  - `profile_loader.py` kiểm tra `competencies` của profile phải nằm trong `competency_catalog`, không trùng, không rỗng. Đã thử: id sai chính tả và id trùng đều bị chặn.
  - `auto-qa` chưa có `competencies`, chờ AU-10.
- T-01 (judge) thêm việc đề xuất skill → competency; T-02 (báo cáo) thêm chấm B, C theo competency và ghi rõ mapping. T-02 giờ chờ M-02, M-11, M-29.
- `references/assessment-profiles.md`: thêm các dòng competency vào mục "Scoring (course-wide)", cập nhật version.

## 2026-10-19 — Skill standard v1.2: đặt thông tin ở đâu, A4 áp dụng cả thư mục skill

- Câu hỏi: trong skill template, đặc tả task và domain knowledge để ở đâu? → Skill chỉ chứa **cách làm**, phần dùng lại được cho mọi dự án:
  - Đặc tả task của một lần chạy (user story, AC…) là **đầu vào**, đưa vào lúc chạy.
  - Domain knowledge của dự án nằm **ngoài thư mục skill** (vd `docs/knowledge/` của dự án), skill nhận đường dẫn qua đầu vào `{knowledge_dir}`.
  - Kiến thức QA chung để ở `references/`; template đầu ra để ở `assets/`.
- Đã xác nhận đề xuất, sửa quy tắc chấm A4 → cả hai file lên **v1.2**:
  - `skill-standard.json`: điều kiện Pass đầu tiên của A4 đổi từ "SKILL.md contains no information hard-wired…" thành "The skill folder (SKILL.md, references/, assets/, scripts/) contains no information hard-wired…", và thêm "project business rules" vào danh sách. Lý do: điều kiện cũ chỉ nói SKILL.md, nên business rule của dự án đặt trong `references/` vẫn lọt.
  - `skill-standard.md`:
    - Mục 4: A4 áp dụng cho toàn bộ thư mục skill, thêm ví dụ business rule nằm trong `references/` là Không đạt.
    - Mục mới 4.1 "Đặt thông tin ở đâu": bảng loại thông tin → vị trí, phép thử "dùng cho dự án khác còn đúng không?", và ví dụ `## Inputs`.
    - Mục mới 6 "Thiếu thành phần thì trượt tiêu chí nào".
    - Checklist mục 8 và bảng A1–A4 cập nhật theo.
    - Câu "Template nằm ở `assets/`…" viết lại cho đúng điều kiện: chỉ trượt A4 khi template có hai bản.
  - `SKILL.template.md`: `## Inputs` có thêm `{task_input}` (đặc tả task) và `{knowledge_dir}` (domain knowledge của dự án). Bước 1 đọc cả hai. Hướng dẫn trong comment có thêm một bước về chỗ đặt thông tin.
- Trả lời "thiếu thành phần nào thì trượt tiêu chí nào" (đã đưa vào mục 6 của tài liệu):
  - Nhóm A chỉ chấm: tên thư mục, file SKILL.md (A1); frontmatter, `name`, `description` (A2); description có "Use when…", heading Process, các bước đánh số (A3); không gắn cứng thông tin dự án, mỗi nội dung một nguồn (A4).
  - `## Inputs`, `## Output`, `## Files`, `references/`, `assets/`, `scripts/` là tùy chọn với nhóm A. Riêng auto chấm một số mục này ở B3 và B6.
- Đã kiểm tra: template mới vẫn đạt các kiểm tra tự động A1–A3; hai profile load với nhóm A v1.2; 21 test vẫn pass.

## 2026-10-19 — Trả lời AU-02, AU-27, AU-28

- AU-02: không cần quan tâm cột H "Assessment (Pass/Fail)". Criteria vốn không nạp cột này; không phải sửa gì.
- AU-28: khóa học cố định **Playwright + TypeScript**, không dùng stack khác. `auto-qa/criteria.json`: `tech_stack_assumed` (giả định) đổi thành `tech_stack` (cố định), kèm rule.
- AU-27: dùng **evidence package của rubric cũ**. Nội dung lấy nguyên văn từ `documents/QA_AI_Skills_Assessment_Rubric_AUTO.xlsx`, sheet Guide, ô B6:
  1. Skills folder (SKILL.md, references/, assets/).
  2. Full, unedited chat/agent transcripts, including the skill invocation.
  3. Output files (test case file, framework repo, specs, review report, plan, run report, bug report).
  4. Run logs: `tsc`, lint, `npx playwright test` output, CI/scheduler logs, test reports (JSON/HTML).
  5. Git history / merge request / review records.
  - Rule: "Missing evidence = condition fails." và "Screenshots or pasted text without a transcript do not count."
  - Đã thêm `evidence_package` (items + rules) vào `auto-qa/criteria.json` → v0.9-draft.
- `references/assessment-profiles.md`: thêm dòng `tech_stack` và `evidence_package` ở mục auto-qa, cập nhật version.
- Ghi chú cho manual: rule "thiếu bằng chứng thì điều kiện Fail" mới áp dụng cho auto. Với manual, M-20 (thiếu bằng chứng tính sao) và M-21 (bộ bằng chứng cho nhóm B, C4) vẫn mở.

## 2026-10-19 — Trả lời AU-29

- AU-29: **không giữ** ngưỡng nào của mô hình cũ:
  - maturity level 1–5, tỷ lệ 0.8/0.2, target 3.0
  - ≥5 lần chạy trước, ≥2 lần chạy bằng trigger, ≥90% của 10 mục
- Không phải sửa criteria: `auto-qa/criteria.json` không chứa ngưỡng nào của mô hình cũ.
- Điều kiện "test pass 3 lần liên tiếp" (self-check của B4 cho sub-category SCR) vẫn giữ, vì nó có trong sheet mới `Intermediate_auto`. Cùng con số với mô hình cũ, nhưng nguồn là sheet mới.

## 2026-10-19 — Trả lời AU-25 (gate và C4 không trùng)

- AU-25: gate và C4 là **hai điểm khác nhau**, không chấm trùng:
  - Gate AI Safety: "dùng AI output mà không validate" **chỉ nói về thông tin mật, nhạy cảm**.
  - C4 Human Validation & Improvement: dùng output AI sinh ra mà không refine (không chạy, không review, không sửa).
  - Một lỗi chất lượng output chỉ làm Fail C4, không làm Fail gate.
- `auto-qa/criteria.json` → v0.10-draft: gate `SAFE` có thêm `clarifications`. Lý do: điều kiện gốc (dịch từ sheet) ghi chung chung "uses AI output without validating it", judge đọc theo chữ sẽ chấm trùng với C4. Câu chữ gốc của điều kiện giữ nguyên.
- `references/assessment-profiles.md`: thêm clarification vào dòng gate, cập nhật version.
- Manual: gate chưa có điều kiện (M-16). Khi có, nên áp dụng cùng cách hiểu này nếu gate là chung cho cả khóa học.

## 2026-10-19 — Trả lời AU-22, AU-23, một phần AU-20

- AU-23: điều kiện "giải thích được code đã nộp" của C4 do **người chấm** làm; AI assessor không chấm.
  - Rule engine (`criterion_rules.py`) có thêm `human_conditions`: judge trả về `{"met": null, "pending": "human"}` cho các điều kiện này. Kết quả tiêu chí là `pending` cho tới khi người chấm điền.
  - Nếu kết quả đã rõ thì không phải chờ. Ví dụ với mode `all`, nếu một điều kiện khác đã trượt thì tiêu chí Fail ngay.
  - Tiêu chí phụ thuộc vào tiêu chí đang `pending` (qua `requires_pass_of`, vd B6 phụ thuộc B3) cũng `pending`, trừ khi tự nó đã Fail.
  - `auto-qa` C4: `human_conditions` gồm Pass vị trí 2 ("Can explain why each part…") và Fail vị trí 2 ("Cannot explain the submitted code").
- AU-22: dùng locator **CSS/XPath làm Fail C1**. Câu hỏi mới phát sinh: AU-30 (getByLabel, getByText, getByPlaceholder… có được dùng không).
- AU-20, trả lời một phần:
  - "chỉnh sửa tối thiểu" (C3) = có README / hướng dẫn chạy ngắn.
  - "lỗi quan trọng" = đúng các lỗi liệt kê trong ngoặc ngay cạnh: C1 là test pass nhầm, assert sai, flaky rõ ràng; C4 là locator sai, assert thiếu, flaky.
  - Còn mở: "chạy ổn định" / "flaky thường xuyên" (C1), "phần đáng kể của scope" (C2, chờ xác nhận).
- `auto-qa/criteria.json` → v0.11-draft: thêm `clarifications` cho C1, C3, C4 và `human_conditions` cho C4. Câu chữ gốc của các điều kiện giữ nguyên.
- T-01 (judge): không chấm điều kiện của người, trả "pending". T-02 (báo cáo): liệt kê điều kiện chờ người chấm.
- Test (chạy ngoài repo): 31/31 pass (21 cũ + 10 mới cho trạng thái pending và vị trí `human_conditions` sai).
- Cập nhật `references/assessment-profiles.md` (mục Pass rules, mục auto-qa) và `SKILL.md`.

## 2026-10-20 — Trả lời AU-19, AU-30

- AU-19: B2 "khám phá ứng dụng thật" dùng **Playwright MCP**; không giới hạn dữ liệu thật / tài khoản khi khám phá.
- AU-30: các locator hướng người dùng khác (getByLabel, getByText, getByPlaceholder, getByAltText, getByTitle) **được dùng**, nhưng phải hợp lý và theo thứ tự ưu tiên. CSS/XPath vẫn Fail C1 (AU-22).
- `auto-qa/criteria.json` → v0.12-draft:
  - B2 có thêm `clarifications`: dùng Playwright MCP, không giới hạn dữ liệu / tài khoản khi khám phá.
  - Clarification về locator của C1 được viết lại theo AU-30.
- `references/assessment-profiles.md`: cập nhật dòng nhóm B và nhóm C ở mục auto-qa, cập nhật version.
- Câu hỏi mới:
  - AU-31: thứ tự ưu tiên locator cụ thể.
  - AU-32: dùng tài khoản / dữ liệu thật khi khám phá có vi phạm gate không.

## 2026-10-20 — Trả lời AU-32 (khám phá chỉ dùng dữ liệu test)

- AU-32: khi khám phá ứng dụng bằng Playwright MCP, **chỉ được dùng tài khoản test, dữ liệu test của môi trường test**. Câu trả lời này thay cho phần "không giới hạn dữ liệu / tài khoản" của AU-19; AU-19 đã được sửa trong bảng, có ghi chú.
- `auto-qa/criteria.json` → v0.13-draft:
  - B2 `clarifications`: "No restriction on using real data or accounts…" đổi thành "Only test accounts and test data of a test environment may be used…".
  - Gate `SAFE` có thêm một clarification: khám phá bằng Playwright MCP với tài khoản / dữ liệu thật (không phải test) là vi phạm gate.
- `references/assessment-profiles.md`: cập nhật dòng nhóm B và dòng gate ở mục auto-qa, cập nhật version.

## 2026-10-20 — AU-21: đang cân nhắc auto không có đáp án sẵn

- AU-21 vẫn **Mở**: đang cân nhắc cho assessment auto không có đáp án sẵn, chưa chốt.
- Nếu chốt, cần quyết định thêm cho C2 (đã ghi vào nội dung AU-21):
  - scope lấy từ đầu vào của đề hay từ đâu;
  - ai đánh giá "edge case / risk quan trọng" khi không có đáp án;
  - auto không cần baseline.
- Chưa sửa criteria: C2 của auto vẫn giữ nguyên điều kiện như sheet.

## 2026-10-21 — Nạp Playwright Assessment Level 1 làm chuẩn chấm output script

- Nguồn: `Downloads/[Level 1] Playwright Assessment.xlsx` (sheet Overall, Assessment, Rating). sha256 `caac7cc4686d97f4671410ffb80678b571ca699aeb28c96b0469a4256673ee30`. File tải về được copy vào thư mục riêng trong scratchpad trước khi đọc.
- Quyết định: output của script tự động (competency automation scripts, sub-category SCR) được chấm theo tài liệu này.
- Đã tạo `profiles/auto-qa/playwright-assessment.json` (giữ nguyên văn tiếng Anh):
  - 4 phần, 17 mục, mỗi mục có trọng số:
    - PW-INT Interface (Locator and Page structure): 4 mục
    - PW-SD Scripting and Debugging: 7 mục
    - PW-DES Automation Test design: 3 mục
    - PW-CFG Configuration: 3 mục
  - Thang 1–5 (Poor → Excellent), công thức điểm phần (trung bình có trọng số), Qualified ≥ 3, mục dưới Meet phải có comment.
  - Kỳ vọng Level 1 (sheet Overall): biết Test automation và Playwright, áp dụng được pageObject, áp dụng framework là điểm cộng.
  - Sửa 2 lỗi chữ trong ô của sheet: "Plawright" → "Playwright"; "try/catch�" → "try/catch…".
- `auto-qa/criteria.json` → v0.14-draft: nhóm C có thêm `output_reference` trỏ tới file trên, áp dụng cho SCR. Chưa đổi điều kiện C1–C4.
- `references/assessment-profiles.md`: thêm dòng mô tả file, cập nhật version.
- Câu hỏi mới:
  - AU-33: kết hợp với C1–C4 thế nào (có 3 phương án và ánh xạ đề xuất).
  - AU-34: thang 1–5 so với Đạt/Không đạt; ai chấm.
  - AU-35: PW-INT-2 không có trọng số.
  - AU-36: XPath được phép ở đây nhưng Fail theo AU-22.

## 2026-10-21 — Trả lời AU-36 (ngoại lệ XPath)

- AU-36: nếu locator có sẵn của Playwright (getByRole, getByLabel…) không hỗ trợ tốt trường hợp đó và phải dùng XPath, thì **không Fail**. Các trường hợp khác dùng CSS/XPath vẫn Fail C1 (AU-22). AU-22 đã được ghi thêm ngoại lệ này.
- `auto-qa/criteria.json` → v0.15-draft: clarification về locator của C1 có thêm ngoại lệ.
  - XPath dùng được khi locator có sẵn không nhắm tới phần tử một cách ổn định.
  - XPath đó phải gọn (Playwright Assessment PW-INT-3).
  - Judge kiểm tra xem locator có sẵn có dùng được không. Một dòng comment trong code giải thích vì sao phải dùng XPath sẽ giúp việc này rõ ràng, nhưng không bắt buộc.
- `references/assessment-profiles.md`: cập nhật dòng nhóm C và version.
- Còn để ngỏ: ngoại lệ chỉ nói về XPath. CSS selector trong trường hợp tương tự có được miễn không? Hiện vẫn tính là Fail.

## 2026-10-21 — Ngoại lệ locator chỉ áp dụng cho XPath

- Chốt: ngoại lệ ở AU-36 **chỉ áp dụng cho XPath**. CSS selector không có ngoại lệ, luôn Fail C1. Điểm còn để ngỏ trong entry trước đã xong.
- `auto-qa/criteria.json` → v0.16-draft: clarification về locator của C1 ghi rõ "CSS selectors have no such exception: a CSS selector always fails".
- `references/assessment-profiles.md`: cập nhật dòng nhóm C và version.

## 2026-10-21 — Trả lời AU-19 (Playwright CLI), AU-21, bổ sung AU-30

- AU-19: công cụ khám phá ứng dụng thật là **Playwright CLI**, thay cho Playwright MCP ở câu trả lời trước. Quy tắc dữ liệu giữ nguyên: chỉ dùng tài khoản và dữ liệu test của môi trường test (AU-32).
- AU-21: **không có answer key cho đề auto**; bỏ qua phần này. Không làm baseline cho auto; các câu hỏi phụ về đáp án (scope lấy từ đâu, ai đánh giá edge case) không theo đuổi nữa.
- AU-30, bổ sung: các locator hướng người dùng khác được chấp nhận, nhưng phải **chọn tối ưu theo độ ưu tiên về hiệu suất** của từng loại built-in locator.
- AU-31 vẫn mở: đã biết tiêu chí chọn (theo hiệu suất), nhưng chưa có thứ tự cụ thể.
- `auto-qa/criteria.json` → v0.17-draft:
  - B2 và gate: "Playwright MCP" → "Playwright CLI".
  - C1: clarification về locator ghi theo câu trả lời mới của AU-30.
  - Thêm `answer_key: {exists: false}`.
- `references/assessment-profiles.md`: cập nhật mục auto-qa (CLI, locator, không có answer key) và version.

## 2026-10-21 — Prompt template mô phỏng bài nộp của học viên

- Tạo `evaluator/prompts/simulate-trainee-submission.md`: prompt cho AI agent đóng vai học viên, làm một bài nộp hoàn chỉnh từ đầu tới cuối theo tiêu chí hiện tại của evaluator. Bài nộp dùng làm test fixture cho evaluator.
- Tham số: profile (manual-qa / auto-qa), thư mục đề, competency, sub-category (auto), mục tiêu `pass` hoặc `planted` (cố ý trượt một số điều kiện), persona học viên, thư mục fixture.
- Các pha:
  - **Pha 0:** đọc tiêu chí trực tiếp từ evaluator (`profile_loader.py --out`), không chép lại vào prompt, để prompt không lỗi thời khi tiêu chí đổi. Không mở answer key / baseline / expected.
  - **Pha 1:** thiết kế: evidence map (mỗi điều kiện → artefact → đường dẫn), workflow map, danh sách skill.
  - **Pha 2:** dựng bài nộp: skills, knowledge (ngoài skill), chạy skill thật trong subagent riêng và lưu transcript nguyên văn (≥ 2 lần mỗi skill), review-log, outputs, evidence (auto), README. Tuân thủ gate.
  - **Pha 3:** tự kiểm tra: ghi `expected/conditions.json` theo đúng format `criterion_rules.py` đọc, rồi chạy `criterion_rules.py` để xem verdict.
- Sửa `profile_loader.py`: `--out` tự tạo thư mục cha (trước đây lỗi khi `design/` chưa có).
- Đã thử hai lệnh trong prompt: resolve auto-qa ra `design/resolved-criteria.json`; `conditions.json` mẫu cho SCR cho ra verdict pass ở mọi tiêu chí và `pending` ở C4 (điều kiện do người chấm). 31 test vẫn pass.
- Giới hạn: fixture manual vẫn cần trainer làm answer key riêng (prompt không tạo, vì học viên không thấy đáp án). Chỉ so sánh được kết quả theo từng điều kiện và từng tiêu chí; điểm nhóm, competency và ngưỡng đạt chưa so được (chờ M-02).

## 2026-10-21 — Trả lời M-29 (manual chấm cả bug report)

- M-29: bài manual **chấm cả bug report**. Competency của manual thành 5: requirements-analysis, test-design, test-case-generation, test-data-generation, **defect-analysis-reporting**.
- `manual-qa/criteria.json` → v0.11-draft: thêm `defect-analysis-reporting` vào `competencies`, bỏ câu "chưa rõ có chấm bug report" khỏi `status`.
- `references/assessment-profiles.md`: cập nhật danh sách competency và version, bỏ blocker về bug report.
- T-02 không còn chờ M-29.
- Hệ quả cho bài nộp mô phỏng: bug report cần bằng chứng lỗi (ứng dụng có lỗi, hoặc screenshot / log). Hai đề trong repo đều chưa có:
  - US-VP02 chỉ có user story và mockup.
  - Acme Notes (`manual-qa-sample`) có baseline 5 bug, nhưng thư mục exam chỉ có user story; screenshot / log mà đề nhắc tới không có trong repo.

## 2026-10-21 — Bằng chứng lỗi cho bài nộp mô phỏng: bug giả lập (tạm thời)

- Quyết định: trước khi đóng vai học viên, agent **đóng vai trainer** trong một subagent riêng:
  - dựng trang demo tĩnh của US-VP02 có cài vài bug;
  - ghi danh sách bug (vị trí, triệu chứng, severity) vào `baseline/` của fixture mới.
- Học viên chỉ thấy trang demo, không thấy danh sách bug. Subagent trainer chỉ báo lại đường dẫn file, không báo nội dung bug, để phần đóng vai học viên vẫn "mù" đáp án.
- **Ghi chú: đây là cách tạm.** Người dùng sẽ thay bằng bug thật sau → T-08.

## 2026-10-21 — Tạo fixture `manual-qa-sim-pass` (bài nộp mô phỏng)

- Chạy prompt `simulate-trainee-submission.md` bằng subagent:
  - trainer: trang demo có bug giả lập + baseline;
  - học viên: plan, 5 skill, knowledge;
  - 9 phiên chạy skill (skill 1–4 chạy 2 lần, skill 5 chạy 1 lần);
  - tester: chạy 97 test case trên trang demo bằng Chrome qua `playwright-core`, rồi chạy lại để kiểm tra.
- Kết quả thực thi: 145 case = 66 Pass, 9 Fail, 22 Observed, 22 Blocked, 26 Not run. Bug report có 3 bug. Lần chạy lại tìm thêm lỗi dòng tóm tắt điểm (RT-01), chưa đưa vào bug report.
- Review log có 11 mục. Học viên tìm và sửa lỗi của AI, và cả lỗi trong skill / knowledge của chính mình. AI cũng chỉ ra 2 lỗi học viên bỏ sót: ảnh bằng chứng bị trùng, và lỗi dòng tóm tắt điểm.
- Self-check (`expected/conditions.json`): 10 tiêu chí pass, B3 và C4 fail (do dừng phần bug report theo yêu cầu), C1 và C3 pending (C1 cần answer key; C3 do mâu thuẫn "không placeholder" vs "không đoán").
- Cách đóng 2 fail: chạy run-2 của skill 5; cập nhật bug report với RT-01.
- Transcript chứa đường dẫn tuyệt đối trên máy (tên user Windows). Chưa commit gì.

## 2026-10-21 — Trả lời M-02: cách tính điểm (5 điểm mỗi nhóm, ngưỡng 20%)

- Quyết định (chat): mỗi nhóm A, B, C = **5 điểm**, chia đều cho các tiêu chí nhỏ. Trong một tiêu chí, mỗi điều kiện có trọng số bằng nhau; điều kiện không thỏa bị trừ phần của nó. Tiêu chí **Fail khi ≥ 20%** số điều kiện của nó không thỏa.
- Hệ quả: M-07 đổi, có đạt một phần (có sai sót nhỏ vẫn Pass nhưng bị trừ). Pass rule mặc định chuyển từ `all` sang mode mới `deduction`. M-05 (phải thỏa tất cả) không còn đúng cho điều kiện đơn lẻ; vẫn đúng nếu đổi lại `{"mode": "all"}`.
- Code:
  - `criterion_rules.py`: mode `deduction` (`fail_unmet_ratio`, so sánh chính xác bằng `Fraction`; score = thỏa / tổng, giữ điểm một phần cả khi Fail); hàm `score_groups()` tính điểm nhóm và Competency Score; CLI `--results` in thêm điểm nhóm khi đủ tiêu chí.
  - `_shared/course-rules.json`: `pass_rule` = deduction 0.2; `scoring.group_points` = 5; `criterion_score` và `pass_threshold` = 3 đã có giá trị.
  - B6 của auto giữ rule riêng (`at_least` 2/3 + `requires_pass_of`), điểm 1 hoặc 0.
- Ví dụ số điều kiện: Fail ở 1/5, 1/4 (25%), 2/6, 2/10; vẫn Pass ở 1/6 (16,7%), 1/7, 1/10. Điểm nhóm B ví dụ: B1 thiếu 1/6 → 5/6 × (5/6 điểm) ≈ 0,69 / 0,83 điểm.
- **Giả định cần xác nhận (không có trong lời bạn):**
  1. Giữ trọng số nhóm 0.2/0.5/0.3 và ngưỡng đạt ≥ 3 trên thang 0–5 cho Competency Score (đây là ngưỡng "< 3" cũ, nay có nghĩa vì tổng là 5 điểm).
  2. "Vi phạm 20%" hiểu là **≥ 20%** thì Fail (1/5 là Fail). Nếu là > 20% thì sửa `fail_unmet_ratio` / phép so sánh.
  3. Tiêu chí Fail vẫn giữ điểm một phần (chỉ ảnh hưởng nhãn Fail và điều kiện qua/trượt, không về 0).
- Đã kiểm tra: 14 tiêu chí manual-qa chạy được với kết quả giả, ranh giới 20% đúng (5/4 fail, 6/5 pass, 10/9 pass, 10/8 fail); loader hai profile vẫn load.

## 2026-10-21 — Xác nhận 3 giả định điểm; T-02: plan và báo cáo cho weighted-pass-fail

- Người dùng xác nhận cả ba giả định: ngưỡng ≥ 3/5 với trọng số 0.2/0.5/0.3; "20%" là ≥ 20% thì Fail; tiêu chí Fail vẫn giữ điểm một phần. M-02 giờ là đã trả lời hẳn. Đã bỏ chữ "giả định" khỏi `course-rules.json` và `assessment-profiles.md`.
- `build_plan_from_profile.py`: nhánh `weighted-pass-fail` (baseline tùy chọn, `--sub-category`); plan ghi criteria đã resolve kèm rule và điều kiện, competency, scoring, gate, sha256. Mô hình `deduction` cũ vẫn chạy như trước.
- `render_assessment_report.py`: `render_weighted()`. Báo cáo theo từng competency: verdict từng tiêu chí, điểm nhóm (5 điểm), competency score, kết quả gate, bảng skill → competency (trainer review), danh sách điều kiện chờ người chấm; xuất xlsx, md, json.
- **Quyết định tạm cho M-11 (vẫn Mở):** nhóm A chấm theo từng skill, điểm mỗi tiêu chí A của competency = trung bình qua các skill thuộc competency đó; một skill Fail thì tiêu chí A hiển thị Fail. Competency không có skill nào → A = 0 và có ghi chú.
- Gate: nếu không có verdict (manual chưa có điều kiện, M-16) thì tổng là PENDING, status provisional. Gate Fail → FAIL. Status chỉ `final` khi trainer đã xác nhận mapping (`mapping_reviewed`).
- Còn lại: judge trả kết quả đúng định dạng result (T-01); auto-qa chưa có `competencies` nên chưa dựng plan được (AU-10).
- Đã kiểm tra bằng bài thử giả (5 competency, một skill trượt A1, B2 thiếu 1/7, một điều kiện chờ người, gate pass/fail): điểm khớp tính tay, PENDING → PASS sau khi người điền, gate Fail → FAIL.

## 2026-10-21 — T-01 xong: judge mới và bước gộp kết quả

- `agents/manual-qa-assessment-judge.md`: viết lại cho mô hình weighted-pass-fail. Judge trả từng điều kiện `{met, evidence}` đúng thứ tự `conditions` của plan; nhóm A chấm theo từng skill; B và C theo từng competency; đề xuất skill → competency kèm lý do; điều kiện của người trả `met: null`; gate chỉ ghi quan sát (verdict `pending`); không đọc `expected/`, `design/`. `fail_when_any` không có điều kiện tương ứng thì ghi vào `notes` (M-06 còn mở).
- `scripts/merge_judge_results.py` (mới): kiểm tra từng file judge (JSON hợp lệ, số kết quả = số điều kiện, mỗi kết quả có bằng chứng, competency hợp lệ, không báo trùng) rồi gộp thành `assessment_result.json`; không ghi gì nếu còn lỗi, và liệt kê lỗi theo file để chỉ chạy lại judge bị lỗi.
- Lần chấm `evals/sim-pass-run-1`: judge A (nhóm A, 5 skill) đã qua kiểm tra; chờ 5 judge B/C.


## 2026-10-21 — Chấm `manual-qa-sim-pass` bằng evaluator (lần 1)

- Chạy: plan → 6 judge song song (A theo skill; B và C theo 5 competency) → `merge_judge_results.py` → `render_assessment_report.py`. Kết quả ở `evaluator/evals/sim-pass-run-1/` (`eval_plan.json`, `judge/`, `assessment_result.json`, `report/`).
- Competency score: requirements-analysis 4,86; test-design 4,91; test-case-generation 4,57; test-data-generation 4,90; defect-analysis-reporting 4,78. Cả 5 ≥ 3 nên đạt; tổng **PENDING** vì gate chưa có điều kiện (M-16) và trainer chưa duyệt mapping skill → competency.
- Tiêu chí Fail (≥ 20% điều kiện không thỏa): requirements-analysis C3; test-case-generation C1, C3, C4; defect-analysis-reporting C2.
- Nhóm A: 5 skill đều đạt A1–A4.
- Vấn đề của tiêu chí (judge báo, cần course owner quyết): C1 viết cho điểm mơ hồ của requirements, các competency khác phải đọc theo nghĩa; Must/Nice của AMB5 bị tách đôi, bị tính ở cả requirements-analysis và test-case-generation C1; B3 điều kiện "chạy tương tự nhất quán" không áp dụng được khi chỉ chạy một lần.
- Lệch so với `expected/` của fixture (người dựng fixture tự dự đoán): expected cho B3 Fail, C4 Fail, C1/C3 pending; judge cho C3 và C1 Fail ở một số competency. Chưa xem xét chi tiết.

## 2026-10-21 — Vị trí lỗi chính xác, tài liệu cho course owner, quy đổi v0.3 (T-04)

### 1. Vị trí lỗi chính xác trong báo cáo
- Mỗi điều kiện `met: false` phải có `locations` (judge, quy tắc 3a): Excel `{file, sheet, cell, quote}`, text `{file, line, quote nguyên văn}`, thiếu `{file, absent}`.
- `merge_judge_results.py --submission-dir` kiểm tra từng vị trí với file thật (file có tồn tại, sheet, cell có giá trị chứa quote, quote xuất hiện nguyên văn và đúng dòng); lỗi thì liệt kê theo file, không ghi gì.
- `render_assessment_report.py`: đường dẫn tuyệt đối, sheet, cell hoặc dòng + quote trong cột Evidence/Notes của xlsx và md, thêm mục "Failed conditions: where to look". Nếu xlsx đang mở trong Excel thì ghi `assessment_scoring_sheet.new.xlsx`.
- 5 judge đã bổ sung vị trí cho 18 điều kiện không thỏa của `sim-pass-run-1`, qua kiểm tra; báo cáo ở `evaluator/evals/sim-pass-run-1/report/`. Lưu ý: số dòng transcript phải đếm theo `splitlines` của Python (khác `grep -n` ở vài file).

### 2. Điều kiện C1, C2, B3 không áp dụng được theo competency
- Tài liệu gửi course owner: `documents/criteria-applicability-for-course-owner.md` (bảng áp dụng/không áp dụng cho 5 competency, 9 câu hỏi, 4 đề xuất). Điểm chính: C1 viết cho requirements-analysis; DAR đạt C1 ở đúng 60% (đạt theo `bug_found_pct`, trượt theo 70% viết trong điều kiện); B3.4 cần ≥ 2 lần chạy mà DAR chỉ chạy một lần; AMB5 bị judge chấm khác nhau giữa RA/TD (đạt) và TCG (không đạt) cho cùng bằng chứng; DAR bị trừ vì BUG-04 không tìm thấy do test case BLOCKED ở khâu thực thi.

### 3. T-04: quy đổi kết quả v0.3
- `profiles/manual-qa/v03-conversion.json` (ánh xạ tiêu chí v0.3 → điều kiện hiện tại, exact/approximate) và `scripts/convert_v03_results.py`.
- Quy đổi được: A1–A4, A7, A8, C1–C4, C6, C7 và lỗi template của B2–B4. Không có tương đương: A5, A6, B1, phần provenance của B2–B4, cờ C6-severity; các lỗi này được liệt kê, không quy đổi.
- Kết quả v0.3 chấm cho cả bài; skill → competency theo tên thư mục skill, lỗi B/C → competency theo file lỗi trỏ tới.
- Vì phần lớn điều kiện không có dữ liệu v0.3 (vd 44/231 ở `manual-qa-sample`) nên điểm là **khoảng** thấp–cao, chưa kết luận được đạt/trượt (vd requirements-analysis 1,05–4,77).
- Đã chạy trên 4 kết quả: `test-fixtures/manual-qa-sample/expected/`, `manual-qa-sample-review/expected/`, `evals/sample-review-run-1`, `-2`; mỗi nơi có thư mục `converted/` (`assessment_result.v04.json`, `conversion_report.md`). Kết quả cũ giữ nguyên.
- Muốn có điểm đầy đủ: chấm lại các bài đó bằng judge mới (cần bài nộp thật cho B và C), hoặc chốt T-05 để đưa lại tiêu chí v0.3.

## 2026-10-23 — Bỏ fail_when_any; tiêu chí đạt khi thỏa ≥ 80% điều kiện

- Quyết định (chat): tiêu chí chỉ giữ các quy tắc Pass, không giữ `fail_when_any`. Điểm tiêu chí **Fail nếu tổng không đạt 80%** yêu cầu, tức đạt khi số điều kiện thỏa / tổng ≥ 80% (4/5 đạt, 3/4 Fail, 5/6 đạt, 4/6 Fail). Thay cho "Fail khi ≥ 20% không thỏa" (22/10), theo đó 1/5 là Fail; giờ đúng 80% là đạt.
- Criteria: đã xóa `fail_when_any` khỏi mọi tiêu chí (`manual-qa/criteria.json`, `auto-qa/criteria.json` kể cả `by_sub_category`, `_shared/skill-standard.json`) và khỏi `human_conditions` của auto C4. Gate `SAFE` của auto giữ nguyên danh sách Fail (là quy tắc của gate, không phải tiêu chí).
- Rule: `_shared/course-rules.json` v0.4-draft: `pass_rule = {"mode": "proportional", "min_ratio": 0.8}`. Mode `deduction` (mới thêm hôm trước) bỏ vì trùng với `proportional`; `proportional` so sánh chính xác bằng `Fraction`, vẫn giữ điểm một phần khi Fail. `criterion_rules.py` không còn kiểm `fail_when_any` ở `human_conditions`.
- Judge: bỏ quy tắc `fail_when_any`; lỗi quan sát được mà không điều kiện nào bao phủ thì ghi vào `notes`, không tính. M-06 → Không còn áp dụng.
- Chấm lại `evals/sim-pass-run-1` với plan mới: kết quả không đổi (không tiêu chí nào nằm đúng ở 80%), điểm competency giữ nguyên 4,57–4,91; không cần chạy lại judge.
- Cập nhật `references/assessment-profiles.md`, `SKILL.md`, tài liệu gửi course owner. Các kết quả v0.3 đã quy đổi (`converted/`) không dùng pass rule nên không đổi.

## 2026-10-24 — M-30: giới hạn thật của B1-B4 Provenance (T-05)

- Khi thảo luận T-05's đề xuất B1-B4 Provenance (bằng chứng output do skill thực sự tạo ra): judge đối chiếu `ai-original/<file>` với nội dung code tạo file trong `transcript`. Câu hỏi: nếu học viên tự sửa tay output rồi **copy luôn bản đã sửa thành `ai-original/`** (giả bản gốc), judge có bắt được không?
- Trả lời: **không**, nếu chỉ nhìn `ai-original/` một mình — nó chỉ là file học viên tự đặt vào bài nộp, không có gì đảm bảo tính xác thực. Nguồn đối chiếu độc lập duy nhất là `transcript`.
- Nhưng `transcript` hiện tại (theo `test-fixtures/manual-qa-sim-pass/README.md`) cũng **"exported from the session logs"** — tức là học viên tự xuất ra rồi nộp. Nếu quy trình thi thật cũng vậy (không có hệ thống độc lập tự ghi log phiên chat mà học viên không sửa được), học viên có thể giả cả `ai-original/` lẫn transcript cho khớp nhau — judge không có cách nào phát hiện bằng nội dung bài nộp.
- → B1-B4 Provenance (T-05) chỉ có ý nghĩa thật nếu transcript được thu thập tamper-proof (platform/LMS tự động ghi log, không qua tay học viên). Ghi thành câu hỏi mở **M-30**, cần course owner xác nhận quy trình thi thật thu thập transcript thế nào trước khi đưa B1-B4 vào criteria chính thức.

## 2026-10-24 — Rà soát repo: mâu thuẫn, dư thừa, thiếu sót

Rà soát toàn bộ `evaluator/` (SKILL.md, references/, scripts/, profiles/, test-fixtures/) cộng `documents/`, `research/`, `.gitignore`. Việc cần sửa đã thêm vào bảng "Việc cần làm" (T-09 → T-15). Ghi chú thêm các phát hiện không tạo thành việc riêng:

- **Dư thừa:** `scripts/check_consistency.py` nằm chết (không ai gọi) — gộp vào T-13.
- **Thiếu sót khác không tạo T riêng:**
  - `research/kiro-demo/` ở root repo, không liên quan evaluator — không phải lỗi, chỉ dễ gây nhầm cho người mới nếu không có ghi chú ở root.
  - Nhiều mục "Chưa làm" cũ (T-03, T-04, T-05, T-07, T-08) vẫn còn tồn đọng, trong đó **T-07 đáng chú ý nhất**: `skill-standard.md` + `SKILL.template.md` (tiêu chuẩn chấm hiện hành) có thể chưa được gửi cho học viên.
- **Việc đang dở cần nhớ xử lý:** `test-fixtures/manual-qa-sim-pass/submission/skills/test-case-generation/SKILL.md` đang có lỗi cố ý (`name: test-case-generation-intentional`, dùng để test judge ở run-4) — cần revert nếu không còn dùng để test.


## 2026-10-28 — Chấm thử bài nộp `Week06_3` (đề Home Product Discovery); quyết định phạm vi

Chấm bằng evaluator (profile manual-qa, plan sinh từ `baseline/*.xlsx` của trainer). Kết quả **FAIL, provisional**: requirements-analysis 2.92, test-case-generation 2.10, defect-analysis-reporting 2.58 (đạt khi >= 3). Safety gate chưa chấm.

**Quyết định (chat, 2026-10-28):**
- Đề thi chỉ dùng **Home Product Discovery** (My Shop, US-VP03); đề Login (Acme Notes) bỏ.
- **Loại `test-design` và `test-data-generation`** khỏi phạm vi chấm của đề này (đề chỉ phủ 3 competency). Trước đó hai competency này bị tính 0 điểm vì không có skill/transcript/output. Kết luận tổng vẫn FAIL dù có hay không có hai competency đó.
- Evidence/Notes trong báo cáo dùng đường dẫn tương đối tính từ thư mục `submission/`.

**Phát hiện, chưa xử lý:**
- Evaluator chưa có cách bỏ competency theo từng đề: `build_plan_from_profile.py` lấy `competencies` thẳng từ `criteria.json`. Cần chọn: chạy với bản sao profile ngoài repo, hoặc thêm cờ (vd `--competencies`).
- `render_assessment_report.py` dòng 247 (`loc_lines`) vẫn in đường dẫn tuyệt đối khi render với `--submission-dir` (634 lần trong báo cáo thử), dù `relativize()` đã xử lý `check_ref`. Chưa sửa.
- Bài nộp không nhất quán: `chat-transcript.md` và cả 3 skill vẫn mô tả bài Login (A1, A2, A4 của Test-Case-Generation và A3 của defect-analysis-reporting trượt; B1-B5 trượt vì transcript không khớp output), trong khi output là của Home. Output trùng nhiều với baseline (TR 55/64, TC 91/120 dòng giống hệt): chưa rõ đây là bài mẫu của đội manual hay bài thật; không có tiêu chí trừ điểm cho việc này.
- Thư mục `outputs/lack info version with bad prompting/` không chấm (plan không có điều kiện thứ hai).
- Còn chờ người quyết định: mapping skill -> competency (judge đề xuất), TR_034-036 importer tự đặt là mandatory, M-16..M-18 (safety gate).

## 2026-10-29 — Cờ `--competencies` cho `build_plan_from_profile.py`

- Lý do: đề Home Product Discovery chỉ phủ 3 competency (xem mục 2026-10-28); trước đó test-design và test-data-generation bị tính 0 điểm.
- Cách làm: thêm `--competencies id1,id2,...` (chỉ cho weighted-pass-fail). Plan chỉ giữ các competency được chọn; id không có trong profile bị từ chối. Merge và render đọc danh sách từ plan nên không cần sửa.
- Không xóa 2 competency khỏi `profiles/manual-qa/criteria.json`: fixture `manual-qa-sim-pass` và `v03-conversion.json` vẫn dùng đủ 5 competency.
- Chưa chạy lại fixture `manual-qa-sim-pass`; `check_consistency.py` đạt.
