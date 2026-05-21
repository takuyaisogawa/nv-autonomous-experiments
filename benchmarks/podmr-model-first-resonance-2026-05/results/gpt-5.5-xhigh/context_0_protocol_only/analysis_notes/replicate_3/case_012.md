Sequence review:

The provided sequence is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active flow is polarization, immediate detection, wait, then a modulated Rabi microwave pulse followed by final detection. The optional "Acquire 1 level reference" block is inactive because full_expt = 0, so the adiabatic-inversion path is not used.

Readout roles:

Readout 1 is the true 0-level/reference fluorescence readout collected immediately after optical polarization, before the swept microwave pulse. Readout 2 is the signal fluorescence readout collected after the active rabi_pulse_mod_wait_time call.

Pulse settings from the provided XML:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, i.e. 52 ns
- sample_rate = 250 MHz, so the 52 ns pulse is exactly 13 samples after rounding

Data assessment:

The combined traces and per-average overlay show strong point-to-point scatter. Comparing readout 2 against readout 1 gives alternating positive and negative contrast excursions across the scan rather than a smooth, localized ODMR dip or peak. The largest positive average contrasts appear near 3.895 GHz and at the high-frequency edge, while negative extrema appear near 3.860 GHz and 3.885 GHz; these do not form a consistent resonance shape across neighboring frequencies. With only two averages, the per-average traces do not support a reproducible resonance feature.

Decision: resonance absent.
