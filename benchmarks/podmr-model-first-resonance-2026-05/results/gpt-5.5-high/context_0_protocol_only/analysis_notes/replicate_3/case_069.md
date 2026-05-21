I used the provided sequence XML and raw export only.

Active sequence:
- SequenceName is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave operation is rabi_pulse_mod_wait_time followed by detection.

Readout roles from the instruction order:
- Readout 1 is the initial true 0-level / bright reference detection after adj_polarize.
- full_expt is 0, so the optional 1-level reference block is skipped.
- Readout 2 is the detection after the modulated rabi pulse.

Pulse settings:
- length_rabi_pulse is 5.2e-08 s, which is 52 ns and remains 52 ns after rounding at 250 MHz sample rate.
- mod_depth is 1 in the provided sequence XML and exported variable values.

Decision:
The combined signal/reference contrast has no single reproducible resonance-like feature. Several points show comparable negative contrast, including around 3.83, 3.85, 3.88, and 3.90 GHz, and the two individual averages do not maintain a consistent localized dip shape. The raw readouts also show broad baseline drift and point-to-point scatter comparable to the apparent features. I therefore classify this case as resonance_absent.
