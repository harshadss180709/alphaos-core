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

## 2026-08-05 — Return type and rounding for cumulative_return

**Decision:**
Return a `Decimal` quantised to 6 decimal places using `ROUND_HALF_UP`.

```python
return Decimal(str(total)).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
```

**Why a Decimal, when a return is a ratio:**

This sits in tension with the rule above, and the tension is deliberate. A
daily return is an intermediate value consumed by other calculations, so
`float` is right. A cumulative return is a **headline figure** — it gets
reported, stored and compared against a benchmark.

Multiplying nine floats gives `0.06080000000000001` where the true answer is
`0.0608`. A report should not show that. Rounding once, at a defined point,
with a defined rule, makes the output reproducible across runs and machines.

**Why ROUND_HALF_UP:**

Python's default is `ROUND_HALF_EVEN` (banker's rounding), which rounds 0.5 to
the nearest even digit. It is statistically better because it does not bias
sums upward. But finance conventionally rounds half up, and matching
convention matters when a figure has to agree with a broker or exchange
statement.

**Important detail — `str()` before `Decimal()`:**

`Decimal(total)` would carry the float's binary error straight in, exactly as
`Decimal(0.1)` produced 55 digits on Day 2. Converting via the string
representation gives the intended value. Whenever a float must become a
Decimal, it goes through `str()`.

**Revisit:** if AlphaOS ever needs more than 6 decimal places of precision on
a reported return, or if a downstream consumer needs the unrounded value, this
should return both.