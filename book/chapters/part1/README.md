# Part I: Scientific Computing Foundations

This directory stores the Chinese textbook chapters for Part I: scientific
computing and reproducible workflow after the reader has completed the Python
prerequisite materials.

These chapters are included by `book/main_zh.tex`, the only active textbook
entry point.

Current chapter files:

- `part1_intro.tex`
- `ch01_unix_linux_scientific_computing.tex`
- `ch02_git_reproducible_research.tex`
- `ch04_libraries_scripts_jupyter.tex`
- `ch06_data_io_fits.tex`
- `ch08_plotting_scientific_figures.tex`
- `part1_synthesis.tex`

Current status:

- These chapters have completed the 2026-05-05 major textbook-depth rebuild and are now in reader-polish mode.
- Part I now has an explicit Chinese guide chapter and synthesis chapter, framing Linux, Git, scripting, I/O, and plotting as one reproducible research workflow.
- The synthesis chapter compresses Part I into a minimum reproducible project package: environment, version, execution, data-contract, and evidence layers.
- Part I should emphasize reproducible habits: safe command-line work, clear Git history, stable scripts, data contracts, and scientific figure standards.
- Each chapter now includes a micro-project or explicit bridge from textbook prose to its companion notebook workflow.
- The current reader-QA pass adds minimum record templates for command-line runs, script runs, data checks, version-linked results, and figure explanations, so Part I outputs can feed the capstone evidence cards.
- The latest one-pass Part I completion adds worked examples and intermediate reasoning layers: path-resolution examples, shell pipeline construction, chmod arithmetic, remote-run checks, Git status decisions, commit/HEAD/branch/tag semantics, commit boundaries, checksum-based data provenance, install/import/dependency distinctions, notebook-to-script maturity levels, function boundaries, argparse entry points, row validation, raw-vs-clean data boundaries, FITS HDU/WCS context, count-rate unit checks, figure reference relations, color/readability guidance, executable reproducible plotting scripts, and an integrated Part I mini research package task.
- Latest local validation for the current text checkpoint: `bash scripts/run_release_checks.sh full` passes, including `59` notebook smoke tests, Chinese LaTeX build, log scan, release inventory, data manifest, publication blocker scan, Overleaf dry-run payload, and `git diff --check`; generated PDF is `/tmp/aifor_book_main_zh/main_zh.pdf` at 564 pages.
- Part I assumes the reader has completed Part 0 and can already run notebooks, read small tables with `Path`/`csv`, follow `if`/`for`/`while`, and read small functions and object-method calls.
- Before committing Part I changes, run `bash scripts/build_book_local.sh zh`, `python scripts/smoke_test_notebooks.py`, and `git diff --check`.
