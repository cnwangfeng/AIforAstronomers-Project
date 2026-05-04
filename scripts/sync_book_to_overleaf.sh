#!/usr/bin/env bash
set -euo pipefail

APPLY=0
if [[ "${1:-}" == "--apply" ]]; then
  APPLY=1
  shift
fi

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOOK_SRC="${PROJECT_ROOT}/book"
OVERLEAF_REPO="${1:-${PROJECT_ROOT}/../AIforAstronomers}"

if [[ ! -d "${BOOK_SRC}" ]]; then
  echo "Book source directory not found: ${BOOK_SRC}" >&2
  exit 1
fi

if [[ ! -d "${OVERLEAF_REPO}" ]]; then
  echo "Overleaf repository directory not found: ${OVERLEAF_REPO}" >&2
  exit 1
fi

if [[ ! -d "${OVERLEAF_REPO}/.git" ]]; then
  echo "Destination does not look like a Git repository: ${OVERLEAF_REPO}" >&2
  exit 1
fi

RSYNC_ARGS=(
  -av
  --itemize-changes
  --delete
  # QA inventories live in the full project repo; keep the Overleaf-facing
  # repository focused on compile-facing book sources.
  --exclude "*_QA.md"
  --exclude ".git/"
  --exclude ".gitignore"
  --exclude ".DS_Store"
  --exclude "*.aux"
  --exclude "*.bbl"
  --exclude "*.bcf"
  --exclude "*.blg"
  --exclude "*.fdb_latexmk"
  --exclude "*.fls"
  --exclude "*.log"
  --exclude "*.out"
  --exclude "*.run.xml"
  --exclude "*.synctex.gz"
  --exclude "*.toc"
)

if [[ "${APPLY}" -eq 0 ]]; then
  echo "Dry-run only. Add --apply to actually sync."
  RSYNC_ARGS+=(--dry-run)
fi

rsync "${RSYNC_ARGS[@]}" "${BOOK_SRC}/" "${OVERLEAF_REPO}/"

if [[ "${APPLY}" -eq 1 ]]; then
  echo "Book synced to ${OVERLEAF_REPO}"
else
  echo "Dry-run complete. No files were changed."
fi
