Sequence inspection:
- Active sequence: Rabimodulated.xml, sweeping mw_freq.
- Active instructions: polarize, detection, wait, then rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detection.
- The optional 1-level reference block is disabled because full_expt = 0, so it does not contribute readouts.
- Readout roles: readout 1 is the initial true 0-level/polarized reference detection before the microwave pulse; readout 2 is the detection after the modulated Rabi microwave pulse.
- mod_depth is 1 in the recorded variable values, and the pulse duration is length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Resonance assessment:
The frequency scan covers 3.825 to 3.925 GHz with 21 points and two averages. Both raw readouts show point-to-point fluctuations of similar size, including a shared high point near the low-frequency side and no stable, localized pODMR-like dip or contrast feature in the microwave-pulsed readout relative to the reference. The per-average traces are also inconsistent around possible features, so the apparent variations look dominated by noise or baseline drift rather than a reproducible resonance.

Decision: resonance_absent.
