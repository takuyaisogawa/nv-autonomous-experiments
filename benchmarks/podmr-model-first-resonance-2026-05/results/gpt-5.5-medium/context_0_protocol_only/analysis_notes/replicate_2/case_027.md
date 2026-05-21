Active pulse sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence has full_expt = 0, so the optional 1-level reference block is skipped. The active readouts are therefore:
- readout 1: true 0-level reference acquired after adj_polarize and detection, before the microwave pulse.
- readout 2: signal readout acquired after rabi_pulse_mod_wait_time and detection.

Relevant pulse settings from the provided XML/exported variable values:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns
- mw_freq is the scanned variable; detuning = 0

Decision: resonance_present.

Reasoning: readout 2 shows a pronounced, localized ODMR-like fluorescence dip centered around roughly 3.875-3.880 GHz, dropping from a baseline near 41-43 counts to about 34 counts, while readout 1 remains comparatively flat without the same feature. The per-average overlay shows the dip in both averages, so it is not just a single-average fluctuation.
