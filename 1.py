from string import ascii_lowercase as alphabet

ciphertext = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""


def main():
    plaintext = rot_2(ciphertext)
    print(plaintext)
    print(rot_2("map"))


def rot_2(text):
    return "".join(alphabet[(ord(c) - 97 + 2) % 26] if c.isalpha() else c for c in text)


def better_method():
    alphabet_2 = alphabet[2:] + alphabet[:2]
    trans = ciphertext.maketrans(alphabet, alphabet_2)
    plaintext = ciphertext.translate(trans)
    print(plaintext)


if __name__ == "__main__":
    main()
