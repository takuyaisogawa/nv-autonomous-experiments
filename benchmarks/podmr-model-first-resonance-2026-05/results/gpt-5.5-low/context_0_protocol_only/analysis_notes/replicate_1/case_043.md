Sequence inspection:
- Active sequence: Rabimodulated.xml.
- The instructions first polarize and acquire a true 0-level reference detection.
- The optional 1-level reference block is inactive because full_expt = 0.
- The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection.
- Therefore readout 1 is the pre-pulse 0-level reference and readout 2 is the post-Rabi-pulse measurement readout.

Run parameters:
- Varying mw_freq from 3.825e9 to 3.925e9 Hz in 5e6 Hz steps.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so effectively 52 ns.
- mod_depth = 1 in the exported variable values used for this run.
- Averages = 2, repetitions = 100000.

Data assessment:
The two combined readouts fluctuate around roughly 43 to 49 counts with only two averages. The signal readout does not show a stable, localized ODMR-like dip or peak relative to the reference across the sweep. Several excursions, including the high point near the low-frequency side and variations around 3.86 to 3.90 GHz, are comparable to average-to-average scatter visible in the per-average overlay. There is no coherent contrast feature that persists across averages or stands out from the noise.

Decision:
No convincing pODMR resonance is present in this scan.
