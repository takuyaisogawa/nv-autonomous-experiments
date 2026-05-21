Case podmr_044_2026-05-16-232730

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The active sequence first polarizes and detects the true 0-level reference, waits, skips the optional 1-level reference because full_expt = 0, then applies rabi_pulse_mod_wait_time followed by detection. The active MW pulse uses length_rabi_pulse = 52 ns, rounded at 250 MS/s, and mod_depth = 1 in the provided XML/current variable values. do_adiabatic_inversion is set but not active because that block is commented/skipped.

Readout roles: readout 1 is the polarized reference detection before the MW pulse; readout 2 is the detection after the modulated Rabi pulse. Since full_expt = 0, there is no separate active 1-level reference readout.

The raw readouts mostly show slow drift and average-to-average offsets. The post-pulse/reference ratio fluctuates around 1.003 with point-to-point scatter and no reproducible ODMR-like resonance feature across the frequency sweep. There is a low point near 3.865 GHz, but it is isolated and comparable to the noise/scatter rather than a coherent resonance line shape.

Decision: resonance_absent.
