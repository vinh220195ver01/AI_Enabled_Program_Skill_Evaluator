#!/usr/bin/env python3
"""
Scores a profile-based assessment and writes one scoring sheet (Excel + Markdown) plus JSON.

Inputs:
  --plan            evals/eval_plan.json        (from build_plan_from_profile.py)
  --result          assessment_result.json      (from agents/manual-qa-assessment-judge.md)
  --human           human_decisions.json        (optional; the human's call on advisory flags)
  --submission-dir  root folder of the trainee's submission (optional; lets the script
                    check that every evidence ref points at a file that exists)
  --out-dir         report/

A plan with `scoring_model: weighted-pass-fail` is rendered by render_weighted() (see its
docstring for the result and human file shapes): per competency, criterion verdicts from
criterion_rules.py, group points (5 per group), competency score = A*0.2 + B*0.5 + C*0.3,
pass at 3 for every competency plus a passing gate; the skill -> competency mapping and the
conditions still waiting for a person are listed. The text below is the old points model.

Scoring (the judge reports counts of errors, never points; this script does the maths):
  criterion points = max_points - penalty_per_error x errors, floored at 0
  a criterion marked na scores full max_points (the trainee is not penalised for a
  criterion that does not apply to them) and is flagged in the report
  group total = sum of its criteria; total = sum of groups
  PASS when total >= pass_threshold

Advisory flags (criteria with `advisory`, e.g. C6 severity deviation): the judge only
records them. A flag costs nothing until a human decides:
  human_decisions.json = {"C6-severity:BUG-02": {"decision": "fail", "errors": 1}}
  decision "fail" adds `errors` (default 1) to that criterion; "pass" adds nothing.
While any flag has no decision, the report status is "provisional", not final.

Evidence refs: every error's `where` must be a path relative to the submission root plus an
optional locator:  path[:line] | path!Sheet!Cell | path#Heading
  skills/Test-Case-Generation/SKILL.md:17
  outputs/tc-list.xlsx!TC List!F7
  chat-transcript.md#Turn 2
A `where` with no file path is shown as "(no file ref)", and with --submission-dir a path
that does not exist is shown as "(ref not found)". Both are also listed under Notes.

Outputs: assessment_scoring_sheet.xlsx (the table), assessment_report.md, assessment_report.json

Usage:
    python scripts/render_assessment_report.py --plan evals/eval_plan.json \
        --result L1/1/run-1/assessment_result.json --out-dir report/ \
        [--human decisions.json] [--submission-dir path/to/submission]
"""
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

QUOTE_MAX = 90
HEADERS = ["Competency", "Category", "Evaluation Criteria", "Max", "Points", "Errors",
           "Evidence/Notes"]
WIDTHS = [30, 22, 48, 8, 9, 9, 70]


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def ref_path(where):
    """The file-path part of an evidence ref, or None when there is none."""
    p = re.split(r"[:!#]", where or "", maxsplit=1)[0].strip()
    return p if re.search(r"\.[A-Za-z0-9]+$|/", p) else None


def short(text, n=QUOTE_MAX):
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[: n - 1] + "…"


def relativize(where, sub_dir):
    """Strip the submission root (or any absolute prefix up to it) so the shared report shows
    submission-relative paths only, e.g. skills/x/SKILL.md:12 -- never C:\\...\\submission\\skills/x/SKILL.md."""
    where = str(where or "")
    if sub_dir is not None:
        for root in {str(Path(sub_dir)), str(Path(sub_dir).resolve())}:
            for sep_root in (root, root.replace("\\", "/")):
                idx = where.replace("\\", "/").find(sep_root.replace("\\", "/") + "/")
                if idx != -1:
                    where = where[:idx] + where.replace("\\", "/")[idx + len(sep_root) + 1:]
                    break
    where = where.replace("\\", "/")
    m = re.match(r"^(?:[A-Za-z]:)?/.*?/submission/(.+)$", where)   # fallback: anything ending in /submission/<rel>
    return m.group(1) if m else where


def check_ref(where, sub_dir):
    """Returns (display, problem or None). `where` is displayed submission-relative."""
    where = relativize(where, sub_dir)
    path = ref_path(where)
    if path is None:
        return f"{where} (no file ref)", "no file ref"
    if sub_dir is not None and not (sub_dir / path).exists():
        return f"{where} (ref not found)", "ref not found"
    return where, None


