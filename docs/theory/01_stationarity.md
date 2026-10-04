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

## ADF and KPSS

**ADF (Augmented Dickey-Fuller).** Rewrites the series as Δy_t = β·y_{t-1} + noise,
where β = φ − 1. β = 0 means a random walk. The test asks whether β is
significantly negative, i.e. whether there is a pull back toward the mean.
- Null hypothesis: unit root (non-stationary).
- Small p-value (< 0.05) → reject the null → evidence of stationarity.
- The statistic is a t-statistic, but it follows the Dickey-Fuller distribution,
  so critical values are more negative (about −2.86 at 5%).
- Weakness: low power. It struggles to separate φ = 0.99 from φ = 1.

**KPSS.** The reverse test.
- Null hypothesis: the series is stationary.
- Small p-value → reject → evidence of non-stationarity.

**Why both.** Each test fails in a different way, so agreement is stronger evidence.

| ADF | KPSS | Conclusion |
|---|---|---|
| stationary | stationary | strong evidence of stationarity |
| non-stationary | non-stationary | clearly non-stationary |
| stationary | non-stationary | ambiguous (possibly trend-stationary) |
| non-stationary | stationary | ambiguous (weak mean reversion or low power) |

**Check I did:** computed the ADF statistic by hand with a regression and
matched the library to ~15 digits.

**Check 2: the φ experiment (1,000 points).**

| φ | ADF p | KPSS p | Verdict |
|---|---|---|---|
| 1.0 | 0.982 | 0.01 | non-stationary (correct) |
| 0.99 | 0.246 | 0.01 | non-stationary (wrong: it is stationary) |
| 0.95 | 0.0 | 0.028 | ambiguous (it is stationary) |
| 0.5 | 0.0 | 0.1 | stationary (correct) |

Lessons:
- At φ = 0.99 (half-life ≈ 69 steps) both tests agreed and were both wrong,
  because 1,000 points are not enough to tell it from a random walk.
  Agreement between the tests is not proof.
- At φ = 0.95, KPSS over-rejects a persistent but stationary series.

**How I will use this.** ADF on the spread (through Engle-Granger) is the
primary gate for screening pairs. KPSS is a supporting flag, and an
"ambiguous" result does not automatically reject a pair. Half-life and
out-of-sample validation make the final call.