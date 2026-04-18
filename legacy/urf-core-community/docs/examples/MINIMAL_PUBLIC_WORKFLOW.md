# Minimal Public Workflow

1. Start from the frozen interface tag or current main.
2. Run local verification with:
   - python3 -m pytest -q
   - ./scripts/test_repo.zsh
3. Read:
   - docs/examples/QUICKSTART.md
   - docs/status/CORE_INTERFACE_HARDENING_2026_04_17.md
   - docs/status/INTERFACE_HARDENING_FREEZE_2026_04_17.md
4. Keep canonical authority in urf-core.
5. Restrict public additions here to:
   - examples
   - exposition
   - tests
   - implementations
   - visualizations
   - explicitly labeled non-canonical extensions
