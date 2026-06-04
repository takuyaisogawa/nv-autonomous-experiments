# Public Scope

This repository is a public case-study and project-management source release.

## Scope Statement

The case-referenced NV project-management source is public for audit.

This repository cannot control hardware.

Real completed case artifacts are included.

## What Is Public

- Durable project state and project-manager logic.
- Scheduler wake records and agent completion records.
- Backlog, evidence ledger, and experiment-intent handling.
- Submit-spec validation.
- Sanitized source copies of the case-referenced NV project-manager,
  batch-runner, bridge-watch, and direct-enqueue layers, with execution
  disabled.
- A public summary of the project-manager prompt context.
- Sanitized copies of three completed NV-center autonomous-agent projects.
- MATLAB/Python analysis helpers, raw data copies, figures, and reports
  needed to inspect the included cases.

## What Is Not Public

- Live instrument control as a runnable public entry point.
- Live laboratory queue mutation as a runnable public entry point.
- Hardware drivers and lab-specific device configuration.
- MATLAB live-lab backend source.
- Automatic startup wiring for a real experiment machine.
- Operator-channel integration.

The public code is meant to make the autonomy loop auditable. It is not a
turnkey lab-control package.
