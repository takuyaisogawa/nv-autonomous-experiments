Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects the bright/0-level reference, then because full_expt is 0 it skips the optional 1-level reference block. It then applies rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns, and performs the second detection. Thus readout 1 is the polarized reference and readout 2 is the post-microwave-pulse readout.

Data assessment:

The two raw readouts fluctuate at the 1-count level and share broad drift/drop structure, especially near 3.90 GHz. The post-pulse/reference difference changes sign across the scan, with some negative points around 3.86 GHz and 3.885-3.92 GHz, but these are broad and not consistently reproduced in the two per-average traces as a clear localized pODMR dip. The apparent low points are comparable to average-to-average scatter and common PL variation rather than a resolved resonance feature.

Decision: resonance_absent.
