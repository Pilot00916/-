import math

def square_calculation(a):
    perimeter = 4 * a
    square = round(a ** 2, 2)
    diagonal = round(a * math.sqrt(2), 2)

    return perimeter, square, diagonal
