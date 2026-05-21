Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation from inputs/sequence.xml:
- The first detection after adj_polarize is the true 0-level/reference readout.
- full_expt is 0, so the optional 1-level reference block is inactive.
- The active microwave step is rabi_pulse_mod_wait_time followed by detection, giving the pODMR signal readout.
- mod_depth is 1 from the provided sequence XML.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MS/s to 52 ns.

Data assessment:
Readout 1 is the reference and readout 2 is the microwave-pulse signal. Across the scanned microwave frequency range, both readouts fluctuate and drift downward, especially at the high-frequency end. The difference/relative behavior between signal and reference does not form a clear, localized pODMR dip or peak; the apparent changes are comparable to per-average scatter and baseline drift. I therefore do not see sufficient evidence for a pODMR resonance in this scan.
