Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML sets length_rabi_pulse = 5.2e-08 s and then rounds it to the 250 MHz sample clock, so the active pulse duration remains 52 ns. The XML sets mod_depth = 1. The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.

Readout roles from the instructions:
- Readout 1 is the initial detection after optical polarization, labeled in the XML as the true 0 level reference. It is taken before the modulated microwave pulse.
- The full_expt block for acquiring a 1 level reference is inactive because full_expt = 0.
- Readout 2 is the final detection after the 52 ns modulated microwave pulse, so it is the microwave-sensitive pODMR signal readout.

The scan shows a frequency-localized, reproducible drop in readout 2 around 3.875-3.880 GHz, reaching about 26 counts compared with nearby values near 34-37. The same feature is visible in the per-average overlay, while readout 1 stays comparatively flat and does not show a matching deep dip. Because the active signal readout after the microwave pulse has a clear localized contrast feature, I classify this case as resonance_present.
