Sequence inspection:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active experiment has full_expt = 0, so the optional 1-level reference branch is skipped.
- Readout 1 role: true 0/bright reference acquired immediately after optical polarization.
- Readout 2 role: signal readout acquired after the rabi_pulse_mod_wait_time microwave pulse.
- Pulse settings: length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Resonance assessment:

The signal readout does not show a stable frequency-localized pODMR dip or peak relative to the reference. The apparent low points in readout 2 are comparable to point-to-point scatter and do not repeat cleanly across the two averages; the reference readout also fluctuates strongly over the same range. The per-average overlay indicates the combined traces are dominated by noise rather than a consistent resonance feature.

Decision: resonance_absent.
