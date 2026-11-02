# Ma trận điểm đánh giá AI-assisted QA Core Competencies

> Phiên bản: 0.1-draft · Ngày: 2026-10-13 · Trạng thái: đề xuất, cần SME review

## 0. Tóm tắt thiết kế

- **2 trục**: 7 competency (dòng) × 3 dimension (cột): **Skill · Prompt · Output**.
- **2 tầng tiêu chí**:
  - *Tiêu chí chung*: 16 tiêu chí (S1–S6, P1–P5, O1–O5) dùng chung cho cả 7 competency, nên các competency so sánh được với nhau.
  - *Chỉ báo riêng*: mỗi ô (competency × tiêu chí) có chỉ báo và metric riêng, nên đo được đúng chuyên môn của từng competency.
- **Thang chấm**: 0–4, mỗi mức có mô tả hành vi cụ thể (Behaviorally Anchored Rating Scale, BARS). Tiêu chí nào đo được bằng số (recall, pass rate, …) thì quy đổi sang 0–4 theo ngưỡng cố định.
- **Không cho bù trừ**: có điều kiện loại (gate) và điểm sàn cho từng dimension, để Output đẹp không bù được cho việc vi phạm an toàn dữ liệu hay bịa yêu cầu.
- **Kiểm chứng**: có quy trình đo content validity (CVI), xác định trọng số bằng AHP, đo inter-rater reliability (ICC/kappa), và dùng bộ bài mẫu cài lỗi sẵn (calibration fixture) để hiệu chỉnh.

---

## 1. Ba dimension đo cái gì

| Dimension | Câu hỏi đánh giá | Bằng chứng (evidence) |
|---|---|---|
| **S – Skill** (skill hiệu quả) | Gói skill có điều khiển AI làm đúng competency này một cách **lặp lại được** trên input mới không? | Thư mục skill (SKILL.md, references/, assets/, scripts/) + kết quả chạy lại trên input ẩn |
| **P – Prompt** (prompt tốt) | Người học có cung cấp đủ ngữ cảnh, ràng buộc, và **phản biện, sửa** output của AI không? | Transcript chat đầy đủ, không cắt |
| **O – Output** (output chất lượng) | Sản phẩm cuối có đúng, đủ, không bịa, đúng chuẩn, và dùng được ngay không? | File output, so với baseline / answer key |

> Lưu ý: khi dùng skill thì prompt gọi skill thường rất ngắn ("dùng skill X cho story này"). Vì vậy dimension P **không chấm độ dài hay độ "hoa mỹ"** của prompt. P chấm việc *cấp ngữ cảnh* và *vòng phản biện (human-in-the-loop)*.

---

## 2. Thang chấm 0–4 (dùng cho mọi tiêu chí)

| Điểm | Mức | Mô tả chung |
|---|---|---|
| 0 | Không có | Không có bằng chứng, hoặc sai hoàn toàn |
| 1 | Sơ khai | Có làm nhưng thiếu/sai nghiêm trọng; không dùng được nếu không làm lại |
| 2 | Đạt một phần | Đúng hướng nhưng còn lỗi đáng kể; phải sửa nhiều |
| 3 | Đạt | Đáp ứng đầy đủ tiêu chuẩn; chỉ cần chỉnh nhỏ |
| 4 | Xuất sắc | Vượt chuẩn: có cơ chế tự kiểm tra, đo lường, hoặc tái sử dụng rõ ràng |

**Quy đổi metric định lượng sang 0–4** (mặc định; từng metric có thể có ngưỡng riêng):

| Metric (%) | ≥ 90 | 75–89 | 50–74 | 25–49 | < 25 |
|---|---|---|---|---|---|
| Điểm | 4 | 3 | 2 | 1 | 0 |

Với metric "càng thấp càng tốt" (fabrication rate, duplicate rate, flaky rate), lật ngược ngưỡng, ví dụ ≤ 2% → 4, ≤ 5% → 3, ≤ 10% → 2, ≤ 20% → 1, > 20% → 0.

