def freundberg_encrypt(plaintext, sub_table, gamma):
    alphabet = 'ABCDEFG' 
    cipher_table = list(sub_table)  # Початкова таблиця, напр. 'DXTVNSW'
    result = ''
    for i, char in enumerate(plaintext):
        if char in alphabet:
            idx = alphabet.index(char)
            cipher_char = cipher_table[idx]
            result += cipher_char
            # Перестановка: ротація вліво на gamma[i]
            shift = gamma[i] % len(alphabet)
            cipher_table = cipher_table[shift:] + cipher_table[:shift]
    return result

def freundberg_decrypt(ciphertext, sub_table, gamma):
    alphabet = 'ABCDEFG'
    cipher_table = list(sub_table)
    result = ''
    for i, char in enumerate(ciphertext):
        if char in cipher_table:
            idx = cipher_table.index(char)
            plain_char = alphabet[idx]
            result += plain_char
            shift = gamma[i] % len(alphabet)
            cipher_table = cipher_table[shift:] + cipher_table[:shift]
    return result

# Приклад
sub_table = 'DXTVNSW'
gamma = [4, 0, 3, 6, 3, 1, 2]
plaintext = 'CGE DAGG'
cipher = freundberg_encrypt(plaintext.replace(' ', ''), sub_table, gamma)
print(cipher) 
print(freundberg_decrypt(cipher, sub_table, gamma)) 