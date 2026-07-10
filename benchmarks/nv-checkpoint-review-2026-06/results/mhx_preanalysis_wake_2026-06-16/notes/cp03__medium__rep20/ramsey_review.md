# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `evidence/e017.md`.
- New Ramsey data and bridge artifacts: `measurement/m001.json` through `measurement/m005.json`.
- Fresh run: `1DExp-seq-ramsey-vary-tau-2026-05-13-230350`, accepted r03 target, `auto__ramsey`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 48 ns..1.968 us` in 41 points, `12 x 90000` repetitions, final counts `35.122 kcps`.

## Calculations/scripts run

- Added and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.
- Checks performed:
  - Parsed combined and per-average raw export arrays: combined data `1 x 2 x 41`, per-average data `1 x 12 x 2 x 41`.
  - Reviewed raw signal, reference channel, signal/reference ratio, per-average SEM, and average-to-average count stability.
  - Least-squares sinusoid checks with offset + linear trend at the programmed carrier `1.000 MHz` and expected 13C sideband positions `0.615 MHz` and `1.385 MHz`.
  - Broad frequency screen over `0.30..3.0 MHz` and FFT-bin check after linear detrending.
  - Descriptive fixed-`1 MHz` decaying-carrier grid fit, used only as a diagnostic and not as claim evidence.

## Quantitative results

- Raw signal range over tau: `47.568..49.744 kcps` (`2.176 kcps` span); median per-point raw-signal SEM across averages: `1.120 kcps`.
- Reference channel range: `40.698..47.197 kcps` (`6.499 kcps` span), much larger than the raw signal span.
- Signal/reference ratio range: `1.0174..1.1910` (`0.1736` span); median ratio SEM: `0.01508`.
- Average-to-average means changed substantially: raw signal mean range `27.1%` of mean, reference mean range `30.8%`, ratio mean range `6.9%`. This is significant count/readout instability context even though the run completed safely.
- Target least-squares amplitudes:
  - `1.000 MHz` carrier: raw signal amplitude `0.213 kcps` (`0.19 x` raw SEM), ratio amplitude `0.03275` (`2.17 x` ratio SEM), ratio `R2 = 0.452`.
  - `0.615 MHz` lower 13C sideband: raw amplitude `0.175 kcps` (`0.16 x` raw SEM), ratio amplitude `0.02923` (`1.94 x` ratio SEM).
  - `1.385 MHz` upper 13C sideband: raw amplitude `0.149 kcps` (`0.13 x` raw SEM), ratio amplitude `0.03175` (`2.10 x` ratio SEM).
- Broad LS screen is dominated by the lower edge of the screened band (`0.300 MHz`) in the ratio channel, consistent with slow normalization/reference structure rather than a clean Ramsey spectral feature.
- FFT after linear detrending has coarse bin spacing `0.508 MHz` because the scan spans only `1.92 us`; the strongest raw-signal bin falls near `1.016 MHz`, but the amplitude is not supported by the direct LS/raw SEM check.
- Descriptive fixed-carrier decaying fit prefers `T2* ~0.162 us`, but this is not claim-grade because it is driven by ratio/reference structure and not by a supported raw carrier.

## Plausible interpretation

- This short-tau/high-shot Ramsey diagnostic does not reveal a robust raw 1 MHz Ramsey carrier. The raw carrier amplitude is far below the measured across-average SEM, so a T2star fit is not scientifically supported from the raw signal.
- Ratio-only structure exists near the carrier and sideband frequencies, but the reference channel varies much more strongly than the signal channel and the broad screen is low-frequency dominated. The ratio features are therefore plausible normalization/readout artifacts or drift-coupled structure, not reliable Ramsey fringes.
- The result strengthens the prior pattern: r03 remains an aligned, trackable NV by pODMR evidence, but three Ramsey attempts have not produced a clean detuning-following carrier/13C sideband model.

## Claims not yet supported

- No supported numeric T2star for r03.
- No supported nearby 13C conclusion from Fourier/Ramsey sidebands.
- No claim that the weak ratio-only features at `1.000`, `0.615`, or `1.385 MHz` are physical Ramsey/13C features.
- No claim that the descriptive `~0.162 us` decay-fit value is T2star.

## Recommended next action

- Stop blind Ramsey repeats on r03 under the current route. The specific very-short-T2star/early-time-carrier hypothesis was tested and still did not produce raw claim-grade Ramsey evidence.
- Next, either run an alternate validation protocol that does not rely on the same weak raw Ramsey contrast, or close the r03 Ramsey/13C branch as unsupported under current conditions while preserving the aligned-NV claim.
- If continuing experimentally, first do a non-Ramsey health/contrast check: repeat a compact weak-pi pODMR or Rabi/readout sanity measurement at r03 to verify contrast and readout stability after the final counts dropped to `35.122 kcps`. Only then choose an alternate T2star/13C protocol; do not queue another long or short blind Ramsey repeat.
