Sequence interpretation:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and performs a detection readout without the Rabi-modulated microwave pulse. This is the true 0-level reference readout.
- full_expt is 0, so the optional 1-level reference block is inactive and does not contribute a readout.
- The active signal readout follows a Rabi-modulated microwave pulse from rabi_pulse_mod_wait_time, then detection.
- The active pulse uses length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, so the pulse duration is 52 ns.
- The provided sequence XML has mod_depth = 1 for the active Rabi-modulated pulse.

Readout assessment:

Readout 1 is the no-pulse 0-level reference and stays near the low-40 count range across the scan, without a matching deep feature near the center of the sweep. Readout 2 is the MW-pulsed signal and shows a pronounced, structured dip from roughly 3.870 GHz to 3.885 GHz, reaching about 33.9 at 3.880 GHz compared with surrounding values around 41 to 43. The same dip is visible in both individual averages of readout 2, while readout 1 remains comparatively flat. Because the dip is tied to the MW-pulsed readout and is repeatable across averages, this is consistent with a pODMR resonance being present.
