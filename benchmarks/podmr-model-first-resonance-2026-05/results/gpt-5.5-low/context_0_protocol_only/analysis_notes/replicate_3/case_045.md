Active sequence: Rabimodulated.xml / Rabimodulated, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- The instruction first runs adj_polarize followed by detection, giving the true 0-level reference readout.
- full_expt is 0, so the optional 1-level reference block is skipped despite do_adiabatic_inversion being true.
- The active experiment readout is after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.
- Therefore the two combined raw readouts are reference and pulse-affected signal, not two independent resonance channels or a normalized 0/1 pair.

Data assessment:
The two averaged traces fluctuate around roughly 52-54 counts with only two averages and substantial point-to-point scatter. There are isolated excursions, including a low point in readout 1 near the high-frequency end and a nearby high point, but they are not corroborated by a consistent dip or peak in the other readout and are comparable to the per-average variation. The difference between signal and reference does not form a stable, repeatable ODMR-like feature across neighboring frequency points. I therefore do not identify a reliable pODMR resonance in this scan.
