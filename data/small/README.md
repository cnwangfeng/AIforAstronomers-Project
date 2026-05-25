# Small Teaching Datasets

This directory stores small datasets that can safely live in the repository and
be used in notebooks, CI checks, and classroom demos.

The main textbook line now runs through Part I--V. Files whose names begin with
`capstone_` are retained as historical/teaching auxiliary datasets for optional
project-support material; they are not part of the main textbook companion
workflow.

Current datasets:

- `planetary_orbits_demo.csv`
  A tiny Solar System inspired table for early Python, I/O, and plotting
  notebooks.
- `stellar_photometry_demo.csv`
  A small Gaia-style synthetic table for uncertainty, stellar catalog, and
  HR-diagram notebooks.
- `fits_wcs_cutout_demo.csv`
  A tiny FITS/WCS-style cutout table for the Part II image, WCS, and basic
  aperture-photometry chapter and notebook.
- `spectral_wavelength_redshift_demo.csv`
  A tiny teaching spectroscopy table for the Part II wavelength, line feature,
  normalization, and redshift chapter and notebook.
- `lightcurve_period_demo.csv`
  A tiny time-series table for the Part II period-search, phase-folding, and
  light-curve workflow chapter and notebook.
- `physics_model_fit_demo.csv`
  A tiny physics-experiment table for the Part II model-fitting, residual,
  and Monte Carlo uncertainty chapter and notebook.
- `photometric_redshift_demo.csv`
  A tiny photometric-redshift table for the Part III regression workflow
  notebook.
- `object_classification_demo.csv`
  A tiny object-classification table for the Part III classification and
  model-evaluation notebooks.
- `object_preprocessing_demo.csv`
  A tiny preprocessing table for the Part III feature-engineering,
  leakage-check, and preprocessing-audit notebook.
- `stellar_teff_model_selection_demo.csv`
  A tiny stellar color-temperature table for the Part III model-selection and
  hyperparameter notebook.
- `stellar_hr_unsupervised_demo.csv`
  A tiny HR-diagram table for the Part III unsupervised-learning notebook.
- `spectral_anomaly_demo.csv`
  A tiny spectral-feature table for the Part III anomaly-detection notebook.
- `gaia_hr_case_demo.csv`
  A tiny Gaia HR case-study table for the Part IV HR-diagram case notebook.
- `photoz_case_demo.csv`
  A tiny photometric-redshift case-study table for the Part IV photo-z case
  notebook.
- `photoz_trust_demo.csv`
  A tiny trust and coverage-diagnostic table for the Part IV photo-z
  uncertainty and interpretation case workflow.
- `spectral_classification_case_demo.csv`
  A tiny spectral-classification case-study table for the Part IV spectrum
  classification notebook.
- `galaxy_morphology_case_demo.csv`
  A small synthetic Galaxy Zoo style morphology table for the Part IV galaxy
  morphology case study notebook.
- `neural_network_regression_demo.csv`
  A small synthetic nonlinear-regression table for the Part V neural-network
  basics notebook.
- `cnn_cutout_demo.csv`
  A tiny synthetic galaxy-cutout table for the Part V convolution and local
  feature notebook.
- `cnn_transfer_learning_demo.csv`
  A tiny synthetic source/target cutout table for the Part V convolution,
  local-feature, and transfer-learning extension workflow.
- `cnn_transfer_workflow_demo.csv`
  A tiny synthetic source/target cutout workflow table with
  source/adapt/validation/test/review roles for the deeper Part V image-CNN
  and transfer-learning extension.
- `spectral_conv1d_demo.csv`
  A tiny synthetic spectral-window table for the Part V one-dimensional
  convolution notebook.
- `spectral_conv1d_workflow_demo.csv`
  A tiny synthetic spectral-window workflow table with continuum slope,
  quality flags, and train/validation/test/review roles for the deeper Part V
  one-dimensional convolution notebook extension.
- `spectral_autoencoder_demo.csv`
  A tiny synthetic spectral-window table for the Part V representation-learning
  and autoencoder notebook.
- `spectral_token_attention_demo.csv`
  A tiny tokenized spectral-sequence table for the Part V transformer,
  attention, and scientific-foundation-model notebook.
- `spectral_masked_token_workflow_demo.csv`
  A tiny masked-token workflow table with clean train/validation/test rows and
  manual-review cases for the deeper Part V transformer and attention notebook
  extension.
- `spectral_masked_patch_workflow_demo.csv`
  A tiny masked-patch workflow table with clean train/validation/test rows and
  manual-review cases for the deeper Part V transformer, patch-token, and
  pretraining-objective notebook extension.
- `lightcurve_debug_demo.csv`
  A tiny light-curve debugging table for the Part V LLM-assisted research
  programming, code-verification, and notebook-workflow notebook.
