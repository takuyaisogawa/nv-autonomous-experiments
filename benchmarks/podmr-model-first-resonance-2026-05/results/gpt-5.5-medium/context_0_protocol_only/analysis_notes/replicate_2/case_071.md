Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Relevant sequence settings from the provided XML/export:
- full_expt = 0, so the optional 1-level reference acquisition block is inactive.
- The active readout roles are therefore:
  - readout 1: true 0-level/reference detection immediately after optical polarization, before the swept microwave pulse.
  - readout 2: detection after the modulated Rabi microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate and unchanged.

Decision reasoning:
The post-pulse readout does not show a clear, reproducible pODMR resonance relative to the reference readout. Both readouts fluctuate strongly over the sweep, including shared dips and crossings, and the per-average traces are noisy with only two averages. The apparent low points in the combined traces are not isolated signal-specific depressions that remain consistent relative to the reference. I therefore classify this scan as resonance absent.
