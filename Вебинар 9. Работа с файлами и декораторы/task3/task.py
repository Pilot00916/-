def memorize(func):
    # todo Здесь нужно написать код
    cached = {}
    def wrapper(*args, **kwargs):
        if args in cached:
            pass
        result_kinetic = func(*args)
        cached[args] = result_kinetic
        return result_kinetic, cached
    return wrapper



# todo Здесь ничего изменять не нужно!
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2)/2

