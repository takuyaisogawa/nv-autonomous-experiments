Active sequence and parameters:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction flow first polarizes and detects the true 0-level reference, then waits.
- The optional 1-level reference block is inactive because full_expt = 0, so only two readouts are expected here: readout 1 is the 0-level/reference detection and readout 2 is the detection after the microwave pulse.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.

Resonance assessment:
The raw readouts show a broad upward drift with frequency and point-to-point scatter in both readouts. The signal readout after the microwave pulse does not show a reproducible, localized dip or peak relative to the reference across the two averages. Several isolated excursions are comparable to the average-to-average variation, and there is no coherent resonance-like feature over adjacent frequency points. Based on the active sequence and the raw readouts, I classify this case as resonance absent.
