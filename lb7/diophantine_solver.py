def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve_diophantine(a, b, c):
    gcd, x, y = extended_gcd(a, b)
    if c % gcd != 0:
        return None
    x *= c // gcd
    y *= c // gcd
    return x, y, gcd

# Приклад використання для 7x - 5y = 1
solution = solve_diophantine(7, -5, 1)
if solution:
    x, y, gcd = solution
    print(f"x = {x}, y = {y}")