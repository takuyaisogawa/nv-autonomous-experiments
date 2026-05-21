Sequence inspection:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and detects a true 0-level reference.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The measurement readout is taken after a rabi_pulse_mod_wait_time call.
- mod_depth is 1 in the exported variable values.
- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns, rounded at 250 MHz sample rate.

Readout interpretation:
The two combined raw readouts correspond to the initial 0-level reference and the post-pulse signal readout. Since the 1-level reference is inactive, I should not interpret a third reference or use a full contrast calibration.

Resonance assessment:
The post-pulse signal compared with the 0-level reference shows large point-to-point scatter and drift between the two averages. Some individual frequency points have negative contrast, but they are isolated and not accompanied by a coherent neighboring feature. The per-average overlay shows strong baseline drift in opposite directions across averages, and the combined traces do not show a stable pODMR dip or peak over the scan range.

Decision:
No reliable pODMR resonance is present in this scan.
