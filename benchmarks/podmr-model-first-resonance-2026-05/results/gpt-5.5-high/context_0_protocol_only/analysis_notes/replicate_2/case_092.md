Sequence inspection:

- Active sequence: Rabimodulated.xml.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- Readout roles: readout 1 is the true 0-level reference after optical polarization and before the microwave pulse; readout 2 is the detection after the modulated Rabi microwave pulse.
- Rabi pulse duration: length_rabi_pulse = 5.2e-08 s = 52 ns, rounded to the 250 MHz sample clock.
- mod_depth = 1 from the provided sequence XML and variable values.

Data assessment:

The second readout should show a frequency-dependent ODMR response relative to the first readout if a resonance is present. The combined readouts show fluctuations of roughly one to two counts, but the two channels share broad motion and the signal/reference contrast does not form a stable, localized resonance. Some low normalized points appear around 3.86 GHz and 3.905-3.92 GHz, but they are irregular and not clearly reproduced across the two averages. The per-average overlay shows substantial average-specific scatter, including reference-channel excursions, so the apparent structure is not reliable evidence of a pODMR resonance.

Decision: resonance_absent.
