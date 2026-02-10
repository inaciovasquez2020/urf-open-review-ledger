#!/usr/bin/env python3
import json, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
P = ROOT / "PROVENANCE.json"

def sh(cmd):
    return subprocess.check_output(cmd, cwd=ROOT).decode().strip()

def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)

data = json.loads(P.read_text(encoding="utf-8"))

parent = sh(["git","rev-parse","HEAD^"])
if data.get("commit","") != parent:
    fail(f"provenance mismatch: PROVENANCE={data.get('commit')} parent(HEAD)={parent}")

print("OK: PROVENANCE.json = parent(HEAD)")
