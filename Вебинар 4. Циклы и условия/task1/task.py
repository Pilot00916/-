def which_triangle(a: int, b: int, c: int) -> str:
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Не треугольник'
    if a == b == c:
        return 'Равносторонний'
    elif a == b or b == c or a == c:
        return 'Равнобедренный'
    else:
        return 'Обычный'

