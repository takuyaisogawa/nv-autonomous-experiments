Active sequence: Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence.xml has full_expt = 0, so the intermediate 1-level reference block is inactive. The first active detection follows adj_polarize and is the true 0-level / pre-microwave reference. The second active detection follows rabi_pulse_mod_wait_time and is the post-microwave signal readout.

The provided sequence.xml sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz the rounding leaves a 52 ns pulse, so the active microwave pulse is a 52 ns full-depth rabi_pulse_mod_wait_time pulse before the signal readout.

The combined readout contrast, using readout 2 minus readout 1, is mostly positive at lower frequencies but develops localized negative contrast at the high-frequency side. The clearest combined negative points are near 3.895 GHz and 3.915 GHz, both about -1.365 counts or roughly -5.3 percent relative to readout 1. The individual averages are noisy and there is a positive outlier around 3.905 GHz, but both averages show negative post-pulse contrast at 3.895 GHz and again around 3.915 to 3.920 GHz.

Decision: resonance_present. The feature is noisy, but the post-microwave signal falls below the pre-microwave reference at reproducible high-frequency points, consistent with a weak pODMR resonance.
