def mod_pow(base, exp, mod):  
    return pow(base, exp, mod)  

def gq_prove(r, v, n, private_B):  
    T = mod_pow(r, v, n)  
    return T  

def gq_challenge(v):  
    import random  
    return random.randint(0, v-1)  

def gq_response(d, r, private_B, n):  
    D = (r * mod_pow(private_B, d, n)) % n  
    return D  

def gq_verify(d, T, D, public_J, v, n):  
    left = (mod_pow(D, v, n) * mod_pow(public_J, d, n)) % n  
    return left == T  

# Приклад використання  
n = 15  
v = 2  
public_J = 4  
private_B = 2 
r = 3  
T = gq_prove(r, v, n, private_B)  
print(f'T = {T}')  
d = 1  
D = gq_response(d, r, private_B, n)  
print(f'D = {D}')  
verified = gq_verify(d, T, D, public_J, v, n)  
print(f'Перевірка: {verified}')  