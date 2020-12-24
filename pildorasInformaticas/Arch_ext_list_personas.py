import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona nueva con el nombre de", self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)



class ListaPersonas:

	personas = []
	####Creo un constructor que me cree el fichero y lo abra en forma de
	####lectura y escritura binaria, además que me sitúe el cursor al inicio

	def __init__(self):
		listadePersonas = open("ficheroExterno_personas", "ab+")
		listadePersonas.seek(0)

		try:
			self.personas = pickle.load(listadePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

		except:
			print("El fichero está vacío")

		finally:
			listadePersonas.close()
			del(listadePersonas)

	def agregarPersonas(self,p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listadePersonas = open("ficheroExterno_personas", "wb")
		pickle.dump(self.personas, listadePersonas)
		listadePersonas.close()
		del(listadePersonas)	

	def mostrarInfoFicheroExterno(self):
		print("La información del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)


miLista = ListaPersonas()
persona = Persona("Ana","Femenino", 19)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()