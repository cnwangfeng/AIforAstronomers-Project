# Part III Editorial Spec V3

Status: authoritative spec for Part III revision.

Freeze target: Part III V3 Freeze is an interface freeze, not a content freeze. After freeze, template names, field meanings, Exit Gate logic, and Part III-to-IV handoff language should remain stable unless Part IV pressure testing exposes a real interface failure.

This file is the execution spec for future edits to Part III chapters, notebooks, templates, and grading requirements. It supersedes older language that described separate per-chapter record families such as problem statement, workflow record, regression record, classification record, evaluation record, preprocessing record, model selection record, unsupervised record, and anomaly review record.

---

## Core Goal

Part III should not become a model encyclopedia or a full mathematical machine learning textbook.

The V3 goal is:

> Upgrade Part III from workflow-only strength to workflow + algorithm cards + hard evidence requirements.

Part III edits should make each core model explain:

- what it assumes;
- what it optimizes or how it decides;
- how it is trained or run;
- how it fails;
- what scientific boundary its result has.

Do not add model names unless they help students understand the core workflow or a recurring astronomical/physical use case.

---

## Template Hierarchy

Part I/II:

```text
Evidence Record -> Data Card -> Dataset Contract
```

Part III:

```text
Dataset Contract -> Model Experiment Record -> Trust Statement
```

The Dataset Contract remains the gate from Part II to Part III. The Model Experiment Record is the mother template for all model experiments. Trust Statement is the final claim-boundary template for model outputs.

Do not create independent per-chapter record families. Regression, classification, evaluation, preprocessing, model selection, unsupervised learning, and anomaly detection should add chapter-specific fields or evidence sections to the Model Experiment Record.

---

## Global Assets

Authoritative templates:

- `templates/model_experiment_record_template.md`
- `templates/algorithm_card_template.md`
- `templates/trust_statement_template.md`
- `templates/part3_chapter_specific_fields.md`
- `templates/part3_exit_gates.md`

Related Part I/II bridge:

- `templates/part3_dataset_contract_template.md`
- `templates/data_card_v0.1_template.md`
- `templates/evidence_record_template.md`

---

## Model Experiment Packet

A complete Part III model experiment packet contains:

1. Dataset Contract
2. Model Experiment Record
3. Algorithm Card(s)
4. Evaluation artifact
5. Error analysis artifact
6. Trust Statement

Roles:

- Dataset Contract: explains how data safely enter modeling.
- Model Experiment Record: explains how the experiment was run, evaluated, and made reproducible.
- Algorithm Card: explains why the model works the way it does.
- Evaluation artifact: shows model performance.
- Error analysis artifact: shows how the model fails.
- Trust Statement: defines the boundary of trust and claim.

---

## Algorithm Card Rule

Algorithm Card is not an administrative form. It is the algorithm-understanding layer.

Every core algorithm introduced in Ch18-Ch24 should have a compact card covering:

- model form or decision rule;
- optimization target or training rule;
- key assumptions;
- minimal hand calculation / pseudocode / minimal code;
- diagnostics;
- failure modes;
- scientific boundary.

Prefer short cards embedded near the first serious use of the algorithm. Do not turn them into long theory appendices.

Use three card depths:

- Full card: first serious introduction of a core algorithm in Part III.
- Short card: later reminders or variants that reuse an already introduced idea.
- Sidebar card: Part IV case chapters that only need to point back to the Part III algorithm logic.

Do not add fields to Algorithm Card during Part IV drafting unless a real case cannot express the algorithm assumption, objective/rule, diagnostic, failure mode, or scientific boundary.

---

## Part III V3 Freeze Criteria

Part III can be treated as frozen for Part IV drafting when all of the following are true:

1. Dataset Contract, Model Experiment Record, Trust Statement, and Algorithm Card are the stable interface names.
2. `templates/part3_chapter_specific_fields.md` and `templates/part3_exit_gates.md` match the chapter language in Ch16-Ch25.
3. Ch16-Ch20 consistently use the supervised-learning spine: task definition, split discipline, baseline, algorithm understanding, evaluation, error analysis.
4. Ch21, Ch22, and Ch25 consistently cover train-only preprocessing, search range / model complexity, and trust boundaries.
5. Ch23 and Ch24 consistently label exploratory outputs as candidates, not physical conclusions.
6. Notebooks do not create a separate regression/classification/evaluation/preprocessing/model-selection record family.
7. Part III synthesis hands off to Part IV as a Model Experiment Packet, not as disconnected chapter artifacts.

Freeze does not mean wording cannot be polished. It means Part IV authors can now rely on the interface without guessing which template or term to use.

---

## Phase Plan

### Phase 1: Global Templates

Create and maintain:

- Model Experiment Record template
- Algorithm Card template
- Trust Statement template
- Part III chapter-specific fields
- Part III Exit Gates

### Phase 2: Protocol Layer

Revise:

- `book/chapters/part3/part3_intro.tex`
- `book/chapters/part3/part3_synthesis.tex`

Required changes:

- remove independent record-family language;
- introduce Model Experiment Packet;
- define Algorithm Card and Trust Statement roles;
- connect Part III explicitly to Part I/II Dataset Contract.

### Phase 3: Ch16-Ch20 Supervised Learning Core

Ch16:

- Add Dataset Contract -> ML task -> Model Experiment Record bridge.
- Distinguish scientific question, ML task, and optimization target.
- Requirement: no Dataset Contract, no model experiment.

Ch17:

- Add test-set freeze rule.
- Requirement: test set must not participate in feature selection, preprocessing parameter estimation, hyperparameter selection, threshold selection, or model selection.

Ch18:

- Add Algorithm Cards for mean baseline, linear regression, polynomial regression, and optional ridge/lasso.
- Add residual-plot pattern section.
- Requirement: cannot report only MAE/RMSE; must include residual diagnosis and at least one systematic or extrapolation risk.

Ch19:

- Add Algorithm Cards for rule baseline, kNN, logistic regression, and decision tree.
- Add classifier-boundary section.
- Requirement: must explain label source and class boundary; model class is not natural class.

Ch20:

- Distinguish metric, threshold, decision policy, and scientific cost.
- Requirement: cannot report only accuracy; must explain threshold or operating point with scientific cost.

### Phase 4: Ch21, Ch22, Ch25 Reliability Core

Ch21:

- Add Feature Ledger.
- Requirement: every feature entering the model must trace to Data Card / Evidence Record / Dataset Contract; preprocessing fits only on training data.

Ch22:

- Add section: choosing model complexity is choosing what structure the model is allowed to believe.
- Requirement: record search range, not only best parameter.

Ch25:

- Formally introduce Trust Statement.
- Requirement: must include uncertainty, interpretability, and failure boundary; interpretability describes model behavior, not physical causality.

### Phase 5: Ch23, Ch24 Exploration Core

Ch23:

- Compress framing to two questions: which directions vary most, and which samples are close in feature space?
- Requirement: any cluster name must first state algorithmic group, not physical class unless externally validated.

Ch24:

- Add Anomaly Review Triage: bad data/artifact, boundary but ordinary sample, scientifically interesting candidate.
- Requirement: cannot report only anomaly score; must include human-review fields and candidate tiering.

---

## Editorial Brake

Part III edits do not aim to increase the number of models. They aim to make each core model explainable as:

```text
assumption + objective/decision rule + training/run procedure + diagnostic + failure mode + scientific boundary
```

If a new detail does not help the student complete a Model Experiment Record, Algorithm Card, evaluation/error-analysis artifact, or Trust Statement, keep it out of the main line. Put it in a note, appendix, notebook comment, or future advanced chapter.
