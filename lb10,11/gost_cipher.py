# Simple GOST implementation (requires S-boxes; use standard ones)
S_BOX = [
    [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
    [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
    [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
    [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
    [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
    [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
    [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
    [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12],
]

def gost_round(left, right, key_word):
    temp = (right + key_word) % (1 << 32)
    s_out = 0
    for i in range(8):
        nibble = (temp >> (4 * i)) & 0xF
        s_out |= S_BOX[i][nibble] << (4 * i)
    s_out = ((s_out << 11) | (s_out >> 21)) & 0xFFFFFFFF
    return right, left ^ s_out

def gost_encrypt(block, key):
    left = (block >> 32) & 0xFFFFFFFF
    right = block & 0xFFFFFFFF
    keys = [int.from_bytes(key[i:i+4], 'big') for i in range(0, 32, 4)] * 3 + keys[::-1]
    for k in keys:
        left, right = gost_round(left, right, k)
    return (right << 32) | left

# Приклад
key = bytes.fromhex('FEDCBA9876543210' * 4) 
plaintext = 0x0123456789ABCDEF
cipher = gost_encrypt(plaintext, key)
print(hex(cipher))