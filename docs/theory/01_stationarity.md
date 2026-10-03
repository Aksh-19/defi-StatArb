# Stationarity and the spread

## 1. What a spread is, and why we trade it
Statistical arbitrage doesn't bet on an asset going up or down. It bets that
the gap between two related assets will close. That gap is the **spread**,
usually log(price_A) − β·log(price_B), where β is the hedge ratio. Individual
prices wander unpredictably, but if two assets share a fundamental link, the
spread between them can be predictable. Our profit comes from **mean
reversion**: the spread returning to its average after an unusual stretch.
The risk is a **structural break**, where the average itself shifts for good
and the spread never returns. The rest of the project is about telling
those two cases apart.

## 2. Stationary vs random walk
A series is **stationary** if its mean and variance stay constant over time.
It wanders, but around a fixed level. A **random walk** (each value is the
previous value plus a random shock) has no such level, and its variance grows
without limit. In simulation, the spread of end values over 1,000 steps was
about 31 for a random walk but only about 3 for a stationary series, roughly
ten times smaller. Betting on a return to the mean only makes sense when
there is a mean to return to.

## 3. What phi controls
In x_t = φ·x_{t-1} + shock, φ is the strength of the "spring":
- φ = 1: no spring, a random walk.
- φ < 1: the series is pulled back toward its mean each step.
- The closer φ is to 1, the weaker the pull and the slower the reversion.

The long-run spread of the series is 1/√(1 − φ²), so a weaker spring means
wider excursions. The time to close half a gap is
**half-life = ln(0.5) / ln(φ)**:
- φ = 0.5 → about 1 step
- φ = 0.95 → about 13.5 steps
- φ = 0.99 → about 69 steps

At φ = 0.99 the series is technically stationary, but over a finite sample it
looks like a random walk with a slight leash. Telling φ = 0.99 apart from
φ = 1 takes a lot of data, which is why stationarity tests have low power.

## 4. Why this matters for the strategy
- We need spreads with a real spring (φ clearly below 1).
- The half-life must fit our trading horizon: fast enough that capital isn't
  locked up for months, slow enough that costs and execution delays don't
  eat the move.
- Every later tool (ADF/KPSS, cointegration, OU fitting) is a way of
  estimating whether a spring exists and how strong it is.

## 5. Blockchain note
Prices on a DEX only change when someone trades in that pool, so related
pools can drift apart between trades. Arbitrageurs close large gaps, but gas
and swap fees leave small ones standing. Those small gaps are what we try to
trade.