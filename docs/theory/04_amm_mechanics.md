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
   Check: a 10 ETH sale raised k from 3,000,000,000 to 3,000,089,112, which
   matches the 0.03 ETH fee × the pool's USDC reserve after the trade.
2. **Price impact:** about Δx / (x + Δx), the trade size relative to pool
   depth. Moving along the curve gives a worse average price.

Experiment (1,000 ETH / 3M USDC pool):
sell 1 ETH → 0.40% below mid, 10 ETH → 1.28%, 100 ETH → 9.34%.
Doubled pool (2,000 ETH / 6M USDC): 
sell 1 ETH → 0.35% below mid, 10 ETH → 0.79%, 100 ETH → 5.03%.

## Why it matters for stat arb
- Impact depends on trade size relative to pool depth, not on dollars:
  deeper pools mean cheaper trades.
- Each leg of a trade pays this. A spread edge must be larger than the
  combined cost of both legs, plus gas, or the trade loses money.
- Uniswap V3 concentrates liquidity in price ranges, so depth varies with
  price (covered later at overview level).