- `transient_agent_workflow_demo.csv`
  A tiny transient-candidate triage table for the Part V agentic research
  assistant, tool-calling, and workflow-boundary notebook.
- `literature_reading_workflow_demo.csv`
  A tiny paper-evidence-card table for the Part V literature-reading,
  claim-ledger, and report-writing notebook.
- `ai_ethics_workflow_demo.csv`
  A tiny AI-usage-case table for the Part V AI-ethics, copyright,
  academic-integrity, and usage-statement notebook.
- `capstone_project_workflow_demo.csv`
  A tiny historical capstone-project board table for the project-integration,
  readiness-routing, and delivery-workflow notebook.
- `capstone_project_scoping_demo.csv`
  A tiny historical capstone-project proposal table for the topic-selection,
  scope-control, and pilot-readiness notebook.
- `capstone_delivery_review_demo.csv`
  A tiny historical capstone final-delivery review table for the report,
  presentation, reproducibility, and signoff notebook.
- `capstone_rubric_case_template_demo.csv`
  A tiny historical capstone rubric and case-template table for the grading,
  feedback-routing, and student revision-checklist notebook.
- `capstone_trial_teaching_feedback_demo.csv`
  A tiny historical capstone trial-teaching feedback table for the student
  handout, TA calibration, runtime, privacy-boundary, and rollout notebook.
- `capstone_course_calendar_demo.csv`
  A tiny historical 16-week capstone course-calendar table for the milestone,
  checkpoint, instructor-intervention, and final-delivery notebook.
- `capstone_student_handout_ta_guide_demo.csv`
  A tiny historical capstone student-handout and TA grading-guide release table for the
  historical material publishing, policy-review, and calibration notebook.
- `capstone_revision_archive_feedback_demo.csv`
  A tiny historical capstone revision and archive-feedback table for the
  course-run feedback, reproducibility, policy-review, and public-archive
  notebook.
- `capstone_instructor_handoff_demo.csv`
  A tiny historical capstone instructor-handoff table for the course-run evidence,
  owner assignment, unresolved-risk, and handoff-package notebook.
- `capstone_public_release_maintenance_demo.csv`
  A tiny historical capstone public-release and course-maintenance table for the
  release index, license-boundary, owner assignment, stale-material audit, and
  maintenance-checklist notebook.
- `capstone_launch_qa_adoption_demo.csv`
  A tiny historical capstone launch-QA and adoption-note table for the public
  release QA, link-check, smoke-test, support-boundary, and adoption-note
  notebook.
- `capstone_adoption_feedback_maintenance_demo.csv`
  A tiny historical capstone adoption-feedback and course-maintenance table for
  feedback triage, evidence check, owner assignment, maintenance cadence, and
  release-retrospective notebook.
- `capstone_final_package_closure_demo.csv`
  A tiny historical capstone final-package and closure-checklist table for the
  package index, closure gate, owner handoff, dependency sync, and final-course-
  package notebook.
- `capstone_course_package_directory_release_notes_demo.csv`
  A tiny historical capstone course-package directory and release-note table for
  the package directory, version pointer, audience copy, and
  publication-entry notebook.
- `capstone_semester_reboot_preflight_demo.csv`
  A tiny historical capstone semester-reboot and preflight table for the startup
  checklist, term refresh, blocker triage, owner assignment, and reboot package
  notebook.
- `capstone_failure_mode_escalation_demo.csv`
  A tiny historical capstone failure-mode and escalation table for the incident
  routing, local patch, rollout pause, human review, and escalation-playbook
  notebook.
- `capstone_contingency_substitute_handoff_demo.csv`
  A tiny historical capstone contingency and substitute-handoff table for the
  minimal run package, substitute owner, context brief, and emergency handoff
  notebook.
- `capstone_shutdown_warmstart_demo.csv`
  A tiny historical capstone shutdown and warm-start table for the end-of-term
  closure, archive snapshot, next-cohort seed, and handoff-to-next-run notebook.
- `capstone_alumni_mentor_relay_demo.csv`
  A tiny historical capstone alumni-example and mentor-relay table for the mentor
  availability, privacy boundary, handoff scope, and continuity notebook.
- `capstone_community_memory_maintenance_ledger_demo.csv`
  A tiny historical capstone community-memory and long-term-maintenance table for
  retention value, refresh cadence, access boundary, and ledger
  workflow notebook.
- `capstone_external_collaboration_guest_intake_demo.csv`
  A tiny historical capstone external-collaboration and guest-intake table for the
  collaboration boundary, host owner, scope control, and guest-project intake
  notebook.

Dataset notes:

- current CSV files: 52, matching `data/manifest.yml`
- keep files small enough for fast sync and classroom use
- document units and provenance clearly
- prefer CSV or similarly transparent formats for intro chapters
