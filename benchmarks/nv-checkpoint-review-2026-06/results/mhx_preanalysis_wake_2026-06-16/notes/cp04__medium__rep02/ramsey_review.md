# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md` for the project objective, accepted r03 context, and interpretation rules.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: job spec/result/status/control for `nv23_ramsey_20260514_015423_auto_ramsey`.
- `evidence/e008.json`, `evidence/e019.json`, `evidence/e021.json`: prior det=1.0 short-tau terminal summary and det-shift model/intent.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs:
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_trace.png` (generated, but not visually inspected because local image viewing returned an access error)
- Checks performed:
  - Parsed raw reference/signal readouts and 12 stored averages over 41 tau points.
  - Verified tau grid: 0.048 to 1.968 us, 48 ns step, Nyquist about 10.42 MHz.
  - Computed raw signal, signal/reference ratio, and signal divided by a fitted reference line.
  - Computed per-point SEM across stored averages: median signal SEM 0.711 kcps; median ratio SEM 0.0126.
  - Robust per-average mean drift screen found no >3 robust-z flags in signal, reference, or ratio.
  - Ran least-squares sinusoid screens with linear baseline terms and FFT checks.
  - Compared target frequencies: fixed prior feature 1.192 MHz, programmed carrier 1.500 MHz, det-tracking prediction 1.692 MHz, and approximate 13C sidebands 1.307/2.077 MHz.

## Plausible interpretation

- The measurement completed cleanly: 12 x 90000 repetitions, final count text 44.796 kcps, no stop request, no bridge error, and no simple per-average drift flags.
- The unrestricted LS screen is dominated by a large slow early-time component near the low-frequency edge of the search. This argues against treating the full trace as a clean Ramsey decay fit.
- In the physically relevant 1.2-2.2 MHz band, the strongest combined ratio components are around 1.62-1.67 MHz; the explicit 1.692 MHz det-tracking target has ratio amplitude 0.0250 and raw-signal amplitude 1.225 kcps.
- The old fixed 1.192 MHz component is weak in the combined ratio view: ratio amplitude 0.00511 and raw-signal amplitude 0.474 kcps.
- The programmed 1.500 MHz target is comparable to the det-tracking target: ratio amplitude 0.0240 and raw-signal amplitude 1.128 kcps.
- Per-average restricted-band ratio peaks are not locked to a single frequency, but most lie in the 1.5-1.8 MHz neighborhood. This supports a plausible det-shift response relative to the previous det=1.0 run, but not a clean claim-grade model.
- 13C sideband support remains weak: target amplitudes at 1.307 and 2.077 MHz are much smaller than the carrier/det-tracking neighborhood and do not form a clear symmetric sideband pattern.

## Claims not yet supported

- Do not claim a numeric T2star from this run. The low-frequency transient/baseline structure and mixed per-average frequency peaks make a decay fit descriptive at best.
- Do not claim nearby 13C coupling. The expected sideband frequencies are not dominant or consistently supported across raw/readout-aware views.
- Do not claim that the exact Ramsey carrier is 1.692 MHz. The result is consistent with det-shifting away from the prior fixed 1.192 MHz feature, but the 1.5-1.7 MHz band is broad and not uniquely resolved.
- Do not revise the accepted aligned-NV claim; this run does not invalidate r03 alignment evidence from pODMR.

## Recommended next action

- Stop blind Ramsey repeats on r03. The det-shift diagnostic gives useful evidence that the prior 1.19 MHz feature is not simply fixed, but it still does not yield a clean T2star/13C conclusion.
- Recommended next action: use an alternate protocol or analysis route aimed at separating baseline/transient behavior from coherent phase evolution before any further T2star/13C claim. A Hahn echo or another controlled phase/reference Ramsey variant would be more informative than another same-style short-tau repeat.
