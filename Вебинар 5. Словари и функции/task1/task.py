def letter_stat(our_str):
    letters_dict = {}
    for letter in set(our_str):
        letters_dict[letter] = our_str.count(letter)
    return letters_dict
