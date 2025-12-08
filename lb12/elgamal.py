def mod_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def mod_inverse(a, m):
    # Розширений Евклід для оберненого
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def elgamal_encrypt(m, p, g, y, k):
    c1 = mod_pow(g, k, p)
    c2 = (m * mod_pow(y, k, p)) % p
    return c1, c2

def elgamal_decrypt(c1, c2, p, x):
    s = mod_pow(c1, x, p)
    s_inv = mod_inverse(s, p)
    m = (c2 * s_inv) % p
    return m


p, g = 23, 5
x = 6  
y = mod_pow(g, x, p)  
m, k = 10, 10
c1, c2 = elgamal_encrypt(m, p, g, y, k)
print(f"c1={c1}, c2={c2}")
dec_m = elgamal_decrypt(c1, c2, p, x)
print(f"Decrypted m={dec_m}")  