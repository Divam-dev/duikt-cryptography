from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def des_encrypt(plaintext, key):
    # Key must be 8 bytes (64 bits), plaintext 8 bytes
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return ct.hex()

def des_decrypt(ciphertext, key):
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    pt = decryptor.update(ciphertext) + decryptor.finalize()
    return pt.hex()

key = b'\x13\x34\x57\x79\x9B\xBC\xDF\xF1' 
plaintext = b'\x01\x23\x45\x67\x89\xAB\xCD\xEF'
ciphertext = bytes.fromhex(des_encrypt(plaintext, key))
print(des_encrypt(plaintext, key))  
print(des_decrypt(ciphertext, key)) 