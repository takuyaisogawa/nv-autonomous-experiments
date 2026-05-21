Active sequence: Rabimodulated.xml / 1DExp-seq-Rabimodulated-vary-mw_freq.

The sequence varies mw_freq from 3.825 GHz to 3.925 GHz. It polarizes the NV, performs a first detection immediately after optical pumping, waits, skips the optional 1-level reference block because full_expt = 0, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 before the second detection. Therefore the two readouts are not two equivalent signal channels: readout 1 is the true-0/reference readout, and readout 2 is the post-microwave-pulse signal readout.

The post-pulse signal readout shows a frequency-dependent excursion relative to the reference, most notably a reproducible high feature near 3.91-3.915 GHz in the averaged signal while the reference trace does not show the same feature. The data are noisy with only two averages, but the signal-reference contrast is structured rather than a flat random scatter across the sweep.

Decision: resonance_present.
