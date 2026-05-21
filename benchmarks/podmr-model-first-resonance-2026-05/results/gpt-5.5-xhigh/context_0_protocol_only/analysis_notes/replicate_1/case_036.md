Case: podmr_021_2026-05-16-171244

Inputs used: inputs/sequence.xml, inputs/raw_export.json, and the raw readout plot.

Active sequence interpretation:
- The scan uses Rabimodulated.xml while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instruction path first polarizes, then performs a detection before any microwave pulse. This is the true 0-level / bright reference readout.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The second active detection occurs after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth. This readout is the pODMR signal after the microwave pulse.
- mod_depth is 1.
- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns. At the 250 MHz sample rate this is 13 samples, so the rounded pulse duration remains 52 ns.

Readout assessment:
The combined readout 2 minus readout 1 contrast is not a single stable localized fluorescence dip. It changes sign repeatedly across the scan, with negative regions near 3.83-3.845 GHz and 3.88-3.885 GHz but positive regions nearby. The raw readout 2 trough around 3.88 GHz is accompanied by a low reference readout, and the two individual averages show strong average-to-average drift. Candidate negative-contrast points are therefore not cleanly separated from baseline/reference motion.

Decision:
I do not find sufficient evidence for a pODMR resonance in this scan.
