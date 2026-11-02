# Dùng chung cho nhóm profile-manual-qa: dựng sandbox cho một lượt chấm.
# submission/ + exam/ + baseline/ từ bản chụp đóng băng; files/ của ca (nếu có) đè lên submission/;
# eval_plan.json dựng lại từ criteria.json HIỆN TẠI (merge từ chối plan lỗi thời).
place_manual_qa() {
  local case_dir="$1" sandbox="$2"
  [ -n "$sandbox" ] || { echo "usage: place-files.sh <sandbox-dir>  (hoặc đặt SANDBOX_DIR)" >&2; return 1; }
  local snap="$case_dir/../../_shared/fixtures/manual-qa-sim-pass@2026-10-29"
  local root="$case_dir/../../.."
  mkdir -p "$sandbox/submission"
  cp -r "$snap/submission/." "$sandbox/submission/"
  cp -r "$snap/exam" "$sandbox/exam"
  cp -r "$snap/baseline" "$sandbox/baseline"
  [ -d "$case_dir/files" ] && cp -r "$case_dir/files/." "$sandbox/submission/"
  python "$root/skills/skill-evaluator/scripts/build_plan_from_profile.py" "$root/skills/skill-evaluator/profiles/manual-qa" \
    --skill-name trainee-sim-01 --skill-version final --hypothesis "fixture cho ca profile-manual-qa" \
    --baseline "$sandbox/baseline/baseline.json" \
    --competencies requirements-analysis,test-case-generation,defect-analysis-reporting \
    --out "$sandbox/eval_plan.json" > /dev/null
}
