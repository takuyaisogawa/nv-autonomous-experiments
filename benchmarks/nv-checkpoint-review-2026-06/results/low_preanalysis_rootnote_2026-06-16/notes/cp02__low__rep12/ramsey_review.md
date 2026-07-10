# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- New Ramsey raw export: `measurement/m001.json`, saved experiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Ramsey job/result/status/control: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Local outputs from this review: `analyze_ramsey.py`, `ramsey_analysis_summary.txt`, `ramsey_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` after setting Matplotlib to the noninteractive `Agg` backend.
- Parsed combined and per-average readouts from `ExperimentData` and `ExperimentDataEachAvg`.
- Used channel 0 as a reference-like readout and reviewed both raw channel 1 and normalized `channel1/channel0`.
- Checked per-average channel means and normalized means for common-mode changes.
- Ran detrended Hann-window FFT on combined channel 1 and combined `channel1/channel0`.
- Ran least-squares sinusoid checks with constant plus linear baseline at:
  - expected det carrier: `1.000 MHz`
  - expected 13C sidebands from the project model: about `0.615 MHz` and `1.385 MHz`
  - prior scout feature: about `0.884 MHz`
- Ran a descriptive damped-cosine fit on the combined normalized trace only after confirming visible oscillatory content.

## Plausible interpretation

- The Ramsey run completed normally: status `completed`, final counts `44.184 kcps`, `tau = 0..8 us`, `dt = 0.2 us`, 41 points, 8 averages x 50000 repetitions.
- The normalized combined trace has real oscillatory contrast: `channel1/channel0` mean `0.9042`, standard deviation `0.0290`, peak-to-peak span about `18.8%` of the mean.
- The strongest combined normalized FFT bins are near `1.098 MHz` and `1.220 MHz`; the nearest bin to the programmed `1.0 MHz` carrier is `0.976 MHz` and is third strongest.
- The prior scout feature is not strongly reproduced: the nearest bin to `0.884 MHz` is `0.854 MHz` with smaller FFT amplitude than the carrier-region bins.
- The descriptive damped-cosine fit to the combined normalized trace gives `f = 1.187 +/- 0.027 MHz` and `T2* = 2.27 +/- 0.81 us`, but this should be treated as descriptive rather than claim-grade because per-average spectra/phases are not consistent.
- The data support a Ramsey-like oscillatory signal on r03, and the det-shift diagnostic weakens the idea that the earlier `~0.884 MHz` component was a stable physical carrier.

## Claims that are not yet supported

- Do not claim a final T2star yet. A combined-trace fit gives a plausible few-microsecond scale, but per-average disagreement and common-mode readout variation make the fit insufficient as the project conclusion.
- Do not claim nearby 13C coupling. Targeted checks at `0.615 MHz` and `1.385 MHz` are not dominant or consistently reproduced across averages.
- Do not claim the Ramsey frequency is exactly the programmed `1.0 MHz`; the combined spectrum is strongest around `1.10..1.22 MHz`.
- Do not claim sub-grid pODMR/Ramsey detuning precision from this dataset alone.

## Recommended next action

Run one targeted confirmation Ramsey on the same accepted r03 NV, centered on the observed carrier region rather than broad discovery: keep `mw_freq = 3.8759 GHz`, choose a detuning near `1.18 MHz`, and use a longer window or denser sampling only if the per-average tracking window remains acceptable. The acceptance criterion should be per-average phase/frequency consistency and a stable damped-cosine T2* estimate before making the final T2star claim. If the confirmation again shows inconsistent per-average spectra, close the 13C branch as unsupported and report only a conservative, non-claim-grade Ramsey timescale.
