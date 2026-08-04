# Decisions 

## 2026-08-03 - mypy and pandas type checking 

### Decision 

I decided to ignore missing pandas type information in mypy for now.

Added:

'ignore_missing_imports = true'

for pandas in 'pyproject.toml'.

### Why I chose this 

I considered installing 'pandas-stubs' for better type checking.

But right now, my project uses only basic pandas features, and strict checking creates many extra errors inside pandas itself 

Those errors do not help me improve my own code at this stage 

So for now:
- My own code will still be checked by mypy 
- Pandas internal code will be ignored

### Revisit 

I will review this decision in Week 2 when AlphaOS starts using pandas more heavily 

## 2026-08-04 — Decimal to Float Boundary in daily_returns

**Decision:**
Convert Decimal stock prices into float before calculating daily returns.

```python
closes = prices["close"].astype(float)
```

**Why:**

In AlphaOS, stock prices are stored as Decimal because they represent real
money values and require accuracy.

However, daily returns are not money values. They are statistical values used
for analysis and machine learning models.

The calculation:
Daily Return = (Today's Close / Yesterday's Close) - 1
does not need extremely high decimal precision, because returns, volatility
and other features are approximate statistical values.

Keeping the Decimal → float conversion on one clear line makes the data type
change visible and easier to understand.

**Important learning:**

`shift(1)` creates a NaN value for the first row, because there is no previous
day's price to calculate a return from. Decimal refuses to divide by NaN, so
converting to float before the calculation avoids unnecessary complexity.

**Rejected:**

Calculating returns entirely in Decimal and converting to float afterwards.

Reasons:

- More precision than needed for statistical calculations
- Slower calculations
- More complicated handling of NaN values

**Final AlphaOS rule:**

| Kind of value | Type |
|---|---|
| Money, prices, share quantities, cost basis | `Decimal` |
| Daily returns, volatility, correlation, model features | `float` |