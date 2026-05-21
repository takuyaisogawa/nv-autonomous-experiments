Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional 1-level reference block is inactive. The active readouts are therefore:
- readout 1: detection immediately after adj_polarize, the polarized 0-level/reference readout.
- readout 2: detection after rabi_pulse_mod_wait_time, the microwave-driven signal readout.

Pulse parameters from the provided XML/variable values: mod_depth = 1, length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz this remains 13 samples, or 52 ns.

The combined signal-reference difference is noisy, but the largest negative contrast occurs at 3.890 GHz: readout 1 = 47.519 and readout 2 = 44.250, a -3.269 count difference (-6.88%). This same sign appears in both averages at that frequency. Other negative excursions exist, but they are less consistent between averages or are not as strong. The feature is narrow, but a single-bin dip is plausible with a 5 MHz scan step.

Decision: resonance_present, with the resonance assignment based on the localized post-pulse fluorescence dip relative to the polarized reference.
