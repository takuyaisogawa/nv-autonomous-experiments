# Ramsey Review: r03 First T2star/13C Scout

## Files/Data Used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project objective, accepted r03 context, prior pODMR basis, and intended Ramsey plan.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: bridge job contract for `nv23_ramsey_20260513_185505_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result/status/control metadata.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations/Scripts Run

- Ran `python analyze_ramsey.py`.
- Extracted readout 0 as the pre-Ramsey 0-level reference and readout 1 as the Ramsey signal from `ramsey.xml` with `full_experiment=0`.
- Built `tau = 0..6 us` in 31 points, `dt = 0.2 us`, sampling `5.0 MHz`, Nyquist `2.5 MHz`, NumPy FFT bin spacing `0.1613 MHz` (`1/6 us = 0.1667 MHz` planned span scale).
- Reviewed raw readouts, signal/reference ratio, per-average ratios, FFT of detrended normalized data, fixed-frequency sinusoid checks, and damped-cosine fits.
- Count/drift check: pre-run fresh track was `43.535 kcps`; terminal final counts were `38.249 kcps`, a `12.1%` drop.
- Normalized Ramsey ratio: mean `0.9292`, std `0.0340`, median SEM across four stored averages `0.0256`.
- Intended carrier check at `det = 1.5 MHz`: linear sinusoid amplitude `0.0058` in ratio units, `R2 = 0.030`, and BIC was worse than a line-only model by `+6.38`.
- FFT peaks were broad/nonunique. Largest detrended-windowed peaks were `0.968`, `0.806`, `0.323`, `1.935`, and `1.774 MHz`; the intended `1.5 MHz` carrier was not a dominant peak.
- Free damped-cosine fit found a feature near `0.941 MHz` with nominal `T2star = 2.39 +/- 1.19 us`, `R2 = 0.446`, and BIC improvement `-4.12` vs line-only. This is descriptive only; it uses six parameters on 31 points and the per-average coherence is weak.
- Fixed `1.5 MHz` damped-cosine fit gave nominal `T2star = 0.38 +/- 0.34 us`, `R2 = 0.207`, and BIC worse than line-only by `+3.57`; do not use this as a T2star value.
- 13C model sideband check around `det +/- 0.385 MHz` corresponds approximately to `1.115` and `1.885 MHz`. The nearest linear checks at `1.129` and `1.935 MHz` had small amplitudes (`0.0064` and `0.0135`) and BIC worse than line-only (`+6.29` and `+4.19`), so they are not claim-grade.

## Plausible Interpretation

- The run completed and contains analyzable Ramsey data, but the signal is weak relative to stored-average scatter and run drift.
- There may be a weak Ramsey-like oscillatory component near `0.94 MHz`; if real, it could reflect MW/resonance detuning or phase-convention offset relative to the intended `1.5 MHz` programmed detuning. The current evidence is not strong enough to promote that feature to a calibrated Ramsey carrier.
- The lack of a clean `1.5 MHz` carrier and the `12.1%` count drop make this scout non-claim-grade for T2star. It is best treated as diagnostic evidence that the next Ramsey should be redesigned or repeated under tighter drift/count control.

## Claims Not Yet Supported

- No well-supported T2star value is established. The only finite T2star numbers are descriptive fit outputs and are not robust against model choice.
- No well-supported 13C coupling conclusion is established. The FFT does not show a clear carrier with reproducible sidebands at the expected `~0.385 MHz` separation.
- The observed `~0.94 MHz` feature is not yet established as a physical Ramsey frequency.
- This run does not invalidate r03 as the aligned candidate; prior pODMR evidence still supports r03 alignment, but this Ramsey acquisition alone is not sufficient for final T2star/13C conclusions.

## Recommended Next Action

Retrack r03 and repeat a bounded Ramsey diagnostic only if counts are recovered/stable. Use a shorter per-average tracking window than this run, then require a reproducible carrier across stored averages before fitting T2star or interpreting 13C sidebands. If the repeat again shows a stable carrier shifted from `1.5 MHz`, use that carrier to refine the MW resonance/frequency convention before attempting a longer or higher-SNR 13C-resolving Ramsey scan.
