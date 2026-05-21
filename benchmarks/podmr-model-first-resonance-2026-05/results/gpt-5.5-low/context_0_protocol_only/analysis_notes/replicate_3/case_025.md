Sequence inspection:
- Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave pulse is rabi_pulse_mod_wait_time after the initial polarization/reference detection.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MHz sample rate, so the pulse duration is 52 ns.
- mod_depth in the provided sequence XML is 1.
- full_expt is 0, so the optional 1-level reference block is not active despite do_adiabatic_inversion being true.

Readout roles:
- readout 1 is the initial "true 0 level" reference after adj_polarize and before the swept Rabi pulse.
- readout 2 is the signal readout after the swept 52 ns modulated Rabi pulse.

Resonance decision:
The signal readout shows a localized dip centered near 3.875 GHz, falling from about 39 counts to about 31 counts, while the reference channel does not show a matching dip of comparable shape at the same frequency. The per-average overlay shows the dip structure in the post-pulse readout rather than only in the reference. This is consistent with a pODMR resonance being present.
