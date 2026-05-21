Case podmr_028_2026-05-13-100213, timestamp 2026-05-13-100213.

I used only the provided sequence XML and raw readouts. The active sequence is Rabimodulated.xml / Rabimodulated with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence sets a microwave tone with IQ modulation, polarizes the NV, records an initial detection, waits, and because full_expt = 0 it skips the optional 1-level reference block. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the pre-MW polarized 0-level reference, and readout 2 is the post-Rabi-pulse measurement used for the pODMR response.

The combined readouts are noisy with only two averages, but readout 2 shows a localized decrease near 3.900-3.905 GHz. The deepest normalized point is at 3.905 GHz, where readout 2/readout 1 is about 0.873 and the absolute difference readout2 - readout1 is about -3.5 counts. The same high-frequency dip is visible in both per-average traces for readout 2, while neighboring points recover. This looks more like a resonance-like pODMR contrast feature than a purely monotonic drift or isolated single-average spike.

Decision: resonance_present.
