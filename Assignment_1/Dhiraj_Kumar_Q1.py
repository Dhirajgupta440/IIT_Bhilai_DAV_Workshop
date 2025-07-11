def is_disarium(n):
    """
    A Disarium number is one where the sum of its digits
    raised to their positions equals the number itself.
    """
    s = str(n)
    total = 0
    for i in range(len(s)):
        digit = int(s[i])
        power = i + 1
        total += digit ** power
    return total == n
print(is_disarium(75))   # False, because 71 + 52 = 32 
print(is_disarium(135))   # True, 11 + 32 + 53 = 135
print(is_disarium(72))    # False, 81 + 82 = 72