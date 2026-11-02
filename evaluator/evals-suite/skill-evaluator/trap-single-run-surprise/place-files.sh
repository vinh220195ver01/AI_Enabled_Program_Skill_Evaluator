#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/../../_shared/place-files.common.sh"
place_files "$HERE" "${1:-${SANDBOX_DIR:-}}"
