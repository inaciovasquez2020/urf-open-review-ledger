from pathlib import Path

def test_scope_limitations_status():
    text = Path("SCOPE_LIMITATIONS_STATUS.md").read_text(encoding="utf-8")
    assert "- canonical" in text
    assert "- public-review-ledger" in text
    assert "- certificate-verified" in text
    assert "- not theorem-prover-complete" in text
    assert "- not a primary mathematics-closure repository" in text
    assert "the repository has no live missing-math theorem lock" in text
    assert "review-ledger/process hardening" in text

def test_scope_matches_repo_role_surface():
    scope = Path("SCOPE_LIMITATIONS_STATUS.md").read_text(encoding="utf-8")
    readme = Path("README.md").read_text(encoding="utf-8")
    governance = Path("GOVERNANCE.md").read_text(encoding="utf-8")
    accept = Path("MANUSCRIPT_ACCEPTABILITY.md").read_text(encoding="utf-8")
    assert "public manuscript registry and open review ledger" in scope
    assert "review" in readme.lower()
    assert "governance" in governance.lower() or "policy" in governance.lower()
    assert "acceptability" in accept.lower() or "manuscript" in accept.lower()
