# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior calibration/model context: `evidence/e003.json` for accepted r03 weak-pi pODMR at 3.876 GHz; `evidence/e005.json` for Ramsey protocol/model/advisory context.
- New Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` submitted job/metadata, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.

## Calculations or Scripts Run

- Added and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Checks performed:
  - Parsed Ramsey raw export: `ramsey.xml`, `tau = 0..6 us`, 31 points, `dt = 0.2 us`, 4 averages x 50000 repetitions.
  - Used prior protocol inspection: readout 1 is reference, readout 2 is Ramsey signal for `full_experiment=0`.
  - Computed raw reference/signal traces, signal/reference ratio, and signal over fitted reference line.
  - Computed scan-order-aware common-mode drift using snake acquisition order.
  - Computed FFTs after linear detrending for raw signal, reference, point-wise ratio, and line-normalized signal.
  - Ran simple fits: fixed 1.5 MHz cosine, free-frequency cosine, and fixed 1.5 MHz Gaussian-decay cosine.

## Quantitative Findings

- The job completed normally: `nv23_ramsey_20260513_185505_auto_ramsey`, final counts `38.249 kcps`, elapsed `2124 s`.
- Sampling: actual RFFT bin spacing `161.3 kHz`; sampling Nyquist `2.5 MHz`; highest positive RFFT bin `2.419 MHz`.
- Raw readouts: reference mean `45.32 kcps`, signal mean `42.10 kcps`, signal median SEM from 4 averages `1.01 kcps`.
- Drift/provenance:
  - Per-average common-mode means span `6.37%` of their mean.
  - Scan-order linear drop scores were `0`, `3.46%`, `3.03%`, `0`; none exceeded a `15%` drop flag.
  - Final counts are lower than the earlier r03 weak-pODMR/fresh-track counts, so brightness drift is provenance, but this is not a count-collapse failure.
- The only robust-looking time-domain feature is the first point:
  - Signal at `tau=0` is `38.10 kcps` vs median `tau>0` signal `42.25 kcps`.
  - Drop is `4.15 kcps` or `9.83%`.
  - All 4 averages have tau=0 below their own `tau>0` median; mean drop `4.15 +/- 1.50 kcps` SEM over averages.
- FFT checks do not support the expected Ramsey carrier or 13C sidebands:
  - Raw signal top peak is `0.968 MHz` with amplitude `1.07 kcps`.
  - Programmed det target near `1.5 MHz` maps to the `1.452 MHz` bin, amplitude `0.281 kcps`, rank 13 excluding DC.
  - Expected 13C sideband bins near `1.129 MHz` and `1.935 MHz` rank 14 and 12 in raw signal.
  - Normalized views produce some peaks near low-frequency or high-sideband bins, but these are not stable across raw/line-normalized views and the reference itself has structure near those bins.
- Fit checks are not claim-grade:
  - Fixed 1.5 MHz cosine fit: amplitude `0.133 kcps`, `R2 = 0.009`.
  - Best free-frequency cosine: `0.962 MHz`, amplitude `1.08 kcps`, `R2 = 0.294`; not tied to the programmed det or 13C model.
  - Fixed 1.5 MHz Gaussian-decay fit can improve to `R2 ~ 0.30` with `T2* ~0.35 us`, but this is driven mainly by the tau=0 point and is not stable enough to use as a T2* value.

## Plausible Interpretation

The scout likely contains a real short-delay Ramsey/readout contrast feature at `tau=0`, because it appears in all stored averages and is much larger than the median point SEM. However, the 0.2 us step and 0..6 us scout do not show a sustained, model-consistent 1.5 MHz Ramsey oscillation. A very short T2* on the order of or below the first time step is plausible, but the current data cannot distinguish that from an under-resolved initial contrast plus drift/noise/phase issues.

## Claims Not Yet Supported

- No well-supported numeric T2* value is established.
- No supported 13C sideband or nearby-13C coupling conclusion is established from this Ramsey FFT.
- The free-frequency FFT/fit feature near `0.96-0.97 MHz` should not be promoted as physical.
- The result does not invalidate r03 as the aligned candidate; prior pODMR evidence still supports r03.
- The result is not evidence of hardware failure or count-collapse failure; the job completed and drift checks are advisory only.

## Recommended Next Action

Do not run a blind longer Ramsey repeat yet. First run a short-span, finer-step Ramsey diagnostic on r03 after normal fresh tracking/current resonance checks: keep the same weak-pODMR frequency basis and `det = 1.5 MHz`, but scan approximately `tau = 0..1.0-1.5 us` with `<=50 ns` spacing, using repetitions/averages chosen by the current advisory cap. The goal is to resolve whether the tau=0 contrast becomes a real early Ramsey oscillation/decay and to bracket T2*. Only if that short-span scan is fit-grade should a longer/higher-SNR FFT-oriented Ramsey be used for 13C sideband claims; if T2* is confirmed below about the current 0.2 us step, Ramsey FFT is not a viable 13C conclusion route.
