import hashlib, random, math

def H_int(msg):
    return int(hashlib.sha1(msg).hexdigest(), 16)  

def modinv(a, m):
    return pow(a, -1, m)

p = 467
q = 233 
g = 2
x = random.randrange(1, q)
y = pow(g, x, p)

def sign(message):
    hm = H_int(message) % q
    while True:
        k = random.randrange(1, q)
        r = pow(g, k, p) % q
        if r == 0: continue
        k_inv = modinv(k, q)
        s = (k_inv * (hm + x * r)) % q
        if s != 0:
            return (r, s)

def verify(message, sig):
    r, s = sig
    if not (0 < r < q and 0 < s < q):
        return False
    hm = H_int(message) % q
    w = modinv(s, q)
    u1 = (hm * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q
    return v == r

# demo
if __name__ == "__main__":
    msg = b"Test DSA"
    sig = sign(msg)
    print("sig:", sig, "verify:", verify(msg, sig))
