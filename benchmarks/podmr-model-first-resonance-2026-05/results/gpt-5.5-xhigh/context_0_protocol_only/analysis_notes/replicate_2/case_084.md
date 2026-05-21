Case podmr_070_2026-05-17-082720

The provided sequence is Rabimodulated.xml. The active instructions set the microwave, acquire an initial polarized detection, skip the optional 1-level reference block because full_expt = 0, then apply rabi_pulse_mod_wait_time followed by detection.

Readout roles:
- readout 1 is the initial true 0-level / polarized reference detection before the swept Rabi-modulated microwave pulse.
- readout 2 is the signal detection after the swept Rabi-modulated microwave pulse.

Key pulse settings from the provided XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active pulse duration is 52 ns.
- swept parameter is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Decision:
The post-pulse readout does not show a clean, reproducible pODMR resonance relative to the reference. Both readouts share a broad downward drift toward the high-frequency side, and the readout2/readout1 contrast fluctuates with comparable point-to-point noise rather than forming a clear localized dip. The per-average overlays also do not show a consistent resonance feature at the same scan point. I therefore classify this trace as resonance absent.
