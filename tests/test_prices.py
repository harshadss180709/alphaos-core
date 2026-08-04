from decimal import Decimal

import pandas as pd
import pytest

from alphaos_core.prices import daily_returns, load_prices


def test_load_prices_raises_on_missing_file():
    """A missing file must fail loudly, not return an empty frame."""
    with pytest.raises(FileNotFoundError):
        load_prices("does/not/exist.csv")


def test_load_prices_returns_clean_utc_decimal_frame():
    """Loading the fixture gives 10 UTC-indexed rows with Decimal closes."""
    df = load_prices("tests/fixtures/simple_prices.csv")

    assert len(df) == 10
    assert isinstance(df.index, pd.DatetimeIndex)
    assert isinstance(df["close"].iloc[0], Decimal)
    assert df["close"].iloc[0] == Decimal("100.00")


def test_daily_returns_matches_hand_computed_value():
    """First return equals the hand-computed (101/100) - 1."""
    df = load_prices("tests/fixtures/simple_prices.csv")
    returns = daily_returns(df)

    assert len(returns) == 9
    assert returns.iloc[0] == pytest.approx(0.01)


def test_daily_returns_rejects_single_row():
    """One price cannot produce a return."""
    df = load_prices("tests/fixtures/simple_prices.csv").head(1)

    with pytest.raises(ValueError):
        daily_returns(df)
