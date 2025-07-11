def count_letters(text):
    """
    Return a tuple (vowels, consonants) in the text.
    Count only English letters, ignore case.
    """
    vowels = "aeiou"
    v_count = 0
    c_count = 0
    for ch in text.lower():
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return (v_count, c_count)
print(count_letters("Data Science"))    #(5,5)
print(count_letters("IIT Bhilai"))    #(4,4)
print(count_letters("1234"))    #(0,0)