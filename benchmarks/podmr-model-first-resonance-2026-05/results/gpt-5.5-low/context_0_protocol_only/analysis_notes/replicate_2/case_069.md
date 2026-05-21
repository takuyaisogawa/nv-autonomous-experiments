Sequence review:

The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The saved variable values give length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at the 250 MHz sample rate, and mod_depth = 1. The sequence first polarizes and detects a true 0-level/reference readout, waits, and because full_expt = 0 it skips the optional 1-level reference block. It then applies rabi_pulse_mod_wait_time with the scanned microwave frequency, the 52 ns pulse, and mod_depth, followed by the signal detection.

Readout interpretation:

With full_expt disabled, the two plotted raw readouts correspond to the reference detection and the post-pulse detection for each scan point/average rather than a full 0/1 reference/signal set. The per-average overlay shows substantial average-to-average vertical offsets and irregular point-to-point fluctuations. The combined readouts do not show a clear, localized, reproducible ODMR-like dip or peak as a function of microwave frequency. Both traces have broad/noisy variation and some drift across the sweep, but the features are not consistent across averages or between the reference and signal roles in a way that would support a resonance call.

Decision:

I classify this case as resonance_absent. The scan does not contain a distinct pODMR resonance above the raw readout noise and drift.
