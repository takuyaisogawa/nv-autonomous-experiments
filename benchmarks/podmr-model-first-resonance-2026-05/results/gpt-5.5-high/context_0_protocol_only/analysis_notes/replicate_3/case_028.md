Case podmr_013_2026-05-16-123121.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed instructions first polarize and detect a true 0-level reference, then wait.
- full_expt is 0, so the optional Acquire 1 level reference block is skipped despite do_adiabatic_inversion being true.
- The active microwave manipulation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns, followed by detection.
- With sample_rate = 250 MHz, the 52 ns pulse is exactly 13 samples after rounding, so the active pulse duration remains 52 ns.

Readout roles:
- Readout 1 is the initial polarized 0-level reference detection, with no preceding microwave pulse in that repetition segment.
- Readout 2 is the signal detection after the modulated Rabi microwave pulse and is the readout expected to show pODMR contrast.

Data assessment:
Readout 1 stays comparatively flat around the low-to-mid 40s across the sweep, while readout 2 shows a pronounced reproducible dip centered near 3.875-3.880 GHz, falling to about 34 counts while neighboring points recover into the 40s. The same dip is visible in the per-average traces, so it is not just a single averaged artifact. Because the signal readout has a frequency-localized contrast feature relative to the stable reference, this is consistent with a pODMR resonance being present.
