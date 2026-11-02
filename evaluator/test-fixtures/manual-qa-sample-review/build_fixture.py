#!/usr/bin/env python3
"""
Builds the "perfect trainee" sample for the Submit-a-Product-Review exam from the trainer's own
files, so it contains every finding of the baseline.

Inputs (read only):  --source <folder holding exam/ and baseline/ from the trainer>
  exam/User Story for My Shop.docx
  baseline/Test_Requirement.xlsx, baseline/Test_Case.xlsx

What it writes into this fixture folder:
  exam/                 the docx, a text version of it, and its mockup images
  baseline/             the trainer's workbooks (copied) and baseline.json (via import_baseline_xlsx.py)
  submission/skills/    two clean skills (test-requirements-analysis, test-case-generation)
  submission/outputs/   the TR and TC workbooks = the baseline workbooks, i.e. a trainee who found everything
  submission/chat-transcript.md   built from the baseline's own Appendix and Python script
  expected/assessment_result.json no errors on any assessed criterion

Usage:  python build_fixture.py --source "D:/.../judge_example from Vinh"
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
SKILL_SCRIPTS = HERE.parents[1] / "skills" / "skill-evaluator" / "scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
from import_baseline_xlsx import read_workbook  # noqa: E402

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
TR_TITLE, TC_TITLE = "Requirements Traceability Matrix", "Test Case List"
TR_H = ["AC ID", "Acceptance Criteria", "TR ID", "Test Requirements", "Notes"]
TC_H = ["TR ID", "TC ID", "TC Summary", "Pre-Condition", "Steps", "Expected Result", "Notes"]


def col(i):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]


def write_template(path, sheet, title, headers):
    """Empty template: title in A1, header in row 4 (the trainer's layout)."""
    def cell(r, c, v):
        return f'<c r="{col(c)}{r}" t="inlineStr"><is><t>{escape(v)}</t></is></c>'
    rows = f'<row r="1">{cell(1, 0, title)}</row><row r="4">' + "".join(cell(4, i, h) for i, h in enumerate(headers)) + "</row>"
    cols = "<cols>" + "".join(f'<col min="{i+1}" max="{i+1}" width="26" customWidth="1"/>' for i in range(len(headers))) + "</cols>"
    sheet_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                 f'{cols}<sheetData>{rows}</sheetData></worksheet>')
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        z.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml", f'<?xml version="1.0" encoding="UTF-8"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="{escape(sheet)}" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml)


SKILL_TR = """---
name: test-requirements-analysis
description: Use when a user story with acceptance criteria (and optional mockups) is given and a Test Requirement (TR) list is needed before any test case is written; finds ambiguities and clarification questions, then exports the TR list as Excel. Do NOT use to write test cases from an existing TR list.
---

# Test Requirements Analysis

## Process

1. Read the user story, its acceptance criteria (AC) and any mockup; give each AC an ID.
2. Separate facts, assumptions and missing information; never mix the three.
3. Identify ambiguous points, edge cases and risks per AC, tagging each with the origin tags in `references/tr-writing-rules.md`.
4. Draft clarification questions in two groups: "Must ask" (blocks test design) and "Nice to confirm".
5. Write the Test Requirements, one verifiable behaviour each, with an origin tag in Notes.
6. Export by copying `assets/Test_Requirement_Template.xlsx`, keeping its title, header, styles and column widths, and fill the sheet "Test Requirement".

## Files

- `references/tr-writing-rules.md`: open at Step 3 (origin tags) and again at Step 5 (wording rules).
- `assets/Test_Requirement_Template.xlsx`: open at Step 6; copy it, never rebuild it.
"""

RULES_TR = """# TR writing rules

- One Test Requirement states one verifiable behaviour, not a test step.
- Every AC gets at least one TR. A TR that traces to no AC gets `N/A` in AC ID.
- IDs run continuously (e.g. TR_001, TR_002, ...) with no gaps.
- Every Notes cell starts with its origin: `Fact`, `Assumption`, `Missing info`, `Edge case (...)` or `Risk (...)`.
- `Missing info` rows say `Must ask` when test design is blocked without the answer, otherwise `Nice to confirm`.
- Anything the source does not state is never written as a confirmed requirement: tag it `Assumption` or `Missing info`.
- Mockup content may be used as a source; say so in Notes.
"""

