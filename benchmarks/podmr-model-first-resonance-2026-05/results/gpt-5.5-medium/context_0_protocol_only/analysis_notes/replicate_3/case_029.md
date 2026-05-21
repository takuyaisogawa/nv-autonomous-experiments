Active sequence: Rabimodulated.xml / Rabimodulated, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Relevant XML settings:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active microwave pulse is 52 ns.
- mod_depth = 1.
- full_expt = 0, so the optional 1-level reference block is skipped.
- The active readouts are the first detection after polarization, used as the true 0/reference readout, and the later detection after the modulated Rabi pulse, used as the microwave-sensitive signal readout.

Decision:
Readout 2, the post-microwave signal readout, has a clear localized fluorescence dip around 3.875-3.880 GHz, reaching about 39 counts from a baseline near 46-48 counts. The dip is visible in both per-average traces and is not mirrored in readout 1, which remains comparatively flat and noisy. This pattern is consistent with a pODMR resonance being present.
