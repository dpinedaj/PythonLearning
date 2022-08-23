# Decorators
###############################
# Motivation:
# Augment funcionality
# Do no want to rewrite or alter existing code (OCP)
# Performing modifications
# Want to keep new functionality separate (SRP)
# Need to be able to interact with existing structures


import time
from abc import ABC
from unittest import TestCase


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {int((end-start)*1000)} ms")
        return result

    return wrapper


@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("We are done")
    return 123


# if __name__ == "__main__":
#     some_op()

# Classic decorator


class Shape(ABC):
    def __str__(self):
        return ""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return "A circle of radius %s" % self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return "A square with side %s" % self.side


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception("Cannot apply same decorator twice")
        self.color = color
        self.shape = shape

    def __str__(self):
        return "%s has the color %s" % (self.shape, self.color)


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has {self.transparency * 100.0}% transparency"


# if __name__ == "__main__":
#     circle = Circle(2)
#     print(circle)

#     red_circle = ColoredShape(circle, "red")
#     print(red_circle)

#     red_half_transparent_circle = TransparentShape(red_circle, 0.5)
#     print(red_half_transparent_circle)

#     mixed = ColoredShape(ColoredShape(Square(3), "red"), "green")
#     print(mixed)


# Dynamic Decorator
class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f"wrote {len(strings)} lines")

    def __getattr__(self, item):
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key, value):
        if key == "file":
            self.__dict__[key] = value
        else:
            setattr(self.__dict__["file"], key)

    def __delattr__(self, item):
        delattr(self.__dict__["file"], item)


# if __name__ == "__main__":
#     file = FileWithLogging(open("Hello.txt", "w"))
#     file.writelines(["Hello", "world"])
#     file.write("testing")
#     file.close()


# Exercise


class ColoredShape(ColoredShape):
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        if hasattr(self.shape, "resize"):
            self.shape.resize(factor)


class Evaluate(TestCase):
    def test_circle(self):
        circle = ColoredShape(Circle(5), "red")
        self.assertEqual("A circle of radius 5 has the color red", str(circle))
        circle.resize(2)
        self.assertEqual("A circle of radius 10 has the color red", str(circle))
