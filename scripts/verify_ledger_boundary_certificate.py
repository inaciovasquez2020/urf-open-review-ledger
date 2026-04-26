#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ledger_boundary_certificate import ledger_boundary_certificate


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    doc = ROOT / "docs/status/LEDGER_BOUNDARY_CERTIFICATE.md"
    source = ROOT / "src/ledger_boundary_certificate.py"
    status = ROOT / "STATUS.md"
    if not status.exists():
        status = ROOT / "README.md"
    require(doc.exists(), "missing ledger boundary certificate doc")
    require(source.exists(), "missing certificate source")
    require(status.exists(), "missing status/readme boundary source")
    boundary_text = doc.read_text(encoding="utf-8") + "\n" + status.read_text(encoding="utf-8")
    cert = ledger_boundary_certificate(
        ROOT,
        [
            "docs/status/LEDGER_BOUNDARY_CERTIFICATE.md",
            "scripts/verify_ledger_boundary_certificate.py",
            "src/ledger_boundary_certificate.py",
            "tests/test_ledger_boundary_certificate.py",
        ],
        boundary_text,
    )
    require(cert.theorem_id == "UORL-LBC-1", "wrong theorem id")
    require(cert.status == "PASS", f"certificate failed: {cert}")
    require(cert.all_required_present, "required manifest is incomplete")
    require(cert.boundary_declared, "ledger boundary missing")
    doc_text = doc.read_text(encoding="utf-8")
    for literal in [
        "Status: CLOSED repository-scope certificate.",
        "Theorem ID: UORL-LBC-1.",
        "No repository-level claim of completed external review.",
        "No repository-level claim of peer-reviewed acceptance.",
        "No repository-level claim that ledger entries are independent validation unless explicitly documented.",
    ]:
        require(literal in doc_text, f"missing doc literal: {literal}")
    print(json.dumps(cert.__dict__, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
