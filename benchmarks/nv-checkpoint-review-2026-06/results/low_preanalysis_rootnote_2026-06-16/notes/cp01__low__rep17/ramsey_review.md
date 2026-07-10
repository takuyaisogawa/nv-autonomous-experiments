# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective and prior candidate/resonance context.
- `md/memory.md`, `md/knowledge.md`: local NV analysis guidance, especially raw/readout-aware review and fit-after-signal-presence caution.
- `context.json`: checkpoint provenance and recent evidence summary.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: Ramsey job specification; `tau = 0..6 us`, 31 points, `det = 1.5 MHz`, `mw_freq = 3.876 GHz`, `4 x 50000`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control; run completed, no stop requested, final count text `38.249 kcps`.
- Generated locally: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python/NumPy/SciPy.
- Treated readout 1 as reference and readout 2 as signal, consistent with the local default for no explicit +/-1 reference; checked both raw signal and signal/reference ratio.
- Confirmed data shape: `ExperimentData = [1, 2, 31]`, `ExperimentDataEachAvg = [1, 4, 2, 31]`, snake scan, per-average tracking.
- Basic acquisition numbers: 31 tau points, `dt = 0.2 us`, 6.0 us span, 4 averages, 50000 repetitions per average.
- Count/readout checks:
  - Final count after run: `38.249 kcps`, down from weak-pODMR final `43.890 kcps`.
  - Mean reference: `45.318 kcps`, peak-to-peak/mean `8.6%`.
  - Mean signal: `42.098 kcps`, peak-to-peak/mean `18.4%`.
  - Mean signal/reference: `0.9292`, peak-to-peak/mean `14.6%`.
- Descriptive damped-cosine fits with offset and linear baseline:
  - Raw signal free-frequency fit: `T2* = 2.06 us`, `f = 0.962 MHz`, `R2 = 0.484`.
  - Ratio free-frequency fit: `T2* = 2.39 us`, `f = 0.941 MHz`, `R2 = 0.446`.
  - Ratio fixed at programmed `1.5 MHz`: `R2 = 0.207`, `T2* = 0.38 us`.
  - Ratio fixed at expected `det - 13C ~= 1.115 MHz`: `R2 = 0.283`.
  - Ratio fixed at expected `det + 13C ~= 1.885 MHz`: `R2 = 0.077`, with `T2*` pinned at the upper bound.
- FFT checks used detrended fractional signal with a Hann window:
  - Actual DFT bin spacing from 31 samples at `0.2 us` is `161.3 kHz`; highest positive grid bin is `2.419 MHz`.
  - Ratio FFT strongest bins: `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `1.935 MHz`, `1.774 MHz`.
  - Programmed detuning bin near `1.5 MHz` ranks 12th in ratio FFT.
  - Expected `det - 13C` bin near `1.129 MHz` ranks 11th in ratio FFT.
  - Expected `det + 13C` bin near `1.935 MHz` ranks 4th in ratio FFT but is not isolated from other comparable peaks.
  - Per-average top ratio FFT bins are inconsistent: avg1 `0.968 MHz`, avg2 `1.452 MHz`, avg3 `0.323 MHz`, avg4 `0.806 MHz`.
- Rough physical scale check from the project model:
  - `mw_freq = 3.876 GHz` implies `B ~ 359.3 G` using the working `ms=+1` approximation.
  - Expected 13C Larmor scale is `~0.385 MHz`.

## Plausible interpretation

The Ramsey scout is analyzable and shows real structure in both raw signal and normalized ratio, with a contrast-scale oscillatory component. However, the dominant frequency content does not land cleanly at the programmed `1.5 MHz` detuning, and the free damped-cosine fits explain less than half the variance. The descriptive fit suggests a few-microsecond decay scale, roughly `T2* ~ 2 us`, but this should be treated as a scout-level estimate, not a supported project conclusion.

The FFT contains bins near the expected 13C sideband scale, including a ratio peak near `1.935 MHz` close to `det + 0.385 MHz`, but comparable peaks appear elsewhere and the per-average top bins are not stable. The `0.323 MHz` bin is near the standalone 13C Larmor scale, but in this Ramsey configuration that alone is not sufficient evidence for a nearby 13C coupling assignment.

The final counts dropped by about 13% relative to the weak-pODMR final count, and the reference readout itself varies by about 8.6% peak-to-peak. Drift or baseline changes are therefore plausible contributors to the non-ideal fit and the broad/multiple FFT peaks.

## Claims that are not yet supported

- No well-supported final `T2*` value is established from this Ramsey scout.
- No well-supported nearby `13C` conclusion is established.
- The free-fit frequency near `0.94-0.96 MHz` should not be claimed as the physical Ramsey detuning without a follow-up diagnostic, because it disagrees with the programmed `1.5 MHz` and is not stable enough across averages.
- The FFT peaks near `det +/- 13C` or near the standalone `13C` Larmor scale are not assignable to 13C with the present data quality.

## Recommended next action

Do a bounded Ramsey follow-up on the same r03 candidate only after refreshing the immediate resonance/tracking state. First repeat or spot-check weak-pi pODMR/current resonance because the Ramsey frequency content is not centered at the programmed detuning and counts drifted down. If resonance/tracking remains healthy, run a redesigned Ramsey with better frequency discrimination and stability: use a detuning whose expected carrier is verified by the refreshed resonance, keep the per-average tracking window inside the advisory cap, and increase evidence quality by adding averages rather than lengthening untracked windows. The next Ramsey should be planned to distinguish the carrier from `carrier +/- ~0.385 MHz` sidebands and should retain raw/readout plus per-average FFT review before any T2* or 13C claim.
