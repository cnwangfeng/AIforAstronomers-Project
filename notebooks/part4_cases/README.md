# Part IV Notebook Index

These notebooks turn the methods from Part III into end-to-end astronomy and
physics mini-projects.

Part IV notebooks should feed the same case package used in the book chapters:

- `dataset_contract.md`
- `model_experiment_record.md`
- evaluation artifact(s)
- error-analysis artifact(s)
- `trust_statement.md`

They should not create standalone case-specific record families. Algorithm
details should point back to Part III Algorithm Cards unless the case needs a
domain-specific interpretation.

Current notebook set:

- `ch26_gaia_hr_case_study.ipynb`
- `ch27_photometric_redshift_case_study.ipynb`
- `ch28_spectral_classification_case_study.ipynb`
- `ch29_galaxy_morphology_case_study.ipynb`

Expected local exports after running the notebooks:

```text
results/ch26_gaia_hr_case/
  dataset_contract_gaia_hr.md
  model_experiment_record_gaia_hr.md
  trust_statement_gaia_hr.md
  confusion_matrix.csv
  boundary_examples.csv
  figures/hr_diagram_boundary_examples.png

results/ch27_photoz_case/
  dataset_contract_photoz.md
  model_experiment_record_photoz.md
  trust_statement_photoz.md
  worst_residual_examples.csv
  residual_by_type.csv
  figures/residual_vs_specz.png
  figures/residual_by_type.png

results/ch28_spectral_case/
  dataset_contract_spectral.md
  model_experiment_record_spectral.md
  trust_statement_spectral.md
  confusion_matrix.csv
  misclassified_spectra.csv
  figures/pca_and_review_spectra.png

results/ch29_morphology_case/
  dataset_contract_morphology.md
  model_experiment_record_morphology.md
  trust_statement_morphology.md
  confusion_matrix.csv
  review_queue.csv
  figures/feature_space_diagnostic.png
```

Later this directory will grow into:

- time-domain signal-analysis case studies
