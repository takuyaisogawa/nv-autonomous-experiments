# Ramsey Review: Short-Tau r03 Diagnostic

## Files/Data Used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, and targeted Ramsey guidance in `md/memory.md`.
- New terminal measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` bridge job, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Generated local artifacts: `analyze_ramsey_shorttau.py`, `ramsey_analysis_summary.json`, `ramsey_shorttau_diagnostics.png`.

## Calculations/Scripts Run

- Ran `python analyze_ramsey_shorttau.py`.
- Confirmed terminal job `nv23_ramsey_20260513_230331_auto_ramsey` completed without bridge error or stop request; savedexperiment path was `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Parsed Ramsey scan: `tau = 48 ns..1.968 us`, 41 points, 48 ns step, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, 12 averages x 90000 repetitions = `1.08e6` shots per tau point.
- Used embedded `ramsey.xml` to assign readouts: readout 0 is the initial 0-level reference, readout 1 is the Ramsey signal after the pulse block. `full_experiment=0`, so there is no separate inverted 1-level reference.
- Checked raw signal, pointwise `signal/reference`, and `signal / fitted-reference-line`; computed per-point SEM across stored averages, scan-order drift metrics, FFT after linear detrending, target least-squares sinusoid amplitudes, and free/fixed-frequency cosine/decay fits.

## Quantitative Checks

- Run health: completed; final count text `35.122 kcps`, above the job's `20 kcps` minimum but lower than the prior `44.184 kcps` baseline.
- Raw Ramsey signal is present: signal readout spans `40.698..47.197 kcps`, peak-to-peak `6.499 kcps`, about `14.6%` of the signal mean and `5.7x` the median per-point raw SEM (`1.138 kcps`).
- Reference-line-normalized signal also shows the oscillation: peak-to-peak `0.1376` ratio, median pointwise-ratio SEM `0.0127`.
- Frequency checks:
  - Best LS screen on raw signal and fitted-reference normalization is near `1.187 MHz`, with raw amplitude `1.682 kcps` and reference-line-normalized amplitude `0.0346`.
  - Programmed `1.0 MHz` carrier is present but not dominant: raw LS amplitude `1.282 kcps`, R2 improvement over linear baseline `0.377`; line-normalized amplitude `0.0264`.
  - Expected 13C sideband targets using prior project basis, `0.615 MHz` and `1.385 MHz`, are not dominant: line-normalized amplitudes `0.0227` and `0.0251`, smaller than the `1.187 MHz` screen maximum and likely contaminated by the short-window broad response.
  - FFT is only a coarse sanity check because the 1.92 us window gives `0.508 MHz` bin spacing; its top bin was `1.524 MHz`, while the nearest carrier bin was `1.016 MHz`. LS is the more useful frequency check here.
- Drift/provenance:
  - Stored-average mean levels vary substantially across the run: reference means span about `42.016..55.188 kcps`, signal means `37.474..51.213 kcps`.
  - Scan-order common-mode endpoint changes are mostly a few percent, with the largest about `+11.8%` in average 7 and `-6.2%` in average 10. This is significant provenance for decay/amplitude fits, but it does not remove the raw and reference-line-normalized oscillation.
- T2* fit check:
  - A free-frequency non-decaying cosine gives `f = 1.187 MHz`, amplitude `1.682 kcps`, SSE `27.67`, AIC `-6.12`.
  - Adding an exponential decay gives `f = 1.196 MHz`, nominal `T2* = 2.99 us`, SSE `26.84`, AIC `-5.36`.
  - The extra decay parameter is not favored over the flat-envelope model on this short window, so the numeric `~3 us` value should not be promoted as a supported T2*.

## Plausible Interpretation

- The short-tau/high-SNR diagnostic succeeded at the signal-presence question: r03 has a real Ramsey-like oscillation in the first `~2 us`.
- The dominant frequency near `1.18..1.20 MHz` is consistent with the prior det=1.0 MHz long-window dataset's largest screen near `1.178 MHz`, which was previously too weak to promote. The new data make that feature plausible rather than noise-only.
- The frequency offset from the programmed `1.0 MHz` detuning suggests either an effective Ramsey detuning/frequency-center offset of roughly `+0.18..0.20 MHz`, a sequence/timing phase effect, or another apparatus/model mismatch. It is not, by itself, evidence for a nearby 13C.
- A very-short-T2* explanation for the earlier absent carrier is less likely: oscillations persist across the full `48 ns..1.968 us` window. However, this window is too short and too drift-affected to determine the decay envelope.

## Claims Not Yet Supported

- No numeric T2* claim is supported. The current data support Ramsey signal presence, not a stable decay time.
- No nearby-13C claim is supported. The expected `det +/- 13C` sideband targets are not isolated, dominant, or model-consistent.
- Do not claim that the Ramsey frequency is exactly the programmed `1.0 MHz`; the best current screen is offset near `1.187 MHz`.
- Do not use the fixed-1 MHz exponential fit as evidence for `T2* ~0.19 us`; that fit is model-mismatched and worse than the free-frequency descriptions.

## Recommended Next Action

Do not run another blind long-window Ramsey repeat. First resolve the effective Ramsey frequency offset with a targeted detuning/frequency diagnostic on r03, using the same short-tau/high-SNR style and avoiding tau=0. If the `~1.19 MHz` component follows the programmed detuning with a fixed offset, update the resonance/detuning model and then run a longer high-SNR Ramsey window with adequate sampling to fit T2*. Only revisit 13C sideband claims after the carrier model is locked.
