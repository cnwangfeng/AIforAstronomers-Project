# Part V Quick Review: Deep Learning, Modern AI, and Trusted Delivery

Status: diagnostic review and light alignment target.

Part V is already structurally strong. Its chapters consistently keep a
baseline-first posture, avoid treating deep models as magic, and repeatedly
return to validation, review queues, human handoff, disclosure, and final
scientific responsibility.

The main editorial risk is not missing content. The risk is terminology drift:
some passages still refer to `model card`, `usage log`, `Reproducibility card`,
`Integrity card`, and other older card language. If left unchanged, Part V could
quietly recreate a family of local records after Part I/II and Part III have
already converged on unified record systems.

## Overall Judgment

Part V should not become a second machine-learning textbook or a catalogue of
modern AI tools. Its role is to answer a narrower question:

How can complex models and AI assistants enter a research project without
breaking baseline discipline, validation evidence, review boundaries, and human
responsibility?

The strongest current through-line is:

- start from a simple baseline;
- introduce one complex tool only when it solves a specific limitation;
- preserve validation artifacts and failure examples;
- route uncertain cases to review rather than forcing automation;
- disclose AI assistance from a real usage record, not from memory.

That is the right direction.

## Interface Alignment

Part V should inherit the frozen Part III/IV interface instead of inventing a
new record family.

For deep learning chapters:

- Dataset Contract, when new data enters the model;
- Model Experiment Record;
- Algorithm Card, usually short or sidebar depth;
- Evaluation artifact;
- Error / failure / review artifact;
- Trust Statement.

For LLM, agent, reading, writing, and ethics chapters:

- Evidence Record, when the work is primarily code, text, or workflow evidence;
- AI Usage Log, as a lightweight AI-tool extension;
- Verification artifact, such as regression checks, action logs, claim ledgers,
  or routed queues;
- Disclosure note / AI-use statement;
- Trust Statement when a model result or automated decision enters a scientific
  claim.

The important editorial rule is:

Part V may introduce AI Usage Log, but it should not introduce separate
Programming Record, Agent Record, Literature Record, Ethics Record, or Integrity
Card families.

## Chapter-Level Review

### Ch30 Neural Network Basics

Current role is solid: it treats neural networks as a controlled increase in
function complexity after a linear baseline fails. The chapter should remain a
minimal nonlinear-regression bridge, not a neural-network encyclopedia.

Keep:

- linear baseline before the network;
- loss / hidden layer / activation intuition;
- comparison of error patterns, not just final score.

Light requirement:

- the minimum output should be a Model Experiment Record plus a Trust Statement
  paragraph explaining why the neural network is justified over the baseline.

### Ch31 CNNs

This is the best candidate for a Part V deep-learning sample chapter. It already
connects cleanly to Ch29 morphology: raw-pixel baseline, local convolution
features, transfer-learning intuition, validation threshold, and review queue.

Keep:

- raw-pixel baseline;
- local-feature explanation before framework API;
- frozen backbone / target head / quality-gate workflow;
- review queue as a first-class output.

Light requirement:

- make the case-package expectation explicit: Model Experiment Record, feature
  or validation diagnostic, review queue, Trust Statement.

### Ch32 1D CNNs for Spectra

The chapter correctly distinguishes spectra from generic vectors by foregrounding
wavelength alignment, normalization, local line patterns, and shifted features.

Keep:

- raw-window baseline;
- continuum normalization;
- shifted-line failure analysis;
- review queue for low-SNR or contaminated spectra.

Light requirement:

- make clear that 1D convolution supports local pattern reuse, but does not
  remove the need for wavelength-grid and preprocessing evidence.

### Ch33 Autoencoders

The chapter has the right epistemic restraint: reconstruction error is a
candidate-ranking signal, not a discovery announcement.

Keep:

- mean-spectrum baseline;
- latent representation as compression, not physical truth;
- validation-calibrated review queue;
- anomaly review before scientific claim.

Light requirement:

- align anomaly outputs to Trust Statement language: supported claim is
  "candidate deserves review," not "object is novel."

### Ch34 Transformers, Attention, and Foundation Models

The chapter's baseline-first token examples work well because they show what
sequence order adds beyond bag-of-token counting.

Keep:

- bag-of-tokens baseline;
- attention as context-dependent information routing;
- caution that attention weights are not automatic scientific explanations;
- foundation-model boundary language.

Light requirement:

- emphasize that foundation-model transfer requires a Dataset Contract /
  input-boundary check before claims move into a project.

### Ch35 LLM-Assisted Programming

This is a strong workflow chapter. The AI-draft transit-depth example makes the
central lesson concrete: code that looks plausible can fail basic quality and
reference checks.

Keep:

- AI draft versus verified implementation;
- regression checks;
- notebook rerun discipline;
- rejected outputs as evidence.

Required alignment:

- replace `Reproducibility card` / `Integrity card` language with Evidence
  Record, AI Usage Log, verification artifact, and disclosure note.

### Ch36 Agentic Workflows

The chapter correctly treats agentic workflow as a protocol problem, not a
"make the AI do more" problem.

Keep:

- single-score baseline;
- explicit gates;
- action log;
- manual review as correct endpoint;
- human signoff.

Required alignment:

- replace `Integrity card` and `Evaluation / Interpretation cards` language with
  AI Usage Log, action log, review queue, and Trust Statement / disclosure note.

### Ch37 Literature Reading and Report Writing

The chapter has the right central object: claim ledger. It prevents AI-assisted
writing from collapsing evidence into fluent prose.

Keep:

- freeform-summary baseline;
- verified claims versus caveats;
- citation/page review queue;
- human review before report claims.

Required alignment:

- replace `Interpretation card` / `Integrity card` language with claim ledger,
  Evidence Record, AI Usage Log, and disclosure note.

### Ch38 Ethics, Copyright, and Research Norms

This chapter is well placed as the Part V close. It translates ethics into
routes, queues, disclosure, permissions, and signoff rather than abstract
attitudes.

Keep:

- speed-gain baseline;
- allow / license review / human only / prohibit routing;
- disclosure versus permission versus final signoff distinction;
- AI-use statement from actual logs.

Light requirement:

- tie the final AI-use statement explicitly to AI Usage Log fields.

## Recommended Immediate Pass

Do a light interface pass, not a deep rewrite:

1. Add a lightweight `ai_usage_log_template.md`.
2. Update `part5_intro.tex` so deep models use the Part III/IV model package and
   AI-tool chapters use Evidence Record plus AI Usage Log.
3. Update `part5_synthesis.tex` so the trusted delivery package contains:
   - Model Experiment Record or Evidence Record;
   - AI Usage Log, if AI assistance/tool use is involved;
   - validation artifact;
   - failure/review artifact;
   - Trust Statement or disclosure note.
4. Replace remaining old card-family references in Ch35--Ch37.
5. Keep Ch31 and Ch35/36 as likely sample chapters for the next deeper pass.

## Freeze Criterion

Part V can be considered interface-aligned when a student can explain any deep
model or AI-assisted workflow using:

- why the complex tool was needed beyond the baseline;
- what input boundary applied;
- what record or log preserves the run / interaction;
- what validation evidence exists;
- what failed or required review;
- what the student personally verified and is willing to disclose.

