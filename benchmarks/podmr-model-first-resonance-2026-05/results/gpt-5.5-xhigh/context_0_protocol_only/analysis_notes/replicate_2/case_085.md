Case podmr_071_2026-05-17-084118.

The provided sequence XML is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave pulse is rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns. At the 250 MHz sample rate, 52 ns is exactly 13 samples, so the rounded pulse duration remains 52 ns.

The readout roles are determined from the instructions. The first detection follows adj_polarize and is the true 0-level reference with no microwave pulse immediately before it. The full_expt variable is 0, so the optional 1-level reference block is inactive. The second detection follows the 52 ns modulated Rabi microwave pulse and is the pODMR-sensitive readout.

The two raw readouts share an upward baseline trend across the sweep. Comparing the post-pulse readout with the 0-level reference gives alternating positive and negative differences rather than a coherent dip or peak at a microwave frequency. The largest excursions are isolated and are not reproducible as a smooth resonance shape across the two averages. I therefore judge that this scan does not show a pODMR resonance.
