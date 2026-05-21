Active sequence: Rabimodulated microwave-frequency sweep.

The provided XML sets sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, and mod_depth = 1. The pulse length is already on the 4 ns sample grid, so the active Rabi pulse duration is 52 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the instruction order:
- readout 1 is the true 0-level reference detection immediately after optical polarization.
- full_expt = 0, so the optional 1-level reference block is skipped.
- readout 2 is the signal detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay).

Decision notes:
The post-pulse signal and the signal/reference contrast fluctuate strongly from point to point. The combined contrast has a deep low point near 3.875 GHz, but it is mainly driven by one of the two averages; the other average does not show a matching pronounced dip there. Similar-scale excursions appear elsewhere in the scan, and the raw signal readout does not form a stable, smooth resonance feature. I therefore do not identify a reliable pODMR resonance in this measurement.
