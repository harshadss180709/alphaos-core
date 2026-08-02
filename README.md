# AlphaOS Core

## What this is

AlphaOS Core is a small Python package that loads historical price data and computes daily and cumulative returns. It is the foundation for a larger project called AlphaOS, an AI-powered investment research and portfolio intelligence platform.

## What it does

- Loads historical stock price data from CSV files and validates the data
- Computes daily returns to measure day-to-day price changes
- Calculates cumulative returns to measure overall performance over a period

## Install

```bash
# Clone the repository
git clone https://github.com/harshadss180709/alphaos-core.git
cd alphaos-core

# Install dependencies
uv sync
```

## Tests

Run the test suite using:

```bash
uv run pytest
```

To run tests with detailed output:

```bash
uv run pytest -v
```
