import pickle
##import io

fichero = open("lista_nombres","rb")

lista = pickle.load(fichero)###Carga la información en la variable lista

print(lista)





####Escribir el fichero abierto en un texto###
#lista_nombres = io.open("lista_nombres.txt","w")

#lista_nombres.writelines(lista)

#lista_nombres.close()


