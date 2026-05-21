Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence has full_expt = 0, so the optional "1 level reference" block is inactive. The executed readout roles are therefore:
- readout 1: true 0-level / bright reference after optical polarization and before the microwave Rabi pulse.
- readout 2: signal readout after the microwave rabi_pulse_mod_wait_time block.

Pulse settings from the provided sequence XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns.

The combined data show readout 1 staying relatively flat near 41-43 counts across the scan, while readout 2 has a pronounced and repeatable dip centered near 3.875-3.880 GHz, falling from the low 40s to about 33 counts. The same dip appears in both averages in the per-average overlay, which argues against a single noisy point or reference drift. Since the dip is in the post-microwave signal readout and not in the bright reference readout, this is consistent with a pODMR resonance.
