Sequence inspection:

The active pulse sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first acquire a true 0-level reference by polarization and detection, then wait. Because full_expt is 0, the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true. The active driven measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth before the second detection.

Readout roles:

Readout 1 is the true 0-level reference readout acquired before the microwave pulse. Readout 2 is the readout after the modulated Rabi pulse. There is no active 1-level reference readout in this run.

Key parameters:

mod_depth = 1
length_rabi_pulse = 5.2e-08 s, i.e. 52 ns
mw_freq scan = 3.825e9 to 3.925e9 Hz
averages = 2
repetitions = 100000

Resonance assessment:

The combined raw traces fluctuate around roughly 19-21 counts without a reproducible, localized ODMR-like dip or peak in the pulse readout relative to the reference. The per-average overlay shows strong average-dependent drift: one average trends downward while the other trends upward across the scan, and the averaged combined traces are dominated by that drift/noise rather than by a consistent resonance feature. Around the nominal center and across the full scanned band, readout 2 does not show a clear coherent contrast feature that repeats across averages or stands out from point-to-point scatter.

Decision: resonance_absent.
