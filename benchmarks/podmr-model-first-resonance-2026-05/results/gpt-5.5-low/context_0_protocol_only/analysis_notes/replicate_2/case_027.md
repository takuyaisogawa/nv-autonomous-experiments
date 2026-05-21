Sequence review:

The provided sequence is Rabimodulated.xml. The active experiment varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence sets mw_freq plus detuning, then performs an initial adj_polarize and detection to acquire the true 0 level reference. Because full_expt is 0, the optional 1 level reference block is skipped. The active signal block is a rabi_pulse_mod_wait_time call followed by detection.

Readout roles:

Readout 1 is the initial polarized reference detection before the Rabi pulse. Readout 2 is the detection after the modulated Rabi pulse. Since full_expt is disabled, there is no separate active 1-level reference readout.

Pulse settings:

mod_depth is 1 in the provided XML and exported variable values. length_rabi_pulse is 5.2e-08 s, i.e. 52 ns, rounded to the 250 MHz sample grid. The sequence also has switch_delay 100 ns and length_last_wait 1 us.

Resonance decision:

The reference readout remains mostly near 41-43 counts across the sweep, while the pulsed readout shows a pronounced, frequency-localized dip centered around 3.875-3.880 GHz, falling to about 33.9 counts. The dip is visible in the per-average traces as well, though the two averages have different offsets. This contrast-selective depression in the post-pulse readout is consistent with a pODMR resonance.
