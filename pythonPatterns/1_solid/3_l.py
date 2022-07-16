# Liskov substution principle


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self._width}, Height: {self._height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    # Those methods directly violates the principle
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f"Expected an area of {expected}, got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)


# A good Idea to solve this issue is just creating
# a boolean that says that that rectangle is actually a square
# and not creating a child of that one
