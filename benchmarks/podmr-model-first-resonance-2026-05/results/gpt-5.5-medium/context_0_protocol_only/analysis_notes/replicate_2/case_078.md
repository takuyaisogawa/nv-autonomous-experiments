Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence, scanned over mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Sequence details used for the decision:
- full_expt = 0, so the optional "Acquire 1 level reference" branch is disabled.
- Readout 1 is the true 0-level reference: adj_polarize, detection, then wait_for_awg before the microwave pulse.
- Readout 2 is the active post-pulse detection after rabi_pulse_mod_wait_time.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 in the provided sequence XML variable values.

Assessment:
The combined readouts do not show a stable pODMR resonance. The post-pulse readout relative to the 0-level reference fluctuates around zero contrast across the scan. There are isolated excursions, including a positive point near 3.915 GHz and negative points near 3.890 and 3.920 GHz, but these do not form a coherent resonance feature and are not consistently reproduced across the two averages. Because the active readout lacks a repeatable dip or structured resonance-like contrast against the reference, I classify this case as resonance absent.
