"""Generates a simple financial model and asserts the outputs match.

The scenario we are modelling is defined as follows:

1. The first revenue line item is a constant $1000 per month.
2. The second revenue line item starts at $100 per month and increases by $10 each month.
3. The first expense line item is a constant $500 per month.
4. The second expense line item starts at $50 per month and increases by $5 each month.

Our testing will model that our profits match our expectations.
"""

# pylint: disable=redefined-outer-name,unnecessary-lambda-assignment,missing-function-docstring

from typing import Callable

import pytest
import pandas as pd
from pandas.testing import assert_index_equal

from pycashflow import Model, LineItem

##############
## Fixtures ##
##############


@pytest.fixture
def r1():
    return lambda t: 1000


@pytest.fixture
def r2():
    return lambda t: 100 + 10 * t


@pytest.fixture
def e1():
    return lambda t: 500


@pytest.fixture
def e2():
    return lambda t: 50 + 5 * t


@pytest.fixture
def profit(r1, r2, e1, e2):
    """An explicitly defined profit function to use when testing."""
    return lambda t: r1(t) + r2(t) - e1(t) - e2(t)


@pytest.fixture
def model(r1, r2, e1, e2) -> Model:
    """Defines the financial model outlined in the module docstring."""
    model = Model("simple")

    revenue = model.section("revenue")
    revenue["1"] = LineItem(r1)
    revenue["2"] = LineItem(r2)
    revenue.output = revenue["1"] + revenue["2"]

    expenses = model.section("expenses")
    expenses["1"] = LineItem(e1)
    expenses["2"] = LineItem(e2)
    expenses.output = expenses["1"] + expenses["2"]

    profit = model.section("profit")
    profit.output = revenue.output - expenses.output

    return model


###########
## Tests ##
###########


def test_model_correct_at_each_step(model: Model, profit: Callable):
    """Asserts that the model matches the explicitly defined profit function."""
    for t in range(1, 13):
        assert model["profit"](t) == profit(t)


def test_model_can_return_dataframe(model: Model):
    """Asserts that the model can return a DataFrame."""
    results = model.run(steps=12)

    assert isinstance(results, pd.DataFrame)
    assert_index_equal(results.index, pd.RangeIndex(0, 12, name="step"))
    assert set(results.columns) == {
        "revenue_1",
        "revenue_2",
        "revenue",
        "expenses_1",
        "expenses_2",
        "expenses",
        "profit",
    }
