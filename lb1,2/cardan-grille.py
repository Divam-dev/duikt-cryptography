def rotate(grille):
    return [list(row) for row in zip(*grille[::-1])]

def print_table(table):
    for row in table:
        print(row)

def grille_cipher(text, grille, n):
    table = [['.'] * n for _ in range(n)]
    k = 0

    for turn in range(4):
        print(f"\n=== Поворот {turn * 90}° ===")
        print("Поточний трафарет:")
        print_table(grille)

        for i in range(n):
            for j in range(n):
                if grille[i][j] == 'X':
                    char = text[k] if k < len(text) else 'х'
                    print(f"Записуємо '{char}' у позицію ({i},{j})")
                    table[i][j] = char
                    k += 1

        print("\nТаблиця після заповнення:")
        print_table(table)

        grille = rotate(grille)

    print("\n=== Фінальний результат ===")
    print_table(table)

    result = ''.join(''.join(r) for r in table)
    print("\nКриптограма:", result)
    return result


grille = [
    ['X','.','.','.'],
    ['.','.','X','.'],
    ['.','X','.','.'],
    ['.','.','.','X']
]

grille_cipher("крипт", grille, 4)
