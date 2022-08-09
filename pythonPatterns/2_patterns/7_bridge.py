# Bridge Pattern
######################
# THe Bridge Pattern is all about connectiong components together
# through abstractions

# Bridge prevents 'Cartesian product' complexity explosion
# Example:
# - Base class ThreadScheduler
# - Can be preemptive or cooperative
# - Can run on Windows or Unix
# - End up with with a 2x2 scenario: WindowsPTS, UnixPTS, WindowsCTS, UnixCTS
#######
# Yoy can rely on inheritance and aggregations

# Definition:
# A mechanism that decouples an interface (hierarchy) from an
# implementation (hierarchy).


# Bridge
# circle square
# vector raster implementations (How can you draw a circle square??
# VectorCircle VectorSquare, VectorRaster..... what to do?


from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        # Here we are using the Bridge pattern using the
        # renderer instance as a bridge to draw the circle with the
        # specifications
        # Here is the connection of 2 hierarchies of different classes
        # (Shapes and Renderers)
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()


########################################################################
# Exercise
# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def __str__(self):
        return "Drawing {} as {}".format(self.name, self.renderer.what_to_render_as)


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Triangle"


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Square"
