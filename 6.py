import os
import requests
import zipfile
from pathlib import Path
import re
import shutil


def main():
    zipped_filename = "channel.zip"
    unzipped_folder = "channel"

    if not os.path.exists(zipped_filename):
        resp = requests.get(f"http://www.pythonchallenge.com/pc/def/{zipped_filename}")
        with open(zipped_filename, "w") as f:
            f.write(bytes(resp.text, resp.encoding))
        # os.system(f"wget www.pythonchallenge.com/pc/def/{zipped_filename}")

    archive = zipfile.ZipFile(zipped_filename, "r")

    if not os.path.exists(unzipped_folder):
        archive.extractall(unzipped_folder)

    pattern = r"nothing is (\d+)"
    nothing = "90052"
    comments = ""
    while True:
        next_filepath = f"{unzipped_folder}/{nothing}.txt"
        next_file = Path(next_filepath).open("r").read()
        # print(next_filepath, " : ", next_file)

        comment = archive.getinfo(f"{nothing}.txt").comment.decode("ascii")
        comments += comment

        match = re.search(pattern, next_file)
        if match:
            nothing = match.group(1)
        else:
            break

    os.remove(zipped_filename)
    shutil.rmtree(unzipped_folder)

    print(comments)


if __name__ == "__main__":
    main()
