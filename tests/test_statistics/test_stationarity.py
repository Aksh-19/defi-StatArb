import numpy as np
from src.statistics.stationarity import check_stationarity

def _ar1(phi, n=2000, seed=0):
    rng = np.random.default_rng(seed)
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + rng.normal()
    return x

def test_random_walk_is_non_stationary():
    assert check_stationarity(_ar1(1.0)).conclusion == "non-stationary"

def test_mean_reverting_is_stationary():
    assert check_stationarity(_ar1(0.5)).conclusion == "stationary"