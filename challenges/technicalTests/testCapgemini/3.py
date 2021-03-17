myArray = [1, 3, 4, 2, 7, 0]


def print_values():
    for i in myArray:
        for j in myArray:
            if i + j == 10:
                print("{} {}".format(i, j))
                return

print_values()
            