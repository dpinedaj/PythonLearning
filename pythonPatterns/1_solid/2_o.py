# Open Close Principle
# Open for extension, closed for modification


from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# This one not scales
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p


# Specification


class Specification:
    def is_satisfied(self, item):
        raise NotImplementedError

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        raise NotImplementedError


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Old Approach
    print("Green Old")
    pf = ProductFilter()
    for p in pf.filter_by_color(products, Color.GREEN):
        print(p.name)

    # New Approach
    print("Green:")
    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(p.name)

    print("Large:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(p.name)

    print("Blue and large:")
    blue = ColorSpecification(Color.BLUE)
    large_blue = AndSpecification(blue, large)
    for p in bf.filter(products, large_blue):
        print(p.name)

    print("Green and Large:")
    large_and_green = green & large
    for p in bf.filter(products, large_and_green):
        print(p.name)
