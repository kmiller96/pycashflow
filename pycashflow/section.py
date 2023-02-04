"""Defines a new section in a model."""

from typing import Optional

from .types_ import LineItemCallable
from .lineitem import LineItem


class Section:
    """Defines a new section in a model."""

    def __init__(self, name: str) -> None:
        self.name = name

        self.items: dict[str, LineItem] = {}
        self._section_output: Optional[LineItem] = None

    def __getitem__(self, key: str) -> LineItem:
        """Returns the line item with the specified name."""
        return self.items[key]

    def __setitem__(self, key: str, item: LineItem) -> None:
        """Adds a line item to the model."""
        self.items[key] = item

    def __call__(self, t: int) -> LineItem:
        """Returns the output of the section for the specified time step."""
        if self.output is None:
            raise ValueError("No output defined for section.")

        line = self.output
        return line(t)

    @property
    def output(self) -> Optional[LineItem]:
        """Returns the primary output of the section."""
        return self._section_output

    @output.setter
    def output(self, item: LineItem) -> None:
        """Sets the primary output of the section."""
        self._section_output = item

    def line(self, name: str, func: LineItemCallable) -> LineItem:
        """Creates a new line item in the section & returns it to the user.

        This is shorthand syntax for:

        >>> section = Section("section")
        >>> section["line"] = LineItem(func)
        >>> section["line"]

        Args:
            name (str): The name of the line item.
            func (callable): The function that will be used to calculate the
                value of the line item.

        Returns:
            LineItem: The newly created line item.
        """
        self[name] = LineItem(func)
        return self[name]
