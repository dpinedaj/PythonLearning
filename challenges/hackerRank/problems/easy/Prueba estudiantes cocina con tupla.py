numero_estudiantes=int(input("Inserte el número de estudiantes en el curso: "))

lista_estudiantes=[]
lista_de_nombres=[]

a=1



for i in range(numero_estudiantes):#Aquí se insertan todos los nombres a la lista
	print(f"Inserte el nombre completo del estudiante {a}",end="")
	nombre=input(": ")
	lista_estudiantes.insert(i,nombre)
	a+=1
	


for j in range(numero_estudiantes):#Crea una nueva lista solo con los nombres
	lista_de_nombres.insert(j,lista_estudiantes[j].split()[0])


tupla_nombres=tuple(lista_de_nombres)

for k in range(numero_estudiantes):#Revisa cuántas veces está el nombre
	if tupla_nombres.count(tupla_nombres[k])==1:
		lista_estudiantes[k]=lista_de_nombres[k]


c=1
for estudiante in lista_estudiantes:#Imprime la lista de estudiantes del curso
	print(str(c)+" "+estudiante)
	c+=1


