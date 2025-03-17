def get_list_info(lst):
    min_elem = min(lst)
    max_elem = max(lst)
    sum_list = sum(lst)
    average = round(sum_list / len(lst), 2)
    return min_elem, max_elem, sum_list, average
