from pathlib import Path

def test_readme_has_verification_path():
    s = Path("README.md").read_text()
    assert "## Verification Path" in s
    assert "python3 -m pytest -q" in s
    assert "./scripts/test_repo.zsh" in s

def test_readme_preserves_authority_rule():
    s = Path("README.md").read_text()
    assert "Canonical authority remains in `urf-core`." in s
    assert "public additive interface layer" in s
