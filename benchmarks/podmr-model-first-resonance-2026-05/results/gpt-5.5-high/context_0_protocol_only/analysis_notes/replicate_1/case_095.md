Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout roles:
- The first detection occurs immediately after optical polarization and is the bright/0-level reference readout.
- full_expt is 0, so the optional 1-level reference block is inactive.
- The second active detection follows a rabi_pulse_mod_wait_time microwave pulse and is the pODMR signal readout.

Pulse settings used for the decision:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, i.e. 52 ns.
- mod_depth = 1 from the exported variable values.

Assessment:
Both combined raw readouts show a gradual downward drift across frequency. The post-microwave signal readout does not show a stable, localized ODMR dip relative to the initial reference. The signal-reference difference changes sign repeatedly, with isolated dips near several frequencies rather than one coherent resonance feature. The per-average overlay also suggests average-to-average offset/drift rather than a repeatable resonant response.

Decision: resonance_absent.
