Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Relevant sequence details:
- The sequence first polarizes the NV and performs a detection readout before any microwave pulse; this is the true 0-level/reference readout.
- The optional 1-level reference block is inactive because full_expt = 0, despite do_adiabatic_inversion being true.
- The active signal operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection readout.
- The pulse duration is rounded at 250 MS/s, so 52 ns corresponds to 13 samples and remains 52 ns.

Readout assessment:
The two combined raw readouts are close in scale and both show a broad downward drift across the sweep with point-to-point noise. The signal readout does not show a distinct localized dip or peak relative to the reference that would indicate a pODMR resonance. Per-average traces show substantial offset between averages and similar noisy behavior, making the apparent variations better explained by drift/noise than by a reproducible resonance.

Decision: resonance absent.
