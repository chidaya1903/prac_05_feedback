"""
Wimbledon champions and countries
Estimate: 35 minutes
Actual:   __ minutes
"""

from collections import defaultdict
import csv

FILENAME = "wimbledon.csv"


def main():
    rows = load_rows(FILENAME)  # list[dict]
    champion_to_wins = count_champions(rows)
    countries = extract_countries(rows)

    print("Wimbledon Champions:")
    for champion in sorted(champion_to_wins):
        print(f"{champion} {champion_to_wins[champion]}")

    country_list = sorted(countries)
    print(f"\nThese {len(country_list)} countries have won Wimbledon:")
    print(", ".join(country_list))


def load_rows(filename: str) -> list[dict]:
    """Return list of dict rows from CSV. Handles BOM via utf-8-sig."""
    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def count_champions(rows: list[dict]) -> dict[str, int]:
    """Return dict champion->win_count from CSV rows."""
    wins = defaultdict(int)
    # Try to pick robustly (header names vary slightly across datasets)
    name_key = _first_present_key(rows, ["Champion", "Winner", "Name"])
    for row in rows:
        champion = row[name_key].strip()
        wins[champion] += 1
    return dict(wins)


def extract_countries(rows: list[dict]) -> set[str]:
    """Return set of champion countries/abbreviations from CSV rows."""
    countries = set()
    country_key = _first_present_key(rows, ["Country", "Nationality", "Country of Winner"])
    for row in rows:
        countries.add(row[country_key].strip())
    return countries


def _first_present_key(rows: list[dict], candidates: list[str]) -> str:
    """Return the first key from candidates that exists in the CSV header."""
    header = rows[0].keys() if rows else []
    for k in candidates:
        if k in header:
            return k
    raise KeyError("Expected header not found; check CSV column names.")


if __name__ == "__main__":
    main()
