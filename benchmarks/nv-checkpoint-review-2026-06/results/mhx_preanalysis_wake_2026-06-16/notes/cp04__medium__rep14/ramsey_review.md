# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md` for objective, current project state, and review rules.
- `measurement/m001.json` terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.
- Prior context from `evidence/e008.json` / `evidence/e009.py` for the immediately preceding det=1.0 MHz short-tau Ramsey terminal review, plus `evidence/e019.json` and `evidence/e028.json` for the det-shift measurement intent.

## Calculations Or Scripts Run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs:
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_review.png`
- Checks performed:
  - Verified raw export axis contract: averaging `ExperimentDataEachAvg[:, readout, tau]` reproduces combined `ExperimentData`.
  - Confirmed terminal run metadata: status completed, 12 averages x 90000 repetitions, 1.08e6 shots/tau, final counts 44.796 kcps, no monitor error, no stop request.
  - Reviewed raw signal, reference, signal/reference, and signal/fitted-reference-line views.
  - Computed per-point SEM from stored averages: median signal SEM 0.711 kcps; median ratio SEM 0.0126.
  - Ran least-squares sinusoid screens after linear baseline removal over 0.25..2.35 MHz, plus FFT checks. The FFT bin spacing is coarse, 0.508 MHz, so the LS screens are the more useful frequency discriminator.
  - Checked target frequencies: programmed 1.5 MHz carrier, previous fixed 1.192 MHz feature, det-tracking prediction 1.692 MHz, programmed 13C sidebands 1.115/1.885 MHz, and det-tracking sidebands 1.307/2.077 MHz.

## Plausible Interpretation

- The det-shift run is analyzable and has no hard terminal anomaly in the provided metadata.
- The old fixed 1.192 MHz feature is weak in this run: ratio LS amplitude 0.00511.
- The strongest combined all-tau ratio LS component is near 1.623 MHz with amplitude 0.02547. The predicted det-tracking point at 1.692 MHz is nearly as large, amplitude 0.02505; the programmed 1.5 MHz carrier is also comparable, amplitude 0.02399.
- This directionally argues against a strictly fixed 1.192 MHz artifact and is broadly compatible with a det-shifted Ramsey-like component, but the short time window gives poor frequency discrimination and the per-average top-frequency screens are inconsistent.
- A large early-time transient remains: 0..0.75 us peak-to-peak is 6.46 kcps in signal and 0.134 in ratio. Skipping tau <= 0.2 us moves the top ratio screen to about 0.746 MHz, so the spectral conclusion depends strongly on early points.

## Claims Not Yet Supported

- Do not claim a numeric T2star from this run. The descriptive damped-sinusoid grid fit prefers unrelated low frequencies, about 0.678 MHz in ratio and 0.818 MHz in raw signal, with sub-us T2star-like values; this is model/early-transient sensitive rather than a supported physical parameter.
- Do not claim nearby 13C coupling. Neither programmed sidebands nor det-tracking sidebands are dominant or stable enough: tracking-sideband ratio amplitudes are 0.00953 at 1.307 MHz and 0.00614 at 2.077 MHz.
- Do not claim that the Ramsey branch has a clean carrier model. The det-shift result is suggestive, not claim-grade, because the carrier frequency is broad/ambiguous and average-to-average frequency screens disagree.

## Recommended Next Action

- Stop doing blind Ramsey repeats on r03.
- Do a bridge-free synthesis of all r03 Ramsey datasets and decide the branch: either close r03 Ramsey/T2star/13C as unsupported under the current Ramsey protocol, or switch to a targeted alternate protocol/calibration that directly tests the early-time transient and carrier phase behavior before any more T2star fitting.
