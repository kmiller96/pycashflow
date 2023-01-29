"""Validates that you can perform arithmetic on LineItems."""

import pytest

from pycashflow import LineItem


def test_lineitem_negation():
    """Tests that LineItems can be negated."""
    li = LineItem(lambda t: 1)
    result = -li
    assert result(0) == -1


@pytest.mark.parametrize(
    "left,right",
    [
        (1, LineItem(lambda t: 1)),
        (1.0, LineItem(lambda t: 1)),
        (LineItem(lambda t: 1), 1),
        (LineItem(lambda t: 1), 1.0),
    ],
)
def test_lineitem_addition(left, right):
    """Tests that LineItems can be added to numbers or other LineItems.""" ""
    result = left + right
    assert result(0) == 2.0


@pytest.mark.parametrize(
    "left,right",
    [
        (2, LineItem(lambda t: 1)),
        (2.0, LineItem(lambda t: 1)),
        (LineItem(lambda t: 2), 1),
        (LineItem(lambda t: 2), 1.0),
    ],
)
def test_lineitem_subtraction(left, right):
    """Tests that LineItems can be subtracted from numbers or other LineItems."""
    result = left - right
    assert result(0) == 1.0


@pytest.mark.parametrize(
    "left,right",
    [
        (2, LineItem(lambda t: 2)),
        (2.0, LineItem(lambda t: 2)),
        (LineItem(lambda t: 2), 2),
        (LineItem(lambda t: 2), 2.0),
    ],
)
def test_lineitem_multiplication(left, right):
    """Tests that LineItems can be multiplied against numbers or other LineItems."""
    result = left * right
    assert result(0) == 4.0


@pytest.mark.parametrize(
    "left,right",
    [
        (4, LineItem(lambda t: 2)),
        (4.0, LineItem(lambda t: 2)),
        (LineItem(lambda t: 4), 2),
        (LineItem(lambda t: 4), 2.0),
    ],
)
def test_lineitem_division(left, right):
    """Tests that LineItems can be divided against numbers or other LineItems."""
    result = left / right
    assert result(0) == 2.0


@pytest.mark.parametrize(
    "left,right",
    [
        (5, LineItem(lambda t: 2)),
        (5.0, LineItem(lambda t: 2)),
        (LineItem(lambda t: 5), 2),
        (LineItem(lambda t: 5), 2.0),
    ],
)
def test_lineitem_floordivision(left, right):
    """Tests that LineItems can be floor-divided against numbers or other LineItems."""
    result = left // right
    assert result(0) == 2.0
