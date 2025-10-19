"""
Word Occurrences
Estimate: 20 minutes
Actual:   __ minutes
"""

def main():
    text = input("Text: ").strip()
    counts: dict[str, int] = {}

    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1

    # Sorted by word
    words = sorted(counts.keys())
    width = max((len(w) for w in words), default=0)

    for w in words:
        print(f"{w:{width}} : {counts[w]}")


if __name__ == "__main__":
    main()
