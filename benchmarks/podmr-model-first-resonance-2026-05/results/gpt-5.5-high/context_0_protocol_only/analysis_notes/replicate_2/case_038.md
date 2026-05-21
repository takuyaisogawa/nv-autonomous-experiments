Sequence and readout interpretation:

The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence polarizes the NV, detects a true 0-level/reference readout, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 from the provided sequence XML, followed by the signal detection. The full_expt variable is 0, so the intermediate 1-level reference block is inactive. Therefore the two active readouts are: readout 1 = pre-MW 0/reference readout, readout 2 = post-Rabi-pulse signal readout.

Resonance assessment:

For a pODMR resonance, I would expect the post-pulse signal relative to the 0-reference to show a coherent localized feature, normally a dip for resonant transfer out of the bright state, with some consistency across averages. The combined readout2-readout1 contrast changes sign repeatedly across the sweep: negative at several separated frequencies, positive at others, and with no single smooth or reproducible resonance-shaped feature. The per-average overlays show substantial drift between averages, and the apparent extrema do not isolate a convincing resonance. I therefore classify this trace as resonance absent.
