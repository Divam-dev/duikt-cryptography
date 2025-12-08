def generate_gamma(key, length):
    gamma = []
    i = 0
    while len(gamma) < length:
        gamma.append(ord(key[i % len(key)]))
        i += 1
    return bytes(gamma)

def xor_cipher(text, key):
    text_bytes = text.encode('utf-8')
    gamma = generate_gamma(key, len(text_bytes))
    cipher_bytes = bytes(a ^ b for a, b in zip(text_bytes, gamma))
    return cipher_bytes.hex()

def xor_decipher(cipher_hex, key):
    cipher_bytes = bytes.fromhex(cipher_hex)
    gamma = generate_gamma(key, len(cipher_bytes))
    text_bytes = bytes(a ^ b for a, b in zip(cipher_bytes, gamma))
    return text_bytes.decode('utf-8')

# Приклад
cipher = xor_cipher("HELLO", "KEY")
print(cipher) 
print(xor_decipher(cipher, "KEY"))  