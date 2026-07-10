# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `context.json`.
- Prior/follow-up evidence: `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md`, plus the fine-pODMR and second-Ramsey job/advisory artifacts in `evidence/`.
- New Ramsey measurement: `measurement/m001.json` raw export and `measurement/m002.json` through `measurement/m005.json` job/result/status/control artifacts.
- Scratch outputs created here: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.

## Calculations or scripts run

- Loaded `measurement/m001.json` with Python and extracted `ExperimentData`, `ExperimentDataEachAvg`, errors, scan variables, and `ScanOrderInfo`.
- Checked the saved `ramsey.xml` text in the raw export: with `full_experiment=0`, readout 1 is the pre-Ramsey mS=0 reference and readout 2 is the Ramsey signal.
- Computed raw reference/signal statistics, signal/reference, and signal divided by a fitted linear reference baseline.
- Ran a simple per-average common-mode drift check using the combined readout mean vs median under the recorded snake scan order.
- Ran detrended Hann-window FFT checks and fixed-frequency least-squares sinusoid fits at:
  - programmed carrier: `1.000 MHz`
  - planned 13C sidebands: `0.615423 MHz` and `1.384577 MHz`
  - prior scout feature: `0.884 MHz`
- Ran a single-frequency least-squares grid search and descriptive decaying-cosine fits, including per-average and bootstrap sanity checks.
- Checked whether a free-carrier interpretation near `0.462 MHz` has a stable companion line separated by the expected `~0.3846 MHz` 13C Larmor splitting.

## Plausible interpretation

- The second Ramsey job completed safely: `tau=0..8 us`, 41 points, `dt=0.2 us`, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `8 x 50000` repetitions, final counts `44.184 kcps`, tracking per average.
- The raw Ramsey signal is analyzable and shows a real-looking contrast scale: signal mean `44.58 kcps`, raw range `7.72 kcps`, and the `tau=0` signal is `12.3%` below the later median. The reference mean is `49.31 kcps` with a `4.29 kcps` range.
- Drift/count provenance is mixed: average 7 is low by `18.4%` in common-mode combined readout vs the per-average median. This is not by itself a hard invalidation, but it weakens per-average repeatability.
- The planned `1.0 MHz` Ramsey carrier is not supported by fixed-frequency raw fits: amplitude `0.277 kcps`, incremental R2 `0.024`, descriptive p `0.63`. Reference-normalized fits are also weak at `1.0 MHz`.
- Planned 13C sidebands are not supported: raw fixed-frequency fits give `0.475 kcps`, incremental R2 `0.069`, p `0.27` at `0.615 MHz`, and `0.263 kcps`, incremental R2 `0.022`, p `0.66` at `1.385 MHz`.
- The prior `0.884 MHz` feature is not reproduced as a strong fixed component in this run: raw amplitude `0.286 kcps`, incremental R2 `0.026`, p `0.61`.
- A descriptive free-frequency view finds the strongest raw single-frequency component near `0.466 MHz` with amplitude `0.915 kcps`, incremental R2 `0.261`, p `0.0037`. A free decaying-cosine fit gives about `f=0.462 +/- 0.040 MHz` and `T~1.66 +/- 0.56 us` with R2 `0.56`.
- That `~0.46 MHz` component could plausibly be Ramsey-like, and it could be related to the prior non-claim-grade `~0.884 MHz` scout if the programmed det and a residual frequency offset combine in the sequence. The implied offsets are roughly `1.0-0.462 = 0.538 MHz` and `1.5-0.884 = 0.616 MHz`, comparable at this resolution.
- The same interpretation is not yet claim-grade: per-average free fits are broad/bimodal, one average has a common-mode drop, and the strongest normalized/reference views do not give a clean matching carrier.

## Claims not yet supported

- No well-supported T2star value should be claimed from this run. The descriptive `~1.7 us` envelope is useful for planning, not a final T2star.
- No nearby 13C coupling claim is supported. Neither the planned `det +/- f13C` sidebands nor a companion line around the tentative `~0.46 MHz` carrier are stable enough.
- Do not claim that the programmed `1.0 MHz` carrier was observed.
- Do not claim a precise resonance offset from the `~0.46 MHz` component without a det-dependence diagnostic.
- Do not treat normalization-only peaks as physical Ramsey evidence.

## Recommended next action

Do not simply add more shots to the same Ramsey setting. First run a compact Ramsey phase-response/protocol diagnostic on accepted r03, or inspect the generated pulse/phase semantics if that is available locally: keep the same `mw_freq=3.8759 GHz` and test whether the observed carrier moves linearly with programmed `det` using a short controlled set such as det `0`, `0.5`, `1.0`, and `1.5 MHz`. If the carrier shift is confirmed, retune or model the residual offset and then run a claim-grade T2star/13C Ramsey. If it is not confirmed, treat the present oscillatory structure as sequence/timing/reference/artifact risk and debug the Ramsey route before further T2star claims.
