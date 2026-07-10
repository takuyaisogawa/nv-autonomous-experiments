# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, and relevant prior notes in `md/knowledge.md`, `md/memory.md`, `evidence/e017.md`.
- New terminal measurement metadata: `measurement/m002.json` job contract, `measurement/m003.json` bridge result, `measurement/m004.json` run status, `measurement/m005.json` control.
- New raw export: `measurement/m001.json`, saved run `1DExp-seq-ramsey-vary-tau-2026-05-13-230350`, accepted target `image145844_reimage_r03`.
- Scratch artifacts created here: `ramsey_shorttau_analysis.py`, `ramsey_shorttau_analysis_summary.json`, `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Ran Python extraction/checks on `measurement/m001.json`.
- Verified terminal settings: `tau = 48 ns..1.968 us`, 41 points, 48 ns spacing, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` repetitions.
- Treated channel 0 as reference-like and channel 1 as signal-like based on the readout shapes; checked both raw signal and normalized `ch1/ch0` / `ch1/linear(ch0)`.
- Quantified per-point uncertainty from 12 stored averages:
  - median signal-like SEM `1.14 kcps`;
  - median reference-like SEM `1.12 kcps`;
  - median ratio SEM `0.0127`.
- Checked average-to-average count drift:
  - reference-like average means ranged `42.02..55.19 kcps`;
  - signal-like average means ranged `37.47..51.21 kcps`;
  - ratio average means ranged `0.893..0.956`;
  - reference/signal mean correlation across averages was high in the interactive check (`r ~ 0.96`), so much of the count change is common-mode.
- Ran least-squares sine/cosine amplitude checks after a linear baseline term at the planned frequencies:
  - raw signal amplitudes: `0.615 MHz = 1.10 kcps`, `1.000 MHz = 1.28 kcps`, `1.385 MHz = 1.22 kcps`;
  - ratio amplitudes: `0.615 MHz = 0.0243`, `1.000 MHz = 0.0274`, `1.385 MHz = 0.0271`;
  - reference-line normalized amplitudes: `0.615 MHz = 0.0227`, `1.000 MHz = 0.0264`, `1.385 MHz = 0.0251`.
- Checked per-average phase consistency in the ratio LS coefficients:
  - vector/scalar mean ratios were `0.88`, `0.96`, `0.91` at `0.615`, `1.000`, `1.385 MHz`;
  - phase resultants were `0.87`, `0.95`, `0.92`.
- Ran exploratory frequency screens from `0.1..5 MHz`. They were dominated by very-low-frequency/baseline curvature near the lower screen boundary, not by an isolated carrier or sideband peak.

## Plausible interpretation

The measurement is complete, analyzable, and higher-SNR than the previous long-window Ramsey attempts. The short-tau trace has reproducible early-time structure, and the programmed `1.0 MHz` carrier plus expected `det +/- 13C` sideband positions (`~0.615` and `~1.385 MHz`) all return coherent LS components across averages.

However, the target amplitudes are all similar in size and ride on a much larger slow transient/baseline curvature. The short `1.92 us` window also gives coarse FFT discrimination, so the data do not cleanly separate a carrier from 13C sidebands. Ratio/reference normalization reduces common-mode count drift but does not turn the trace into a simple decaying Ramsey oscillation.

This supports the idea that r03 has real short-window Ramsey-like contrast or a protocol/readout transient, but it does not yet support a numeric T2star or nearby-13C conclusion.

## Claims not yet supported

- No claim-grade T2star value. A decaying sinusoid model is not uniquely supported by the normalized data shape.
- No supported nearby 13C claim. The expected sideband frequencies have coherent LS components, but they are not isolated from the carrier/baseline structure and have not been validated by a same-window detuning shift.
- No claim that the broad early rise is solely NV dephasing. It could include readout/protocol transient, normalization residual, or remaining drift structure.
- No sub-grid or sub-model precision on the resonance center beyond the prior fine pODMR grid-supported `3.8759 GHz` basis.

## Recommended next action

Do not run another blind long-window Ramsey repeat. If continuing r03, run one targeted same-window detuning-shift Ramsey confirmation, keeping the short-tau/high-SNR structure comparable but changing `det` so carrier and expected sidebands must move predictably. For example, a short-tau det=`1.5 MHz` confirmation would test whether the coherent components shift toward `1.115`, `1.5`, and `1.885 MHz`; failure to shift should close the r03 Ramsey/13C branch as unsupported under current conditions or move to an alternate protocol such as phase-controlled/quadrature Ramsey or echo/XY8-style nuclear-spin sensing.
