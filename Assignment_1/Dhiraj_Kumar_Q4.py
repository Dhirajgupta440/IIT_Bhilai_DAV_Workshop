def is_palindrome(s):
    """
    Return True if string s reads the same forwards and backwards.
    Ignore case and non-alphanumeric characters.
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("Madam"))   # True
print(is_palindrome("Step on no pets"))   # True
print(is_palindrome("Hello, World"))   # False