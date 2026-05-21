Sequence XML inspection:

The active sequence is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250000000 samples/s, the rounded pulse duration remains 52 ns, or 13 samples.

The instruction block first acquires a true 0-level bright reference using polarization followed by detection. Because full_expt = 0, the separate 1-level reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth = 1, followed by the second detection. Therefore readout 1 is the bright/reference readout, and readout 2 is the post-pulse pODMR signal readout.

The combined post-pulse signal readout shows a localized dip around 3.875 to 3.880 GHz, reaching its minimum at 3.880 GHz. At that point readout 2 is about 29.31 while readout 1 is about 35.65, giving the lowest normalized signal ratio in the sweep. Neighboring points recover, and the reference readout does not show the same localized depression. This supports a pODMR resonance being present.
