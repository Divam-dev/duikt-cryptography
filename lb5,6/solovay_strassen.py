import random
import math

def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        return 0
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            n_mod8 = n % 8
            if n_mod8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0

def mod_pow(a, d, n):
    return pow(a, d, n)

def is_probable_prime_solovay_strassen(n, k=5):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(k):
        a = random.randint(2, n-1)
        x = jacobi(a, n)
        if x == 0:
            print(f"[Solovay-Strassen] a={a}, gcd(a,n)≠1 → {n} складене.")
            return False
        mod = mod_pow(a, (n-1)//2, n)
        x_mod = x % n
        if mod != x_mod:
            print(f"[Solovay-Strassen] Свідок a={a} → число {n} складене.")
            return False
    print(f"[Solovay-Strassen] Після {k} ітерацій: {n} — можливо просте.")
    return True

if __name__ == "__main__":
    tests = [17, 561, 2047]
    for t in tests:
        print("----")
        print("Тест:", t)
        is_probable_prime_solovay_strassen(t, k=6)
