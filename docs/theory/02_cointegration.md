# Cointegration

## Correlation vs cointegration
- Correlation: short-term co-movement. Says nothing about long-run distance.
- Cointegration: each series is non-stationary, but y − β·x is stationary.
  The spread is bounded, like a dog on a leash.
- Independent random walks can show high level-correlation and a good-looking
  regression (spurious regression). Experiment: median |corr| = 0.39.

## Engle-Granger
1. OLS y = α + β·x + ε; β is the hedge ratio, ε is the spread.
2. Test ε for stationarity.
Critical values differ from a plain ADF because β was fitted to make ε look
stationary. Use statsmodels coint (MacKinnon values).
Experiment on 300 unrelated pairs: false positive rate EG = 4%, naive ADF = 13%.

## Notes for the project
- Use log prices.
- Result can depend on which asset is y; test both directions.
- Cointegration found in-sample can disappear. Out-of-sample checks come later.

## Uniswap V3 (overview)
Concentrated liquidity; depth varies with price; use the Quoter for quotes;
fee tiers matter; sqrtPriceX96 needs a decimals adjustment.