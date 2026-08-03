from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import pandas as pd


def load_prices(csv_path: str | Path) -> pd.DataFrame:
    """Load a daily price CSV into a DataFrame.

    The CSV must have columns: date, close.

    Returns a DataFrame with:
      - a DatetimeIndex named "date", timezone-aware in UTC,
        sorted ascending, with no duplicate dates
      - a "close" column of Decimal objects

    Raises:
        FileNotFoundError: the path does not exist
        ValueError: required columns missing, file empty, duplicate
        dates, or any close value missing, non-numeric
        or negative
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
