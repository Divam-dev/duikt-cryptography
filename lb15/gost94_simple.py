import hashlib, random

def H_int_gost_like(msg):
    return int(hashlib.sha256(msg).hexdigest(), 16)

p = 467
q = 233
a = 2
x = random.randrange(1, q)
y = pow(a, x, p)

def sign(msg):
    hm = H_int_gost_like(msg) % q
    while True:
        k = random.randrange(1, q)
        r = pow(a, k, p) % q
        if r == 0: continue
        s = (k * (hm + x * r)) % q
        if s != 0:
            return (r, s)

def verify(msg, sig):
    r, s = sig
    if not (0 < r < q and 0 < s < q): return False
    hm = H_int_gost_like(msg) % q
    v = pow(a, hm, p)
    left = pow(y, r, p) * pow(r, s, p) % p
    return v % p == left % p
