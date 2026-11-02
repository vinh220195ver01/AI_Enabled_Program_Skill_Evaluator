# Skill Standard: chuẩn đặt tên, cấu trúc và cách viết skill

Phiên bản 1.2 · 2026-10-19 · Trạng thái: đã duyệt · Tiêu chí chấm: `skill-standard.json` v1.2

Tài liệu này là "skill standard / skill template / naming convention" mà nhóm A (Skill Standard) của cả `manual-qa` và `auto-qa` dùng để chấm. Học viên đọc để viết skill. Assessor đọc để hiểu tiêu chí A1–A4.

## Cách đọc

A1–A4 là **mã tiêu chí chấm** của nhóm A (Skill Standard):

| Mã | Tiêu chí | Chấm điều gì | Mục trong tài liệu |
|---|---|---|---|
| A1 | Naming Convention (quy ước đặt tên) | Tên thư mục skill và file `SKILL.md` | 1 |
| A2 | Structure Compliance (tuân thủ cấu trúc) | Frontmatter của SKILL.md: `---`, `name`, `description` | 1, 3.1 |
| A3 | Instruction Quality (chất lượng hướng dẫn) | Description có điều kiện kích hoạt; quy trình đánh số | 3.2, 3.3 |
| A4 | Reusability & Maintainability (tái sử dụng và bảo trì) | Không gắn cứng thông tin dự án ở bất kỳ file nào trong thư mục skill; mỗi nội dung một nguồn | 4, 4.1 |

Thiếu thành phần nào thì trượt tiêu chí nào: xem mục 6.

- **[Bắt buộc · Ax]**: được chấm ở tiêu chí Ax của nhóm A. Vi phạm là Không đạt tiêu chí đó, vì một điều kiện không thỏa là Không đạt cả tiêu chí.
- **[Khuyến nghị]**: không chấm ở nhóm A, nhưng giúp skill dễ dùng và dễ đạt các nhóm khác. Mục nào được chấm ở nhóm khác thì ghi rõ (vd auto-qa B3).
- Điều kiện chấm chính thức nằm ở `skill-standard.json`. Tài liệu này diễn giải và cho ví dụ. Nếu hai file khác nhau, `skill-standard.json` được dùng để chấm. Đánh version như sau:
  - Đổi quy tắc chấm: sửa cả hai file và tăng version của cả hai (vd 1.0 → 1.1).
  - Chỉ sửa câu chữ hoặc ví dụ trong tài liệu, không đổi quy tắc: chỉ tăng số cuối của tài liệu (vd 1.0 → 1.0.1).

---

## 1. Đặt tên (A1 Naming Convention, A2 Structure Compliance)

### Tên thư mục skill

- **[Bắt buộc · A1]** Chỉ gồm chữ thường, số và dấu gạch ngang. Dấu gạch ngang không được đứng đầu, đứng cuối hay đứng liền nhau (regex `^[a-z0-9]+(-[a-z0-9]+)*$`). Tối đa 64 ký tự.
- **[Bắt buộc · A1]** Không có chữ hoa, khoảng trắng, dấu gạch dưới `_` hay dấu tiếng Việt.
- **[Khuyến nghị]** Đặt theo hoạt động hoặc sản phẩm đầu ra, dạng `<hoạt động>-<đối tượng>`, để đọc tên là biết skill làm gì. Với auto-qa, mục "đặt tên theo deliverable" được tính ở B6.

| Tên | Kết quả | Lý do |
|---|---|---|
| `test-case-generation` | Đạt | |
| `test-requirements-analysis` | Đạt | |
| `playwright-script-development` | Đạt | |
| `Test-Case-Generation` | Không đạt | có chữ hoa |
| `test_case_generation` | Không đạt | có dấu gạch dưới |
| `test case generation` | Không đạt | có khoảng trắng |
| `phân-tích-yêu-cầu` | Không đạt | có dấu tiếng Việt |
| `-test-case` hoặc `test--case` | Không đạt | gạch ngang ở đầu hoặc liền nhau |
| `qa-helper` | Đạt A1, nhưng không nên dùng | quá chung chung, không cho biết skill làm gì |

### File SKILL.md

- **[Bắt buộc · A1]** Mỗi skill có đúng một file tên chính xác `SKILL.md` (viết hoa, đuôi `.md`), nằm ngay gốc thư mục skill.
- Không đạt nếu: file tên `skill.md`, `SKILL.MD` hay `SKILL.md.txt`; hoặc `SKILL.md` nằm trong thư mục con.

### Tên trong frontmatter

- **[Bắt buộc · A2]** Giá trị `name` trong frontmatter phải **giống hệt** tên thư mục, phân biệt hoa thường. Thư mục `test-case-generation` thì `name: test-case-generation`, không phải `name: Test Case Generation`.

### Tên file trong references/, assets/, scripts/

