# TODO se ingresa el número de páginas "n", y la página "p" a la que se debe llegar, hay que hacer un programa que elija
# TODO cuál es el camino más corto para llegar a la página, si contando desde atrás del libro o desde adelante, y cuáles son las páginas mínimas.

import math


def pageCount(n, p):

    if n / 2 < p:
        if n % 2 == 0:
            result = math.ceil((n - p) / 2)
        else:
            result = math.ceil((n - p - 1) / 2)

    elif n / 2 >= p:

        result = math.ceil((p - 1) / 2)

    return result


n = int(input("Ingrese n: "))
p = int(input("Ingrese p: "))

result = pageCount(n, p)

print(result)
