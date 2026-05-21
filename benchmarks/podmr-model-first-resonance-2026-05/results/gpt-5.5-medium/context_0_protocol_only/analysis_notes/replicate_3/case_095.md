Sequence inspection:

- Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active microwave operation: rabi_pulse_mod_wait_time followed by detection.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate to the same 52 ns.
- mod_depth: 1 in the exported variable values.
- full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true.

Readout roles:

- The first detection occurs immediately after adj_polarize and is the true 0-level / bright reference readout.
- The second active detection occurs after the modulated 52 ns Rabi pulse and is the microwave-affected signal readout.

Resonance assessment:

Both combined raw readouts show a broad downward trend across the scan and substantial point-to-point noise. The post-pulse readout does not show a localized dip, peak, or contrast feature relative to the polarized reference that is consistent across averages. The per-average overlays show the same lack of a stable frequency-localized feature; changes near individual scan points are comparable to noise and common drift.

Decision: resonance absent.
