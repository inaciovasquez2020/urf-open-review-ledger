from pathlib import Path

def test_status_exists():
    p = Path("docs/status/CORE_INTERFACE_HARDENING_2026_04_17.md")
    assert p.exists()

def test_canonical_separation():
    s = Path("docs/status/CORE_INTERFACE_HARDENING_2026_04_17.md").read_text()
    assert "urf-core" in s
    assert "does not alter canonical authority" in s

def test_quickstart_exists():
    assert Path("docs/examples/QUICKSTART.md").exists()
