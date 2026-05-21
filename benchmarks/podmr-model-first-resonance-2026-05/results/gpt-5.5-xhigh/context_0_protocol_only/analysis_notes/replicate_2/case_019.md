Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation from the provided XML:
- sample_rate is 250 MHz, so the programmed 52 ns rabi pulse is exactly 13 samples after rounding.
- mod_depth is 1.
- full_expt is 0, so the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true.
- Readout 1 is the true 0-level reference: adj_polarize followed by detection, before the microwave pulse.
- Readout 2 is the active pODMR signal readout: rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) followed by detection.

Data assessment:
Readout 1 stays comparatively flat around 40-42 counts across the sweep. Readout 2 has a strong localized depression at 3.875-3.880 GHz, dropping to about 32 counts while the paired reference remains about 40-41 counts. The minimum readout2/reference ratio is about 0.785 at 3.875 GHz and 0.787 at 3.880 GHz, and the same dip is visible in both averages. This is the expected pODMR contrast signature rather than a shared readout fluctuation.

Decision: resonance_present.