**Vì sao chọn 0–4 mà không dùng 1–10:** thang ít mức, mỗi mức có mô tả hành vi, cho độ đồng thuận giữa người chấm cao hơn. Bốn mức khác 0 (số chẵn) cũng tránh được xu hướng chấm dồn vào mức giữa.

---

## 3. Tiêu chí chung và trọng số trong từng dimension

### 3.1 Skill (S)

| ID | Tiêu chí | Trọng số | Mức 3 (Đạt) trông như thế nào | Map với profile manual-qa hiện có |
|---|---|---|---|---|
| S1 | Packaging & Trigger | 15% | Cấu trúc chuẩn; description có "Use when…" + activity + input; không chồng lấn skill khác | A1, A2, A3, A8 |
| S2 | Process design | 20% | Các bước đánh số; có input → xử lý → output; có điểm dừng để hỏi khi thiếu thông tin | A4 |
| S3 | Knowledge & Resources | 20% | references/ chứa kỹ thuật/checklist **đúng chuyên môn của competency**; assets/ chứa template; mỗi file gắn với một bước | A5, A6 |
| S4 | Reusability | 10% | Không chứa domain knowledge của AUT; tham số hóa được | A7 |
| S5 | Built-in quality control | 15% | Có bước self-check theo checklist; có rule chống bịa ("ghi rõ Assumption"); có schema cho output | *(mới)* |
| S6 | Empirical effectiveness | 20% | Chạy lại **3 lần** trên **input ẩn** (khác input bài thi): trigger đúng 3/3, output đạt ≥ mức 3 ở O1–O2 trong ≥ 2/3 lần chạy | B1–B4 (một phần) |

> S6 là tiêu chí làm cho phần "skill hiệu quả" có tính khoa học: đo hiệu quả bằng thực nghiệm thay vì chỉ đọc file, đồng thời chặn trường hợp skill bị "overfit" vào đúng input của bài thi.

### 3.2 Prompt (P)

| ID | Tiêu chí | Trọng số | Mức 3 (Đạt) trông như thế nào |
|---|---|---|---|
| P1 | Context supply | 25% | Đưa đủ nguồn: tài liệu, mockup, convention, log…; nói rõ vai trò và phạm vi |
| P2 | Task & constraints | 20% | Mục tiêu, phạm vi in/out, ràng buộc và definition of done đều rõ ràng |
| P3 | Output specification | 15% | Chỉ định format/template/cấu trúc đầu ra (hoặc để skill làm việc này) |
| P4 | Critical review & iteration | 30% | Phát hiện ít nhất một lỗi thật của AI và yêu cầu sửa bằng feedback cụ thể; không chấp nhận output một cách mù quáng |
| P5 | Efficiency | 10% | Đạt output chấp nhận được trong số lượt hợp lý; không phải làm lại từ đầu |
| P6 | Data safety | **Gate** | Không đưa PII thật, credential, hay dữ liệu mật của khách hàng vào AI (xem mục 5) |

> P4 có trọng số cao nhất vì đây là năng lực phân biệt "người dùng AI" với "người giao việc cho AI".

### 3.3 Output (O)

| ID | Tiêu chí | Trọng số | Ý nghĩa |
|---|---|---|---|
| O1 | Correctness | 30% | Nội dung đúng so với baseline / yêu cầu gốc |
| O2 | Completeness / Coverage | 25% | Recall so với baseline (bao phủ được bao nhiêu phần cần có) |
| O3 | Faithfulness / No fabrication | 20% | Precision: không bịa rule, bug hay dữ liệu; mọi item truy vết được về nguồn |
| O4 | Conformity | 10% | Đúng template, convention, naming |
| O5 | Usability / Actionability | 15% | Người khác dùng hoặc chạy được ngay mà không cần hỏi lại |

