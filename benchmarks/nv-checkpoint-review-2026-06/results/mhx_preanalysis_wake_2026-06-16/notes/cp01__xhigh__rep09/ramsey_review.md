# Ramsey Review: r03 first T2star/13C scout

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Ramsey data and metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final status, `measurement/m005.json` control.
- Prior support/model context: `evidence/e003.json` weak-pi pODMR review supporting `mw_freq = 3.876 GHz`; `evidence/e005.json` Ramsey model/advisory with expected `13C` Larmor near `0.385 MHz`.
- Generated local artifacts: `analysis_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analysis_ramsey.py`.
- Parsed the Ramsey scan as `full_experiment=0`: readout 1 is reference, readout 2 is Ramsey signal.
- Confirmed scan settings: `tau = 0..6 us`, 31 points, `dt = 0.2 us`, 4 averages x 50000 repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, Nyquist `2.5 MHz`.
- Computed raw signal, pointwise signal/reference, and signal over a fitted linear reference baseline.
- Performed linear-baseline plus sinusoid least-squares checks at the programmed carrier `1.5 MHz`, expected sidebands `1.115 MHz` and `1.885 MHz`, and a dense `0.15..2.45 MHz` frequency scan.
- Performed FFT checks on detrended views and per-average normalized checks.
- Checked scan-order first/last five acquired points for drift-like changes and tested endpoint sensitivity by dropping the first tau point.

## Plausible interpretation

- The Ramsey job completed normally and produced analyzable readouts, but it is not claim-grade for T2star or 13C.
- Raw combined readouts: reference mean `45.32 kcps` with `0.87 kcps` point scatter; signal mean `42.10 kcps` with `1.44 kcps` point scatter. The fitted reference baseline changes only `-0.68%` over the tau span, but post-run final counts were `38.249 kcps`, a `12.1%` drop from the fresh pre-Ramsey track count `43.535 kcps`.
- The programmed `1.5 MHz` Ramsey carrier is not visible in a supported way. In the signal/reference-line view, the fixed-`1.5 MHz` fit amplitude is only `0.00295` normalized units and reduces RSS by only about `0.4%` versus a linear baseline; raw-signal amplitude is only `0.133 kcps`.
- The largest combined frequency-scan feature is near `0.96 MHz` with amplitude `1.08 kcps` raw / `0.0238` normalized, but this is comparable to the residual scatter and is endpoint sensitive: dropping the first tau point moves the best feature to about `0.26 MHz`.
- Per-average best frequencies are not stable (`~0.94`, `0.54`, `0.21`, `0.84 MHz` in the normalized view), so the combined `0.96 MHz` feature is more plausibly noise/drift/outlier structure or at most a weak non-claim-grade Ramsey hint.
- Expected `13C` sidebands for `det = 1.5 MHz` and `f13C ~0.385 MHz` are near `1.115 MHz` and `1.885 MHz`. The nearest normalized FFT-bin amplitudes are small (`~0.0058` and `~0.0064`) and not dominant or per-average consistent.

## Claims not yet supported

- No numeric T2star value is supported by this Ramsey scout.
- No nearby `13C` coupling/presence claim is supported.
- A definitive no-`13C` conclusion is also not supported; the measurement quality is insufficient for exclusion.
- The `0.96 MHz` feature should not be claimed as a physical Ramsey carrier or resonance shift.
- The Ramsey result does not invalidate the prior pODMR-supported alignment of r03 by itself.

## Recommended next action

Do not fit or report T2star/13C from this run. First re-check r03 tracking/counts and the current weak-pi pODMR resonance near `3.876 GHz`, because the Ramsey run ended with a material count drop and no stable carrier. If the target is still bright and the resonance is confirmed or updated, repeat Ramsey with the corrected `mw_freq` and higher effective averaging while keeping per-average tracking windows inside the drift cap.
