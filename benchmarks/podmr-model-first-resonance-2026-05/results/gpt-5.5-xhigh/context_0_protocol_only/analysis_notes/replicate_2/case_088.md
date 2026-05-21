The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active sequence uses sample_rate = 250 MHz, length_rabi_pulse = 52 ns after rounding, mod_depth = 1, switch_delay = 100 ns, and full_expt = 0. Because full_expt is zero, the optional 1-level reference block is skipped.

The active detection windows are therefore:
1. Readout 1: detection immediately after adj_polarize, serving as the bright/0-state reference.
2. Readout 2: detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), serving as the microwave-pulse signal readout.

I normalized the post-pulse signal readout against the preceding bright reference by comparing readout 2 minus readout 1 and readout 2/readout 1 across the microwave-frequency sweep. The strongest negative contrast appears near 3.895 to 3.900 GHz: readout 2 is lower than readout 1 by about 2.92 counts at 3.895 GHz and 3.92 counts at 3.900 GHz, corresponding to roughly -5.8% and -7.7% contrast. This local dip is followed by recovery above the reference at 3.905 GHz and above, which supports an on-resonance response rather than a flat trace. The individual averages are noisy, but both contribute negative contrast in this region, with the deepest point split between the two adjacent frequencies.

Decision: a pODMR resonance is present, centered approximately around 3.895 to 3.900 GHz.
