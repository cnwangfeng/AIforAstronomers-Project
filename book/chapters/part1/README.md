# Part I: Scientific Computing Foundations

This directory stores the Chinese textbook chapters for Part I: scientific
computing and reproducible workflow after the reader has completed the Python
prerequisite materials.

These chapters are included by `book/main_zh.tex`. The English `book/main.tex`
remains a separate stable entry point.

Current chapter files:

- `ch01_unix_linux_scientific_computing.tex`
- `ch02_git_reproducible_research.tex`
- `ch04_libraries_scripts_jupyter.tex`
- `ch06_data_io_fits.tex`
- `ch08_plotting_scientific_figures.tex`

Current status:

- These chapters have completed the first textbook-depth pass and are being reviewed for polish.
- Part I should emphasize reproducible habits: safe command-line work, clear Git history, stable scripts, data contracts, and scientific figure standards.
- Each chapter now includes an explicit bridge from textbook prose to its companion notebook workflow.
- Part I assumes the reader has completed Part 0 and can already run notebooks, read small tables with `Path`/`csv`, follow `if`/`for`/`while`, and read small functions and object-method calls.
- Before committing Part I changes, run `bash scripts/build_book_local.sh zh`, `python scripts/smoke_test_notebooks.py`, and `git diff --check`.
