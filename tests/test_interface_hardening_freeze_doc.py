from pathlib import Path

def test_interface_hardening_freeze_doc_exists():
    p = Path("docs/status/INTERFACE_HARDENING_FREEZE_2026_04_17.md")
    assert p.exists()

def test_interface_hardening_freeze_doc_content():
    s = Path("docs/status/INTERFACE_HARDENING_FREEZE_2026_04_17.md").read_text()
    assert "scripts/test_repo.zsh present" in s
    assert "python3 -m pytest -q" in s
