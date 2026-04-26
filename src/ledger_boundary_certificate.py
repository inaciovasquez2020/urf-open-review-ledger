from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class LedgerBoundaryCertificate:
    theorem_id: str
    status: str
    required_count: int
    present_count: int
    missing: tuple[str, ...]
    all_required_present: bool
    boundary_declared: bool


def _normalize_required(paths: Iterable[str]) -> tuple[str, ...]:
    out: list[str] = []
    for p in paths:
        s = str(p).strip()
        if not s:
            raise ValueError("required paths must be nonempty")
        out.append(s)
    if not out:
        raise ValueError("at least one required path is needed")
    return tuple(out)


def missing_required_paths(root: Path | str, required: Sequence[str]) -> tuple[str, ...]:
    base = Path(root)
    normalized = _normalize_required(required)
    return tuple(p for p in normalized if not (base / p).exists())


def ledger_boundary_certificate(root: Path | str, required: Sequence[str], boundary_text: str) -> LedgerBoundaryCertificate:
    normalized = _normalize_required(required)
    missing = missing_required_paths(root, normalized)
    boundary = str(boundary_text)
    boundary_declared = all(
        token in boundary
        for token in [
            "No repository-level claim of completed external review.",
            "No repository-level claim of peer-reviewed acceptance.",
            "No repository-level claim that ledger entries are independent validation unless explicitly documented.",
        ]
    )
    passed = not missing and boundary_declared
    return LedgerBoundaryCertificate(
        theorem_id="UORL-LBC-1",
        status="PASS" if passed else "FAIL",
        required_count=len(normalized),
        present_count=len(normalized) - len(missing),
        missing=missing,
        all_required_present=not missing,
        boundary_declared=boundary_declared,
    )
