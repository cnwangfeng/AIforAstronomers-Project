# Part II: Astronomy and Physics Data Processing

This directory stores the Chinese textbook chapters for Part II: Astronomy and
Physics Data Processing.

These chapters are included by `book/main_zh.tex`. The English `book/main.tex`
remains a separate stable entry point.

Current chapter files:

- `ch10_measurement_uncertainty.tex`
- `ch11_gaia_hr_diagram.tex`
- `ch12_fits_images_wcs.tex`
- `ch13_spectroscopy.tex`
- `ch14_time_series_and_periods.tex`
- `ch15_physics_experiment_simulation_data.tex`

Current status:

- The current pass is a textbook-depth refinement pass, not a new-chapter expansion.
- Each chapter should connect concepts, formulas, algorithmic steps, code bridges, common errors, AI-assistant usage, exercises, and a short summary.
- Part II assumes the reader has Part 0 under control and can follow small Python workflows with tables, loops, functions, and object-method calls without stopping to relearn the basics.
- Before committing Part II changes, run `bash scripts/build_book_local.sh zh`, `python scripts/smoke_test_notebooks.py`, and `git diff --check`.
