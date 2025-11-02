"""CP1404 Prac 6 - Simple tests for Guitar methods."""

from guitar import Guitar, VINTAGE_AGE


def main() -> None:
    l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    print(f"{l5.name} get_age() - Expected >= 100. Got {l5.get_age()}")
    print(f"{another.name} get_age() - Expected ~{(2025-2013)}. Got {another.get_age()}")

    print(f"{l5.name} is_vintage() - Expected True. Got {l5.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

    # Quick boundary check near VINTAGE_AGE
    boundary = Guitar("Fifty-ish", l5.year + l5.get_age() - VINTAGE_AGE, 1000)
    print(f"{boundary.name} is_vintage() - Expected True. Got {boundary.is_vintage()}")


if __name__ == "__main__":
    main()
