Active sequence and roles:

- Sequence name: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is not active.
- The first detection follows adj_polarize and is the polarized/0-level reference readout.
- The second detection follows rabi_pulse_mod_wait_time and is the signal readout after the microwave pulse.
- length_rabi_pulse is 52 ns. With the 250 MHz sample rate this is rounded to 52 ns exactly.
- The active exported variable values give mod_depth = 1.

Data assessment:

Readout 1 stays near 20-22 counts with only modest structure. Readout 2 shows a clear frequency-localized depression, falling from roughly 22 near the low-frequency side to about 17 around 3.88 GHz, then recovering above 21 by about 3.895-3.92 GHz. This dip is also visible in the combined raw readout plot and is stronger than the variations in the reference readout. The per-average traces have drift, but the averaged second readout has a coherent ODMR-like contrast feature centered near 3.88 GHz.

Decision:

A pODMR resonance is present.
