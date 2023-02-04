"""Defines commonly used types throughout the codebase."""

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Callable, Any
from datetime import datetime, date

if TYPE_CHECKING:
    from pycashflow.lineitem import LineItem

LineItemCallableReturn = Union[float, int, bool, str, None]
LineItemCallable = Union[
    Callable[[int], LineItemCallableReturn],
    Callable[[int, "LineItem"], LineItemCallableReturn],
]
LineItemOperand = Union["LineItem", Any]

DateLike = Union[str, datetime, date]
