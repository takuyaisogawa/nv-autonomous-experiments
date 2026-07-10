# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective and current r03 context.
- `evidence/e003.json`: prior weak-pi pODMR review supporting the r03 grid resonance at `3.876 GHz`.
- `evidence/e005.json`: Ramsey protocol/model/advisory record.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: Ramsey job spec, terminal result, status, and control.
- Generated locally: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_stdout.txt`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py` using only local JSON files.
- Confirmed `ramsey.xml` with `full_experiment=0`: readout 1 is the 0-level reference and readout 2 is the Ramsey signal.
- Ramsey grid: `tau = 0..6 us`, 31 points, `dt = 200 ns`, `4 x 50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, final counts `38.249 kcps`.
- Sampling checks: discrete FFT bin spacing `161.3 kHz` (`1/(31*dt)`), nominal span reciprocal `166.7 kHz`, Nyquist `2.5 MHz`.
- Working field/13C scale from the project model: `B ~= 359.3 G`, `13C Larmor ~= 384.6 kHz`; expected Ramsey sidebands for `det=1.5 MHz` are `1.115 MHz` and `1.885 MHz`.
- Raw/readout stats: reference mean `45.32 kcps`, signal mean `42.10 kcps`, signal/reference mean `0.929`; median pointwise SEM across stored averages is `1.01 kcps` for signal and `0.0256` for signal/reference.
- Ramsey scan-order drift check: no stored average exceeded a 15% common-mode drop; largest linear drop was about `3.5%`.
- FFT and least-squares sinusoid checks:
  - Strongest detrended signal/reference FFT peak is at `0.968 MHz`.
  - Sinusoid at `0.968 MHz`: normalized amplitude `0.0244 +/- 0.0077`, raw-signal amplitude `1.08 +/- 0.32 kcps`; improves AIC versus linear baseline by about `5.7` to `6.6`.
  - Programmed `1.5 MHz` check: normalized amplitude `0.0058 +/- 0.0088`; AIC is worse than a linear baseline.
  - Expected 13C sidebands: normalized amplitudes `0.0079 +/- 0.0089` at `1.115 MHz` and `0.0118 +/- 0.0087` at `1.885 MHz`; nearest upper FFT bin at `1.935 MHz` is only `0.0135 +/- 0.0087`.

## Plausible interpretation

The Ramsey scout completed cleanly and the target did not suffer a hard count collapse, but the trace is non-claim-grade. There is weak oscillatory structure, with the largest simple-sinusoid/FFT component near `0.97 MHz`, not at the programmed `1.5 MHz` carrier. That could be residual resonance detuning, a time-zero/systematic feature, or finite-window noise. The expected 13C sideband-scale features are comparable to other peaks and are not strong enough to assign physically.

## Claims that are not yet supported

- No supported numeric `T2*` value from this run.
- No supported nearby `13C` conclusion from this run.
- No supported claim that the `0.97 MHz` component is a real Ramsey carrier rather than residual detuning/artifact/noise.
- No supported rejection of r03 as the aligned candidate; the prior pODMR evidence still supports r03, but this Ramsey scout is inconclusive for T2*/13C.
- No supported absence claim for nearby 13C; the data quality is insufficient to prove absence.

## Recommended next action

Do not fit or report T2*/13C from this dataset. Before a longer T2* run, run a targeted frequency diagnostic: preferably a fresh/finer weak-pi pODMR around `3.876 GHz` or a short Ramsey detuning check, because this scout's strongest component is displaced from the planned carrier. Then repeat Ramsey with a design that keeps per-average tracking windows bounded, uses more independent averages if feasible, and places the carrier/expected `~0.385 MHz` sidebands cleanly inside the FFT band.
