# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`, and `evidence/e017.md`.
- New terminal Ramsey run: `measurement/m001.json` with bridge/result metadata in `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, and run control in `measurement/m005.json`.
- Run identity: `nv23_ramsey_20260513_230331_auto_ramsey`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Measurement settings: accepted r03 target, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 48 ns..1968 ns` in 41 points at 48 ns spacing, `12 x 90000` repetitions, snake acquisition order saved in tau order.

## Calculations/scripts run

- Created and ran `ramsey_shorttau_analysis.py`.
- Wrote quantitative output to `ramsey_shorttau_analysis_summary.json`.
- Wrote inspection plot to `ramsey_shorttau_review.png`.
- Checks performed:
  - extracted combined signal/reference traces and all 12 stored averages;
  - computed signal/reference ratio and per-average ratio;
  - estimated combined scatter and across-average SEM;
  - ran least-squares sinusoid screens at the programmed carrier `1.000 MHz` and expected sideband locations `0.615 MHz` and `1.385 MHz`;
  - ran Hann-windowed FFT peak screens on linearly detrended raw signal and ratio traces;
  - checked per-average mean levels for drift/common-mode changes.

Key numerical results:

- Raw signal mean `48.573 kcps`, tau scatter `0.456 kcps`, median across-average SEM `1.120 kcps`, median exported SEM `1.455 kcps`.
- Reference mean `44.655 kcps`, tau scatter `1.574 kcps`, with early low reference values driving large signal/reference ratio excursions.
- Per-average signal means ranged `42.016..55.188 kcps`; reference means ranged `37.474..51.213 kcps`, indicating substantial average-to-average common-mode/count changes.
- Raw-signal least-squares amplitude at `1.000 MHz`: `0.213 kcps` with approximate `z = 2.09`, below the per-point SEM scale. Raw sideband screens were also weak: `0.175 kcps` at `0.615 MHz` and `0.149 kcps` at `1.385 MHz`.
- Ratio least-squares amplitudes were larger, about `0.029..0.033`, with approximate `z = 3.7..4.4`, but this is not decisive because the reference channel has strong tau-dependent structure and the raw signal does not show a matching claim-grade carrier.
- FFT screens did not give a clean target model: raw signal peak cluster was near `1.09 MHz` with amplitude about `0.291 kcps`; ratio peak cluster was near `1.36 MHz` with amplitude about `0.035`. These are not cleanly locked to the programmed carrier or a supported 13C sideband pattern.

## Plausible interpretation

This short-tau/high-SNR Ramsey diagnostic does not reveal a robust early-time Ramsey carrier in the raw signal. The raw signal varies only weakly over tau relative to the measured per-point uncertainty, while the reference channel varies much more strongly and can create ratio-only structure. The data therefore argue against the simple explanation that the earlier non-claim-grade 8 us Ramsey runs merely missed a large, clean, very-short-T2star carrier at early tau.

The run remains scientifically useful as a targeted negative/weak diagnostic on accepted r03. It supports the project posture that r03 has a real pODMR resonance but that the Ramsey/T2star route, under these settings, is not producing a supported carrier/decay model.

## Claims not yet supported

- No numeric T2star value is supported from this run.
- No nearby 13C claim is supported from this run.
- The ratio-only oscillatory features should not be promoted to a Ramsey carrier or sideband model without raw/readout support.
- A decaying-cosine fit, if forced, would be model-selected rather than data-supported because the raw carrier amplitude is below/near noise and the reference channel is structured.
- This does not disprove all possible T2star/13C behavior for r03; it only says the current Ramsey configuration has not produced claim-grade evidence.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the r03 Ramsey/T2star/13C conclusion as unsupported under the current Ramsey route and choose an alternate targeted protocol before spending more bridge time: either use a sequence/readout variant designed to suppress the reference/tau artifact and validate a raw carrier first, or close the r03 Ramsey/13C branch as non-claim-grade and move to another aligned candidate/search branch.
