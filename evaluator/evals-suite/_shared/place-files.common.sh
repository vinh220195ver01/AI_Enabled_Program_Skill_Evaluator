# Dùng chung: copy <case>/files/ vào sandbox của lượt chạy.
place_files() {
  local case_dir="$1" sandbox="$2"
  [ -n "$sandbox" ] || { echo "usage: place-files.sh <sandbox-dir>  (hoặc đặt SANDBOX_DIR)" >&2; return 1; }
  mkdir -p "$sandbox"
  cp -r "$case_dir/files/." "$sandbox/"
}
