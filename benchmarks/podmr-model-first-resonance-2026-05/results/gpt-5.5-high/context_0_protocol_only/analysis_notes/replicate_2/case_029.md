Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence sets full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. The readout roles are therefore:
- readout 1: true 0-level reference after adj_polarize and detection, before the microwave pulse.
- readout 2: signal readout after rabi_pulse_mod_wait_time and detection.

The microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, i.e. 52 ns. With sample_rate = 250 MHz this is exactly 13 samples after rounding. The sequence file sets mod_depth = 1.

The reference readout remains near 46 to 49 counts over the scan without a matching feature. The signal readout shows a clear, localized reduction near 3.875 to 3.880 GHz, dropping to about 39 counts, and this dip is present in both per-average traces. Because the feature appears in the signal channel after the microwave pulse and not in the reference channel, it is consistent with a pODMR resonance.
