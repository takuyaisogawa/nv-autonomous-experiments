Sequence inspection:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At the 250 MHz sample rate this is 13 samples, so the active pulse duration remains 52 ns.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true.
- The enabled readouts are therefore the initial polarized true 0-level reference detection, followed by the detection after the 52 ns rabi_pulse_mod_wait_time pulse.

Data assessment:

The two combined raw readouts have similar means and comparable scatter. The post-pulse/readout-2 to reference/readout-1 ratio is centered near 1.002 with about 0.031 point-to-point standard deviation, and the difference readout has no coherent frequency-localized dip or peak. Individual excursions change sign and are not supported by a consistent feature across the two averages. This looks like noise/drift rather than a pODMR resonance.

Decision: resonance_absent.
