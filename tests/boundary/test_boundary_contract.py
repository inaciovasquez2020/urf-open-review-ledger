from pathlib import Path

FORBIDDEN = [
    "canonical",
    "axioms",
    "dependency-ledger",
]

def test_forbidden_roots_absent() -> None:
    root = Path(__file__).resolve().parents[2]
    for name in FORBIDDEN:
        assert not (root / name).exists(), f"forbidden path present: {name}"
