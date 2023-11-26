def decompress(x):
    word = ""
    bits_per_letter = 5

    while x > 0:
        letter_value = x & 31
        letter = chr(letter_value + 64)
        word = letter + word
        x = x >> bits_per_letter

    reversed_word = word[::-1]


    return reversed_word

