Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML has full_expt = 0, so the optional 1-level reference block is inactive.
- The active detections are therefore:
  - first detection after optical polarization, before the microwave pulse: 0-level/reference readout
  - second detection after rabi_pulse_mod_wait_time: signal readout after the microwave pulse
- Pulse settings from the provided sequence XML / variable values: length_rabi_pulse = 52 ns, mod_depth = 1, mw_ampl = -5 dBm, ampIQ = 5 dBm, freqIQ = 50 MHz.

Data assessment:

The combined readouts show the post-pulse signal readout falling below the pre-pulse reference most strongly around 3.870-3.875 GHz, with the largest contrast at 3.875 GHz. The feature is localized relative to adjacent points and is consistent with microwave-driven spin contrast in the active Rabimodulated pODMR sequence. Although the two averages show drift and limited statistics, the reference/signal contrast around the expected center is large enough to call a resonance present.
