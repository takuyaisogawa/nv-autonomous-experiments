Case podmr_063_2026-05-17-064555 was evaluated using only the provided sequence XML and raw readouts.

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets length_rabi_pulse to 5.2e-08 s, which rounds to 52 ns at the 250 MHz sample rate. The XML sets mod_depth to 1. The instruction block first performs adj_polarize followed by detection, so readout 1 is the polarized true 0-level reference. The optional 1-level reference block is skipped because full_expt is 0. The active experimental readout then applies rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth 1, followed by detection, so readout 2 is the pulsed signal readout.

The combined raw readouts do not show a clear pODMR resonance. Both readouts fluctuate and generally drift downward toward higher microwave frequency. The signal/reference contrast changes sign several times, with isolated extrema near 3.84, 3.86, 3.88, 3.90, and 3.915 GHz rather than a single reproducible resonance-like dip. The two per-average traces also show substantial scatter at individual points, so the apparent features are not stable enough to identify as a resonance.

Decision: resonance_absent.
