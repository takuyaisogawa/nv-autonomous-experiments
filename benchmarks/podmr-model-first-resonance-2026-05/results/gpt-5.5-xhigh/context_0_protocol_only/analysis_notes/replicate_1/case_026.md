Sequence inspection:

The active pulse sequence is the Rabimodulated pODMR frequency scan. The scan varies mw_freq across 3.825-3.925 GHz in 5 MHz steps. In the provided sequence XML, mod_depth is 1 and length_rabi_pulse is 5.2e-08 s, i.e. 52 ns after the sample-rate rounding step.

Readout roles:

The first detection occurs immediately after optical polarization and is marked in the XML as the true 0 level reference. Because full_expt is 0, the optional 1 level reference branch is inactive. The active microwave operation is then rabi_pulse_mod_wait_time using the 52 ns pulse and mod_depth 1, followed by the second detection. Thus readout 1 is the 0-state reference and readout 2 is the signal after the modulated microwave pulse.

Data assessment:

Readout 1 stays comparatively flat near 41-43 counts across the frequency scan. Readout 2 shows a strong, localized, repeatable dip near 3.875-3.880 GHz, dropping from about 42 counts off resonance to 34.75 at 3.875 GHz and 33.10 at 3.880 GHz. The same trough is visible in both averages, while the reference readout does not show a matching depression. This is consistent with a pODMR resonance being present.
