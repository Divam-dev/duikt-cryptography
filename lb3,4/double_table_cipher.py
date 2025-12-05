def create_square(key):
    key = key.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []

    for ch in key:
        if ch not in table and ch in alphabet:
            table.append(ch)

    for ch in alphabet:
        if ch not in table:
            table.append(ch)

    square = [table[i*5:(i+1)*5] for i in range(5)]
    return square


def print_square(name, square):
    print(f"{name}:")
    for row in square:
        print(" ".join(row))
    print()


def find_position(square, letter):
    for r in range(5):
        for c in range(5):
            if square[r][c] == letter:
                return r, c
    return None


def double_table_encrypt(text, key1, key2):
    text = text.upper()
    if len(text) % 2 == 1:
        text += "X"

    t1 = create_square(key1)
    t2 = create_square(key2)

    print_square("Table 1", t1)
    print_square("Table 2", t2)

    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    print("Bigrams:", pairs)

    encrypted = ""

    for pair in pairs:
        a, b = pair

        r1, c1 = find_position(t1, a)
        r2, c2 = find_position(t2, b)

        encrypted += t1[r1][c2]
        encrypted += t2[r2][c1]

    print("Encrypted text:", encrypted)
    return encrypted


double_table_encrypt("KRYPTO", "KIBER", "ZAHIST")
