class Coche():
	#Estado inicial __init__
	def __init__(self):

		#Encapsulamos las variables con __
		self.LargoChasis=250
		self.anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False
	#son 4 propiedades

	#Al llamar la función con True, se almacena
	#el true en "arrancamos" y Self sería el objeto
	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			return "El coche está en marcha"

		else:
			return "El coche está parado"



	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, "y un largo de ",
			self.LargoChasis)
		
#son 2 comportamientos

	
		

miCoche=Coche()



print(miCoche.arrancar(True))

miCoche.estado()

print("-----------A continuación creamos el segundo objeto----------")


miCoche2=Coche()


miCoche2.__ruedas=2


print(miCoche2.arrancar(False))



miCoche2.estado()
