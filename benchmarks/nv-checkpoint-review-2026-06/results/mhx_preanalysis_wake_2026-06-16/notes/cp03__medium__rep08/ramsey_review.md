# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and short-tau design note `evidence/e017.md`.
- New measurement data/metadata: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` bridge job spec; `measurement/m003.json` terminal bridge result; `measurement/m004.json` terminal status; `measurement/m005.json` control state.
- Generated during review: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `analysis_output.txt`, and `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` on `measurement/m001.json`.
- Reconstructed tau from `vary_begin`, `vary_step_size`, and `vary_points`: 41 points, 0.048 to 1.968 us, median step 48 ns.
- Parsed combined readouts as reference and signal plus 12 stored averages. The terminal bridge result reports a normal completion of `nv23_ramsey_20260513_230331_auto_ramsey`, final count 35.122 kcps, 12 averages x 90000 repetitions, no abort, no stop request.
- Checked raw signal/reference levels, per-tau SEM across stored averages, fitted-reference-line normalization, scan-order-aware per-average start/end trends, broad frequency screens, and least-squares sinusoid projections at 1.000 MHz, 0.615 MHz, 1.385 MHz, and prior exploratory frequencies.

Key numerical results:

- Combined signal mean 44.655 kcps; reference mean 48.573 kcps.
- Signal span across tau 6.499 kcps; reference span 2.176 kcps.
- Median per-point signal SEM across averages 1.138 kcps; median ratio SEM 0.0127.
- Full frequency screen is dominated by very-low-frequency structure at the lower search bound, 0.1 MHz, not by the programmed carrier or 13C sidebands.
- Restricted 0.4 to 2.0 MHz screen peaks at the lower bound, 0.4 MHz: raw amplitude 1.853 kcps; ratio amplitude 0.0381. This is not a clean Ramsey carrier/sideband model.
- Target LS amplitudes with linear baseline:
  - 1.000 MHz carrier: raw 1.282 kcps, residual sigma 1.209 kcps, amplitude/sigma 1.06; ratio 0.0264, amplitude/sigma 1.06.
  - 0.615 MHz 13C lower sideband: raw 1.103 kcps, amplitude/sigma 0.87; ratio 0.0227, amplitude/sigma 0.87.
  - 1.385 MHz 13C upper sideband: raw 1.220 kcps, amplitude/sigma 0.97; ratio 0.0251, amplitude/sigma 0.97.
  - Prior det=1.0 MHz exploratory feature near 1.178 MHz: raw 1.678 kcps, amplitude/sigma 1.94; ratio 0.0345, amplitude/sigma 1.94. This is the largest of the prechecked target-ish components but remains post-hoc/non-carrier and baseline-sensitive.
- Baseline sensitivity check over polynomial degrees 0 to 3 does not make the 1.0 MHz carrier or 13C sidebands robust; target amplitudes remain around the noise/residual scale.
- Per-average common-mode levels vary substantially: average-mean signal ranges from 37.47 to 51.21 kcps and reference from 42.02 to 55.19 kcps. Average 7 also has a large within-average acquisition-order signal delta of 9.44 kcps and reference delta of 4.96 kcps. These are provenance against over-interpreting slow structure as coherent Ramsey physics.

## Plausible interpretation

The short-tau/high-SNR diagnostic completed safely and produced analyzable raw readouts, but it did not reveal a robust det-following 1.0 MHz Ramsey carrier. The main visible structure is slow and common-mode-sensitive, with sizeable between-average count variation late in the run. A weak projection near the previous 1.178 MHz exploratory feature is present, but it is not the programmed carrier and not an expected 13C sideband; it is too post-hoc and too close to baseline/noise choices to promote.

This run weakens the hypothesis that the previous long-window failures were only caused by tau=0 or by insufficient early-time SNR. If there is a real Ramsey oscillation on r03 under this protocol, it is not cleanly resolved by these three Ramsey datasets. An extremely short or poorly initialized/coherently controlled Ramsey response is still possible, but this data shape does not support fitting a numeric T2star.

## Claims that are not yet supported

- No well-supported T2star value or bound is established from this run.
- No well-supported nearby-13C conclusion is established.
- The 1.178 MHz component should not be claimed as a physical coupling or carrier feature.
- The slow low-frequency envelope should not be claimed as Ramsey decay without an independent protocol/timing/readout explanation.
- The current data do not support another blind long-window or same-protocol accumulation on r03.

## Recommended next action

Do not run another blind Ramsey repeat on r03. First do a bridge-free protocol/decision review: reconcile the three non-claim-grade Ramsey outcomes with the validated `auto__ramsey` timing/readout path, the fine-pODMR center, and the large count/common-mode variation in this terminal run. If continuing r03 experimentally, make the next experiment an alternate diagnostic with a specific failure-mode test, such as rechecking r03 resonance/counts and then using a phase-cycled or otherwise protocol-controlled Ramsey sanity test before any further T2star/13C attempt. If that is not justified, close the r03 Ramsey/T2star/13C branch as unsupported under current conditions and decide whether to move to another aligned candidate search.
