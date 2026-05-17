# Part IV Case Package QA

Status: close-out QA for Part IV after Part III V3 Freeze.

Purpose: verify that the four Part IV cases act as reusable case-package examples rather than standalone notebook walkthroughs.

---

## Common Requirement

Each Part IV case should export or describe:

1. Dataset Contract
2. Model Experiment Record
3. Evaluation artifact
4. Error analysis artifact
5. Trust Statement

The case may also point to Part III Algorithm Card sidebar links. It should not introduce a new independent record family.

---

## Case Export Matrix

| Chapter | Case | Dataset Contract | Model Experiment Record | Evaluation artifact | Error analysis artifact | Trust Statement |
|---|---|---|---|---|---|---|
| Ch26 | Gaia HR | `dataset_contract_gaia_hr.md` | `model_experiment_record_gaia_hr.md` | `confusion_matrix.csv`, `figures/hr_diagram_boundary_examples.png` | `boundary_examples.csv` | `trust_statement_gaia_hr.md` |
| Ch27 | Photo-z | `dataset_contract_photoz.md` | `model_experiment_record_photoz.md` | `figures/residual_vs_specz.png`, `figures/residual_by_type.png` | `worst_residual_examples.csv`, `residual_by_type.csv` | `trust_statement_photoz.md` |
| Ch28 | Spectral classification | `dataset_contract_spectral.md` | `model_experiment_record_spectral.md` | `confusion_matrix.csv`, `figures/pca_and_review_spectra.png` | `misclassified_spectra.csv` | `trust_statement_spectral.md` |
| Ch29 | Galaxy morphology | `dataset_contract_morphology.md` | `model_experiment_record_morphology.md` | `confusion_matrix.csv`, `figures/feature_space_diagnostic.png` | `review_queue.csv` | `trust_statement_morphology.md` |

---

## Smoke Test

Run the four Part IV notebooks in a non-interactive environment. Expected generated directories:

```text
notebooks/part4_cases/results/ch26_gaia_hr_case/
notebooks/part4_cases/results/ch27_photoz_case/
notebooks/part4_cases/results/ch28_spectral_case/
notebooks/part4_cases/results/ch29_morphology_case/
```

These outputs are local generated artifacts and remain ignored by git through `notebooks/**/results/`.

---

## Close-Out Judgment

Part IV is ready to serve as the pressure-tested case layer for the frozen Part III interface.

Next recommended step: begin Part V quick review, checking that deep learning and AI-tool chapters preserve baseline, review queue, error analysis, and Trust Statement discipline instead of replacing them with model complexity.
