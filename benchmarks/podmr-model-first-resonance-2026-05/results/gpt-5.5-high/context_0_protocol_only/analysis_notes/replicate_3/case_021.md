Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the "Acquire 1 level reference" block is inactive. The active detections are:
- readout 1: detection immediately after adj_polarize, the true 0 level/reference readout.
- readout 2: detection after rabi_pulse_mod_wait_time, the microwave-modulated signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, giving a 52 ns pulse. The provided sequence variables set mod_depth = 1.

The combined signal readout has a pronounced dip around 3.875-3.88 GHz, dropping from roughly 39 counts to about 31 counts. The same dip is visible in both per-average traces for readout 2, while readout 1 remains comparatively stable and does not show the same deep minimum. This is consistent with a real pODMR resonance rather than a reference fluctuation.
