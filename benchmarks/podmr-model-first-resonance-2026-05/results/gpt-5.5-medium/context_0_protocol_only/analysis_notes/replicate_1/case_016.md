Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the pulse duration is already an integer 13 samples, so the active Rabi pulse remains 52 ns.

Readout roles from the active instructions:
- The first detection occurs immediately after adj_polarize and is the true 0-level reference.
- full_expt = 0, so the optional 1-level reference block is skipped.
- The second detection occurs after rabi_pulse_mod_wait_time using the 52 ns pulse and mod_depth = 1, so it is the pODMR signal readout.

The signal readout shows a pronounced dip across the middle of the frequency scan, reaching its minimum near 3.880 GHz. This dip is much stronger and more structured than the fluctuations in the reference readout and is visible in both averages. The feature is therefore consistent with a pODMR resonance.
