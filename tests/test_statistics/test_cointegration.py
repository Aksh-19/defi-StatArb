import numpy as np
from src.statistics.cointegration import engle_granger

def _pair(n=1000, seed=1):
    r = np.random.default_rng(seed)
    x = np.cumsum(r.normal(size=n))
    noise = np.zeros(n)
    for t in range(1, n):
        noise[t] = 0.9 * noise[t - 1] + r.normal()
    return 2 * x + 5 + noise, x

def test_detects_cointegration_and_recovers_beta():
    y, x = _pair()
    res = engle_granger(y, x)
    assert res.is_cointegrated
    assert abs(res.hedge_ratio - 2) < 0.1

def test_false_positive_rate_is_controlled():
    hits = 0
    for seed in range(100):
        r = np.random.default_rng(seed)
        res = engle_granger(np.cumsum(r.normal(size=500)),
                            np.cumsum(r.normal(size=500)))
        hits += res.is_cointegrated
    assert hits / 100 < 0.15      # expect about 5%