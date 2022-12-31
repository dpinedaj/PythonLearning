class Coche:
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto:
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


# Ubica el tipo al que le corresponda según su tipo con polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


# se almacena en un tipo para luego poder ubicarse con la función general

mivehiculo = Camion()

desplazamientoVehiculo(mivehiculo)
