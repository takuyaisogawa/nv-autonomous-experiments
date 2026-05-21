I used inputs/sequence.xml as the sequence source. The active sequence is Rabimodulated with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. The XML sets full_expt = 0, so the optional 1-level reference block is skipped.

Active readout roles:
- Readout 1 is the true 0-level reference after adj_polarize and before the microwave Rabi pulse.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time.

Pulse settings from the XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, which is 52 ns. At the 250 MHz sample rate this is 13 samples, so rounding keeps it at 52 ns.

Decision:
The relevant pODMR contrast is the post-pulse signal readout relative to the pre-pulse 0-level reference. The combined readout2 - readout1 contrast has pronounced negative features at about 3.855 GHz (-3.81 counts, -11.3 percent) and 3.895 GHz (-3.00 counts, -9.1 percent). These negative contrast points are present in both individual averages, while neighboring points are mixed in sign. This is noisy but consistent with a real pODMR resonance response rather than a flat/no-resonance sweep.
