Sequence inspection:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional 1-level reference block is disabled.
- Readout roles: first detection is the true 0 / bright reference after optical polarization and before the microwave pulse; second detection is after the modulated Rabi microwave pulse.
- mod_depth from the provided sequence XML is 1.
- Active microwave pulse duration is length_rabi_pulse = 52 ns, already aligned to the 250 MHz sample clock.

Data assessment:
The combined readouts show point-to-point fluctuations of a few counts and the post-pulse/reference contrast changes sign across the sweep. The largest apparent dips or peaks are not supported by a consistent shape across the two averages. There is no clear localized ODMR resonance feature, such as a repeatable dip in the post-pulse readout relative to the reference, within this scan.

Decision: resonance_absent.
