# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`: objective and current project context.
- `measurement/m001.json`: raw export of completed Ramsey savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`: executed recipe/intent, confirming `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `tau=0..8 us`, 41 points, `8 x 50000` repetitions.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control; run completed successfully.
- Relevant prior context from `project/state.md`: r03 is the accepted aligned candidate; first Ramsey scout at `det=1.5 MHz` was analyzable but non-claim-grade, with a weak exploratory component near `0.884 MHz`; expected 13C sidebands for this run were about `0.615/1.385 MHz`.

## Calculations or scripts run

- Ran a local Python analysis script and saved outputs under `scratch_ramsey_analysis/`.
- Parsed combined and per-average readouts from `measurement/m001.json`.
- Treated readout1 as reference and readout2 as Ramsey signal, consistent with the prior project route review.
- Computed raw readout means, signal/reference ratio, linear-detrended FFTs, targeted sine/cosine least-squares amplitudes, per-average amplitudes/phases, and exploratory damped-cosine fits.
- Wrote plot `scratch_ramsey_analysis/ramsey_m001_summary.png` and machine summary `scratch_ramsey_analysis/summary.json`.

Key numeric checks:

- Sampling: `0..8 us`, 41 points, `dt=0.2 us`; `rfftfreq` spacing is `0.12195 MHz`, Nyquist `2.439 MHz`.
- Combined raw means: reference `49.31 kcps`, signal `44.58 kcps`; mean signal/reference ratio `0.9042`, ratio range `0.8025..0.9721`.
- Average-to-average common-mode level variation is nontrivial: per-average reference means `40.47..55.53 kcps` and signal means `36.20..50.27 kcps`, both about `10-11%` CV. Ratio means are more stable, about `0.891..0.926`.
- Strongest detrended ratio FFT bins: `1.2195 MHz` amplitude `0.0197`, `0.4878 MHz` amplitude `0.0165`, `1.0976 MHz` amplitude `0.0133`, `0.9756 MHz` amplitude `0.0129`, `0.6098 MHz` amplitude `0.0112`.
- Targeted ratio least-squares amplitudes with linear baseline:
  - `1.000 MHz`: amp `0.0092`, z-like amp/SE `1.39`, `R2=0.053`.
  - `0.615 MHz` lower 13C sideband: amp `0.0111`, z-like amp/SE `1.67`, `R2=0.074`.
  - `1.385 MHz` upper 13C sideband: amp `0.0084`, z-like amp/SE `1.28`, `R2=0.046`.
  - prior `0.884 MHz` diagnostic: amp `0.0074`, z-like amp/SE `1.10`, `R2=0.035`.
- Exploratory damped-cosine fits to the combined ratio prefer a frequency near `1.19..1.21 MHz`, not the programmed `1.0 MHz` carrier; exponential-envelope fit gave `T ~= 2.27 us`, `f ~= 1.187 MHz`, `R2 ~= 0.49`, but this is fit-exploratory, not claim-grade.
- Per-average checks do not support a robust common component: at `1.2195 MHz`, per-average ratio amplitudes span `0.0006..0.0387` with amp CV about `0.59`, and phases are only partly clustered; at the planned carrier and sidebands, phases and amplitudes are likewise inconsistent.

## Plausible interpretation

- The completed run is analyzable and contains weak oscillatory structure, but the combined trace is not dominated by the intentionally programmed `1.0 MHz` Ramsey carrier.
- The strongest combined exploratory component is near the `1.2 MHz` FFT bin / `1.19 MHz` damped-fit frequency. This is shifted from both the programmed carrier and the prior scout's weak `~0.884 MHz` component, so it does not straightforwardly validate either a clean Ramsey carrier or a fixed artifact hypothesis.
- The sideband checks at `~0.615 MHz` and `~1.385 MHz` are small and not statistically or per-average compelling. This run does not provide support for nearby 13C coupling.
- Because average-to-average brightness changes are about `10%` common-mode while the candidate spectral amplitudes are only around `1-2%` in ratio, normalization helps but does not by itself make the spectral features claim-grade.
- A conservative read is: r03 remains a valid aligned NV candidate from the pODMR evidence, but this second Ramsey still does not establish T2star or 13C. It suggests either weak/unstable Ramsey contrast, imperfect frequency/phase conditions, drift/normalization limits, or another sequence/acquisition issue.

## Claims not yet supported

- No supported T2star value from this run. The damped-cosine `T ~= 2.3 us` exploratory fit is not supported as a project claim because signal presence and per-average consistency are insufficient.
- No supported 13C conclusion from this run. The expected sideband amplitudes are weak and not repeatable enough across averages.
- No claim that the Ramsey carrier is cleanly at `1.0 MHz`.
- No claim that the prior `~0.884 MHz` feature was physical or fixed artifact; the det-shift diagnostic remains inconclusive rather than confirmatory.
- No need to revise the r03 alignment conclusion from this Ramsey alone; alignment rests on the earlier strong/weak/fine pODMR evidence.

## Recommended next action

Do not immediately repeat the same Ramsey again. Review the sequence/readout phase path and frequency basis before spending more bridge time: verify that the programmed `det` produces the expected phase advance in this `auto__ramsey` route, and consider a short calibration/diagnostic Ramsey on the same r03 settings that deliberately scans a smaller tau range or phase condition to confirm a carrier with high contrast before attempting another T2star/13C claim run. If the route check is clean, the next measurement should be a bounded high-SNR carrier-confirmation Ramsey, not a 13C claim attempt.
