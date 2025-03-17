def modification(lst):
    if len(lst) < 2:
        raise ValueError("Список должен содержать минимум 2 элемента")
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
