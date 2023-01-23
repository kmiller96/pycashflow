"""Defines the financial model class."""

from .lineitem import LineItem
from .types import LineItemCallable, DateLike


class FinancialModel:
    """Defines a financial model that you wish to construct.

    Args:
        name (str): The model's name. Use for filenames, titles, etc.
        step (str): The step size of the model.
    """

    def __init__(self, name: str, step: str = "1D") -> None:
        self.name = name
        self.step = step

        self.items = {}

    def run(self, start: DateLike, end: DateLike) -> "FinancialModel":
        """Simulates the financial model within the specified range."""
        # TODO! Try convert everything to datetime.
        print(start, end)
        print(self.items)
        return self
