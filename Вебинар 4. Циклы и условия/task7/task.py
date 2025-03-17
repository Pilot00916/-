def move_zeros(lst):
    non_zeros = [num for num in lst if num != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros
