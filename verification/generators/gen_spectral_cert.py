#!/usr/bin/env python3
import json, datetime, hashlib, argparse
import numpy as np

def write_sha256(path_json: str, path_sha: str):
    h = hashlib.sha256()
    with open(path_json, "rb") as f:
        h.update(f.read())
    with open(path_sha, "w", encoding="utf-8") as g:
        g.write(h.hexdigest() + "  " + path_json.split("/")[-1] + "\n")

def load_matrix(path: str, n: int | None):
    A = np.load(path)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(f"{path}: must be square 2D array")
    if n is not None and A.shape != (n, n):
        raise ValueError(f"{path}: shape {A.shape} does not match n={n}")
    return A.astype(float)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=None, help="matrix size (optional if loading .npy)")
    ap.add_argument("--epsilon", type=float, required=True)
    ap.add_argument("--L", type=str, default=None, help="path to L.npy")
    ap.add_argument("--P", type=str, default=None, help="path to P.npy")
    ap.add_argument("--id", type=str, default=None)
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    eps = float(args.epsilon)
    if eps <= 0:
        raise SystemExit("epsilon must be > 0")

    if args.L and args.P:
        L = load_matrix(args.L, args.n)
        P = load_matrix(args.P, L.shape[0])
        n = L.shape[0]
        notes = "Loaded from .npy"
    else:
        n = int(args.n) if args.n is not None else 6
        L = np.diag([0.0] + [1.0] * (n - 1))
        P = np.zeros((n, n))
        P[0, 0] = 1.0
        notes = "Toy example"

    cid = args.id or f"URF-SG-{n}-{int(1000*eps)}"
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    out = args.out or f"URF-SG-{cid}.json"

    cert = {
        "schema_version": "1.0",
        "kind": "URF_SPECTRAL_GAP_CERT",
        "id": cid,
        "created_utc": now,
        "n": int(n),
        "epsilon": eps,
        "L": L.tolist(),
        "P": P.tolist(),
        "notes": notes
    }

    with open(out, "w", encoding="utf-8") as f:
        json.dump(cert, f, indent=2, sort_keys=True)

    write_sha256(out, out.replace(".json", ".sha256"))
    print(out)

if __name__ == "__main__":
    main()

