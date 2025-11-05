import string
from os import getcwd


def atbash(plaintext: str) -> str:
    cipher = ""
    cipher_alphabet = (
        f"{string.ascii_uppercase}{string.ascii_lowercase}{string.digits} "
    )
    alphabet_length = len(cipher_alphabet)
    for character in plaintext:
        if cipher_alphabet.__contains__(character):
            index = cipher_alphabet.index(character)
            cipher += cipher_alphabet[alphabet_length - index - 1]
    return cipher


assert atbash("A") == " "
assert atbash(" ") == "A"

assert atbash("2137") == "IJHD"
assert atbash("Lovecraft") == "zWPgiTkfR"

assert atbash("Lorem ipsum dolor sit amet") == "zWTgYAcVSQYAhWZWTAScRAkYgR"
assert atbash("zWTgYAcVSQYAhWZWTAScRAkYgR") == "Lorem ipsum dolor sit amet"


def atbash_cli():
    file_path = input("Enter input file path\n")
    if not file_path.startswith(("~", "/")):
        file_path = f"{getcwd()}/{file_path}"
    print(file_path)
    file_content = open(file_path).read()
    output = atbash(file_content)
    print(output)


atbash_cli()
