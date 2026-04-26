#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-main}"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOOK_DIR="${PROJECT_ROOT}/book"

case "${TARGET}" in
  main)
    OUTDIR="/tmp/aifor_book_main"
    ENGINE_ARGS=(-pdf)
    ENTRY="main.tex"
    ;;
  zh)
    OUTDIR="/tmp/aifor_book_main_zh"
    ENGINE_ARGS=(-xelatex)
    ENTRY="main_zh.tex"
    ;;
  *)
    echo "Usage: $0 [main|zh]" >&2
    exit 1
    ;;
esac

mkdir -p "${OUTDIR}"

run_latexmk() {
  latexmk "${ENGINE_ARGS[@]}" \
    -interaction=nonstopmode \
    -halt-on-error \
    -outdir="${OUTDIR}" \
    "${ENTRY}"
}

cd "${BOOK_DIR}"

if run_latexmk; then
  :
elif [[ "${TARGET}" == "zh" ]]; then
  echo "First Chinese build requested another pass; retrying once..." >&2
  run_latexmk
else
  exit 1
fi

PDF_PATH="${OUTDIR}/${ENTRY%.tex}.pdf"

if [[ -f "${PDF_PATH}" ]]; then
  echo "Build succeeded: ${PDF_PATH}"
else
  echo "Expected PDF not found: ${PDF_PATH}" >&2
  exit 1
fi
