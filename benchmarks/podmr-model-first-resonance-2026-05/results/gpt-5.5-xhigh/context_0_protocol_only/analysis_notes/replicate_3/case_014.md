The provided sequence XML is Rabimodulated.xml, run as a microwave-frequency scan. The active variables show sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns, and full_expt = 0. Because full_expt is zero, the optional 1-level reference block is skipped even though do_adiabatic_inversion is true.

Readout role interpretation from the active instructions:
- readout 1 is the first detection immediately after adj_polarize, so it is the true 0-level optical reference.
- readout 2 is the detection after rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth = 1, so it is the pODMR-sensitive readout.

The combined raw data show readout 2 dropping strongly around 3.875 GHz: about 28.8 at 3.875 GHz and about 31.0 at 3.880 GHz, compared with nearby values mostly in the mid to high 30s. The same dip appears in both averages, while readout 1 remains comparatively flat around 38-40 and does not show a matching resonance-like decrease. This pattern is consistent with a real pODMR resonance in the pulse-affected readout rather than a reference or common-mode artifact.
