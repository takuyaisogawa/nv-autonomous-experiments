Inspected the provided sequence XML before interpreting the traces.

Active sequence:
- The scan is using Rabimodulated.xml with mw_freq swept across the plotted range.
- length_rabi_pulse is 5.2e-08 s. At sample_rate 250 MHz, the rounding step leaves this as 13 samples, or 52 ns.
- mod_depth is 1 in the provided sequence XML.
- full_expt is 0, so the optional "Acquire 1 level reference" block is skipped. The adiabatic inversion setting is therefore not active in the executed path.

Readout roles from the instruction order:
- readout 1 is the detection immediately after adj_polarize, before the microwave pulse. This is the true 0-level reference.
- readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay). This is the microwave-pulsed pODMR signal.

Data interpretation:
The signal readout should be judged by whether readout 2 drops relative to the 0-reference readout 1 as mw_freq is swept. The combined readout2/readout1 ratio has its strongest minimum near 3.920 GHz, where the post-pulse signal is lower than the reference in both averages. Other fluctuations are present, but this point is the largest normalized contrast feature and is consistent with a pODMR resonance in the swept range.

Decision: resonance_present.
