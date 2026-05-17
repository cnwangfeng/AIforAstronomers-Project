"""Export small Part V trusted-delivery packages from teaching notebooks."""

from __future__ import annotations

import csv
from pathlib import Path


def _write_text(path: Path, content: str) -> None:
    path.write_text(content.strip() + "\n", encoding="utf-8")


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
- Algorithm Card link: CNN / transfer-learning sidebar in Ch31
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
- Algorithm Card link: 1D convolution sidebar in Ch32
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

    _write_text(results_dir / "model_experiment_record_autoencoder.md", f"""
# Model Experiment Record: Autoencoder Anomaly Workflow

## 1. Task
- Scientific question: which toy spectra deserve anomaly review after reconstruction?
- ML task: representation learning / anomaly candidate ranking.
- Prediction target / discovery goal: normal_like, manual_review, or anomaly_candidate route.
- Intended use: Part V representation-learning delivery example.

## 2. Dataset Contract
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
- Algorithm Card link: autoencoder sidebar in Ch33
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

    _write_text(results_dir / "model_experiment_record_attention.md", f"""
# Model Experiment Record: Masked-Patch Attention Workflow

## 1. Task
- Scientific question: can position-aware attention recover a masked spectral patch when bag-of-patches cannot?
- ML task: masked patch prediction / representation learning.
- Prediction target / discovery goal: target patch and ready/review route.
- Intended use: Part V attention / foundation-model boundary example.

## 2. Dataset Contract
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
- Algorithm Card link: attention / transformer sidebar in Ch34
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
