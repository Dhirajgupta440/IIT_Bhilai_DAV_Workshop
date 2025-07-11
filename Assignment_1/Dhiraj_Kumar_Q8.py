def is_perfect(n):
    """
    A perfect number equals the sum of its proper divisors
    (excluding itself).
    """
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
print(is_perfect(6))   # True(1+2+3=6)
print(is_perfect(28))   # True(1+2+4+7+14=28)
print(is_perfect(12))   # True(1+2+3+4+6!=12)