The sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz. The active instructions first polarize and detect a true 0-level reference, then skip the 1-level reference because full_expt is 0, then apply rabi_pulse_mod_wait_time and detect the microwave-pulse signal. The pulse duration is length_rabi_pulse = 52 ns after sample-rate rounding, and mod_depth is 1 in the variable values used for the run.

Thus readout 1 is the 0-level reference and readout 2 is the post-modulated-Rabi-pulse signal. Comparing readout 2 against readout 1 is the relevant resonance indicator. The signal/reference ratio shows its clearest trough around 3.895-3.900 GHz, with readout 2 below the reference at both points and recovery at the neighboring higher-frequency point. The feature is not perfectly smooth because there are only two averages and visible noise, but it is sequence-consistent and stronger than the surrounding scatter.

Decision: pODMR resonance present.
