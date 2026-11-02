#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/../../_shared/place-files.common.sh"
place_files "$HERE" "${1:-${SANDBOX_DIR:-}}"
# bài nộp lấy từ bản chụp đóng băng dùng chung
SNAP="$HERE/../../_shared/fixtures/manual-qa-sim-pass@2026-10-29/submission"
SB="${1:-${SANDBOX_DIR:-}}"
mkdir -p "$SB/submission"
cp -r "$SNAP/." "$SB/submission/"
# plan dựng lại từ criteria.json HIỆN TẠI để không bị chặn vì hash cũ (merge từ chối plan lỗi thời)
EVAL_ROOT="$HERE/../../.."
python "$EVAL_ROOT/skills/skill-evaluator/scripts/build_plan_from_profile.py" "$EVAL_ROOT/skills/skill-evaluator/profiles/manual-qa"   --skill-name trainee-sim-01 --skill-version final --hypothesis "fixture cho ca trap-fabricated-evidence-quote"   --competencies requirements-analysis,test-design,test-case-generation,test-data-generation,defect-analysis-reporting   --out "$SB/eval_plan.json" > /dev/null
