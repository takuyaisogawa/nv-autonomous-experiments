# Ramsey Review

## Files/Data Used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior context/evidence: `evidence/e006.md` for fine weak-pi pODMR center support, `evidence/e007.json` for the second-Ramsey model, expected frequencies, and readout roles, plus `evidence/e010.json`/`e011.json`/`e012.json`/`e013.md` for the submitted Ramsey job context.
- New measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.

## Calculations Or Scripts Run

- Created and ran `analyze_ramsey.py`.
- Outputs written under `analysis_outputs/`:
  - `ramsey_analysis_summary.txt`
  - `ramsey_combined_table.csv`
  - `ramsey_bootstrap.csv`
  - `ramsey_traces.png`
  - `ramsey_fft.png`
- Checks performed:
  - Parsed two readouts over 41 tau points and 8 stored averages.
  - Confirmed scan settings: `tau = 0..8 us`, `dt = 0.2 us`, 41 points, `det = 1.0 MHz`, `mw_freq = 3.8759 GHz`, `8 x 50000` repetitions, final counts `44.184 kcps`.
  - Treated readout 1 as reference and readout 2 as Ramsey signal per the prior inspected protocol context.
  - Compared raw signal, point-wise signal/reference, and reference-line-normalized signal.
  - Computed line-detrended Hann FFT amplitudes and least-squares sinusoid amplitudes at:
    - expected low 13C sideband: `0.615 MHz`
    - prior scout feature: `0.884 MHz`
    - programmed Ramsey carrier: `1.000 MHz`
    - expected high 13C sideband: `1.385 MHz`
  - Checked per-average acquisition-order slopes using snake-order metadata.
  - Bootstrapped stored averages for ratio-based least-squares amplitudes and dominant FFT-bin stability.
  - Ran a descriptive fixed-`1 MHz` Gaussian-envelope Ramsey fit on the ratio only as a diagnostic, not as a claim.

## Quantitative Result

- The run completed without bridge abort or low-count terminal failure; final counts were healthy at `44.184 kcps`.
- Raw signal/readout levels show large common-mode average-to-average variation:
  - raw signal average-mean CV: `0.111`
  - ratio average-mean CV: `0.013`
  - This makes ratio/reference-aware views more reliable than raw level alone.
- In the point-wise ratio, the strongest FFT bins are near `1.098 MHz` and `1.220 MHz`, not exactly the programmed `1.000 MHz` bin.
- Ratio FFT/least-squares checks:
  - `0.615 MHz`: nearest FFT bin `0.610 MHz`, FFT/median `1.15`, LS amplitude `0.0111`
  - `0.884 MHz`: nearest FFT bin `0.854 MHz`, FFT/median `1.00`, LS amplitude `0.00742`
  - `1.000 MHz`: nearest FFT bin `0.976 MHz`, FFT/median `2.01`, LS amplitude `0.00916`
  - `1.385 MHz`: nearest FFT bin `1.341 MHz`, FFT/median `1.00`, LS amplitude `0.00843`
- Bootstrap over stored averages using per-average ratios:
  - `1.000 MHz` LS amplitude 5/50/95%: `0.00607 / 0.00979 / 0.01499`
  - dominant FFT-bin bootstrap mode is `1.098 MHz`, occurring about `67%` of resamples.
  - `0.884 MHz` is not a dominant or enhanced feature in this det-shifted run.
- Per-average ratio phase/coherence is incomplete:
  - `1.000 MHz` coherent amplitude `0.00939`, per-average amplitude mean `0.01463`, phase span `2.75 rad`.
  - Sideband candidates have comparable or weaker coherence and no clean symmetric sideband pattern.
- Descriptive fixed-`1 MHz` Gaussian-envelope fit on ratio gave `T2star = 0.468 +/- 0.158 us`, amplitude `-0.109 +/- 0.025`, `R2 = 0.411`; the fitted amplitude is driven by the early-time shape and is not claim-grade because the carrier/spectrum is not cleanly established.

## Plausible Interpretation

- This is analyzable Ramsey data on the accepted r03 NV, and it usefully disfavors the prior `~0.884 MHz` scout feature as a stable physical carrier because it is not enhanced after the programmed detuning was changed to `1.0 MHz`.
- There is weak Ramsey-like spectral content near the intended carrier region, but the dominant ratio FFT bin is `1.098 MHz`, the neighboring `1.220 MHz` bin is also strong, and the exact `1.000 MHz` component is modest. This could reflect a small residual resonance-frequency offset, drift/baseline structure, finite-window leakage, or a weak true Ramsey oscillation mixed with systematics.
- The expected 13C sidebands near `0.615 MHz` and `1.385 MHz` are not supported: the low sideband is weak and the high sideband is at the median FFT background in the ratio view, with no robust symmetric pattern.

## Claims Not Yet Supported

- Do not claim a numeric T2star from this run.
- Do not claim nearby 13C coupling or resolved 13C sidebands.
- Do not claim that the Ramsey carrier is cleanly at the programmed `1.000 MHz`.
- Do not claim that the prior `0.884 MHz` feature was physical; the current det-shift data argues against that, but does not identify its source.
- Do not use the descriptive `0.468 us` fit result as a project T2star value.

## Recommended Next Action

Before another long Ramsey repeat, do a short targeted resonance/phase diagnostic on r03:

1. Recheck/refresh the weak-pi pODMR center if the hardware is still available, because the carrier region suggests possible residual detuning.
2. Then run a shorter Ramsey diagnostic with the same target but tighter early-time sampling and a deliberately chosen detuning/frequency offset test, designed to distinguish true carrier shift from acquisition/window artifacts.
3. If that diagnostic yields a clean carrier with coherent stored-average phase, run the T2star-quality acquisition; otherwise move away from blind Ramsey repeats and consider an alternate sequence/baseline approach before making T2star or 13C conclusions.
