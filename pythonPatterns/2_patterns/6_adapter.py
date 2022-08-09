###############################
# Adapter
# It tries to adapt the interface requirements
# For example
# - Electrical devices have different power (interface) requirements
#   - Voltage (5V, 220V)
#   - Socket/plug type (Europe, UK, USA)
# We cannot modify our gadgets to support every possible interface
# Thus, we use a special device (an adapter) to give us the interface
# we require from the interface we have
################
# An Adapter is a construct which adapts an existing interface X to
# conform to the required interface Y.


# Adapter (No caching)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end="")


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        point_c1 = Point(x, y)
        point_c2 = Point(x + width, y)
        point_c3 = Point(x, y + height)
        point_c4 = Point(x + width, y + height)

        self.append(Line(point_c1, point_c2))
        self.append(Line(point_c2, point_c4))
        self.append(Line(point_c1, point_c3))
        self.append(Line(point_c3, point_c4))


class LineToPointAdapter(list):
    count = 0

    def __init__(self, line):
        self.count += 1
        print(f'{self.count}: Generating points for line '
              f'[{line.start.x},{line.start.y}]→'
              f'[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))


def draw(rcs):
    print('\n\n--- Drawing some stuff ---\n')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == '__main__':
    rcs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6),
    ]

    draw(rcs)


# With Caching

class LineToPointAdapter:
    count = 0
    cache = {}

    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return

        super().__init__()
        self.count += 1
        print(f'{self.count}: Generating points for line ' +
              f'[{line.start.x},{line.start.y}]→[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])


if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    draw(rs)
    draw(rs)

    # can define your own hashes or use the defaults
    print(hash(Line(Point(1, 1), Point(10, 10))))