def col_letter(i):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]


STYLES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
    '<fonts count="4"><font><sz val="11"/><name val="Calibri"/></font>'
    '<font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font>'
    '<font><b/><sz val="16"/><color rgb="FF1F5C99"/><name val="Calibri"/></font>'
    '<font><b/><sz val="11"/><name val="Calibri"/></font></fonts>'
    '<fills count="5"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill>'
    '<fill><patternFill patternType="solid"><fgColor rgb="FF1F3864"/></patternFill></fill>'
    '<fill><patternFill patternType="solid"><fgColor rgb="FFFFF2CC"/></patternFill></fill>'
    '<fill><patternFill patternType="solid"><fgColor rgb="FFE7E6E6"/></patternFill></fill></fills>'
    '<borders count="2"><border/><border><left style="thin"/><right style="thin"/><top style="thin"/><bottom style="thin"/></border></borders>'
    '<cellStyleXfs count="1"><xf/></cellStyleXfs>'
    '<cellXfs count="6">'
    '<xf fontId="0" fillId="0" borderId="1" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>'
    '<xf fontId="1" fillId="2" borderId="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center" wrapText="1"/></xf>'
    '<xf fontId="2" fillId="0" borderId="0" applyFont="1"/>'
    '<xf fontId="0" fillId="3" borderId="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>'
    '<xf fontId="3" fillId="4" borderId="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>'
    '<xf fontId="0" fillId="0" borderId="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="top"/></xf>'
    '</cellXfs>'
    '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>'
    '</styleSheet>'
)
S_CELL, S_HEAD, S_TITLE, S_EVID, S_SUB, S_NUM = range(6)


def write_xlsx(path, title, subtitle, table):
    """table: list of rows; each row is a list of (value, style) for the 8 columns."""
    def cell(r, c, v, s):
        ref = f"{col_letter(c)}{r}"
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            return f'<c r="{ref}" s="{s}"><v>{v}</v></c>'
        return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(str(v))}</t></is></c>'

    rows = [f'<row r="1">{cell(1, 0, title, S_TITLE)}</row>',
            f'<row r="2">{cell(2, 0, subtitle, S_CELL)}</row>',
            '<row r="4" ht="32" customHeight="1">' + "".join(cell(4, i, h, S_HEAD) for i, h in enumerate(HEADERS)) + "</row>"]
    for n, row in enumerate(table, start=5):
        rows.append(f'<row r="{n}">' + "".join(cell(n, i, v, s) for i, (v, s) in enumerate(row)) + "</row>")
    cols = "<cols>" + "".join(f'<col min="{i+1}" max="{i+1}" width="{w}" customWidth="1"/>' for i, w in enumerate(WIDTHS)) + "</cols>"
    sheet = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
             '<sheetViews><sheetView workbookViewId="0"><pane ySplit="4" topLeftCell="A5" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>'
             f'{cols}<sheetData>{"".join(rows)}</sheetData></worksheet>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml",
                   '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
                   '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        z.writestr("_rels/.rels",
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml",
                   '<?xml version="1.0" encoding="UTF-8"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   '<sheets><sheet name="Scoring Sheet" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
                   '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
        z.writestr("xl/styles.xml", STYLES)
        z.writestr("xl/worksheets/sheet1.xml", sheet)


SUMMARY_HEADERS = ["ID", "Name", "Final Result", "Competency", "Score", "Comments"]
SUMMARY_WIDTHS = [11, 18, 14, 34, 11, 26]


