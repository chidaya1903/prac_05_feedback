"""State name lookup  case-insensitive input, neat listing."""

SHORT_TO_FULL = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}


def main():
    # Neatly list all abbreviations and names
    for abbr in sorted(SHORT_TO_FULL):
        print(f"{abbr:<3} is {SHORT_TO_FULL[abbr]}")

    # Lookups (case-insensitive), EAFP approach
    state_code = input("Enter short state: ").strip()
    while state_code:
        try:
            print(SHORT_TO_FULL[state_code.upper()])
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").strip()


if __name__ == "__main__":
    main()
