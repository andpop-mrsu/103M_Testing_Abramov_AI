import pytest
from triangle_class import Triangle
from incorrectTriangleSidesExceptions import IncorrectTriangleSides


# Позитивные тесты
def test_create_valid_triangle():
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12

def test_equilateral():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"

def test_isosceles():
    t = Triangle(3, 3, 2)
    assert t.triangle_type() == "isosceles"

def test_nonequilateral():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"

def test_float_isosceles():
    t = Triangle(2.5, 2.5, 3)
    assert t.triangle_type() == "isosceles"

def test_very_small_isosceles():
    t = Triangle(0.0002, 0.0002, 0.0003)
    assert t.triangle_type() == "isosceles"

    # Негативные тесты
def test_invalid_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)

def test_negative():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 2)

def test_zero():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 2)

def test_wrong_type():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 2, 3)