# Ramsey Review

Created: 2026-06-16

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey measurement:
  - `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: run control.
- Comparison/model context:
  - `evidence/e008.json`: prior det=1.0 MHz short-tau terminal review.
  - `evidence/e019.json`: det=1.5 MHz shift-check model plan and target frequencies.
- Generated local artifacts: `ramsey_analysis.py`, `ramsey_analysis_summary.json`, `ramsey_detshift_review.png`.

## Calculations/scripts run

- Ran `python ramsey_analysis.py`.
- The script:
  - verified `ExperimentDataEachAvg` reconstructs `ExperimentData` as `[scan, avg, readout, point]`;
  - used the saved tau grid `48 ns..1.968 us`, `41` points, `48 ns` step;
  - computed raw readout, signal/reference, and signal/fitted-reference-line views;
  - computed per-point SEM over `12` stored averages;
  - ran a local scan-order-aware drift proxy from per-average residual offsets;
  - ran fixed-frequency least-squares screens and nearest FFT-bin checks at the programmed carrier, programmed 13C sidebands, det-tracking predictions, and prior fixed-component control;
  - ran exploratory all-frequency LS screens for raw reference, raw signal, point-wise ratio, and fitted-reference normalization;
  - ran a descriptive damped-sinusoid grid fit, kept as diagnostic only.

Key quantitative checks:

- Run status: completed, no stop request, monitor `last_error` empty, final counts `44.796 kcps`.
- Acquisition: `12 x 90000 = 1.08e6` shots per tau point, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`.
- Noise/shape: median signal SEM `0.711 kcps`, median ratio SEM `0.0126`; first `0.75 us` peak-to-peak is `6.46 kcps` in raw signal and `0.134` in ratio.
- Local drift proxy: no average residual-offset flags; this is a local proxy, not the original MATLAB drift tool.
- Spectral/LS checks:
  - Point-wise ratio all-tau screen is strongest near `1.623 MHz`, ratio amplitude `0.0255`.
  - Raw signal all-tau screen is strongest near `0.882 MHz`, amplitude `1.53 kcps`.
  - Signal/fitted-reference-line screen is also strongest near `0.882 MHz`, amplitude `0.0319`.
  - Programmed carrier `1.5 MHz`: ratio amplitude `0.0240`, raw-signal amplitude `1.13 kcps`.
  - Det-tracking carrier prediction `1.692 MHz`: ratio amplitude `0.0250`, raw-signal amplitude `1.22 kcps`.
  - Prior fixed-component control `1.192 MHz`: ratio amplitude `0.0051`, raw-signal amplitude `0.474 kcps`.
  - Programmed 13C sidebands `1.115/1.885 MHz`: ratio amplitudes `0.0108/0.0173`.
  - Det-tracking 13C sidebands `1.307/2.077 MHz`: ratio amplitudes `0.0095/0.0061`.
  - FFT bin spacing is coarse at about `0.508 MHz`, so FFT alone cannot separate `1.5 MHz` from `1.692 MHz`.
- Descriptive damped-grid fits are view-dependent: ratio fit `0.674 MHz`, `T2star ~0.46 us`; raw-signal fit `0.820 MHz`, `T2star ~0.74 us`. These are not promoted.

## Plausible interpretation

The run is terminal, analyzable, and useful as a det-shift diagnostic. It argues against simply promoting the old fixed `~1.192 MHz` point-wise-ratio feature: that component is weak in the new run.

It still does not establish a clean det-tracking Ramsey carrier. The point-wise ratio has a strongest component near `1.62 MHz`, reasonably near the `~1.692 MHz` det-tracking prediction on this short frequency-resolution-limited window, but raw signal and signal/fitted-reference-line normalization are instead dominated near `0.88 MHz`. Per-average screens are inconsistent. The readout-aware views therefore do not support a physical carrier/sideband model strongly enough to fit or claim T2star.

The most plausible current interpretation is that r03 has repeatable tau-dependent structure under Ramsey, but the observed structure is mixed with early-time transient, readout/reference, baseline, or protocol effects. The det-shift result is not a clean fixed-artifact result, but it is also not claim-grade carrier tracking.

## Claims not yet supported

- A numeric T2star for r03.
- A nearby 13C coupling or resolved 13C sideband model.
- A clean det-tracking Ramsey carrier at `1.5 MHz` or `~1.692 MHz`.
- A definitive claim that all observed structure is an artifact.
- A physics-level negative conclusion that no nearby 13C exists; the supported statement is only that these Ramsey data do not establish one.

## Recommended next action

Do not run another blind same-grid Ramsey repeat. The next project action should be a branch synthesis across all Ramsey datasets and then a targeted alternate-control plan. If continuing hardware work, use a fresh resonance check first, then choose a control or alternate protocol that separates early-time/readout artifacts from true phase evolution before attempting another T2star or 13C claim.
