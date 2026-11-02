# T-05 — Bản nháp: đưa lại các tiêu chí v0.3 đã bị bỏ (manual-qa)

Gửi: course owner · Nguồn: `evaluator/skills/skill-evaluator/profiles/manual-qa/v03-conversion.json`, criteria v0.3 gốc (`git show aca441e:...criteria.json`) · Ngày: 2026-10-24

Đây là **bản nháp để course owner duyệt**, chưa đưa vào `criteria.json`. Mỗi mục bên dưới: nội dung tiêu chí v0.3 gốc (tóm tắt), tình trạng che phủ hiện tại trong model `weighted-pass-fail`, và đề xuất bổ sung ở dạng điều kiện `pass_when_all` (khớp văn phong các tiêu chí A/B/C hiện có).

**Lưu ý về điểm:** group A/B/C hiện chia đều 5 điểm cho số tiêu chí trong nhóm (`group_points / n`). Thêm tiêu chí mới vào một nhóm sẽ làm giảm trọng số của các tiêu chí hiện có trong nhóm đó — course owner cần xác nhận có chấp nhận việc này không, hoặc chọn gộp vào tiêu chí sẵn có (không tăng n) như phương án thay thế ở mỗi mục.

## Nhóm A — Skill Standard

### A5 (cũ): File-opening instructions — **chưa có tương đương** (`no_equivalent`)

v0.3: mọi file trong `references/`/`assets/` phải được SKILL.md nhắc tới bằng đường dẫn, đường dẫn phải tồn tại, và phải nói rõ bước nào mở file đó.

**Đề xuất — Phương án 1 (tiêu chí mới A5, nhóm A còn 5 tiêu chí):**
```
A5. File References
Pass khi:
- Mọi file trong references/ và assets/ được SKILL.md nhắc tới bằng đường dẫn tương đối
- Mọi đường dẫn được nhắc trong SKILL.md đều tồn tại (đúng chính tả, đúng hoa/thường)
- Mỗi file nói rõ được mở ở bước nào (ghi "Step N" hoặc nằm trong nội dung bước N đó), và bước N đó thực sự có trong Process
N/A khi: skill không có references/ lẫn assets/
```
**Phương án 2 (gộp vào A2 Structure Compliance, không tăng n):** thêm 1 điều kiện vào `pass_when_all` của A2.

### A6 (cũ): Files in the right place — **chưa có tương đương**

v0.3: `references/` chỉ chứa tài liệu để đọc, `assets/` chỉ chứa template để copy, `scripts/` chỉ chứa code chạy được, không có thư mục lạ hay file rác (`~$*.xlsx`, file output đã có dữ liệu).

**Đề xuất — Phương án 1 (tiêu chí mới A6):**
```
A6. File Placement
Pass khi:
- Gốc thư mục skill chỉ có SKILL.md (cho phép thêm LICENSE)
- references/ chỉ chứa tài liệu Claude ĐỌC (quy tắc, checklist, hướng dẫn, định dạng), .md/.txt
- assets/ chỉ chứa file để DÙNG/COPY vào output (.xlsx/.docx template, hình ảnh)
- scripts/ chỉ chứa code chạy được (.py/.sh)
- Không có thư mục lạ (docs/, templates/...), không có file khóa (~$*.xlsx), không có file output đã điền sẵn dữ liệu
```
**Phương án 2:** gộp vào A4 Reusability & Maintainability.

### A8 (cũ): No overlap — **đã có, không cần làm gì thêm**

Đã trùng với A3 điều kiện 3 hiện tại ("Read on its own, the description does not overlap with any other skill the trainee submitted"). Xác nhận với v03-conversion.json: confidence "exact".

## Nhóm B — AI Application & Enablement

### B1–B4 (cũ): Provenance (bằng chứng output do skill thực sự tạo ra) — **chưa có tương đương đầy đủ**

v0.3: mỗi output (câu hỏi làm rõ, file TR, file TC, báo cáo bug) phải có bằng chứng transcript cho thấy đúng skill đó được gọi, và output xuất hiện ngay sau lời gọi đó trong cùng phiên chat — không chấp nhận file được gõ tay hoặc dán vào.

