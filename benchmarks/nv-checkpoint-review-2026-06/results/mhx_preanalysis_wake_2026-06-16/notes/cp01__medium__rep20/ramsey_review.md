# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: project objective and current context.
- `md/memory.md`, `md/knowledge.md`: local NV/Ramsey guardrails, especially raw-readout-first and FFT-before-claims guidance.
- `evidence/e003.json`: prior weak-pi pODMR review supporting r03 and `mw_freq = 3.876 GHz`.
- `evidence/e008.json`, `evidence/e009.json`, `measurement/m002.json`: submitted Ramsey plan/job spec.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: completed bridge status/control for `nv23_ramsey_20260513_185505_auto_ramsey`.
- `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Generated local artifact: `ramsey_analysis.png`.

## Calculations or scripts run

- Used inline Python with `json`, `numpy`, `scipy`, and `matplotlib` to inspect `measurement/m001.json`.
- Confirmed scan shape and settings: 31 tau points from `0` to `6 us` in `0.2 us` steps, `4` averages, `50000` repetitions, snake scan order, data saved in tau order, tracking per average.
- Extracted `ExperimentData` and `ExperimentDataEachAvg` as two readout channels.
- Checked raw channel statistics:
  - Channel 1 mean `45.318 kcps`, peak-to-peak `3.904 kcps` (`8.6%` of mean).
  - Channel 2 mean `42.098 kcps`, peak-to-peak `7.750 kcps` (`18.4%` of mean).
  - Per-average channel-2 means were `43.365`, `40.553`, `42.797`, `41.677 kcps`, indicating appreciable average-to-average offset/drift.
- Checked channel-2 line trend: fitted slope `0.057 kcps/us`, only `0.8%` relative change over the full 6 us span, so the averaged channel-2 structure is not just a simple linear tau drift.
- Ran FFTs on averaged channel 2 after mean and linear detrending. Dominant line-detrended bins were:
  - `0.967742 MHz` amplitude `7.75`
  - `0.161290 MHz` amplitude `7.56`
  - `0.322581 MHz` amplitude `6.74`
  - `1.129032 MHz` amplitude `5.02`
  - `1.612903 MHz` amplitude `4.20`
- Compared against planned Ramsey features:
  - Programmed detuning: `1.5 MHz`
  - Expected 13C sidebands from project model: about `1.115 MHz` and `1.885 MHz`
  - Fixed-frequency linear fits on averaged channel 2 gave weak explanatory power: `R2 = 0.009` at `1.5 MHz`, `R2 = 0.042` at `1.115 MHz`, and `R2 = 0.042` at `1.885 MHz`.
- Ran empirical damped-cosine fits on averaged channel 2. Best fit found `f = 0.962 +/- 0.036 MHz`, `T = 2.06 +/- 0.91 us`, amplitude `3.18 kcps`, `R2 = 0.484`. This is descriptive only because per-average consistency is poor and the feature is not at the programmed carrier.
- Per-average frequency checks did not show a stable common Ramsey frequency:
  - Best simple sinusoid frequencies for channel 2 by average were about `0.935`, `0.540`, `0.210`, and `0.840 MHz`.
  - Detrended per-average channel-2 correlations were low, about `0.20` to `0.33` between different averages.
  - At `0.967742 MHz`, per-average fixed-frequency fits had `R2 = 0.315`, `0.065`, `0.128`, and `0.138`; only average 1 strongly supports that component.

## Plausible interpretation

- The measurement completed successfully and produced analyzable raw data; final counts were `38.249 kcps`, above the job minimum and not a hardware/count failure.
- Channel 2 is the spectroscopy-sensitive readout in this export. It shows a visible, non-flat structure in the averaged trace, with a descriptive best frequency near `0.96-0.97 MHz` and a fit-scale decay time around `2 us`.
- That feature could be a Ramsey response with the actual microwave center offset from the weak-pi pODMR grid estimate by roughly several hundred kHz. This remains only plausible because the per-average support is uneven and the programmed `1.5 MHz` carrier is not recovered.
- The FFT has a bin near the lower expected 13C sideband (`1.129 MHz` vs expected `1.115 MHz`), but it is not dominant and the corresponding fixed-frequency fit is weak. The stronger low-frequency bins and scattered per-average best frequencies make a 13C assignment premature.
- Drift and average-to-average changes are material. Tracking was per average, but each average still had an estimated untracked window near the project drift cap, and measured channel means differ substantially between averages.

## Claims that are not yet supported

- No well-supported `T2*` value is established. The damped-cosine `T ~2 us` is a descriptive fit to a non-claim-grade averaged trace.
- No well-supported 13C coupling conclusion is established. The expected sideband frequencies are not cleanly resolved with consistent per-average support.
- The Ramsey carrier is not confirmed at the programmed `1.5 MHz`; fixed-frequency checks at `1.5 MHz` explain almost none of the averaged channel-2 variance.
- The `0.96-0.97 MHz` component should not be promoted to a resonance-frequency correction without a repeat or independent frequency refinement.
- This measurement should not be used to reject r03 as an aligned candidate; prior weak-pi pODMR support remains, and this Ramsey scout is ambiguous rather than negative.

## Recommended next action

Run a targeted follow-up on r03 before making T2* or 13C claims. The most useful next experiment is a finer weak-pi pulsed ODMR or short Ramsey frequency/refinement diagnostic around `3.876 GHz` to resolve whether the Ramsey carrier offset is real, followed by a repeated Ramsey with shorter per-average tracking windows. Preserve total shots by reducing repetitions per average and increasing averages or splitting the acquisition, rather than lengthening the per-average window. Use the follow-up only if raw channel-2 oscillation, ratio/line-normalized behavior, per-average traces, and FFT all support the same frequency family.
