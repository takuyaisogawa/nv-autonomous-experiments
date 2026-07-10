# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`: objective, accepted r03 context, weak-pi pODMR basis, and planned Ramsey parameters.
- `md/memory.md`, `md/knowledge.md`: local NV analysis conventions, especially raw/readout-aware review and fit-after-signal guidance.
- `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: submitted Ramsey job contract.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json`, `measurement/m005.json`: terminal status/control records.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Output artifacts:
  - `ramsey_review_calc.json`: numeric summaries, FFT checks, and bounded fit results.
  - `ramsey_review_plot.png`: raw readouts, signal/reference trace, and FFT plot.
- Confirmed acquisition parameters from raw export/result:
  - `tau = 0..6 us`, `31` points, `dt = 0.2 us`.
  - `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
  - `4` averages x `50000` repetitions, snake order, tracking per average.
  - `full_experiment = 0`, so readout 1 is the 0-level reference and readout 2 is the Ramsey signal.
  - FFT Nyquist `2.5 MHz`; nominal bin spacing from span `166.7 kHz` (`np.fft` bins for 31 points are spaced `161.3 kHz`).
- Quantitative checks:
  - Raw signal mean `42.10 kcps`; raw signal peak-to-peak `7.75 kcps` (`18.4%` of mean).
  - Signal/reference mean `0.929`; normalized peak-to-peak `0.1355` (`14.6%` of mean).
  - Reference peak-to-peak fraction `8.6%`, so baseline/reference motion is non-negligible.
  - Average signal means: `43.36`, `40.55`, `42.80`, `41.68 kcps`.
  - Average reference means: `46.44`, `43.68`, `46.59`, `44.56 kcps`.
  - Combined normalized FFT strongest peaks: `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `1.935 MHz`, `1.774 MHz`.
  - Nearest programmed carrier bin to `1.5 MHz`: `1.452 MHz`, amplitude `0.087`.
  - Nearest expected sidebands using `f13C ~0.385 MHz`: `1.129 MHz`, amplitude `0.093`; `1.935 MHz`, amplitude `0.151`.
  - Per-average normalized traces are not strongly repeatable: pairwise correlations are mostly small (`-0.09` to `0.28`, with one `-0.08`), and each average's top FFT peak differs.
  - Bounded exp-cos fit to signal/reference gives frequency `0.944 MHz`, T2* `2.39 us`, `R2 = 0.44`, T2* stderr `1.17 us`. A stretched fit collapses to an unphysical very short envelope and lower `R2 = 0.14`.

## Plausible interpretation

- The measurement completed cleanly and contains a real-looking Ramsey-scale modulation in the combined raw and normalized traces.
- The combined trace is not consistent enough to support a quantitative T2* claim. The best simple fit is descriptive only: it does not lock to the programmed `1.5 MHz` carrier, explains less than half of the normalized variance, and has large T2* uncertainty.
- The FFT does not provide a clean 13C signature. A peak near the expected upper sideband (`~1.935 MHz`) exists, but it is comparable to unrelated peaks and the carrier bin is weaker than several other components. Per-average FFTs do not reproduce a stable carrier/sideband pattern.
- A reasonable scout-level hypothesis is that r03 remains a plausible aligned NV with a short/low-SNR Ramsey signal, possibly mixed with drift/reference variation or an effective detuning different from the requested `1.5 MHz`. This run is useful for redesigning the follow-up but not for final interpretation.

## Claims not yet supported

- No well-supported T2* value is established from this run.
- Do not report `T2* = 2.39 us` as a result; it is only a weak descriptive fit.
- No well-supported nearby 13C conclusion is established.
- Do not assign the `1.935 MHz` FFT component to `det + 13C`; it is not isolated from comparable peaks and is not repeatable across averages.
- Do not claim that the requested `1.5 MHz` Ramsey carrier was cleanly observed.

## Recommended next action

Run a redesigned Ramsey follow-up on r03 before changing candidates. Keep the weak-pi frequency basis unless a quick resonance check indicates drift, but improve claim quality by increasing independent averages and/or using a denser tau grid while respecting the tracking-window cap. The next Ramsey should be designed to test whether the effective Ramsey carrier is near `~0.9-1.0 MHz` or `1.5 MHz`, and should preserve FFT coverage for `det +/- ~0.385 MHz`. If the follow-up remains non-repeatable, switch from blind repeats to a targeted resonance/detuning diagnostic or a different coherence sequence.
