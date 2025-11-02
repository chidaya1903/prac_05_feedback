"""CP1404 Prac 6 - Guitar class."""

from __future__ import annotations
from datetime import date

VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar with name, year and cost."""

    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0) -> None:
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self) -> int:
        """Return age in whole years."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self) -> bool:
        """Return True if the guitar is considered vintage."""
        return self.get_age() >= VINTAGE_AGE
