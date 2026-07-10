# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior Ramsey context: `evidence/e008.json` terminal det=1.0 MHz short-tau review, plus associated prior files noted in `project/state.md`.
- New terminal Ramsey measurement:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: bridge job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: control state.

## Calculations/Scripts Run

- Created and ran `analyze_current_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_det1p5_review.png`
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract as `[scan, avg, readout, point]` by reconstructing `ExperimentData`.
  - Parsed scan conditions: `tau = 0.048..1.968 us`, 41 points, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`, 12 averages x 90000 repetitions = 1.08e6 shots/tau, Nyquist about 10.42 MHz.
  - Confirmed terminal health: completed, final `44.796 kcps`, no monitor error, no stop request, safe shutdown OK.
  - Computed raw reference/signal, point-wise signal/reference ratio, signal over fitted-reference-line, SEM across stored averages, FFT of detrended ratio, and least-squares sinusoid screens.
  - Ran target LS checks at: programmed 1.5 MHz; prior fixed feature 1.192 MHz; det-tracking prediction 1.692 MHz; tracking-sideband predictions 1.307 and 2.077 MHz; programmed-det sidebands 1.115 and 1.885 MHz.
  - Ran a local acquisition-order common-mode drift proxy using `Scan.ScanOrderEachAvg`; no average crossed the 15% drop threshold.
  - Verified the generated PNG structurally with PIL after the image viewer reported local access denial: PNG, 1800 x 2250, nonblank channel extrema.

## Key Quantitative Results

- Median point SEM: `0.711 kcps` signal and `0.0126` ratio.
- Early `tau <= 0.75 us` structure: `6.46 kcps` raw-signal peak-to-peak and `0.134` ratio peak-to-peak, so structure is large relative to SEM.
- All-tau ratio LS screen top: `1.623 MHz`, ratio amplitude `0.02547`, linear-baseline R2 improvement `0.430`.
- Programmed carrier `1.5 MHz`: ratio amplitude `0.02399`, R2 improvement `0.359`.
- Prior feature fixed at `1.192 MHz`: ratio amplitude `0.00511`, R2 improvement `0.0167`.
- Prior feature det-tracking prediction `1.692 MHz`: ratio amplitude `0.02505`, R2 improvement `0.411`.
- Tracking-sideband predictions are weak/non-dominant: `1.307 MHz` amplitude `0.00953`; `2.077 MHz` amplitude `0.00614`.
- Programmed-det sidebands are also not decisive: `1.115 MHz` amplitude `0.01076`; `1.885 MHz` amplitude `0.01732`.
- Descriptive damped-sinusoid ratio fit preferred `0.678 MHz`, `T2* ~0.469 us`, but this is model-dependent and not aligned with the intended carrier/sideband test.

## Plausible Interpretation

The det=1.5 MHz shift-check Ramsey is terminal, analyzable evidence with real short-tau structure. It does not support the prior `~1.192 MHz` component as a fixed artifact because that exact frequency is weak in this run. However, it also does not cleanly support a det-following Ramsey carrier: the strongest all-tau ratio screen is near `1.623 MHz`, while the non-blind det-tracking prediction was `~1.692 MHz` and the programmed carrier was `1.5 MHz`. The structure is broad/model-sensitive over this short window and changes substantially when early tau points are skipped, so it should be treated as an empirical transient rather than a claim-grade Ramsey carrier.

## Claims Not Yet Supported

- A numeric `T2*` for r03 from these Ramsey datasets.
- Nearby `13C` coupling from the Ramsey FFT/LS screens.
- The prior `~1.19 MHz` component as a clean det-following physical Ramsey carrier.
- A clean programmed-carrier Ramsey response at `1.5 MHz`.
- Any sub-grid or fit-derived physical parameter from the descriptive damped-sinusoid fits.

## Recommended Next Action

Stop blind Ramsey repeats on r03. Do a branch-level synthesis/closeout from all r03 Ramsey attempts: either report the aligned r03 as having unsupported Ramsey/T2*/13C conclusions under current Ramsey conditions, or switch deliberately to an alternate protocol such as Hahn/CPMG or phase-readout 13C spectroscopy after fresh tracking/resonance checks. If another experiment is considered, it should test a specific protocol/model failure mode rather than repeating short-tau Ramsey accumulation.
