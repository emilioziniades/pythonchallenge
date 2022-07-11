import pickle
import requests


def main():
    resp = requests.get("http://www.pythonchallenge.com/pc/def/banner.p", stream=True)
    banner_raw = bytes(resp.text, resp.encoding)
    banner_pickle = pickle.loads(banner_raw)

    banner = ""
    for row in banner_pickle:
        curr_line = "".join([char * length for char, length in row])
        banner += curr_line + "\n"

    print(banner)


if __name__ == "__main__":
    main()