SKILL_TC = """---
name: test-case-generation
description: Use when a Test Requirement (TR) Excel list already exists and manual test cases must be written from it, one or more per TR, before test execution; exports the TC list as Excel. Do NOT use to analyse a raw user story.
---

# Test Case Generation

## Process

1. Open the TR Excel file and list every TR ID with its Notes.
2. Split complex TRs into several test cases so that each test case verifies one behaviour (rules in `references/tc-writing-rules.md`).
3. Write specific steps with concrete test data and an observable Expected Result.
4. Mark each TR tagged `Missing info — Must ask` as BLOCKED: its Expected Result starts with `TBD —` and its Notes start with `BLOCKED —`.
5. Carry the TR Notes tags (Assumption, Edge case, Risk, Nice to confirm) into the TC Notes.
6. Check that every TR ID has at least one test case, and that every edge case has its own.
7. Export by copying `assets/Test_Case_Template.xlsx`, keeping its title, header, styles and column widths, and fill the sheet "TC List".

## Files

- `references/tc-writing-rules.md`: open at Step 2 and again at Step 3.
- `assets/Test_Case_Template.xlsx`: open at Step 7; copy it, never rebuild it.
"""

RULES_TC = """# TC writing rules

- One test case verifies one behaviour; split a TR when it has several.
- Steps contain concrete test data (e.g. `qa.tester@example.com`, a 20-character string), never "enter valid data".
- An Expected Result states at least one observable outcome: message text, displayed value, destination screen, field or button state, data saved or not saved.
- Vague phrases are not allowed on their own: "works correctly", "as expected", "displayed correctly", "no error", "success", "OK".
- A BLOCKED test case keeps its TR ID, uses `TBD —` at the start of Expected Result and `BLOCKED —` at the start of Notes.
- Every TR ID of the TR file appears at least once in the TR ID column.
"""


