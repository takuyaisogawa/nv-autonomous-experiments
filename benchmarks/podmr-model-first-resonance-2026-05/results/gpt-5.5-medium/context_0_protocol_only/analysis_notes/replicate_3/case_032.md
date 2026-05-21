Sequence inspection:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse path: polarize, detection for the true 0-level reference, wait, then rabi_pulse_mod_wait_time, detection, final wait.
- full_expt is 0, so the optional 1-level reference block is not executed.
- Readout 1 is the true 0-level reference. Readout 2 is the signal readout after the modulated Rabi pulse.
- mod_depth is 1 in the provided sequence XML / exported variable values.
- length_rabi_pulse is 52 ns, rounded at 250 MS/s, and is used for the active Rabi pulse.

Data assessment:
The reference readout stays roughly flat around the mid-40 count level, while the signal readout shows a clear, localized dip centered near 3.875 GHz, reaching about 34 counts before recovering on both sides. The feature appears in both per-average traces for readout 2 and is not mirrored in the reference channel. This is consistent with a pODMR resonance.
