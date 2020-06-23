print("programa de becas año 2019")
#Nombrar las variables
distancia_escuela=int(input("introduce la distancia a la escuela en km "))
print(distancia_escuela)

numero_hermanos=int(input("introduce el n° de hermanos en el centro "))
print(numero_hermanos)

salario_familiar=int(input("salario anual bruto "))
print(salario_familiar)
#Insertar las condicionales
if distancia_escuela>40 and numero_hermanos>2 and salario_familiar>=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")
	
