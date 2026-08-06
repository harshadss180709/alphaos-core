from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import pandas as pd


def load_prices(csv_path: str | Path) -> pd.DataFrame:
    """Load a daily price CSV into a DataFrame.

    The CSV must have columns: date, close.

    Returns:
        DataFrame with:
        - UTC timezone-aware DatetimeIndex named "date"
        - sorted dates with no duplicates
        - "close" column containing Decimal values

    Raises:
        FileNotFoundError:
            If the CSV file does not exist.

        ValueError:
            If required columns are missing, file is empty,
            dates are duplicated, or prices are invalid.
    """

    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"No such file: {path}")

    df = pd.read_csv(path, converters={"close": Decimal})

    for column in ["date", "close"]:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    if df.empty:
        raise ValueError(f"No rows in {path}")

    df["date"] = pd.to_datetime(df["date"], utc=True)

    df = df.set_index("date").sort_index()

    if df.index.has_duplicates:
        raise ValueError(f"Duplicate dates in {path}")

    if (df["close"] <= 0).any():
        raise ValueError(f"Non-positive close price in {path}")

    return df


def daily_returns(prices: pd.DataFrame) -> pd.Series:
    """Calculate simple daily returns.

    Formula:
        r_t = (close_t / close_t-1) - 1

    Returns:
        Float Series indexed by date.
        First date is removed because a return
        requires two prices.

    Raises:
        ValueError:
            If close column is missing or there are
            fewer than two prices.
    """

    if "close" not in prices.columns:
        raise ValueError("Missing required column: close")

    if len(prices) < 2:
        raise ValueError("Need at least two prices to compute a return")

    closes = prices["close"].astype(float)

    returns = closes / closes.shift(1) - 1

    return returns.rename("daily_return").dropna()


def cumulative_return(returns: pd.Series) -> Decimal:
    """Total compounded return over the whole series.

    Formula:
        (1 + r_1) * (1 + r_2) * ... * (1 + r_n) - 1

    Returns:
        Decimal quantised to 6 decimal places, rounded half up.
        Decimal is used because this is a headline figure that gets
        reported and compared, so it must round the same way every
        time on every machine.

    Raises:
        ValueError:
            If the series is empty or contains any NaN.
    """

    if returns.empty:
        raise ValueError("Cannot compute cumulative return of an empty series")

    if returns.isna().any():
        raise ValueError("Returns series contains NaN")

    total = float((1 + returns).prod() - 1)

    # str() first: Decimal(float) carries the binary error straight in,
    # exactly as Decimal(0.1) does.
    return Decimal(str(total)).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
