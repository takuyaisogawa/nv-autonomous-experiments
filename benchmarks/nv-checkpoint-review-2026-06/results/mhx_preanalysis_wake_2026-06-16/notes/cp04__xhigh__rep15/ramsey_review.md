# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New Ramsey data and terminal metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json` and `measurement/m005.json`: terminal status/control snapshots.
- Prior comparison context:
  - `evidence/e008.json`: terminal det=1.0 MHz short-tau Ramsey review.
  - `evidence/e019.json` and `evidence/e021.json`: det-shift model/intent and comparison targets.
  - `evidence/e009.py`: prior short-tau Ramsey review script pattern, used only as a reference for local checks.

## Calculations or scripts run

- Created and ran `analyze_ramsey_det1p5.py`.
- Output files:
  - `ramsey_det1p5_analysis.json`
  - `ramsey_det1p5_diagnostic.png`
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract by averaging per-average readouts back to `ExperimentData`.
  - Used `ramsey.xml`/job metadata readout roles: `full_experiment=0`, readout 1 is reference and readout 2 is Ramsey signal.
  - Computed signal/reference and signal/fitted-reference-line views.
  - Computed common-mode scan-order drift proxy from snake `ScanOrderInfo`.
  - Ran least-squares sinusoid screens over 0.25 to 2.5 MHz and at planned targets:
    - programmed carrier: 1.500 MHz
    - programmed 13C sidebands: 1.115 and 1.885 MHz
    - det-tracking carrier from prior 1.192 MHz feature: 1.692 MHz
    - det-tracking sidebands: 1.307 and 2.077 MHz
    - prior artifact-control frequency: 1.192 MHz
  - Computed detrended FFT checks. The 1.92 us span gives only about 0.521 MHz nominal resolution, so FFT bins are coarse.
  - Ran descriptive damped-sinusoid grid fits only as diagnostics.
- Mechanical plot verification: `PIL.Image.open("ramsey_det1p5_diagnostic.png")` reported a valid 1800 x 2250 PNG after the image viewer returned a local access-denied error.

## Plausible interpretation

- The run completed cleanly: status `completed`, final counts `44.796 kcps`, `12 x 90000` repetitions, `1.08e6` shots per tau point, safe shutdown OK, no stop request, and no monitor error.
- The tau grid was `48 ns..1.968 us` in 41 points with `48 ns` spacing; Nyquist is about `10.4 MHz`.
- The local scan-order drift proxy flagged no averages on common-mode trend; maximum common-mode drop score was `0.117`, below the `0.15` flag threshold. Single-signal-trace drops were larger but are shape-sensitive because the Ramsey transient itself is tau dependent.
- The data are analyzable, but they are not claim-grade for a Ramsey carrier model.
- The dominant feature remains an early-time transient: first `0.75 us` signal peak-to-peak is `6.46 kcps`, and ratio peak-to-peak is `0.134`, compared with median per-point SEM of `0.711 kcps` and `0.0126` ratio.
- The all-tau ratio LS screen peaks near `1.623 MHz` and the skip-first-point screen near `1.650 MHz`, which is in the neighborhood of the planned det-tracking `1.692 MHz` target. However, this does not by itself support a physical carrier:
  - programmed 1.500 MHz ratio amplitude: `0.02399`
  - det-tracking 1.692 MHz ratio amplitude: `0.02505`
  - all-tau ratio-screen top: `0.02547` near `1.623 MHz`
  - these are close to each other and only about 2x the median ratio SEM.
- Raw/readout-aware cross-checks do not agree with a clean det-tracking carrier:
  - raw signal LS screen peaks near `0.882 MHz`
  - signal/fitted-reference-line screen also peaks near `0.882 MHz`
  - ratio screen after skipping `tau <= 0.2 us` shifts to about `0.746 MHz`
  - per-average top frequencies are inconsistent.
- The prior `1.192 MHz` artifact-control component is not dominant in the combined ratio view here (`0.00511` ratio amplitude), but the replacement feature is still not robust enough to claim det tracking.
- Expected 13C sidebands are weak or inconsistent:
  - programmed-sideband ratio amplitudes: `0.01076` at 1.115 MHz and `0.01732` at 1.885 MHz
  - det-tracking-sideband ratio amplitudes: `0.00953` at 1.307 MHz and `0.00614` at 2.077 MHz
  - none is supported across raw, fitted-reference, skip-transient, and per-average views.
- Descriptive damped fits are not physically promotable:
  - ratio fit: `0.684 MHz`, `T2* ~0.482 us`
  - raw-signal fit: `0.818 MHz`, `T2* ~0.721 us`
  - these disagree with each other and with the det-tracking target, so they mainly describe the transient.

## Claims not yet supported

- A numeric T2star for r03 from Ramsey data.
- A nearby 13C coupling conclusion from these Ramsey FFT/LS screens.
- A clean physical Ramsey carrier at the programmed 1.500 MHz.
- A clean det-tracking physical carrier at 1.692 MHz.
- Absence of nearby 13C in an absolute sense. The supported statement is narrower: these Ramsey datasets do not support a 13C claim under the current conditions.

The prior aligned-NV conclusion for r03 remains supported by the pODMR evidence in project state; this review only concerns the completed det-shift Ramsey/T2star/13C question.

## Recommended next action

Do not run another blind or same-style Ramsey repeat. First do a bridge-free branch synthesis across the Ramsey datasets. If continuing r03 experimentally, switch to a targeted alternate protocol or control designed to separate early-time sequence/readout transients from true coherent precession before attempting a T2star or 13C claim. If no alternate protocol is justified, close this r03 Ramsey branch as "T2star/13C unsupported under current Ramsey conditions" rather than assigning a numeric T2star.