---

## 4. Ma trận chỉ báo riêng theo competency

Mỗi bảng dưới đây giữ nguyên ID tiêu chí chung nhưng viết lại *chỉ báo cụ thể* và *metric* cho competency đó. Những tiêu chí không ghi trong bảng thì dùng mô tả chung ở mục 3.

### 4.1 REQ – AI-assisted Requirements Analysis

**Baseline cần có:** danh sách điểm mơ hồ (ambiguity) và edge case đã cài sẵn; danh sách TR chuẩn.

| Tiêu chí | Chỉ báo / Metric |
|---|---|
| S3 | references/ có checklist phát hiện mơ hồ (thiếu rule, biên giá trị, trạng thái lỗi, NFR, quyền) và chuẩn INVEST/testability |
| S5 | Có rule "không suy diễn thành requirement, ghi rõ Assumption"; có self-check "mỗi AC có ≥ 1 TR" |
| P1 | Đính kèm đủ story + mockup + glossary/rule liên quan |
| P4 | Loại bỏ câu hỏi thừa và bổ sung điểm mơ hồ mà AI bỏ sót |
| O1 | TR diễn giải đúng ý AC (judge đối chiếu baseline) |
| O2 | **Ambiguity recall** = số điểm mơ hồ tìm được / số đã cài · **AC coverage** = % AC có ≥ 1 TR |
| O3 | **Fabrication rate** = số rule bịa / tổng TR (mục tiêu ≤ 5%) · **Question precision** = câu hỏi liên quan / tổng câu hỏi |
| O5 | Câu hỏi cụ thể, PO trả lời được (dạng đóng hoặc có phương án); có chia Must ask / Nice to confirm |

### 4.2 DES – AI-assisted Test Design

**Baseline cần có:** danh sách test condition chuẩn (partition, boundary, tổ hợp rule, transition).

| Tiêu chí | Chỉ báo / Metric |
|---|---|
| S3 | references/ có hướng dẫn **khi nào dùng kỹ thuật nào** (EP, BVA, Decision Table, State Transition, Pairwise, Error Guessing) |
| S5 | Bắt buộc ghi kỹ thuật đã chọn và lý do cho từng TR; có self-check biên giá trị (min−1, min, max, max+1) |
| P2 | Nêu rõ ràng buộc dữ liệu và rule nghiệp vụ; yêu cầu ưu tiên theo rủi ro |
| P4 | Bác bỏ kỹ thuật chọn sai, ví dụ dùng EP cho logic tổ hợp lẽ ra phải dùng Decision Table |
| O1 | **Technique fit**: chọn đúng kỹ thuật và áp dụng đúng (biên chính xác, không lệch ±1) |
| O2 | **Condition coverage** = condition tìm được / condition trong baseline (partition, boundary, rule combination) |
| O3 | Không có condition nào thiếu nguồn (truy vết về TR/AC) |
| O5 | Có traceability TR → condition và mức ưu tiên theo rủi ro |

### 4.3 TCG – AI-assisted Test Case Generation

**Baseline cần có:** bộ TC chuẩn và danh sách scenario bắt buộc.

| Tiêu chí | Chỉ báo / Metric |
|---|---|
| S3 | assets/ có template TC; references/ có rule viết TC (atomic step, expected result đo được) |
| S5 | Chain từ file TR (mọi TR ID trong file TC phải tồn tại trong file TR); self-check "mỗi TR có ≥ 1 TC" |
| P4 | Phát hiện và sửa TC trùng, hoặc expected result mơ hồ |
| O1 | Step và expected result đúng với hành vi mong đợi |
| O2 | **TR coverage** = % TR có ≥ 1 TC · **Scenario recall** so với baseline · có cả positive và negative |
| O3 | Không có TC kiểm tra hành vi không có trong yêu cầu |
| O4 | Đúng template; ID và naming nhất quán |
| O5 | **ER specificity** = % expected result quan sát/kiểm chứng được (không có "works correctly") · **Duplicate rate** ≤ 5% · chạy được độc lập (có precondition) |