def write_summary_xlsx(path, rows, merges):
    """rows: list of 6-value rows (ID, Name, Final Result, Competency, Score, Comments), header excluded.
    merges: list of (first_row, last_row) 1-based data-row spans (relative to row 2) to merge columns A-C over,
    matching the template's one-trainee-per-block layout."""
    def cell(r, c, v, s):
        ref = f"{col_letter(c)}{r}"
        if v is None:
            return f'<c r="{ref}" s="{s}"/>'
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            return f'<c r="{ref}" s="{s}"><v>{v}</v></c>'
        return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(str(v))}</t></is></c>'

    xml_rows = ['<row r="1">' + "".join(cell(1, i, h, S_HEAD) for i, h in enumerate(SUMMARY_HEADERS)) + "</row>"]
    for n, row in enumerate(rows, start=2):
        xml_rows.append(f'<row r="{n}">' + "".join(cell(n, i, v, S_CELL) for i, v in enumerate(row)) + "</row>")
    merge_refs = []
    for first, last in merges:
        if last > first:
            for col in "ABC":
                merge_refs.append(f'<mergeCell ref="{col}{first}:{col}{last}"/>')
    merge_xml = f'<mergeCells count="{len(merge_refs)}">{"".join(merge_refs)}</mergeCells>' if merge_refs else ""
    cols = "<cols>" + "".join(f'<col min="{i+1}" max="{i+1}" width="{w}" customWidth="1"/>' for i, w in enumerate(SUMMARY_WIDTHS)) + "</cols>"
    sheet = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
             '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>'
             f'{cols}<sheetData>{"".join(xml_rows)}</sheetData>{merge_xml}</worksheet>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml",
                   '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
                   '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        z.writestr("_rels/.rels",
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml",
                   '<?xml version="1.0" encoding="UTF-8"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   '<sheets><sheet name="Summary" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
                   '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
        z.writestr("xl/styles.xml", STYLES)
        z.writestr("xl/worksheets/sheet1.xml", sheet)


def _flag(r):
    return r.get("met") if isinstance(r, dict) else r


def _apply_human(results, decisions, label):
    """Fill the conditions the judge left open (met null) from {position: bool}."""
    out = []
    for i, r in enumerate(results):
        if _flag(r) is None and str(i) in decisions:
            r = {**(r if isinstance(r, dict) else {}), "met": bool(decisions[str(i)]), "evidence": f"decided by a person ({label})"}
        out.append(r)
    return out


def loc_lines(locs, root):
    """One line per failure location: where to open the file, and what to look for."""
    out = []
    for lo in locs or []:
        f = lo.get("file", "?")
        path = str((root / f).resolve()) if root is not None else f
        if "absent" in lo:
            where = f"{path}" + (f" | sheet {lo['sheet']}" if lo.get("sheet") else "")
            out.append(f"\n    MISSING in {where}: {lo['absent']}")
        elif "sheet" in lo:
            out.append(f"\n    EXCEL {path} | sheet \"{lo['sheet']}\" | cell {lo['cell']} | \"{lo.get('quote', '')}\"")
        else:
            out.append(f"\n    FILE {path} | line {lo.get('line', '?')} | \"{lo.get('quote', '')}\"")
    return "".join(out)


def evidence_block(n, who, cond, pending, why, locs, root):
    """One numbered, labelled block per unmet condition, for the Evidence/Notes cell."""
    lines = [f"#{n} " + (f"[{who}] " if who else "") + ("(PENDING person) " if pending else "") + "Condition: " + short(cond, 160),
             f"   Why: {short(why, 300) or 'not met'}"]
    for lo in locs or []:
        f = lo.get("file", "?")
        path = f.replace("\\", "/")
        if "absent" in lo:
            lines.append(f"   Missing: {lo['absent']}")
            lines.append(f"   In: {path}" + (f" (sheet {lo['sheet']})" if lo.get("sheet") else ""))
        elif "sheet" in lo:
            lines.append(f"   Where: {path} (sheet \"{lo['sheet']}\", cell {lo['cell']})")
            lines.append(f"   Quote: \"{lo.get('quote', '')}\"")
        else:
            lines.append(f"   Where: {path} (line {lo.get('line', '?')})")
            lines.append(f"   Quote: \"{lo.get('quote', '')}\"")
    return "\n".join(lines)


