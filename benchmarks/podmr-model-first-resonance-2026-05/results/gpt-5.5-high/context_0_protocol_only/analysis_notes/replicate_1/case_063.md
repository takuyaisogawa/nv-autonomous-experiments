Case podmr_049_2026-05-17-004217.

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz. The active instructions first polarize and detect a true 0-level reference, then skip the 1-level reference branch because full_expt = 0, then apply rabi_pulse_mod_wait_time and detect the post-pulse signal. Therefore readout 1 is the 0 reference and readout 2 is the pODMR signal after the microwave pulse.

The sequence XML and exported variable values give mod_depth = 1. The active rabi pulse duration is length_rabi_pulse = 5.2e-08 s, which is 52 ns and corresponds to 13 samples at the 250 MHz sample rate.

Decision: resonance_absent. The combined readout 2 trace has noisy local highs and lows, but there is no reproducible localized resonance dip in the post-pulse signal relative to the 0 reference. The reference readout also drifts across the sweep, and the per-average contrast features are inconsistent, so the apparent excursions do not support a clear pODMR resonance.
