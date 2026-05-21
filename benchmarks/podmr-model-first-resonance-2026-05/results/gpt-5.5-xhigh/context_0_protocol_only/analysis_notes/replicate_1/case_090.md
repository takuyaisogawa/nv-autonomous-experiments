Sequence review:

The active sequence is Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, length_rabi_pulse is 5.2e-08 s and is rounded at 250 MS/s, leaving an active 52 ns Rabi pulse. mod_depth is 1. The do_adiabatic_inversion variable is set, but the adiabatic inversion calls are commented and the only non-commented "1 level reference" block is gated by full_expt. Since full_expt is 0, that block is inactive.

Readout roles:

The first active detection occurs immediately after adj_polarize and before the microwave Rabi pulse, so readout 1 is the polarized/0-level reference. The second active detection occurs after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so readout 2 is the pODMR signal readout after the 52 ns modulated microwave pulse.

Data assessment:

The combined signal readout has a clear low point near 3.905 GHz, and relative to the reference the combined contrast there is about -5.2 percent. The two individual averages both show negative post-pulse contrast at that same point, roughly -4.4 percent and -6.1 percent, which makes this feature more convincing than the isolated edge and single-average excursions elsewhere. The trace is noisy and sparse, but the active signal readout contains a repeatable negative contrast feature consistent with a pODMR resonance.

Decision: resonance present.
