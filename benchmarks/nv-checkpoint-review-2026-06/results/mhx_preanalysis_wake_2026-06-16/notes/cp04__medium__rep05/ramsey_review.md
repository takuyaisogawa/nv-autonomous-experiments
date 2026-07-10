# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: objective and current r03 Ramsey context.
- `md/memory.md`: local review rules for raw/readout-aware Ramsey interpretation, contrast/noise caution, and fit discipline.
- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: submitted job contract.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control for `nv23_ramsey_20260514_015423_auto_ramsey`.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_detshift_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed combined readouts with shape `2 x 41` and per-average readouts with shape `12 x 2 x 41`.
- Confirmed scan settings: `tau = 48 ns..1.968 us`, `48 ns` step, `41` points, `12` averages, `90000` repetitions, snake scan order, tracking per average, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`.
- Computed raw signal/reference, point-wise `signal/reference`, and `signal/reference-line` views.
- Estimated per-point SEM from stored averages: median signal SEM `0.711 kcps`, median reference SEM `0.745 kcps`.
- Ran detrended FFT peak checks and linear least-squares sinusoid screens over `0.2..3.0 MHz`.
- Directly tested the programmed det carrier `1.500 MHz`, predicted det-shifted prior component `1.692 MHz`, prior short-tau component `1.192 MHz`, and predicted det-tracking 13C sidebands near `1.307/2.076 MHz`.

## Plausible interpretation

- The prior `~1.192 MHz` short-tau component is not reproduced as the dominant component after changing `det` to `1.5 MHz`. Direct LS checks at `1.192 MHz` are weak: raw-signal amplitude `0.474 kcps`, `R2 = 0.105`; point-ratio amplitude `0.0051`, `R2 = 0.019`.
- There is some evidence in normalized views for power near the expected det-shift region: point-ratio best LS frequency is `1.624 MHz` with amplitude `0.0255` and `R2 = 0.432`; direct `1.692 MHz` gives amplitude `0.0250` and `R2 = 0.412`. The programmed `1.500 MHz` test is nearby but weaker (`R2 = 0.361` in point ratio).
- This is not clean claim-grade det tracking. The raw signal and signal/reference-line screens are still dominated by `0.882 MHz`, and the raw reference also has a nearby low-frequency best component (`0.924 MHz`). That makes baseline/reference structure a plausible contributor.
- The direct sideband checks at `1.307/2.076 MHz` are weak in all views. The current dataset does not support a nearby-13C sideband assignment.
- Stored-average frequency screens are inconsistent; point-ratio best frequencies scatter across averages rather than locking to one carrier. Average means show common-mode intensity variation, with signal-average mean range `7.28 kcps` and reference-average mean range `6.01 kcps`; average ratio range is about `7.0%` of its median.

## Claims not yet supported

- No supported numeric `T2star` should be claimed from this run.
- No supported nearby-`13C` conclusion should be claimed from this run.
- Do not claim a clean programmed `1.5 MHz` Ramsey carrier.
- Do not claim that the earlier `~1.192 MHz` component is physical; this run argues against simply promoting it, but does not prove the replacement component is physical.
- Do not infer sub-grid resonance precision beyond the prior fine pODMR-supported `3.8759 GHz` working frequency.

## Recommended next action

Stop blind Ramsey repeats on r03 under this sequence/short-tau pattern. The det-shift diagnostic weakens the fixed `~1.192 MHz` artifact hypothesis but still leaves the carrier/sideband model unsupported. Next, choose an alternate protocol or close r03 Ramsey/T2star/13C as unsupported under current conditions. If continuing experimentally, use a non-blind protocol change aimed at resolving the ambiguity rather than more accumulation: for example, an echo/DD-style or phase/quadrature Ramsey diagnostic that can separate real det-dependent phase accumulation from readout/reference baseline structure.
