"""Defines the financial model class."""

import logging

import pandas as pd

from pycashflow.section import Section

LOGGER = logging.getLogger(__name__)


class Model:
    """Defines a model that you wish to construct.

    This serves as the main interface into the package. Think of it as the
    "app" that you would define in a flask app, or the "main" function in a
    C++ program.

    From here the user can create new sections, pages, etc.

    Args:
        name (str): The model's name. Used for filenames, titles, etc.
    """

    def __init__(self, name: str) -> None:
        self.name = name

        self.sections: dict[str, Section] = {}

    def __getitem__(self, key: str) -> Section:
        """Returns the section of the model with the specified name."""
        return self.sections[key]

    def __setitem__(self, key: str, item: Section) -> None:
        """Adds a section to the model."""
        self.sections[key] = item

    def section(self, name: str) -> Section:
        """Creates a new section in the model.

        This is shorthand syntax for:

        >>> model = Model("model")
        >>> model["section"] = Section("section")
        >>> model["section"]

        Args:
            name (str): The name of the section.

        Returns:
            Section: The newly created section.
        """
        self[name] = Section(name)
        return self[name]

    def run(self, steps: int) -> pd.DataFrame:
        """Simulates the financial model for the supplied number of steps.

        Args:
            steps (int): The number of steps to simulate.

        Returns:
            pd.DataFrame: A DataFrame containing the results of the simulation.
        """

        data = []

        for n in range(steps):
            row = {"step": n}

            for name, section in self.sections.items():
                row[name] = section.output

                for k, v in section.items.items():
                    row[f"{name}_{k}"] = v

            data.append(row)

        df = pd.DataFrame(data)
        df = df.set_index("step")

        return df
