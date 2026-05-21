Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- The sequence first polarizes and performs detection for the true 0-level reference.
- The optional 1-level reference block is inactive because full_expt = 0.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.
- Therefore readout 1 is the reference readout and readout 2 is the microwave-affected signal readout.

Data assessment:
The combined signal/reference ratio fluctuates around unity with a standard deviation of about 0.032. There are several negative excursions where readout 2 is lower than readout 1, including around 3.880-3.900 GHz, but the pattern is not a clean or repeatable resonance: the apparent low region is interrupted by a strong positive point at 3.895 GHz, and comparable high/low excursions occur elsewhere. The per-average traces are noisy with only two averages, so the feature is not convincing as a real pODMR resonance.

Decision: resonance_absent.
