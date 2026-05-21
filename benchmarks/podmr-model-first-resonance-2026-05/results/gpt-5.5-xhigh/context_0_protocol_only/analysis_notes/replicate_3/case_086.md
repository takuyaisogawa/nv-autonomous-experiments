Active sequence: Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz. The provided XML has full_expt = 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is set. The active detections are therefore: readout 1 is the bright/reference detection after optical polarization with no microwave pulse, and readout 2 is the detection after a rabi_pulse_mod_wait_time microwave pulse.

Pulse settings used for the decision: length_rabi_pulse = 52 ns after rounding to the 250 MHz sample rate grid, mod_depth = 1, switch_delay = 100 ns, and delay_wrt_1mus = 200 ns.

The resonance check should compare the post-pulse readout against the reference as a function of mw_freq. The combined readout 2 minus readout 1 contrast is mostly small and irregular, with alternating positive and negative deviations rather than a localized resonance-shaped dip or peak. The largest negative points occur at several separated frequencies and the individual averages do not show a consistent feature at the same scan position. This looks like measurement scatter and baseline/readout noise rather than a reproducible pODMR resonance.

Decision: resonance_absent.
