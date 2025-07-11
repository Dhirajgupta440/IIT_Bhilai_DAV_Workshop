def is_isogram(s):
    """
    Return True if the string has no repeating letters.
    Ignore case and non-letters.
    """
    cleaned = [c.lower() for c in s if c.isalpha()]
    return len(cleaned) == len(set(cleaned))
print(is_isogram("Machine"))   # False  (two 'i's)
print(is_isogram("Algorithm"))   # True
print(is_isogram("Dermatoglyphics"))   # True