Hiện tại: judge instructions có nói "Group B is a provenance check. It needs the transcript..." (mục 10, `agents/manual-qa-assessment-judge.md`) nhưng đây là hướng dẫn chung cho judge, không phải điều kiện `pass_when_all` cụ thể để chấm nhất quán.

**Đề xuất — thêm vào B3 Skill Execution & Repeatability (không tăng n, B3 đã đúng chủ đề):**
```
Thêm điều kiện: Mỗi deliverable nộp có bằng chứng transcript cho thấy đúng skill đó được gọi (tên skill trong tool call, hoặc Claude đọc SKILL.md đó), và deliverable xuất hiện ngay sau lời gọi đó trong cùng phiên chat — không chỉ là file/text được dán vào mà không có transcript
```
**Phương án 2 (tiêu chí mới B7 Output Provenance):** tách riêng nếu course owner muốn theo dõi lỗi này độc lập với B3's "repeatability".

**Giới hạn thật cần biết trước khi áp dụng (xem M-30):** judge chỉ đối chiếu `ai-original/<file>` (hoặc nội dung sửa tay) với code/kết quả trong `transcript` — không đối chiếu được với gì khác. Nếu học viên tự chỉnh sửa output rồi tạo luôn `ai-original/` giả khớp với bản đã sửa, VÀ transcript cũng là file học viên tự export rồi nộp (không phải hệ thống độc lập tự ghi log), thì học viên có thể làm giả cả hai cho khớp nhau — judge không có cách nào phát hiện chỉ từ nội dung bài nộp. Điều kiện B1-B4 Provenance ở trên **chỉ có ý nghĩa chống gian lận thật sự nếu transcript được thu thập tamper-proof** (platform/LMS tự động ghi log phiên chat, học viên không sửa được trước khi nộp). Cần course owner xác nhận quy trình thi thật trước khi đưa điều kiện này vào `criteria.json` — nếu không, điều kiện này chỉ có giá trị bắt lỗi sơ ý (quên gắn transcript), không bắt được gian lận cố ý.

## Nhóm C — QA Output Quality

### C3 (cũ): TC coverage — **đã che phủ một phần** qua C2 điều kiện 0

Còn thiếu so với v0.3: (a) edge case phải có TC riêng (không được gộp vào TC happy-path), (b) TR đánh dấu BLOCKED phải có TC kèm theo hoặc lý do nêu rõ.

**Đề xuất — thêm vào C2 Completeness & Coverage (test-case-generation):**
```
- Mỗi TR được đánh dấu "Edge case" có ít nhất 1 TC riêng nhắm đúng edge case đó, không gộp vào TC happy-path
- Mỗi TR đánh dấu BLOCKED có TC kèm theo (có thể gắn cờ BLOCKED) hoặc có lý do nêu rõ vì sao không có TC
```

### C4 (cũ): TC quality (Expected Result cụ thể) — **đã che phủ một phần** qua C3 điều kiện 2

v0.3 liệt kê rõ các cụm từ bị cấm đứng một mình: "works correctly/properly/as expected", "displayed correctly", "no error", "success", "OK". Hiện tại C3 chỉ nói chung "expected results verifiable" — judge có thể đọc khác nhau giữa các lần chấm.

**Đề xuất — làm rõ điều kiện C3 hiện tại (test-case-generation), không tăng n:**
```
Expected Result không được đứng một mình với các cụm chung chung: "works/displays correctly/properly/as expected", "no error", "success", "OK" — phải nêu ít nhất 1 điều quan sát được cụ thể (nội dung message, giá trị hiển thị, màn hình chuyển tới, trạng thái field/button, dữ liệu có lưu hay không)
```

### C5 (cũ): Bug finding (tìm đủ N% bug trong answer key) — **chưa có tương đương đủ mạnh** (chỉ map lỏng vào C2 cond 6 "no serious omissions")

