from math import ceil


def transposition_cipher_encryption(plaintext: str, key: str):
    columns_count = len(key)
    rows_count = ceil((len(plaintext) - plaintext.count(" ")) / columns_count)
    matrix = [["" for _ in range(columns_count)] for _ in range(rows_count)]
    plaintext_index = 0
    for i in range(rows_count):
        for j in range(columns_count):
            matrix[i][j] = plaintext[plaintext_index]
            plaintext_index += 1
            if plaintext_index >= len(plaintext):
                break
            while plaintext[plaintext_index] == " ":
                plaintext_index += 1
    cipher = ""
    columns = determine_columns_sequence(key)
    for i in range(columns_count):
        for j in range(rows_count):
            cipher += matrix[j][columns[i]]
    return cipher


def transposition_cipher_decryption(cipher: str, key: str):
    plaintext = ""
    columns_count = len(key)
    columns = determine_columns_sequence(key)
    rows_count = ceil(len(cipher) / columns_count)
    matrix = [["" for _ in range(columns_count)] for _ in range(rows_count)]
    missing_characters = rows_count * columns_count - len(cipher)
    for i in range(-1, -1 * missing_characters - 1, -1):
        matrix[-1][i] = "*"
    cipher_index = 0
    for i in range(columns_count):
        for j in range(rows_count):
            if cipher_index == len(cipher):
                break
            if matrix[j][columns[i]] == "*":
                continue
            matrix[j][columns[i]] = cipher[cipher_index]
            cipher_index += 1
    for i in range(rows_count):
        for j in range(columns_count):
            if matrix[i][j] == "*":
                break
            plaintext += matrix[i][j]
    return plaintext


def determine_columns_sequence(key: str) -> list[int]:
    columns = []
    sorted_key = list(key)
    sorted_key.sort()
    for letter in sorted_key:
        columns.append(key.index(letter))
    return columns


assert (
    transposition_cipher_encryption("This is some text for testing", "KEY")
    == "hiottrsnTssexoeiismefttg"
)
assert (
    transposition_cipher_decryption("hiottrsnTssexoeiismefttg", "KEY")
    == "Thisissometextfortesting"
)
