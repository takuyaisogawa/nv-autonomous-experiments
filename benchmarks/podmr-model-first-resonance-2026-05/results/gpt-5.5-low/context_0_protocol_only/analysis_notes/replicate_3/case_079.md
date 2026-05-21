Active sequence and roles:

- The sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed instructions first polarize and detect a true 0-level reference. Because full_expt = 0, the optional 1-level reference branch is skipped.
- The active signal operation is rabi_pulse_mod_wait_time followed by detection, so readout 1 is the pre-microwave/reference detection and readout 2 is the post-pulse detection.
- The exported variable values give length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, and mod_depth = 1.

Data assessment:

The two combined raw readouts vary mostly together with slow baseline drift across the frequency sweep. The signal/reference ratio ranges roughly from 0.952 to 1.043, with the largest negative excursions near the low-frequency edge around 3.830 GHz and another isolated point near 3.890 GHz. These features are not a clean, reproducible pODMR resonance: they are comparable to the point-to-point noise and average-to-average spread, and the per-average overlays do not show a consistent dip at one frequency. The response also lacks a convincing localized ODMR contrast feature around the expected swept range; instead it alternates sign between neighboring regions.

Decision: resonance absent.
