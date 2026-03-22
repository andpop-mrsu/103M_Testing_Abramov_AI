from incorrectTriangleSidesExceptions import IncorrectTriangleSides

class Triangle:

    def __init__(self, a, b, c):
        sides = [a, b, c]

        if any(type(x) not in (int, float) for x in sides):
            raise IncorrectTriangleSides

        if any(x <= 0 for x in sides):
            raise IncorrectTriangleSides

        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c