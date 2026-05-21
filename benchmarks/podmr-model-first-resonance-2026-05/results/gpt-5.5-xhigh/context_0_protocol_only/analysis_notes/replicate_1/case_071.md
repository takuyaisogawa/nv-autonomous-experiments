Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation:
- The XML enables channels 1:3 and sets the microwave source before the measurement blocks.
- full_expt = 0, so the optional 1-level reference block is skipped.
- Readout 1 is the detection immediately after polarization, serving as the bright/0-level reference.
- Readout 2 is the detection after the rabi_pulse_mod_wait_time block, serving as the microwave-pulse signal readout.
- mod_depth = 1 from the provided sequence variables.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active pulse duration is 52 ns.

Data assessment:
The combined signal-minus-reference contrast fluctuates around zero, with relative deviations of roughly -4.5% to +4.0%. Negative contrast points occur at several separated frequencies, but they are not organized into a clear localized dip, and the strongest edge point is not consistent across the two per-average traces. The reference readout also moves substantially point to point, so several apparent signal lows track general readout noise rather than a microwave-specific resonance.

Decision:
No reliable pODMR resonance is present in this scan.
