Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the pulse duration rounds to 52 ns. The active instruction flow first polarizes and detects a true 0-level reference. The "Acquire 1 level reference" block is inactive because full_expt = 0. The sequence then applies rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth = 1, followed by the second detection. Thus readout 1 is the no-microwave 0-level reference, and readout 2 is the post-Rabi-pulse signal readout.

For a pODMR resonance in this sequence, the post-pulse signal should show a coherent frequency-localized contrast relative to the reference, normally as reduced fluorescence from resonant transfer out of the bright state. The combined readout 2/reference ratio ranges roughly from 0.943 to 1.092, but the apparent negative contrasts at 3.830 and 3.855 GHz are isolated single-point dips rather than a clear pulse-width-limited feature. The largest positive excursion near 3.910-3.915 GHz is not consistent with the expected sign and is strongly affected by the individual-average scatter. Across the two averages, the contrast alternates sign at several neighboring points and does not form a reproducible resonance line.

Decision: resonance_absent.
