"""Defines the LineItem class: the building block of your models."""

import itertools
import logging

from pycashflow.types_ import LineItemCallable, LineItemOperand, LineItemCallableReturn

LOGGER = logging.getLogger(__name__)


class LineItem:
    """Defines a single line item. The building block of your model.

    Args:
        func (callable): The function which computes your line item at time `t`.
    """

    # pylint: disable=unnecessary-lambda-assignment

    ID_COUNTER = itertools.count()

    def __init__(self, func: LineItemCallable) -> None:
        self.id = next(self.ID_COUNTER)
        self._func = func

        LOGGER.debug("Created LineItem %s.", self)

    def __str__(self):
        return f"<LineItem id='{self.id}'>"

    def __repr__(self):
        return str(self)

    def __call__(self, t: int) -> LineItemCallableReturn:
        """Computes the value of the line item at time `t`."""
        return self.func(t)

    ################
    ## Attributes ##
    ################

    @property
    def func(self):
        """Returns the underlying function."""
        return self._func

    @func.setter
    def func(self, f: LineItemCallable):
        """Fails when setting the function, due to the immutability of this attribute.

        We force the function to be immutable to make our lives easier. If we
        allowed this function to change post-initialisation, we'd have to
        maintain pointers everywhere and compute each value "just-in-time". That
        would be a nightmare.

        Instead, we can just inject the `_func` attribute into composed line
        items knowing that they will never change.
        """
        raise AttributeError(
            "Cannot set the function of a LineItem after initialisation."
        )

    #############
    ## Methods ##
    #############

    def previous(self, n: int = 1) -> "LineItem":
        """Returns a line item which returns the value of this line item `n` periods ago.

        Args:
            n (int): The number of periods to look back.

        Returns:
            LineItem: The new line item.
        """
        return LineItem(lambda t: self.func(t - n))

    ###############
    ## Operators ##
    ###############

    def negate(self) -> "LineItem":
        """Negates a line item, making positives into negatives and vice versa."""
        return LineItem(lambda t: -self.func(t))

    def add(self, other: LineItemOperand) -> "LineItem":
        """Adds a line item to another line item or a number."""
        return (
            LineItem(lambda t: self(t) + other(t))
            if isinstance(other, LineItem)
            else LineItem(lambda t: self(t) + other)
        )

    def sub(self, other: LineItemOperand) -> "LineItem":
        """Subtracts a line item from another line item or a number."""
        return (
            LineItem(lambda t: self(t) - other(t))
            if isinstance(other, LineItem)
            else LineItem(lambda t: self(t) - other)
        )

    def mul(self, other: LineItemOperand) -> "LineItem":
        """Multiplies a line item by another line item or a number."""
        return (
            LineItem(lambda t: self(t) * other(t))
            if isinstance(other, LineItem)
            else LineItem(lambda t: self(t) * other)
        )

    def div(self, other: LineItemOperand) -> "LineItem":
        """Divides a line item by another line item or a number."""
        return (
            LineItem(lambda t: self(t) / other(t))
            if isinstance(other, LineItem)
            else LineItem(lambda t: self(t) / other)
        )

    def floordiv(self, other: LineItemOperand) -> "LineItem":
        """Floor-divides a line item by another line item or a number."""
        return (
            LineItem(lambda t: self(t) // other(t))
            if isinstance(other, LineItem)
            else LineItem(lambda t: self(t) // other)
        )

    def pow(self, other: LineItemOperand) -> "LineItem":
        """Raises a line item to the power of another line item or a number."""
        return (
            LineItem(lambda t: self(t) ** other(t))
            if isinstance(other, LineItem)
            else LineItem(lambda t: self(t) ** other)
        )

    def logical_and(self, other: LineItemOperand) -> "LineItem":
        """Logical ANDs a line item with another line item or a number."""
        return (
            LineItem(lambda t: self(t) and other(t))
            if isinstance(other, LineItem)
            else LineItem(lambda t: self(t) and other)
        )

    def logical_or(self, other: LineItemOperand) -> "LineItem":
        """Logical ORs a line item with another line item or a number."""
        return (
            LineItem(lambda t: self(t) or other(t))
            if isinstance(other, LineItem)
            else LineItem(lambda t: self(t) or other)
        )

    ############################
    ## Magic Method Operators ##
    ############################

    __neg__ = negate

    __add__ = add
    __radd__ = add

    __sub__ = sub
    __rsub__ = lambda self, other: -self.sub(other)

    __mul__ = mul
    __rmul__ = mul

    __div__ = div
    __rdiv__ = lambda self, other: (lambda t: other / self(t))

    __truediv__ = div
    __rtruediv__ = lambda self, other: (lambda t: other / self(t))

    __floordiv__ = floordiv
    __rfloordiv__ = lambda self, other: (lambda t: other // self(t))

    __pow__ = pow
    __rpow__ = pow

    __and__ = logical_and
    __rand__ = logical_and

    __or__ = logical_or
    __ror__ = logical_or
