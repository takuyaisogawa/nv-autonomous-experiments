Active sequence review:

- Sequence name from the export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first polarize, then run detection before any microwave pulse. This detection is explicitly marked as the true 0 level reference, so readout 1 is the reference role.
- full_expt is 0, so the optional 1 level reference branch is inactive.
- The active experiment pulse is rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second detection is the post-pulse signal role, so readout 2 is the experiment/signal readout.
- sample_rate is 250 MHz and length_rabi_pulse is 5.2e-08 s. The sequence rounds this to sample clock ticks; 52 ns is 13 samples at 250 MHz, so the active pulse duration remains 52 ns.
- The active mod_depth is 1.

Data assessment:

The raw readouts have substantial average-to-average count offset and a slow upward drift, so the useful check is whether readout 2 shows a reproducible relative feature versus readout 1. The combined trace has scattered local dips and a high point near 3.915 GHz, but the per-average signal/reference behavior does not repeat cleanly at the same scan values. The apparent extrema are not a coherent ODMR-like resonance feature across the sweep.

Decision: resonance_absent.
