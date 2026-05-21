Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active instructions first polarize and detect a true 0-level/reference readout. Because full_expt is 0, the optional 1-level reference block is skipped. The only microwave-driven measurement readout is after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Thus the two stored readouts are interpreted as the polarized reference and the post-rabi-pulse signal.

The combined post-pulse signal relative to the reference has a near-zero mean difference and alternates sign across the scan. The largest apparent contrast excursions are comparable to the scatter and are not reproducible between the two averages: one average has its strongest positive feature near 3.875 GHz, while the other has the strongest positive feature near 3.910 GHz. Both raw readouts also share broad drift over the scan, which does not isolate a stable frequency-localized ODMR feature.

Decision: no reliable pODMR resonance is present in this case.
