# Part III V3 Freeze Checklist

Status: interface-freeze checklist for moving into Part IV review.

Purpose: freeze the Part III method and template interface before using Part IV as a pressure test. This is not a promise that Part III prose will never change; it means Part IV can rely on stable terms, templates, and Exit Gates.

---

## Frozen Interface

Stable Part III objects:

1. Dataset Contract
2. Model Experiment Record
3. Algorithm Card
4. Evaluation artifact
5. Error analysis artifact
6. Trust Statement

Stable hierarchy:

```text
Dataset Contract -> Model Experiment Record -> Trust Statement
```

Stable packet:

```text
Dataset Contract
Model Experiment Record
Algorithm Card(s)
Evaluation artifact
Error analysis artifact
Trust Statement
```

No Part IV chapter should introduce a new independent record family for regression, classification, evaluation, preprocessing, model selection, unsupervised learning, or anomaly detection.

---

## Algorithm Card Depth

- Full card: first serious introduction of a core algorithm in Part III.
- Short card: compact reminder or variant in later Part III sections.
- Sidebar card: Part IV case chapter reference to a Part III algorithm.

Part IV should not re-teach the algorithm unless the case requires a domain-specific interpretation. It should instead state why the algorithm is appropriate for the case and point back to the relevant Part III card.

---

## Chapter Interface Checks

Ch16:
- Distinguishes scientific question, ML task, and optimization target.
- Uses Dataset Contract -> ML task -> Model Experiment Record.

Ch17:
- Freezes test-set rules.
- Records split unit, seed, stratification/group split, baseline, and test-set opening time.

Ch18:
- Uses regression Algorithm Cards.
- Requires residual diagnostics, not only MAE/RMSE.

Ch19:
- Uses classification Algorithm Cards.
- Requires label source and class-boundary statement.

Ch20:
- Separates metric, threshold, decision policy, and scientific cost.
- Rejects accuracy-only reporting.

Ch21:
- Requires Feature Ledger.
- Requires train-only fit for standardization, imputation, PCA, and feature selection.

Ch22:
- Treats model complexity as a structural assumption.
- Requires search range, not only best parameter.

Ch23:
- Treats clusters as algorithmic groups unless externally validated.
- Requires sensitivity or stability check.

Ch24:
- Treats anomaly score as candidate ranking.
- Requires Anomaly Review Triage and human-review fields.

Ch25:
- Introduces Trust Statement.
- Requires uncertainty, interpretability, and failure boundary.

---

## Notebook Bridge Checks

- Notebook README states the Part III V3 evidence hierarchy.
- Notebook outputs should extend Model Experiment Record or produce artifacts that attach to it.
- Notebook examples should not create standalone `regression_record`, `classification_record`, `evaluation_record`, `preprocessing_record`, `model_selection_record`, `unsupervised_record`, or `anomaly_record` templates.

---

## Part IV Pressure-Test Questions

Use these questions during the Part IV quick review:

1. What scientific question does each Part IV chapter answer?
2. Which Part III Algorithm Card(s) does the chapter rely on?
3. Does the chapter have a Dataset Contract or equivalent data-entry description?
4. Does it include a baseline?
5. Does it produce a Model Experiment Record or the evidence needed to fill one?
6. Does it include evaluation and error-analysis artifacts?
7. Does it end with a meaningful Trust Statement or claim boundary?
8. Does it avoid re-teaching algorithms already covered in Part III?
9. Does it avoid becoming a notebook walkthrough?
10. Does it give students a path to adapt the case into a capstone?

If Part IV exposes a repeated failure in these questions, adjust the Part III interface once, then refreeze.