- **[Khuyến nghị]** Cũng đặt theo kiểu chữ thường, gạch ngang và mô tả nội dung, vd `tc-writing-rules.md`, `severity-guide.md`. Template có thể giữ tên gốc của team (vd `Test_Case_Template.xlsx`).

---

## 2. Cấu trúc thư mục (template)

```
<skill-name>/
├── SKILL.md          bắt buộc: frontmatter + quy trình
├── references/       tùy chọn: tài liệu để AI ĐỌC (quy tắc, checklist, hướng dẫn), .md / .txt
├── assets/           tùy chọn: file để DÙNG / COPY vào output (template .xlsx / .docx, ảnh)
└── scripts/          tùy chọn: code chạy được (.py / .sh)
```

- **[Bắt buộc · A1]** Chỉ có `SKILL.md` là bắt buộc. Các thư mục còn lại chỉ tạo khi cần.
- **[Khuyến nghị]** Đặt file đúng chỗ: template ở `assets/`, quy tắc ở `references/`, code ở `scripts/`. Không để file thừa: file lock `~$*.xlsx`, file output đã điền dữ liệu, thư mục lạ như `docs/` hay `templates/`. Với auto-qa, mục "assets/ chứa template, references/ chứa quy tắc" được chấm ở B3.

---

## 3. Cấu trúc SKILL.md

Bản để copy: [`SKILL.template.md`](SKILL.template.md).

### 3.1 Frontmatter (A2 Structure Compliance)

```yaml
---
name: test-case-generation
description: Use when a Test Requirement (TR) Excel list already exists and manual test cases must be written from it, one or more per TR, before test execution; exports the TC list as Excel. Do NOT use to analyse a raw user story.
---
```

- **[Bắt buộc · A2]** Dòng 1 của file là `---`, có dòng `---` đóng, và YAML ở giữa parse không lỗi.
- **[Bắt buộc · A2]** Có `name` (xem mục 1) và `description`.
- **[Bắt buộc · A2]** `description` không rỗng, tối đa 1024 ký tự, không chứa ký tự `<` hoặc `>`.
- Không đạt nếu: thiếu frontmatter; thiếu `---` đóng; frontmatter không bắt đầu ở dòng 1 (vd có dòng trống hoặc tiêu đề phía trên).
- Mẹo: nếu `description` có dấu `:` thì đặt cả câu trong dấu nháy kép, để YAML không parse lỗi.

### 3.2 Description: viết để AI chọn đúng skill (A3 Instruction Quality)

- **[Bắt buộc · A3]** Có mệnh đề kích hoạt: `Use when…`, `Use this skill when…` hoặc `Dùng khi…`.
- **[Bắt buộc · A3]** Nêu rõ **hoạt động + đầu vào** cụ thể, vd "Use when reviewing a user story before designing test cases".
- **[Bắt buộc · A3]** Đọc riêng description này thì không trùng phạm vi với các skill khác mà học viên nộp: mỗi skill làm một task khác nhau, không có hai skill cùng làm một việc. Cách kiểm tra: với mỗi skill, nghĩ ra một yêu cầu điển hình của nó, rồi xem yêu cầu đó có khớp description của skill khác không. Nếu hai skill dùng cùng loại đầu vào, nên nêu ranh giới trong description để khỏi bị coi là trùng (vd "before designing test cases", "Do NOT use for …").
- **[Bắt buộc · A3]** Điều kiện kích hoạt phải nằm trong `description`. Viết trong thân SKILL.md thì không tính, vì AI chọn skill dựa trên description.
- **[Khuyến nghị]** Nêu đầu ra (vd "exports the TC list as Excel") và ranh giới với skill gần giống (vd "Do NOT use to analyse a raw user story").

| Description | Kết quả | Lý do |
|---|---|---|
| `This skill generates test cases.` | Không đạt | chỉ nói skill là gì, không có điều kiện kích hoạt |
| `Use when testing.` | Không đạt | quá chung, không nêu hoạt động và đầu vào |
| `Use when a TR Excel list exists and manual test cases must be written from it; exports Excel.` | Đạt | có hoạt động, đầu vào và đầu ra |

### 3.3 Quy trình (A3 Instruction Quality)

- **[Bắt buộc · A3]** Có heading tên `Process`, `Workflow`, `Steps` hoặc `Quy trình`.
- **[Bắt buộc · A3]** Các bước đánh số liên tục từ 1, không nhảy số, không trùng số, tối thiểu 3 bước.
- **[Bắt buộc · A3]** Mỗi bước bắt đầu bằng một động từ hành động (Read, Identify, Write, Check, Export…).
- **[Bắt buộc · A3]** Quy trình phải nằm trong SKILL.md. Đặt quy trình chỉ trong file `references/` thì không đạt.
- Không đạt nếu: quy trình viết thành đoạn văn hoặc gạch đầu dòng `-` không đánh số; số bị nhảy hoặc trùng (vd 1, 2, 4).

