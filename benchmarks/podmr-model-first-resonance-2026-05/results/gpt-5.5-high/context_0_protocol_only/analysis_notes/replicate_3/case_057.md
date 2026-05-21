Sequence XML: Rabimodulated.xml, sweeping mw_freq across 3.825 to 3.925 GHz. The active instructions first polarize and detect the bright/0-level reference, then because full_expt = 0 the optional 1-level reference block is skipped. The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, mod_depth = 1, switch_delay = 1e-07 s, followed by the second detection. Thus readout 1 is the 0-level reference before the microwave pulse, and readout 2 is the post-pulse signal readout.

The two-average raw traces are noisy and the post-pulse signal does not show a consistent, localized resonance feature relative to the reference across the frequency sweep. The signal-reference difference changes sign and contains broad excursions and isolated high points, but no stable ODMR-like dip or peak that is reproducible enough to identify as a pODMR resonance.

Decision: resonance_absent.
