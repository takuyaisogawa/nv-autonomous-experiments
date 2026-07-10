# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey measurement:
  - `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: submitted Ramsey job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: terminal control.
- Prior/context evidence was used through the compact state: accepted r03, fine weak-pi pODMR grid center `mw_freq_hz = 3.8759e9`, planned Ramsey `det = 1.0 MHz`, expected 13C sidebands near `0.615/1.385 MHz`, and prior non-claim-grade `~0.884 MHz` Ramsey component.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis.png`
- The script loaded only `measurement/m001.json`, interpreted readout 1 as the `m_S=0` reference and readout 2 as the Ramsey signal from the embedded `ramsey.xml` (`full_experiment = 0` disables the optional `m_S=1` reference).
- Checks performed:
  - Raw reference/signal summaries.
  - Signal/reference ratio and reference-line-normalized signal.
  - Linear detrending before FFT/least-squares spectral checks.
  - FFT ranking and fixed-frequency least-squares sinusoid checks at `0.615 MHz`, `0.884 MHz`, `1.000 MHz`, and `1.385 MHz`.
  - Exploratory frequency search over `0.2..2.0 MHz`.
  - Per-average signal/reference means and per-average carrier amplitudes.
  - Simple drift/common-mode checks from stored averages.
  - Trial damped-sinusoid fits; these were not promoted because they hit bounds or were not shape-stable.

Key quantitative results:

- Run completed cleanly: `2026-05-13T20:49:36` to `22:17:11`, final counts `44.184 kcps`, 8 averages x 50000 repetitions, tau `0..8 us` in 41 points, saved scan tracking `Per average`.
- Sampling: `dt = 0.2 us`, Nyquist `2.5 MHz`, nominal span resolution `125 kHz`; rFFT bin spacing from the 41-point transform is `121.95 kHz`.
- Combined raw readouts: reference mean `49.31`, signal mean `44.58`, signal peak-to-peak `7.72` readout units (`17.3%` of signal mean), signal linear slope about `0.17` readout units/us.
- FFT, raw signal detrended: strongest bins at `1.2195 MHz` (`0.797` amplitude), `1.0976 MHz` (`0.764`), and `0.4878 MHz` (`0.640`).
- FFT, signal/reference detrended: strongest bins at `1.0976 MHz` (`0.0211` ratio amplitude), `1.2195 MHz` (`0.0188`), and `0.9756 MHz` (`0.0133`).
- Fixed exact `1.000 MHz` sinusoid is weak: raw amplitude `0.277`, partial `R2 = 0.024`, `p ~ 0.63`; ratio amplitude `0.00916`, partial `R2 = 0.050`, `p ~ 0.39`.
- Exploratory best signal/reference sinusoid is near `1.175 MHz`: amplitude `0.0225` ratio units, partial `R2 ~ 0.305`, nominal `p ~ 0.0012` before accounting for frequency-search/multiple-testing selection. Raw signal at the same frequency gives amplitude `0.883`, partial `R2 ~ 0.248`, nominal `p ~ 0.0051`.
- Expected 13C sideband checks are weak:
  - `0.615 MHz`: ratio amplitude `0.0111`, partial `R2 ~ 0.071`, `p ~ 0.26`.
  - `1.385 MHz`: ratio amplitude `0.00843`, partial `R2 ~ 0.043`, `p ~ 0.45`.
- Prior `0.884 MHz` component is not supported here: ratio amplitude `0.00742`, partial `R2 ~ 0.032`, `p ~ 0.55`.
- Stored averages show large common-mode variation: per-average signal means range from `36.20` to `50.27`; first-half to second-half signal mean changes by `-5.17%`. Reference means vary similarly, so much of this is common-mode/count drift, but per-average oscillation amplitudes are not consistent enough to use as independent repeat proof.

## Plausible interpretation

- The run is valid and analyzable: it completed cleanly, final counts were healthy, and the saved raw data match the intended `auto__ramsey` tau scan.
- There is plausible Ramsey-like spectral content near `1.1..1.2 MHz` in both raw signal and reference-normalized views. This is closer to the programmed `1.0 MHz` detuned Ramsey carrier than the prior scout's `~0.884 MHz` component, and the prior `0.884 MHz` feature is not dominant in this run.
- The strongest exploratory component is not exactly at `1.0 MHz`; it is closer to `1.17 MHz`, and the exact `1.0 MHz` fixed-frequency fit is weak. That could reflect modest resonance-frequency mismatch, phase/timing convention details, leakage/windowing from a short record, or noise/drift structure. It should not be treated as a calibrated carrier without a det-tracking diagnostic.
- The expected 13C sidebands near `0.615/1.385 MHz` are not supported by these checks. This is evidence against a claim of resolved nearby 13C coupling in this Ramsey record, but not a definitive absence statement.
- The data do not support a robust T2star extraction. Damped-sinusoid fits are unstable and/or hit bounds, and the trace shape includes baseline/common-mode variation that is comparable to the oscillatory features.

## Claims not yet supported

- No well-supported numerical T2star claim.
- No well-supported nearby 13C claim.
- No claim that the `~1.17 MHz` component is the true physical Ramsey carrier; it is an exploratory feature until it is shown to track programmed detuning or is reproduced under a cleaner protocol.
- No claim that the prior `~0.884 MHz` component was physical; this run does not reproduce it as a dominant component.
- No definitive no-13C conclusion; this single non-claim-grade Ramsey record only says the expected sidebands are not resolved here.

## Recommended next action

Do not blindly repeat the same higher-shot Ramsey for T2star yet. First run a targeted detuning diagnostic or equivalent bridge-free sequence/model review to determine whether the `~1.17 MHz` feature tracks programmed Ramsey detuning. A practical experiment would keep r03 and the fine-pODMR `mw_freq = 3.8759 GHz`, then acquire a short matched Ramsey pair at two detunings bracketing this case, for example `det = 0.5 MHz` and `det = 1.5 MHz`, with the same tau span/resolution and enough averages for a clear FFT comparison. If the feature shifts with det, then design a higher-SNR T2star acquisition around the confirmed carrier. If it does not shift, treat it as artifact/noise/baseline structure and move to an alternate sequence or close the Ramsey-based 13C branch as unsupported.
