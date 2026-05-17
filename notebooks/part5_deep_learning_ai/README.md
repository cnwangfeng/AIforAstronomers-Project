# Part V Notebook Index

These notebooks introduce deep learning and modern AI workflows for the
textbook. They continue the repo style of using tiny teaching datasets and
pure-Python baselines first, with optional framework comparisons when the
environment has extra libraries installed.

Notebook outputs should align with the frozen Part III/IV interface. Deep-model
notebooks should be able to feed a Model Experiment Record, evaluation artifact,
error/review artifact, and Trust Statement. LLM, agent, reading, writing, and
ethics notebooks should be able to feed an Evidence Record, AI Usage Log,
verification artifact, and disclosure note.

Current sample delivery exports:

- Ch31 exports `results/ch31_cnn_delivery/` as a deep-model package with Dataset Contract, Model Experiment Record, routing/review artifacts, and Trust Statement.
- Ch32 exports `results/ch32_spectral_conv_delivery/` as a 1D spectral CNN package with Dataset Contract, Model Experiment Record, route artifacts, and Trust Statement.
- Ch33 exports `results/ch33_autoencoder_delivery/` as an autoencoder anomaly-review package with Model Experiment Record, reconstruction/retrieval artifacts, and Trust Statement.
- Ch34 exports `results/ch34_attention_delivery/` as an attention / masked-patch package with Model Experiment Record, route artifacts, and Trust Statement.
- Ch35 exports `results/ch35_llm_programming_delivery/` as an AI-assisted programming package with Evidence Record, AI Usage Log, regression checks, validation figure, and disclosure note.
- Ch36 exports `results/ch36_agentic_workflow_delivery/` as an agentic workflow package with Evidence Record, AI Usage Log, action log, manual-review queue, routing figure, and disclosure note.
- Ch37 exports `results/ch37_literature_delivery/` as an AI-assisted literature package with Evidence Record, AI Usage Log, claim ledger artifacts, and disclosure note.
- Ch38 exports `results/ch38_ethics_delivery/` as an AI ethics/disclosure package with Evidence Record, AI Usage Log, route queues, and disclosure note.

Current notebook set:

- `ch30_neural_network_basics.ipynb`
- `ch31_convolutional_neural_networks.ipynb`
- `ch32_one_dimensional_convolutions_for_spectra.ipynb`
- `ch33_representation_learning_autoencoders.ipynb`
- `ch34_transformer_attention_foundation_models.ipynb`
- `ch35_llm_assisted_research_programming.ipynb`
- `ch36_agentic_research_assistants_tool_workflows.ipynb`
- `ch37_llm_literature_reading_report_writing.ipynb`
- `ch38_ai_ethics_copyright_research_norms.ipynb`

Later this directory will grow into:

- transfer-learning and real-image CNN notebooks
- deeper workflow-integrated model notebooks that can feed the Part VI capstone templates
