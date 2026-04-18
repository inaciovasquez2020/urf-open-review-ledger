# tests/test_pca_rank1.py

import os
import sys
import pytest
import numpy as np

# Ensure repo root is on PYTHONPATH so `standards` is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from standards.urf_sg_base_1.pca.rank1 import covariance, is_rank1


def test_rank1_synthetic():
    rng = np.random.default_rng(0)
    m, d = 100, 4
    u = rng.normal(size=(m, 1))
    v = rng.normal(size=(1, d))
    D = u @ v
    C = covariance(D)
    assert bool(is_rank1(C, tol=1e-12)) is True


def test_perfect_rank1():
    v = np.array([1.0, 2.0, 3.0])
    data = np.outer(v, v)
    assert bool(is_rank1(data)) is True


def test_noisy_rigidity_wall():
    v = np.array([1.0, 2.0, 3.0])
    pure_data = np.outer(v, v)
    noisy_data = pure_data + np.eye(3) * 0.5
    assert bool(is_rank1(noisy_data)) is False


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))

