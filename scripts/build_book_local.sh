#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-zh}"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOOK_DIR="${PROJECT_ROOT}/book"

if [[ -d "/Library/TeX/texbin" ]]; then
  export PATH="/Library/TeX/texbin:${PATH}"
fi

if ! command -v latexmk >/dev/null 2>&1; then
  echo "latexmk not found. Install MacTeX/TeX Live or expose /Library/TeX/texbin in PATH." >&2
  exit 1
fi

case "${TARGET}" in
  zh)
    STABLE_OUTDIR="/tmp/aifor_book_main_zh"
    OUTDIR="$(mktemp -d "${STABLE_OUTDIR}.XXXXXX")"
    ENGINE_ARGS=(-xelatex)
    ENTRY="main_zh.tex"
    ;;
  *)
    echo "Usage: $0 [zh]" >&2
    echo "The legacy book/main.tex entry has been removed; use book/main_zh.tex." >&2
    exit 1
    ;;
esac

run_latexmk() {
  latexmk "${ENGINE_ARGS[@]}" \
    -interaction=nonstopmode \
    -halt-on-error \
    -outdir="${OUTDIR}" \
    "$@" \
    "${ENTRY}"
}

prepare_outdir() {
  mkdir -p "${OUTDIR}"

  # LaTeX writes per-\include aux files under paths such as
  # chapters/part1/*.aux.  Pre-create those paths in the output directory so a
  # clean build does not spend latexmk passes discovering missing subfolders.
  while IFS= read -r dir; do
    mkdir -p "${OUTDIR}/${dir}"
  done < <(find chapters -type d -print)
}

publish_outputs() {
  mkdir -p "${STABLE_OUTDIR}"
  cp "${OUTDIR}/${ENTRY%.tex}.pdf" "${STABLE_OUTDIR}/${ENTRY%.tex}.pdf"
  cp "${OUTDIR}/${ENTRY%.tex}.log" "${STABLE_OUTDIR}/${ENTRY%.tex}.log"
}

cd "${BOOK_DIR}"
prepare_outdir

if run_latexmk; then
  :
else
  echo "First Chinese build did not settle cleanly; forcing dependency refresh in a fresh output directory..." >&2
  run_latexmk -g
fi

PDF_PATH="${OUTDIR}/${ENTRY%.tex}.pdf"

if [[ -f "${PDF_PATH}" ]]; then
  publish_outputs
  echo "Build succeeded: ${STABLE_OUTDIR}/${ENTRY%.tex}.pdf"
  echo "Build work directory: ${OUTDIR}"
else
  echo "Expected PDF not found: ${PDF_PATH}" >&2
  exit 1
fi
