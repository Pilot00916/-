def minimum_length_slice(first_string, second_string):


    indices = [second_string.find(char) for char in first_string]
    min_index = min(indices)
    max_index = max(indices)
    min_slice = second_string[min_index:max_index + 1]

    return min_slice