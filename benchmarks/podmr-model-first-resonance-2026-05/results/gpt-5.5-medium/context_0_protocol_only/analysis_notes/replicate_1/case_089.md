Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The provided XML sets length_rabi_pulse to 52 ns and mod_depth to 1, with full_expt = 0, so the optional 1-level reference block is skipped.

Readout roles: the first detection after adj_polarize is the true 0-level/reference readout. The second detection follows rabi_pulse_mod_wait_time with the 52 ns modulated microwave pulse and is the signal readout. Therefore I compare readout 2 against readout 1 rather than treating the two traces as separate resonances.

The raw traces drift upward with frequency and are noisy with only two averages, but the paired signal/reference contrast has a repeated negative excursion near 3.900 GHz: combined readout2/readout1 is about 0.958 there, and both individual averages show readout 2 below readout 1 at that point. There are other one-point excursions, including near 3.830 GHz, but the 3.900 GHz dip is a credible microwave-induced fluorescence reduction in this pulse sequence.

Decision: resonance_present.
