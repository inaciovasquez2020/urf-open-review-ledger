from pathlib import Path

FORBIDDEN = [
    "canonical",
    "axioms",
    "dependency-ledger",
]

REQUIRED = [
    "README.md",
    "docs/CANONICAL_BOUNDARY.md",
    "docs/CONTRIBUTION_CLASSES.md",
    "docs/PROMOTION_PROTOCOL.md",
    "glossaries/urf-glossary.md",
    "maps/axiom-to-example-map.md",
    "maps/theorem-to-test-map.md",
    "maps/interfaces/public-object-index.md",
    "examples/minimal/README.md",
    "implementations/reference/README.md",
]

def test_forbidden_roots_absent() -> None:
    root = Path(__file__).resolve().parents[2]
    for name in FORBIDDEN:
        assert not (root / name).exists(), f"forbidden path present: {name}"

def test_required_public_interface_files_present() -> None:
    root = Path(__file__).resolve().parents[2]
    for rel in REQUIRED:
        assert (root / rel).exists(), f"missing required interface file: {rel}"
