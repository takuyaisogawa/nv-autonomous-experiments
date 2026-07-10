# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior Ramsey context: `evidence/e003.json` terminal det=1.0 MHz 8 us review, `evidence/e006.json` short-tau design/advisory, `evidence/e017.md` short-tau start note.
- New terminal measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- New run identity: `nv23_ramsey_20260513_230331_auto_ramsey`, saved experiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`, status `completed`, finished `2026-05-14T01:23:47`.
- Terminal post-run final-count text is `Final = 35.122 kcps`. The `44.184 kcps` value in job/result metadata is stale context from the previous Ramsey, not this run's terminal final count.

## Calculations/scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json`, `ramsey_shorttau_review.png`, `analysis_output.txt`.
- First plotting attempt hit a local Tk backend error; script was changed to matplotlib `Agg` and rerun successfully.
- Readout roles used from local protocol notes: trace 0 = reference/readout1, trace 1 = Ramsey signal/readout2.
- Measurement geometry: tau `0.048..1.968 us`, `48 ns` step, `41` points, `12 x 90000` repetitions = `1.08e6` shots per tau point.
- Signal/reference checks:
  - Reference mean `48.573 kcps`; signal mean `44.655 kcps`.
  - Median per-point SEM: reference `1.455 kcps`, signal `1.397 kcps`.
  - Signal/reference ratio mean `0.9195`, ratio std over tau `0.0348`, propagated median ratio SEM estimate `0.0400`.
  - Signal peak-to-peak is `5.691 kcps` over the first `0.75 us` and `6.499 kcps` over the full short window.
- Target-frequency least-squares screens after a linear baseline:
  - Programmed carrier `1.000 MHz`: ratio amplitude `0.0274`, raw signal amplitude `1.282 kcps`, residual improvement `0.355` ratio / `0.377` signal.
  - Expected low 13C sideband `0.615 MHz`: ratio amplitude `0.0243`, raw signal amplitude `1.102 kcps`.
  - Expected high 13C sideband `1.385 MHz`: ratio amplitude `0.0271`, raw signal amplitude `1.222 kcps`.
  - Broad screen peak: ratio near `1.192 MHz` with amplitude `0.0363`; raw signal near `1.187 MHz` with amplitude `1.683 kcps`.
- FFT sanity check:
  - Short-window FFT bin spacing is coarse, `0.508 MHz`.
  - Largest ratio FFT bins: `0.508 MHz` amplitude `0.0335`, `1.016 MHz` amplitude `0.0261`, `1.524 MHz` amplitude `0.0180`.
- Diagnostic damped-cosine fit to ratio:
  - Free frequency fit converges near `1.198 MHz`, amplitude `0.0417 +/- 0.0097`.
  - Fitted decay `T2* = 6.29 +/- 9.61 us`, which is longer than and poorly constrained by the `1.92 us` window. This is not a supported T2* estimate.
- Per-average checks:
  - Reference and signal mean levels vary strongly across averages, about `27%` and `31%` span respectively.
  - Ratio mean varies less, about `6.8%` span.
  - Per-average broad-screen top frequencies are not consistent enough for a frequency claim.

## Plausible interpretation

- The new short-tau/high-SNR Ramsey run completed safely and produced analyzable terminal raw data.
- Unlike the prior 8 us Ramsey, this short-window run shows a real early-time signal structure: a low initial signal, crests around `0.67 us` and `1.30..1.34 us`, and a later fall. A Ramsey-like transient near roughly `1.2 MHz` is plausible.
- The run supports the idea that the earlier long-window data may have missed or diluted an early-time oscillatory feature.
- It does not yet establish a physical carrier/sideband model. The programmed `1.0 MHz` carrier, the expected `0.615/1.385 MHz` 13C sidebands, and the broad-screen `~1.19 MHz` component are too close in explanatory power for this short span, and the FFT resolution is intentionally poor for 13C.
- Common-mode brightness drift across averages is substantial, although the ratio is more stable. That makes raw/readout-aware and det-shift confirmation important before promoting the feature.

## Claims not yet supported

- No numeric T2* claim is supported. The diagnostic fit's decay is unconstrained relative to the measurement window.
- No nearby 13C claim is supported. The short span cannot resolve sidebands well enough, and the sideband targets are not dominant or consistent.
- Do not claim that the `~1.19 MHz` component is the programmed carrier, a 13C sideband, or a stable physical line yet.
- Do not use the stale `44.184 kcps` metadata field as the terminal final count for this run.
- Do not treat this as closeout evidence for r03 without a det-following check or an alternate protocol decision.

## Recommended next action

Run a deliberate det-shift short-tau/high-SNR Ramsey diagnostic on the same r03, after normal advisory and queue checks. A good test would keep the same tau grid and shot scale but change the programmed detuning, for example to `1.5 MHz`, then ask whether the early-time component shifts by the programmed det change. If it follows detuning, plan a longer high-SNR Ramsey with enough span/resolution for T2* and 13C. If it does not, stop blind Ramsey repeats on r03 and move to an alternate diagnostic or mark T2*/13C unsupported under current conditions.
