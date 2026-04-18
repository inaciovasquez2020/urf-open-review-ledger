from pathlib import Path

def test_gitignore_covers_python_cache():
    s = Path(".gitignore").read_text()
    assert "__pycache__/" in s
    assert "*.py[cod]" in s
