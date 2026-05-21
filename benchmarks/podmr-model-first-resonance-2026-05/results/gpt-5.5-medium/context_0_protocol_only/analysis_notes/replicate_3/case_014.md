Case podmr_033_2026-05-15-233800.

The provided sequence is Rabimodulated.xml and scans mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect a reference readout, then, because full_expt is 0, skip the optional 1-level reference block. The active signal operation is rabi_pulse_mod_wait_time followed by detection.

Readout roles: readout 1 is the initial 0-level/reference fluorescence detection before the microwave pulse; readout 2 is the detection after the modulated Rabi pulse. The exported variable values show mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, i.e. 52 ns after sample-rate rounding.

The reference readout stays relatively flat near 38-40 counts across the scan. The post-pulse readout has a pronounced localized dip near 3.875 GHz: the combined readout 2 drops to about 28.8 counts while neighboring and off-resonant values are mostly in the mid/high 30s. The per-average traces both show a dip at the same scan point, so this is not just a single-average fluctuation. Since the dip is in the post-pulse readout and not mirrored in the reference readout, it is consistent with a pODMR resonance.
