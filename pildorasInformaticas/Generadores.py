def devuelve_ciudades(*ciudades): 
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from elemento


ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona","Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))