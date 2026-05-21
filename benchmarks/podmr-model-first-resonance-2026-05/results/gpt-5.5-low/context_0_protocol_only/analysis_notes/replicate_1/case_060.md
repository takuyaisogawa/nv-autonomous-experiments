Sequence XML/readout interpretation:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, which is rounded at the 250 MHz sample rate and remains a 52 ns pulse. The instructions first polarize and detect a true 0-level/bright reference, then wait. Because full_expt = 0, the optional 1-level reference block is skipped. The active measurement then applies rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth, followed by detection. Thus readout 1 is the 0-level reference and readout 2 is the post-microwave-pulse signal.

Resonance assessment:

For a pODMR resonance I would expect a reproducible frequency-localized contrast change in the signal relative to the reference, normally visible consistently across averages. Here the combined readouts are jagged and the per-average overlays show substantial average-to-average scatter. The apparent extrema in readout 2 are not stable against the individual averages, and readout 1 also varies strongly over the same scan range, indicating baseline/readout fluctuation rather than a clean microwave-frequency-dependent resonance. There is no convincing localized dip or peak in the signal relative to the reference across the scan.

Decision: resonance_absent.
