# Release Sync Checklist

Version date: `2026-05-04`

This checklist is the practical companion to the capstone release chapters. It
is meant for the final repo-to-Overleaf sync and publication pass.

## 1. Pre-Release Validation

- Run `python scripts/validate_data_manifest.py`
- Run `python scripts/check_release_inventory.py`
- Run `python scripts/smoke_test_notebooks.py`
- Run `bash scripts/build_book_local.sh main`
- Run `bash scripts/build_book_local.sh zh`
- Run `python scripts/check_latex_log.py`
- Or run `bash scripts/run_release_checks.sh full` for the full local sequence
- Confirm `/tmp/aifor_book_main_zh/main_zh.pdf` builds successfully
- Confirm recent Chinese log has no blocking `Overfull \hbox`, undefined
  references, missing math delimiters, or fatal LaTeX errors
- Review `Roadmap.md` counts and recovery pointers

## 2. Package Sanity Check

- Confirm `book/main_zh.tex` includes the intended chapter set
- Confirm `book/FIGURE_TABLE_QA.md` reflects current figure/table counts
- Confirm `book/EVIDENCE_CARD_QA.md` reflects current capstone evidence-card names
- Confirm `book/FORMULA_QA.md` reflects current formula counts and explanation policy
- Confirm `book/SOURCE_LICENSE_QA.md` reflects current bibliography, license, attribution, and AI-use status
- Confirm `book/chapters/part6/README.md` matches actual chapter files
- Confirm `notebooks/part6_capstone/README.md` matches actual notebooks
- Confirm `data/small/README.md` and `data/manifest.yml` match current datasets
- Confirm `COURSE_PACKAGE_RELEASE_NOTES.md` reflects current counts and outputs
- Confirm `PUBLICATION_DECISIONS.md` has no unresolved blocker for the intended release path

## 3. Overleaf Sync Dry Run

- Run:

```bash
bash scripts/sync_book_to_overleaf.sh
```

- Review the itemized dry-run file list carefully
- Check for accidental large-file or notebook-output leakage
- Confirm project-side QA inventories such as `*_QA.md` stay out of the
  Overleaf-facing sync payload unless explicitly needed for a special review
- `bash scripts/run_release_checks.sh quick` also fails if the dry-run payload
  includes QA inventories, notebooks, or LaTeX build artifacts
- Confirm only intended `book/` content will be synced

## 4. Overleaf Sync Apply

- Run:

```bash
bash scripts/sync_book_to_overleaf.sh --apply
```

- Move into `../AIforAstronomers/`
- Review `git status`
- Commit only the intended book-sync delta
- Push the Overleaf-facing repo after one final sanity check

## 5. Post-Sync Checks

- Confirm the Overleaf repository still compiles
- Confirm chapter order and table of contents look right
- Confirm new chapter titles appear correctly
- Confirm no expected figures or included files are missing

## 6. Recovery Anchors

If work needs to resume later, start here:

- `Roadmap.md`
- `README.md`
- `book/README.md`
- `book/FIGURE_TABLE_QA.md`
- `book/EVIDENCE_CARD_QA.md`
- `book/FORMULA_QA.md`
- `book/SOURCE_LICENSE_QA.md`
- `COURSE_PACKAGE_RELEASE_NOTES.md`
- `book/main_zh.tex`
- `book/chapters/part6/README.md`
- `notebooks/part6_capstone/README.md`
- `data/manifest.yml`

Current recovery counts to confirm before sync:

- Chinese PDF: about `507` pages
- Notebook smoke test: `59` notebooks
- Data manifest: `52` datasets
- Local validation: `build_book_local.sh main`, `build_book_local.sh zh`, notebook smoke, data manifest, `check_latex_log.py`, and `git diff --check` have passed; `run_release_checks.sh full` is the one-command equivalent for the final local pass

## 7. Remaining Publication Polish

- Reader QA is now targeted rather than a blank sweep; use QA inventories and reader feedback for focused patches
- Figure/table inventory is tracked in `book/FIGURE_TABLE_QA.md`; evidence-card inventory is tracked in `book/EVIDENCE_CARD_QA.md`; formula inventory is tracked in `book/FORMULA_QA.md`; source/license inventory is tracked in `book/SOURCE_LICENSE_QA.md`; these QA files are project-side release records and are excluded from the default Overleaf sync payload
- Bibliography, source, license, and AI-use statement audit remain blocked on final project-level license decisions
- Final wording pass on release notes and audience-facing copy
- Overleaf dry-run before any `--apply` sync
