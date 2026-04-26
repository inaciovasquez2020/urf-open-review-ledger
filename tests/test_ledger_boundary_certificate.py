from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ledger_boundary_certificate import missing_required_paths, ledger_boundary_certificate


BOUNDARY = """
No repository-level claim of completed external review.
No repository-level claim of peer-reviewed acceptance.
No repository-level claim that ledger entries are independent validation unless explicitly documented.
"""


def test_missing_required_paths_detects_absence() -> None:
    missing = missing_required_paths(ROOT, ["docs/status/LEDGER_BOUNDARY_CERTIFICATE.md", "definitely_missing.file"])
    assert "definitely_missing.file" in missing


def test_ledger_boundary_certificate_passes_for_manifest() -> None:
    cert = ledger_boundary_certificate(
        ROOT,
        [
            "docs/status/LEDGER_BOUNDARY_CERTIFICATE.md",
            "scripts/verify_ledger_boundary_certificate.py",
            "src/ledger_boundary_certificate.py",
            "tests/test_ledger_boundary_certificate.py",
        ],
        BOUNDARY,
    )
    assert cert.theorem_id == "UORL-LBC-1"
    assert cert.status == "PASS"
    assert cert.required_count == 4
    assert cert.present_count == 4
    assert cert.missing == ()
    assert cert.all_required_present is True
    assert cert.boundary_declared is True


def test_ledger_boundary_certificate_fails_without_boundary() -> None:
    cert = ledger_boundary_certificate(ROOT, ["docs/status/LEDGER_BOUNDARY_CERTIFICATE.md"], "")
    assert cert.status == "FAIL"
    assert cert.boundary_declared is False


def test_repository_scope_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/verify_ledger_boundary_certificate.py"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    assert '"theorem_id": "UORL-LBC-1"' in result.stdout
    assert '"status": "PASS"' in result.stdout


def test_nonclaim_boundary_retained() -> None:
    text = (ROOT / "docs/status/LEDGER_BOUNDARY_CERTIFICATE.md").read_text(encoding="utf-8")
    assert "No repository-level claim of completed external review." in text
    assert "No repository-level claim of peer-reviewed acceptance." in text
    assert "No repository-level claim that ledger entries are independent validation unless explicitly documented." in text
