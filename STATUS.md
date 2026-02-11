# URF Core — Status

## What this repo guarantees
- Deterministic verification: same inputs (repo commit + certificate + environment constraints) => same verdict.
- Explicit hashing of verification-relevant artifacts (files, manifests, digests) when provided.

## What it verifies (given a certificate)
- Validity of a certificate under the verifier’s ruleset.
- Integrity checks: hashes, structural checks, and replay checks as implemented.

## What it does not claim
- It does not claim a theorem is true without a corresponding certificate and the verifier ruleset.
- It does not claim completeness outside the declared certificate format and verifier scope.
