Sequence inspection:

The active sequence is Rabimodulated.xml / Rabimodulated. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is a rabi_pulse_mod_wait_time pulse followed by detection.

Readout roles:

- The first detection occurs immediately after adj_polarize and is the true 0-level reference.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The second active detection follows the modulated Rabi pulse and is the pODMR signal readout.

Relevant pulse parameters:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate, i.e. 52 ns
- delay_wrt_1mus = 2e-07 s
- switch_delay = 1e-07 s

Data assessment:

The absolute raw readouts are noisy, but the relevant contrast is the post-pulse signal readout compared with the preceding 0-level reference. Around 3.895 to 3.900 GHz, readout 2 is substantially below readout 1, with normalized differences of about -5.8% and -7.7%. The adjacent point at 3.905 GHz recovers upward, making this a localized negative-contrast feature rather than a monotonic baseline shift. The per-average data also supports a dip in both averages near this region, although the two-average scan remains noisy.

Decision:

A pODMR resonance is present.
