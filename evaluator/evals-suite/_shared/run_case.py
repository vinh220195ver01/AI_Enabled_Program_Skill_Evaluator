#!/usr/bin/env python3
"""
Chuẩn bị và kiểm tra một lượt chạy ca eval của evals-suite.

Không tự gọi agent (môi trường không có CLI để làm việc đó): `prepare` dựng thư mục lượt chạy
và viết sẵn AGENT_PROMPT.md; người chạy giao file đó cho agent (làm việc trong sandbox/);
`check` kiểm tra tự động những gì kiểm được bằng script và in đường dẫn expected_outcome để đối chiếu tay.

    python evals-suite/_shared/run_case.py prepare profile-manual-qa/main-clean-group-a withX
    python evals-suite/_shared/run_case.py check <đường dẫn thư mục lượt chạy>

Lượt chạy nằm ở  evaluator/evals/suite-runs/<nhóm>/<ca>/<yyyy-mm-dd>/<withX|noX>-<n>/
  sandbox/        thư mục làm việc của agent (chứa kết quả agent ghi ra)
  AGENT_PROMPT.md lời giao việc (lời dặn của lượt + prompt.md của ca)
  run.json        thông tin lượt chạy
  check.json      kết quả `check`
"""
import argparse
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUITE = HERE.parent
EVAL_ROOT = SUITE.parent
RUNS = EVAL_ROOT / "evals" / "suite-runs"
SKILL_DIR = EVAL_ROOT / "skills" / "skill-evaluator"
MERGE = SKILL_DIR / "scripts" / "merge_judge_results.py"

LANES = {
    "withX": ("Bạn CÓ skill skill-evaluator tại {skill} (đọc SKILL.md và các file nó dẫn tới, làm theo khi phù hợp). "
              "Mọi file bạn tạo phải nằm trong sandbox (kể cả khi skill nói lưu vào evaluator/evals/, hãy thay bằng sandbox). "
              "Không sửa gì ngoài sandbox. Không đọc thư mục {suite} hay {fixtures}, và không đọc các thư mục khác trong {evals}\\evals ngoài sandbox của bạn."),
    "noX": ("Bạn KHÔNG có skill hay script đặc biệt nào. Chỉ làm việc trong sandbox; TUYỆT ĐỐI không đọc hay chạy gì ngoài sandbox "
            "(không đọc thư mục evaluator). Mọi file bạn tạo phải nằm trong sandbox."),
}


def find_case(arg):
    p = (SUITE / arg).resolve()
    if not (p / "case.yaml").exists():
        sys.exit(f"không thấy ca: {p}")
    return p


def prepare(a):
    case = find_case(a.case)
    group, name = case.parent.name, case.name
    day = datetime.date.today().isoformat()
    base = RUNS / group / name / day
    n = 1
    while (base / f"{a.lane}-{n}").exists():
        n += 1
    run = base / f"{a.lane}-{n}"
    sandbox = run / "sandbox"
    run.mkdir(parents=True)
    r = subprocess.run(["bash", str(case / "place-files.sh"), str(sandbox)], capture_output=True, text=True)
    if r.returncode:
        sys.exit("place-files.sh lỗi:\n" + r.stdout + r.stderr)
    prompt = (case / "prompt.md").read_text(encoding="utf-8").strip()
    lane_text = LANES[a.lane].format(skill=SKILL_DIR, suite=SUITE, evals=EVAL_ROOT, fixtures=EVAL_ROOT / "test-fixtures")
    body = (f"Bạn là trợ lý thực hiện yêu cầu của người dùng. Sandbox (thư mục làm việc): {sandbox}\n{lane_text}\n"
            f"Lời người dùng:\n\"{prompt}\"\n"
            "Trả lời người dùng như bình thường." + (" Thêm cuối cùng dòng \"TOOLS_USED:\" liệt kê file/script của skill bạn đã đọc hoặc chạy." if a.lane == "withX" else "") + "\n")
    (run / "AGENT_PROMPT.md").write_text(body, encoding="utf-8")
    (run / "run.json").write_text(json.dumps({
        "case": f"{group}/{name}", "lane": a.lane, "run": n, "date": day, "sandbox": str(sandbox),
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(), "case_yaml": str(case / "case.yaml"),
        "prepared_at": datetime.datetime.now().isoformat(timespec="seconds")}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"run dir : {run}\nsandbox : {sandbox}\nprompt  : {run / 'AGENT_PROMPT.md'}")


def check(a):
    run = Path(a.run_dir).resolve()
    meta = json.loads((run / "run.json").read_text(encoding="utf-8"))
    sb = Path(meta["sandbox"])
    out = {"case": meta["case"], "lane": meta["lane"], "grade_files": [], "notes": []}
    grades = sorted(sb.glob("grade*.json"))
    if not grades:
        out["notes"].append("không có file grade*.json trong sandbox")
    for g in grades:
        rec = {"file": g.name}
        try:
            d = json.loads(g.read_text(encoding="utf-8"))
        except Exception as e:
            rec["problem"] = f"JSON lỗi: {e}"
            out["grade_files"].append(rec)
            continue
        rec["keys"] = list(d)
        rec["shape_ok"] = bool({"skill_results", "competency_results"} & set(d)) and "gate" in d or bool({"skill_results", "competency_results"} & set(d))
        text = json.dumps(d)
        rec["score_like_keys"] = sorted(set(re.findall(r'"(points|score|total|pass|passed)"\s*:', text)))
        plan, sub = sb / "eval_plan.json", sb / "submission"
        if plan.exists() and sub.exists():
            r = subprocess.run([sys.executable, str(MERGE), "--plan", str(plan), "--out", str(run / "merge_probe.json"),
                                "--submission-dir", str(sub), str(g)], capture_output=True, text=True)
            lines = [l for l in (r.stdout + r.stderr).splitlines() if l.strip()]
            own = [l for l in lines if l.startswith("  - ")]
            rec["merge_file_problems"] = own
            rec["merge_other"] = [l for l in lines if not l.startswith("  - ")][:3]
        out["grade_files"].append(rec)
    (run / "check.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, ensure_ascii=False))
    print("\nĐối chiếu tay với expected_outcome:", meta["case_yaml"])
    print("Lưu ý: merge chỉ phàn nàn competency chưa chấm là bình thường với file chấm một lát cắt; "
          "mọi dòng 'problems' của chính file là lỗi thật.")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("case", help="<nhóm>/<ca>, ví dụ profile-manual-qa/main-clean-group-a")
    p.add_argument("lane", choices=list(LANES))
    p.set_defaults(fn=prepare)
    c = sub.add_parser("check")
    c.add_argument("run_dir")
    c.set_defaults(fn=check)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
