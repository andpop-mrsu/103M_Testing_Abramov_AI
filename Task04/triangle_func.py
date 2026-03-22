from incorrectTriangleSidesExceptions import IncorrectTriangleSides


def get_triangle_type(a, b, c):
    """

    Позитивные тесты:
    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 2)
    'isosceles'
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(2.5, 2.5, 3)
    'isosceles'
    >>> get_triangle_type(0.0002, 0.0002, 0.0003)
    'isosceles'

    Негативные тесты:
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
    ...
    incorrectTriangleSidesExceptions.IncorrectTriangleSides
    >>> get_triangle_type(0, 1, 1)
    Traceback (most recent call last):
    ...
    incorrectTriangleSidesExceptions.IncorrectTriangleSides
    >>> get_triangle_type(-1, 2, 2)
    Traceback (most recent call last):
    ...
    incorrectTriangleSidesExceptions.IncorrectTriangleSides
    >>> get_triangle_type("a", 2, 3)
    Traceback (most recent call last):
    ...
    incorrectTriangleSidesExceptions.IncorrectTriangleSides
    """

    sides = [a, b, c]

    if any(type(x) not in (int, float) for x in sides):
        raise IncorrectTriangleSides

    if any(x <= 0 for x in sides):
        raise IncorrectTriangleSides

    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides

    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"