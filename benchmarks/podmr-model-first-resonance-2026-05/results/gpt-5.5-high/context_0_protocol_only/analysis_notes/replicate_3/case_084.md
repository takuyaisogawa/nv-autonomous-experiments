Case podmr_070_2026-05-17-082720.

The provided sequence is Rabimodulated.xml with mw_freq as the scanned variable from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active path has full_expt = 0, so the optional 1-level reference branch is skipped even though do_adiabatic_inversion is true. The executed cycle is polarization, detection, wait, a modulated Rabi microwave pulse, detection, and final wait.

Readout role identification from the active instructions:
- readout 1 is the detection immediately after adj_polarize, serving as the polarized / true 0 level reference.
- readout 2 is the detection after rabi_pulse_mod_wait_time, serving as the microwave-affected pODMR signal readout.

The relevant microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The exported variable list gives mod_depth = 1.

The combined raw readouts show both channels varying slowly downward over the scan, especially toward the high-frequency end. The post-microwave readout does not show a distinct localized dip or peak relative to the reference that is reproducible across the two averages. Differences between readout 2 and readout 1 fluctuate in sign and size across the sweep, and the low values near the upper end appear as shared baseline drift rather than a narrow resonance feature.

Decision: resonance_absent.
