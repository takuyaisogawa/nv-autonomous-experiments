Active sequence assessment:

The supplied sequence is Rabimodulated.xml. The instruction flow first polarizes the NV and detects the true 0-level reference, then waits. The optional 1-level reference block is disabled because full_expt is 0, even though do_adiabatic_inversion is true. The active experiment readout after that is a rabi_pulse_mod_wait_time call followed by detection.

Readout roles:

Readout 1 is the initial post-polarization reference detection. Readout 2 is the detection after the modulated Rabi pulse and is the readout expected to carry pODMR contrast versus mw_freq. There is no active separate 1-level reference readout because the full_expt conditional is false.

Pulse parameters:

The sequence XML gives length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active pulse duration remains 52 ns. The XML variable table gives mod_depth = 1 for the active modulated Rabi pulse.

Resonance decision:

The mw_freq scan runs from 3.825 GHz to 3.925 GHz. Readout 2 shows a strong localized dip around 3.875-3.880 GHz, falling from a typical high-30s baseline to about 30.3-30.6, and the per-average overlay shows the same depression in both averages. Readout 1 stays comparatively flat through this region and even peaks near the dip, so the feature is not a common-mode count-rate loss. This is consistent with a pODMR resonance being present.
