Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The saved variable values give length_rabi_pulse = 52 ns and mod_depth = 1. full_expt = 0, so the optional 1-level reference block is inactive.

Readout roles from the sequence instructions:
- readout 1 follows adj_polarize and is the true 0 / bright reference detection before the swept microwave pulse.
- readout 2 follows rabi_pulse_mod_wait_time at the swept microwave frequency and is the microwave-affected signal detection.

The relevant pODMR observable is the post-pulse signal relative to the reference, not either raw readout alone. Across the sweep, readout 2 / readout 1 fluctuates around 1.0 with isolated high and low points but no coherent resonance-shaped contrast feature. The per-average traces show substantial scatter and do not reproduce a stable dip or peak at a common frequency. The raw readouts also share slow baseline variation, including a low end near the high-frequency edge, which is not enough evidence for a microwave resonance.

Decision: no reliable pODMR resonance is present in this scan.
