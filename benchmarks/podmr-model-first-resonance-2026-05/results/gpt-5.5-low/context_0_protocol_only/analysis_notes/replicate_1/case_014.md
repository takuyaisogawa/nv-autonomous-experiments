Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- First detection follows adj_polarize and is the true 0 level reference.
- full_expt is 0, so the optional 1 level reference block is inactive.
- Second detection follows rabi_pulse_mod_wait_time and is the microwave-driven pODMR readout.

Key pulse settings:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns
- switch_delay = 1e-07 s

Decision:
The driven readout shows a pronounced, localized dip near 3.875 GHz, falling from the high-30s baseline to about 28.8, while the 0-reference readout stays comparatively flat. The dip appears in the per-average traces as well, so it is not only a single combined-point artifact. This is consistent with a pODMR resonance being present.
