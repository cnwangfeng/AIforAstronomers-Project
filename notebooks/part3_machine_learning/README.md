# Part III Notebook Index

These notebooks start the machine-learning workflow of the textbook. The first
notebooks deliberately use tiny teaching datasets and pure-Python baselines so
they can run even in a minimal environment.

Part III V3 uses one modeling evidence hierarchy:

- `Dataset Contract -> Model Experiment Record -> Trust Statement`
- Algorithm understanding is documented with compact `Algorithm Card`s.
- Chapter-specific notebook outputs should extend the common record instead of
  creating separate regression/classification/evaluation record families.

Current notebook plan in progress:

- `ch16_ai_ml_scientific_inference.ipynb`
- `ch17_minimal_classification_workflow.ipynb`
- `ch18_regression_workflow.ipynb` exports
  `results/part3_algorithm_understanding/ch18_algorithm_understanding.md`
- `ch19_classification_workflow.ipynb` exports
  `results/part3_algorithm_understanding/ch19_algorithm_understanding.md`
- `ch20_model_evaluation_diagnostics.ipynb` exports
  `results/part3_evidence_artifacts/ch20_evaluation_artifact.md`
- `ch21_feature_engineering_preprocessing.ipynb` exports
  `results/part3_evidence_artifacts/ch21_feature_ledger.md`
- `ch22_model_selection_hyperparameters.ipynb` exports
  `results/part3_evidence_artifacts/ch22_model_selection_artifact.md`
- `ch23_unsupervised_learning.ipynb` exports
  `results/part3_algorithm_understanding/ch23_algorithm_understanding.md`
- `ch24_anomaly_detection.ipynb` exports
  `results/part3_algorithm_understanding/ch24_algorithm_understanding.md`
- `ch25_uncertainty_interpretability_trust.ipynb` exports
  `results/part3_evidence_artifacts/ch25_trust_statement_draft.md`

The exported algorithm-understanding notes and evidence artifacts are not new
record templates. They are lightweight attachments for the `Algorithm Card
link`, `Evaluation`, `Error Analysis`, `Preprocessing`, `Model Selection`, or
`Trust Statement` sections of a common `Model Experiment Record`.

Later this directory can grow into:

- model-evaluation notebooks
- feature-engineering notebooks
- clustering and anomaly-detection notebooks
