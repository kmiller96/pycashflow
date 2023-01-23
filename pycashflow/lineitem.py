import itertools
import functools

from .types import LineItemCallable


class LineItem:
    """Defines a single line item. The building block of your model.

    Args:
        name (str): The name of your line item.
        func (callable): The function which computes your line item at time `t`.
    """

    ID_COUNTER = itertools.count()

    def __init__(self, func: LineItemCallable) -> None:
        self.id = next(self.ID_COUNTER)
        self.func = func

    def __repr__(self):
        return f"<LineItem id='{self.id}'>"

    ###############
    ## Operators ##
    ###############

    @staticmethod
    def __validate_arithmatic_operand(f):
        """Validates that the item passed in is of a valid type."""

        @functools.wraps(f)
        def _wrapper(self, other):
            if not isinstance(other, self.__class__):
                raise TypeError("Can only perform arithmatic on LineItems.")

        return _wrapper

    def negate(self) -> "LineItem":
        """Negates a line item, making positives into negatives and vice versa."""
        return LineItem(lambda t: -self.func(t))

    __neg__ = negate

    @__validate_arithmatic_operand
    def add(self, other: "LineItem") -> "LineItem":
        """Adds two line items."""
        return LineItem(lambda t: self.func(t) + other.func(t))

    __add__ = add
    __radd__ = add

    @__validate_arithmatic_operand
    def sub(self, other: "LineItem") -> "LineItem":
        """Subtracts two line items."""
        return self.add(-other)

    __sub__ = sub
    __rsub__ = sub

    @__validate_arithmatic_operand
    def mul(self, other: "LineItem") -> "LineItem":
        """Multiplies two line items."""
        return LineItem(lambda t: self.func(t) * other.func(t))

    __mul__ = mul
    __rmul__ = mul

    @__validate_arithmatic_operand
    def div(self, other: "LineItem") -> "LineItem":
        """Divides two line items."""
        return LineItem(lambda t: self.func(t) / other.func(t))

    __div__ = mul
    __rdiv__ = mul

    @__validate_arithmatic_operand
    def floordiv(self, other: "LineItem") -> "LineItem":
        """Floor-divides two line items."""
        return LineItem(lambda t: self.func(t) // other.func(t))

    __floordiv__ = floordiv
    __rfloordiv__ = floordiv

    @__validate_arithmatic_operand
    def pow(self, other: "LineItem") -> "LineItem":
        """Raises a line item to another line item."""
        return LineItem(lambda t: self.func(t) ** other.func(t))

    __pow__ = pow
    __rpow__ = pow
