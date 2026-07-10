# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective, accepted r03 context, prior Ramsey/fine-pODMR conclusions, and expected checks.
- `evidence/e013.md`: note for the fine-pODMR review and second Ramsey start.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json` through `measurement/m005.json`: execute request, terminal result, terminal status, and run-control records for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- Generated local artifacts: `ramsey_scratch_summary.txt`, `ramsey_robustness_checks.txt`, and `ramsey_review_plot.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python/NumPy/SciPy.
- Confirmed run settings from raw export: `tau = 0..8 us`, 41 points, `0.2 us` step, 8 averages, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, snake scan order, per-average tracking.
- Computed raw readout means, point-wise `signal/reference` ratio, per-average ratios, detrended/windowed FFT, and least-squares sinusoid amplitudes at `0.615 MHz`, prior `0.884 MHz`, programmed `1.000 MHz`, and `1.385 MHz`.
- Fit descriptive offset+slope+Gaussian-decay cosine models from several starting frequencies; also repeated fits after excluding early tau points to check robustness.
- Plotted raw lines, ratio, and FFT in `ramsey_review_plot.png`.

Key numeric checks:

- FFT grid: bin spacing `0.121951 MHz`, Nyquist `2.500 MHz`; this covers the programmed carrier and expected sideband windows.
- Mean raw readouts: reference `49.313 kcps`, signal `44.580 kcps`; mean ratio `0.904215`, ratio range `0.802513..0.972134`.
- Strongest windowed FFT bins in the detrended ratio: `1.098 MHz`, `1.220 MHz`, `0.976 MHz`, then smaller bins at `0.488`, `0.366`, `1.707`, `2.317`, and `0.610 MHz`.
- Least-squares combined ratio amplitudes:
  - `0.615 MHz`: `0.01109`
  - prior `0.884 MHz`: `0.00742`
  - `1.000 MHz`: `0.00916`
  - `1.385 MHz`: `0.00843`
- Per-average LS amplitudes are scattered at all targets. For the programmed `1.000 MHz` component the per-average mean is `0.01463` with SD `0.00677`; for `0.615 MHz`, mean `0.02013` with SD `0.01225`; for `1.385 MHz`, mean `0.01417` with SD `0.00913`.
- Descriptive full-range decay-cosine fits converge near `0.956 MHz`, amplitude about `0.109`, `T2* ~0.465 us`, and `R2 ~0.41`. This is mainly driven by the initial high-contrast points; dropping early points makes fitted frequency/T2* non-unique.
- Average-level common-mode readout means vary substantially (`ref/sig` from about `40.47/36.20` to `55.53/50.27 kcps`), but detrended per-average ratio correlations with the combined ratio are positive and moderate (`0.318..0.647`).

## Plausible interpretation

- The second Ramsey is analyzable and has a det-shifted oscillatory response in the expected carrier region. The strongest FFT bins are around `0.976..1.220 MHz`, consistent with the deliberate `det = 1.0 MHz` within the 8 us / 41 point resolution and finite-envelope leakage.
- The prior scout's non-claim-grade `~0.884 MHz` component is not reproduced as the dominant component here; this favors treating it as noise/fit artifact or a weak unstable component rather than a stable physical Ramsey carrier.
- The envelope appears very short, with a descriptive full-range fit around `T2* ~0.5 us`. Because that value is sensitive to the earliest tau points and becomes non-unique when those points are excluded, it should be treated as a provisional short-T2* indication, not a final claim-grade T2*.
- No 13C conclusion is supported. The expected sideband targets near `0.615 MHz` and `1.385 MHz` are not clearly separated from carrier leakage, spectral-bin limits, and per-average scatter.

## Claims that are not yet supported

- A precise or claim-grade `T2*` value for r03.
- A nearby `13C` coupling/sideband claim.
- A resolved triplet or stable sideband pattern at `1.0 MHz +/- f13C`.
- A sub-grid resonance-frequency correction from this Ramsey alone.

## Recommended next action

Do not repeat the same 0..8 us Ramsey blindly. The data suggest a very short envelope, so run a short-span, denser Ramsey centered on the first few microseconds, still with `det = 1.0 MHz` and enough averages to preserve per-average diagnostics. A practical next measurement would prioritize `tau = 0..3 us` or `0..4 us` with finer spacing and 8+ averages, after confirming current tracking/counts. Use that to test whether the early-time decay and carrier frequency are reproducible enough for a T2* fit. Defer 13C-specific claims or sideband-optimized scans until the carrier/envelope is reproducible.