### 4.4 TDG – AI-assisted Test Data Generation

**Baseline cần có:** schema/ràng buộc dữ liệu; danh sách partition và boundary cần có dữ liệu.

| Tiêu chí | Chỉ báo / Metric |
|---|---|
| S2 | Quy trình: trích ràng buộc → sinh dữ liệu → validate → map về TC |
| S3 | scripts/ có generator (có seed để tái lập); references/ có rule về dữ liệu synthetic |
| S5 | Có bước validate theo schema; rule cấm PII thật |
| P1 | Cung cấp schema, ràng buộc, quan hệ giữa các entity |
| O1 | **Valid-set validity** = % bản ghi "valid" pass schema (mục tiêu ≥ 95%) · **Invalid-set precision** = % bản ghi "invalid" vi phạm **đúng 1** rule (single-fault) |
| O2 | Bao phủ partition và boundary; có null, rỗng, unicode, ký tự đặc biệt, độ dài tối đa |
| O3 | Giữ referential integrity; không có giá trị vô nghĩa với domain |
| O4 | Đúng format yêu cầu (CSV/JSON/SQL), đúng số lượng |
| O5 | Tái lập được (seed/script); mỗi dataset map về TC |
| Gate | Có PII thật trong dữ liệu → áp G1 |

### 4.5 AUT – AI-assisted Automation Development

**Baseline cần có:** bộ TC đầu vào, AUT chạy được, convention của framework.

| Tiêu chí | Chỉ báo / Metric |
|---|---|
| S3 | references/ chứa convention của framework (POM, naming, locator strategy, wait strategy) |
| S5 | Có vòng run → fix → re-run; có checklist review code |
| P1 | Cung cấp code hiện có, cấu trúc framework, cách truy cập AUT |
| P4 | Phát hiện AI dùng hard wait, locator giòn, hoặc assertion yếu, rồi yêu cầu sửa |
| O1 | **First-run pass rate** trên môi trường sạch · mỗi test có assertion kiểm chứng expected result của TC |
| O2 | **TC → script coverage** = % TC trong phạm vi đã được tự động hóa |
| O3 | **Assertion-free tests = 0**; không có assertion "luôn đúng" |
| O4 | Lint pass; dùng POM; locator ưu tiên role/test-id; không có `sleep` cứng |
| O5 | **Flaky rate** khi chạy 3 lần liên tiếp = 0 · không hardcode secret · có README chạy test |

### 4.6 MNT – AI-assisted Test Maintenance

**Baseline cần có:** test suite bị hỏng sau một thay đổi UI/API, **cài thêm 1 bug sản phẩm thật** để kiểm tra xem người học có "sửa test để che bug" hay không.

| Tiêu chí | Chỉ báo / Metric |
|---|---|
| S2 | Bắt buộc **triage trước khi sửa**: phân loại test issue / product bug / env-flaky |
| S5 | Rule "không sửa expected value nếu không có bằng chứng từ requirement" |
| P1 | Cung cấp log, trace, screenshot, diff thay đổi của app |
| P4 | Bác bỏ đề xuất của AI khi AI định nới assertion hoặc skip test |
| O1 | **Triage accuracy** = % failure được phân loại đúng nguyên nhân |
| O2 | **Fix rate** = % test hỏng do test issue được sửa và pass |
| O3 | **Bug masking = 0**: không sửa/skip test để che bug thật (vi phạm → áp G3) |
| O4 | Sửa ở đúng tầng (page object/locator dùng chung, không vá từng test) |
| O5 | Diff tối thiểu; có change log giải thích từng thay đổi |

### 4.7 DEF – AI-assisted Defect Analysis & Reporting

