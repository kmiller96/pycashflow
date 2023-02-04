"""Validates that you can self-reference line items."""

import pytest

from pycashflow import LineItem


def test_can_use_previous_step() -> None:
    """Validates that you can self-reference line items."""
    line = LineItem(lambda t, self: 0 if t == 0 else self(t - 1) + t)

    assert line(0) == 0
    assert line(1) == 1
    assert line(2) == 3
    assert line(3) == 6


@pytest.mark.parametrize(
    "func",
    [
        lambda t, self: self(t - 1) + t,
        lambda t, self: self(t + 1) + t,
    ],
)
def test_raises_recursion_error_if_undefined(func) -> None:
    """Validates that a recursion error is raised if the line item is poorly defined."""
    line = LineItem(func)

    with pytest.raises(RecursionError):
        line(0)  # Will recurse infinitely
