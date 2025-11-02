"""CP1404 Prac 6 - ProgrammingLanguage class."""

from __future__ import annotations


class ProgrammingLanguage:
    """
    Represent a programming language with typing style, reflection support and first-appeared year.
    """

    def __init__(self, name: str, typing: str, reflection: bool, year: int) -> None:
        self.name = name
        self.typing = typing  # "Dynamic" or "Static"
        self.reflection = reflection
        self.year = int(year)

    def __str__(self) -> str:
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")

    def is_dynamic(self) -> bool:
        """Return True if this language is dynamically typed."""
        return self.typing.strip().lower() == "dynamic"
