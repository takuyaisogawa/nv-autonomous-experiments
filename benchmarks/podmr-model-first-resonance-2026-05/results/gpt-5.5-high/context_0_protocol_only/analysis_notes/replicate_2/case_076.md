Case podmr_062_2026-05-17-063134.

I used the provided sequence XML before judging the trace. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active flow first polarizes and detects a true 0-level reference, then skips the optional 1-level reference because full_expt = 0, then applies rabi_pulse_mod_wait_time followed by detection. Therefore readout 1 is the true 0-level reference readout and readout 2 is the pulsed measurement readout. The active pulse duration is length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, so 52 ns. The provided XML has mod_depth = 1.

The combined readouts fluctuate by roughly the same size as the apparent features. Readout 2 has a pronounced low point near 3.920 GHz, but it is a single-point excursion near the edge of the scan and the per-average overlay shows that it is mainly driven by one average rather than a reproducible resonance-shaped dip. Readout 1 also has substantial structure, so the readout-2 variation does not separate cleanly from baseline/reference noise.

Decision: resonance_absent.
