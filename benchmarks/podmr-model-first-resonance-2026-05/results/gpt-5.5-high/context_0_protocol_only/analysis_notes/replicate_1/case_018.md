Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence has sample_rate 250 MHz, length_rabi_pulse 52 ns after rounding, mod_depth 1, and full_expt = 0. Because full_expt is zero, the optional 1-level reference block is skipped.

Readout roles: readout 1 is the detection immediately after optical polarization, before the MW Rabi pulse, so it is the bright/0 reference for each scan point. Readout 2 is the detection after the modulated 52 ns MW Rabi pulse, so it is the pODMR signal channel. The sequence then waits length_last_wait = 1 us.

Decision: readout 2 shows a pronounced localized fluorescence drop around 3.875-3.880 GHz, falling to about 29.3 and 28.1 while readout 1 stays near 35.9 and 40.0 at the same points. The dip is visible in both averages in the per-average overlay, so it is not just a single-average fluctuation. This is consistent with a pODMR resonance.
