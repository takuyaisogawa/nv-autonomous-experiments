Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided XML sets full_expt = 0, so the optional 1-level reference branch is inactive. The two active detections are:

1. Readout 1: true 0-level reference after adj_polarize and before the swept microwave/Rabi pulse.
2. Readout 2: signal after rabi_pulse_mod_wait_time followed by detection.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. The provided sequence XML and exported variable values give mod_depth = 1. The pulse length is already aligned to the 250 MHz sample rate, so it remains 52 ns.

Decision: resonance_absent.

Reasoning: For a pODMR resonance I would expect a reproducible frequency-dependent PL dip in the post-pulse signal readout relative to the reference. The combined readout 2 trace has isolated lows, but similar-scale structure appears in the reference and the per-average traces do not show a stable dip at the same frequency. The largest negative signal-reference contrasts are dominated by one average or sit next to large positive fluctuations, so the data look noise-like rather than a coherent pODMR resonance.
