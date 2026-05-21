Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The XML and exported variable values show sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, and length_last_wait = 1 us. Because full_expt is zero, the optional 1-level reference block is inactive. The executed readout roles are therefore: first detection after adj_polarize is the true 0-level/reference readout; second detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) is the microwave-driven signal readout.

The combined raw traces both show a broad downward drift over frequency. Comparing the driven signal readout to the preceding reference readout does not reveal a consistent resonance-shaped dip: the signal/reference ratio has alternating point-to-point excursions, with low points near 3.855, 3.875, 3.905, and 3.915 GHz and intervening high points. The per-average overlay also shows offset/drift between averages rather than a reproducible narrow pODMR feature.

Decision: resonance_absent.
