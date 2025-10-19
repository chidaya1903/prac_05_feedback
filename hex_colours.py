"""Look up hexadecimal colour codes (case-insensitive); blank to quit."""

NAME_TO_HEX = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "BEIGE": "#f5f5dc",
    "BLACK": "#000000",
    "BLUEVIOLET": "#8a2be2",
    "BROWN": "#a52a2a",
    "CORNFLOWERBLUE": "#6495ed",
    "CRIMSON": "#dc143c",
    "DARKCYAN": "#008b8b",
}


def main():
    name = input("Colour name: ").strip()
    while name:
        code = NAME_TO_HEX.get(name.replace(" ", "").upper())
        if code:
            print(code)
        else:
            print("Invalid colour name")
        name = input("Colour name: ").strip()


if __name__ == "__main__":
    main()
