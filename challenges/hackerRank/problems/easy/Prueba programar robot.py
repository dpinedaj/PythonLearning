print("Programa para medir los pasos de un robot")


print(f"Inserta el número de pruebas para el robot",end="")

numero_casos=int(input(":"))
a=1

visitas=[]
lista_conteo=[]
cuenta_visitas=[]


for i in range(numero_casos):#Se ingresan los datos de las variables y se gurdan en una lista
	print(f"Inserte la cantidad de instrucciones y el inicio de la prueba {a}",end="")
	pasos,inicio=input(":").split()
	pasos=int(pasos)
	inicio=int(inicio)
	
	instruccion=str(input(f"Inserte las letras L y R (exactamente {pasos} letras sin espacios) para instruir al robot:")).upper()
	while len(instruccion)!=pasos:

		if len(instruccion)>pasos:
			instruccion=instruccion[0: pasos]
			print("Sus pasos son "+instruccion)

		else:
			print("Cantidad de pasos insuficiente.")
			instruccion=str(input(f"Inserte de nuevo las {pasos} letras L y R sin espacios:")).upper() 

	

	a+=1


	

	lista_conteo.append(inicio)

	for j in instruccion:#Ingresa los datos en una nueva lista para contarlos luego

		
		if j=="L":
			inicio=inicio-1
			
		elif j=="R":
			inicio=inicio+1

		lista_conteo.append(inicio)

	

	
	
	for k in range(len(lista_conteo)):#Cuenta en cuántas posiciones diferentes estuvo

		if lista_conteo[k] in cuenta_visitas:

			continue

		cuenta_visitas.append(lista_conteo[k])


		
	visitas.append(len(cuenta_visitas))

	cuenta_visitas.clear()
	lista_conteo.clear()
		
		

b=1
for l in visitas:
	print("El robot estuvo en "+str(l) +f" posiciones en la prueba {b}")
	b+=1








