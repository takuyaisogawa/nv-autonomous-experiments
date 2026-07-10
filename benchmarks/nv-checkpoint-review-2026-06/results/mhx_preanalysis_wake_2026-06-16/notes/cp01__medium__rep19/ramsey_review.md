# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, targeted `rg` checks in `md/`, `evidence/`, `measurement/`, and `context.json`.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` and `ExperimentDataEachAvg` from `measurement/m001.json`.
- Used tau axis `0..6 us`, `31` points, `0.2 us` step, `4` snake-ordered averages, `50000` repetitions.
- Treated readout 1 as reference and readout 2 as Ramsey signal; analyzed `signal/reference`.
- FFT check used detrended, Hann-windowed normalized signal. The actual `np.fft.rfftfreq` bin spacing is `161.29 kHz` for 31 samples at 0.2 us, close to the planned span estimate of `166.67 kHz`; Nyquist is `2.419 MHz`.
- Linear sinusoid checks were run at programmed detuning `1.500 MHz` and expected 13C sideband positions `1.115 MHz` and `1.885 MHz`.
- Descriptive damped-cosine fits were run only as diagnostics, not as claim-grade T2star evidence.

## Plausible interpretation

- The Ramsey job completed without bridge abort. Final counts were `38.249 kcps`, down `12.1%` from the fresh r03 track count `43.535 kcps` and `12.9%` from the weak-pODMR final count `43.890 kcps`, so drift/count loss is material.
- The normalized combined trace has visible oscillatory structure: `signal/reference` mean `0.9292`, std `0.0334`, range `0.8591..0.9946`. Per-average ratio means are close (`0.9199..0.9377`), but per-average ratio std is large (`0.055..0.064`), so average-to-average scatter is not negligible.
- The strongest FFT peaks are not at the programmed `1.5 MHz` carrier. Top windowed FFT peaks are near `0.968`, `0.806`, `0.323`, `1.935`, and `1.774 MHz`.
- Descriptive fits prefer a carrier near `0.943..0.944 MHz`, with weak fit quality (`R2 ~0.43..0.44`). Exponential-envelope fit gives `T2star ~2.39 us` with large uncertainty (`~1.17 us`) and Gaussian-envelope fit gives `~3.21 us` with `~1.05 us` uncertainty.
- Explicit linear regression at `1.500 MHz` explains little of the combined normalized variance (`R2 = 0.030`, amplitude `0.0058`). Checks at expected 13C sidebands are also weak: `1.115 MHz` gives `R2 = 0.042`, amplitude `0.0079`; `1.885 MHz` gives `R2 = 0.078`, amplitude `0.0118`. Per-average amplitudes at these frequencies are inconsistent enough that the sideband-looking FFT bins should be treated as non-claim-grade.
- A plausible but not established explanation is that the weak-pODMR grid center at `3.876 GHz` was still off by roughly `0.5..0.6 MHz`, shifting the Ramsey beat away from the intended detuning, with drift further degrading the scout.

## Claims not yet supported

- No well-supported T2star value is established from this scout. The few-us fitted values are descriptive only because the carrier is not the programmed carrier, fit quality is modest, and counts drifted.
- No nearby 13C coupling conclusion is supported. Peaks near the expected high sideband region are comparable to other FFT peaks and are not robust in the direct frequency checks.
- A no-13C claim is also not supported; the scout is too drift-affected and frequency-ambiguous to rule out weak sidebands.
- The exact resonance offset or cause of the unexpected `~0.94 MHz` Ramsey carrier is not established by this data alone.

## Recommended next action

Do not promote a T2star or 13C conclusion from this scout. First run a fresh r03 tracking/count check and a narrow weak-pi frequency confirmation around the `3.876 GHz` grid minimum, preferably with sub-MHz spacing. Then repeat Ramsey with the confirmed center and a detuning/sampling plan that keeps the carrier and expected `~0.385 MHz` 13C sidebands away from ambiguous FFT bins while staying inside the drift window.
