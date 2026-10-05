from dataclasses import dataclass
import numpy as np
from statsmodels.tsa.stattools import coint

@dataclass
class CointegrationResult:
    is_cointegrated: bool
    pvalue: float            # Engle-Granger p-value (correct critical values)
    test_statistic: float
    hedge_ratio: float       # beta
    intercept: float         # alpha
    spread: np.ndarray       # y - alpha - beta * x

def engle_granger(y, x, significance: float = 0.05) -> CointegrationResult:
    y, x = np.asarray(y, float), np.asarray(x, float)

    # Step 1: OLS  y = alpha + beta * x
    X = np.column_stack([np.ones(len(x)), x])
    intercept, hedge_ratio = np.linalg.lstsq(X, y, rcond=None)[0]
    spread = y - intercept - hedge_ratio * x

    # Step 2: stationarity test on the residual with the right critical values
    stat, pvalue, _ = coint(y, x, trend="c", autolag="aic")

    return CointegrationResult(pvalue < significance, pvalue, stat,
                               hedge_ratio, intercept, spread)