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

from pycashflow import FinancialModel, LineItem

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
def model(r1, r2, e1, e2) -> FinancialModel:
    """Defines the financial model outlined in the module docstring."""
    model = FinancialModel("simple")

    model["revenue_1"] = LineItem(r1)
    model["revenue_2"] = LineItem(r2)
    model["expense_1"] = LineItem(e1)
    model["expense_2"] = LineItem(e2)

    model["profit"] = (
        model["revenue_1"]
        + model["revenue_2"]
        - model["expense_1"]
        - model["expense_2"]
    )

    return model


###########
## Tests ##
###########


def test_model_correct_at_each_step(model: FinancialModel, profit: Callable):
    """Asserts that the model matches the explicitly defined profit function."""
    for t in range(1, 13):
        assert model["profit"](t) == profit(t)


def test_model_can_return_dataframe(model: FinancialModel):
    """Asserts that the model can return a DataFrame."""
    results = model.run(steps=12)

    assert isinstance(results, pd.DataFrame)
    assert_index_equal(results.index, pd.RangeIndex(0, 12, name="step"))
    assert set(results.columns) == {
        "revenue_1",
        "revenue_2",
        "expense_1",
        "expense_2",
        "profit",
    }
