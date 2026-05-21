Case podmr_017_2026-05-12-134151.

The provided sequence XML and raw export identify the active sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse block first performs polarization and detection for the true 0-level reference, then skips the 1-level reference block because full_expt = 0, then applies rabi_pulse_mod_wait_time and detects the microwave-pulse signal. Thus readout 1 is the 0-reference and readout 2 is the signal after the modulated Rabi pulse.

The relevant sequence settings are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate to 52 ns. There are 2 averages and 100000 repetitions.

I compared readout 2 against readout 1 across the sweep rather than relying only on the raw combined traces, because the per-average traces show strong opposite baseline drift. The combined normalized contrast (readout2 - readout1) / readout1 fluctuates around zero with alternating signs. The most negative point is near 3.855 GHz at about -8.7%, but it is isolated and is immediately followed by a positive point near +8.7%; other negative points are scattered rather than forming a consistent localized dip of the expected pulse-limited width. The two averages agree at some individual negative points, but the overall spectrum does not show a stable resonance feature against the 0-reference.

Decision: resonance_absent.
