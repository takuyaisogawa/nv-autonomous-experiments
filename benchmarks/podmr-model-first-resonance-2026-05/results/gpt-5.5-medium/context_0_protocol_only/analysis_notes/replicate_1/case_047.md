Active sequence from inputs/sequence.xml: Rabimodulated.xml / rabi_pulse_mod_wait_time with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. The relevant variables are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, switch_delay = 100 ns, delay_wrt_1mus = 200 ns, and full_expt = 0.

Readout roles from the instructions: after adj_polarize, the first detection acquires the true 0-level reference. The optional 1-level reference block is inactive because full_expt = 0. The active Rabi-modulated microwave pulse is then applied, followed by the second detection, which is the post-pulse signal readout.

The two combined raw readouts are noisy and mostly share a gradual upward drift with frequency. Comparing the post-pulse signal to the 0-level reference does not reveal a stable ODMR-like resonance dip or a reproducible localized contrast feature across the sweep. The largest feature is an upward signal excursion near 3.915 GHz, not a clear fluorescence decrease, and it is not enough to identify a pODMR resonance from these raw readouts.

Decision: resonance_absent.
