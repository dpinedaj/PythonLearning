# *Ver qué gato (x o y), alcanzará primero al ratón (z)
# * O si el ratón se escapará primero


def catAndMouse(x, y, z):
    if abs(x - z) - abs(y - z) == 0:
        return "Mouse C"
    elif abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"


q = int(input())

for q_itr in range(q):
    xyz = input().split()

    x = int(xyz[0])

    y = int(xyz[1])

    z = int(xyz[2])
    print(catAndMouse(x, y, z) + "\n")
