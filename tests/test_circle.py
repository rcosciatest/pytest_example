import pytest
import math
from source.shapes import Circle


class TestCircle:

    def test_circle_perimeter():
        circle = Circle(10)
        assert circle.perimeter() == 2 * math.pi * 10

        
    def test_circle_area():
        circle = Circle(10)
        assert circle.area() == 314.159