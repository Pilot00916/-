def segment(first_point, second_point):
    try:
        result = first_point[0] + second_point[0] + first_point[1] + second_point[1]
    except TypeError as e:
        return ''.join(reversed(str(e)))
    return result