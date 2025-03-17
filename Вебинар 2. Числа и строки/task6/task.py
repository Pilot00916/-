def delete_symbols(string):

    new_string = ''.join([char for index, char in enumerate(string) if index % 2 == 0])
    return new_string
