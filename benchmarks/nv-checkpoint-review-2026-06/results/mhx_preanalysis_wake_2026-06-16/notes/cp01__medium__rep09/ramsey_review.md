# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, and `context.json` for objective and current project constraints.
- `measurement/m001.json`: raw-exported Ramsey savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: Ramsey job contract; `tau = 0..6 us`, 31 points, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `length_pi_pulse = 52 ns`, 4 averages x 50000 repetitions.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal job/result/status/control metadata. The job completed at `2026-05-13T19:30:40`, elapsed `2124 s`, with no stop request.
- Prior context from `evidence/e003.json` to `evidence/e011.json` was used only to confirm the accepted r03 weak-pi ODMR context and Ramsey plan provenance.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis.png`
- Checks performed:
  - Parsed Ramsey arrays: `ExperimentData` shape `(1, 2, 31)`, `ExperimentDataEachAvg` shape `(1, 4, 2, 31)`.
  - Treated trace 1 as reference and trace 2 as signal by project convention, then analyzed `signal/reference`.
  - Computed per-average means/correlations, mean normalized ratio, FFT spectrum, and damped-cosine fits.
  - Fit models on normalized `signal/reference`:
    - Exponential envelope cosine: `T2* = 3.11 +/- 2.17 us`, `f = 1.686 +/- 0.030 MHz`, `R2 = 0.173`.
    - Gaussian envelope cosine: degenerate/unstable fit, `R2 = 0.048`.
  - FFT check:
    - 31-point bin spacing `0.161 MHz`, Nyquist `2.419 MHz`.
    - Strongest zero-padded peak near `0.929 MHz`, not the programmed `1.5 MHz` detuning.
    - Nearest-bin amplitudes: carrier `1.452 MHz = 0.0937`, lower sideband `1.129 MHz = 0.1002`, upper sideband `1.935 MHz = 0.1623`. These are comparable to other broad/noisy peaks rather than an interpretable carrier-plus-sideband pattern.
  - Per-average normalized correlations with the mean were modest: `0.68`, `0.42`, `0.58`, `0.56`.

## Plausible interpretation

- The Ramsey run completed and contains a measurable reference-normalized variation: normalized `signal/reference` peak-to-peak is about `14.6%`.
- The variation is not well described by a simple decaying Ramsey cosine at the intended `1.5 MHz` detuning. The best exponential fit moves to `1.686 MHz` and still explains little variance.
- The data are therefore best treated as a low-confidence Ramsey scout: some oscillatory/readout structure is present, but SNR, drift, phase instability, detuning mismatch, or a mixture of these dominates enough that T2* extraction is not claim-grade.
- The result does not invalidate r03 alignment by itself; the prior strong-pi and weak-pi pODMR evidence still supports r03 as the current aligned candidate.

## Claims not yet supported

- No well-supported T2* value is established. The only numerical fit gives `T2* ~3.1 us`, but uncertainty is large and fit quality is poor.
- No well-supported 13C conclusion is established. The expected sideband scale near `1.5 +/- 0.385 MHz` is not cleanly resolved against the noisy/broad spectrum.
- This measurement does not support a claim of either 13C coupling presence or absence.
- The apparent spectral peak near `0.93 MHz` should not be interpreted as a physical coupling without a repeat or protocol check.

## Recommended next action

Run a Ramsey repeat on r03 aimed first at establishing a clean carrier/T2* trace, not yet a final 13C spectrum. Use the same weak-pi ODMR center unless a quick resonance check suggests drift, keep `det = 1.5 MHz`, but shorten the per-average window below the prior `492.9 s` estimate, e.g. `tau = 0..4 us` with `0.2 us` spacing and more tracked averages if advisory allows. If that repeat shows a stable carrier and reproducible decay across averages, then run a longer/higher-resolution Ramsey specifically for the `~0.385 MHz` 13C sideband question.
