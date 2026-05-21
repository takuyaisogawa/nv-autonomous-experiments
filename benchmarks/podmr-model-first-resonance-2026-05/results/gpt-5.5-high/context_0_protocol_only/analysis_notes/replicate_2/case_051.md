Sequence interpretation:

- Active sequence: Rabimodulated.xml / Rabimodulated.xml-style pODMR scan, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML has full_expt = 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true.
- Readout roles: readout 1 is the detection immediately after adj_polarize, labeled in the XML comments as the true 0 level reference. Readout 2 is the detection after rabi_pulse_mod_wait_time and is the pODMR signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- Active mod_depth: 1.0 from the provided sequence XML and exported variable values.

Resonance assessment:

The signal readout after the modulated Rabi pulse is noisy and does not form a clear, repeatable ODMR-like dip or peak across the scanned microwave frequencies. The largest apparent normalized contrast excursions are strongly affected by reference-channel fluctuations, especially where readout 1 drops around 3.900 GHz while readout 2 remains near its typical level. The two per-average traces are not consistent enough to support a frequency-locked resonance feature. I therefore classify this case as resonance absent.
