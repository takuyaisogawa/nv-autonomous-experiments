Sequence inspection:

The active sequence is Rabimodulated.xml. It varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect a true 0-level reference, then wait. The optional 1-level reference block is inactive because full_expt = 0. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection.

Readout roles:

Readout 1 is the true 0-level reference acquired after optical polarization and before the microwave pulse. Readout 2 is the signal readout acquired after the modulated Rabi pulse. Because the 1-level reference block is skipped, there are only these two active readouts.

Pulse parameters:

The provided sequence XML gives length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active pulse duration is 52 ns. The provided sequence XML gives mod_depth = 1. The microwave frequency is swept over the pODMR scan.

Resonance assessment:

The raw readouts are noisy and do not show a stable, frequency-localized ODMR feature. Readout 2 does not show a clear dip or peak relative to readout 1 that persists across averages. The apparent fluctuations are comparable to the per-average scatter and the combined traces cross several times. The high-frequency end trends downward in both readouts, which looks like shared drift rather than a distinct resonance contrast. I therefore classify this case as resonance absent.
