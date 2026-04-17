from pathlib import Path

def test_minimal_public_workflow_doc_exists():
    p = Path("docs/examples/MINIMAL_PUBLIC_WORKFLOW.md")
    assert p.exists()

def test_minimal_public_workflow_doc_content():
    s = Path("docs/examples/MINIMAL_PUBLIC_WORKFLOW.md").read_text()
    assert "python3 -m pytest -q" in s
    assert "./scripts/test_repo.zsh" in s
    assert "canonical authority in urf-core" in s
