Active sequence: Rabimodulated, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided XML sets full_expt = 0, so the "Acquire 1 level reference" branch is inactive. The active readouts are:
- readout 1: the initial true 0-level reference after adj_polarize and detection.
- readout 2: the signal readout after rabi_pulse_mod_wait_time followed by detection.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz, the XML rounding keeps this at 52 ns. The active mod_depth is 1, with switch_delay = 100 ns.

The reference readout remains roughly flat near 40-42 counts across the scan. The post-pulse readout has a strong, repeatable drop centered around 3.875-3.880 GHz, reaching about 32 counts, and the same dip is visible in both per-average traces. Because this contrast is specific to the post-pulse readout and repeats across averages, I classify the scan as showing a pODMR resonance.
