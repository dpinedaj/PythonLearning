from io import open

archivo_texto = open(
    "archivo.txt", "r+"
)  ###Abre el archivo en modo lectura y escritura


# archivo_texto = open("archivo.txt",w)------Abre el archivo en modo escritura


# archivo_texto.write("\n texto.....")


lista_texto = archivo_texto.readlines()

lista_texto[
    1
] = "Esta línea ha sido incluída desde el exterior\n"  ####Pone el cursor en la posición 1(línea 2)

archivo_texto.seek(0)  ###Pone el cursor en la posición 0 para seguir escribiendo ahí

archivo_texto.writelines(lista_texto)

archivo_texto.close()


###print(archivo_texto.read(11))---- Imprime el contenido del texto desde la posición 11

###print(archivo_texto.read())---Imprime el contenido desde la pos actual (empieza en 0)
