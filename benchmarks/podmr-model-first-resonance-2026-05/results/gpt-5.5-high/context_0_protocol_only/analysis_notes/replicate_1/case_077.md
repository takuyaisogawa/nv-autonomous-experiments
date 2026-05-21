Sequence XML / raw export review:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional "1 level reference" block is skipped.
- Readout roles:
  - readout 1 is the first detection after adj_polarize, serving as the true 0-level / no-microwave reference.
  - readout 2 is the detection after rabi_pulse_mod_wait_time, serving as the microwave-driven signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, so 52 ns.
- mod_depth from the provided sequence variables is 1.

Resonance assessment:

The raw signal and reference both show broad scan-to-scan drift and point noise. The signal/reference contrast changes sign repeatedly rather than forming a single coherent dip or peak. The strongest apparent negative contrast points are not consistently reproduced in the per-average traces and often come from excursions in the reference channel as much as from a signal-channel dip. With only two averages and no stable localized contrast feature over the frequency sweep, this does not support a pODMR resonance assignment.

Decision: resonance_absent.
