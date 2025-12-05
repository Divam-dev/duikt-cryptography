def create_playfair_square(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []

    for ch in key:
        if ch not in table and ch in alphabet:
            table.append(ch)

    for ch in alphabet:
        if ch not in table:
            table.append(ch)

    square = [table[i*5:(i+1)*5] for i in range(5)]
    return square


def print_square(square):
    print("Playfair Square:")
    for row in square:
        print(" ".join(row))
    print()


def find_position(square, letter):
    for r in range(5):
        for c in range(5):
            if square[r][c] == letter:
                return r, c
    return None


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"

        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    return pairs


def playfair_encrypt(text, key):
    square = create_playfair_square(key)
    print_square(square)

    pairs = prepare_text(text)
    print("Bigrams:", pairs)

    encrypted = ""

    for a, b in pairs:
        r1, c1 = find_position(square, a)
        r2, c2 = find_position(square, b)

        if r1 == r2: 
            encrypted += square[r1][(c1 + 1) % 5]
            encrypted += square[r2][(c2 + 1) % 5]

        elif c1 == c2: 
            encrypted += square[(r1 + 1) % 5][c1]
            encrypted += square[(r2 + 1) % 5][c2]

        else:  
            encrypted += square[r1][c2]
            encrypted += square[r2][c1]

    print("Encrypted text:", encrypted)
    return encrypted


playfair_encrypt("KRYPTO", "MONARCHY")
