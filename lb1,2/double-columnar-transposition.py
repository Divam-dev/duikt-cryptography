def double_transposition(text, row_key, col_key, rows, cols):
    print("\n=== Крок 1. Формуємо таблицю ===")
    table = [[''] * cols for _ in range(rows)]
    k = 0

    for i in range(rows):
        for j in range(cols):
            table[i][j] = text[k] if k < len(text) else 'х'
            k += 1

    for row in table:
        print(row)

    print("\n=== Крок 2. Переставляємо рядки ===")
    table = [table[i - 1] for i in row_key]
    for row in table:
        print(row)

    print("\n=== Крок 3. Переставляємо стовпці ===")
    new_table = []
    for r in table:
        new_row = [r[j - 1] for j in col_key]
        new_table.append(new_row)

    for row in new_table:
        print(row)

    print("\n=== Крок 4. Зчитуємо по стовпцях ===")
    result = ''
    for j in range(cols):
        for i in range(rows):
            result += new_table[i][j]
            print(f"Додаємо: {new_table[i][j]}  →  {result}")

    print("\nРЕЗУЛЬТАТ:", result)
    return result


double_transposition("крипт", [2, 1], [3, 1, 2], 2, 3)
