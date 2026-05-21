Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation:
- Channels 1:3 are enabled.
- The sequence first polarizes the NV and performs a detection readout described in the XML as "Acquiring true 0 level reference"; this is readout 1.
- full_expt is 0, so the conditional "Acquire 1 level reference" block is not active and no separate 1-level reference is acquired.
- The active microwave manipulation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection; this is readout 2.
- The pulse duration is rounded at 250 MS/s, but 52 ns is already exactly 13 samples, so the effective pulse duration remains 52 ns.

Data assessment:
The two readouts fluctuate around roughly 30-34 counts with substantial point-to-point noise and only two averages. There is no consistent, reproducible dip or contrast feature in readout 2 relative to the 0-level reference across the microwave frequency sweep. The apparent highs and lows are isolated and not supported by both averages as a stable resonance-shaped feature. Therefore I classify this scan as resonance absent.
