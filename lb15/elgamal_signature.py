import hashlib
import random

def H_int(msg):
    return int(hashlib.sha256(msg).hexdigest(), 16)

def modinv(a, m):
    return pow(a, -1, m)

def generate_params_small():
    p = 467
    g = 2
    return p, g

def keygen(p, g):
    x = random.randrange(1, p-1)     
    y = pow(g, x, p)                 
    return x, y

def sign(p, g, x, message):
    hm = H_int(message) % (p-1)     
    while True:
        k = random.randrange(1, p-1)
        if pow(k, 1, p-1) and (math.gcd(k, p-1) == 1):
            break
    r = pow(g, k, p)
    k_inv = modinv(k, p-1)
    s = (k_inv * (hm - x * r)) % (p-1)
    return (r, s)

def verify(p, g, y, message, sig):
    r, s = sig
    if not (0 < r < p): return False
    hm = H_int(message) % (p-1)
    left = pow(g, hm, p)
    right = (pow(y, r, p) * pow(r, s, p)) % p
    return left == right

# Невеликий demo
if __name__ == "__main__":
    import math
    p, g = generate_params_small()
    x, y = keygen(p, g)
    msg = b"Hello, ElGamal!"
    sig = sign(p, g, x, msg)
    print("p,g:", p, g)
    print("priv x:", x)
    print("pub y:", y)
    print("signature (r,s):", sig)
    print("verify:", verify(p, g, y, msg, sig))
