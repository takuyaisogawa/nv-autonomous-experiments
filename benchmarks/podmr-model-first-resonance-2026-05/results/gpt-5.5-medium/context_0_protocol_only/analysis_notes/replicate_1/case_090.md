Active sequence: Rabimodulated.xml / Rabimodulated sequence, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation from the provided XML:
- full_expt = 0, so the optional one-level reference block is inactive.
- Readout 1 is the true 0-level reference: polarization followed directly by detection, before the swept microwave pulse.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time with the swept mw_freq.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.

Data assessment:
The combined signal readout has point-to-point fluctuations of a few counts, including a low point near 3.905 GHz, but the feature is not smooth and is largely driven by one average. The reference readout also fluctuates on a similar scale, and the two-average overlays do not show a consistent, repeatable dip or lineshape in the microwave-pulse readout relative to the zero-level reference.

Decision: no reliable pODMR resonance is present in this scan.
