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
    raise NotImplementedError
