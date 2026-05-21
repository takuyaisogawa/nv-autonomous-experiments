Sequence inspection:
- Active sequence: Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is skipped.
- Readout 1 role: initial true 0-level/no-MW reference after polarization and detection.
- Readout 2 role: signal detection after the active microwave Rabi pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Resonance assessment:
The combined readouts show a broad baseline drift over the scan rather than a localized, reproducible ODMR-like contrast feature. The per-average traces are not consistent with each other; individual averages have large opposing baseline trends, so the combined readout shape is not reliable evidence of a resonance. The signal/reference contrast has a few isolated negative excursions near the high-frequency side, but these are not smooth or repeatable and are mixed with comparable positive excursions. Based on the active Rabimodulated sequence and the raw readout behavior, I do not identify a pODMR resonance in this case.
