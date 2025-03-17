def string_concatenation(str1, str2):
    if len(str1) < 2 or len(str2) < 2:
        return "Обе строки должны содержать как минимум два символа."
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    # todo Здесь нужно написать код
    result_string = new_str1 + ' ' + new_str2
    return result_string
