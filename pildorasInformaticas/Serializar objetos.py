import pickle

class Vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False


	def arrancar(self):

		self.enmarcha=True

	def acelerar(self):

		self.acelera=True

	def frenar(self):

		self.frena=True

	def estado(self):
		print("Marca: ", self.marca,"\nModelo: ", self.modelo, "\nEn marcha: ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena )


###Creamos objetos para serializar
coche1 = Vehiculos("Mazda","MX5")
coche2 = Vehiculos("Seat","Leon")
coche3 = Vehiculos("Renault","Megane")

####Metemos los objetos serializados en una lista
coches = [coche1, coche2, coche3]


###Creamos o abrimos el fichero en modo "Escritura de bytes"##
fichero=open("losCoches","wb")


###"Volcamos"La información de la lista en el fichero con .dump
pickle.dump(coches,fichero)

##Cerrar el fichero para que no quede abierto en la memoria
fichero.close()

#Borrar la variable para que no ocupe memoria
del (fichero)




###------------------Hasta Aquí parte 1 del programa----------------------#############

###Abrimos el fichero en modo lectura de bytes
ficheroApertura = open("losCoches","rb")

###Metemos la información del fichero en la variable "misCoches"
misCoches = pickle.load(ficheroApertura)

###Como ya la información está cargada en "misCoches", cerramos el fichero

ficheroApertura.close()


###Imprime la función "estado" de los objetos del fichero
for c in misCoches:
	print(c.estado())