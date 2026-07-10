# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- New Ramsey run: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job plan, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Planning/context cross-checks: `evidence/e007.json`, `evidence/e008.json`, `evidence/e009.json`, `evidence/e010.json`, `evidence/e013.md`.

## Calculations/scripts run

- Ran JSON/schema inspection with local Python and `rg`.
- Created and ran `scratch_ramsey_analysis.py`.
- Outputs: `ramsey_analysis_results.json` and `ramsey_analysis.png`.
- Analysis used local readout-role context: for `ramsey.xml` with `full_experiment=0`, readout 1 is the mS=0 reference and readout 2 is the Ramsey signal.

Key quantitative checks:

- Run completed cleanly: job `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940`, final counts `44.184 kcps`, 8 averages x 50000 repetitions.
- Scan: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, FFT bin spacing from sampled trace `121.95 kHz`, Nyquist `2.5 MHz`, programmed `det = 1.0 MHz`.
- Raw combined trace: reference mean `49.31 kcps`; signal mean `44.58 kcps`; signal peak-to-peak `7.72 kcps`. Point-wise signal/reference peak-to-peak after median normalization was `18.7%`; fitted-reference-line signal normalization peak-to-peak was `17.0%`.
- Drift/provenance check: average 7 common-mode mean was `18.4%` below the per-average median and was the only `>15%` drop flag. Other averages were not drop-flagged. Snake-order first/second-half common-mode shifts were at most about `5.6%`.
- Least-squares sinusoid checks on fitted-reference-line-normalized signal:
  - Expected carrier `1.000 MHz`: amplitude `0.00624`, `R2 = 0.0287`.
  - Expected low 13C sideband `0.615423 MHz`: amplitude `0.01073`, `R2 = 0.0730`.
  - Expected high 13C sideband `1.384577 MHz`: amplitude `0.00595`, `R2 = 0.0266`.
  - Prior scout component `0.884 MHz`: amplitude `0.00648`, `R2 = 0.0308`.
  - Best all-average exploratory sine frequency was `0.466 MHz` with amplitude `0.02063`, `R2 = 0.264`, not a planned carrier or sideband.
- FFT top bins for fitted-reference-line-normalized signal were near `1.220`, `1.098`, `0.488`, `0.122`, and `0.610 MHz`; this is not clean carrier-locked evidence.
- Removing the flagged average 7 did not rescue the carrier: `1.000 MHz` amplitude fell to `0.00417`, `R2 = 0.0182`; best exploratory frequency remained about `0.467 MHz`.
- Per-average carrier phase coherence at `1.0 MHz` was weak (`|mean phasor| = 0.45`), and per-average best frequencies were scattered, so average consistency does not support a claim.

## Plausible interpretation

The measurement is usable as diagnostic evidence and the NV remained bright at the terminal level, but the Ramsey spectral content is still non-claim-grade. The combined traces contain oscillatory structure, yet the programmed `1.0 MHz` Ramsey carrier is weak in least-squares fits, the expected `13C` sidebands are not robust, the strongest exploratory components are model-inconsistent, and stored averages disagree. The det-shift follow-up therefore does not convert the prior `~0.884 MHz` scout feature into a supported physical carrier or sideband, and it also does not establish a clean programmed-det carrier response.

Average 7's common-mode drop is provenance that further weakens confidence, but it is not the sole reason for rejection: excluding it leaves the same non-claim-grade conclusion.

## Claims not yet supported

- No supported numeric `T2*` value from this Ramsey run.
- No supported nearby `13C` conclusion from FFT or sideband fits.
- No supported claim that the prior `~0.884 MHz` feature is physical.
- No supported claim that the second Ramsey has a clean carrier at the programmed `1.0 MHz`.
- No sub-grid resonance-frequency precision beyond the prior fine-pODMR grid-supported `3.8759 GHz` input.

## Recommended next action

Do not blindly repeat the same Ramsey measurement or fit `T2*` from this run. Next, run a targeted Ramsey carrier diagnostic after a fresh tracking/count sanity check, ideally with deliberately chosen detunings whose carrier should shift predictably while keeping the tau span and Nyquist guard adequate. Only return to a longer/higher-SNR T2*/13C acquisition after the Ramsey route shows a coherent carrier response in raw/readout-aware data.
