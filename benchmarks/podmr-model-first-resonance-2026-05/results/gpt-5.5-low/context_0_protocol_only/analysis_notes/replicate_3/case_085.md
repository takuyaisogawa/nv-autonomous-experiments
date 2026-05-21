Sequence inspection:
- Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns after sample-rate rounding.
- mod_depth is 1 in the provided sequence file and exported variable values.
- full_expt = 0, so the optional 1-level reference branch is not active.

Readout roles:
- Readout 1 is the initial reference detection after adj_polarize, before the scanned microwave pulse.
- Readout 2 is the detection after the scanned modulated Rabi pulse.

Resonance decision:
The two raw readouts mostly show a shared upward drift across the frequency sweep with point-to-point noise. There is no consistent, localized contrast feature between the reference and post-pulse readout that stands out across the two averages as a pODMR resonance. The apparent variations are comparable to the per-average scatter and do not form a clear dip or peak at a specific microwave frequency.

Decision: resonance_absent.
