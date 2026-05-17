# Part IV Quick Review

Status: diagnostic review after Part III V3 Freeze.

Purpose: use Part IV as a pressure test for the frozen Part III interface before doing deep case rewrites.

---

## Overall Judgment

Part IV is structurally strong. It already behaves like a case-study section rather than a second algorithm textbook. The four current cases have clear scientific contexts, reasonable baselines, diagnostic artifacts, error/sample review, and interpretation boundaries.

The main issue is not content depth. The main issue is interface language.

Several chapters still describe final deliverables using older `Project/Data/Baseline/Model/Evaluation/Interpretation/Integrity card` language. After Part III V3 Freeze, Part IV should instead use:

```text
Dataset Contract -> Model Experiment Record -> Trust Statement
```

and package each case as:

```text
Dataset Contract
Model Experiment Record
Algorithm Card sidebar links
Evaluation artifact
Error analysis artifact
Trust Statement
```

This is a light alignment pass, not a content expansion pass.

---

## Part III Interface Pressure Test

### 1. Dataset Contract

Part IV already has enough material for Dataset Contract-style descriptions:

- Ch26: Gaia-like table fields, parallax quality, derived absolute magnitude, reference class.
- Ch27: SDSS-like colors, magnitude, galaxy type, spectroscopic redshift target.
- Ch28: wavelength grid, flux columns, SNR, quality flags, bad-pixel handling.
- Ch29: morphology labels, quality flags, vote fraction, traditional image features.

Gap: chapters often say "data contract" in prose, but the report templates do not consistently name `Dataset Contract` as a formal case artifact.

### 2. Model Experiment Record

All four chapters already contain the ingredients:

- task definition;
- baseline;
- model choice;
- split / fixed test logic, at least implicitly;
- diagnostic figure or table;
- failure sample review;
- limits.

Gap: these ingredients are currently framed as case-report sections or capstone cards, not as sections of a `Model Experiment Record`.

### 3. Algorithm Card

Part IV generally avoids re-teaching algorithms, which is good. It should use sidebar-level Algorithm Card references:

- Ch26: k-means, nearest-centroid classifier.
- Ch27: linear regression, optional random forest comparison.
- Ch28: PCA, nearest-centroid classifier, optional CNN upgrade path.
- Ch29: nearest-centroid classifier, optional CNN / transfer learning upgrade path.

Gap: Part IV should explicitly say these are sidebar references to Part III cards, not new algorithm tutorials.

### 4. Trust Statement

All four chapters already discuss limits and interpretation boundaries:

- Ch26: extinction, binaries, variables, Gaia selection effects, simplified labels.
- Ch27: rare galaxy types, training coverage, photometric system differences, photo-z extrapolation.
- Ch28: wavelength grid, bad pixels, normalization, SNR, instrument/pipeline differences.
- Ch29: image quality, vote fraction, projection effects, label noise, low-confidence review.

Gap: report templates should end with a named `Trust Statement`, not only "适用边界" or "有限结论".

---

## Chapter Review Matrix

| Chapter | Scientific task | Part III algorithm links | Current strength | Main gap |
|---|---|---|---|---|
| Ch26 Gaia HR | HR-structure exploration + stellar classification | Ch23 clustering, Ch19 classification, Ch20 diagnostics | Strong physical-first framing; error cases return to HR diagram | Replace capstone card language with Model Experiment Packet; make Dataset Contract / Trust Statement explicit |
| Ch27 Photo-z | Regression from colors/magnitude to reference redshift | Ch18 regression, Ch20 evaluation, Ch25 trust | Strong baseline and residual framing; clear rare-type failure discussion | Convert "photoz_report" into Model Experiment Record + Trust Statement language |
| Ch28 Spectral Classification | Preprocess spectra, PCA structure, classify spectrum types | Ch21 preprocessing, Ch23 PCA, Ch19 classification | Strong data-generation awareness; avoids CNN-first mistake | Replace Data/Reproducibility/Interpretation card language; add Algorithm Card sidebar references |
| Ch29 Galaxy Morphology | Image-feature classification with label-quality awareness | Ch19 classification, Ch21 feature ledger, Ch20 diagnostics, Ch25 trust | Strong image-quality and label-noise framing; good baseline-before-CNN logic | Replace evidence-card language; turn CNN upgrade into Model Choice / Trust Statement boundary |

