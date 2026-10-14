# OU process and half-life

dS = κ(μ − S)dt + σ dW. μ is the target level, κ the spring strength, σ the noise.
Sampled per period it is an AR(1): S_{t+1} = a + φ S_t + noise, with φ = e^(−κ).

- κ = −ln φ, μ = a/(1 − φ), half-life = ln 2 / κ (in periods).
- Equilibrium std = residual std / √(1 − φ²): the typical width of the spread.
- φ ≥ 1 means no spring: not tradable.
- Half-life must fit the trading horizon: fast enough that capital is not tied
  up, slow enough that costs and execution delay do not eat the move.
- The roadmap approximates κ ≈ −b from ΔS on S; I use the exact −ln φ.

Experiment: parameter estimates are noisy on short samples. True half-life
13.5; with n=200 the 10th–90th percentile range was <fill in>.