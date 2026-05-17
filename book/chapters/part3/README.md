# Part III: Machine Learning Practice

This directory stores the Chinese textbook chapters for Part III: Machine
Learning Practice.

These chapters are included by `book/main_zh.tex`, the only active textbook
entry point.

Current chapter files:

- `part3_intro.tex`
- `ch16_ai_ml_scientific_inference.tex`
- `ch17_ml_workflow.tex`
- `ch18_regression.tex`
- `ch19_classification.tex`
- `ch20_model_evaluation_diagnostics.tex`
- `ch21_feature_engineering_preprocessing.tex`
- `ch22_model_selection_hyperparameters.tex`
- `ch23_unsupervised_learning.tex`
- `ch24_anomaly_detection.tex`
- `ch25_uncertainty_interpretability_trust.tex`
- `part3_synthesis.tex`

Current status:

- Part III has a guide chapter and synthesis chapter, framing machine learning as scientific inference rather than model invocation.
- The chapter sequence covers task definition, baseline workflow, regression, classification, evaluation, preprocessing, model selection, unsupervised learning, anomaly detection, uncertainty, interpretability, and trust.
- The Part III V3 pass aligns the record system with the Part I/II mother-template principle: model work now flows through Dataset Contract, Model Experiment Record, Algorithm Card(s), evaluation/error-analysis artifacts, and Trust Statement rather than separate per-chapter record families.
- The latest polish pass adds a model-result reporting frame and concrete minimum report, audit, review, and trust-statement templates from regression/classification through evaluation, preprocessing, model selection, unsupervised learning, anomaly detection, and trust.
- The current textbook-depth pass adds worked mini-calculations and algorithm skeletons across Part III: loss/metric hand calculations, centroid classifier code, least-squares slope source, threshold scans, train-only preprocessing, cross-validation loops, PCA/k-means/DBSCAN workflows, anomaly triage, and coverage-distance trust checks.
- The latest continuation pass adds chapter-opening guide sections to `ch16`--`ch25`, so each method chapter now starts from the scientific role, workflow risk, and interpretation boundary before listing learning goals.
- The synthesis chapter now includes an immediately assignable Part III model experiment packet task, connecting task definition, data split, baseline, model run, diagnostic evidence, error analysis, and trust boundary.
- The next refinement pass should focus on consistency of notation, notebook bridges, figure explanations, and exercise levels.
