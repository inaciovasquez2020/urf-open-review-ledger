# Scope and Limitations Status

## Repository Status
- canonical
- public-review-ledger
- certificate-verified
- not theorem-prover-complete
- not a primary mathematics-closure repository

## Canonical Surface
- README.md
- GOVERNANCE.md
- HOW_TO_REVIEW.md
- MANUSCRIPT_ACCEPTABILITY.md
- registry/
- status/
- docs/
- fsm/
- templates/

## Repository Role
This repository is a public manuscript registry and open review ledger.
Its role is to track immutable manuscript identifiers, review-state transitions,
public review records, governance constraints, and certificate-checked ledger consistency.

## Mathematical Scope
This repository does not serve as the canonical location for theorem closure of URF mathematics.
Mathematical claims live in the linked manuscript or source repositories.

## Validation Modality
Validation is ledger/certificate/workflow based:
- registry consistency
- status consistency
- certificate schema checks
- CI verification
It is not a Lean-level theorem-complete repository.

## Closure Statement
Within its declared scope, the repository has no live missing-math theorem lock.
The remaining gap is review-ledger/process hardening, not theorem existence.

## Canonical Upgrade Path
Any future strengthening should be labeled as one of:
- schema hardening
- workflow verification
- registry/status consistency
- review-governance clarification
and must not relabel the repository as theorem-complete without a new proof layer.
