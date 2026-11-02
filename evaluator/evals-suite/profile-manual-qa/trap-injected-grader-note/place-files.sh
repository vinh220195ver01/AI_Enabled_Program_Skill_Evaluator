#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/../../_shared/place-manual-qa.common.sh"
place_manual_qa "$HERE" "${1:-${SANDBOX_DIR:-}}"
