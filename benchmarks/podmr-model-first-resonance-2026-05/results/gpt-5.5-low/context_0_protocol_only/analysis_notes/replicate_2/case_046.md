Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The sequence first performs adj_polarize followed by detection, giving the true 0-level reference readout. The full_expt branch is disabled because full_expt = 0, so no separate 1-level reference is acquired. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the final detection. Thus readout 1 is the pre-microwave reference and readout 2 is the pulsed pODMR signal.

Data assessment:

The signal readout has a pronounced localized maximum near 3.875 GHz, reaching about 58.1 while nearby/off-feature values are closer to 54-56. The reference readout does not show the same peak and is lower at the same point, producing the largest signal-reference separation in the scan. The feature is also consistent with the programmed center frequency in the sequence. Although the scan has only two averages and visible noise, the frequency-localized change in the pulsed signal relative to the reference is sufficient to call a pODMR resonance present.
