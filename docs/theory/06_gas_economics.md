# Gas economics

Gas fee = gas units × (base fee + tip) × ETH price. On Arbitrum, plus a cost for
posting data to Ethereum. A round trip = 2 transactions, 4 swaps.

Per unit of position: gross edge ≈ (entry_z − exit_z) × eq_std; trading cost ≈
4 × (pool fee + price impact); gas is a fixed dollar amount, so larger
positions dilute it.

Break-even position = 2·gas / (max_gas_share × (edge − 4·cost)).
If edge ≤ 4·cost, no position size is profitable.

Findings: <fill in from the table: which eq_std/gas combinations work, and what
happened with a 0.3% pool>.