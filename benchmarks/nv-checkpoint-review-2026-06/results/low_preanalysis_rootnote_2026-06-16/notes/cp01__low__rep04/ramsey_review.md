# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`: objective, accepted r03 context, prior pODMR basis, and planned Ramsey parameters.
- `measurement/m001.json`: raw Ramsey export from `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: submitted Ramsey job contract.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result/status/control metadata.
- `md/knowledge.md`, `md/memory.md`: local project lessons relevant to Ramsey/T2star and 13C FFT caution.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_results.json` and `ramsey_analysis.png`.
- Checks performed:
  - Confirmed Ramsey scan shape: 31 tau points from 0 to 6 us with 0.2 us step; 4 averages; two readout channels.
  - Computed raw signal/reference ratio and per-average normalized ratios.
  - FFT of the normalized ratio using the actual sample grid: bin spacing 161.29 kHz, Nyquist 2.419 MHz.
  - Damped-cosine-plus-linear-trend fits to raw signal and normalized signal/reference.
  - Per-average common-mode and ratio consistency checks.

## Plausible interpretation

- The measurement completed without bridge abort and saved the expected Ramsey artifact. Final count was 38.249 kcps, above the 20 kcps minimum, but below the fresh pre-run track count of 43.535 kcps, so drift/brightness change remains relevant.
- The combined signal/reference ratio has weak-to-moderate oscillatory structure. A descriptive damped-cosine fit to the normalized ratio gives frequency 0.943 MHz and T2star about 2.30 us with large uncertainty, R2 = 0.446, and about 7.4% fitted relative amplitude. This is a scout-level indication, not a claim-grade T2star.
- The raw signal channel alone does not support the same conclusion: fit R2 = 0.031 and the fitted amplitude is only about 0.44% of offset, with T2star pinned at the upper bound.
- Per-average normalized ratios are not identical but are not single-average-only either: correlations to the combined normalized trace are 0.71, 0.42, 0.55, and 0.60. Mean signal/reference ratios vary from 1.071 to 1.091 across averages.
- FFT evidence is ambiguous. The largest normalized-ratio FFT components are at 0.968, 0.323, 0.161, 0.806, 1.935, and 1.774 MHz. The programmed detuning was 1.5 MHz; the expected 13C sidebands from the project model would be near 1.115 and 1.885 MHz. A component near 1.935 MHz is present, but it is not dominant and nearby power is broadly distributed. This is not enough to identify a nearby 13C.

## Claims not yet supported

- A well-supported T2star value for r03 is not yet established.
- A well-supported nearby-13C conclusion is not yet established.
- The observed normalized-ratio oscillation cannot yet be confidently assigned to the programmed 1.5 MHz Ramsey detuning.
- The FFT does not yet support a resolved 13C sideband pattern.
- This run does not invalidate r03 as the aligned candidate; prior pODMR evidence still supports r03, but this Ramsey scout is not claim-grade.

## Recommended next action

Run a targeted Ramsey follow-up on r03 rather than broad candidate search. Use the same pODMR-supported center unless a fresh quick pODMR/track check says otherwise, but improve claim quality by increasing frequency resolution and/or SNR while keeping the per-average drift window acceptable. A practical next design is a bounded repeat with a longer tau span or denser sampling if advisory allows, and enough repetitions to test whether the normalized-ratio feature locks to the programmed detuning and whether sidebands near det +/- about 0.385 MHz repeat. If runtime/advisory blocks that, first do a shorter validation Ramsey at the same settings to test repeatability under better count stability.
