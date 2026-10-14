import numpy as np
from src.statistics.mean_reversion import fit_ou_process, compute_half_life

def _ar1(phi, mu=0.0, n=20000, seed=0):
    r = np.random.default_rng(seed)
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + r.normal()
    return x + mu

def test_recovers_known_parameters():
    fit = fit_ou_process(_ar1(0.95, mu=3.0))
    assert abs(fit["half_life"] - np.log(2) / -np.log(0.95)) < 1.5   # about 13.5
    assert abs(fit["mu"] - 3.0) < 0.5

def test_random_walk_has_very_long_half_life():
    walk = np.cumsum(np.random.default_rng(1).normal(size=2000))
    assert compute_half_life(walk) > 50