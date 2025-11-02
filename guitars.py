"""CP1404 Prac 6 - Using the Guitar class (collect then display)."""

from guitar import Guitar


def main() -> None:
    print("My guitars!")
    guitars = []

    # Input phase
    name = input("Name: ").strip()
    while name:
        year = get_int("Year: ", minimum=0)
        cost = get_float("Cost: $", minimum=0)
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ").strip()

    # Display phase
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_tag}")


def get_int(prompt: str, minimum: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Value must be >= {minimum}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")


def get_float(prompt: str, minimum: float | None = None) -> float:
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Value must be >= {minimum}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()
