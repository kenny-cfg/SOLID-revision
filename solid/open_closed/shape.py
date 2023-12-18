from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_area(self):
        return self._length * self._width


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return pi * self._radius ** 2
