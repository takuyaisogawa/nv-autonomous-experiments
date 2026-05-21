Active sequence inspection:

- Sequence: Rabimodulated.xml, with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active instructions: polarize, detection, wait, then a rabi_pulse_mod_wait_time call, then detection. The optional "Acquire 1 level reference" block is inactive because full_expt = 0.
- Readout roles: readout 1 is the initial polarized/0-level reference detection; readout 2 is the detection after the modulated microwave pulse.
- Pulse settings: length_rabi_pulse = 52 ns before sample-rate rounding; sample_rate = 250 MHz, so the rounded duration remains 52 ns. mod_depth = 1 in the provided sequence XML. switch_delay = 100 ns.

Resonance assessment:

The two raw readouts fluctuate substantially across the scan and between the two averages, with no reproducible localized dip or dispersive feature in the post-pulse readout relative to the reference. The largest changes are isolated point-to-point variations and average-dependent baseline shifts rather than a stable ODMR contrast feature. Because the active sequence is a pODMR frequency scan and the signal channel does not show a coherent resonance-like suppression against the reference, I classify this case as resonance absent.
