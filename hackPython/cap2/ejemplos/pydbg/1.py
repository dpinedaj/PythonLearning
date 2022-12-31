from pydbg import dbg

a = 2

b = 3

dbg(a + b)


def square(x: int) -> int:
    return x * x


dbg(square(a))
