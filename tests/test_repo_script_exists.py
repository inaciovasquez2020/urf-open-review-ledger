from pathlib import Path

def test_repo_script_exists():
    p = Path("scripts/test_repo.zsh")
    assert p.exists()

def test_repo_script_uses_module_pytest():
    s = Path("scripts/test_repo.zsh").read_text()
    assert "python3 -m pytest -q" in s
