# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior Ramsey/design context: `evidence/e003.json` (terminal det=1.0 MHz 8 us Ramsey review), `evidence/e006.json` (short-tau model/advisory), `evidence/e017.md` (design/start note).
- New terminal measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Generated local analysis artifacts: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis.json`, `ramsey_shorttau_overview.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_shorttau.py`.
- Parsed the terminal raw export for `nv23_ramsey_20260513_230331_auto_ramsey`: `tau = 48 ns..1.968 us`, 41 points, `det = 1.0 MHz`, `mw_freq = 3.8759 GHz`, 12 averages x 90000 reps, 1.08e6 shots per tau point.
- Checked completion metadata: bridge status completed, no abort/error, no stop request, safe shutdown ok, final count text `35.122 kcps`.
- Used readout convention from the project context/prior XML review: readout 1 is the `mS=0` reference and readout 2 is the Ramsey signal for `ramsey.xml` with `full_experiment=0`.
- Computed raw signal/reference statistics, point-wise ratio, fitted-reference-line ratio, scan-order-aware common-mode drift scores, least-squares sinusoid amplitudes at 0.615422875, 1.000000, and 1.384577125 MHz, an exploratory frequency screen, FFT bins, and profile damped-sinusoid fits.

Key quantitative checks:

- The signal readout shows stronger short-window contrast than the prior 8 us scans: raw signal peak-to-peak `6.50 kcps`; first 0.75 us peak-to-peak `5.69 kcps`; median across-average signal SEM `1.14 kcps`. Reference peak-to-peak is smaller, `2.18 kcps`.
- Ratio views also show contrast: point-wise ratio peak-to-peak `0.143`; fitted-reference-line ratio peak-to-peak `0.138`.
- Scan-order common-mode drift flags: none. Per-average common-mode slopes were all below the 15% drop threshold, with drift scores `0.046..0.114`.
- Target LS amplitudes in raw signal: low 13C sideband `1.10 kcps`, carrier `1.28 kcps`, high 13C sideband `1.22 kcps`. Corresponding point-wise ratio amplitudes: `0.0243`, `0.0274`, `0.0271`.
- The broad LS screen, excluding sub-resolution low-frequency degeneracy below 0.5 MHz, peaks near `1.204 MHz` with raw amplitude `1.69 kcps`; FFT bins are coarse, with leading bins at about `1.524`, `1.016`, and `0.508 MHz`.
- The short span gives nominal frequency resolution `0.521 MHz`, worse than the planned carrier-to-13C-sideband offset of about `0.385 MHz`, so this run cannot resolve the expected 13C sidebands.
- Descriptive T2star profiles are not stable: a fixed 1.0 MHz damped fit prefers about `0.186 us` with an unrealistically large initial amplitude, while the screen-top-frequency fit near 1.204 MHz has an essentially open high-T2star profile (`delta AIC < 2` range about `1.19 us` to the 50 us grid limit in raw signal).

## Plausible interpretation

The short-tau/high-SNR Ramsey diagnostic produced real early-time Ramsey-like contrast on r03. This is materially stronger than the previous det=1.0 MHz 8 us terminal Ramsey, where the programmed-carrier raw amplitude was only `0.277 kcps` and below/near SEM. The result supports continuing the r03 Ramsey branch rather than closing it immediately.

However, the feature is not yet a clean physical model. The strongest simple screen is around `1.2 MHz`, not exactly the programmed `1.0 MHz`; target carrier and planned 13C sideband fits have similar amplitudes because the short time span makes them poorly separable. A modest resonance detuning/drift, baseline/window artifacts, and actual Ramsey contrast are all plausible contributors.

## Claims not yet supported

- No well-supported numeric T2star claim. The damped fits are model-dependent and not constrained by a clean decay envelope.
- No supported nearby-13C claim. The measurement was not designed with enough frequency resolution to separate the expected `1.0 MHz +/- 0.3846 MHz` components.
- No supported claim that the current resonance center remained exactly `3.8759 GHz` through the end of the run; the run finished several hours after the fine weak-pi pODMR calibration and final counts were lower.
- No supported assignment of the `~1.2 MHz` screen maximum to a specific physical source.

## Recommended next action

Run a fresh r03 fine weak-pi pODMR/retrack check before another Ramsey, because the apparent Ramsey frequency is offset from the programmed detuning and the run ended near the practical age limit of the prior frequency calibration. If the resonance remains usable, advisory-check a no-tau0, higher-SNR longer Ramsey spanning at least 6-8 us with enough points to resolve the carrier and expected 13C sidebands, then fit T2star only after raw/readout-aware signal shape is supported. Avoid a blind repeat of either previous long-window Ramsey.
