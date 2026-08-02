# alphaos-core 

## What this is 
AlphaOS Core is a small Python package that loads historical price data and computes daily and cumulative returns. It is the foundation for a larger project called AlphaOS, an AI - powered investment research and portfolio intelligence platform

## What it does 
- Loads historical stock price data from CSV files and validates the data 
- Computes daily returns to measure day-to-day price changes 
- Calculates cumulative returns to measure overall investment performance over a period 

## Install

```bash 
# Clone the repository 
git clone <your-github-repostiroy-url>
cd alphaos-core

# Install dependencies 
uv sync 

# Activate the virtual environment (optional)
source .venv/bin/activate 

## Tests 
Run the test suite using: 
uv run pytest 

To run tests with detailed output: 
uv run pytest -v
