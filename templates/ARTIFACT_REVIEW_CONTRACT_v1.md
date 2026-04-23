# Artifact Review Contract v1

## Required Fields
- artifact identifier
- immutable version pointer
- scope
- non-scope
- claims policy
- live public review issue
- closure status
- reviewer classification rule

## Reviewer Classification
- ERROR
- MISSING ASSUMPTION
- CLARIFICATION
- NON-BLOCKING SUGGESTION

## Minimum Public Review Rule
A public-facing artifact is not review-active unless it links to a live issue in `urf-open-review-ledger`.

## Falsifiability Rule
Each artifact must expose at least one explicit failure condition that would invalidate its current public claim.
