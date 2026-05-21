Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.
- The sequence first polarizes and detects a true 0-level reference readout.
- The optional 1-level reference block is inactive because full_expt = 0, despite do_adiabatic_inversion being true.
- The active signal readout follows a rabi_pulse_mod_wait_time call using length_rabi_pulse.
- mod_depth is 1 in the exported variable values, and the pulse duration is 5.2e-08 s (52 ns).

Data assessment:

Readout 1 is the 0-level reference and stays near the high-PL baseline with only small fluctuations. Readout 2 is the signal after the modulated 52 ns microwave pulse. It shows a clear, localized PL dip centered around roughly 3.875-3.880 GHz, falling from the surrounding 46-47 count level to about 39.6 counts. The same dip is visible in the per-average overlay rather than being confined to a single averaged trace. Because the dip is localized in the swept microwave frequency and appears in the signal readout relative to the reference, this is consistent with a pODMR resonance being present.
