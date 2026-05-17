# Dirty / PSF Convention Parity Audit

Status: blocker memo.

Current conclusion: the residual-floor issue should not be debugged at the
TopN, GraphBatch, component-budget, or deeper-sweep layer yet. The discrepancy
is already present before CLEAN selection begins.

## Blocking Evidence

The 4K audit shows that FP-CLEAN and WSClean are not producing the same
zero-model imaging product under nominally identical image geometry:

- FP-CLEAN dirty RMS / WSClean dirty RMS: about 15.19x
- FP-CLEAN normalized PSF RMS / WSClean normalized PSF RMS: about 15.49x
- FP-CLEAN beam area / WSClean beam area: about 21.77x
- Dirty / PSF correlation: about 0.086 / 0.090
- Dirty peak offset: about -4 / +3 px
- WSClean beam: about 35.11 x 24.36 px
- FP-CLEAN beam: about 196 x 95 px

This is not a residual-depth or component-selection problem. It indicates that
the dirty image, PSF, beam, weighting, coordinate convention, row selection, or
normalization convention differs before minor-cycle behavior can be meaningfully
compared.

## Pause Until Parity Improves

Pause these directions:

- TopN selection debug
- GraphBatch conflict graph debug
- deeper component sweeps
- larger component budgets
- 8K / 16K scaling gates
- performance optimization

Any CLEAN strategy comparison is currently contaminated because the two systems
are not cleaning the same effective dirty/PSF product.

## New Phase

Recommended phase name:

**Phase B2: Dirty-PSF Convention Parity Audit**

Goal:

Explain why FP-CLEAN and WSClean dirty / PSF / beam products differ so strongly
before CLEAN selection begins.

## Priority Checks

### 1. Effective UV Coverage / Row Selection

First suspicion: FP-CLEAN is using a different effective UV coverage, losing
high-UV rows, downweighting them, or selecting different rows/channels/pols.

Compare WSClean input rows and FP-CLEAN actually used rows:

- total rows
- used rows
- flagged rows
- nonzero-weight rows
- sum weights
- sum weight squared
- u_lambda min / max / p50 / p95 / p99
- v_lambda min / max / p50 / p95 / p99
- uv_radius_lambda min / max / p50 / p95 / p99
- per-channel row counts
- per-pol row counts
- per-w-bin row counts
- radial weight profile: uv_radius bin -> sum imaging weight

Key test:

If FP-CLEAN uv_radius max or p99 is much smaller than WSClean, the broader beam
is immediately explained.

### 2. Cell Size / UV-to-Pixel Mapping

Verify:

- `cell_rad = 9 arcsec` converted to radians
- phase term uses `2*pi*u*l + 2*pi*v*m`
- `l = pixel_offset * cell_rad`
- x/y sign conventions
- RA-axis flip
- u/v swap
- center index uses `N/2` versus `(N-1)/2`
- phase-center reference pixel

Run synthetic point-source tests:

- point source at phase center
- point source at +10 px x
- point source at +10 px y
- point source at arbitrary off-center position

Record expected peak, actual peak, x/y sign, and pixel offset.

### 3. Weighting Convention

Compare:

- raw WEIGHT / SIGMA usage
- flag handling
- natural / uniform / Briggs settings
- UV density correction
- taper status
- imaging weight sum
- gridding weight sum
- normalization by sum weights
- normalization by PSF peak

Export radial weight profiles for both systems.

### 4. PSF Normalization

Check:

- PSF peak value
- PSF peak position
- PSF center value
- PSF sum
- PSF abs sum
- PSF L2 norm
- PSF RMS
- direct half-maximum width
- second-moment width
- Gaussian-fit width
- central x/y cuts
- radial profile

If PSF peak is not centered, coordinate / gridding origin comes before beam fit
debugging.

### 5. Beam Fit Convention

Do not rely only on fitted beam. Compare direct PSF width diagnostics:

- horizontal cut
- vertical cut
- radial profile
- direct half-maximum width
- second-moment width
- Gaussian fit

If all direct measures show FP-CLEAN is wider, the beam fitter is not the main
problem.

### 6. DFFT Window / Analysis-Basis Normalization

FP-CLEAN-specific risks:

- facet window correction differs between dirty and PSF
- analysis/native basis mismatch
- divide-by-n map applied to one product but not the other
- facet interior / halo / trust-region normalization differs
- support-response normalization applied in the wrong direction

Internal consistency tests:

- `dirty_from_vis`
- `psf_from_unit_weights`
- `response_from_unit_delta`
- `major_refresh_response`

These should agree in normalization and coordinate basis before comparing to
WSClean.

### 7. Internal vs Exported Product

Compare:

- internal dirty / residual stats
- exported dirty / residual stats
- reloaded FITS/image stats

If internal and exported differ, the issue is export/restoration units. If
internal already differs from WSClean, the issue is the imaging operator.

## Minimal Experiment Matrix

### Experiment A: Zero-Model Dirty Operator Audit

Same MS, image size, cell, channel/pol/flag selection, and weighting as closely
as possible.

Output:

- FP dirty
- FP PSF
- WSClean dirty
- WSClean PSF
- row and weight summaries
- UV-radius profile
- dirty stats
- PSF stats
- beam widths by multiple methods
- peak positions
- correlation
- scale-fit residual

### Experiment B: Single-Row / Small-Row Synthetic Audit

Use:

- one row
- two symmetric rows
- small UV ring
- small UV patch

Purpose:

Locate u/v sign, phase convention, pixel origin, and lambda scaling errors.

### Experiment C: Same-Row Same-Weight Internal PSF Audit

Inside FP-CLEAN only:

- same selected rows
- same weights
- dirty = A^H W y
- PSF = A^H W A delta

Check:

- PSF peak at center
- dirty peak alignment
- response center alignment
- one-component closure

### Experiment D: WSClean Simple-Weight Compatibility

Run WSClean with the simplest comparable settings:

- natural weighting
- no taper
- no multiscale
- no automask
- no primary-beam correction
- no joined channels
- same image size
- same cell size

Run FP-CLEAN with matching simple weights. The target is dirty/PSF parity, not
CLEAN parity.

## Current Root-Cause Ranking

High probability:

1. Effective UV coverage / row selection / high-UV rows lost or downweighted
2. `uv_lambda` scaling or cell-radian mapping error
3. Weighting convention mismatch
4. DFFT window / analysis-basis normalization mismatch

Medium probability:

5. Beam-fitting method mismatch
6. Phase-center / reference-pixel convention offset
7. Support graph / response support affecting PSF

Low priority for now:

8. TopN candidate selection
9. GraphBatch conflict graph
10. Component budget

## Working Statement

The 4K residual-floor audit shows that the FP-CLEAN residual-floor excess is not
primarily caused by TopN/GraphBatch selection or insufficient component depth.
The discrepancy is already present at the zero-model dirty and normalized PSF
level. FP-CLEAN and WSClean currently produce substantially different dirty,
PSF, and beam products under nominally identical 4K, 9 arcsec image geometry.
The next blocker is therefore imaging / normalization / beam / PSF convention
parity, not GraphBatch scheduling.

