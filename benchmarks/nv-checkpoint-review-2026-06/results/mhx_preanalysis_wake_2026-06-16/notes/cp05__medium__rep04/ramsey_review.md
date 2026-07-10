# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Measurement data/metadata: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` executed plan; `measurement/m003.json` terminal result; `measurement/m004.json` final bridge status; `measurement/m005.json` run control.
- Supporting local plan context checked through search: `evidence/e014.json` / `evidence/e017.json` for the intended refreshed-center Ramsey targets.

## Calculations or scripts run

- Wrote and ran `analyze_ramsey.py`.
- Outputs created: `ramsey_analysis_summary.json` and `ramsey_diagnostic.png`.
- Checks performed:
  - Parsed `ExperimentData` shape `(1, 2, 41)` and `ExperimentDataEachAvg` shape `(1, 20, 2, 41)`.
  - Used the local contract that readout 1 is reference and readout 2 is Ramsey signal.
  - Verified run settings: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us`, `0.2 us` step, `41` points, `20 x 50000` shots.
  - Checked terminal status: completed, no bridge error, no stop request, safe shutdown OK.
  - Ran robust common-mode drift screen across averages under snake order: no average exceeded `abs(robust_z)>3.5`; first-half common-mode mean was `47.90 kcps`, second-half `45.56 kcps`.
  - Compared raw signal, point-wise signal/reference, and fitted-reference-line-normalized signal.
  - Ran least-squares sinusoid screens and FFT screens over `0.1..2.45 MHz`, with full span and skip-first-4-tau views.
  - Checked target amplitudes at carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior det-shift targets, and per-average coherent sine/cos coefficients.

## Quantitative findings

- Raw levels: reference mean `48.79 kcps`, signal mean `44.67 kcps`; raw signal range `40.57..46.84 kcps`; median signal SEM across stored averages `0.85 kcps`; median ratio SEM `0.0116`.
- Combined least-squares screen:
  - Raw/fitted-reference views have the largest full-span component near `2.271 MHz` with amplitude about `0.818 kcps`; skip-first-4 remains near `2.271 MHz` with amplitude about `0.555 kcps`.
  - Point-wise ratio screen has the largest full-span component near `2.270 MHz` with amplitude `0.01845`; skip-first-4 remains near `2.266 MHz` with amplitude `0.01418`.
  - The programmed carrier is present but not dominant: ratio amplitude `0.01575` full / `0.01231` skip-first-4; raw amplitude `0.705 kcps` full / `0.512 kcps` skip-first-4.
  - Expected 13C sideband amplitudes are weaker: ratio low sideband `0.00278` full / `0.00067` skip; ratio high sideband `0.00962` full / `0.00527` skip.
- FFT sanity check is more carrier-favorable than the LS screen: ratio FFT full/skip peaks are around `1.50..1.52 MHz`, but `2.26..2.29 MHz` remains close in the full-span view.
- Per-average frequency screens are scattered. In the 20 stored averages, ratio top frequencies cluster only weakly: 4/20 within `0.15 MHz` of the `1.5 MHz` carrier, 4/20 within `0.15 MHz` of the new `2.27 MHz` top, and only 1/20 near each expected 13C sideband.
- Coherent per-average coefficient bootstrap supports a modest carrier component: ratio carrier mean-vector amplitude `0.0161` with bootstrap 95% interval `0.0119..0.0211`; raw carrier amplitude `0.705 kcps` with bootstrap 95% interval `0.564..0.869 kcps`. The low 13C sideband is consistent with near-zero in ratio (`0.00285`, bootstrap `0.00078..0.00833`), and the high sideband is weaker than the carrier (`0.00942`, bootstrap `0.00429..0.01514`).
- A free descriptive damped-cosine fit locks to the unexplained `~2.27 MHz` component, not the programmed carrier, with non-claim-grade fit quality (`ratio` full-span `T2* ~2.56 us`, `R2 ~0.56`; raw full-span `T2* ~1.80 us`, `R2 ~0.65`). This is not a supported T2star estimate.

## Plausible interpretation

- The refreshed-center high-shot run is analyzable and healthier than a pure null: it contains a coherent, modest `1.5 MHz` carrier-like component in the averaged data.
- The data still do not show a clean, dominant Ramsey carrier plus decay envelope. The strongest LS component near `2.27 MHz` is not the programmed detuning, not an expected 13C sideband, and not established as physical.
- The prior fixed `~1.192 MHz` artifact-control feature is weak here, so this run does not simply repeat the earlier artifact-like behavior.
- The expected 13C sideband pattern is not present at claim grade. The low sideband is very weak, and the high sideband is at most a secondary component without per-average support.

## Claims not yet supported

- No well-supported numeric `T2*` should be claimed from this dataset.
- No nearby `13C` coupling conclusion should be claimed from this dataset.
- Do not claim the `~2.27 MHz` feature as a physical Ramsey frequency without a deliberate detuning/alias/control test.
- Do not claim sub-grid microwave resonance precision beyond the refreshed pODMR context already in the project state.

## Recommended next action

Stop accumulating blind long Ramsey repeats on r03. If continuing experimentally, run a targeted control that can distinguish a true detuning-following Ramsey carrier from the unexplained high-frequency component: for example, a refreshed-center det-shift/phase-cycled Ramsey with finer tau sampling and the same raw/readout-aware review gates. If that still fails to produce a clean carrier/sideband model, record r03 as aligned but unsupported for quantitative T2star and nearby-13C under the present conditions, then switch to an alternate protocol or candidate strategy.
