# Ramsey Review

## Files and data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior relevant evidence: `evidence/e006.md` fine weak-pi pODMR note, `evidence/e007.json` second Ramsey model/advisory, `evidence/e013.md` handoff note before the Ramsey completed.
- New Ramsey artifacts: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal-ish status snapshot, `measurement/m005.json` control snapshot.
- Derived local artifacts created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- The script loaded only local JSON files, reconstructed `tau = 0..8 us` with 41 points, and treated readout1 as reference and readout2 as Ramsey signal per the project protocol review.
- Computed raw signal, point-wise signal/reference, and signal/fitted-reference-line views.
- Performed linear detrending, FFT checks, exact-frequency least-squares sinusoid checks at:
  - programmed detuning: `1.000 MHz`
  - expected 13C sidebands from the project model: `0.615423 MHz` and `1.384577 MHz`
  - prior exploratory component: `0.884 MHz`
- Computed a frequency-scan amplitude floor over `0.3..2.3 MHz`, per-average target amplitudes/phases, and a simple scan-order common-mode drift proxy.
- Ran an extra endpoint-sensitivity check excluding the first one or two `tau` points; this did not recover a supported `1.0 MHz` carrier.

## Key quantitative checks

- The run completed safely with `8 x 50000` repetitions, final counts `44.184 kcps`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau_step = 0.2 us`, nominal `1/span = 125 kHz` resolution, and Nyquist `2.5 MHz`.
- Drift proxy: no average exceeded a `15%` common-mode drop threshold; largest negative acquisition-order common-mode drop was about `3.8%`.
- Combined raw signal exact-frequency fits:
  - `1.000 MHz`: amplitude `0.277 kcps`, `0.62%` of mean signal, `R2 = 0.115`.
  - `0.615423 MHz`: amplitude `0.475 kcps`, `1.07%` of mean signal, `R2 = 0.156`.
  - `1.384577 MHz`: amplitude `0.263 kcps`, `0.59%` of mean signal, `R2 = 0.113`.
  - `0.884 MHz`: amplitude `0.286 kcps`, `0.64%` of mean signal, `R2 = 0.117`.
- Signal/fitted-reference-line exact-frequency fits:
  - `1.000 MHz`: amplitude `0.00564`, `0.62%` of mean normalized signal, `R2 = 0.029`.
  - `0.615423 MHz`: amplitude `0.00970`, `1.07%`, `R2 = 0.073`.
  - `1.384577 MHz`: amplitude `0.00538`, `0.60%`, `R2 = 0.027`.
  - `0.884 MHz`: amplitude `0.00586`, `0.65%`, `R2 = 0.031`.
- Frequency-scan floor comparison in the fitted-reference-line-normalized view:
  - `0.615423 MHz` is only `1.60x` the median scanned amplitude and `0.64x` the 90th-percentile scanned amplitude.
  - `1.000 MHz`, `1.384577 MHz`, and `0.884 MHz` are near or below the median scanned amplitude.
- Per-average phase coherence is weak to moderate, not claim-grade:
  - raw signal phase-locking values: `1.000 MHz = 0.45`, low sideband `0.67`, high sideband `0.28`, prior `0.37`.
  - normalized signal phase-locking values are similar.
- FFT peaks do not cleanly select the programmed carrier or a symmetric 13C triplet. The raw signal's largest detrended FFT bins are near `1.220`, `1.098`, `0.488`, `0.122`, and `0.610 MHz`; reference readout also has nontrivial spectral structure, including near the prior `0.884 MHz` region.

## Plausible interpretation

- This is a valid completed Ramsey acquisition on the accepted r03 branch, with healthy terminal counts and no simple drift-collapse signature.
- The programmed `1.0 MHz` Ramsey carrier is not supported strongly in raw signal or normalized views.
- The prior `0.884 MHz` scout feature is not confirmed as a physical Ramsey component in this det-shifted run.
- A weak feature near the lower expected 13C sideband (`~0.615 MHz`) is present, but it is small, not clearly above the scan-amplitude background, and not accompanied by a supported carrier or high-side sideband. It is therefore best treated as a hypothesis or artifact/noise candidate, not a 13C observation.
- The data look more consistent with weak/incoherent Ramsey contrast plus baseline/reference structure than with a clean decaying Ramsey fringe.

## Claims not yet supported

- No claim-grade numeric `T2star` is supported from this run.
- No `13C` coupling conclusion is supported.
- The fine weak-pi pODMR center at `3.8759 GHz` is not invalidated by this Ramsey alone, but the Ramsey evidence does not independently confirm a clean carrier at the programmed detuning.
- There is no evidence here for a terminal tracking/count failure or explicit stop/cancel event.

## Recommended next action

Do not run another blind long `8 us` Ramsey repeat. Next, use a diagnostic Ramsey step designed to answer why the carrier is missing: re-check or refresh the weak-pi resonance if needed, then run a shorter, denser early-time Ramsey on r03, preferably avoiding reliance on the `tau=0` endpoint and using a detuning/phase-ramp check that can confirm whether the observed frequency follows the programmed detuning. If that diagnostic still lacks a coherent carrier, switch away from T2star fitting and treat this branch as no claim-grade Ramsey/T2star/13C result unless a sequence/readout issue is found.
