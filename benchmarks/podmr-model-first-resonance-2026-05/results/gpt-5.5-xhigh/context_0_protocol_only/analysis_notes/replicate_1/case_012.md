Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence sets full_expt = 0, so the intermediate "1 level reference" block is skipped. The active detections are:
- readout 1: detection immediately after optical polarization, serving as the true 0-level/reference readout.
- readout 2: detection after rabi_pulse_mod_wait_time, serving as the microwave-driven signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, i.e. 52 ns. With the 250 MHz sample rate this is already aligned to the 4 ns sample grid. The active mod_depth is 1.

For a pODMR resonance from this sequence, I would expect the post-pulse signal readout to show a reproducible fluorescence dip relative to the reference near the resonance frequency. The combined readouts show point-to-point scatter of similar size to any possible feature. The readout-2/readout-1 ratio has isolated low points near 3.860 and 3.885 GHz, but these are not a coherent resonance line and the per-average traces do not show a consistent dip at the same frequency. The two averages mainly show noisy baseline variation and drift-like changes.

Decision: resonance_absent.
