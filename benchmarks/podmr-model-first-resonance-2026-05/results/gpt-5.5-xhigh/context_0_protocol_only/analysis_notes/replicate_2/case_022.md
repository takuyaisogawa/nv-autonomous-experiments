Active sequence inspection:

- Sequence name: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- mod_depth = 1 in the provided sequence XML.
- length_rabi_pulse = 5.2e-08 s, i.e. 52 ns; at 250 MHz sample rate this is already an integer 13 samples.

Readout roles:

- Readout 1 is the first detection after adj_polarize, before the microwave Rabi pulse. This is the true 0-level/reference readout.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay). This is the microwave-sensitive pODMR readout.

Decision:

Readout 2 shows a strong, localized dip around 3.870-3.880 GHz, reaching 28.21 counts at 3.880 GHz compared with an off-resonance level near 35.5 counts, about a 20.6% drop. The same dip is visible in both individual averages, while readout 1 stays comparatively flat and does not show a matching central depression. The post-pulse readout therefore contains a real pODMR resonance.
