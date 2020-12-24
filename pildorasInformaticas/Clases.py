

class Coche():
	LargoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False
#son 4 propiedades


	def arrancar(self):
		self.enmarcha=True

	def estado(self):
		if(self.enmarcha):
			return "El coche está en marcha"

		else:
			return "El coche está parado"
		
#son 2 comportamientos

	
		

miCoche=Coche()

print("El largo del coche es: ",miCoche.LargoChasis)
print("El coche tiene ",miCoche.ruedas," ruedas")

miCoche.arrancar()

print(miCoche.estado())

print("-----------A continuación creamos el segundo objeto----------")


miCoche2=Coche()

print("El largo del coche es: ",miCoche.LargoChasis)
print("El coche tiene ",miCoche.ruedas," ruedas")

print(miCoche2.estado())
