# Facade
# - Exposing several components through a single interface
# ----------------------------------------------------------------
# Motivation
# - Balancing Complexity and presentation/usability
# - Typical home
# -- Many subsystems (electrical, sanitation)
# -- Complex internal structure (e.g., floor layers)
# -- End user is not exposed to internals
# - Same with software
# -- Many systems to provide flexibility, but...
# -- API consumers want it to "just work"
# ----------------------------------------------------------------
# Definition:
# Provides a simple, easy to understand/user interface over a
# large and sophisticated body of code


class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.value = [" "] * (width * height)

    def __getitem__(self, item):
        return self.value.__getitem__(item)

    def write(self, text):
        self.value += text


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offser = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)


if __name__ == "__main__":
    c = Console()
    c.write("hello")


# Exercise

from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for x in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def generate(self, size):
        generator = Generator()
        splitter = Splitter()
        verifier = Verifier()

        while True:
            array = [generator.generate(size) for i in range(size)]
            splitted = splitter.split(array)
            if verifier.verify(splitted):
                return array


if __name__ == "__main__":
    square = MagicSquareGenerator().generate(3)
    print(square)
