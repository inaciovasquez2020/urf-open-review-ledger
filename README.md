# urf-core-community

## Status
Public additive interface layer for URF.

## Canonical source
The authoritative source remains `inaciovasquez2020/urf-core`.

## Repository function
This repository exists to make the canonical system usable without modifying canonical authority.

## Admissible contribution classes
1. examples
2. exposition
3. tests
4. implementations
5. visualizations
6. non-canonical extensions explicitly labeled as such

## Inadmissible contribution classes
1. edits to canonical theorem statements
2. edits to canonical axioms
3. edits to dependency ledgers
4. edits to closure claims
5. parallel authority claims

## Promotion rule
No artifact here changes canonical status unless explicitly promoted by maintainer review into `urf-core`.

## Verification Path

Minimal local verification:
- `python3 -m pytest -q`
- `./scripts/test_repo.zsh`

Minimal reading order:
1. `docs/examples/QUICKSTART.md`
2. `docs/examples/MINIMAL_PUBLIC_WORKFLOW.md`
3. `docs/status/CORE_INTERFACE_HARDENING_2026_04_17.md`
4. `docs/status/PYTEST_NORMALIZATION_2026_04_17.md`
5. `docs/status/INTERFACE_HARDENING_FREEZE_2026_04_17.md`

Authority rule:
- Canonical authority remains in `urf-core`.
- This repository is a public additive interface layer.
