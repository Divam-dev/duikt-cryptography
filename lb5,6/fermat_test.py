import random

def mod_pow(a, d, n):
    return pow(a, d, n)

def is_probable_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    # випадкові бази
    for i in range(k):
        a = random.randrange(2, n - 1)
        if mod_pow(a, n - 1, n) != 1:
            print(f"[Fermat] Свідок a={a} → число {n} складене.")
            return False
    print(f"[Fermat] Після {k} ітерацій: {n} — можливо просте.")
    return True

if __name__ == "__main__":
    tests = [17, 561, 2047]
    for t in tests:
        print("----")
        print("Тест:", t)
        is_probable_prime_fermat(t, k=6)
