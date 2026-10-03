# DeFi Statistical Arbitrage Engine

A complete statistical arbitrage system for decentralized exchanges — from mathematical research to live execution on a blockchain testnet. Finds token pairs that are statistically bound together, detects when they diverge, and executes atomic trades to capture the reversion.

## Architecture

- **Research Environment:** Jupyter notebooks for statistical testing (ADF, Engle-Granger, OU process).
- **Core Package (`src/`):** Python backtesting and real-time execution engine.
- **Smart Contracts (`contracts/`):** Foundry-based Solidity contracts for atomic trade execution.
- **Data Engineering:** Ingests from CoinGecko (historical), The Graph (historical swap events), and on-chain RPC (real-time pool prices).

## Setup Guide

### 1. Prerequisites
- Python 3.10+
- Foundry (Solidity framework)
- Node/npm (optional, for tooling)

### 2. Python Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Smart Contracts (Foundry)
```bash
cd contracts
forge install
forge build
```

### 4. Configuration
Copy `.env.example` to `.env` and fill in the required values.

## Development Commands
See `Makefile` for available commands.
