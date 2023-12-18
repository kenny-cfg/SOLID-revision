class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def calculate_area(self):
        return self._width * self._height

    def elongate(self):
        return Rectangle(self._width * 2, self._height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
