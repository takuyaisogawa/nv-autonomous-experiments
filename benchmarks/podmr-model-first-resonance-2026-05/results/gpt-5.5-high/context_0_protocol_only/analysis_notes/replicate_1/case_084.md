Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence XML sets length_rabi_pulse = 5.2e-08 s, sample_rate = 250 MHz, and mod_depth = 1. The pulse duration rounds to the same 52 ns value at this sample rate.

Readout roles:

The first detection occurs after adj_polarize and before any microwave pulse, so readout 1 is the bright/0-level reference for each frequency point. The full_expt variable is 0, so the optional 1-level reference block is inactive. The active measurement then applies rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth 1, followed by detection; this is readout 2, the pODMR signal readout.

Data assessment:

Both raw readouts show a shared downward drift toward the high-frequency end of the scan. The signal readout is sometimes lower than the reference, but the differential trace alternates sign at several neighboring points and does not form a clear reproducible localized resonance feature. The apparent dips near individual points are comparable to the two-average scatter visible in the per-average overlay. Because the only consistent structure is common-mode drift rather than a distinct pODMR contrast feature, I classify this case as resonance absent.
