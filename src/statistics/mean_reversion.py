import numpy as np

def fit_ou_process(spread) -> dict:
    """Fit S_{t+1} = a + phi*S_t + noise. Results are in units of 'periods'."""
    s = np.asarray(spread, float)
    s_lag, s_next = s[:-1], s[1:]
    X = np.column_stack([np.ones(len(s_lag)), s_lag])
    a, phi = np.linalg.lstsq(X, s_next, rcond=None)[0]
    resid = s_next - X @ np.array([a, phi])
    resid_std = resid.std(ddof=2)

    if phi >= 1:                      # no spring: not mean-reverting
        return {"phi": phi, "kappa": 0.0, "mu": np.nan, "half_life": np.inf,
                "resid_std": resid_std, "eq_std": np.inf, "sigma": np.nan}
    mu = a / (1 - phi)
    eq_std = resid_std / np.sqrt(1 - phi**2)
    if phi <= 0:                      # flips sign each step: reverts within 1 period
        return {"phi": phi, "kappa": np.inf, "mu": mu, "half_life": 0.0,
                "resid_std": resid_std, "eq_std": eq_std, "sigma": np.nan}
    kappa = -np.log(phi)
    return {"phi": phi, "kappa": kappa, "mu": mu,
            "half_life": np.log(2) / kappa,
            "resid_std": resid_std, "eq_std": eq_std,
            "sigma": eq_std * np.sqrt(2 * kappa)}   # since eq_var = sigma^2 / (2 kappa)

def compute_half_life(spread) -> float:
    return fit_ou_process(spread)["half_life"]