def render_weighted(a, plan, result, human):
    """Report for a weighted-pass-fail plan: per competency, group points and a competency score.

    result  = {"skills": [{"name", "competency", "reason"}],
               "skill_results": {skill: {"A1": [cond, ...], ...}},          # group A, per skill
               "competency_results": {competency: {"B1": [...], ..., "C4": [...]}},
               "gate": {"verdict": "pass" | "fail" | "pending", "note": "..."}}
      cond = true | false | {"met": true | false | null, "evidence": "..."}   (null = a person grades it)
    human   = {"conditions": {"<competency>/<criterion>": {"<position>": true}},
               "gate": {"verdict": "pass" | "fail", "note": "..."},
               "skill_to_competency": {"<skill>": "<competency>"},          # trainer corrections
               "mapping_reviewed": true}
    """
    import criterion_rules as cr
    import profile_loader as pl

    asm = plan["scope"]["assessment"]
    profile_dir = Path(__file__).resolve().parent.parent / "profiles" / asm["profile"]
    stale = pl.check_plan_fresh(asm, profile_dir)
    if stale:
        print(f"error: eval_plan.json is stale (profile {asm['profile']!r} changed since it was built):",
              file=sys.stderr)
        for p in stale:
            print(f"  - {p}", file=sys.stderr)
        return 1
    root = a.submission_dir
    sub = asm.get("sub_category")
    profile = {"groups": asm["groups"], "scoring": asm["scoring"],
               "criteria": [{**c, "pass_rule": c["effective_rule"]} for c in asm["criteria"]]}
    by_id = {c["id"]: c for c in asm["criteria"]}
    top = asm["scoring"]["group_points"]
    notes = []

    mapping = {}
    for s in result.get("skills", []):
        mapping[s["name"]] = {"competency": s["competency"], "reason": s.get("reason", ""), "corrected": False}
    for skill, comp in human.get("skill_to_competency", {}).items():
        if skill in mapping:
            mapping[skill] = {**mapping[skill], "competency": comp, "corrected": True}
    for skill, m in mapping.items():
        if m["competency"] not in asm["competencies"]:
            print(f"error: skill {skill!r} is mapped to {m['competency']!r}, not one of {asm['competencies']}", file=sys.stderr)
            return 1
    uncovered = [s for s in result.get("skill_results", {}) if s not in mapping]
    if uncovered:
        print(f"error: skill_results for skills not in `skills`: {uncovered}", file=sys.stderr)
        return 1
    a_ids = [c["id"] for c in asm["criteria"] if c["group"] == "A"]
    rest_ids = [c["id"] for c in asm["criteria"] if c["group"] != "A"]

    comps, any_pending = [], False
    for comp in asm["competencies"]:
        skills = [s for s, m in mapping.items() if m["competency"] == comp]
        merged, skill_outcomes = {}, {}
        for s in skills:
            res = result.get("skill_results", {}).get(s)
            if res is None:
                print(f"error: no skill_results for skill {s!r}", file=sys.stderr)
                return 1
            res = {k: _apply_human(v, human.get("conditions", {}).get(f"{comp}/{s}/{k}", {}), f"{s}/{k}") for k, v in res.items()}
            missing = [i for i in a_ids if i not in res]
            if missing:
                print(f"error: skill {s!r} has no results for {missing}", file=sys.stderr)
                return 1
            skill_outcomes[s] = cr.evaluate_all(profile, {i: res[i] for i in a_ids}, sub)
        for i in a_ids:
            outs = [skill_outcomes[s][i] for s in skills]
            if not outs:
                merged[i] = {"verdict": "fail", "score": 0.0, "met": 0, "total": 0, "pending": 0}
                continue
            scores = [o["score"] for o in outs]
            avg_score = None if any(x is None for x in scores) else round(sum(scores) / len(scores), 4)
            if len(outs) == 1:
                # single skill: keep the criterion's own pass_rule verdict (M-10/M-11 only
                # changes how *several* skills of one competency are combined, below)
                verdict = outs[0]["verdict"]
            elif avg_score is None or any(o["verdict"] == "pending" for o in outs):
                verdict = "pending"
            else:
                # M-11 (2026-10-24): when a competency has several skills, group A's verdict
                # for a criterion is the average score across those skills against the same
                # pass line as a competency score (>= 3 of 5) -- not "fail if any skill fails".
                verdict = "pass" if avg_score >= asm["scoring"]["pass_threshold"] / top else "fail"
            merged[i] = {"verdict": verdict, "score": avg_score,
                         "met": sum(o["met"] for o in outs), "total": sum(o["total"] for o in outs),
                         "pending": sum(o["pending"] for o in outs)}
        if not skills:
            notes.append(f"{comp}: no submitted skill belongs to this competency, so group A scores 0 for it.")
        raw = result.get("competency_results", {}).get(comp)
        if raw is None:
            print(f"error: no competency_results for {comp!r}", file=sys.stderr)
            return 1
        res = {k: _apply_human(v, human.get("conditions", {}).get(f"{comp}/{k}", {}), f"{comp}/{k}") for k, v in raw.items()}
        missing = [i for i in rest_ids if i not in res]
        if missing:
            print(f"error: {comp} has no results for {missing}", file=sys.stderr)
            return 1
        outs = cr.evaluate_all(profile, {i: res[i] for i in rest_ids}, sub)
        outcomes = {**merged, **outs}
        sc = cr.score_groups(profile, outcomes)
        any_pending |= sc["competency_score"] is None
        comps.append({"id": comp, "skills": skills, "outcomes": outcomes, "score": sc,
                      "unmet": {i: [(t, _flag(r), (r.get("evidence", "") if isinstance(r, dict) else ""), (r.get("locations", []) if isinstance(r, dict) else []))
                                    for t, r in zip(by_id[i]["conditions"], res[i]) if _flag(r) is not True]
                                for i in rest_ids},
                      "skill_unmet": {s: {i: [(t, _flag(r), (r.get("evidence", "") if isinstance(r, dict) else ""), (r.get("locations", []) if isinstance(r, dict) else []))
                                              for t, r in zip(by_id[i]["conditions"],
                                                              _apply_human(result["skill_results"][s][i], {}, ""))
                                              if _flag(r) is not True] for i in a_ids} for s in skills}})

    gate = human.get("gate") or result.get("gate") or {"verdict": "pending", "note": "no gate result"}
    gate_verdict = gate.get("verdict", "pending")
    verdicts = [c["score"]["verdict"] for c in comps]
    if "fail" in verdicts or gate_verdict == "fail":
        verdict = "FAIL"
    elif None in verdicts or gate_verdict != "pass":
        verdict = "PENDING"
    else:
        verdict = "PASS"
    mapping_reviewed = bool(human.get("mapping_reviewed"))
    status = "final" if verdict != "PENDING" and mapping_reviewed else "provisional"
    if not mapping_reviewed:
        notes.append("Skill -> competency mapping is the judge's proposal; the trainer has not reviewed it yet "
                     "(human `mapping_reviewed`).")
    if gate_verdict == "pending":
        notes.append("The AI Safety & Responsible Use gate has no verdict yet.")

    report = {"scoring_model": "weighted-pass-fail", "status": status, "verdict": verdict,
              "pass_threshold": asm["scoring"]["pass_threshold"], "gate": {"id": "SAFE", **gate},
              "skill_to_competency": [{"skill": s, **m} for s, m in mapping.items()],
              "mapping_reviewed": mapping_reviewed,
              "competencies": [{"id": c["id"], "skills": c["skills"], "competency_score": c["score"]["competency_score"],
                                "verdict": c["score"]["verdict"], "groups": c["score"]["groups"],
                                "criteria": {i: {k: v for k, v in o.items()} for i, o in c["outcomes"].items()}}
                               for c in comps],
              "criteria_sha256": asm["criteria_sha256"], "notes": notes}
    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / "assessment_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    def fmt(x):
        return "pending" if x is None else x
    table = []
    for c in comps:
        for g in asm["groups"]:
            ids = [i for i in (a_ids if g["id"] == "A" else rest_ids) if by_id[i]["group"] == g["id"]]
            for i in ids:
                o, crit = c["outcomes"][i], by_id[i]
                if g["id"] == "A":
                    items = [(s, t, m, e, lo) for s in c["skills"] for t, m, e, lo in c["skill_unmet"][s][i]]
                    ev = [evidence_block(n, f"skill {s}", t, m is None, e, lo, root) for n, (s, t, m, e, lo) in enumerate(items, 1)] \
                        or ([] if c["skills"] else ["No skill in this competency"])
                else:
                    ev = [evidence_block(n, "", t, m is None, e, lo, root) for n, (t, m, e, lo) in enumerate(c["unmet"][i], 1)]
                table.append([(c["id"], S_CELL), (f"{g['id']} {g['name']}", S_CELL), (f"{i} {crit['name']}", S_CELL),
                              (round(top / len(ids), 3), S_NUM), (fmt(None if o["score"] is None else round(o["score"] * top / len(ids), 3)), S_NUM),
                              (f"{o['total'] - o['met'] - o['pending']}/{o['total']}", S_NUM),
                              (f"[{o['verdict'].capitalize()}] " + (f"{len(ev)} issue(s)\n\n" + "\n\n".join(ev) if ev else "All conditions met"), S_EVID)])
            gp = c["score"]["groups"][g["id"]]
            table.append([(c["id"], S_SUB), (f"{g['id']} {g['name']}", S_SUB), ("Group points (weight " + str(g["weight"]) + ")", S_SUB),
                          (gp["max"], S_SUB), (fmt(gp["points"]), S_SUB), ("", S_SUB), ("", S_SUB)])
        table.append([(c["id"], S_SUB), ("Competency", S_SUB), (f"Competency score (pass at {asm['scoring']['pass_threshold']})", S_SUB),
                      (top, S_SUB), (fmt(c["score"]["competency_score"]), S_SUB), ("", S_SUB),
                      (f"[{(c['score']['verdict'] or 'pending').capitalize()}] " + (", ".join(c["skills"]) or "no skill"), S_SUB)])
    table.append([("SAFE", S_SUB), ("GATE", S_SUB), ("AI Safety & Responsible Use", S_SUB), ("", S_SUB), ("", S_SUB), ("", S_SUB),
                  (f"[{gate_verdict.capitalize()}] " + short(gate.get("note", "")), S_SUB)])
    table.append([("", S_SUB), ("TOTAL", S_SUB), (f"{verdict} ({status})", S_SUB), ("", S_SUB), ("", S_SUB), ("", S_SUB),
                  (verdict, S_SUB)])
    title = f"Scoring Sheet - {plan['skill_name']}"
    subtitle = (f"Status: {status}. Competency score = A*0.2 + B*0.5 + C*0.3 on a 0-{top} scale; pass at "
                f"{asm['scoring']['pass_threshold']} for every competency and the gate passes.")
    xlsx_path = a.out_dir / "assessment_scoring_sheet.xlsx"
    try:
        write_xlsx(xlsx_path, title, subtitle, table)
    except PermissionError:  # the old sheet is open in Excel
        xlsx_path = a.out_dir / "assessment_scoring_sheet.new.xlsx"
        write_xlsx(xlsx_path, title, subtitle, table)
        print(f"warning: assessment_scoring_sheet.xlsx is open elsewhere; wrote {xlsx_path.name} instead", file=sys.stderr)

    # --- one-page Summary sheet (course template: ID | Name | Final Result | Competency | Score | Comments) ---
    comp_names = {c["id"]: c["name"] for c in asm.get("competency_catalog", [])}
    summary_rows = [[a.student_id or "", a.student_name or plan["skill_name"], verdict,
                     comp_names.get(c["id"], c["id"]), fmt(c["score"]["competency_score"]), ""] for c in comps]
    gate_segments = re.split(r"(?=\[[^\]]+\.json\])", gate.get("note", "")) if gate.get("note") else []
    gate_comment = "; ".join(short(re.sub(r"^\[[^\]]+\]\s*", "", seg), 60) for seg in gate_segments if seg.strip()) or short(gate.get("note", ""), 180)
    summary_rows.append(["", "", "", "AI Safety & Responsible Use", gate_verdict.capitalize(), gate_comment])
    summary_path = a.out_dir / "assessment_summary.xlsx"
    try:
        write_summary_xlsx(summary_path, summary_rows, [(2, 1 + len(summary_rows))])
    except PermissionError:
        summary_path = a.out_dir / "assessment_summary.new.xlsx"
        write_summary_xlsx(summary_path, summary_rows, [(2, 1 + len(summary_rows))])
        print(f"warning: assessment_summary.xlsx is open elsewhere; wrote {summary_path.name} instead", file=sys.stderr)

    def cellmd(t):
        return str(t).replace("|", "\\|").replace("\n", "<br>")
    md = [f"# Scoring Sheet - {plan['skill_name']}", "", f"**{verdict}** -- status: {status}", "",
          "## Competency scores", "", "| Competency | A | B | C | Score | Verdict |", "|---|---|---|---|---|---|"]
    for c in comps:
        g = c["score"]["groups"]
        md.append(f"| {c['id']} | " + " | ".join(str(fmt(g[k]['points'])) for k in "ABC") +
                  f" | {fmt(c['score']['competency_score'])} | {(c['score']['verdict'] or 'pending')} |")
    md += ["", f"Gate AI Safety & Responsible Use: **{gate_verdict}**" + (f" -- {gate['note']}" if gate.get("note") else ""),
           "", "## Skill to competency mapping (trainer reviews)", "", "| Skill | Competency | Reason |", "|---|---|---|"]
    md += [f"| {s} | {m['competency']}{' (trainer-corrected)' if m['corrected'] else ''} | {cellmd(m['reason'])} |"
           for s, m in mapping.items()]
    md += ["", "## Scoring sheet", "", "| " + " | ".join(HEADERS) + " |", "|" + "---|" * len(HEADERS)]
    for row in table:
        md.append("| " + " | ".join(cellmd(v) for v, _ in row) + " |")
    md += ["", "## Failed conditions: where to look", ""]
    any_fail = False
    for c in comps:
        for i in rest_ids + a_ids:
            if i in a_ids:
                items = [(f"skill {sk}", u) for sk in c["skills"] for u in c["skill_unmet"][sk][i]]
            else:
                items = [("", u) for u in c["unmet"][i]]
            for who, (t, m, e, lo) in items:
                if m is not False:
                    continue
                any_fail = True
                md.append(f"**{c['id']} / {i} {by_id[i]['name']}** {who}: {t}")
                md.append(f"- why: {e}")
                for line in loc_lines(lo, root).split("\n"):
                    if line.strip():
                        md.append(f"- {line.strip()}")
                md.append("")
    if not any_fail:
        md += ["No failed condition.", ""]
    open_cond = [f"{c['id']}/{i}" for c in comps for i, o in c["outcomes"].items() if o["verdict"] == "pending"]
    if open_cond:
        md += ["", "## Waiting for a person", ""] + [f"- {k}: fill `human.conditions[\"{k}\"]` by condition position" for k in open_cond]
    if notes:
        md += ["", "## Notes"] + [f"- {n}" for n in notes]
    (a.out_dir / "assessment_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{verdict} status={status}; " + ", ".join(f"{c['id']}={fmt(c['score']['competency_score'])}" for c in comps))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--result", required=True)
    ap.add_argument("--human")
    ap.add_argument("--submission-dir", type=Path)
    ap.add_argument("--out-dir", required=True, type=Path)
    ap.add_argument("--student-id", default="")
    ap.add_argument("--student-name", default="")
    a = ap.parse_args()

    plan, result = load(a.plan), load(a.result)
    human = load(a.human) if a.human else {}
    asm = plan["scope"]["assessment"]
    if asm.get("scoring_model") == "weighted-pass-fail":
        return render_weighted(a, plan, result, human)
    graded = result.get("criteria", {})

    missing = [c["id"] for c in asm["criteria"] if c["id"] not in graded]
    if missing:
        print(f"error: result has no entry for criteria {missing}", file=sys.stderr)
        return 1

    flags = result.get("advisory_flags", [])
    known_adv = {adv["id"] for c in asm["criteria"] for adv in c.get("advisory", [])}
    for f in flags:
        if f.get("id") not in known_adv:
            print(f"error: advisory flag id {f.get('id')!r} is not defined in the plan", file=sys.stderr)
            return 1
    flag_keys = {f"{f['id']}:{f.get('ref', '')}": f for f in flags}
    stale = sorted(set(human) - set(flag_keys))
    pending = sorted(k for k in flag_keys if k not in human)

    rows, notes = [], []
    for c in asm["criteria"]:
        g = graded[c["id"]]
        na = bool(g.get("na"))
        adv_ids = {x["id"] for x in c.get("advisory", [])}
        my_flags = {k: f for k, f in flag_keys.items() if f["id"] in adv_ids}
        adv_fail = sum(human[k].get("errors", 1) for k in my_flags if human.get(k, {}).get("decision") == "fail")
        errors = len(g.get("errors", []))
        points = c["max_points"] if na else max(0, c["max_points"] - c["penalty_per_error"] * (errors + adv_fail))
        if na and not c.get("na_when"):
            notes.append(f"{c['id']} was graded N/A but the criterion defines no N/A condition -- check the judge's reasoning.")

        evidence = []
        for e in g.get("errors", []):
            shown, problem = check_ref(e.get("where", ""), a.submission_dir)
            if problem:
                notes.append(f"{c['id']}: evidence ref {problem}: {relativize(e.get('where'), a.submission_dir)!r}")
            evidence.append(f"- {shown} -- \"{short(e.get('quote', ''))}\"")
        for k, f in my_flags.items():
            d = human.get(k)
            state = "human: fail" if d and d["decision"] == "fail" else "human: pass" if d else "PENDING human decision"
            evidence.append(f"- flag {k} ({state}) -- {short(f.get('detail', ''))}")
        if na:
            evidence.append(f"- N/A: {short(g.get('note', ''))}")
        meets = ("N/A" if na else "Pending human" if any(k in pending for k in my_flags)
                 else "Yes" if points == c["max_points"] else "No")
        rows.append({"id": c["id"], "group": c["group"], "name": c["name"], "criteria": c["pass_when"],
                     "max": c["max_points"], "errors": errors, "human_errors": adv_fail, "na": na,
                     "points": points, "evidence": evidence, "meets": meets})
    if stale:
        notes.append(f"human decisions with no matching flag (ignored): {stale}")

    group_rows = []
    for gr in asm["groups"]:
        group_rows.append({"id": gr["id"], "name": gr["name"], "max": gr["max_points"],
                           "points": sum(r["points"] for r in rows if r["group"] == gr["id"])})
    total = sum(g["points"] for g in group_rows)
    max_total = sum(g["max"] for g in group_rows)
    verdict = "PASS" if total >= asm["pass_threshold"] else "FAIL"
    status = "provisional" if pending else "final"

    na_list = asm.get("not_assessed", [])
    if na_list:
        notes.append("Not assessed in this exam: " + "; ".join(f"{x['criterion']} ({x['reason']})" for x in na_list)
                     + f". Pass line scaled from {asm.get('pass_threshold_original')}/{asm.get('full_total')} to {asm['pass_threshold']}/{max_total}.")

    report = {"status": status, "verdict": verdict, "total": total, "max_total": max_total,
              "pass_threshold": asm["pass_threshold"], "not_assessed": na_list, "groups": group_rows, "criteria": rows,
              "pending_human_flags": pending, "criteria_sha256": asm["criteria_sha256"],
              "baseline_sha256": asm["baseline_sha256"], "notes": notes}
    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / "assessment_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    # --- the scoring sheet (same layout idea as the course's Excel scoring sheet) ---
    table = []
    for gr in group_rows:
        for r in (x for x in rows if x["group"] == gr["id"]):
            table.append([(f"{r['id']} {r['name']}", S_CELL), (f"{gr['id']} {gr['name']}", S_CELL),
                          (r["criteria"], S_CELL), (r["max"], S_NUM), (r["points"], S_NUM),
                          ("N/A" if r["na"] else r["errors"] + r["human_errors"], S_NUM),
                          (f"[{r['meets']}] " + ("\n".join(r["evidence"]) or "No deduction"), S_EVID)])
        table.append([("", S_SUB), (f"{gr['id']} {gr['name']}", S_SUB), ("Subtotal", S_SUB), (gr["max"], S_SUB),
                      (gr["points"], S_SUB), ("", S_SUB), ("", S_SUB)])
    table.append([("", S_SUB), ("TOTAL", S_SUB), (f"Target: pass at {asm['pass_threshold']}", S_SUB),
                  (max_total, S_SUB), (total, S_SUB), ("", S_SUB), (f"{verdict} ({status})", S_SUB)])
    title = f"Scoring Sheet - {plan['skill_name']}"
    subtitle = f"Status: {status}. Pass threshold: {asm['pass_threshold']} of {max_total}. Evidence refs: path[:line] | path!Sheet!Cell | path#Heading."
    write_xlsx(a.out_dir / "assessment_scoring_sheet.xlsx", title, subtitle, table)

    # --- Markdown copy of the same table ---
    def cellmd(t):
        return str(t).replace("|", "\\|").replace("\n", "<br>")
    md = [f"# Scoring Sheet - {plan['skill_name']}", "",
          f"**{total} / {max_total}: {verdict}** (pass at {asm['pass_threshold']}) -- status: {status}", ""]
    if pending:
        md += [f"Provisional: {len(pending)} advisory flag(s) await a human decision and cost nothing yet: "
               + ", ".join(pending), ""]
    md += ["| " + " | ".join(HEADERS) + " |", "|" + "---|" * len(HEADERS)]
    for row in table:
        md.append("| " + " | ".join(cellmd(v) for v, _ in row) + " |")
    if notes:
        md += ["", "## Notes"] + [f"- {n}" for n in notes]
    (a.out_dir / "assessment_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{verdict} {total}/{max_total} status={status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
