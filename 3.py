from pathlib import Path
import re


def main():
    mess = Path("3.txt").open("r").read()
    pattern = r"[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}"
    matches = re.finditer(pattern, mess)
    answer = "".join(m.group(1) for m in matches)
    print(answer)


if __name__ == "__main__":
    main()
