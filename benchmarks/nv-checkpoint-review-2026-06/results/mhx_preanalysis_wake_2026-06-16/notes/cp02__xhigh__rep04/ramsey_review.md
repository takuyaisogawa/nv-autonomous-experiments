# Ramsey Review

## Files/Data Used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Planning/evidence context: `evidence/e007.json`, `evidence/e009.json`, `evidence/e013.md` for the detuned Ramsey intent and expected `13C` sidebands.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.

## Calculations/Scripts Run

- Ran local inline Python JSON/NumPy checks on `measurement/m001.json`, `m003.json`, and `m004.json`.
- Confirmed terminal run completion: state `completed`, run id `1DExp-seq-ramsey-vary-tau-2026-05-13-204940`, final counts `44.184 kcps`, safe shutdown true, no stop request.
- Confirmed scan: `tau = 0..8 us`, `41` points, `dt = 0.2 us`, `8 x 50000` shots, snake order, tracking per average. Nominal FFT resolution is about `125 kHz`; Nyquist is `2.5 MHz`.
- Channel summaries from the combined trace:
  - raw signal mean `49.31 kcps`, peak-to-peak `4.29 kcps`;
  - reference mean `44.58 kcps`, peak-to-peak `7.72 kcps`;
  - signal/reference ratio mean `1.1071`, peak-to-peak `0.2174`.
- Per-average common-mode check: raw signal means ranged from about `-18.1%` to `+12.3%` versus the median, and reference means from `-18.8%` to `+12.8%`; ratio means were much steadier, about `-2.65%` to `+1.32%`.
- Single-frequency least-squares fits with linear baseline at the planned frequencies:
  - raw signal: `0.615423 MHz` amplitude `0.146 +/- 0.180 kcps`; prior `0.884 MHz` amplitude `0.365 +/- 0.173 kcps`; carrier `1.000 MHz` amplitude `0.245 +/- 0.180 kcps`; high sideband `1.384577 MHz` amplitude `0.239 +/- 0.179 kcps`.
  - signal/reference ratio: `0.615423 MHz` amplitude `0.0135 +/- 0.0083`; prior `0.884 MHz` amplitude `0.0095 +/- 0.0084`; carrier `1.000 MHz` amplitude `0.0120 +/- 0.0082`; high sideband `1.384577 MHz` amplitude `0.0107 +/- 0.0082`.
- FFT spot checks after linear detrending:
  - raw-signal largest components were near `0.854` and `0.976 MHz`, not a clean isolated programmed carrier;
  - ratio peaks were near `1.098` and `1.220 MHz`, with no convincing symmetric `13C` sideband pair.

## Plausible Interpretation

The run is analyzable and the NV stayed bright enough for review, but the Ramsey signal is not claim-grade. The det-shifted follow-up does not show a strong, coherent `1.0 MHz` carrier. The old `~0.884 MHz` region is again the largest raw-signal single-frequency fit, but only at about `2.1 sigma` in raw signal and weaker in signal/reference ratio, so it should remain an exploratory feature rather than a physical claim.

The per-average raw counts show substantial common-mode motion, especially one low-count average, while the ratio is steadier. That makes readout-aware quantities important and weakens any interpretation based only on the raw FFT. The expected `13C` sidebands at `0.615423 MHz` and `1.384577 MHz` are not supported by either raw-signal or ratio fits.

## Claims Not Yet Supported

- No well-supported numeric `T2*` is established from this measurement.
- No nearby `13C` coupling/sideband conclusion is established.
- The `~0.884 MHz` component is not proven physical, nor proven to be a fixed artifact; it is only a weak, non-claim-grade recurring feature.
- A longer or higher-SNR Ramsey repeat is not yet justified as the default next move, because the issue is carrier/average/readout consistency rather than only shot noise.

## Recommended Next Action

Do not make a `T2*` or `13C` claim and do not blindly repeat the same Ramsey with more averaging. The next project action should be a targeted det-following/sequence diagnostic: verify whether the Ramsey carrier follows the programmed detuning under the validated route, using a bounded plan on r03 or an appropriate control. If that diagnostic still fails to produce a det-following carrier, stop the r03 Ramsey claim path and pivot to an alternate sequence strategy or candidate/branch closure.
