def is_armstrong(n):
    """
    An Armstrong number is an n-digit number that equals
    the sum of each digit raised to the power n.
    """
    digits = [int(d) for d in str(n)]
    power = len(digits)
    total = sum(d**power for d in digits)
    return total == n
print(is_armstrong(153))   # True
print(is_armstrong(370))   # True
print(is_armstrong(123))   # False
