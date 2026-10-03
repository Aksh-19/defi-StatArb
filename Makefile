.PHONY: test lint run deploy setup test-contracts

setup:
	python3 -m venv .venv
	.venv/bin/pip install -e .
	cd contracts && forge install

test:
	pytest tests/

lint:
	flake8 src/ tests/
	black --check src/ tests/

test-contracts:
	cd contracts && forge test

deploy:
	cd contracts && forge script script/Deploy.s.sol --rpc-url $${ARBITRUM_SEPOLIA_RPC_URL} --broadcast

run-paper:
	python src/main.py --mode paper

run-live:
	python src/main.py --mode live

dashboard:
	streamlit run src/monitoring/dashboard.py
