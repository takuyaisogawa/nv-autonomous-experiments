Sequence XML inspection:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true.
- Active readout roles:
  - readout 1 is the true 0-level/reference readout after adj_polarize and detection, before the microwave pulse.
  - readout 2 is the measurement readout after a rabi_pulse_mod_wait_time pulse and detection.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- mod_depth = 1.

Data assessment:

The combined traces have no stable frequency-localized dip or peak that is clearly separated from readout drift/noise. The largest apparent contrast feature is a positive readout-2 minus readout-1 excursion near 3.915 GHz, but the per-average data show that this is dominated by one average while the other average is near zero at the same point. Other excursions alternate in sign and are not reproducible as a coherent resonance shape. Because the signal readout does not show a consistent resonance-like feature relative to the reference readout, I classify this case as resonance absent.
