"""Verifies that the line items behave as expected."""

import pytest

from pycashflow import Section, LineItem


def test_create_via_init():
    """Tests creating a line item via the __init__ method."""
    line_item = LineItem(lambda t: 100)
    assert line_item(0) == 100


def test_create_via_section():
    """Tests creating a line item via the section method."""
    section = Section("test")
    line_item = section.line("test", lambda t: 100)
    assert line_item(0) == 100


def test_negation():
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
def test_addition(left, right):
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
def test_subtraction(left, right):
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
def test_multiplication(left, right):
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
def test_division(left, right):
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
def test_floordivision(left, right):
    """Tests that LineItems can be floor-divided against numbers or other LineItems."""
    result = left // right
    assert result(0) == 2.0


def test_logical_and():
    """Tests that LineItems can be logically ANDed."""
    li1 = LineItem(lambda t: True)
    li2 = LineItem(lambda t: True)
    result = li1 & li2
    assert result(0) == True  # pylint: disable=singleton-comparison


def test_logical_or():
    """Tests that LineItems can be logically ORed."""
    li1 = LineItem(lambda t: True)
    li2 = LineItem(lambda t: False)
    result = li1 | li2
    assert result(0) == True  # pylint: disable=singleton-comparison


def test_previous():
    """Tests that LineItems can be used to access the previous value."""
    li = LineItem(lambda t: t)
    result = li.previous()
    assert result(1) == 0


def test_previous_with_offset():
    """Tests that LineItems can be used to access the previous value with an offset."""
    li = LineItem(lambda t: t)
    result = li.previous(2)
    assert result(1) == -1
