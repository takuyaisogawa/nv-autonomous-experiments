# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective, prior r03 alignment/pODMR/Ramsey context, and current analysis plan.
- `md/memory.md`, `md/knowledge.md`: local NV analysis conventions, especially raw/readout-aware review and fit-after-signal-presence rule.
- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted job spec for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control evidence.

## Calculations or scripts run

- Added and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_diagnostic.png`.
- Verified raw-export axis contract: `ExperimentDataEachAvg` shape `[1,20,2,41]`; averaging axis 1 reproduces `ExperimentData` with max difference `1.42e-14`.
- Confirmed measurement settings: `tau = 0.048..8.048 us`, step `0.200 us`, 41 points, `20 x 50000` shots per tau, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, final counts `43.433 kcps`.
- Screened raw signal, point-wise ratio, and fitted-reference normalization with least-squares sinusoid amplitudes over 0.125..2.45 MHz, including full data and skip-first-4-tau views.
- Checked target frequencies: carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, old artifact-control `1.192 MHz`, and prior det-shift top `1.623 MHz`.

## Plausible interpretation

- The run completed normally and is analyzable; there is no stop request or bridge error in the local terminal/status files.
- The raw signal varies over `40.57..46.84 kcps` with point-to-point range `6.27 kcps`, but the median per-point SEM across stored averages is `0.85 kcps`, so apparent oscillatory components need consistency checks.
- The strongest combined frequency screen is near `2.27 MHz` in raw signal, point-wise ratio, and fitted-reference normalization, and remains near that value after skipping the first 4 tau points. This is not the programmed carrier or expected 13C sideband structure.
- The programmed `1.5 MHz` carrier is present only weakly: raw LS amplitude `0.690 kcps`, point-wise ratio amplitude `0.0154`, fitted-reference-normalized amplitude `0.0142`. These are comparable to the median uncertainties (`0.85 kcps` raw SEM and `0.0116` ratio SEM), so this does not establish a clean Ramsey carrier.
- Expected 13C sidebands are weaker/inconsistent: ratio amplitudes are about `0.00234` at `1.115 MHz` and `0.00960` at `1.885 MHz`; raw amplitudes are `0.125 kcps` and `0.260 kcps`, below the raw SEM scale.
- Per-average ratio frequency screens are widely scattered (`IQR 0.813..2.069 MHz`; median `1.555 MHz`), so the combined spectral peak is not a stable average-by-average feature.
- This result is consistent with another analyzable but non-claim-grade Ramsey dataset on r03: useful negative/diagnostic evidence, not a supported T2star or 13C measurement.

## Claims not yet supported

- A numerical T2star for r03 is not supported from this Ramsey run.
- A nearby 13C conclusion is not supported; the expected `1.115/1.885 MHz` sidebands are not clean, dominant, or repeatable.
- The `2.27 MHz` screen maximum should not be promoted as a physical coupling or detuning without an independent protocol/frequency-shift check.
- The weak `1.5 MHz` component should not be fit for a decay constant as a physical Ramsey envelope because signal presence is not yet established above noise and baseline structure.

## Recommended next action

Avoid another blind long Ramsey repeat on the same conditions. The best next action is to switch to an alternate, more discriminating protocol for the aligned r03 NV, such as a Hahn/CPMG baseline (`auto__cpmg` with `N = 1` for echo-like T2 baseline, after normal manifest/protocol checks) or a deliberately targeted phase/readout diagnostic that can separate carrier tracking from transient/baseline artifacts. If the project goal must close on Ramsey only, record the current supported conclusion as: aligned r03 found, but T2star and 13C remain unsupported under the tested Ramsey conditions.
