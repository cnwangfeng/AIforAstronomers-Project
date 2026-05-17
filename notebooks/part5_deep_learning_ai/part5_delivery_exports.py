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

