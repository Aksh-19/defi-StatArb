# AMM mechanics (constant product)

## The rule
A pool holds x of token A and y of token B. Every trade must keep x·y = k.
There is no order book. The marginal price of A in B is y/x.

## What happens in a trade
Selling Δx of A into the pool, after a fee f:
    Δx_eff = Δx·(1 − f)
    B received = y·Δx_eff / (x + Δx_eff)
(Buying Δx of A out of the pool costs y·Δx / (x − Δx) instead, which is a
different formula.)

## Where the cost comes from
1. **Fee:** flat (0.3% in V2). The fee stays in the pool, so k grows slightly.
2. **Price impact:** about Δx / (x + Δx), the trade size relative to pool
   depth. Moving along the curve gives a worse average price.

Experiment (1,000 ETH / 3M USDC pool):
sell 1 ETH → 0.40% below mid, 10 ETH → 1.28%, 100 ETH → 9.34%.

## Why it matters for stat arb
- Impact depends on trade size relative to pool depth, not on dollars:
  deeper pools mean cheaper trades.
- Each leg of a trade pays this. A spread edge must be larger than the
  combined cost of both legs, plus gas, or the trade loses money.
- Uniswap V3 concentrates liquidity in price ranges, so depth varies with
  price (covered later at overview level).