```markdown
## Process

1. Open the TR Excel file and list every TR ID with its Notes.
2. Split complex TRs so that each test case verifies one behaviour (rules in `references/tc-writing-rules.md`).
3. Write specific steps with concrete test data and an observable Expected Result.
4. Check that every TR ID has at least one test case.
5. Export by copying `assets/Test_Case_Template.xlsx`, keeping its title, header and styles.
```

### 3.4 Các mục khuyến nghị khác

- **[Khuyến nghị]** `## Inputs`: đầu vào cần có, định dạng, và phải làm gì khi thiếu ("If missing, ask the user; do not guess").
- **[Khuyến nghị]** `## Output`: sản phẩm đầu ra và định dạng.
- **[Khuyến nghị]** `## Files`: mỗi file trong `references/` và `assets/` được mở ở bước nào (vd "`references/tc-writing-rules.md`: open at Step 2"). Với auto-qa, mục "mỗi file được dẫn tới đúng ở bước mở nó" được chấm ở B3.

---

## 4. Tái sử dụng và bảo trì (A4 Reusability & Maintainability)

- **[Bắt buộc · A4]** Toàn bộ thư mục skill (SKILL.md, `references/`, `assets/`, `scripts/`) không chứa thông tin gắn cứng vào một dự án hoặc khách hàng cụ thể:
  - tên dự án, tên khách hàng
  - URL nội bộ, đường dẫn máy cá nhân
  - tài khoản, mật khẩu
  - dữ liệu thật
  - business rule của dự án (vd "giỏ hàng tối đa 20 sản phẩm")
- **[Bắt buộc · A4]** Thông tin riêng của dự án được đưa vào qua đầu vào: dùng placeholder như `{project_name}`, hoặc skill ghi rõ "hỏi người dùng nếu thiếu". Không viết thẳng vào quy trình.
- **[Bắt buộc · A4]** Mỗi nội dung chỉ có **một nguồn duy nhất** (template đầu ra, checklist, danh sách severity…), để khi cần sửa chỉ phải sửa một chỗ:
  - Template đã nằm ở `assets/` thì không chép lại vào SKILL.md (hai bản là hai nguồn).
  - Nhiều skill dùng chung một nội dung thì không mỗi skill giữ một bản copy. Cách tổ chức nội dung dùng chung giữa các skill đang chờ course owner xác nhận (xem "Câu hỏi còn mở").
- Không đạt nếu:
  - tên dự án, URL, đường dẫn hoặc thông tin đăng nhập bị viết cứng trong skill;
  - skill chỉ chạy được cho đúng một dự án (vd "Kiểm tra theo màn hình Login của app ABC");
  - nhiều skill cùng giữ bản copy riêng của một nội dung.

| Câu trong skill | Kết quả |
|---|---|
| `Log in to https://staging.myshop.vn with admin / 123456.` | Không đạt: URL và tài khoản viết cứng |
| `Check the Login screen of app ABC.` | Không đạt: chỉ dùng được cho một dự án |
| `Log in to {app_url} with the test account the user provides. If missing, ask the user.` | Đạt |
| `references/business-rules.md` ghi "A cart holds at most 20 items" của dự án đang test | Không đạt: business rule của dự án nằm trong skill |

### 4.1 Đặt thông tin ở đâu

Skill chỉ chứa **cách làm**, phần dùng lại được cho mọi dự án. **Nội dung** của từng dự án được đưa vào lúc chạy.

| Loại thông tin | Đặt ở đâu | Liên quan |
|---|---|---|
| Các bước làm task | `SKILL.md`, mục `## Process` | A3 |
| Đặc tả task của một lần chạy (user story, AC, requirement, mockup) | **Không để trong skill.** Đưa vào lúc chạy (đính kèm file hoặc dán vào chat). `SKILL.md` chỉ khai báo cần đầu vào gì ở `## Inputs` và ghi "thiếu thì hỏi" | A4; manual B2 (tách dữ liệu đầu vào của từng lần chạy) |
| Kiến thức QA chung (kỹ thuật test design, quy tắc viết test case, hướng dẫn severity, checklist review) | `references/` của skill | Đúng với mọi dự án |
| Template đầu ra | `assets/` của skill | A4 (một nguồn); auto B3 |
| Domain knowledge của dự án (business rule, glossary, màn hình, luồng, môi trường, tài khoản test) | **Ngoài thư mục skill**: file knowledge của dự án, vd `docs/knowledge/*.md` trong repo dự án. Skill nhận đường dẫn qua đầu vào (vd `{knowledge_dir}`) hoặc hỏi người dùng, rồi đọc phần cần thiết ở một bước cụ thể | A4; manual B2 (tách project/domain knowledge); auto B2 (bước ghi kết quả khám phá vào file knowledge); auto B3 (không đưa dữ liệu dự án vào file của skill) |

