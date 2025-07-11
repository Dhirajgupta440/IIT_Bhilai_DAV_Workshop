def swap(a, b):
    """
    Swap two integers without using a third variable.
    Return the new pair (a, b).
    """
    a = a + b
    b = a - b
    a = a - b
    return (a, b)
print(swap(3,5))    # (5,3)
print(swap(-1,10))    # (10,-1)
print(swap(0,0))    # (0,0)
