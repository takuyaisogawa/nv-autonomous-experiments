# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`, plus `md/memory.md` and `md/knowledge.md` for local project rules.
- New completed Ramsey run:
  - Raw export: `measurement/m001.json`
  - Job/result/status/control metadata: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`
- Prior comparison data:
  - Previous det=1.0 MHz short-tau raw export: `evidence/e006.json`
  - Previous terminal review and det-shift plan: `evidence/e008.json`, `evidence/e019.json`, `evidence/e021.json`
  - Prior drift review for the det=1.0 MHz run: `evidence/e007.json`

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Output files:
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_analysis.png`
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract by confirming per-average means reconstruct `ExperimentData`; shape is `[1, 12, 2, 41]`.
  - Confirmed new run metadata: `nv23_ramsey_20260514_015423_auto_ramsey`, completed, final counts `44.796 kcps`, `mw_freq=3.8759 GHz`, `det=1.5 MHz`, `tau=48 ns..1.968 us`, 41 points, `12 x 90000` shots.
  - Computed raw signal/reference, point-wise signal/reference ratio, signal over fitted reference line, per-point SEM, simple scan-order drift, detrended FFT amplitudes, and linear-baseline-plus-sinusoid least-squares screens.
  - Compared target frequencies:
    - Programmed carrier: `1.500 MHz`
    - Programmed 13C sidebands: `1.115` and `1.885 MHz`
    - Prior top shifted by +0.5 MHz: `1.692 MHz`
    - Shifted sidebands: `1.307` and `2.077 MHz`
    - Prior artifact-control frequency: `1.192 MHz`

## Quantitative results

- New run quality:
  - Total shots per tau point: `1.08e6`
  - Median signal SEM: `0.711 kcps`
  - Median ratio SEM: `0.0126`
  - Simple snake-order drift check flagged no averages.
  - Nominal frequency resolution from the 1.92 us span is coarse: about `0.521 MHz`; FFT bin spacing is also about `0.508 MHz`.
- New ratio-view LS screen:
  - Empirical top: `1.623 MHz`, ratio amplitude `0.02547`, R2 improvement `0.430`.
  - Programmed `1.500 MHz`: ratio amplitude `0.02399`, R2 improvement `0.359`.
  - Predicted det-tracking `1.692 MHz`: ratio amplitude `0.02505`, R2 improvement `0.411`.
  - Prior artifact-control `1.192 MHz`: ratio amplitude `0.00511`, R2 improvement `0.0167`.
- Raw signal view is less clean:
  - Its strongest LS screen is near `0.882 MHz`, not the ratio-view `1.623 MHz`.
  - At the ratio-view empirical top, raw signal amplitude is `1.25 kcps`, comparable to but not clearly dominant over other target checks.
- 13C sideband checks are weak:
  - Programmed low/high sideband ratio amplitudes: `0.0108` and `0.0173`.
  - Det-tracking low/high sideband ratio amplitudes: `0.00953` and `0.00614`.
  - None are dominant in raw/readout-aware views.

## Plausible interpretation

The new det=1.5 MHz run is terminal and analyzable. It weakens the fixed-artifact interpretation for the old `~1.192 MHz` feature because the old frequency is strongly suppressed in the new ratio screen, while the strongest ratio-view component moves upward to about `1.62 MHz`, close to the expected `~1.69 MHz` det-tracking region within the coarse frequency resolution of this short window.

That is only partial support for a Ramsey carrier hypothesis. The programmed `1.5 MHz`, predicted tracking `1.692 MHz`, and empirical `1.623 MHz` checks are close in amplitude and not separable by FFT resolution. More importantly, the raw signal LS screen does not independently choose the same frequency; it peaks near `0.882 MHz`. Under the project rule that signal presence should not be promoted from normalization-only evidence, this is not claim-grade.

## Claims not yet supported

- No supported numeric `T2*` claim from this dataset or the r03 Ramsey branch.
- No supported nearby-13C claim. The expected sidebands are weak and not consistently dominant.
- No supported precise detuning claim such as "the carrier is exactly 1.623 MHz" or "the prior component shifted exactly by +0.5 MHz"; the tau span gives only about `0.52 MHz` nominal frequency resolution.
- No supported conclusion that the raw `0.882 MHz` component is physical; it may be baseline/protocol/readout structure or a separate weak feature.

## Recommended next action

Do not run another blind Ramsey repeat on r03. The best next action is a bridge-free branch decision: either close the r03 Ramsey/T2star/13C branch as unsupported under the current short-tau Ramsey protocol, or switch to a different protocol designed to establish the carrier and decay independently, such as a Hahn/CPMG-style baseline or a deliberately longer-span Ramsey only after a fresh weak-pi pODMR check and an explicit resolvability/noise model.
