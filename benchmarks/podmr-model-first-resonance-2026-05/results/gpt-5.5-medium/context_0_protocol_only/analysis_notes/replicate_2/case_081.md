Case podmr_067_2026-05-17-074342.

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The active instructions first perform adj_polarize and detection to acquire the true 0-level reference. The optional 1-level reference block is inactive because full_expt = 0, so only two readouts are active: readout 1 is the pre-microwave 0-level/reference detection and readout 2 is the detection after the Rabi-modulated microwave pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. The XML variable values for this run set mod_depth = 1, with switch_delay = 100 ns. Although do_adiabatic_inversion is true, the adiabatic inversion calls are commented out and the conditional reference block is skipped, so it is not part of the active pulse sequence.

The combined raw readouts fluctuate around roughly 48 to 50 counts. The post-pulse readout does not show a clear, localized, reproducible dip or peak relative to the reference across the frequency sweep. The per-average overlay shows substantial average-to-average variation, including endpoint and isolated-point excursions, so the apparent differences are consistent with noise rather than a pODMR resonance.

Decision: resonance_absent.
