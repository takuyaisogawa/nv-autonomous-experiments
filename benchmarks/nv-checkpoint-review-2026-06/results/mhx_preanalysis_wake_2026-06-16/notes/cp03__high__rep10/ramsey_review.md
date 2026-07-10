# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- `measurement/m002.json`: bridge job contract for `nv23_ramsey_20260513_230331_auto_ramsey`.
- `measurement/m003.json` and `measurement/m004.json`: terminal result/status. Run completed at `2026-05-14T01:23:47`, final count text `35.122 kcps`, no stop request, safe shutdown ok.
- `evidence/e006.json`, `evidence/e009.json`, and `evidence/e017.md`: short-tau diagnostic model/intent/design context.
- `project/state.md`, `project/brief.md`, `project/advice.md`, and `md/memory.md`: project objective, prior Ramsey conclusions, and analysis posture.

## Calculations or scripts run

- Inspected the raw JSON arrays with local Python. Combined data shape is `(2, 41)` readouts; stored averages shape is `(12, 2, 41)`.
- Ran `python analyze_ramsey_shorttau.py`.
  - Outputs: `ramsey_shorttau_analysis_summary.json`, `ramsey_shorttau_analysis_stdout.json`, and `ramsey_shorttau_analysis.png`.
  - The script checks raw signal, point-wise signal/reference ratio, signal divided by a fitted reference line, empirical SEM across stored averages, target-frequency least-squares components, FFT bins, and descriptive damped fits.
- Programmatically verified the PNG file with PIL: `1440 x 1440`, RGBA.

## Key quantitative checks

- Run settings match the planned diagnostic: `tau = 0.048..1.968 us`, `48 ns` step, 41 points, `det = 1.0 MHz`, `mw_freq = 3.8759 GHz`, `12 x 90000 = 1.08e6` shots per tau point.
- Raw signal readout range is `6.50 kcps`; first `0.75 us` peak-to-peak is `5.69 kcps`. Median saved signal error is `1.40 kcps`; empirical stored-average SEM is `1.14 kcps`.
- Point-wise ratio range is `0.143`; first `0.75 us` peak-to-peak is `0.111`; empirical ratio SEM is `0.0127`.
- Stored-average means show substantial common-mode count drift: reference average-mean range `13.17 kcps`, signal average-mean range `13.74 kcps`. Ratio average-mean range is smaller but still non-negligible at `0.0626`.
- Linear LS components with a linear baseline:
  - Raw signal: carrier `1.000 MHz` p2p `2.56 kcps`, low 13C sideband `0.615 MHz` p2p `2.20 kcps`, high sideband `1.385 MHz` p2p `2.44 kcps`.
  - Point-wise ratio: carrier p2p `0.0548`, low sideband p2p `0.0486`, high sideband p2p `0.0543`.
  - Fitted-reference-line normalization: carrier p2p `0.0528`, low sideband p2p `0.0453`, high sideband p2p `0.0503`.
- FFT after linear detrending gives strongest bins at `1.524 MHz`, then `1.016 MHz`, then `0.508 MHz` in raw, ratio, and fitted-reference-line normalized views.
- Descriptive free damped fits prefer about `1.195 MHz` in raw, ratio, and fitted-reference-line normalized views. This is close to the earlier non-carrier feature near `1.178 MHz`, not a clean programmed-carrier confirmation.

## Plausible interpretation

This run is analyzable and does improve on the two prior long-window Ramsey attempts: the short-tau data contain a visible early-time oscillatory structure in the raw signal, and it is also present after reference normalization. A `1.0 MHz` carrier component is now plausible at roughly the expected order of magnitude, unlike the previous 8 us run where the carrier was below/near noise.

However, the short window gives only about two carrier cycles and about `0.52 MHz` nominal FFT resolution. The target-frequency LS amplitudes at the carrier and both expected 13C sideband positions are comparable, and the free damped fit prefers about `1.20 MHz`. The data therefore support "there is short-tau oscillatory structure" more strongly than they support "the programmed 1.0 MHz carrier is isolated" or "a 13C sideband is resolved."

The substantial stored-average common-mode count drift is provenance, not a hard invalidation, because the ratio/fitted-reference views retain the oscillatory structure. It does reduce confidence in extracting a precise decay envelope from this run.

## Claims not yet supported

- No well-supported numeric T2star value from this run. The descriptive damped fits are frequency/model dependent and should not be promoted.
- No supported nearby-13C conclusion. The low/high sideband targets are not separated from carrier/nearby-bin ambiguity.
- No claim that the earlier `~1.18 MHz` feature is physical. The new free-fit preference near `1.20 MHz` makes it worth explaining, but does not by itself rule out drift, sequence/analysis artifact, or under-resolved carrier/sideband mixing.
- No sub-grid resonance-frequency precision beyond the prior fine-pODMR grid-supported `3.8759 GHz` context.

## Recommended next action

Do not run another blind Ramsey accumulation or claim T2star/13C from this dataset. The next action should be a targeted decision step: refresh/check the r03 weak-pi pODMR resonance and then either run one deliberately det-shifted short-tau Ramsey diagnostic to test whether the `~1.2 MHz` structure follows the programmed carrier, or stop the r03 Ramsey branch and move to an alternate protocol. The critical requirement is that any next experiment must distinguish carrier-following behavior from the persistent non-carrier feature; more shots on the same scan will not do that.
