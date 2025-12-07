def affine_encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            p = ord(char) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
    return result

def affine_decrypt(cipher, a, b):
    a_inv = pow(a, -1, 26)  # Обернене a mod 26
    result = ""
    for char in cipher.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            p = (a_inv * (c - b)) % 26
            result += chr(p + ord('A'))
    return result

# Приклад
print(affine_encrypt("HELLO", 5, 8))  
print(affine_decrypt("RCLLA", 5, 8))  