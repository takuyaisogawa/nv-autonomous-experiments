# Dataset Card

## Dataset

The benchmark contains 96 pODMR measurements from a single NV center workflow.
All cases use `Rabimodulated.xml` with a 100 MHz microwave-frequency sweep,
21 points, 5 MHz step, and two stored averages.

## Labels

Labels are human resonance-present / resonance-absent judgments. They are used
only for offline scoring and are not present in the agent-visible input folder.

## Agent-Visible Inputs

Each case provides:

- a raw export JSON file
- a raw-readout diagnostic PNG with combined and per-average raw readouts
- embedded sequence XML and runtime variable values inside the raw export JSON
