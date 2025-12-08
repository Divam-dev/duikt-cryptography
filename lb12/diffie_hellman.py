def mod_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def diffie_hellman(p, g, a, b):
    A = mod_pow(g, a, p)  
    B = mod_pow(g, b, p)  
    S_alice = mod_pow(B, a, p)
    S_bob = mod_pow(A, b, p)
    return A, B, S_alice, S_bob

p, g = 23, 5
a, b = 6, 15  
A, B, S_a, S_b = diffie_hellman(p, g, a, b)
print(f"A={A}, B={B}, S_Alice={S_a}, S_Bob={S_b}")  