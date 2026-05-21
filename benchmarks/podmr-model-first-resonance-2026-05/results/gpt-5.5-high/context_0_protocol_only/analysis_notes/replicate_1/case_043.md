Case podmr_029_2026-05-16-193002.

The provided sequence is Rabimodulated.xml, with mw_freq swept from 3.825e9 to 3.925e9 Hz. The active instructions use full_expt = 0, so the optional "1 level reference" block is skipped. The executed readouts are therefore:

1. Readout 1: detection after adj_polarize, before the Rabi-modulated microwave pulse. This is the polarized/no-MW reference for the bright state.
2. Readout 2: detection after rabi_pulse_mod_wait_time, which is the pODMR signal readout after the microwave pulse.

From the provided XML, the active Rabi pulse uses length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns, with mod_depth = 1. The pulse is followed by detection after delay_wrt_1mus = 2e-07 s.

The signal readout is noisy with only two averages, but readout 2 is systematically lower than the readout 1 reference through much of the middle of the sweep, especially around roughly 3.855e9 to 3.88e9 Hz. This is the expected sign for pODMR contrast in this sequence: on resonance, the microwave pulse transfers population out of the bright reference state and lowers the post-pulse fluorescence. The feature is not a clean smooth Lorentzian and the per-average traces show substantial scatter, but the central reference-normalized suppression is enough to classify the case as having a pODMR resonance present.
