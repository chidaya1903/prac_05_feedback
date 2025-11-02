"""CP1404 Prac 6 - Car class."""

from __future__ import annotations


class Car:
    """A simple Car with a name, fuel store and odometer reading."""

    def __init__(self, name: str = "", fuel: int = 0) -> None:
        self.name = name
        self.fuel = max(0, int(fuel))
        self.odometer = 0  # start at 0 km

    def __str__(self) -> str:
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    # Keeping the conventional method name used in CP1404 notes
    def add_fuel(self, amount: int) -> None:
        """Add non-negative fuel units."""
        if amount < 0:
            raise ValueError("Fuel amount must be >= 0")
        self.fuel += amount

    def drive(self, distance: int) -> int:
        """
        Drive up to 'distance' km, limited by available fuel.
        Returns the actual distance driven.
        """
        if distance < 0:
            raise ValueError("Distance must be >= 0")
        distance_driven = min(distance, self.fuel)
        self.fuel -= distance_driven
        self.odometer += distance_driven
        return distance_driven
