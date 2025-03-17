def flatten_and_sort(array):
    flat_list = [item for sublist in array for item in sublist]
    sorted_list = sorted(flat_list)
    return sorted_list
