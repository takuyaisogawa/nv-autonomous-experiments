Sequence review:

- Active sequence: Rabimodulated.xml / Rabimodulated, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active readout roles: readout 1 is the true 0-level reference after laser polarization and before the microwave pulse. Because full_expt = 0, the optional 1-level reference block is skipped. Readout 2 is the detection after the modulated microwave pulse.
- Microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.
- Modulation depth: mod_depth = 1 from the provided sequence XML and variable values.

Resonance assessment:

The expected pODMR signature would be a reproducible frequency-localized reduction of the post-microwave signal readout relative to the reference readout. The combined readout 2 minus readout 1 trace fluctuates around a small negative offset, with sign changes and isolated extrema. The per-average overlays do not show the same dip location: negative excursions appear at different scan points in the two averages, while some neighboring points are positive. There is no coherent Lorentzian-like dip or consistent localized contrast feature across the 3.825-3.925 GHz sweep.

Decision: resonance_absent.
