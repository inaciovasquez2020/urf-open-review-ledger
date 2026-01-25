import json, numpy as np, sys, hashlib

path = sys.argv[1]
with open(path, "rb") as f:
    raw = f.read()
    cert = json.loads(raw)

G = np.array(cert["gram_matrix"])
alpha = cert["alpha"]

h = hashlib.sha256(raw).hexdigest()
lam = np.linalg.eigvalsh(G)[0]

print("sha256 =", h)
print("lambda_min =", lam)
print("alpha =", alpha)

if lam >= alpha and alpha > 0:
    print("PASS: URF-SG certificate valid")
else:
    print("FAIL: spectral gap violated")

