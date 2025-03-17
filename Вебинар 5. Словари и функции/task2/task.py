def repeats(our_str: str) -> str:
    char_count = {}
    result = []
    for char in our_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        result.append(f"{char}_{char_count[char]}")
    return ''.join(result)
