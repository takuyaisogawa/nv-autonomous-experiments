# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior/related evidence skimmed: `evidence/e003.json` (terminal 8 us det=1.0 MHz Ramsey review), `evidence/e006.json` (short-tau design/model), `evidence/e017.md` (short-tau job start note).
- New terminal measurement data:
  - `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: bridge job spec.
  - `measurement/m003.json`: completed bridge result.
  - `measurement/m004.json`, `measurement/m005.json`: status/control, no stop request.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.
- Confirmed run settings: `auto__ramsey`, readout1 reference/readout2 Ramsey signal from project design evidence, `tau=0.048..1.968 us`, `41` points, `48 ns` spacing, `det=1.0 MHz`, `mw_freq=3.8759 GHz`, `12 x 90000` repetitions (`1.08e6` shots per tau point), terminal final counts `35.122 kcps`.
- Raw/readout checks:
  - Combined raw signal range over tau: `6.50 kcps`.
  - Median per-point signal SEM across averages: `1.14 kcps`.
  - Fitted-reference-line normalized signal range: `0.138`; mean SEM `0.0106`.
- Target sinusoid least-squares checks with offset + linear trend:
  - Programmed carrier `1.000 MHz`: raw-signal amplitude `1.28 kcps`; line-normalized amplitude `0.0264`; point-wise-ratio amplitude `0.0274`.
  - Expected 13C sideband checks, using the project model sidebands near `0.615/1.385 MHz`: line-normalized amplitudes `0.0227` and `0.0251`, comparable to the carrier.
  - Exploratory line-normalized LS screen above `0.3 MHz`: largest components at about `0.300 MHz` (`0.057`), `1.208 MHz` (`0.0346`), `0.451 MHz` (`0.0325`), `1.056 MHz` (`0.0300`), and `1.359 MHz` (`0.0275`).
  - Detrended FFT bins: `0.508 MHz` (`0.0285`) and `1.016 MHz` (`0.0273`) are the largest two bins; the short window gives coarse frequency resolution around `0.52 MHz`.
- Fixed-frequency decay-grid checks at `1 MHz`:
  - Gaussian-envelope grid minimum around `T2star = 0.36 us`; exponential-envelope grid minimum around `T2star = 0.19 us`.
  - These fits improve residuals versus a no-decay sinusoid, but are not promoted because the fitted amplitudes are inflated by early-time recovery/baseline terms and the model is not uniquely supported by the data shape.
- Drift/provenance checks:
  - Average-level reference means span `26.8%` of median; signal means span `30.8%` of median.
  - Late averages are substantially lower: reference averages 10-11 are about `-10.8%` and `-14.4%`; signal averages 10-11 are about `-11.2%` and `-15.9%` versus median.
  - The measurement completed safely with no stop request or bridge abort, but the common-mode movement is significant provenance.

## Plausible interpretation

- The short-tau/high-SNR run is better than the prior 8 us det=1.0 MHz Ramsey for early-time visibility: the programmed `1 MHz` component is now detectable in raw and normalized least-squares screens (`1.28 kcps` raw, `0.026` ratio), whereas the prior terminal 8 us run reported only `0.277 kcps` raw / `0.00916` ratio at the carrier.
- The combined trace has a strong early low-to-high recovery over the first few hundred ns and then broad structure over the rest of the 1.92 us window. This is compatible with a very short-lived Ramsey response mixed with baseline/transient behavior, but it is not a clean decaying sinusoid.
- The data make "very short T2star, probably sub-us" plausible, but they do not support a numeric T2star claim. The decay-grid minima around `0.2..0.4 us` should be treated as descriptive only.
- The short window was not designed for high-resolution 13C spectroscopy. The expected sideband amplitudes are comparable to the carrier and to nearby exploratory components, so there is no supported nearby-13C conclusion from this run.

## Claims not yet supported

- A well-supported numeric `T2star` for r03.
- A well-supported nearby `13C` coupling/no-coupling conclusion.
- A clean det-following Ramsey carrier model for r03 under the current Ramsey route.
- Any assignment of the `0.300`, `0.508`, `1.016`, `1.208`, or `1.359 MHz` components to physical sidebands rather than short-window leakage, baseline/transient structure, or drift/systematics.
- Sub-grid or sub-kHz precision for the microwave resonance beyond the existing grid-supported `3.8759 GHz` input.

## Recommended next action

Do not run another blind long-window Ramsey repeat and do not promote the forced decay fits. If continuing r03, run a targeted control that tests whether the short-tau feature follows the programmed Ramsey phase, preferably a phase-cycled/differential Ramsey route if available. If only the current simple Ramsey route is available, use the same short-tau window/SNR class but intentionally change `det` (for example `0.5` or `1.5 MHz`) and require the feature to move coherently before any T2star fit is promoted. If the feature does not det-follow, close the r03 Ramsey/T2star/13C branch as unsupported under this route and move to an alternate protocol such as Hahn/CPMG for coherence baseline rather than more Ramsey accumulation.
