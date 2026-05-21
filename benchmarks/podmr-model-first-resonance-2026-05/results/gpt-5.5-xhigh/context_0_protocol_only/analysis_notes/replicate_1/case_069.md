Active sequence assessment from inputs/sequence.xml:

- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and performs a detection readout before any active microwave pulse; this is the 0-level/reference readout.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The microwave-dependent readout follows rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns, and mod_depth = 1.

Readout interpretation:

- Readout 1 is the pre-microwave 0-level/reference fluorescence.
- Readout 2 is the fluorescence after the modulated 52 ns microwave pulse at the scanned mw_freq.
- A pODMR resonance should appear as a localized, repeatable reduction of readout 2 relative to readout 1.

Decision:

The signal/reference contrast fluctuates around unity with isolated negative points near several frequencies, but these dips are not a coherent resonance profile and are interleaved with positive excursions. The two averages also show substantial drift and inconsistent point-to-point structure. I therefore classify this case as resonance_absent.
