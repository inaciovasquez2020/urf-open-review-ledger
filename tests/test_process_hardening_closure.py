from pathlib import Path

def test_process_hardening_closure():
    text = Path("PROCESS_HARDENING_CLOSURE.md").read_text(encoding="utf-8")
    assert "- live mathematics frontier: none" in text
    assert "- live repository role: open review ledger" in text
    assert "- closure status within declared scope: complete" in text
    assert "there is no remaining theorem-level object to solve" in text

def test_scope_status_declares_no_live_frontier():
    text = Path("SCOPE_LIMITATIONS_STATUS.md").read_text(encoding="utf-8")
    assert "## Remaining Live Frontier" in text
    assert "- none" in text
    assert "not a primary mathematics-closure repository" in text
