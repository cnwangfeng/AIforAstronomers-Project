# Part IV: Astronomy and Physics Case Studies

This directory stores the Chinese textbook chapters for Part IV: Astronomy and
Physics Case Studies.

These chapters are included by `book/main_zh.tex`, the only active textbook
entry point.

Current chapter files:

- `part4_intro.tex`
- `ch26_gaia_hr_case_study.tex`
- `ch27_photometric_redshift_case_study.tex`
- `ch28_spectral_classification_case_study.tex`
- `ch29_galaxy_morphology_case_study.tex`
- `part4_synthesis.tex`

Current status:

- Part IV has a guide chapter and synthesis chapter that connect the case studies back to Part II data processing and Part III machine-learning workflow.
- Current cases cover Gaia HR diagrams and stellar classification, photometric redshift estimation, spectral classification, and galaxy morphology classification.
- Each current case chapter now includes a minimum case-report template that should map to the Part III frozen interface: Dataset Contract, Model Experiment Record, evaluation/error-analysis artifacts, and Trust Statement.
- The latest continuation pass adds case-opening guide sections to ch26--ch29, so each case starts from why the scientific problem matters, what evidence chain the workflow builds, and what interpretation boundary must be preserved.
- The synthesis chapter now includes an immediately assignable Part IV case package task, connecting Dataset Contract, Model Experiment Record, baseline, diagnostic figures, failure samples, and Trust Statement.
- Possible later refinements include additional time-domain or simulation-centered case studies, but the current four-case backbone is already connected to `book/main_zh.tex` and ready for review.
