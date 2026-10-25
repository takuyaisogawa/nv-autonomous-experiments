# Experiment Intent Schema

An experiment intent is the agent-authored record between a scientific decision
and backend action.

The intent says: this is the measurement I want, this is why it is justified,
this is what evidence it should produce, these are the stop conditions, and this
is the backend boundary that must be verified before submission.

## Flow

```text
agent scientific decision
        |
        v
experiment intent
        |
        v
schema and boundary verification
        |
        v
bridge boundary / execution-source layer
        |
        v
result artifact
        |
        v
evidence ledger and project state update
```

This layer prevents the agent from jumping directly from a scientific thought
to backend action.

## Minimal Fields

The case folders contain completed intents under:

```text
cases/<case>/project/experiment_intents/
```

The practical schema is intentionally document-like rather than a tiny command
object. Important fields include:

| Field | Purpose |
| --- | --- |
| `schema_version` | Version of the intent schema. |
| `kind` | Should be `experiment_intent`. |
| `intent_id` | Stable id used to link intent, submit spec, result, and evidence. |
| `project_id` | Project that owns the intent. |
| `status` | Planned, verified, submitted, done/completed, failed, canceled, or superseded. |
| `summary` | One-line measurement objective. |
| `scientific_rationale` | Why the agent thinks this measurement is worth doing. |
| `comparison_targets` | Prior state, evidence, or analysis artifacts this intent should test against. |
| `expected_evidence` | Artifacts expected after successful execution. |
| `success_criteria` | Conditions for interpreting the run as useful. |
| `stop_conditions` | Conditions that should prevent or halt the action. |
| `planned_measurement` | Measurement family, sequence, target, and planned parameters. |
| `submit_spec` or `submit_spec_path` | Deterministic backend-facing measurement specification. |
| `safety_contract` | Human-readable boundary between agent reasoning and backend action. |
| `safety_verification` | Machine-readable record of checks required before submission. |

## Backend Boundary

The public release exposes the intent and submit-spec records plus the
execution-source boundary. Direct public execution is disabled, and private live
queue roots/configuration are excluded.

That boundary is part of the intent design. A reviewer can inspect whether the
agent's scientific plan, the deterministic submit spec, and the backend boundary
agree before any result is considered evidence.

## Why It Matters

The intent record is useful scientifically and operationally.

Scientifically, it preserves the hypothesis-like step before the measurement:
what was expected, what comparison was intended, and what would count as useful
evidence.

Operationally, it gives deterministic code a narrow job: check project state,
schema shape, and backend boundary. The agent keeps responsibility for research
judgment, while code enforces the parts that should not depend on judgment.