---

## Repetition Risk

Part IV currently does not badly repeat Part III. It mostly uses algorithms inside cases.

Keep this rule:

```text
Part III explains how the algorithm works.
Part IV explains why this algorithm is appropriate, risky, or insufficient for this scientific case.
```

Any future Part IV edit that starts explaining regression, PCA, k-means, or CNNs from scratch should be moved to:

- an Algorithm Card sidebar reference;
- a notebook comment;
- Part V, if it is genuinely about deep learning.

---

## Notebook-Walkthrough Risk

Part IV mostly avoids becoming notebook instructions. It has a few phrases like "notebook 会..." or "配套 notebook..." but these usually support the case narrative rather than dominate it.

Keep the case-chapter structure centered on:

1. Scientific Question
2. Dataset Contract
3. Baseline
4. Model Choice
5. Model Experiment Record
6. Scientific Interpretation
7. Trust Statement
8. Extension to capstone

The notebook should remain the reproducibility artifact, not the chapter spine.

---

## Recommended Minimal Alignment Pass

Do not rewrite Part IV yet. First do a light interface alignment:

1. Update Part IV intro:
   - define Part IV case package as a Model Experiment Packet for a specific astronomy/physics case;
   - name Dataset Contract, Model Experiment Record, Algorithm Card sidebar links, evaluation/error-analysis artifacts, Trust Statement.

2. Update Part IV synthesis:
   - replace Project/Data/Baseline/Model/Evaluation/Interpretation/Integrity card language with the Part III frozen interface;
   - keep capstone as "later evidence packaging", not as the primary Part IV structure.

3. Update four chapter report-template closers:
   - Ch26: Gaia HR report -> Dataset Contract + Model Experiment Record + Trust Statement.
   - Ch27: photo-z report -> Model Experiment Record + residual artifact + Trust Statement.
   - Ch28: spectral report -> Dataset Contract + preprocessing evidence + Algorithm Card sidebar + Trust Statement.
   - Ch29: morphology report -> Dataset Contract + Feature Ledger / Model Experiment Record + review queue + Trust Statement.

4. Update `notebooks/part4_cases/README.md`:
   - notebook outputs should feed the same Part IV case package, not standalone case reports.

---

## Suggested Sample Chapters for Deep Rewrite

After the light alignment pass, choose two sample chapters:

1. Ch27 Photometric Redshift
   - best table/regression sample;
   - pressure-tests residual diagnostics, coverage, and Trust Statement.

2. Ch29 Galaxy Morphology
   - best image/classification sample;
   - pressure-tests label noise, human review, baseline-before-CNN, and Part V bridge.

These two are complementary and will reveal whether the Part III templates work for both tabular regression and image-like classification.

Ch26 is already a strong first-case chapter and may need only language alignment. Ch28 is also strong, but it may be better refined after Ch29 clarifies the image/deep-learning bridge.

---

## Freeze Feedback to Part III

Part IV does not currently expose a fatal Part III interface failure.

Minor feedback:

- Part III Algorithm Card depth needs the full / short / sidebar distinction now added in the freeze checklist.
- Part IV needs a standard case-package mapping, but that can live in Part IV intro/synthesis rather than forcing Part III changes.
- Trust Statement is useful for all four cases, but should be allowed to stay short; otherwise Part IV chapters will become too bureaucratic.

Conclusion: Part III V3 can remain frozen. Proceed to Part IV light alignment, then deep-rewrite Ch27 and Ch29 as sample chapters.