Đây là tiêu chí objective, có ngưỡng rõ ràng, dễ pre-register — **đáng được đưa lại nguyên vẹn nhất** trong các mục T-05.

**Đề xuất — tiêu chí mới C5 (defect-analysis-reporting), hoặc gộp vào C1 Accuracy:**
```
C5. Bug Finding Rate
Pass khi CẢ HAI đúng:
- Tìm được ít nhất N bug khớp với answer key (N = 60% tổng số BUG-xx, làm tròn lên)
- Tìm được 100% bug mức Critical/Major trong answer key
Khớp = đúng vị trí + đúng triệu chứng; nhiều báo cáo cùng nguyên nhân chỉ tính 1 lần
```
Lưu ý: cần `baseline.json` có field ngưỡng (`thresholds.bug_found_pct`) như v0.3 từng có — kiểm tra lại field này còn trong baseline schema hiện tại không trước khi áp dụng.

### C6 (cũ): Bug report quality (đủ field, không bịa môi trường) — **che phủ rời rạc**, chưa gộp thành 1 chỗ

**Đề xuất — thêm vào C3 Usability & Format hoặc C4 Human Validation (defect-analysis-reporting):**
```
- Mỗi bug có Steps to Reproduce đánh số, bắt đầu từ trạng thái rõ ràng, người khác làm theo được
- Mỗi bug có cả Expected Result và Observed Result, và hai cái khác nhau
- Severity/Priority lấy từ giá trị dropdown, mỗi cái có lý do riêng
- Build found/browser/OS: chỉ điền khi đề bài cung cấp; nếu không có thì để trống kèm ghi chú "not provided", không được bịa
```
Advisory (không tính lỗi cứng, cần người quyết định): severity lệch quá 1 bậc so với answer key — giữ nguyên cơ chế advisory flag `C6-severity` đã có sẵn trong metrics registry.

### C7 (cũ): No fabrication — **chưa có tương đương, và đáng áp dụng cho MỌI competency, không riêng defect-analysis**

v0.3: mọi rule cụ thể (giới hạn, độ dài, định dạng, nội dung message lỗi, quyền, thứ tự xử lý) xuất hiện trong TR/TC/Steps mà user story không nói tới phải được gắn "Assumption —"/"BLOCKED —" hoặc đưa vào câu hỏi làm rõ — không được viết như một requirement đã xác nhận.

Đây là một "anti-hallucination" check tổng quát, không chỉ riêng cho bug report. **Đề xuất ưu tiên 2 sau C5:**
```
Thêm vào C4 Human Validation & Improvement (mọi competency):
- Mọi rule cụ thể không có trong user story/AC đều được gắn nhãn Assumption/BLOCKED hoặc đưa vào câu hỏi làm rõ, không viết như requirement đã xác nhận
```

## Tổng hợp mức độ ưu tiên đề xuất

1. **C5 Bug Finding Rate** — objective, có ngưỡng rõ, dễ pre-register, đang là lỗ hổng lớn nhất (bài nộp có thể bỏ sót bug nghiêm trọng mà không bị trừ điểm tương xứng).
2. **B1–B4 Provenance** — hiện chỉ là hướng dẫn judge, chưa phải điều kiện chấm nhất quán được; rủi ro: bài nộp gõ tay/dán kết quả không bị bắt.
3. **C7 No fabrication** — áp dụng rộng, giá trị cao, nhưng cần course owner xác nhận phạm vi (mọi competency hay chỉ một số).
4. A5, A6, C3, C4, C6 — giá trị thấp hơn (đã che phủ một phần hoặc ít rủi ro hơn), có thể làm sau.

**Việc cần course owner quyết định trước khi đưa vào `criteria.json`:**
- Chấp nhận tăng số tiêu chí trong nhóm (chia lại trọng số) hay chỉ gộp vào tiêu chí sẵn có?
- Với C5: `baseline.json` hiện tại có field ngưỡng bug_found_pct chưa?
- Phạm vi áp dụng C7 (riêng defect-analysis hay mọi competency)?
