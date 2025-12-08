def mod_pow(base, exp, mod):  
    return pow(base, exp, mod)  

def ffs_prove(public_v, secrets_s, N, r):  
    x = mod_pow(r, 2, N)  
    return x  

def ffs_challenge(k):  
    import random  
    return [random.randint(0, 1) for _ in range(k)]  

def ffs_response(a, r, secrets_s, N):  
    prod = 1  
    for i, ai in enumerate(a):  
        prod = (prod * mod_pow(secrets_s[i], ai, N)) % N  
    y = (r * prod) % N  
    return y  

def ffs_verify(a, x, y, public_v, N):  
    left = mod_pow(y, 2, N)  
    prod_v = 1  
    for i, ai in enumerate(a):  
        prod_v = (prod_v * mod_pow(public_v[i], ai, N)) % N  
    right = (x * prod_v) % N  
    return left == right  

# Приклад використання  
N = 2323 
public_v = [25, 49, 9] 
secrets_s = [5, 7, 3]  
k = 3  
r = 13  
x = ffs_prove(public_v, secrets_s, N, r)  
print(f'x = {x}')  
a = [1, 0, 1] 
y = ffs_response(a, r, secrets_s, N)  
print(f'y = {y}') 
verified = ffs_verify(a, x, y, public_v, N)  
print(f'Перевірка: {verified}') 