Sequence review:
The scan uses Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the active instructions, full_expt = 0, so the optional 1-level reference block is not executed. The first detection occurs immediately after adj_polarize and serves as the true 0-level reference. The second detection occurs after rabi_pulse_mod_wait_time and is the microwave-pulse pODMR signal. The pulse uses length_rabi_pulse = 5.2e-08 s, which is 52 ns after rounding at the 250 MHz sample rate, and mod_depth = 1.

Data assessment:
The post-pulse readout has a localized depression near 3.895-3.900 GHz relative to the 0-level reference. The combined normalized contrast (readout 2 - readout 1) / readout 1 is about -4.0% at 3.895 GHz and -4.2% at 3.900 GHz. Both per-average readout-2 traces are low in this region, while earlier large contrast excursions are less reproducible and more affected by reference variation. This supports a pODMR resonance being present.