def docx_text(path):
    z = zipfile.ZipFile(path)
    body = ET.fromstring(z.read("word/document.xml")).find(W + "body")
    lines = []
    for p in body.iter(W + "p"):
        t = "".join(x.text or "" for x in p.iter(W + "t")).strip()
        if t:
            lines.append(t)
    return z, lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, type=Path)
    a = ap.parse_args()
    src_exam = a.source / "exam" / "User Story for My Shop.docx"
    src_tr = a.source / "baseline" / "Test_Requirement.xlsx"
    src_tc = a.source / "baseline" / "Test_Case.xlsx"
    for p in (src_exam, src_tr, src_tc):
        if not p.is_file():
            print(f"error: missing {p}", file=sys.stderr)
            return 1

    # ---- exam ----------------------------------------------------------------------------
    ex = HERE / "exam"
    ex.mkdir(exist_ok=True)
    shutil.copy(src_exam, ex / src_exam.name)
    z, lines = docx_text(src_exam)
    for i, name in enumerate(sorted(n for n in z.namelist() if n.startswith("word/media/")), start=1):
        (ex / f"mockup-{i}{Path(name).suffix}").write_bytes(z.read(name))
    md = ["# Exam: Submit a Product Review (text of the Word file)", ""]
    md += [f"- {l}" if i > 3 else l for i, l in enumerate(lines)]
    md += ["", "The Word file also holds two mockup images, saved here as `mockup-1.png` and `mockup-2.png`."]
    (ex / "user-story.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # ---- baseline ------------------------------------------------------------------------
    bd = HERE / "baseline"
    bd.mkdir(exist_ok=True)
    shutil.copy(src_tr, bd / src_tr.name)
    shutil.copy(src_tc, bd / src_tc.name)
    r = subprocess.run([sys.executable, str(SKILL_SCRIPTS / "import_baseline_xlsx.py"),
                        "--tr", str(bd / src_tr.name), "--tc", str(bd / src_tc.name),
                        "--assessment-id", "US-VP02-submit-product-review",
                        "--requirement-source", "exam/User Story for My Shop.docx",
                        "--out", str(bd / "baseline.json")], capture_output=True, text=True, encoding="utf-8")
    print(r.stdout, r.stderr, sep="")
    if r.returncode:
        return r.returncode

    # ---- submission: skills --------------------------------------------------------------
    sk = HERE / "submission" / "skills"
    if sk.exists():
        shutil.rmtree(sk)
    (sk / "test-requirements-analysis" / "references").mkdir(parents=True)
    (sk / "test-case-generation" / "references").mkdir(parents=True)
    (sk / "test-requirements-analysis" / "SKILL.md").write_text(SKILL_TR, encoding="utf-8")
    (sk / "test-requirements-analysis" / "references" / "tr-writing-rules.md").write_text(RULES_TR, encoding="utf-8")
    (sk / "test-case-generation" / "SKILL.md").write_text(SKILL_TC, encoding="utf-8")
    (sk / "test-case-generation" / "references" / "tc-writing-rules.md").write_text(RULES_TC, encoding="utf-8")
    write_template(sk / "test-requirements-analysis" / "assets" / "Test_Requirement_Template.xlsx", "Test Requirement", TR_TITLE, TR_H)
    write_template(sk / "test-case-generation" / "assets" / "Test_Case_Template.xlsx", "TC List", TC_TITLE, TC_H)

    # ---- submission: outputs = the baseline workbooks ------------------------------------
    out = HERE / "submission" / "outputs"
    out.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_tr, out / "Test_Requirement_US-VP02.xlsx")
    shutil.copy(src_tc, out / "Test_Case_US-VP02.xlsx")

    # ---- submission: transcript, from the baseline's own appendix and script ---------------
    tr_book, tc_book = read_workbook(src_tr), read_workbook(src_tc)
    tr_rows = tr_book["Test Requirement"]["rows"]
    tr_data = [(r.get("A", ""), r.get("B", ""), r.get("C", ""), r.get("D", ""), r.get("E", ""))
               for n, r in sorted(tr_rows.items()) if n > 4 and r.get("C")]
    app = tr_book["Appendix"]["rows"]
    appendix = [app[n]["A"] for n in sorted(app) if "A" in app[n]]
    script_rows = tc_book["Python script"]["rows"]
    tc_script = "\n".join(script_rows.get(n, {}).get("A", "") for n in range(1, max(script_rows) + 1))

    tr_code = ("from pathlib import Path\nimport shutil\nfrom openpyxl import load_workbook\n\n"
               "BASE = Path('/mnt/data')\n"
               "TEMPLATE = BASE / 'skills' / 'test-requirements-analysis' / 'assets' / 'Test_Requirement_Template.xlsx'\n"
               "OUT = BASE / 'Test_Requirement_US-VP02.xlsx'\n"
               "shutil.copy(TEMPLATE, OUT)\nwb = load_workbook(OUT)\nws = wb['Test Requirement']\n\n"
               "rows = [  # (AC ID, Acceptance Criteria, TR ID, Test Requirements, Notes)\n"
               + "".join(f"    {t!r},\n" for t in tr_data) +
               "]\nfor i, row in enumerate(rows, start=5):\n    for c, v in enumerate(row, start=1):\n        ws.cell(i, c, v)\nwb.save(OUT)\nprint(len(rows), 'TR rows written to', OUT.name)\n")

    t = []
    t += ["# Chat transcript (sample trainee, built from the trainer's baseline)", "",
          "> Two skills are installed: `test-requirements-analysis` and `test-case-generation`.", "", "---", "",
          "## Turn 1: requirements analysis", "",
          "**User:** I attached `User Story for My Shop.docx`. Please analyse it.", "",
          "**Assistant:**", "",
          "`[tool call] Skill(test-requirements-analysis)`",
          "`[tool call] Read(skills/test-requirements-analysis/SKILL.md)`",
          "`[tool call] Read(skills/test-requirements-analysis/references/tr-writing-rules.md)`", "",
          "### Requirements analysis", ""]
    section_titles = {"1. Facts", "2. Assumptions", "3. Missing", "4. Risks", "5. Clarification"}
    for line in appendix:
        if line.startswith(("Excel output", "AC_01, AC_02")) or "TR_001" in line:
            break
        if line[:2] in {"1.", "2.", "3.", "4.", "5."}:
            t += ["", f"#### {line}", ""]
        elif line in ("Must ask", "Nice to confirm"):
            t += ["", f"**{line}**", ""]
        elif line.startswith("Main gaps"):
            t += [line, ""]
        else:
            t.append(f"- {line}")
    t += ["", "`[tool call] Bash(python build_tr.py)`", "", "```python", tr_code, "```", "",
          "Created `Test_Requirement_US-VP02.xlsx` by copying the template.", "", "---", "",
          "## Turn 2: test cases", "",
          "**User:** Now generate the test cases from the TR list.", "",
          "**Assistant:**", "",
          "`[tool call] Skill(test-case-generation)`",
          "`[tool call] Read(skills/test-case-generation/SKILL.md)`",
          "`[tool call] Read(skills/test-case-generation/references/tc-writing-rules.md)`",
          "`[tool call] Bash(python build_tc.py)`", "", "```python", tc_script, "```", "",
          "Created `Test_Case_US-VP02.xlsx`: every TR ID has at least one test case; the Must-ask TRs are BLOCKED.", ""]
    (HERE / "submission" / "chat-transcript.md").write_text("\n".join(t), encoding="utf-8")

    # ---- expected result -----------------------------------------------------------------
    base = json.loads((bd / "baseline.json").read_text(encoding="utf-8"))
    skipped = {x["criterion"] for x in base["not_assessed"]}
    ids = [f"A{i}" for i in range(1, 9)] + [f"B{i}" for i in range(1, 5)] + [f"C{i}" for i in range(1, 8)]
    (HERE / "expected").mkdir(exist_ok=True)
    (HERE / "expected" / "assessment_result.json").write_text(json.dumps({
        "eval_id": 1, "layer": "L1",
        "criteria": {c: {"errors": [], "na": False, "note": ""} for c in ids if c not in skipped},
        "advisory_flags": [],
        "grading_notes": ["Ideal result: this trainee's outputs ARE the trainer's baseline, so every assessed criterion should have 0 errors. A real judge may still report a few; each one needs a quoted ref and is worth reading."]},
        indent=2), encoding="utf-8")
    print("fixture built; not assessed:", sorted(skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main())
