Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The instructions first run adj_polarize followed by detection, which is the true 0-level reference. The optional 1-level reference branch is disabled because full_expt = 0. After that, the active measurement applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, then performs the second detection. Therefore readout 1 is the pre-pulse 0-level reference and readout 2 is the post-rabi-pulse signal readout.

Decision: resonance_absent.

The signal readout does not show a localized, repeatable pODMR contrast feature relative to the reference. The combined readout2-readout1 contrast fluctuates between negative and positive values with several isolated extrema, and the two averages do not reproduce a coherent dip or line shape. The apparent low points are comparable to point-to-point and average-to-average scatter rather than a convincing resonance.
