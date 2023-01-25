"""Defines commonly used types throughout the codebase."""

from __future__ import annotations

import typing
from datetime import datetime, date

if typing.TYPE_CHECKING:
    from pycashflow.lineitem import LineItem

LineItemCallable = typing.Callable[[int], float]
LineItemOperand = typing.Union["LineItem", float, int]

DateLike = typing.Union[str, datetime, date]
