#!/usr/bin/env python3
import json, hashlib, argparse
import numpy as np


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def is_symmetric(A, tol=1e-10):
    return np.max(np.abs(A - A.T)) <= tol


def is_projector(P, tol=1e-10):
    return is_symmetric(P, tol) and np.max(np.abs(P @ P - P)) <= tol


def gershgorin_lower_bound(A):
    diag = np.diag(A)
    off = np.sum(np.abs(A), axis=1) - np.abs(diag)
    return float(np.min(diag - off))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cert", help="path to cert.json")
    ap.add_argument("--mode", choices=["eig", "gershgorin"], default="eig")
    args = ap.parse_args()

    path = args.cert
    mode = args.mode

    with open(path, "r", encoding="utf-8") as f:
        cert = json.load(f)

    # Required fields
    for k in ["schema_version","kind","id","created_utc","n","epsilon","L","P"]:
        if k not in cert:
            raise SystemExit(f"FAIL: missing field {k}")

    if cert["kind"] != "URF_SPECTRAL_GAP_CERT":
        raise SystemExit("FAIL: wrong kind")

    n = int(cert["n"])
    eps = float(cert["epsilon"])
    if eps <= 0:
        raise SystemExit("FAIL: epsilon must be > 0")

    L = np.array(cert["L"], dtype=float)
    P = np.array(cert["P"], dtype=float)

    if L.shape != (n,n) or P.shape != (n,n):
        raise SystemExit("FAIL: matrix shapes do not match n")

    if not is_symmetric(L):
        raise SystemExit("FAIL: L is not symmetric")

    if not is_projector(P):
        raise SystemExit("FAIL: P is not an orthogonal projector")

    I = np.eye(n)
    Q = I - P
    A = Q @ L @ Q

    # Orthonormal basis for im(Q)
    U, s, _ = np.linalg.svd(Q)
    idx = np.where(s > 1e-8)[0]
    if len(idx) == 0:
        raise SystemExit("FAIL: im(Q) is {0}")

    B = U[:, idx]
    Ared = B.T @ A @ B

    if mode == "eig":
        w = np.linalg.eigvalsh(Ared)
        lam_min = float(np.min(w))
    else:
        lam_min = gershgorin_lower_bound(Ared)

    if lam_min + 1e-10 < eps:
        raise SystemExit(
            f"FAIL: spectral gap check failed: lam_min={lam_min} < eps={eps}"
        )

    print("OK")
    print(f"mode                   = {mode}")
    print(f"lambda_min(QLQ|im(Q)) = {lam_min}")
    print(f"epsilon               = {eps}")
    print(f"sha256(cert)          = {sha256_file(path)}")


if __name__ == "__main__":
    main()

