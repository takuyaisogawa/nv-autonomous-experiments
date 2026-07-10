# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- New measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- Run/job metadata: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Prior interpretation used from local context only: accepted r03 NV, fine pODMR center `mw_freq = 3.8759 GHz`, prior short-tau Ramsey empirical component near `1.192 MHz`, and det-shift prediction that a physical carrier-like component should move by about `+0.5 MHz`.
- Generated scratch artifacts: `analysis_ramsey_detshift_summary.json`, `ramsey_detshift_analysis.png`. An initial scratch script file `analyze_ramsey_detshift.py` was also created, but the final successful calculation was run directly in Python after a plotting-backend failure.

## Calculations/scripts run

- Parsed `ExperimentData` as two combined channels with shape `[2, 41]` and `ExperimentDataEachAvg` as `[12, 2, 41]`.
- Confirmed run completion from `measurement/m003.json`: job `nv23_ramsey_20260514_015423_auto_ramsey`, completed `2026-05-14T04:15:00`, final counts `44.796 kcps`, `tau = 0.048..1.968 us` in `0.048 us` steps, `12` averages, `90000` repetitions.
- Computed raw signal/reference ratio and per-average SEM across stored averages. Combined signal mean was `48.084 kcps`, signal peak-to-peak was `2.400 kcps`, median signal SEM across averages was `0.745 kcps`. Ratio mean was `1.0872`, ratio peak-to-peak was `0.1632`, median ratio SEM was `0.0146`.
- Ran least-squares screens with model `offset + linear trend + cos(2*pi*f*tau) + sin(2*pi*f*tau)`.
  - Broad `0.25..4.0 MHz` ratio screen was dominated by the low-frequency bound (`0.25 MHz`, ratio amplitude `0.216`), consistent with endpoint/baseline curvature rather than a claim-grade Ramsey carrier.
  - Restricted relevant-band screens:
    - `0.7..3.0 MHz`: best `0.858 MHz`, ratio amplitude `0.0318`, raw signal amplitude `0.400 kcps`.
    - `1.0..2.5 MHz`: best `1.614 MHz`, ratio amplitude `0.0303`, raw signal amplitude `0.054 kcps`.
    - `1.2..2.2 MHz`: best `1.614 MHz`, ratio amplitude `0.0303`, raw signal amplitude `0.054 kcps`.
- Checked planned frequencies:
  - Programmed `1.500 MHz`: ratio amplitude `0.0286`, raw signal amplitude `0.037 kcps`.
  - Det-tracking-from-prior `1.692 MHz`: ratio amplitude `0.0298`, raw signal amplitude `0.099 kcps`.
  - Prior fixed `1.192 MHz`: ratio amplitude `0.00594`, raw signal amplitude `0.294 kcps`.
  - Expected sidebands `1.307/2.076 MHz`: ratio amplitudes `0.0113/0.00681`, raw signal amplitudes `0.222/0.174 kcps`.
- FFT sanity on detrended/windowed ratio had top coarse bins at `0.508`, `1.524`, `2.033`, and `1.016 MHz`; bin spacing is coarse for this short time window, so this is only a sanity check.
- Drift proxy from per-average signal/reference means found no average with absolute robust-z above 3. Average common-mode fraction ranged from about `-9.5%` to `+4.0%`, with no hard drift flag by this simple check.

## Plausible interpretation

- The measurement is complete and analyzable, with adequate final counts and no bridge-level stop/abort anomaly.
- The prior fixed `~1.192 MHz` component is not reproduced strongly in this det=1.5 MHz run, which argues against treating that exact feature as a stable instrument/baseline line.
- The relevant-band ratio screen has power near `1.5..1.7 MHz`, close to the programmed-det/det-tracking region, but the evidence is weak: the `1.500` and `1.692 MHz` ratio amplitudes are similar, the raw signal amplitudes at those frequencies are far below the measured per-point signal SEM, and per-average best frequencies are scattered.
- The high ratio peak-to-peak and low-frequency-bound LS maximum suggest baseline/reference structure remains important. The ratio-only feature is not enough to support a T2star fit.
- There is no supported 13C sideband pattern: neither expected sideband is strong or paired in a way that supports a carrier-plus-sidebands interpretation.

## Claims not yet supported

- No well-supported numeric T2star claim from this run.
- No claim of nearby 13C coupling from this run.
- No claim that the `~1.192 MHz` prior feature was a true Ramsey carrier.
- No claim that the new `~1.6 MHz` relevant-band ratio component is a physical det-tracking Ramsey carrier; it is at most a weak, non-claim-grade hint.

## Recommended next action

Stop blind Ramsey repeats on this r03 configuration. Use the accumulated local evidence to make a branch decision: either switch to an alternate T2star/13C protocol or close r03 Ramsey/T2star/13C as unsupported under current conditions. If continuing experimentally, first run a control/diagnostic aimed at separating reference-normalization/baseline effects from real NV phase evolution, because the present limiting issue is not just shot count.
