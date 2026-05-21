Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional "Acquire 1 level reference" branch is inactive.
- Readout roles: the first detection occurs after optical polarization and before the swept Rabi pulse, acting as a true 0-level / baseline reference. The second detection occurs after rabi_pulse_mod_wait_time and is the pulse-affected signal readout.
- mod_depth is 1 in the provided sequence XML and variable values.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MS/s, i.e. 52 ns.

Data assessment:

Both combined readouts show a broad downward trend across the scan. The post-pulse readout does not show a clean, reproducible, frequency-localized dip or peak relative to the reference. Apparent local deviations around roughly 3.895 to 3.905 GHz are not consistent between readout channels and are comparable to the per-average scatter, including a strong average-dependent background slope/crossover. Because the active sequence provides a baseline readout followed by the Rabi-modulated signal readout, a resonance call would require a localized contrast feature in the pulse-affected signal that is separable from drift; that is not evident here.

Decision: resonance_absent.
