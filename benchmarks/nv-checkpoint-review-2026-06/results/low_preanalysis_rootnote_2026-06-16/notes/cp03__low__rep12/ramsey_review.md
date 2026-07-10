# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior design/start note: `evidence/e017.md`.
- New measurement/job artifacts:
  - `measurement/m001.json`: raw savedexperiment export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: bridge job/spec for `nv23_ramsey_20260513_230331_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result, status `completed`, final counts `35.122 kcps`.
  - `measurement/m004.json`: terminal bridge status, elapsed `8402 s`.
  - `measurement/m005.json`: stop-control record, no stop applied/requested.
- Scratch outputs created:
  - `analysis/shorttau_ramsey_summary.json`
  - `analysis/shorttau_ramsey_review.png`

## Calculations or scripts run

- Parsed the raw export with Python. Combined data shape is `2 readouts x 41 tau points`; per-average data shape is `12 averages x 2 readouts x 41 tau points`.
- Reconstructed tau from the job spec: `0.048..1.968 us`, 41 points, `48 ns` step, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000` repetitions.
- Checked raw signal/reference and per-point SEM across averages:
  - Median signal/readout: `48.568 kcps`; median reference: `44.747 kcps`.
  - Raw signal range across tau: `2.176 kcps`.
  - Median per-point SEM: `1.120 kcps` for raw signal and `0.0151` for point-wise ratio.
  - Reference line slope over the short window: `+0.966 kcps/us`.
- Checked stored-average stability:
  - Common-mode average-level span: `0.848..1.137` relative to median, consistent with large tracking/count changes between averages.
  - Average-level signal/reference ratio shift span: `-4.12%..+2.71%`.
- Ran least-squares sinusoid screens with offset and linear trend terms:
  - At programmed carrier `1.000 MHz`: normalized amplitude `0.00475`, raw amplitude `0.213 kcps`, `R2~0.10`.
  - At expected 13C-offset sidebands from prior project context, `0.615 MHz` and `1.385 MHz`: raw amplitudes `0.175 kcps` and `0.149 kcps`, with `R2~0.06`.
  - Broad normalized-frequency screen is dominated by a very-low-frequency edge (`0.15 MHz`, amplitude `0.0899`, low `R2~0.042`) and small high-frequency residuals near `3.7..4.4 MHz`; not by the carrier/sideband model.
- Ran a simple FFT check after linear detrending. Frequency resolution is `0.508 MHz`; the `1.016 MHz` bin amplitude is `0.00406` normalized, comparable to several unrelated bins from `3..6 MHz`.
- Tried an exploratory 1 MHz Gaussian-decay Ramsey fit only as a sanity check. It returned a tiny normalized amplitude `0.00463` and hit the upper T2star bound (`20 us`), so it is not physically claim-grade for this short-window dataset.

## Plausible interpretation

- The short-tau/high-SNR diagnostic completed and is analyzable, but it still does not show a supported Ramsey carrier at the programmed `1.0 MHz` detuning.
- The target carrier and expected `13C` sideband positions are below or near the measured noise/SEM scale and do not dominate either LS or FFT checks.
- Because this run deliberately concentrated shots in the early-time window, the absence of a clear carrier argues against the earlier non-claim-grade results being explained simply by very short T2star hidden in a long-window scan or by the tau=0 artifact.
- The r03 alignment evidence from pODMR remains intact, but r03 Ramsey contrast under the current protocol appears too weak/unstable to support T2star or nearby-13C conclusions.

## Claims that are not yet supported

- No numeric T2star should be claimed from this dataset.
- No nearby `13C` coupling or absence-of-13C conclusion should be claimed from this dataset alone.
- The weak features near `~1.0 MHz`, `~3.7..4.4 MHz`, or the low-frequency baseline component should not be promoted as physical Ramsey/13C peaks.
- The exploratory decay fit should not be used as evidence for long T2star; it is amplitude-limited and bound-limited.

## Recommended next action

- Do not run another blind Ramsey repeat on r03 under the same protocol.
- Branch decision: either switch to an alternate protocol aimed at establishing spin coherence/contrast by a more robust route, or close the r03 Ramsey/13C branch as unsupported under current conditions while preserving the aligned-NV claim.
- If continuing experimentally, first diagnose contrast/readout with a control that should give a strong oscillatory response before attempting another T2star/13C Ramsey claim.
