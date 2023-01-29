"""Defines the financial model class."""

import logging

import pandas as pd

from pycashflow.lineitem import LineItem

LOGGER = logging.getLogger(__name__)


class FinancialModel:
    """Defines a financial model that you wish to construct.

    Args:
        name (str): The model's name. Used for filenames, titles, etc.
    """

    def __init__(self, name: str) -> None:
        self.name = name

        self.items = {}

    def __getitem__(self, key: str) -> LineItem:
        """Returns the line item with the specified name."""
        return self.items[key]

    def __setitem__(self, key: str, item: LineItem) -> None:
        """Adds a line item to the model."""
        self.items[key] = item

    def run(self, steps: int) -> pd.DataFrame:
        """Simulates the financial model for the supplied number of steps.

        Args:
            steps (int): The number of steps to simulate.

        Returns:
            pd.DataFrame: A DataFrame containing the results of the simulation.
        """

        data = []

        for n in range(steps):
            data.append({k: v(n) for k, v in self.items.items()})

        df = pd.DataFrame(data)
        df.index = pd.RangeIndex(0, steps)
        df.index.name = "step"

        return df
