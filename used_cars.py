"""CP1404 Prac 6 - Using the Car class."""

from car import Car


def main() -> None:
    """Create and manipulate some Car objects."""
    # Existing example car
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(my_car)

    # New car as per instructions
    limo = Car("Limo", 100)     # 1) create with 100 fuel
    limo.add_fuel(20)           # 2) add 20 more
    print(limo.fuel)            # 3) print its fuel

    driven = limo.drive(115)    # 4) attempt to drive 115 km
    print(f"Drove {driven}km")
    print(limo)                 # show final state to confirm fuel/odo


if __name__ == "__main__":
    main()
