class Persona:
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripción(self):

        print(
            "Nombre: ",
            self.nombre,
            " Edad: ",
            self.edad,
            " Residencia: ",
            self.lugar_residencia,
        )


class Empleado(Persona):
    def __init__(
        self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado
    ):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad = antigüedad

    def descripción(self):
        super().descripción()

        print(" Salario: ", self.salario, " Antigüedad: ", self.antigüedad)


Antonio = Empleado(1500, 15, "Antonio", 55, "Colombia")

Antonio.descripción()

print(isinstance(Antonio, Persona))
