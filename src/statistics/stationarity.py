from dataclasses import dataclass
import warnings
from statsmodels.tsa.stattools import adfuller, kpss

@dataclass
class StationarityResult:
    adf_statistic: float
    adf_pvalue: float
    adf_stationary: bool       # ADF rejects unit root (p < alpha)
    kpss_statistic: float
    kpss_pvalue: float
    kpss_stationary: bool      # KPSS fails to reject stationarity (p > alpha)
    conclusion: str            # "stationary" | "non-stationary" | "ambiguous"

def check_stationarity(series, significance: float = 0.05) -> StationarityResult:
    adf_stat, adf_p, *_ = adfuller(series, autolag="AIC")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")        # kpss p-value interpolation warning
        kpss_stat, kpss_p, *_ = kpss(series, regression="c", nlags="auto")

    adf_ok, kpss_ok = adf_p < significance, kpss_p > significance
    if adf_ok and kpss_ok:
        conclusion = "stationary"
    elif not adf_ok and not kpss_ok:
        conclusion = "non-stationary"
    else:
        conclusion = "ambiguous"
    return StationarityResult(adf_stat, adf_p, adf_ok,
                              kpss_stat, kpss_p, kpss_ok, conclusion)