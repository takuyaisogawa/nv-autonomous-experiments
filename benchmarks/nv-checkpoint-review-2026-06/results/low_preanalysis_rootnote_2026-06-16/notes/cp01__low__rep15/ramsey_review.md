# Ramsey review: image145844 reimage r03

## Files/data used

- `project/brief.md`, `project/advice.md`, and `project/state.md` for objective, accepted r03 context, weak-pi pODMR frequency basis, and prior decisions.
- `measurement/m002.json` for the submitted Ramsey contract: `tau = 0..6 us`, 31 points, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, 4 averages x 50000 repetitions, `full_experiment = 0`.
- `measurement/m003.json` and `measurement/m004.json` for completion/status: job completed, saved run `1DExp-seq-ramsey-vary-tau-2026-05-13-185521`, final count text `38.249 kcps`, elapsed `2124 s`.
- `measurement/m001.json` for the exported raw Ramsey data: two readout channels, four stored averages, snake scan order, data saved in tau order.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs written:
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis.png`
- Checks performed:
  - Parsed combined signal/reference readouts and per-average readouts.
  - Computed `signal/reference` ratio and signal normalized by a linear reference line.
  - Checked per-average mean counts and per-average ratio correlation with the final combined ratio.
  - FFT-checked detrended ratio and signal/reference-line traces with a Hann window.
  - Tried simple exponential-decay and Gaussian-decay cosine fits to the combined ratio.

Key quantitative results:

- Tau grid: 31 points from `0` to `6.0 us`, spacing `0.2 us`; FFT bin spacing `0.1613 MHz`, Nyquist `2.5 MHz`.
- Combined signal mean/range: `45.318 kcps`, range `44.038..47.942 kcps`.
- Combined reference mean/range: `42.098 kcps`, range `38.096..45.846 kcps`.
- Combined `signal/reference` ratio mean/range: `1.0776`, range `1.0055..1.1641`, peak-to-peak `0.1586`.
- Reference linear trend over the tau axis is small in the combined data: about `0.82%` fractional change.
- Per-average signal means: `46.44`, `43.68`, `46.59`, `44.56 kcps`; reference means: `43.36`, `40.55`, `42.80`, `41.68 kcps`.
- Per-average ratio correlations with the final combined ratio: avg1 `0.71`, avg2 `0.42`, avg3 `0.55`, avg4 `0.60`. This supports some repeated structure, but not a clean repeat in every average.
- FFT of detrended `signal/reference` has top bins at `0.968`, `0.323`, `0.806`, `1.935`, and `1.774 MHz`, all comparable in amplitude.
- FFT of signal normalized by a linear reference line instead emphasizes `1.935`, `1.774`, `2.097`, `0.161`, and `1.452 MHz`; the intended `1.5 MHz` detuning bin appears but is not dominant.
- Best simple exponential decaying cosine fit to `signal/reference`: frequency `0.947 MHz`, T2-like decay `2.29 us`, `R2 = 0.435`.
- Best simple Gaussian decaying cosine fit: frequency `0.946 MHz`, T2-like decay `3.12 us`, `R2 = 0.427`.

## Plausible interpretation

- The completed r03 Ramsey data likely contains a real oscillatory component: the combined ratio has visible contrast and each stored average has some positive correlation with the combined trace.
- The oscillation is not cleanly centered at the requested `1.5 MHz` detuning. The best simple time-domain fits prefer about `0.95 MHz`, while FFT evidence depends noticeably on normalization choice.
- A frequency near `0.95 MHz` could still be physically plausible if the weak-pi pODMR grid minimum at `3.876 GHz` is offset from the true resonance by several hundred kHz. The prior weak-pi pODMR grid was useful for selecting a Ramsey frequency, but it was not a high-precision resonance center.
- The run also shows count/provenance concerns: final count `38.249 kcps` is below the prior fresh track/weak-pODMR counts near `43.5..43.9 kcps`, and per-average signal/reference means vary substantially. The snake order and even average count reduce simple monotonic tau-order drift artifacts, but do not remove drift as a concern.
- A rough T2* scale of a few microseconds is suggested by the descriptive fits, but the fit quality is too weak to treat `2.3 us` or `3.1 us` as a supported T2* result.

## Claims that are not yet supported

- No well-supported T2* value is established from this scout. The simple fits have low explanatory power and depend on a noisy, normalization-sensitive trace.
- No well-supported 13C conclusion is established. The expected 13C scale is about `0.385 MHz`; the FFT has multiple comparable peaks, and there is no robust, normalization-stable sideband pattern around either the requested `1.5 MHz` carrier or the apparent `~0.95 MHz` oscillation.
- This run does not by itself prove absence of nearby 13C. It is an inconclusive first scout rather than a negative 13C result.
- The data do not invalidate r03 as the aligned candidate. Prior strong-pi and weak-pi pODMR remain the alignment evidence; this Ramsey run mainly says the current T2*/13C evidence is not yet claim-grade.

## Recommended next action

Run a targeted Ramsey follow-up on r03 after confirming/retracking counts, with a more precise resonance/detuning setup before spending on a longer T2* run. Recommended sequence:

1. Re-track r03 and verify counts have recovered near the previous `~43 kcps` level; if not, handle focus/count drift first.
2. Run a narrower weak-pi pODMR or short frequency-calibration Ramsey around the apparent offset to set a better Ramsey carrier/detuning.
3. Then repeat Ramsey with enough time span and points to resolve the apparent carrier and possible `13C` sidebands, while keeping the per-average tracking window within drift guidance.

Do not report a final T2* or 13C conclusion from the current scout.
