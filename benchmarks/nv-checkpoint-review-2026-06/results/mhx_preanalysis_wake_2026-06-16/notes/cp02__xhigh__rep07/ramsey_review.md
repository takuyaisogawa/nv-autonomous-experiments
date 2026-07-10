# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior/local evidence: `evidence/e006.md`, `evidence/e007.json`, `evidence/e008.json`, `evidence/e009.json`, `evidence/e010.json`, `evidence/e011.json`, `evidence/e012.json`, and `evidence/e013.md`.
- New Ramsey terminal data/metadata: `measurement/m001.json` through `measurement/m005.json`.
- Primary raw data: `measurement/m001.json`, exported from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Run identity: `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`, `ramsey.xml`, completed safely with final count text `Final = 44.184 kcps`.
- Acquisition: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, 8 averages x 50000 repetitions, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Readout roles from saved `ramsey.xml`: `full_experiment = 0`, so readout 1 is the initial mS=0 reference and readout 2 is the post-Ramsey signal.

## Calculations or scripts run

- Parsed the JSON raw export and bridge metadata with local Python.
- Generated scratch artifacts: `ramsey_analysis_summary.json`, `ramsey_extra_checks.json`, and `ramsey_review_plot.png`.
- Checked raw signal, signal/reference, and signal/fitted-reference-line views.
- Checked snake scan ordering. Stored averages alternate forward/reverse tau order and are saved in tau order.
- Computed drift/common-mode summaries: per-average readout means vary strongly (`~30.5%` reference range, `~31.6%` signal range), while signal/reference average means vary much less (`~3.9%`). Largest within-average first/second acquisition-half changes were `5.8%` reference and `6.5%` signal.
- FFT sampling check: nominal resolution `1 / 8 us = 125 kHz`; `rfft` bin spacing with 41 samples is `121.95 kHz`; Nyquist is `2.5 MHz`.
- Model targets from local plan: carrier `1.0 MHz`; expected 13C sidebands near `0.6154 MHz` and `1.3846 MHz`; prior scout feature near `0.884 MHz`.
- Fixed-frequency least-squares checks with linear baseline:
  - Raw signal at `1.0 MHz`: amplitude `0.277 kcps`, `R2 = 0.024`, `p = 0.63`; median stored-average SEM of signal points is `1.92 kcps`.
  - Signal/reference at `1.0 MHz`: amplitude `0.0092`, `R2 = 0.050`, `p = 0.39`.
  - Signal/reference at expected 13C sidebands: `0.6154 MHz` amplitude `0.0111`, `p = 0.26`; `1.3846 MHz` amplitude `0.0084`, `p = 0.45`.
  - Signal/reference at prior `0.884 MHz`: amplitude `0.0074`, `p = 0.55`.
- Exploratory frequency scan:
  - Signal/reference has strongest component near `1.176-1.178 MHz`: amplitude `0.0225`, `R2 ~= 0.305`, `p ~= 0.0012`, per-average phase concentration `R ~= 0.91`, bootstrap amplitude CI about `0.014..0.032`.
  - Raw signal also has a component near `1.166-1.178 MHz`: amplitude about `0.88 kcps`, `R2 ~= 0.25`, `p ~= 0.005`, per-average phase concentration `R ~= 0.82`.
  - Bootstrap best-frequency percentiles in the `0.8..1.6 MHz` search were roughly `1.15..1.24 MHz` for both raw signal and signal/reference in the saved scratch check.
- Decay fits were not robust. At the exploratory `~1.178 MHz`, signal/reference fits gave `T2* ~= 2.37 us` when all points were included, but `~4.7..5.6 us` with large errors when early tau points were excluded. Raw-signal unconstrained fits collapsed to the lower T2 bound because the first tau point dominates.

## Plausible interpretation

- The Ramsey acquisition completed and the target remained bright enough; this is valid terminal data for r03.
- The expected programmed `1.0 MHz` carrier is not supported in raw signal or signal/reference.
- The planned 13C sideband positions near `0.615/1.385 MHz` are not supported.
- The prior non-claim-grade `~0.884 MHz` feature is also not supported as a dominant repeat feature.
- There is a plausible but still exploratory Ramsey-like component near `1.17..1.18 MHz`, seen in both raw signal and signal/reference with per-average phase concentration. If physical, it would suggest residual microwave detuning or a shifted effective Ramsey frequency rather than a clean on-center `det = 1.0 MHz` carrier.
- The substantial common-mode per-average count movement means this data set is useful diagnostically, but not clean enough to promote the shifted component into a final T2star or 13C result.

## Claims not yet supported

- No well-supported T2star value is established from this run.
- No nearby 13C conclusion is supported.
- The `1.17..1.18 MHz` component is not yet proven to be a physical Ramsey carrier rather than drift, readout/reference interaction, sequence timing, or analysis artifact.
- No claim is supported that the microwave center is known more accurately than the prior grid-supported fine-pODMR result.
- No coupling or sideband splitting can be extracted from this data.

## Recommended next action

Do not make a same-condition long Ramsey repeat or a T2star fit claim yet. First re-check the r03 microwave center with a quick fine weak-pi pODMR or an equivalent short center diagnostic. If the center has shifted by order `0.1..0.2 MHz`, update `mw_freq` and rerun Ramsey. If the center remains near `3.8759 GHz`, run a deliberately det-shifted Ramsey confirmation and require the `~1.17 MHz` feature to move with programmed det before treating it as a physical carrier; only then fit T2star and search for 13C sidebands separated by about `0.385 MHz`.
