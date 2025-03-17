def treatment_sum(our_tuple):
    if len(our_tuple) < 2:
        return 'Недостаточно данных'
    elif len(our_tuple) > 2:
        raise Exception('Много данных')
    else:
        try:
            result = our_tuple[0] + our_tuple[1]
            return result
        except TypeError:
            return 'Нельзя сложить эти данные'
