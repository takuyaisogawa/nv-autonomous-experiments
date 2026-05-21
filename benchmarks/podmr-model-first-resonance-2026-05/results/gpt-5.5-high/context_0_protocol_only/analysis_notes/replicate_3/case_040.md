Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The XML executes an initial polarization and detection before any microwave pulse, so readout 1 is the bright/0-level reference. Because full_expt = 0, the optional 1-level reference block is skipped. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the microwave-pulse signal readout. The sample rate is 250 MHz, so the 52 ns pulse is exactly 13 samples after rounding.

The raw readouts are noisy with only two averages, but the sequence-relevant comparison is readout 2 relative to the immediately preceding reference readout 1. Around 3.895-3.900 GHz, readout 2 drops below readout 1 by about 2.06 and 2.12 counts, corresponding to roughly -4% normalized contrast, then recovers by 3.905-3.910 GHz. The per-average traces are not perfectly clean, but both averages contribute negative contrast near this region, while isolated excursions elsewhere are less resonance-like because they are single-point or inconsistent with neighboring points.

Decision: a weak pODMR resonance is present, centered approximately near 3.90 GHz.
