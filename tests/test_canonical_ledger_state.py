from pathlib import Path

def test_ledger_state_exists():
    assert Path("docs/status/CANONICAL_LEDGER_STATE.md").exists()

def test_status_is_conditional():
    s = Path("docs/status/CANONICAL_LEDGER_STATE.md").read_text(encoding="utf-8")
    assert "Status: Conditional" in s

def test_classification_rule_present():
    s = Path("docs/status/CANONICAL_LEDGER_STATE.md").read_text(encoding="utf-8")
    assert "type-classified" in s
