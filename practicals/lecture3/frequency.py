"""Count ASCII vowels case-insensitively in a UTF-8 text file."""
from collections import Counter
from pathlib import Path
import json
import sys

def count_vowels(file_path):
    counts = Counter(Path(file_path).read_text(encoding="utf-8").lower())
    return {vowel: counts[vowel] for vowel in "aeiou"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: frequency.py FILE", file=sys.stderr)
        sys.exit(2)
    try:
        print(json.dumps(count_vowels(sys.argv[1]), sort_keys=True))
    except (OSError, UnicodeError) as error:
        print(f"Cannot read input: {error}", file=sys.stderr)
        sys.exit(1)
