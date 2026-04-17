# Pytest Normalization

Canonical invocation:
- python3 -m pytest

Reason:
- avoids stale script interpreter failures
- uses active Python environment

Repository rule:
- prefer module invocation in examples and local verification commands
