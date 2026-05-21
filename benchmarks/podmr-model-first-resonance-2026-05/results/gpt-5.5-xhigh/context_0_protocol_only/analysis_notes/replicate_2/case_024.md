Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is inactive.
- Readout 1 is the first detection after polarization, used as the true 0-level reference.
- Readout 2 is the final detection after the modulated Rabi pulse, used as the microwave-pulse signal.
- mod_depth is 1.
- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns. At 250 MS/s this is 13 samples, so rounding keeps it at 52 ns.

Data assessment:
Readout 1 stays near 28-31 counts with no matching local loss at the main feature. Readout 2 shows a pronounced localized dip from roughly 29 counts down to about 24.2 counts near 3.875-3.880 GHz, then recovers toward 29 counts at higher frequency. The per-average overlay shows the same dip structure in the combined signal despite average-to-average drift. Because the active signal readout after the MW pulse has a frequency-localized contrast feature that is not mirrored as a reference artifact, this is consistent with a pODMR resonance.

Decision: resonance_present.
