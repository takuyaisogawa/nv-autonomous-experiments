Case podmr_020_2026-05-16-165809

Provided sequence XML identifies the active sequence as Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in the raw export. The executable path has full_expt = 0, so the optional 1-level reference block is inactive. The active sequence therefore does:

1. adj_polarize
2. detection
3. wait_for_awg
4. rabi_pulse_mod_wait_time
5. detection
6. final wait

Readout roles: the first readout is the post-polarization reference / nominal 0-level detection without the swept Rabi pulse immediately before it. The second readout is the signal detection after the swept-frequency modulated Rabi pulse.

Relevant pulse settings from the provided sequence XML:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, so the active pulse duration is 52 ns.
- mod_depth = 1.
- switch_delay = 1e-07 s.
- mw_freq is the swept variable, with detuning = 0.

The combined signal readout does not show a clear localized ODMR-like contrast feature relative to the reference. Readout 2 mostly rises from the low-frequency side toward the middle/high side and then gradually falls, while readout 1 also varies by a comparable amount. The apparent crossings and excursions are not stable between the two averages in a way that isolates a resonant dip or peak in the post-pulse signal. With only two averages and large per-average drift/opposite trends, the data look dominated by baseline variation/noise rather than a resolvable pODMR resonance.

Decision: resonance_absent.
