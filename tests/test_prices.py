import pytest

from alphaos_core.prices import load_prices


def test_load_prices_raises_on_missing_file():
    """A missing file must fail loudly, not return an empty frame."""
    with pytest.raises(FileNotFoundError):
        load_prices("does/not/exist.csv")