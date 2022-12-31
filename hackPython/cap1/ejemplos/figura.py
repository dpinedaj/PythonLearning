from numpy import hypot, sqrt


class Figura(object):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2


class Rectangulo(Figura):
    def __init__(self, dim1, dim2):
        super().__init__(dim1, dim2)

    def area(self):
        if self.dim1 == self.dim2:
            print("El área del cuadrado es: ")
        else:
            print("El área del rectángulo es: ")

        return self.dim1 * self.dim2

    def perimetro(self):
        print("El perimetro del rectángulo es: ")
        return 2 * self.dim1 + 2 * self.dim2


class Triangulo(Figura):
    def __init__(self, dim1, dim2, base, altura):
        super().__init__(dim1, dim2)
        self.base = base
        self.altura = altura

    def area(self):
        print("El área del triángulo es: ")
        return (self.base * self.altura) / 2

    def perimetro(self):
        print("El perímetro del triángulo es: ")
        return self.dim1 + self.dim2 + self.base

    def hipotenusa(self):
        print("La hipotenusa es: ")
        return hypot(self.base, self.altura)


def main():
    F = Figura(5, 5)
    R = Rectangulo(6, 5)
    T = Triangulo(7, 6, 5, 4)

    print(R.area())
    print(R.perimetro())
    print(T.area())
    print(T.perimetro())


if __name__ == "__main__":
    main()
