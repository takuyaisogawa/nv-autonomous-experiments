Sequence/readout analysis:

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets mod_depth to 1 in the exported variable values, length_rabi_pulse to 52 ns, sample_rate to 250 MHz, and full_expt to 0.

Because full_expt is zero, the conditional "Acquire 1 level reference" block is inactive. The two detections that remain are:

1. An initial detection after adj_polarize, serving as the bright/0-level reference.
2. A detection after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, serving as the microwave-affected pODMR signal readout.

The raw traces are noisy and show modest drift. The post-pulse signal divided by the initial reference has a shallow local decrease around 3.845-3.850 GHz in the combined average, but the per-average behavior is not consistent: one average has its lowest contrast near 3.830 GHz while the other has broad lows around 3.840-3.875 GHz and then rises with drift. The feature is not a stable, coherent resonance-shaped contrast dip across averages, and its scale is comparable to point-to-point fluctuations.

Decision: resonance_absent. There is no defensible pODMR resonance in this scan after accounting for the active readout roles and average-to-average instability.
