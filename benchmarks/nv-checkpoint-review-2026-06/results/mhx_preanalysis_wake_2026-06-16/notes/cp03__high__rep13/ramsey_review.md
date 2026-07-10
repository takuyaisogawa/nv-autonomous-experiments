# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior/bridge evidence: `evidence/e001.json` through `evidence/e017.md`, especially the prior det=1.0 MHz 8 us Ramsey terminal review summary and the short-tau design/start note.
- New measurement data:
  - `measurement/m001.json`: terminal raw export from `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: job spec for `nv23_ramsey_20260513_230331_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: control file, no stop requested.

## Calculations or scripts run

- Created and ran `analyze_shorttau_ramsey.py`.
- Outputs:
  - `ramsey_shorttau_analysis.json`
  - `ramsey_shorttau_analysis.png`
- Checks performed:
  - Confirmed `ramsey.xml` with `full_experiment=0`: readout 1 is the true mS=0 reference, readout 2 is the Ramsey signal.
  - Reconstructed tau grid: 0.048 to 1.968 us, 48 ns step, 41 points.
  - Checked raw signal/reference ranges and SEM across 12 stored averages.
  - Computed least-squares sin/cos amplitudes with a linear baseline at 0.615, 1.000, 1.178, and 1.385 MHz for raw signal, point-wise ratio, fitted-reference-line ratio, and raw reference.
  - Screened 0.5 to 3 MHz by least-squares amplitude.
  - Ran FFT after linear detrending; FFT bin spacing is 0.508 MHz, so FFT is only a coarse screen.
  - Ran an approximate snake-order intra-average drift check using the recorded acquisition order.

## Quantitative results

- Measurement completed cleanly: 12 averages x 90000 repetitions, final counts 35.122 kcps, no bridge error, no stop request, safe shutdown ok.
- Raw readout scale:
  - Reference range: 2.176 kcps.
  - Signal range: 6.499 kcps.
  - Signal mean: 44.655 kcps.
  - Reference mean: 48.573 kcps.
  - Median signal SEM across stored averages: 1.138 kcps.
- Approximate snake-order drift check:
  - No average exceeded the 0.15 linear end-drop flag threshold.
  - There is still large between-average common-mode brightness variation, so normalization remains provenance rather than a signal-presence criterion.
- Least-squares amplitudes with linear baseline:
  - At programmed 1.000 MHz carrier: raw signal amp 1.282 kcps; fitted-reference-line ratio amp 0.0264; raw-signal R2 0.455.
  - At the prior recurring 1.178 MHz feature: raw signal amp 1.678 kcps; fitted-reference-line ratio amp 0.0345; raw-signal R2 0.720.
  - 0.5 to 3 MHz LS screen peaks near 1.204 MHz in raw signal and fitted-reference-line ratio.
  - Reference readout amplitudes at these frequencies are small by comparison, e.g. 0.187 kcps at 1.178 MHz.
- 13C sideband target checks:
  - Expected sideband positions from local project context are about 0.615 and 1.385 MHz for det=1.0 MHz.
  - Their fitted amplitudes are not cleanly separated from the carrier/near-1.2 MHz structure over this short window.
  - The 1.92 us span gives only about 0.508 MHz FFT bin spacing, so this dataset is not a high-resolution 13C sideband measurement.

## Plausible interpretation

- The short-tau/high-SNR Ramsey diagnostic is analyzable and does show signal-readout structure larger than the reference variation and larger than the median per-point SEM.
- The result is more suggestive of a real Ramsey-like early-time response than the previous 8 us det=1.0 MHz dataset, but it still does not produce a clean programmed-carrier model.
- The strongest constrained component is again near 1.18 to 1.20 MHz, matching the prior non-claim-grade 8 us screen's largest feature more than the programmed 1.0 MHz carrier. Plausible explanations include actual resonance offset/drift relative to the fine pODMR center, sequence/instrument phase behavior, or analysis/baseline coupling over the short window.
- Because the short window and baseline curvature make damped-cosine fits model-dependent, a numeric T2star should not be promoted from this dataset.

## Claims not yet supported

- No supported numeric T2star value.
- No supported nearby-13C coupling/splitting conclusion.
- No claim that the 1.18 to 1.20 MHz feature is definitely physical; it is recurring and signal-dominant, but not yet tied to a det-following carrier model.
- No claim that the programmed 1.0 MHz carrier is absent; it is present in constrained LS fits but weaker than the near-1.2 MHz component and not independently resolved as the dominant model.
- No claim that the weak-pi pODMR center is wrong by a specific amount; Ramsey evidence alone does not fix the sign or mechanism.

## Recommended next action

Do not run another blind long-window Ramsey repeat on r03. Run a targeted detuning/frequency sanity diagnostic that can distinguish whether the recurring near-1.2 MHz component follows the programmed Ramsey detuning, reflects a microwave resonance offset, or is a fixed apparatus/baseline artifact. A practical next branch is immediate fine weak-pi pODMR sanity around 3.8759 GHz plus a compact short-tau Ramsey det-dependence check; only fit T2star after a raw/readout-aware det-following carrier is established. Defer 13C claims to a later longer/high-quality Ramsey or echo/DD measurement after the carrier model is clean.
