# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, and prior design/start note `evidence/e017.md`.
- New terminal Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job/spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison/planning evidence: `evidence/e003.json` for the previous det=1.0 MHz 8 us terminal Ramsey review and readout-role basis, and `evidence/e006.json` for the short-tau plan/expected frequency targets.
- Scratch artifacts created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the terminal raw export as `tau = 0.048..1.968 us`, 41 points, 48 ns step, 12 averages x 90000 repetitions, total `1.08e6` shots per tau point.
- Used the prior protocol review basis for `full_experiment=0`: readout 1 is the true mS=0 reference and readout 2 is the Ramsey signal.
- Computed raw signal/reference summaries, signal/reference ratio, across-average SEM, scan-order-aware drift scores using the stored snake order, target least-squares sinusoid fits at 1.0 MHz, 0.615423 MHz, 1.384577 MHz, and the prior 0.884361 MHz component, exploratory single-frequency screens, FFT-bin checks, and an exploratory damped-sinusoid grid fit.
- Plot artifact was generated and sanity-checked as a nonblank PNG by file size/PIL metadata.

## Plausible interpretation

- The run completed cleanly: job `nv23_ramsey_20260513_230331_auto_ramsey`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`, status `completed`, no stop request, monitor error empty, safe shutdown ok, final count text `35.122 kcps`.
- No scan-order drift average was flagged. Max drop score was `0.060`, below the `0.15` threshold. Average-to-average common-mode brightness varied, but not as a monotonic within-average drop by the stored acquisition order check.
- Unlike the prior 8 us det=1.0 MHz Ramsey, this short-tau/high-SNR run shows credible early-time Ramsey-like signal presence. The programmed 1.0 MHz target has ratio LS amplitude `0.0274` and raw-signal amplitude `1.28 kcps`, versus median across-average SEM `0.0127` ratio and `1.14 kcps` raw signal. The early 0.75 us signal linear-residual peak-to-peak is `5.09 kcps`.
- The broad best single-frequency screen is near `1.19 MHz` with ratio amplitude `0.0363` and raw-signal amplitude `1.68 kcps`; FFT has a strong bin near `1.016 MHz` but also a low-frequency first bin at `0.508 MHz`. With only a `1.92 us` span, the nominal resolution is only about `0.521 MHz`, so the `1.0` vs `1.19 MHz` distinction should not be over-read.
- The exploratory damped ratio grid fit prefers about `1.21 MHz` and `T2* ~ 2.1 us`, with a rough near-optimal region around `1.175..1.24 MHz` and `T2* ~ 1.2..6.5 us`. This is useful as an order-of-magnitude pointer, not a claim-grade T2* result.
- The result supports the hypothesis that the previous long-window Ramsey failures were at least partly a window/SNR/baseline issue rather than complete absence of Ramsey contrast on r03.

## Claims not yet supported

- Do not claim a numeric T2* from this run. The span is short, the envelope is model-dependent, and there are only about two carrier cycles.
- Do not claim nearby 13C coupling or absence of 13C. The expected sidebands at `0.615` and `1.385 MHz` have target-fit amplitudes comparable to the carrier, but the short span cannot cleanly resolve sidebands separated by the expected `~0.385 MHz`; multi-frequency fits are not independent enough for a 13C conclusion.
- Do not claim a precise Ramsey carrier frequency of `1.19 MHz`; the frequency screen is broad at this tau span.
- Do not ignore position provenance: the saved scan position is `[117.345, 117.607, 116.053] um`, while the job metadata seed position is `[117.314, 117.762, 115.142] um`. This is not by itself a disqualifier because tracking/counts were acceptable, but it should be carried forward.

## Recommended next action

- Treat this as supported early-time Ramsey signal-presence evidence on accepted r03, but not as terminal T2*/13C evidence.
- Next, design and advisory-check a claim-grade follow-up rather than another blind repeat: keep tau0 excluded, keep the r03/fine-pODMR frequency basis, and extend the window enough to constrain the decay envelope while preserving higher per-point SNR under the tracking-window cap. A medium-span Ramsey should first target reproducible carrier plus envelope for T2*. Only after that should a longer/high-resolution Ramsey or alternate nuclear-sensitive protocol be used for a 13C conclusion.
