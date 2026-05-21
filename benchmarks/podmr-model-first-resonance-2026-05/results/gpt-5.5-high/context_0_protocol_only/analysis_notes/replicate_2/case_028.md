Case podmr_013_2026-05-16-123121.

The provided sequence is Rabimodulated.xml. The active microwave operation is
`rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth,
switch_delay, ch_on)` followed by detection. `full_expt = 0`, so the optional
1-level reference branch is not active. The first detection after
`adj_polarize` is therefore the bright/0-level reference readout, and the
second detection after the modulated Rabi pulse is the microwave-affected
signal readout.

Relevant pulse settings from the provided XML:
- `length_rabi_pulse = 5.2e-08 s`, rounded at 250 MHz sample rate, i.e. 52 ns.
- `mod_depth = 1`.
- Sweep variable is `mw_freq` from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The first/readout-reference trace remains near the low-to-mid 40 count level
without a matching central dip. The second/signal readout shows a pronounced,
localized decrease around 3.875-3.880 GHz, falling from the surrounding
approximately 42-45 count level to about 34 counts. The same dip is visible in
both per-average overlays, which argues against a single-average artifact.

Decision: a pODMR resonance is present.
