Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

The XML/instructions set up an initial polarization and detection as the true 0-level reference, then because full_expt = 0 the optional 1-level reference block is skipped. The active experiment pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns, followed by detection. Thus the readouts should be interpreted as the baseline/reference readout and the post-Rabi-pulse signal readout, not as a full 0/1 reference-normalized experiment.

The two combined raw readouts both wander upward over the frequency range with point-to-point fluctuations. There is no clear, reproducible pODMR resonance signature such as a localized fluorescence dip in the signal readout relative to the reference; the most prominent feature is instead a high point near the upper end of the scan in readout 2. The two averages shown in the overlay also have substantial scatter and do not support a stable resonance feature.

Decision: resonance_absent.
