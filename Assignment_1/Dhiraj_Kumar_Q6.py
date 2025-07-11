def fibonacci(n):
    """
    Return the n-th Fibonacci number (F1=1, F2=1).
    Use iteration, not recursion.
    """
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a + b
    return b
print(fibonacci(1))   #  1
print(fibonacci(7))   #  13
print(fibonacci(10))   #  55