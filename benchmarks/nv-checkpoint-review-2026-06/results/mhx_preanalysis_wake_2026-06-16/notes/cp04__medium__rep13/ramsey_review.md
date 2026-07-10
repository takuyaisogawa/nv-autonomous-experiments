# Ramsey Review: r03 det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md`.
- New completed Ramsey data: `measurement/m001.json` raw export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- New job/provenance files: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison data: `evidence/e001.json` and prior review context in `evidence/e008.json` for the preceding det=1.0 MHz short-tau Ramsey run.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs created: `ramsey_detshift_analysis.json` and `ramsey_detshift_analysis.png`.
- Checks performed:
  - Parsed raw reference/readout1 and Ramsey signal/readout2 arrays from the combined and per-average data.
  - Verified acquisition context: `tau = 0.048..1.968 us`, 41 points, 12 averages x 90000 repetitions = `1.08e6` shots per tau point, snake scan order, programmed `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`.
  - Checked terminal job health: completed, final counts `44.796 kcps`, safe shutdown true, no error code/message.
  - Computed raw signal/reference, signal divided by fitted reference line, linear-baseline residuals, per-point SEM across stored averages, FFT screens, and least-squares sinusoid screens.
  - Compared targets: programmed `1.5 MHz`, prior fixed-control `1.192 MHz`, det-tracking prediction `1.692 MHz`, det-tracking 13C sidebands near `1.307/2.077 MHz`, and programmed-det 13C sidebands near `1.115/1.885 MHz`.

## Key quantitative results

- New data quality/provenance:
  - Raw reference mean `48.084 kcps`; raw Ramsey signal mean `44.269 kcps`.
  - Median per-point signal SEM `0.711 kcps`; median per-point ratio SEM `0.0126`.
  - Raw signal linear-residual peak-to-peak `6.289 kcps`; ratio linear-residual peak-to-peak `0.133`.
  - Stored-average signal/reference means are strongly common-mode correlated (`r = 0.900`), so normalization artifacts remain a concern.
- Frequency screens:
  - Full-window point-wise ratio LS screen peaks near `1.623 MHz` with ratio amplitude `0.0255` and baseline-residual R2 improvement `0.430`.
  - Raw signal and signal/reference-line LS screens peak near `0.882 MHz`, with raw-signal amplitude `1.53 kcps` and R2 improvement `0.577`.
  - Skipping `tau <= 0.2 us` shifts the top screens lower: ratio near `0.746 MHz`, raw signal/reference-line near `0.805 MHz`.
  - The prior fixed-control `1.192 MHz` component is weak in the new data: ratio amplitude `0.0051`, R2 improvement `0.017`.
  - The programmed `1.5 MHz` target is present only as a modest component: ratio amplitude `0.0240`, R2 improvement `0.359`; raw-signal amplitude `1.13 kcps`.
  - The det-tracking prediction `1.692 MHz` is also modest and not uniquely dominant: ratio amplitude `0.0250`, R2 improvement `0.411`; raw-signal amplitude `1.22 kcps`.
  - Det-tracking sidebands near `1.307/2.077 MHz` are weak: ratio amplitudes `0.0095/0.0061`.
  - Per-average top frequencies are inconsistent across raw, ratio, and reference-line views; they do not provide repeatable support for a single carrier/sideband model.

## Plausible interpretation

- The det=1.5 MHz shift-check is analyzable and not obviously failed.
- The old det=1.0 short-tau `~1.19 MHz` feature does not persist as a fixed-frequency dominant feature in the new run, which argues against simply promoting that old component as a stable physical Ramsey frequency.
- However, the new run also does not cleanly support the intended det-tracking hypothesis. The point-wise ratio screen leans toward `~1.62 MHz`, close-ish to but not identical with the `~1.692 MHz` prediction, while raw-signal and fitted-reference-line views are dominated near `~0.88 MHz` or `~0.80 MHz` depending on early-time exclusion.
- Because the strongest views disagree and the target components are near the measured per-point uncertainty scale, this remains non-claim-grade Ramsey evidence.

## Claims that are not yet supported

- No supported numeric T2star value from this dataset.
- No supported nearby 13C conclusion from Ramsey/FFT sidebands.
- No supported claim that the Ramsey carrier follows the programmed detuning.
- No supported claim that the `~0.88 MHz`, `~1.62 MHz`, or `~1.69 MHz` features are physical rather than baseline/readout/normalization/early-time artifacts.

## Recommended next action

- Do not run another blind Ramsey repeat on the same settings.
- Treat r03 as still aligned by pODMR, but Ramsey/T2star/13C remains unresolved under the current Ramsey route.
- Next decision should be a branch choice rather than more accumulation: either switch to an alternate protocol/readout strategy for T2star/13C, or close the r03 Ramsey branch with a supported statement that the current Ramsey protocol did not yield claim-grade T2star or 13C evidence.
