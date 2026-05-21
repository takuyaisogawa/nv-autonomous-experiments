I inspected inputs/sequence.xml before deciding.

The active sequence is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz. The instructions set full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive even though do_adiabatic_inversion is true. That leaves two active detections: readout 1 is the detection immediately after adj_polarize, acting as the true 0-level reference; readout 2 is the detection after rabi_pulse_mod_wait_time, acting as the pODMR signal readout.

The active Rabi pulse duration is length_rabi_pulse = 5.2e-08 s. At the 250 MHz sample rate this is exactly 13 samples, so the rounded pulse duration remains 52 ns. The provided XML and resolved scan variables give mod_depth = 1, so the pulse is fully modulated.

I compared the second, post-pulse readout against the first reference readout across the sweep. The combined data shows negative signal-reference contrast near 3.855 GHz and again around 3.905-3.910 GHz, with the largest combined differences about -2.5 and -2.4 raw readout units. These suppressions are visible in both averages at the same frequencies, while the rest of the sweep is mostly point-to-point noise around the reference. I therefore classify the scan as having a pODMR resonance present, albeit noisy.
