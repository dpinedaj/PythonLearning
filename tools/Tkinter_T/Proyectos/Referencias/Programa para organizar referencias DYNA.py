


while True:
    print("###\n###")
    m = int(input("Seleccione lo que vas a ingresar\
    \n1.Revista impresa\
    \n2.Artículo de revista impresa\
    \n3.Revista electrónica\
    \n4.Artículo de revista electrónica\
    \n5.Libro\
    \n6.Capítulo de libro impreso\
    \n7.Libro electrónico\
    \n8.Capítulo de libro electrónico\
    \n9.Tesis\
    \n10.Conferencias,congresos,seminarios\
    \n11.Documento presentado en congreso o conferencia\
    \n12.Informe\
    \n>>"))

    if m == 1:
        print("Inserta los datos de la Revista impresa: \n###\n###")
        titulo_revista = input("Título de la revista (i.e. Revista DYNA): ")
        lugar = input("Lugar (i.e. Facultad de Minas, Universidad Nacional de Colombia, sede Medellín): ")
        volumen = input("Volumen(número) (i.e. 79(175) ): ")
        mes = input("Mes(es) (i.e. Octubre) : ")
        anio = input("Año (i.e. 2012 ): ")

        print("##\n##\n("+titulo_revista+", "+lugar+", "+volumen+", "+mes+", "+anio+")")

        print("###\n###")

    if m == 2:

        print("Inserta los datos del Artículo de Revista Impresa: \n###\n###")

        n = int(input("Inserta el número de autores involucrados: "))
        apellido = []
        nombre = []
        for i in range(n):
            print(f"Inserta el apellido del {i+1} autor (i.e. Rodrígez)", end=": ")
            apellido.append(input())
            print(f"Inserta el(las) iniciales del nombre del {i+1} autor (i.e. D A, D)", end=": ")
            nombre.append(input().replace(" ", "."))

        titulo_articulo = input("Inserta el Título del Artículo (i.e. Efecto de dos índices de...): ")
        titulo_revista = input("Inserta el Título de la Revista (i.e. Revista Facultad de Minas): ")
        volumen = input("Inserta el volumen(número) de la revista (i.e. 58(2)): ")
        paginas = input("Inserta el número de páginas (i.e. pp. 2827-2837): ")
        mes = input("Inserta el mes (i.e. Octubre): ")
        anio = input("Inserta el año (i.e. 2005): ")
        c = ""

        for j, k in zip(apellido, nombre):
            c = c+str(j)+", "+str(k)+", "
        print("###\n###")
        print("("+c+titulo_articulo+", "+titulo_revista+", "+volumen+", " + paginas+", "+mes+", "+anio+")")
        print("###\n###")

    option = str.upper(input("Quieres seguir insertando fuentes? (y/n): "))

    if option == "N":
        break
    elif option =="Y":
    	next