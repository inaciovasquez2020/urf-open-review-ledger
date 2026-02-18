URF Review Finite State Machine (v1)

States
- DRAFT
- FROZEN
- OPEN_REVIEW
- REVIEWED
- CONDITIONAL
- DISPUTED
- CERTIFIED
- SUPERSEDED
- WITHDRAWN

Transitions

DRAFT -> FROZEN
Requires a tagged version and immutable artifact hash.

FROZEN -> OPEN_REVIEW
Review window opened.

OPEN_REVIEW -> REVIEWED
At least one substantive review completed.
No unresolved blocking objections.

OPEN_REVIEW -> CONDITIONAL
Result is sound only under explicitly stated missing lemma(s) or assumption(s).

OPEN_REVIEW -> DISPUTED
A blocking objection is raised.

REVIEWED -> CONDITIONAL
A missing assumption is identified post-review.

REVIEWED -> DISPUTED
A blocking objection is raised post-review.

DISPUTED -> OPEN_REVIEW
All blocking objections resolved.

REVIEWED or CONDITIONAL -> CERTIFIED
All stated conditions discharged and review complete.

Any state -> SUPERSEDED
A newer frozen version replaces this one.

DRAFT, FROZEN, OPEN_REVIEW, DISPUTED -> WITHDRAWN
Author withdraws the manuscript from review.

Blocking objection definition

An objection is blocking if and only if it provides:
- an explicit counterexample witness, or
- an exact missing lemma or assumption stated precisely, or
- a localized proof gap used downstream.
