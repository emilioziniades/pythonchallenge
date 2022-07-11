import requests
import zipfile
import re
import io


def main():
    resp = requests.get(f"http://www.pythonchallenge.com/pc/def/channel.zip")
    zip_data = io.BytesIO(resp.content)

    pattern = r"nothing is (\d+)"
    nothing = "90052"
    comments = ""
    with zipfile.ZipFile(zip_data, "r") as archive:
        while True:
            next_file = f"{nothing}.txt"
            with archive.open(next_file) as f:
                comment = archive.getinfo(next_file).comment.decode("ascii")
                comments += comment

                contents = f.read().decode("ascii")
                match = re.search(pattern, contents)
                if match:
                    nothing = match.group(1)
                else:
                    break

    print(comments)


if __name__ == "__main__":
    main()
