#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-quick}"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ZH_LOG="/tmp/aifor_book_main_zh/main_zh.log"

run_step() {
  echo
  echo "==> $*"
  "$@"
}

run_overleaf_dry_run() {
  local output_file
  output_file="$(mktemp -t aifor-overleaf-dry-run.XXXXXX)"

  bash scripts/sync_book_to_overleaf.sh | tee "${output_file}"

  local blocked_lines
  blocked_lines="$(
    grep -E '(_QA\.md|\.ipynb|\.aux|\.bbl|\.bcf|\.blg|\.fdb_latexmk|\.fls|\.log|\.out|\.run\.xml|\.synctex\.gz|\.toc|\.DS_Store)' \
      "${output_file}" || true
  )"

  rm -f "${output_file}"

  if [[ -n "${blocked_lines}" ]]; then
    echo
    echo "Overleaf dry-run payload contains blocked release-maintenance or build files:" >&2
    echo "${blocked_lines}" >&2
    return 1
  fi
}

run_quick() {
  run_step python scripts/validate_data_manifest.py
  run_step python scripts/check_release_inventory.py

  if [[ -f "${ZH_LOG}" ]]; then
    run_step python scripts/check_latex_log.py
  else
    echo
    echo "==> skipping LaTeX log scan; ${ZH_LOG} does not exist yet"
    echo "    Run 'bash scripts/run_release_checks.sh full' to rebuild the book first."
  fi

  run_step git diff --check
  run_step run_overleaf_dry_run
}

run_full() {
  run_step python scripts/validate_data_manifest.py
  run_step python scripts/check_release_inventory.py
  run_step python scripts/smoke_test_notebooks.py
  run_step bash scripts/build_book_local.sh main
  run_step bash scripts/build_book_local.sh zh
  run_step python scripts/check_latex_log.py
  run_step git diff --check
  run_step run_overleaf_dry_run
}

cd "${PROJECT_ROOT}"

case "${MODE}" in
  quick)
    run_quick
    ;;
  full)
    run_full
    ;;
  *)
    echo "Usage: $0 [quick|full]" >&2
    exit 1
    ;;
esac

echo
echo "Release checks (${MODE}) passed"
