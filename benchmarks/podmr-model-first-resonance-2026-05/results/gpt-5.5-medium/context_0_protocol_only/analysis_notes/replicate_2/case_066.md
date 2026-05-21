Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes and detects a true 0-level reference readout. The optional 1-level reference block is inactive because full_expt = 0. The active signal block then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns before the second detection. Thus readout 1 is the bright/reference readout and readout 2 is the MW-pulse signal readout.

The raw readouts have strong per-average drift, with one average trending downward and the other upward, so the relevant feature is the signal relative to the reference at the same scan point. The combined readout2/readout1 ratio is mostly near unity but develops negative contrast at the high-frequency side, especially at 3.900 GHz and most strongly at the final 3.925 GHz point. The same final-point negative contrast is visible in both individual averages, although the feature is at the scan boundary and the data are noisy.

Decision: a pODMR resonance is present, likely only partially captured near the upper edge of the scan.
