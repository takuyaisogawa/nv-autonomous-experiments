Sequence review:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets full_expt = 0, so the optional 1-level reference block is not active.
- Readout 1 is the detection immediately after optical polarization, i.e. the true 0-level/reference readout.
- Readout 2 is the detection after the active rabi_pulse_mod_wait_time call, i.e. the microwave-pulse signal readout.
- The active pulse uses length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- The active modulation depth is mod_depth = 1.

Data assessment:

The reference readout is relatively smooth across the sweep, while the post-pulse readout has a large, repeatable dip centered around 3.875-3.880 GHz. Both individual averages show this depression in the same frequency region, and the combined readout recovers on either side. Because the dip appears in the microwave-pulse signal readout rather than as a comparable feature in the reference readout, this is consistent with a pODMR resonance being present.
