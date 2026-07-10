# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Ramsey design/protocol context: `evidence/e005.json`; it records that `auto__ramsey` / `ramsey.xml` with `full_experiment=0` has readout 1 as the mS=0 reference and readout 2 as the Ramsey signal.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, plus `measurement/m002.json` job contract, `measurement/m003.json` completed bridge result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_metrics.json`, and `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed 31 tau points from 0 to 6 us, step 0.2 us, 4 averages x 50000 repetitions, `mw_freq=3.876 GHz`, `det=1.5 MHz`, `full_experiment=0`.
- FFT sampling checks: Nyquist `2.5 MHz`; DFT bin spacing from `rfftfreq` `161.3 kHz`; 1/span resolution `166.7 kHz`.
- Working field/13C scale from the local model: `B ~359 G`; expected 13C Larmor `~0.384 MHz`; expected det +/- 13C sidebands around `1.116 MHz` and `1.884 MHz`.
- Raw/readout checks: mean reference `45.32 kcps`, mean signal `42.10 kcps`, mean signal/reference `0.929`; per-average signal means `[43.36, 40.55, 42.80, 41.68] kcps`, showing common-mode variation.
- FFT checks after linear detrending:
  - Raw signal strongest bin: `0.968 MHz`; next strong bins include `0.161`, `1.613`, and `1.290 MHz`.
  - Signal/reference strongest bin: `0.968 MHz`; expected carrier-nearest bin `1.452 MHz` is weak.
  - Signal/reference-line view also has strongest bin `0.968 MHz`.
- Fit checks:
  - Fixed `1.5 MHz` fits are poor: fractional amplitude `0.3-0.6%`, `R2 ~0.01-0.03`.
  - Best empirical damped-cosine fits prefer `~0.94-0.96 MHz` and `T2* ~2.1-2.4 us`, but only with `R2 ~0.45-0.49` and broad/noisy residual context.
- Per-average FFT phase checks do not show a clean coherent carrier at the programmed `det` bin; sideband-near bins are not robust across raw and normalized views.

## Plausible interpretation

- The Ramsey run completed and contains real structure, but the strongest oscillatory component is near `0.97 MHz`, not the deliberately programmed `1.5 MHz` Ramsey carrier.
- A plausible physical explanation is residual microwave detuning or drift since the weak-pi pODMR grid point, shifting the apparent Ramsey beat by roughly `0.5 MHz`. This is compatible in scale with the prior center-uncertainty guard, but it is not proven by this dataset alone.
- The run also shows meaningful common-mode count variation across averages and a final bridge count of `38.249 kcps`, lower than the pre-Ramsey/weak-pODMR counts. That drift can contribute to low-frequency and normalization-sensitive FFT power.
- The empirical `~2 us` decay scale is useful as a planning hint, not a supported T2* result.

## Claims not yet supported

- No claim-grade T2* value is supported from this run. The only finite T2* estimate comes from an empirical fit whose preferred carrier is not the planned `det` and whose goodness of fit is modest.
- No nearby 13C claim is supported. The expected `det +/- 13C` sideband locations do not appear as a robust, raw/readout-consistent, per-average-coherent pattern; a sideband-like bin without a secure carrier is not sufficient.
- The observed `~0.97 MHz` feature should not yet be assigned to a specific physical transition, 13C coupling, or apparatus artifact.
- The accepted aligned r03 status from prior pODMR remains usable context, but this Ramsey dataset by itself does not complete the T2star/13C objective.

## Recommended next action

Do a targeted frequency check before spending time on a longer Ramsey: either a fresh narrow weak-pi pODMR around the 3.876 GHz working point or a short Ramsey frequency diagnostic designed to determine whether the current Ramsey carrier is offset by about `0.5 MHz`. Then repeat Ramsey with the updated center/detuning choice and a drift-aware acquisition split; only fit T2* and inspect 13C sidebands after the carrier is raw/readout-consistent and per-average coherent.
