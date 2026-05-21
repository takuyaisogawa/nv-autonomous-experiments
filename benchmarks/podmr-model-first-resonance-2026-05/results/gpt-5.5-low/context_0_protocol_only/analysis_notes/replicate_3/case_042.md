Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Relevant sequence settings from inputs/sequence.xml and the exported variable values:
- full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive.
- The active experimental branch is adj_polarize, detection, wait, then rabi_pulse_mod_wait_time, detection, wait.
- readout 1 is therefore the true 0-level reference after optical polarization.
- readout 2 is the measurement after the microwave Rabi pulse.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 in the provided sequence/variable values.

The two averaged readouts vary by only a few counts and do not show a consistent pODMR-like fluorescence dip or peak at a reproducible frequency. The largest changes are noisy and not supported consistently by both averages; for example, the high readout 2 point near 3.89 GHz is a spike rather than a resonance-shaped feature. Because the active measurement compares the post-pulse readout against the polarized reference and there is no stable frequency-localized contrast, I classify this case as resonance absent.
