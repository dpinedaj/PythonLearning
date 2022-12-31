class MiClase:
    def __init__(self, x=2):
        self.x = x

    def devuelve_valor(self):
        return self.x


A = MiClase(10)
print(A.devuelve_valor())
