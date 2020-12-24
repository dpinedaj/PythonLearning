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

class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar
		if self.cargado:
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"

class Moto(Vehiculos):
	
	hcaballito=""

	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca: ", self.marca,"\nModelo: ", self.modelo, "\nEn marcha: ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,"\n",self.hcaballito )

class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):

		super().__init__(marca,modelo)

		self.autonomia=100

	def cargarEnergía(self):

		self.cargando=True




#Creamos la instancia/objeto Moto
miMoto=Moto("Honda", "CBR")

miMoto.caballito()
miMoto.estado()


#Creamos la instancia/objeto Furgoneta
miFurgoneta=Furgoneta("Renault","Kangoo")

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


#Creamos una subclase que hereda de 2 distintas clases

class BicicletaElectrica(VElectricos,Vehiculos):
	pass

miBici=BicicletaElectrica("Orbea","Kangoo")