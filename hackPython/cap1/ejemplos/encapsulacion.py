# Al definir una variable con 2 guion bajo '__' se considera privada y solo es visible dentro de la misma clase o sus métodos


class ClaseA:
    def __init__(self, x):
        self.__x = x
        self.y = self.__x * 2


A = ClaseA(10)

print(dir(A))
