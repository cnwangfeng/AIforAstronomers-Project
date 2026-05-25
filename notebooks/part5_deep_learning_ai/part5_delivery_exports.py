"""Export small Part V trusted-delivery packages from teaching notebooks."""

from __future__ import annotations

import csv
from pathlib import Path


def _write_text(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


def export_ch30_neural_network_basics_delivery(ns: dict) -> None:
    results_dir = Path("results/ch30_neural_network_basics_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    linear_rmse = ns["linear_rmse"]
    network_rmse = ns["network_rmse"]
    linear_mae = ns["linear_mae"]
    network_mae = ns["network_mae"]
    training_snapshots = ns["training_snapshots"]
    hidden_size = ns["hidden_size"]
    data_name = ns["DATA_PATH"].name

    with (results_dir / "test_predictions.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "sample_id",
                "true_y",
                "linear_prediction",
                "network_prediction",
                "linear_residual",
                "network_residual",
            ],
        )
        writer.writeheader()
        for row, linear_prediction, network_prediction in zip(ns["test_rows"], ns["linear_predictions"], ns["network_predictions"]):
            writer.writerow({
                "sample_id": row["sample_id"],
                "true_y": row["target_y"],
                "linear_prediction": round(linear_prediction, 5),
                "network_prediction": round(network_prediction, 5),
                "linear_residual": round(linear_prediction - row["target_y"], 5),
                "network_residual": round(network_prediction - row["target_y"], 5),
            })

    with (results_dir / "training_loss_snapshots.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["epoch", "mean_training_loss"])
        writer.writeheader()
        for epoch, loss_value in sorted(training_snapshots.items()):
            writer.writerow({"epoch": epoch, "mean_training_loss": round(loss_value, 8)})

    probe_rows = []
    for point in [-1.5, -0.5, 0.0, 0.8, 1.6]:
        prediction, hidden_act = ns["network_predict"](point)
        probe_rows.append({
            "feature_x": point,
            "prediction": round(prediction, 5),
            "hidden_activations": " ".join(f"{value:.4f}" for value in hidden_act),
        })
    with (results_dir / "hidden_activation_probe.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["feature_x", "prediction", "hidden_activations"])
        writer.writeheader()
        writer.writerows(probe_rows)

    try:
        import matplotlib.pyplot as plt

        train_xs = ns["train_xs"]
        train_ys = ns["train_ys"]
        test_xs = ns["test_xs"]
        test_ys = ns["test_ys"]
        grid_xs = [min(train_xs) + 0.05 * index for index in range(int((max(test_xs) - min(train_xs)) / 0.05) + 1)]
        linear_grid = [ns["linear_intercept"] + ns["linear_slope"] * x for x in grid_xs]
        network_grid = [ns["network_predict"](x)[0] for x in grid_xs]

        figure, axis = plt.subplots(figsize=(7.2, 4.2))
        axis.scatter(train_xs, train_ys, color="#2f6b99", label="train")
        axis.scatter(test_xs, test_ys, color="#c97a00", marker="s", label="test")
        axis.plot(grid_xs, linear_grid, linestyle="--", color="#b03a2e", label="linear baseline")
        axis.plot(grid_xs, network_grid, color="#1f7a4d", label="single hidden layer")
        axis.set_xlabel("feature_x")
        axis.set_ylabel("target_y")
        axis.set_title("Ch30 nonlinear baseline vs neural network")
        axis.grid(alpha=0.25)
        axis.legend()
        figure.tight_layout()
        figure.savefig(figures_dir / "baseline_vs_network.png", dpi=160)
        plt.close(figure)
    except Exception as exc:  # pragma: no cover - optional plotting path
        print(f"Optional neural-network figure export skipped: {exc}")

    _write_text(results_dir / "deep_learning_model_card_single_hidden_layer.md", f"""
# Deep Learning Model Card: Single-Hidden-Layer Network

## Model
- Name: single-hidden-layer tanh network
- Task type: regression
- Astronomy / physics use case: teaching proxy for nonlinear calibration or color-to-quantity mapping

## Input Structure
- Input object: one scalar feature per sample
- Shape: `(n_samples, 1)`
- Units / normalization: unitless teaching feature, standardized using train-set mean and standard deviation
- Train-only preprocessing: feature mean `{ns["feature_mean"]:.5f}`, feature std `{ns["feature_std"]:.5f}` computed from train rows only

## Architecture
- Main layers: linear hidden layer with {hidden_size} units, tanh activation, linear output head
- Nonlinearities: tanh
- Pooling / bottleneck / attention, if any: none
- Output head: scalar regression output

## Training Objective
- Loss: mean squared error
- Optimizer: manual batch gradient descent
- Epochs / batch size / learning rate: 6000 epochs, full-batch, learning rate {ns["learning_rate"]}
- Early stopping or validation rule: not used in this tiny concept demo

## What It Learns
- Representation learned: nonlinear basis functions over the scalar input
- Local / global structure captured: saturation at both ends and sharper central transition
- Relation to baseline: linear RMSE {linear_rmse:.4f}; network RMSE {network_rmse:.4f}

## Diagnostics
- Training vs validation curve: `training_loss_snapshots.csv`
- Main evaluation metric: MAE/RMSE on held-out test rows
- Error / residual / review artifact: `test_predictions.csv`
- Representation or activation check: `hidden_activation_probe.csv`

## Failure Modes
- Data issue: tiny synthetic dataset and no real uncertainty model
- Model issue: hidden units can overfit if scaled up without validation
- Interpretation issue: better fit does not prove a physical mechanism

## Scientific Boundary
- Supported claim: a nonlinear hidden representation improves this toy regression over a straight-line baseline.
- Unsupported claim: neural networks are always better, or this model has learned a physical law.
- Human review needed: any extrapolation outside the training feature range
""")

    _write_text(results_dir / "model_experiment_record_neural_network_basics.md", f"""
# Model Experiment Record: Neural Network Basics

## 1. Task
- Scientific question: can a minimal neural network represent a nonlinear response that a straight line misses?
- ML task: regression
- Prediction target / discovery goal: `target_y`
- Intended use: concept demonstration for deep learning foundations

## 2. Dataset Contract
- Dataset Contract link: teaching dataset in `data/small/{data_name}`
- Data Card link: small teaching data README
- Key Evidence Records: notebook execution and exported diagnostics

## 3. Split / Role Assignment
- Train / validation / test split: train/test only
- Split unit: sample ID
- Random seed: deterministic manual initialization
- When was the test set opened? after fitting the linear baseline and neural network

## 4. Baseline
- Baseline type: least-squares straight line
- Baseline reason: minimum interpretable regression reference
- Baseline result: MAE {linear_mae:.4f}, RMSE {linear_rmse:.4f}

## 5. Model
- Model family: single-hidden-layer tanh neural network
- Key parameters / hyperparameters: hidden units {hidden_size}, learning rate {ns["learning_rate"]}, epochs 6000
- Deep Learning Model Card link: `deep_learning_model_card_single_hidden_layer.md`
- Training entry point: `ch30_neural_network_basics.ipynb`

## 6. Evaluation
- Metrics: MAE and RMSE
- Threshold, if any: none
- Scientific cost: overclaiming nonlinear fit as physical explanation
- Main diagnostic figure: `figures/baseline_vs_network.png`

## 7. Error Analysis
- Main failure cases: extrapolation beyond the training feature range
- Error concentration: linear baseline misses saturation; network reduces this residual in the toy data
- Relation to data quality / physical regime: no real noise model; teaching-only data

## 8. Limit
- Supported claim: the hidden layer provides nonlinear basis functions that improve this toy regression.
- Unsupported claim: this network has discovered a physical law or validates deep learning for real survey data.
- Known leakage / selection / extrapolation risk: train-only standardization is used, but the dataset is tiny and synthetic.

## 9. Reproducibility
- Script / notebook: `ch30_neural_network_basics.ipynb`
- Output files: `test_predictions.csv`, `training_loss_snapshots.csv`, `hidden_activation_probe.csv`
- Code version / tag: record current git commit when used in a report
""")

    _write_text(results_dir / "trust_statement_neural_network_basics.md", f"""
# Trust Statement: Neural Network Basics

## Model Output
- Result: network RMSE {network_rmse:.4f} vs linear RMSE {linear_rmse:.4f}
- Main metric / diagnostic: test-set residual comparison and hidden activation probe

## Distribution Status
- In-distribution / out-of-distribution / unclear: in-distribution within the toy feature range
- Evidence: explicit train/test rows from `data/small/{data_name}`

## Uncertainty
- Main uncertainty source: tiny synthetic dataset and fixed deterministic initialization
- Estimated by: held-out test rows only

## Interpretability
- Main feature dependence: tanh hidden units form nonlinear basis functions over `feature_x`
- Interpretation method: hidden activation probe and baseline comparison
- Why this is not causal proof: activations are fitted functions, not physical variables

## Failure Boundary
- Known failure region: extrapolation outside training feature range
- Human review needed: any scientific interpretation beyond the toy demonstration

## Claim Boundary
- Supported claim: a minimal neural network can improve a nonlinear toy regression when compared with a line.
- Unsupported claim: neural networks should replace baseline models by default.
""")

    print(f"Exported Ch30 neural-network basics delivery package to {results_dir}")


def export_ch31_cnn_delivery(ns: dict) -> None:
    results_dir = Path("results/ch31_cnn_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    validation_predictions = ns["workflow_validation_predictions"]
    target_predictions = ns["workflow_target_predictions"]
    review_rows = ns["workflow_review_rows"]
    workflow_model = ns["workflow_model"]
    workflow_target_prototypes = ns["workflow_target_prototypes"]
    workflow_ready_threshold = ns["workflow_ready_threshold"]

    with (results_dir / "validation_predictions.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["sample_id", "true_label", "predicted_label", "confidence"])
        writer.writeheader()
        for item in validation_predictions:
            writer.writerow({
                "sample_id": item["sample_id"],
                "true_label": item["true_label"],
                "predicted_label": item["predicted_label"],
                "confidence": round(item["confidence"], 4),
            })

    with (results_dir / "target_routing_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["sample_id", "true_label", "predicted_label", "route", "confidence"])
        writer.writeheader()
        for item in target_predictions:
            writer.writerow({
                "sample_id": item["sample_id"],
                "true_label": item["true_label"],
                "predicted_label": item["predicted_label"],
                "route": item["route"],
                "confidence": round(item["confidence"], 4),
            })

    review_export = []
    for row in review_rows:
        feature_vector = ns["workflow_feature_vector"](row, workflow_model)
        _, probabilities = ns["workflow_distance_probabilities"](feature_vector, workflow_target_prototypes)
        predicted_label = max(probabilities, key=probabilities.get)
        confidence = probabilities[predicted_label]
        review_export.append({
            "sample_id": row["sample_id"],
            "quality_flag": row["quality_flag"],
            "true_label": row["morphology_label"],
            "predicted_label": predicted_label,
            "confidence": round(confidence, 4),
            "confidence_only_route": "ready_for_science" if confidence >= workflow_ready_threshold else "manual_review",
            "workflow_route": ns["workflow_route"](row, confidence, workflow_ready_threshold),
        })

    with (results_dir / "review_queue.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(review_export[0]))
        writer.writeheader()
        writer.writerows(review_export)

    try:
        import matplotlib.pyplot as plt

        ordered = sorted(target_predictions, key=lambda item: item["confidence"], reverse=True)
        figure, axis = plt.subplots(figsize=(7.6, 3.8))
        colors = ["#1f7a4d" if item["route"] == "ready_for_science" else "#c97a00" for item in ordered]
        axis.bar([item["sample_id"] for item in ordered], [item["confidence"] for item in ordered], color=colors)
        axis.axhline(workflow_ready_threshold, color="#333333", linestyle="--", label="ready threshold")
        axis.set_ylabel("target-head confidence")
        axis.set_title("CNN transfer workflow routing")
        axis.grid(axis="y", alpha=0.25)
        axis.legend()
        figure.tight_layout()
        figure.savefig(figures_dir / "target_routing.png", dpi=160)
        plt.close(figure)
    except Exception as exc:  # pragma: no cover - optional plotting path
        print(f"Optional routing figure export skipped: {exc}")

    source_raw_accuracy = ns["accuracy"](ns["workflow_source_raw_predictions"])
    target_accuracy = ns["accuracy"](target_predictions)
    ready_count = sum(item["route"] == "ready_for_science" for item in target_predictions)
    data_name = ns["WORKFLOW_DATA_PATH"].name

    _write_text(results_dir / "deep_learning_model_card_cnn_transfer.md", f"""
# Deep Learning Model Card: Tiny CNN Transfer Workflow

## Model
- Name: tiny Conv2d-style backbone with target prototype head
- Task type: image classification / review routing
- Astronomy / physics use case: galaxy morphology cutout classification with a conservative review gate

## Input Structure
- Input object: one small 6x6 image cutout per sample
- Shape: `(n_samples, 6, 6)`
- Units / normalization: toy pixel intensities from `data/small/{data_name}`
- Train-only preprocessing: source-domain feature learning and validation-calibrated ready threshold

## Architecture
- Main layers: local convolutional filters, nonlinear feature map, frozen target-domain prototype head
- Nonlinearities: tiny teaching activation inside the hand-written workflow
- Pooling / bottleneck / attention, if any: local feature aggregation
- Output head: nearest target prototype plus confidence route

## Training Objective
- Loss / rule: source-domain local feature learning followed by target prototype adaptation
- Optimizer: hand-written teaching update
- Epochs / batch size / learning rate: epochs {ns["WORKFLOW_EPOCHS"]}, learning rate {ns["WORKFLOW_LEARNING_RATE"]}
- Early stopping or validation rule: ready threshold {workflow_ready_threshold:.4f} calibrated on target validation rows

## What It Learns
- Representation learned: local morphology patterns that transfer better than flattened raw pixels
- Local / global structure captured: compact cores, elongated disks, and double-source-like local patterns
- Relation to baseline: raw-pixel source baseline accuracy {source_raw_accuracy:.3f}; target workflow accuracy {target_accuracy:.3f}

## Diagnostics
- Training vs validation curve: validation predictions and threshold calibration
- Main evaluation metric: target accuracy and ready/review routing
- Error / residual / review artifact: `review_queue.csv`
- Representation or activation check: target routing confidence figure

## Failure Modes
- Data issue: low-quality, neighbor-contaminated, or off-center cutouts
- Model issue: tiny synthetic domain shift and prototype head can overstate confidence
- Scientific interpretation issue: morphology labels are teaching labels, not final physical classes

## Scientific Boundary
- Supported claim: local CNN-style representations can be safer than raw pixels in this toy routing workflow.
- Unsupported claim: this validates a production survey morphology classifier.
- Human review needed: all low-quality or below-threshold cutouts
""")

    _write_text(results_dir / "dataset_contract_cnn_transfer.md", f"""
# Dataset Contract: CNN Transfer Workflow

## 1. Task Definition
- ML task: image classification / transfer learning workflow
- Scientific question: can a source-domain local feature extractor support target-domain morphology routing?
- Prediction target: morphology label for tiny galaxy cutouts
- Intended use: teaching example for CNN baseline discipline and review routing

## 2. Sample Definition
- One sample is one 6x6 cutout row from `data/small/{data_name}`.
- Sample ID: `sample_id`

## 3. Input Features
- Input array: `p00` to `p55`
- Quality metadata: `quality_flag`
- Split role: `split_role`

## 4. Target / Label
- Target: `morphology_label`
- Label leakage risk: labels are toy teaching labels; quality flags must not become morphology labels.

## 5. Selection and Split
- Source train: {len(ns["workflow_source_train_rows"])}
- Target adapt: {len(ns["workflow_target_adapt_rows"])}
- Target validation: {len(ns["workflow_target_validation_rows"])}
- Target test: {len(ns["workflow_target_test_rows"])}
- Review rows: {len(review_rows)}

## 6. Known Limits
- Tiny synthetic teaching dataset.
- Supports workflow reasoning, not survey-scale CNN performance claims.
""")

    _write_text(results_dir / "model_experiment_record_cnn_transfer.md", f"""
# Model Experiment Record: CNN Transfer Workflow

## 1. Task
- Scientific question: whether local CNN-style features improve target-domain morphology routing over raw-pixel baselines.
- ML task: image classification with transfer-style adaptation.
- Prediction target / discovery goal: morphology label and ready/review route.
- Intended use: teaching sample for baseline-before-CNN and review-gated deployment.

## 2. Dataset Contract
- Dataset Contract link: `dataset_contract_cnn_transfer.md`
- Data Card link: teaching data in `data/small/{data_name}`
- Key Evidence Records: notebook execution and exported routing/review artifacts.

## 3. Split / Role Assignment
- Train / validation / test split: source_train / target_adapt / target_validation / target_test / review
- Split unit: cutout sample ID
- Random seed: {ns["WORKFLOW_SEED"]}
- When was the test set opened? after source training, target adaptation, and validation threshold calibration

## 4. Baseline
- Baseline type: source raw-pixel prototypes
- Baseline reason: tests whether flattened pixels are enough across domain shift
- Baseline result: accuracy {source_raw_accuracy:.3f}

## 5. Model
- Model family: tiny Conv2d backbone plus frozen target prototype head
- Key parameters / hyperparameters: filters={ns["WORKFLOW_FILTERS"]}, epochs={ns["WORKFLOW_EPOCHS"]}, lr={ns["WORKFLOW_LEARNING_RATE"]}
- Deep Learning Model Card link: `deep_learning_model_card_cnn_transfer.md`
- Training entry point: this notebook

## 6. Evaluation
- Metrics: accuracy, routing counts, review capture
- Threshold, if any: {workflow_ready_threshold:.4f}
- Scientific cost: low-quality or low-confidence cutouts must route to review rather than automatic claims
- Main diagnostic figure: `figures/target_routing.png`

## 7. Error Analysis
- Main failure cases: low-confidence clean target row and flagged review rows
- Error concentration: target-domain shift and quality flags
- Relation to data quality / physical regime: high confidence does not override quality metadata

## 8. Limit
- Supported claim: this toy workflow shows why frozen local features plus target adaptation can beat raw pixels under a tiny domain shift.
- Unsupported claim: this does not validate a production CNN morphology classifier.
- Known leakage / selection / extrapolation risk: synthetic toy labels and tiny validation set.

## 9. Reproducibility
- Script / notebook: `ch31_convolutional_neural_networks.ipynb`
- Output files: `target_routing_summary.csv`, `review_queue.csv`, `validation_predictions.csv`
- Code version / tag: record current git commit when used in a report
""")

    _write_text(results_dir / "trust_statement_cnn_transfer.md", f"""
# Trust Statement: CNN Transfer Workflow

## Model Output
- Result: adapted target prototype head accuracy {target_accuracy:.3f}; ready rows {ready_count}/{len(target_predictions)}
- Main metric / diagnostic: target routing summary and review queue

## Distribution Status
- In-distribution / out-of-distribution / unclear: target rows are a controlled toy shift, not survey data
- Evidence: source/adapt/validation/test/review split roles are explicit

## Uncertainty
- Main uncertainty source: tiny validation set and synthetic cutouts
- Estimated by: validation-calibrated threshold and review routing

## Interpretability
- Main feature dependence: local patterns learned by the tiny convolutional backbone
- Interpretation method: compare raw-pixel baseline, source-head transfer, and target prototype head
- Why this is not causal proof: local features are teaching constructs, not physical morphology causes

## Failure Boundary
- Known failure region: low-confidence rows, low-SNR / off-center / neighbor-contaminated cutouts
- Human review needed: all rows in `review_queue.csv` and any row below threshold

## Claim Boundary
- Supported claim: CNN-style local representations can support safer routing than raw pixels in this toy setup.
- Unsupported claim: real-survey morphology classification is solved.
""")

    print(f"Exported Ch31 trusted delivery package to {results_dir}")


def export_ch35_llm_programming_delivery(ns: dict) -> None:
    results_dir = Path("results/ch35_llm_programming_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    checks = ns["verified_report"]["checks"]
    with (results_dir / "regression_checks.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["name", "passed", "detail"])
        writer.writeheader()
        writer.writerows(checks)

    snapshot = ns["regression_snapshot"]
    with (results_dir / "regression_snapshot.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(snapshot))
        writer.writeheader()
        writer.writerow(snapshot)

    try:
        import matplotlib.pyplot as plt

        rows = ns["rows"]
        median = ns["median"]
        figure, axis = plt.subplots(figsize=(7.4, 3.6))
        axis.scatter(
            [row["time_days"] for row in rows],
            [row["relative_flux"] for row in rows],
            c=["#c0392b" if row["quality_flag"] != "clean" else "#2f6b99" for row in rows],
            s=45,
        )
        axis.axhline(median(row["relative_flux"] for row in ns["clean_out_of_transit"]), color="#1f7a4d", linestyle="--", label="clean baseline median")
        axis.axhline(median(row["relative_flux"] for row in ns["clean_in_transit"]), color="#8e5ea2", linestyle=":", label="clean transit median")
        axis.set_xlabel("time [day]")
        axis.set_ylabel("normalized flux")
        axis.set_title("Tiny light-curve debugging dataset")
        axis.grid(alpha=0.25)
        axis.legend()
        figure.tight_layout()
        figure.savefig(figures_dir / "lightcurve_validation.png", dpi=160)
        plt.close(figure)
    except Exception as exc:  # pragma: no cover - optional plotting path
        print(f"Optional validation figure export skipped: {exc}")

    all_pass = all(item["passed"] for item in checks)
    data_name = ns["DATA_PATH"].name
    depth = ns["verified_report"]["candidate_depth"]
    reference_depth = ns["reference_depth"]

    _write_text(results_dir / "evidence_record_llm_programming.md", f"""
# Evidence Record: LLM-Assisted Transit-Depth Debugging

## 1. Input
- Data / file path, preferably relative to project root: `data/small/{data_name}`
- AI draft under review: `ai_draft_transit_depth`, max-minus-min flux estimator
- Reference fields: `segment_label`, `quality_flag`, `relative_flux`

## 2. Operation
- Compared the AI draft against a clean-median reference calculation.
- Ran physical-range, flagged-row robustness, reference-match, and transit-direction regression checks.
- Replaced the draft with `verified_transit_depth`, which filters non-clean cadences and uses median in/out-of-transit flux.

## 3. Output
- Verified depth: {depth:.4f}
- Reference depth: {reference_depth:.4f}
- Regression checks: `regression_checks.csv`
- Validation figure: `figures/lightcurve_validation.png`

## 4. Check
- All regression checks pass: {all_pass}
- Flagged cadence count: {len(ns["flagged_rows"])}
- The repaired estimator agrees with the clean-median reference and is robust to flagged rows.

## 5. Limit
- This is a tiny teaching light curve, not a production transit model.
- Passing these checks supports keeping the repaired estimator, not claiming a planet detection.

## 6. Reuse in ML
- Reusable as a verification artifact and AI-assisted coding evidence for Part V / Part VI.
""")

    _write_text(results_dir / "ai_usage_log_llm_programming.md", f"""
# AI Usage Log: LLM-Assisted Programming

## 1. Use Context
- Project / chapter: Ch35 LLM-assisted research programming
- Task: review and repair a transit-depth estimator
- AI tool / model, if known: teaching draft, no live API call
- Date: notebook run date

## 2. Input Boundary
- Materials provided to AI: schema, quality flags, scientific constraints, draft function
- Materials not provided to AI: private data, external credentials, unpublished material
- Data / privacy / copyright constraint: local teaching CSV only

## 3. Interaction / Action
- Prompt or instruction summary: ask for bugs, hidden assumptions, tests, and safer implementation
- Tool actions, if any: none; simulated local review workflow
- Files or sections affected: estimator function and notebook checks

## 4. Output Kept
- Output accepted: quality-aware median estimator and regression-check structure
- Output rejected or rewritten: max-minus-min draft estimator
- Reason for acceptance / rejection: draft failed flagged-row robustness and reference checks

## 5. Verification
- Code run / tests passed: {all_pass}
- Citation or source checked: not applicable
- Numerical or visual sanity check: depth {depth:.4f}, validation figure exported
- Human review needed: flagged cadence policy should be checked before real data use

## 6. Responsibility and Disclosure
- What the student verified: data schema, flagged-row handling, reference calculation, regression checks
- What the student takes responsibility for: final estimator choice and scientific interpretation
- Disclosure note / AI-use statement: AI assisted code review and workflow organization; final code was run and checked by the student.
""")

    _write_text(results_dir / "disclosure_note_llm_programming.md", """
# Disclosure Note

AI assistance was used as a code-review and workflow-organization aid. The retained estimator was verified by running local regression checks against a clean-median reference calculation. The AI draft that ignored quality flags was rejected.
""")

    print(f"Exported Ch35 trusted delivery package to {results_dir}")


def export_ch36_agentic_workflow_delivery(ns: dict) -> None:
    results_dir = Path("results/ch36_agentic_workflow_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    action_log = ns["action_log"]
    decisions = ns["decisions"]
    with (results_dir / "action_log.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["candidate_id", "tool_sequence", "score", "final_action", "rationale"])
        writer.writeheader()
        for item in action_log:
            writer.writerow({
                "candidate_id": item["candidate_id"],
                "tool_sequence": " > ".join(item["tool_sequence"]),
                "score": item["score"],
                "final_action": item["final_action"],
                "rationale": item["rationale"],
            })

    with (results_dir / "triage_decisions.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["candidate_id", "score", "agent_action", "reference_action", "rationale"])
        writer.writeheader()
        for item in decisions:
            writer.writerow({
                "candidate_id": item["candidate_id"],
                "score": round(item["score"], 3),
                "agent_action": item["agent_action"],
                "reference_action": item["reference_action"],
                "rationale": item["rationale"],
            })

    review_queue = [item for item in decisions if item["agent_action"] == "manual_review"]
    with (results_dir / "manual_review_queue.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["candidate_id", "score", "reference_action", "rationale"])
        writer.writeheader()
        for item in review_queue:
            writer.writerow({
                "candidate_id": item["candidate_id"],
                "score": round(item["score"], 3),
                "reference_action": item["reference_action"],
                "rationale": item["rationale"],
            })

    try:
        import matplotlib.pyplot as plt

        ordered = sorted(decisions, key=lambda item: item["score"], reverse=True)
        colors = {"follow_now": "#1f7a4d", "manual_review": "#c97a00", "reject": "#b03a2e"}
        figure, axis = plt.subplots(figsize=(8.0, 3.8))
        axis.bar([item["candidate_id"] for item in ordered], [item["score"] for item in ordered], color=[colors[item["agent_action"]] for item in ordered])
        axis.axhline(0.78, color="#1f7a4d", linestyle="--", label="follow threshold")
        axis.axhline(0.58, color="#c97a00", linestyle=":", label="review threshold")
        axis.set_ylabel("follow-up score")
        axis.set_title("Agentic triage routing")
        axis.grid(axis="y", alpha=0.25)
        axis.legend()
        figure.tight_layout()
        figure.savefig(figures_dir / "agentic_triage_routing.png", dpi=160)
        plt.close(figure)
    except Exception as exc:  # pragma: no cover - optional plotting path
        print(f"Optional triage figure export skipped: {exc}")

    baseline_precision = ns["baseline_precision_at_3"]
    agent_precision = ns["agent_precision"]
    agreement = ns["accuracy"](decisions)
    data_name = ns["DATA_PATH"].name

    _write_text(results_dir / "evidence_record_agentic_workflow.md", f"""
# Evidence Record: Agentic Transient Triage

## 1. Input
- Data / file path, preferably relative to project root: `data/small/{data_name}`
- Input fields: alert score, rise rate, color, crossmatch distance, image quality, moving-object flag
- Reference decision field: `reference_action`

## 2. Operation
- Compared a single-score ranking baseline with a gated agentic workflow.
- Ran artifact, moving-object, novelty, priority-score, and human-handoff gates.
- Exported action log, decisions, manual-review queue, and routing figure.

## 3. Output
- Baseline precision@3: {baseline_precision:.3f}
- Agent agreement with reference: {agreement:.3f}
- Follow-now count: {len(ns["agent_follow_now"])}
- Manual-review count: {len(review_queue)}
- Action log: `action_log.csv`

## 4. Check
- The workflow explicitly rejects artifacts and moving objects before ranking.
- Borderline or weak-novelty candidates route to manual review.
- Follow-now precision: {agent_precision:.3f}

## 5. Limit
- This is a tiny teaching triage table, not a real broker or follow-up system.
- The workflow supports routing discipline, not autonomous discovery claims.

## 6. Reuse in ML
- Reusable as an AI-tool workflow evidence artifact and Part VI capstone protocol example.
""")

    _write_text(results_dir / "ai_usage_log_agentic_workflow.md", f"""
# AI Usage Log: Agentic Workflow

## 1. Use Context
- Project / chapter: Ch36 agentic research assistants
- Task: route transient candidates through a bounded tool workflow
- AI tool / model, if known: simulated local agentic workflow, no live API call
- Date: notebook run date

## 2. Input Boundary
- Materials provided to AI: local teaching candidate table and explicit routing constraints
- Materials not provided to AI: private alert streams, credentials, telescope-control tools
- Data / privacy / copyright constraint: local teaching CSV only

## 3. Interaction / Action
- Prompt or instruction summary: define required tools, order, stop conditions, human handoff rules, and final queues
- Tool actions, if any: artifact gate, moving-object gate, novelty check, priority score, human-handoff gate
- Files or sections affected: generated action log and review queue

## 4. Output Kept
- Output accepted: gated routing decisions and manual-review queue
- Output rejected or rewritten: single-score baseline as final workflow
- Reason for acceptance / rejection: baseline lets artifacts and moving objects into the top-ranked candidates

## 5. Verification
- Code run / tests passed: action log and decision table exported
- Citation or source checked: not applicable
- Numerical or visual sanity check: baseline precision@3 {baseline_precision:.3f}; follow-now precision {agent_precision:.3f}
- Human review needed: all candidates in `manual_review_queue.csv`

## 6. Responsibility and Disclosure
- What the student verified: gate order, stop conditions, routing outcomes, manual-review queue
- What the student takes responsibility for: final follow-up decision and any scientific claim about a candidate
- Disclosure note / AI-use statement: AI workflow assistance was bounded by explicit gates and human handoff; final decisions require human review.
""")

    _write_text(results_dir / "disclosure_note_agentic_workflow.md", """
# Disclosure Note

An agentic workflow was used as a bounded routing aid, not as an autonomous discovery system. The workflow preserved explicit gates, an action log, and a manual-review queue. Final candidate prioritization remains a human scientific decision.
""")

    print(f"Exported Ch36 trusted delivery package to {results_dir}")


def _export_rows(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _simple_bar_figure(path: Path, labels: list[str], values: list[float], title: str, ylabel: str) -> None:
    try:
        import matplotlib.pyplot as plt

        figure, axis = plt.subplots(figsize=(8.0, 3.8))
        axis.bar(labels, values, color="#2f6b99")
        axis.set_title(title)
        axis.set_ylabel(ylabel)
        axis.grid(axis="y", alpha=0.25)
        figure.tight_layout()
        figure.savefig(path, dpi=160)
        plt.close(figure)
    except Exception as exc:  # pragma: no cover - optional plotting path
        print(f"Optional figure export skipped: {exc}")


def export_ch32_spectral_conv_delivery(ns: dict) -> None:
    results_dir = Path("results/ch32_spectral_conv_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    clean_routes = [item for item in ns["trainable_routes"] if item["quality_flag"] == "clean"]
    review_routes = [item for item in ns["trainable_routes"] if item["route"] == "manual_review"]
    _export_rows(results_dir / "trainable_conv1d_routes.csv", [
        {**item, "confidence": round(item["confidence"], 4)} for item in ns["trainable_routes"]
    ])
    _export_rows(results_dir / "validation_summaries.csv", [
        {**item, "confidence": round(item["confidence"], 4)} for item in ns["validation_summaries"]
    ])
    _simple_bar_figure(
        figures_dir / "conv1d_route_confidence.png",
        [item["sample_id"] for item in ns["trainable_routes"]],
        [item["confidence"] for item in ns["trainable_routes"]],
        "Trainable Conv1d routing confidence",
        "confidence",
    )

    baseline_accuracy = ns["accuracy"](ns["workflow_normalized_raw_predictions"])
    model_accuracy = ns["accuracy"](ns["trainable_test_predictions"])
    data_name = ns["WORKFLOW_DATA_PATH"].name

    _write_text(results_dir / "deep_learning_model_card_spectral_conv1d.md", f"""
# Deep Learning Model Card: Tiny Spectral Conv1d

## Model
- Name: tiny trainable Conv1d spectral classifier
- Task type: spectral classification / review routing
- Astronomy / physics use case: local line-pattern recognition in short teaching spectra

## Input Structure
- Input object: one normalized toy spectrum per sample
- Shape: `(n_samples, wavelength_bins)`
- Units / normalization: continuum-normalized teaching flux windows from `data/small/{data_name}`
- Train-only preprocessing: validation threshold selected before opening test/review routes

## Architecture
- Main layers: one-dimensional local filters plus a lightweight classification head
- Nonlinearities: teaching-size nonlinear response after local filtering
- Pooling / bottleneck / attention, if any: local window aggregation
- Output head: spectral class probabilities and ready/review route

## Training Objective
- Loss / rule: supervised classification on training spectra
- Optimizer: hand-written tiny training loop in the notebook
- Epochs / batch size / learning rate: epochs {ns["TRAINABLE_EPOCHS"]}, kernel size {ns["TRAINABLE_KERNEL_SIZE"]}
- Early stopping or validation rule: ready threshold {ns["workflow_trainable_ready_threshold"]:.4f}

## What It Learns
- Representation learned: local spectral-line patterns that tolerate small shifts better than raw windows
- Local / global structure captured: short wavelength neighborhoods rather than whole-spectrum averages
- Relation to baseline: normalized raw-window baseline accuracy {baseline_accuracy:.3f}; Conv1d clean-test accuracy {model_accuracy:.3f}

## Diagnostics
- Training vs validation curve: validation summaries
- Main evaluation metric: clean-test accuracy and route confidence
- Error / residual / review artifact: `trainable_conv1d_routes.csv`
- Representation or activation check: route confidence figure

## Failure Modes
- Data issue: low S/N, bad pixels, artifacts, or wavelength-grid mismatch
- Model issue: filters may learn toy line positions that do not transfer
- Scientific interpretation issue: a class prediction is not a physical explanation of the spectrum

## Scientific Boundary
- Supported claim: local Conv1d filters improve this toy shifted-line workflow.
- Unsupported claim: this is a production spectral classifier.
- Human review needed: all non-clean or low-confidence spectra
""")

    _write_text(results_dir / "dataset_contract_spectral_conv1d.md", f"""
# Dataset Contract: Spectral Conv1d Workflow

## 1. Task Definition
- ML task: spectral classification with review routing
- Scientific question: can local spectral filters handle shifted line patterns more safely than raw flux windows?
- Prediction target: `spectral_label`
- Intended use: teaching package for 1D convolution and quality-aware routing

## 2. Sample Definition
- One sample is one toy spectrum row from `data/small/{data_name}`.
- Sample ID: `sample_id`

## 3. Input Features
- Flux window fields from the workflow spectrum table.
- Quality metadata: `quality_flag`

## 4. Known Limits
- Tiny synthetic spectra, not a survey classifier.
- Supports workflow reasoning about local spectral patterns and review gates.
""")

    _write_text(results_dir / "model_experiment_record_spectral_conv1d.md", f"""
# Model Experiment Record: Spectral Conv1d Workflow

## 1. Task
- Scientific question: whether trainable local spectral filters improve over normalized raw-window baselines.
- ML task: spectral classification.
- Prediction target / discovery goal: spectral label plus ready/review route.
- Intended use: Part V deep-model delivery example.

## 2. Dataset Contract
- Dataset Contract link: `dataset_contract_spectral_conv1d.md`
- Data Card link: teaching data in `data/small/{data_name}`
- Key Evidence Records: notebook execution and exported route artifacts.

## 3. Split / Role Assignment
- Train / validation / test split: workflow train / validation / test / review
- Split unit: spectrum sample ID
- Random seed: {ns["WORKFLOW_SEED"]}
- When was the test set opened? after validation-calibrated threshold selection

## 4. Baseline
- Baseline type: continuum-normalized raw-window nearest centroid
- Baseline result: accuracy {baseline_accuracy:.3f}

## 5. Model
- Model family: tiny trainable Conv1d plus linear head
- Key parameters / hyperparameters: filters={ns["TRAINABLE_FILTERS"]}, kernel_size={ns["TRAINABLE_KERNEL_SIZE"]}, epochs={ns["TRAINABLE_EPOCHS"]}
- Deep Learning Model Card link: `deep_learning_model_card_spectral_conv1d.md`
- Training entry point: this notebook

## 6. Evaluation
- Metrics: clean-test accuracy, validation threshold, review capture
- Threshold, if any: {ns["workflow_trainable_ready_threshold"]:.4f}
- Main diagnostic figure: `figures/conv1d_route_confidence.png`

## 7. Error Analysis
- Main failure cases: low-confidence shifted lines and non-clean quality flags
- Relation to data quality / physical regime: spectral quality gates override model confidence

## 8. Limit
- Supported claim: local filters help the toy shifted-line workflow.
- Unsupported claim: production spectral classification is solved.

## 9. Reproducibility
- Script / notebook: `ch32_one_dimensional_convolutions_for_spectra.ipynb`
- Output files: `trainable_conv1d_routes.csv`, `validation_summaries.csv`
""")

    _write_text(results_dir / "trust_statement_spectral_conv1d.md", f"""
# Trust Statement: Spectral Conv1d Workflow

## Model Output
- Result: clean-test accuracy {model_accuracy:.3f}; manual-review rows {len(review_routes)}
- Main metric / diagnostic: route confidence and validation threshold

## Distribution Status
- In-distribution / out-of-distribution / unclear: controlled toy spectra only
- Evidence: explicit train/validation/test/review roles

## Failure Boundary
- Known failure region: low-SNR, artifacts, shifted or ambiguous line patterns
- Human review needed: all rows routed to manual_review

## Claim Boundary
- Supported claim: Conv1d-style local filters can improve toy spectral routing over raw windows.
- Unsupported claim: this validates a real survey pipeline.
""")

    print(f"Exported Ch32 trusted delivery package to {results_dir}")


def export_ch33_autoencoder_delivery(ns: dict) -> None:
    results_dir = Path("results/ch33_autoencoder_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    routes = ns["conv1d_routes"]
    _export_rows(results_dir / "autoencoder_routes.csv", [
        {
            **item,
            "error": round(item["error"], 4),
            "peak_window_error": round(item["peak_window_error"], 4),
        }
        for item in routes
    ])
    _export_rows(results_dir / "latent_retrieval_triage.csv", [
        {
            **item,
            "nearest_distance": round(item["nearest_distance"], 4),
        }
        for item in ns["workflow_retrieval_triage"]
    ])
    _simple_bar_figure(
        figures_dir / "autoencoder_reconstruction_errors.png",
        [item["sample_id"] for item in routes],
        [item["error"] for item in routes],
        "Conv1d autoencoder reconstruction error",
        "error",
    )

    route_counts = {}
    for item in routes:
        route_counts[item["route"]] = route_counts.get(item["route"], 0) + 1
    data_name = ns["DATA_PATH"].name

    _write_text(results_dir / "dataset_contract_autoencoder.md", f"""
# Dataset Contract: Autoencoder Anomaly Workflow

## 1. Task Definition
- ML task: representation learning / anomaly review routing
- Scientific question: which toy spectra are poorly supported by the learned normal-spectrum representation?
- Prediction target: route label, not a physical anomaly class
- Intended use: teaching package for reconstruction error and latent-support review

## 2. Sample Definition
- One sample is one toy spectrum row from `data/small/{data_name}`.
- Sample ID: `sample_id`

## 3. Input Features
- Input array: normalized flux bins from the teaching spectrum table.
- Quality / role metadata: train, validation, held-out normal, or anomaly/review role as defined in the notebook.

## 4. Target / Label
- Target used for training: input reconstruction of normal-like spectra.
- Label leakage risk: anomaly labels must not be used to set the normal reconstruction threshold.

## 5. Selection and Split
- Thresholds are calibrated from normal validation rows before held-out routes are interpreted.

## 6. Known Limits
- Tiny synthetic spectra.
- Reconstruction error is a triage signal, not a discovery claim.
""")

    _write_text(results_dir / "deep_learning_model_card_autoencoder.md", f"""
# Deep Learning Model Card: Tiny Spectral Autoencoder

## Model
- Name: tiny Conv1d-style autoencoder
- Task type: representation learning / anomaly candidate ranking
- Astronomy / physics use case: spectral anomaly triage through reconstruction and latent support

## Input Structure
- Input object: one normalized toy spectrum per sample
- Shape: `(n_samples, wavelength_bins)`
- Units / normalization: teaching normalized flux from `data/small/{data_name}`
- Train-only preprocessing: thresholds calibrated on normal validation rows

## Architecture
- Main layers: encoder, low-dimensional bottleneck / latent representation, decoder
- Nonlinearities: teaching-size nonlinear encoding and reconstruction
- Pooling / bottleneck / attention, if any: compact latent bottleneck
- Output head: reconstructed spectrum and reconstruction-error route

## Training Objective
- Loss: reconstruction error on normal-like spectra
- Optimizer: hand-written teaching workflow in the notebook
- Epochs / batch size / learning rate: see notebook settings
- Early stopping or validation rule: ready threshold {ns["conv1d_ready_threshold"]:.4f}; anomaly threshold {ns["conv1d_anomaly_threshold"]:.4f}

## What It Learns
- Representation learned: compressed normal-spectrum structure
- Local / global structure captured: broad continuum shape and local residual windows
- Relation to baseline: mean-spectrum baseline is the minimum reconstruction reference

## Diagnostics
- Training vs validation curve: validation-threshold summary in notebook outputs
- Main evaluation metric: reconstruction error and latent nearest-neighbor support
- Error / residual / review artifact: `autoencoder_routes.csv`, `latent_retrieval_triage.csv`
- Representation or activation check: latent retrieval triage

## Failure Modes
- Data issue: artifacts can look like anomalies
- Model issue: manifold-edge normal spectra may receive high reconstruction error
- Scientific interpretation issue: high error is a review flag, not a new-object declaration

## Scientific Boundary
- Supported claim: the autoencoder can rank toy spectra for review.
- Unsupported claim: reconstruction error proves a new physical class.
- Human review needed: manual_review and anomaly_candidate rows
""")

    _write_text(results_dir / "model_experiment_record_autoencoder.md", f"""
# Model Experiment Record: Autoencoder Anomaly Workflow

## 1. Task
- Scientific question: which toy spectra deserve anomaly review after reconstruction?
- ML task: representation learning / anomaly candidate ranking.
- Prediction target / discovery goal: normal_like, manual_review, or anomaly_candidate route.
- Intended use: Part V representation-learning delivery example.

## 2. Dataset Contract
- Dataset Contract link: `dataset_contract_autoencoder.md`
- Data Card link: teaching data in `data/small/{data_name}`
- Key Evidence Records: exported reconstruction routes and latent retrieval triage.

## 3. Split / Role Assignment
- Train / validation / test split: normal training rows, validation rows, held-out normal/anomaly rows
- Split unit: spectrum sample ID
- When was the test set opened? after validation thresholds were set

## 4. Baseline
- Baseline type: mean-spectrum reconstruction
- Baseline reason: checks whether learned compression improves beyond one average template

## 5. Model
- Model family: tiny Conv1d-style autoencoder
- Deep Learning Model Card link: `deep_learning_model_card_autoencoder.md`
- Training entry point: this notebook

## 6. Evaluation
- Metrics: reconstruction error, peak-window residual, route counts
- Threshold, if any: ready {ns["conv1d_ready_threshold"]:.4f}; anomaly {ns["conv1d_anomaly_threshold"]:.4f}
- Main diagnostic figure: `figures/autoencoder_reconstruction_errors.png`

## 7. Error Analysis
- Main failure cases: manifold-edge normal spectra and localized anomalies
- Relation to data quality / physical regime: reconstruction error is a review signal, not a discovery claim

## 8. Limit
- Supported claim: high reconstruction error marks candidates for review.
- Unsupported claim: anomaly route alone proves a new physical class.
""")

    _write_text(results_dir / "trust_statement_autoencoder.md", f"""
# Trust Statement: Autoencoder Anomaly Workflow

## Model Output
- Result: route counts {route_counts}
- Main metric / diagnostic: reconstruction error and latent retrieval triage

## Distribution Status
- In-distribution / out-of-distribution / unclear: unclear for high-error spectra until reviewed
- Evidence: validation-calibrated thresholds and nearest-neighbor latent support

## Uncertainty
- Main uncertainty source: tiny normal training set and synthetic anomalies
- Estimated by: validation threshold and manual-review route

## Failure Boundary
- Known failure region: manifold edges and localized spectral artifacts
- Human review needed: manual_review and anomaly_candidate rows

## Claim Boundary
- Supported claim: model can rank candidates for review.
- Unsupported claim: reconstruction error is a discovery declaration.
""")

    print(f"Exported Ch33 trusted delivery package to {results_dir}")


def export_ch34_attention_delivery(ns: dict) -> None:
    results_dir = Path("results/ch34_attention_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    routes = ns["patch_workflow_routes"]
    _export_rows(results_dir / "masked_patch_routes.csv", [
        {**item, "confidence": round(item["confidence"], 4)} for item in routes
    ])
    _export_rows(results_dir / "masked_patch_validation.csv", [
        {**item, "confidence": round(item["confidence"], 4)} for item in ns["patch_workflow_validation_predictions"]
    ])
    _simple_bar_figure(
        figures_dir / "masked_patch_route_confidence.png",
        [item["sample_id"] for item in routes],
        [item["confidence"] for item in routes],
        "Masked-patch attention routing",
        "confidence",
    )

    baseline_accuracy = ns["accuracy"](ns["patch_workflow_bag_predictions"])
    model_accuracy = ns["accuracy"](ns["patch_workflow_test_predictions"])
    review_count = sum(item["route"] == "manual_review" for item in routes)
    data_name = ns["PATCH_WORKFLOW_DATA_PATH"].name

    _write_text(results_dir / "dataset_contract_attention.md", f"""
# Dataset Contract: Masked-Patch Attention Workflow

## 1. Task Definition
- ML task: masked patch prediction / representation learning
- Scientific question: can ordered context recover a hidden patch when bag-of-patches cannot?
- Prediction target: masked target patch and ready/review route
- Intended use: teaching package for attention and foundation-model pretraining boundaries

## 2. Sample Definition
- One sample is one token / patch sequence row from `data/small/{data_name}`.
- Sample ID: `sample_id`

## 3. Input Features
- Visible token / patch sequence.
- Position metadata implied by sequence order.
- Review metadata for boundary rows.

## 4. Target / Label
- Target: masked patch value or class.
- Label leakage risk: the masked target must not appear in visible input features.

## 5. Selection and Split
- Split roles: train, validation, clean test, review.
- Threshold is calibrated on validation rows before clean-test and review interpretation.

## 6. Known Limits
- Tiny synthetic token/patch data.
- Attention weights explain model routing behavior, not physical causality.
""")

    _write_text(results_dir / "deep_learning_model_card_attention.md", f"""
# Deep Learning Model Card: Tiny Masked-Patch Attention

## Model
- Name: tiny two-head masked-patch attention learner
- Task type: masked patch prediction / representation learning
- Astronomy / physics use case: toy bridge from sequence context to scientific foundation-model ideas

## Input Structure
- Input object: one visible token / patch sequence per sample
- Shape: `(n_samples, sequence_length, patch_features)`
- Units / normalization: teaching token/patch values from `data/small/{data_name}`
- Train-only preprocessing: validation threshold selected before test/review routes

## Architecture
- Main layers: patch tokens, positional context, two attention heads, masked-patch output head
- Nonlinearities: softmax attention weights
- Pooling / bottleneck / attention, if any: multi-head attention over visible patches
- Output head: masked-patch prediction and confidence route

## Training Objective
- Loss: masked-patch prediction loss
- Optimizer: hand-written tiny learner in the notebook
- Epochs / batch size / learning rate: heads {ns["PATCH_WORKFLOW_HEADS"]}, epochs {ns["PATCH_WORKFLOW_EPOCHS"]}
- Early stopping or validation rule: ready threshold {ns["patch_workflow_ready_threshold"]:.4f}

## What It Learns
- Representation learned: ordered context for recovering a masked patch
- Local / global structure captured: position-aware dependencies that bag-of-patches discards
- Relation to baseline: bag-of-patches accuracy {baseline_accuracy:.3f}; attention clean-test accuracy {model_accuracy:.3f}

## Diagnostics
- Training vs validation curve: masked-patch validation summary
- Main evaluation metric: clean-test accuracy and confidence routing
- Error / residual / review artifact: `masked_patch_routes.csv`
- Representation or activation check: attention head peak positions in notebook outputs

## Failure Modes
- Data issue: blended anchors or repeated masks
- Model issue: attention may overfit synthetic token rules
- Scientific interpretation issue: attention weights are model-behavior evidence, not causal proof

## Scientific Boundary
- Supported claim: attention can use ordered context in this toy masked-patch task.
- Unsupported claim: foundation-model outputs are automatically trustworthy or physically causal.
- Human review needed: all manual_review rows
""")

    _write_text(results_dir / "model_experiment_record_attention.md", f"""
# Model Experiment Record: Masked-Patch Attention Workflow

## 1. Task
- Scientific question: can position-aware attention recover a masked spectral patch when bag-of-patches cannot?
- ML task: masked patch prediction / representation learning.
- Prediction target / discovery goal: target patch and ready/review route.
- Intended use: Part V attention / foundation-model boundary example.

## 2. Dataset Contract
- Dataset Contract link: `dataset_contract_attention.md`
- Data Card link: teaching data in `data/small/{data_name}`
- Key Evidence Records: masked-patch routes and validation artifacts.

## 3. Split / Role Assignment
- Train / validation / test split: train, validation, clean test, review
- Split unit: token sequence sample ID
- Random seed: {ns["PATCH_WORKFLOW_SEED"]}
- When was the test set opened? after validation threshold selection

## 4. Baseline
- Baseline type: bag-of-visible-patches nearest centroid
- Baseline result: accuracy {baseline_accuracy:.3f}

## 5. Model
- Model family: tiny two-head masked-patch attention learner
- Key parameters / hyperparameters: heads={ns["PATCH_WORKFLOW_HEADS"]}, epochs={ns["PATCH_WORKFLOW_EPOCHS"]}
- Deep Learning Model Card link: `deep_learning_model_card_attention.md`
- Training entry point: this notebook

## 6. Evaluation
- Metrics: masked-patch accuracy, confidence threshold, review capture
- Threshold, if any: {ns["patch_workflow_ready_threshold"]:.4f}
- Main diagnostic figure: `figures/masked_patch_route_confidence.png`

## 7. Error Analysis
- Main failure cases: blend-anchor and double-mask review rows
- Relation to data quality / physical regime: attention confidence is not a scientific explanation

## 8. Limit
- Supported claim: position-aware attention solves this toy masked-patch task better than bag-of-patches.
- Unsupported claim: attention weights alone prove physical interpretation.
""")

    _write_text(results_dir / "trust_statement_attention.md", f"""
# Trust Statement: Masked-Patch Attention Workflow

## Model Output
- Result: clean-test accuracy {model_accuracy:.3f}; manual-review rows {review_count}
- Main metric / diagnostic: masked-patch route confidence

## Distribution Status
- In-distribution / out-of-distribution / unclear: review rows are intentionally boundary cases
- Evidence: clean/test/review split and validation threshold

## Interpretability
- Main feature dependence: head peak positions and tokens
- Interpretation method: inspect head peaks and compare against bag baseline
- Why this is not causal proof: attention routing explains model behavior, not physical causality

## Failure Boundary
- Known failure region: blended anchors, repeated masks, low-confidence routes
- Human review needed: all manual_review rows

## Claim Boundary
- Supported claim: attention can use ordered context in this toy task.
- Unsupported claim: foundation-model outputs are automatically trustworthy.
""")

    print(f"Exported Ch34 trusted delivery package to {results_dir}")


def export_ch37_literature_delivery(ns: dict) -> None:
    results_dir = Path("results/ch37_literature_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    _export_rows(results_dir / "human_review_queue.csv", ns["human_review_queue"])
    _export_rows(results_dir / "verified_claims.csv", ns["verified_claims"])
    _export_rows(results_dir / "caveat_claims.csv", ns["caveat_claims"])
    _write_text(results_dir / "report_skeleton.md", ns["report_skeleton"])
    _simple_bar_figure(
        figures_dir / "claim_ledger_metrics.png",
        ["baseline precision", "baseline coverage", "route agreement"],
        [ns["baseline_precision_at_3"], ns["baseline_claim_coverage"], ns["route_agreement"]],
        "Literature workflow metrics",
        "score",
    )

    snapshot = ns["reading_snapshot"]
    _export_rows(results_dir / "reading_snapshot.csv", [snapshot])
    data_name = ns["DATA_PATH"].name

    _write_text(results_dir / "evidence_record_literature.md", f"""
# Evidence Record: AI-Assisted Literature Reading

## 1. Input
- Data / file path, preferably relative to project root: `data/small/{data_name}`
- Input object: evidence-card table with note IDs, claim IDs, citation status, and excerpts

## 2. Operation
- Compared salience-only summary baseline with structured claim-ledger routing.
- Routed notes into verified claims, caveats, method notes, human review, or exclude.
- Built report skeleton only after claim ledger was stable.

## 3. Output
- Verified claims: `verified_claims.csv`
- Caveats: `caveat_claims.csv`
- Human-review queue: `human_review_queue.csv`
- Report skeleton: `report_skeleton.md`

## 4. Check
- Route agreement: {ns["route_agreement"]:.3f}
- Human-review count: {len(ns["human_review_queue"])}
- Citation or quote statuses that are not clean stay out of final prose.

## 5. Limit
- This does not replace reading the source paper.
- It supports evidence organization, not automatic literature judgment.

## 6. Reuse in ML
- Reusable as claim-ledger evidence for capstone interpretation and disclosure.
""")

    _write_text(results_dir / "ai_usage_log_literature.md", f"""
# AI Usage Log: Literature Reading and Report Writing

## 1. Use Context
- Project / chapter: Ch37 literature reading and report writing
- Task: structure notes into claim ledger and report skeleton
- AI tool / model, if known: simulated local workflow, no live API call
- Date: notebook run date

## 2. Input Boundary
- Materials provided to AI: local teaching evidence cards
- Materials not provided to AI: copyrighted full-text PDFs or private notes beyond the table
- Data / privacy / copyright constraint: use excerpts only within course teaching data

## 3. Interaction / Action
- Prompt or instruction summary: route claims before writing prose
- Files or sections affected: claim ledger and report skeleton

## 4. Output Kept
- Output accepted: verified claim ledger, caveat list, report skeleton
- Output rejected or rewritten: direct salience-only summary baseline
- Reason for acceptance / rejection: baseline mixes unresolved citation/quote states into prose

## 5. Verification
- Citation or source checked: unresolved entries remain in human_review_queue.csv
- Human review needed: {len(ns["human_review_queue"])} notes

## 6. Responsibility and Disclosure
- What the student verified: claim routing, citation status, caveat retention
- Disclosure note / AI-use statement: AI assisted organization and drafting only after claim ledger construction.
""")

    _write_text(results_dir / "disclosure_note_literature.md", """
# Disclosure Note

AI assistance was used to organize evidence cards into a claim ledger and draft a report skeleton. Claims with unresolved citation, quotation, or page-level checks were kept in the human-review queue and should not enter final prose until verified.
""")

    print(f"Exported Ch37 trusted delivery package to {results_dir}")


def export_ch38_ethics_delivery(ns: dict) -> None:
    results_dir = Path("results/ch38_ethics_delivery")
    figures_dir = results_dir / "figures"
    results_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    _export_rows(results_dir / "allowed_uses.csv", ns["allowed_queue"])
    _export_rows(results_dir / "license_review_queue.csv", ns["license_review_queue"])
    _export_rows(results_dir / "human_only_queue.csv", ns["human_only_queue"])
    _export_rows(results_dir / "prohibit_queue.csv", ns["prohibit_queue"])
    _write_text(results_dir / "ai_use_statement_skeleton.md", ns["statement_skeleton"])
    _export_rows(results_dir / "ethics_snapshot.csv", [ns["ethics_snapshot"]])
    _simple_bar_figure(
        figures_dir / "ethics_route_metrics.png",
        ["baseline ready", "allowed coverage", "route agreement"],
        [ns["baseline_allowed_precision_at_4"], ns["baseline_allowed_coverage"], ns["route_agreement"]],
        "AI ethics routing metrics",
        "score",
    )

    data_name = ns["DATA_PATH"].name
    _write_text(results_dir / "evidence_record_ai_ethics.md", f"""
# Evidence Record: AI Ethics Routing

## 1. Input
- Data / file path, preferably relative to project root: `data/small/{data_name}`
- Input object: AI use-case table with workflow stage, material source, sharing boundary, and reference route

## 2. Operation
- Compared speed-gain baseline with structured AI-use routing.
- Routed cases into allow_with_disclosure, license_review, human_only, or prohibit.
- Built AI-use statement from allowed and held-back queues.

## 3. Output
- Allowed uses: `allowed_uses.csv`
- License review queue: `license_review_queue.csv`
- Human-only queue: `human_only_queue.csv`
- Prohibited queue: `prohibit_queue.csv`
- AI-use statement skeleton: `ai_use_statement_skeleton.md`

## 4. Check
- Route agreement: {ns["route_agreement"]:.3f}
- Baseline blocked-case rate: {ns["baseline_blocked_case_rate"]:.3f}
- Disclosure is generated from routed use cases, not memory.

## 5. Limit
- This is a teaching workflow, not legal advice.
- Real projects must follow course, institutional, journal, and data-provider policies.

## 6. Reuse in ML
- Reusable as integrity and disclosure evidence for capstone delivery.
""")

    _write_text(results_dir / "ai_usage_log_ethics.md", f"""
# AI Usage Log: Ethics and Disclosure Workflow

## 1. Use Context
- Project / chapter: Ch38 AI ethics, copyright, and research norms
- Task: route AI use cases and draft AI-use statement
- AI tool / model, if known: simulated local workflow, no live API call
- Date: notebook run date

## 2. Input Boundary
- Materials provided to AI: local teaching use-case table
- Materials not provided to AI: proprietary data, copyrighted full-text material, credentials, final signoff decisions
- Data / privacy / copyright constraint: teaching examples only

## 3. Interaction / Action
- Prompt or instruction summary: route before drafting disclosure
- Files or sections affected: route queues and AI-use statement skeleton

## 4. Output Kept
- Output accepted: routed queues and statement skeleton
- Output rejected or rewritten: speed-first automation baseline
- Reason for acceptance / rejection: speed-first ranking admits prohibited or review-only uses

## 5. Verification
- Code run / tests passed: route queues and snapshot exported
- Human review needed: license_review and human_only queues

## 6. Responsibility and Disclosure
- What the student verified: material boundary, permission route, final signoff boundary
- Disclosure note / AI-use statement: use `ai_use_statement_skeleton.md` only after confirming real project facts.
""")

    _write_text(results_dir / "disclosure_note_ethics.md", """
# Disclosure Note

AI use should be disclosed from the structured route log. Allowed uses may be retained with disclosure; license-review and human-only items require human resolution; prohibited items should not be executed or retained.
""")

    print(f"Exported Ch38 trusted delivery package to {results_dir}")
