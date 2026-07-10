# Ramsey Review: det-shift short-tau r03 run

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`, and `context.json`.
- New measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` run control.
- Prior comparison point from project state/evidence: previous short-tau det=1.0 MHz run had an empirical ratio-screen component near 1.192 MHz, with no supported T2star or 13C claim.

## Calculations or scripts run

- Ran local Python analysis against `measurement/m001.json`.
- Wrote scratch outputs:
  - `analysis/ramsey_detshift_analysis.json`
  - `analysis/ramsey_detshift_analysis.png`
  - `analysis/ramsey_detshift_skip_screens.json`
- Checks performed:
  - Confirmed terminal run metadata: job `nv23_ramsey_20260514_015423_auto_ramsey`, run `1DExp-seq-ramsey-vary-tau-2026-05-14-015440`, status `completed`, `12` averages x `90000` repetitions, `tau=0.048..1.968 us` in `41` points, programmed `det=1.5 MHz`, final count text `44.796 kcps`, no stop request, safe shutdown OK.
  - Used readout1 as reference and readout2 as Ramsey signal, consistent with prior `full_experiment=0` Ramsey context.
  - Computed signal/reference ratio, per-point SEM from stored averages, reference-line normalization, snake-direction rough consistency, least-squares sinusoid screens, FFT screen, and skip-early-point frequency screens.

## Quantitative results

- Mean signal/readout2: `44.27 kcps`; mean reference/readout1: `48.08 kcps`.
- Median SEM across averages: signal `0.711 kcps`; ratio `0.0126`.
- Ratio range over tau: `0.8429..0.9773`, peak-to-peak `0.1344`.
- Reference line slope was small relative to signal structure: `0.423 kcps/us`, fitted span `0.811 kcps` over the window.
- Rough scan-order check: snake odd/even direction RMS ratio difference `0.0231`; average-mean MAD check flagged no individual average.
- Full-window ratio LS screen:
  - Best RSS frequency: `1.623 MHz`, amplitude `0.0255`.
  - Prior empirical control `1.192 MHz`: amplitude `0.0051`, weak.
  - Programmed det `1.500 MHz`: amplitude `0.0240`.
  - Det-tracking prediction `1.692 MHz`: amplitude `0.0250`, lowest target RSS among checked targets.
  - Putative sidebands `1.307/2.076 MHz`: amplitudes `0.0095/0.0062`, weak.
- FFT of detrended ratio has coarse peaks at about `0.508`, `1.524`, `2.033`, and `1.016 MHz`; the bin spacing is coarse for this short window, so this is only a sanity check.
- Skip-early-point LS screens do not give a stable physical frequency: after skipping 2 points, best RSS is `1.659 MHz`; after skipping 4 to 10 points, best RSS moves toward lower frequencies or about `1.057 MHz`. This makes the det-tracking indication suggestive but not robust.
- A descriptive damped-ratio fit converged to `0.679 MHz`, `T2star ~0.47 us`, amplitude `0.140`, but it is dominated by early transient/shape freedom and should not be promoted as a physical T2star.

## Plausible interpretation

The new det=1.5 MHz short-tau run is analyzable and healthy. It does weaken the fixed-artifact hypothesis for the exact old `~1.192 MHz` feature because the full-window ratio screen now has little amplitude at 1.192 MHz and stronger structure near the programmed/det-tracking region (`1.5..1.7 MHz`).

However, the evidence is still not claim-grade. The apparent frequency depends on preprocessing and early-point inclusion, the strongest very-low-frequency/transient structure remains important, per-average frequency screens are not coherent enough, and the damped fit is not physically stable. The data are consistent with "some det-region Ramsey-like structure may be present," but not with a well-supported carrier/decay/13C model.

## Claims not yet supported

- No supported numeric T2star for r03 from this run.
- No supported nearby 13C conclusion from the Ramsey FFT/LS checks.
- No supported claim that the carrier cleanly tracks from the prior `~1.192 MHz` component to `~1.692 MHz`; the full-window screen is suggestive, but skip-window robustness is insufficient.
- No supported claim that the descriptive `0.679 MHz`, `T2star ~0.47 us` damped fit is a physical parameter.

## Recommended next action

Do not run another blind Ramsey repeat. Synthesize all four r03 Ramsey datasets into a branch-level conclusion: aligned NV remains supported, while T2star/13C remain unsupported under the Ramsey conditions tried. If the project still requires a positive T2star/13C attempt on this NV, switch protocol or measurement design rather than accumulating another same-family short-tau Ramsey repeat; otherwise close the r03 Ramsey/13C branch as unsupported under current conditions.
