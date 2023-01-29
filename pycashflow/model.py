"""Defines the financial model class."""

import logging

from pycashflow.lineitem import LineItem
from pycashflow.types import DateLike

LOGGER = logging.getLogger(__name__)


class FinancialModel:
    """Defines a financial model that you wish to construct.

    Args:
        name (str): The model's name. Use for filenames, titles, etc.
        step (str): The step size of the model.
    """

    def __init__(self, name: str, step: str = "1D") -> None:
        self.name = name
        self.step = step

        LOGGER.warning(
            "Currently there is no support for the `step` argument. You must "
            "normalise your line items to the same step size manually."
        )

        self.items = {}

    def __getitem__(self, key: str) -> LineItem:
        """Returns the line item with the specified name."""
        return self.items[key]

    def __setitem__(self, key: str, item: LineItem) -> None:
        """Adds a line item to the model."""
        self.items[key] = item

    def run(self, start: DateLike, end: DateLike) -> "FinancialModel":
        """Simulates the financial model within the specified range."""
        # TODO! Try convert everything to datetime.
        print(start, end)
        print(self.items)
        return self
