# Small Teaching Datasets

This directory stores small datasets that can safely live in the repository and
be used in notebooks, CI checks, and classroom demos.

Current datasets:

- `planetary_orbits_demo.csv`
  A tiny Solar System inspired table for early Python, I/O, and plotting
  notebooks.
- `stellar_photometry_demo.csv`
  A small Gaia-style synthetic table for uncertainty, stellar catalog, and
  HR-diagram notebooks.
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

Dataset notes:

- keep files small enough for fast sync and classroom use
- document units and provenance clearly
- prefer CSV or similarly transparent formats for intro chapters
