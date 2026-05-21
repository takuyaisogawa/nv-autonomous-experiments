Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes and detects a true 0-level reference. Because full_expt = 0, the optional 1-level reference block is inactive. The second active readout is the signal after a rabi_pulse_mod_wait_time call using length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.

Readout role interpretation:
- readout 1: pre-microwave true 0-level reference.
- readout 2: post-microwave modulated Rabi-pulse signal.

The raw readouts and the signal/reference comparison show no stable pODMR resonance. There are scattered single-point deviations, including apparent dips near 3.855 GHz and 3.91 GHz, but they are not supported by a consistent, reproducible feature across the two averages. The traces are dominated by point-to-point noise and shared drift rather than a coherent resonance-shaped contrast change.

Decision: resonance_absent.
