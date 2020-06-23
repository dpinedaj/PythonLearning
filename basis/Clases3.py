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
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "El coche está en marcha"

		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo, no podemos arrancar"

		else:
			return "El coche está parado"


	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, "y un largo de ",
			self.LargoChasis)
		

	def __chequeo_interno(self):
		print("realizando chequeo interno")


		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok"and self.aceite=="ok" and self.puertas=="cerradas"):
			return True

		else:
			return False



	
		

miCoche=Coche()


print(miCoche.arrancar(True))


miCoche.estado()


print("-----------A continuación creamos el segundo objeto----------")



miCoche2=Coche()


miCoche2.__ruedas=2


print(miCoche2.arrancar(False))



miCoche2.estado()
