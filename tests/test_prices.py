from decimal import Decimal

import pandas as pd
import pytest

from alphaos_core.prices import cumulative_return, daily_returns, load_prices


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


def test_cumulative_return_matches_hand_computed_value():
    """Cumulative return over the fixture equals the hand-computed 0.060800.

    This is the only test where a human independently produced the expected
    answer with a calculator, so it proves the whole chain rather than one
    step. Exact equality is used, not pytest.approx, because the result is a
    Decimal - which is the entire argument for using Decimal here.
    """
    df = load_prices("tests/fixtures/simple_prices.csv")
    returns = daily_returns(df)

    assert cumulative_return(returns) == Decimal("0.060800")


def test_cumulative_return_agrees_with_last_over_first_price():
    """Compounding the returns equals last close / first close - 1.

    Two independent calculation paths must reach the same number. This is the
    telescoping product: every numerator cancels the next denominator.
    """
    df = load_prices("tests/fixtures/simple_prices.csv")
    returns = daily_returns(df)

    first = df["close"].iloc[0]
    last = df["close"].iloc[-1]
    expected = (last / first - 1).quantize(Decimal("0.000001"))

    assert cumulative_return(returns) == expected


def test_cumulative_return_rejects_nan():
    """A NaN in the series must raise rather than propagate silently."""
    bad = pd.Series([0.01, float("nan"), 0.02])

    with pytest.raises(ValueError):
        cumulative_return(bad)


def test_cumulative_return_rejects_empty_series():
    """An empty series has no cumulative return to report."""
    with pytest.raises(ValueError):
        cumulative_return(pd.Series([], dtype=float))
