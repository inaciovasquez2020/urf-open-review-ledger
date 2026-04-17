from pathlib import Path

def test_pytest_normalization_doc_exists():
    p = Path("docs/status/PYTEST_NORMALIZATION_2026_04_17.md")
    assert p.exists()

def test_pytest_normalization_doc_content():
    s = Path("docs/status/PYTEST_NORMALIZATION_2026_04_17.md").read_text()
    assert "python3 -m pytest" in s
    assert "stale script interpreter failures" in s
