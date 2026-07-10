# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, and Ramsey-related pointers in `md/knowledge.md`, `evidence/*.md`, `evidence/*.json`.
- New measurement data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Bridge/job metadata: `measurement/m002.json` planned execute contract, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` control state.
- Scratch outputs created: `scratch/ramsey_analysis_summary.txt` and `scratch/ramsey_analysis.png`.

## Calculations/Scripts Run

- Used local Python with `json`, `numpy`, `scipy.optimize.curve_fit`, and matplotlib `Agg`.
- Extracted combined and per-average readouts from `ExperimentData` and `ExperimentDataEachAvg`.
- Treated readout1 as reference and readout2 as Ramsey signal, using both point-wise `signal/reference` and signal normalized by a linear reference fit.
- Checked scan setup: tau `0..8 us`, `41` points, `dt = 0.2 us`, Nyquist `2.5 MHz`, nominal FFT bin spacing `125 kHz`; acquisition was `8 x 50000`, snake order, final counts `44.184 kcps`.
- Ran simple scan-order drift slopes on per-average common-mode and ratio traces. This flagged average 1 ratio slope `+8.46%` across its scan order and average 6 ratio slope `-5.52%`; no large common-mode flags by the same simple threshold.
- FFT check on detrended, Hann-windowed combined reference-line-normalized signal found strongest components near `1.165 MHz`, `1.245 MHz`, `1.084 MHz`, `0.490 MHz`, and `0.570 MHz`.
- Direct least-squares sinusoid checks with offset+slope at target frequencies gave:
  - `0.615 MHz`: combined amplitude `0.00974`, per-average median amplitude `0.01154`.
  - prior scout component `0.884 MHz`: combined amplitude `0.00586`, per-average median `0.01148`.
  - programmed detuning `1.000 MHz`: combined amplitude `0.00564`, per-average median `0.00857`.
  - upper 13C sideband candidate `1.385 MHz`: combined amplitude `0.00541`, per-average median `0.01363`.
- Per-average phase coherence was modest/inconsistent at the main targets: about `0.56` at `1.000 MHz`, `0.47` at `0.884 MHz`, and `0.37` at `1.385 MHz`; the exploratory `1.165 MHz` component was more coherent at about `0.81`.
- Damped-cosine fits are descriptive only. Starting near `1.0 MHz` pushed to the upper frequency bound `1.300 MHz` with `T2* = 0.20 us` lower bound and `R2 = 0.479`; starting near the FFT peak gave `f = 1.1886 MHz`, `T2* = 2.01 us`, `R2 = 0.413`.

## Plausible Interpretation

- The measurement completed cleanly and has enough raw data for analysis, with final counts above the project gate and no abort.
- The second Ramsey does show structured oscillatory content, but it does not cleanly land on the programmed `1.0 MHz` carrier. The strongest combined exploratory content is near `1.16..1.19 MHz`, while direct amplitude at `1.0 MHz` is weak and not phase-consistent enough across averages.
- The prior non-claim-grade `~0.884 MHz` component did not reappear as the dominant feature after changing detuning from `1.5 MHz` to `1.0 MHz`; this weakens the case that the prior component was a stable physical Ramsey carrier.
- There is no clear support for the expected 13C sideband pair near `0.615/1.385 MHz`. The sideband-target amplitudes are small, not paired in a compelling way, and per-average phase consistency is insufficient.
- A short apparent decay can be forced by fits, but the fits are not robust: one hits parameter bounds and the better exploratory frequency fit has only modest `R2`. Treat any `T2*` number from this dataset as descriptive, not a supported project conclusion.

## Claims Not Yet Supported

- A well-supported `T2*` value is not established by this measurement.
- A nearby `13C` coupling conclusion is not established.
- The observed `~1.16..1.19 MHz` component should not be claimed as the true detuned Ramsey carrier without a repeat or diagnostic that demonstrates reproducibility and detuning/frequency dependence.
- No sub-grid or sub-fit precision claim should be made for the microwave center beyond the earlier fine-pODMR grid-supported `3.8759 GHz` basis.

## Recommended Next Action

Do not immediately claim T2star or 13C from this run. Run one focused diagnostic before spending more long Ramsey time: repeat a shorter, higher-confidence Ramsey around the same r03 target with the same `mw_freq = 3.8759 GHz` but a deliberately different detuning, preferably chosen so the expected carrier is well separated from `1.16 MHz` and the 13C sidebands remain inside Nyquist. Analyze carrier shift, per-average phase coherence, and raw/readout drift before fitting T2star. If the spectral feature does not shift with programmed detuning, treat it as artifact/noise and reconsider the Ramsey sequence/frequency calibration rather than accumulating more averages blindly.
