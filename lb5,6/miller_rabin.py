import random

def mod_pow(a, d, n):
    return pow(a, d, n)

def is_probable_prime_miller_rabin(n, k=6, verbose=True):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    if verbose:
        print(f"n-1 = 2^{s} * {d}")

    for i in range(k):
        a = random.randrange(2, n - 1)
        x = mod_pow(a, d, n)
        if verbose:
            print(f"Ітерація {i+1}, a={a}, x = a^d mod n = {x}")
        if x == 1 or x == n - 1:
            if verbose:
                print("Проходить для цієї бази (x=1 або x=n-1).")
            continue
        composite = True
        for r in range(s - 1):
            x = (x * x) % n
            if verbose:
                print(f"  Квадрат {r+1}: x = {x}")
            if x == n - 1:
                composite = False
                if verbose:
                    print("  Знайдено x == n-1 → проходить.")
                break
        if composite:
            print(f"[Miller-Rabin] Свідок a={a} → число {n} складене.")
            return False
    print(f"[Miller-Rabin] Після {k} ітерацій: {n} — можливо просте.")
    return True

if __name__ == "__main__":
    tests = [17, 561, 2047, 8911]
    for t in tests:
        print("----")
        print("Тест:", t)
        is_probable_prime_miller_rabin(t, k=6, verbose=True)
