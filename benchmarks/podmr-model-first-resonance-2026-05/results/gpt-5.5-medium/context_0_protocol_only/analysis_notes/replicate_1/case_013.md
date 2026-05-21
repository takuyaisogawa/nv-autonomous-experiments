Active pulse sequence: Rabimodulated.xml / Rabimodulated. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- The first detection follows adj_polarize before any MW pulse and is the true 0-level/reference readout.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The second detection follows rabi_pulse_mod_wait_time and is the pODMR signal readout.

Pulse settings used for the decision:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, i.e. 52 ns
- delay_wrt_1mus = 2e-07 s

Decision reasoning:
The signal readout has a distinct local reduction around 3.875-3.880 GHz, reaching about 29.3-29.8 counts compared with nearby values around 32.5-34.3 and higher-frequency recovery. The reference readout does not show the same localized depression at that frequency; its points remain in the low-to-mid 30s with ordinary scatter. The two-average overlay is noisy and has drift between averages, but both signal averages contribute lower values in the resonance region relative to their neighboring trend. This is consistent with a pODMR resonance being present.