**Baseline cần có:** danh sách bug đã cài, kèm severity/priority chuẩn.

| Tiêu chí | Chỉ báo / Metric |
|---|---|
| S3 | assets/ có template bug report; references/ có ma trận severity/priority kèm định nghĩa |
| S5 | Bắt buộc có evidence (screenshot/log); rule "không bịa thông tin môi trường" |
| P1 | Cung cấp observation thực tế, log, môi trường thật |
| P4 | Loại bỏ bug giả do AI suy đoán; kiểm tra lại severity |
| O1 | **Severity/Priority agreement** với baseline (weighted kappa, hoặc % khớp chính xác ±1 mức) |
| O2 | **Bug recall** = số bug tìm được / số bug đã cài |
| O3 | **Bug precision** = số bug hợp lệ / số bug đã report (phạt false positive) · không có môi trường/version bịa |
| O4 | Đủ trường: title, env, steps, expected/actual, evidence, severity, priority |
| O5 | **Reproducibility**: người khác làm theo steps tái hiện được bug · có giả thuyết root cause từ log (nếu có) |

---

## 5. Gate (điều kiện loại / giới hạn điểm)

| ID | Điều kiện | Hệ quả |
|---|---|---|
| G1 | Đưa PII thật, credential, hay dữ liệu mật của khách hàng vào AI, hoặc để chúng xuất hiện trong output | Competency = **0**, cần review riêng |
| G2 | Không có transcript, hoặc transcript bị cắt mất phần gọi skill | P = 0; S6 = 0 |
| G3 | Bịa nghiêm trọng: trình bày rule bịa như requirement, report bug không tồn tại như đã xác nhận, hoặc che bug thật (MNT) | Dimension O bị **giới hạn tối đa 50%** |
| G4 | (AUT/MNT) Code không chạy được | O1 tối đa = 1 |

---

## 6. Công thức tính điểm

**Điểm dimension** (0–100), tính trên các tiêu chí áp dụng được. Tiêu chí N/A thì bỏ ra và chia lại trọng số cho các tiêu chí còn lại:

```
Dim_d = 100 × Σ_i (w_i × s_i / 4) / Σ_i w_i        (s_i ∈ {0..4})
```

**Điểm competency:**

```
Comp_k = W_S,k × Dim_S + W_P,k × Dim_P + W_O,k × Dim_O     → sau đó áp gate
```

**Điều kiện Đạt competency** (không cho bù trừ):
`Comp_k ≥ 70` **và** `min(Dim_S, Dim_P, Dim_O) ≥ 50` **và** không vi phạm G1.

### 6.1 Trọng số dimension theo competency (đề xuất; chốt lại bằng AHP, xem mục 8)

| Competency | Skill | Prompt | Output | Lý do |
|---|---|---|---|---|
| REQ – Requirements Analysis | 30 | 30 | 40 | Chất lượng phụ thuộc nhiều vào ngữ cảnh được cấp và tư duy phản biện |
| DES – Test Design | 35 | 25 | 40 | Kỹ thuật thiết kế đóng gói được vào skill |
| TCG – Test Case Generation | 40 | 20 | 40 | Tác vụ lặp lại nhiều nhất, nên skill quyết định |
| TDG – Test Data Generation | 35 | 25 | 40 | Có thể script hóa; cần context về schema |
| AUT – Automation Development | 30 | 20 | 50 | Output kiểm chứng khách quan được (chạy/pass) |
| MNT – Test Maintenance | 25 | 30 | 45 | Chẩn đoán mang tính tương tác; phản biện quan trọng |
| DEF – Defect Analysis & Reporting | 30 | 30 | 40 | Cần observation thật và phải lọc được bug giả |

### 6.2 Điểm tổng theo role (trọng số competency)

