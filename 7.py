from PIL import Image
import re


def main():
    image = Image.open("7.png")
    width, height = image.size
    row_n = 0
    for i in range(height):
        r, g, b, _ = image.getpixel((0, i))
        if r == g == b:
            row_n = i
            break

    grays = []
    for i in range(0, width, 7):
        r, g, b, _ = image.getpixel((i, row_n))
        if r != g != b:
            break
        grays.append(r)

    message = "".join(chr(i) for i in grays)
    lst = re.search(r"\[.*\]", message).group(0)
    lst = eval(lst)
    print("".join(map(chr, lst)))


if __name__ == "__main__":
    main()
