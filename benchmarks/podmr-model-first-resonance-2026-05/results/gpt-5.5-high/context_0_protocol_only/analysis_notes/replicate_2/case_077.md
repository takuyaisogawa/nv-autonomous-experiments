Sequence and roles:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets length_rabi_pulse to 5.2e-08 s, i.e. 52 ns before sample-rate rounding, and mod_depth to 1. The instruction flow first polarizes and performs a detection before any active swept microwave pulse; this is the true 0-level/reference readout. The full_expt variable is 0, so the optional 1-level reference block is skipped. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection; this second readout is the microwave-interrogated pODMR signal readout.

Data assessment:

Both raw readouts show a broad downward drift toward the high-frequency end of the sweep. A true pODMR resonance should appear as a reproducible localized feature in the microwave-interrogated readout relative to the reference, or in the normalized contrast between the two readouts. Here the readout-2 minus readout-1 contrast changes sign repeatedly from point to point and does not form a stable localized resonance-like dip or peak. The largest deviations are isolated and not consistently reproduced between the two averages in the per-average overlay. The apparent high-frequency decrease is common-mode drift visible in both readouts rather than a distinct microwave-dependent resonance.

Decision: resonance_absent.
