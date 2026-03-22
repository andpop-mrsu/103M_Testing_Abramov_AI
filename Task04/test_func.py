import unittest
from triangle_func import get_triangle_type
from incorrectTriangleSidesExceptions import IncorrectTriangleSides

class TestTriangleFunc(unittest.TestCase):
    # Позитивные тесты
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(3, 3, 2), "isosceles")

    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_float_isosceles(self):
        self.assertEqual(get_triangle_type(2.5, 2.5, 3), "isosceles")

    def test_very_small_values(self):
        self.assertEqual(get_triangle_type(0.0002, 0.0002, 0.0003), "isosceles")


    # Негативные тесты
    def test_invalid_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 1, 1)

    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 2)

    def test_wrong_type(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 2, 3)

if __name__ == "__main__":
    unittest.main()