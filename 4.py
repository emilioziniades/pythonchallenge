import requests
import re


def main():
    nothing = "12345"
    url_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    pattern = r"and the next nothing is (\d*)"

    while True:
        url = url_base + nothing
        resp = requests.get(url)
        print(resp.text)
        if match := re.search(pattern, resp.text):
            nothing = match.group(1)
        elif match := re.search(r".*\.html", resp.text):
            break
        else:
            nothing = str(int(nothing) // 2)


if __name__ == "__main__":
    main()
