Sequence XML/readout interpretation:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The microwave pulse used for the pODMR contrast is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns, mw_ampl = -5 dBm, ampIQ = 5 dBm, and freqIQ = 50 MHz. The configured sample rate is 250 MS/s, so the 52 ns pulse is rounded to the nearest 4 ns sample interval and remains 52 ns.

Readout roles:

The first detection occurs immediately after adj_polarize and is the true 0 level/reference readout. The optional 1 level reference block is inactive because full_expt = 0, despite do_adiabatic_inversion being true. The second active detection occurs after the 52 ns modulated Rabi pulse and is the signal readout for the frequency sweep.

Resonance assessment:

The combined readouts show only small, noisy fluctuations over the sweep. The signal readout has a broad low region around roughly 3.895-3.910 GHz, but this is not a sharp or reproducible pODMR dip: the two averages disagree substantially, several adjacent features are comparable in size, and the reference readout also fluctuates by similar magnitude. The signal/reference behavior does not show a clear localized resonance tied to the microwave sweep.

Decision: resonance_absent.
