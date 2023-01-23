"""Defines commonly used types throughout the codebase."""

import typing
from datetime import datetime, date

LineItemCallable = typing.Callable[[int], float]
DateLike = typing.Union[str, datetime, date]
