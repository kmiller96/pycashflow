"""Defines commonly used types throughout the codebase."""

from __future__ import annotations

import typing
from datetime import datetime, date

if typing.TYPE_CHECKING:
    from pycashflow.lineitem import LineItem

LineItemCallableReturn = typing.Union[float, int, bool, str, None]
LineItemCallable = typing.Callable[[int], LineItemCallableReturn]
LineItemOperand = typing.Union["LineItem", typing.Any]

DateLike = typing.Union[str, datetime, date]
