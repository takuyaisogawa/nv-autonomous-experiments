# Ramsey Review

## Files/Data Used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, and `md/knowledge.md` for project objective, prior r03 acceptance, Ramsey settings, and interpretation rules.
- `context.json` for the checkpoint summary and recent evidence pointer.
- `measurement/m001.json` for the raw exported Ramsey savedexperiment data.
- `measurement/m002.json` through `measurement/m005.json` for the submitted job, terminal result, status, and control metadata.
- `evidence/e009.json` through `evidence/e011.json` for the Ramsey job/start/pre-enqueue context.

## Calculations Or Scripts Run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_metrics.json` and `ramsey_analysis.png` were generated in this working directory. The PNG could not be opened by the local image viewer due to an access error, so conclusions below use the JSON metrics and direct array checks.
- Confirmed run settings from raw export: `ramsey.xml`, `tau = 0..6 us`, 31 points, `0.2 us` step, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `4 x 50000` repetitions, snake order, full experiment off.
- Confirmed terminal execution health: job completed, savedartifact present, no abort/incomplete flag, final count text `38.249 kcps`, still above the `20 kcps` minimum, though lower than the preceding `43.890 kcps` text.
- Readout check: reference mean `45.318 kcps`, signal mean `42.098 kcps`; signal/reference mean `0.9292`, normalized trace standard deviation `0.0340`, peak-to-peak normalized contrast `0.1355`.
- FFT check on signal/reference: actual discrete bin spacing from `N=31`, `dt=0.2 us` is `161.3 kHz`; Nyquist is `2.419 MHz`. Largest combined normalized FFT bins are `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `0.161 MHz`, `1.935 MHz`, and `1.774 MHz`.
- Planned-frequency checks: nearest `det=1.5 MHz` bin is `1.452 MHz` with amplitude `0.77x` the median nonzero FFT amplitude; nearest `det - 13C` bin (`~1.115 MHz`) is `0.83x`; nearest `det + 13C` bin (`~1.885 MHz`) is only `1.34x`.
- Per-average FFT peaks are not consistent: avg 1 peaks near `0.968/0.806 MHz`, avg 2 near `1.452/1.935 MHz`, avg 3 near `0.323/1.129/1.290 MHz`, avg 4 near `0.161/0.806/0.323 MHz`.
- Descriptive damped-cosine fit to signal/reference gave `freq = 0.939 +/- 0.039 MHz`, `T2star = 3.19 +/- 1.05 us`, amplitude `0.0529`, and `R2 = 0.445`. Fixed-frequency linear fits showed the `0.968 MHz` component explains more variance (`R2 ~ 0.28`) than the planned `1.452 MHz` detuning bin (`R2 ~ 0.023`).

## Plausible Interpretation

- The Ramsey execution itself is usable as a scout measurement: it completed, produced raw readouts, and retained adequate counts.
- There is plausible Ramsey-like modulation in the normalized trace, with the strongest combined evidence near `0.94-0.97 MHz`, not at the intended `1.5 MHz` carrier.
- The lower-than-planned Ramsey frequency is compatible with a resonance/detuning mismatch on the order of several hundred kHz, which is plausible given the project already treated the weak-pi pODMR center as grid-supported rather than fit-precise.
- This scout is non-claim-grade for T2star and 13C. The descriptive `T2star ~3.2 us` fit may be a useful planning number, but the fit has modest explanatory power and per-average spectral content is inconsistent.

## Claims Not Yet Supported

- No well-supported numerical T2star claim is supported by this measurement.
- No supported nearby `13C` claim is supported. The expected `det +/- ~0.385 MHz` bins are not prominent enough, and the per-average FFT does not show repeatable sideband structure.
- The observed `0.94-0.97 MHz` component should not yet be assigned as a physical coupling or final detuning without a resonance/detuning follow-up.
- The final count reduction from prior `43.890 kcps` to `38.249 kcps` is provenance for drift/focus/count change, not by itself evidence against r03 or against a Ramsey signal.

## Recommended Next Action

Before attempting a claim-grade T2star/13C Ramsey repeat, refine the resonance/detuning. The most direct next action is a fresh narrow weak-pi pODMR or short Ramsey detuning diagnostic around the accepted r03 resonance to determine whether the effective Ramsey carrier should be near `1.0 MHz` rather than the intended `1.5 MHz`. Then repeat Ramsey with a grid that preserves FFT resolution and per-average tracking limits, using enough averages to test repeatability before promoting T2star or 13C.
