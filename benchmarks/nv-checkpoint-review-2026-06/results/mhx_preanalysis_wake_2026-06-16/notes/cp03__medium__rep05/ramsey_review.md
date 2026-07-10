# Ramsey Review: short-tau high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement data and bridge metadata:
  - `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: submitted job/spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal run status.
  - `measurement/m005.json`: run control.
- Design/start context: `evidence/e017.md`.
- Generated local artifacts: `ramsey_analysis_summary.json`, `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python and inspected array shapes:
  - `ExperimentData`: 2 readouts x 41 tau points.
  - `ExperimentDataEachAvg`: 12 averages x 2 readouts x 41 tau points.
  - Scan: tau `48 ns..1.968 us`, step `48 ns`, 41 points, snake order saved in tau order.
- Checked terminal metadata:
  - `auto__ramsey`, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000` repetitions.
  - Completed safely, final count text `35.122 kcps`, no stop request, no bridge error.
- Computed raw readout means/ranges, per-point SEM from stored averages, signal/reference ratio, and signal divided by a fitted reference line.
- Ran least-squares sinusoid screens with a linear baseline at the target frequencies:
  - expected lower 13C sideband approx `0.616 MHz`
  - programmed carrier `1.000 MHz`
  - expected upper 13C sideband approx `1.384 MHz`
- Ran FFT checks after linear detrending and a Hann window.
- Checked per-average target-frequency amplitudes/phases and a constrained decay-envelope grid for possible short T2star behavior.

## Quantitative checks

- Raw means:
  - reference: `48.573 kcps`
  - signal: `44.655 kcps`
- Raw signal range: `40.698..47.197 kcps`, peak-to-peak `6.499 kcps`.
- Median SEM from stored averages:
  - signal: `1.138 kcps`
  - reference: `1.120 kcps`
  - signal/reference ratio: `0.0127`
- Average-to-average common-mode drift is visible:
  - reference mean changed from `49.376` to `45.918 kcps` from average 1 to 12.
  - signal mean changed from `44.710` to `43.873 kcps`.
  - linear slopes were about `-0.643 kcps/avg` reference and `-0.590 kcps/avg` signal.
- Exact-frequency LS amplitudes with linear baseline:
  - raw signal at `0.616 MHz`: `1.100 kcps`, partial R2 `0.307`
  - raw signal at `1.000 MHz`: `1.282 kcps`, partial R2 `0.377`
  - raw signal at `1.384 MHz`: `1.225 kcps`, partial R2 `0.334`
  - ratio at `1.000 MHz`: `0.0274`, partial R2 `0.355`
- FFT after detrending has broad/nearby components because the short span gives coarse resolution:
  - raw signal top bins include `1.524 MHz` amplitude `1.248 kcps`, `1.016 MHz` amplitude `0.921 kcps`, and `0.508 MHz` amplitude `0.751 kcps`.
- Per-average target phase is fairly coherent, but amplitudes are small:
  - amplitude-weighted phase coherence at `1.000 MHz`: `0.948`
  - per-average 1 MHz raw-signal amplitudes span `0.699..2.040 kcps`
- Constrained damped-cosine grid checks prefer very short envelopes, but not stably:
  - at `1.000 MHz`, exponential envelope best T about `0.186 us`; Gaussian envelope best T about `0.377 us`.
  - nearby frequencies give comparable fits, and some fits require large initial amplitudes. Treat this as a failure-mode hint, not a T2star measurement.

## Plausible interpretation

- The short-tau/high-SNR data show weak evidence for an early-time Ramsey-like oscillatory component near the programmed carrier region. The carrier amplitude is larger than in the previous 8 us terminal review but still only about the per-point SEM scale and smaller than the planned order-`2..6 kcps` raw oscillation scale.
- The data are compatible with a very short T2star/early-time contrast loss on r03, roughly sub-microsecond in character, but the exact T2star is not supported because the fit is model- and frequency-dependent.
- The short window intentionally tests early-time visibility, but it cannot cleanly distinguish `1.000 MHz` carrier from nearby `0.616/1.384 MHz` 13C sideband hypotheses. The FFT bin spacing is about `0.508 MHz`, so sideband interpretation is intrinsically weak here.
- The visible average-to-average drift and small target amplitude make a physical assignment possible but not claim-grade.

## Claims not yet supported

- No well-supported numeric T2star value from this dataset.
- No well-supported nearby 13C conclusion from this dataset.
- No supported claim that the dominant spectral component is the programmed `1.0 MHz` carrier rather than sideband leakage, baseline/decay shape, drift residual, or windowing artifact.
- No support for another blind long-window Ramsey repeat on the same settings.

## Recommended next action

Do not claim T2star or 13C from this short-tau Ramsey alone. Since this was the non-blind diagnostic after two non-claim-grade Ramsey runs, stop blind Ramsey repeats on r03. The next useful action is to switch protocol: run a direct echo/CPMG-family coherence baseline on the same accepted r03, with a fresh tracking/count check and a current frequency sanity check if needed, to determine whether coherence is genuinely very short before investing in 13C-resolved Ramsey/FFT work.
