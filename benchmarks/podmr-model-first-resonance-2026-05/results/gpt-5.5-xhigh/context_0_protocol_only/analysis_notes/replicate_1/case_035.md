Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the active detections are the initial "true 0 level" reference after optical polarization and the later signal readout after a Rabi-modulated microwave pulse. The optional 1-level reference block is skipped. The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, rounded exactly at the 250 MHz sample rate, and mod_depth = 1.

I treated readout 1 as the 0-reference and readout 2 as the post-microwave pulse signal. A pODMR resonance should appear as a localized, repeatable contrast change in the post-pulse readout relative to the 0-reference, normally a dip for resonant population transfer. The combined readouts and per-average overlays show drift and isolated fluctuations, but no stable localized dip or coherent resonance-shaped feature across the scan. The apparent contrast excursions are single-point or inconsistent between neighboring frequencies and averages.

Decision: resonance absent.
