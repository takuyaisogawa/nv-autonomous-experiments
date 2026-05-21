Sequence review:

- SequenceName in the raw export is Rabimodulated.xml.
- The XML sets full_expt = 0, so the optional 1-level reference block is inactive.
- Active readout roles:
  - readout 1: true 0-level reference after polarization and detection before the microwave pulse.
  - readout 2: signal after the modulated Rabi microwave pulse and subsequent detection.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this is already an integer 13 samples, so the pulse duration remains 52 ns.
- mod_depth = 1.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Decision:

Using readout 1 as the paired reference and readout 2 as the post-pulse measurement, the combined readout2/readout1 contrast has a localized minimum at 3.895 GHz. The combined ratio there is about 0.969, compared with about 1.005 at 3.890 GHz and 1.010 at 3.900 GHz. The per-average paired ratios also both dip at 3.895 GHz relative to nearby points: average 0 is about 0.959 and average 1 is about 0.977. This is a frequency-localized suppression in the post-pulse readout rather than a matching suppression in the reference channel.

Prediction: resonance_present.