Phép thử: *"Nếu dùng skill này cho một dự án khác, câu này còn đúng không?"* Còn đúng thì để trong skill. Không đúng thì đó là đầu vào hoặc project knowledge.

```markdown
## Inputs

- {user_story}: the user story and acceptance criteria to work on, as attached files or pasted text. If missing, ask the user; do not guess.
- {knowledge_dir}: the project's knowledge folder (business rules, glossary, screens). If missing, ask the user.

## Process

1. Read {user_story} and the files in {knowledge_dir} that this task needs, and list the acceptance criteria.
```

---

## 5. Checklist tự kiểm tra trước khi nộp

| # | Kiểm tra | Tiêu chí |
|---|---|---|
| 1 | Tên thư mục đúng regex `^[a-z0-9]+(-[a-z0-9]+)*$`, tối đa 64 ký tự | A1 |
| 2 | Có đúng một file `SKILL.md` ở gốc thư mục skill | A1 |
| 3 | Dòng 1 là `---`, có `---` đóng, YAML parse được | A2 |
| 4 | `name` giống hệt tên thư mục | A2 |
| 5 | `description` không rỗng, tối đa 1024 ký tự, không có `<` `>` | A2 |
| 6 | `description` có "Use when…" + hoạt động + đầu vào; không trùng task với skill khác mình nộp | A3 |
| 7 | Có heading Process / Workflow / Steps / Quy trình; tối thiểu 3 bước đánh số liên tục từ 1; mỗi bước bắt đầu bằng động từ | A3 |
| 8 | Không có tên dự án, khách hàng, URL, đường dẫn, tài khoản, dữ liệu thật hay business rule của dự án ở bất kỳ file nào trong thư mục skill | A4 |
| 9 | Thông tin dự án đi vào qua placeholder hoặc "hỏi người dùng nếu thiếu" | A4 |
| 10 | Template và checklist chỉ có một bản; không chép vào SKILL.md hay sang skill khác | A4 |

## 6. Thiếu thành phần thì trượt tiêu chí nào

Theo [`SKILL.template.md`](SKILL.template.md). Một điều kiện không thỏa là Không đạt cả tiêu chí đó. Cột "Nhóm khác" chỉ để tham khảo: các mục đó được chấm ở nhóm B, không phải nhóm A.

| Thành phần | Thiếu hoặc sai thì trượt (nhóm A) | Nhóm khác |
|---|---|---|
| Tên thư mục kebab-case | A1 | |
| File `SKILL.md` ở gốc thư mục | A1. Không có SKILL.md thì không có frontmatter, description và quy trình, nên A2 và A3 cũng trượt | |
| Frontmatter (`---` ở dòng 1 và `---` đóng, YAML hợp lệ) | A2 | |
| `name` giống hệt tên thư mục | A2 | |
| `description` | Rỗng hoặc không có: A2 và A3. Có nhưng thiếu "Use when…", hoạt động hoặc đầu vào, hoặc trùng task với skill khác: A3 | auto B3: description phải có trigger clause |
| Heading `## Process` (hoặc Workflow / Steps / Quy trình) | A3 | |
| Các bước đánh số (từ 1, liên tục, tối thiểu 3, mỗi bước bắt đầu bằng động từ) | A3 | |
| `## Inputs` | Không trượt nếu chỉ thiếu mục này. Nhưng nếu skill cần thông tin dự án mà không khai báo đầu vào, lại viết cứng giá trị vào skill, thì trượt A4 | manual B2, B3: học viên đưa đủ và đúng đầu vào khi chạy |
| `## Output` | Không trượt | |
| `## Files` (file nào mở ở bước nào) | Không trượt | auto B3: mỗi file trong `references/`, `assets/` phải được dẫn tới ở đúng bước mở nó |
| `references/` | Không trượt (thư mục tùy chọn) | auto B3: phải chứa quy tắc của sub-category; auto B6: một ví dụ output tốt trong `references/` là 1 trong 3 mục SHOULD |
| `assets/` (template đầu ra) | Không trượt nếu template chỉ có một bản. Trượt A4 nếu template có hai bản (vd vừa trong SKILL.md vừa ở `assets/`, hoặc mỗi skill một bản copy) | auto B3: template phải ở `assets/`, nhúng template vào SKILL.md là trượt; auto B6: template chỉ nằm trong SKILL.md hoặc prompt là một điều Fail |
| `scripts/` | Không trượt | |

## Câu hỏi còn mở

- Nhiều skill dùng chung một nội dung (A4, "một nguồn duy nhất"): nên đặt ở đâu? Ví dụ một skill giữ file và các skill khác tham chiếu tới bằng đường dẫn tương đối, hay có một thư mục dùng chung?
