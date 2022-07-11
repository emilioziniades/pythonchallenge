from pathlib import Path
from collections import Counter


def main():
    mess = Path("2.txt").open("r").read()
    freq = Counter(mess)
    result = "".join(l for l, c in freq.items() if c == 1)
    print(result)


if __name__ == "__main__":
    main()
