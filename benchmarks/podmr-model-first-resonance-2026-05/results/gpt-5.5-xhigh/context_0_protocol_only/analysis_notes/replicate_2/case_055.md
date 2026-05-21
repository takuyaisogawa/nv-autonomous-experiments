Active sequence and parameters:

- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active microwave pulse: rabi_pulse_mod_wait_time after the initial reference detection.
- Pulse duration: length_rabi_pulse = 5.2e-08 s, which remains 52 ns after sample-rate rounding at 250 MHz.
- mod_depth: 1 from the provided sequence XML / active variable values.
- full_expt = 0, so the optional 1-level reference block is inactive; do_adiabatic_inversion is not used in the active path.

Readout roles:

- Readout 1 is the first detection after adj_polarize and is the polarized 0-level fluorescence reference.
- Readout 2 is the detection after the active Rabi-modulated microwave pulse and is the pODMR signal readout.

Decision:

Readout 1 stays comparatively flat near 46 counts across the scan. Readout 2 shows a coherent reduction relative to readout 1 from about 3.880 GHz through 3.900 GHz, with the strongest point at 3.895 GHz: readout 2 = 43.50 versus readout 1 = 46.10, ratio about 0.944. The same depressed region is visible in both per-average readout-2 traces, followed by recovery near 3.905 GHz. This pattern is consistent with a pODMR resonance rather than an isolated single-point fluctuation.

Prediction: resonance_present.
