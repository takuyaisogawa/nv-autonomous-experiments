Case podmr_038_2026-05-16-214551.

The provided sequence is Rabimodulated.xml. The active instructions first polarize and detect a true 0-level reference, then wait. The 1-level reference block is inactive because full_expt is 0. The measurement block then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection. Therefore readout 1 is the pre-microwave true 0 reference and readout 2 is the post-52 ns modulated Rabi-pulse signal readout. The variable table reports length_rabi_pulse = 5.2e-08 s, mod_depth = 1, and the scan varies mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

For a pODMR resonance I would expect a localized, repeatable contrast feature in the signal readout relative to the reference over the microwave-frequency sweep. The combined traces show point-to-point fluctuations and some broad drift, but the difference between readout 2 and readout 1 changes sign and does not form a stable dip or peak. The per-average overlay also shows substantial average-dependent offsets, especially between the two averages, so apparent excursions in the combined trace are not convincing as a resonance.

Decision: resonance_absent.