| Competency | Manual QA | Auto QA |
|---|---|---|
| REQ | 20 | 10 |
| DES | 20 | 10 |
| TCG | 20 | 10 |
| TDG | 15 | 15 |
| AUT | N/A | 25 |
| MNT | N/A | 20 |
| DEF | 25 | 10 |
| **Tổng** | 100 | 100 |

```
Overall = Σ_k V_k × Comp_k / Σ_k V_k      (bỏ các competency N/A)
```

### 6.3 Quy đổi sang level

| Điểm | Level | Mô tả |
|---|---|---|
| 0–49 | L1 | Chưa đạt |
| 50–69 | L2 | Đang phát triển |
| 70–79 | L3 | Đạt |
| 80–89 | L4 | Thành thạo |
| 90–100 | L5 | Xuất sắc |

---

## 7. Ví dụ tính (TCG)

| Dim | Điểm tiêu chí (0–4) | Dim (%) |
|---|---|---|
| S | S1=4, S2=3, S3=3, S4=4, S5=2, S6=3 | 100×(.15×4+.20×3+.20×3+.10×4+.15×2+.20×3)/4 = **77.5** |
| P | P1=3, P2=3, P3=4, P4=2, P5=3 | 100×(.25×3+.20×3+.15×4+.30×2+.10×3)/4 = **70.0** |
| O | O1=3, O2=3, O3=4, O4=4, O5=2 | 100×(.30×3+.25×3+.20×4+.10×4+.15×2)/4 = **78.8** |

Comp_TCG = 0.40×77.5 + 0.20×70.0 + 0.40×78.8 = **76.5**. min(Dim) = 70 ≥ 50, không vi phạm gate → **Đạt, L3**.

---

## 8. Quy trình kiểm chứng ma trận

| Bước | Phương pháp | Ngưỡng chấp nhận |
|---|---|---|
| 1. Content validity | 3–5 SME chấm mức liên quan của từng tiêu chí (thang 1–4) → tính **I-CVI** | I-CVI ≥ 0.78; tiêu chí dưới ngưỡng thì sửa hoặc bỏ |
| 2. Trọng số | **AHP**: SME so sánh từng cặp S/P/O và từng cặp tiêu chí | Consistency Ratio (CR) < 0.10 |
| 3. Calibration set | Mỗi competency có 3 bài mẫu: tốt / trung bình / cài lỗi (như `manual-qa-sample-review-flawed`), có điểm kỳ vọng | Judge chấm lệch ≤ 1 mức trên mỗi tiêu chí |
| 4. Inter-rater reliability | 2 người chấm độc lập (hoặc 1 người + LLM judge) trên 10–15 bài | **ICC(2,k) ≥ 0.75** cho điểm tổng; **weighted κ ≥ 0.60** cho từng tiêu chí |
| 5. Item analysis (sau pilot) | Tương quan item–total; kiểm tra ceiling/floor effect | Tiêu chí mà ai cũng được 4 (hoặc ai cũng 0) → nâng chuẩn hoặc viết lại anchor |
| 6. Versioning | Mỗi lần đổi anchor hoặc trọng số thì tăng version và chạy lại calibration set | Kết quả calibration vẫn pass |

---

## 9. Các điểm cần chốt

1. **Đồng bộ với rubric AUTO hiện tại**: `QA_AI_Skills_Assessment_Rubric_AUTO.xlsx` dùng mô hình *maturity level 1–5* với tỷ lệ 80% skill / 20% output. Ma trận này đo *chất lượng*. Đề xuất giữ hai trục tách nhau: Maturity (mức tự động hóa) và Quality (ma trận này), thay vì gộp lại.
2. **Bộ input ẩn cho S6**: cần chuẩn bị cho mỗi competency một input tương đương độ khó nhưng khác bài thi.
3. **Baseline cho DES, TDG, MNT**: hiện mới có baseline cho REQ, TCG và DEF (bài manual-qa).
4. **Gate G1** đặt Competency = 0 hay chỉ cảnh cáo: cần chính sách từ phía tổ chức.
