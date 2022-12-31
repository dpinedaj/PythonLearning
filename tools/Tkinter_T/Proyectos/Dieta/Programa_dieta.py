import tkinter as tk
import numpy as np


def ec_miffin():
    miffin = "Ingresa tus datos"
    if str(var.get().strip()) == "Hombre":
        try:
            miffin = (
                (10 * int(peso.get()))
                + (6.25 * int(estatura.get()) - (5 * int(edad.get())))
                + 5
            )
        except:
            miffin = "Ingresa tus datos"
    elif str(var.get().strip()) == "Mujer":
        try:
            miffin = (
                (10 * int(peso.get()))
                + (6.25 * int(estatura.get()) - (5 * int(edad.get())))
                - 161
            )
        except:
            miffin = "Ingresa tus datos"
    return sal.set(miffin)


def gasto():

    if sal != 0:
        if str(fact.get().strip()) == "Factor 1":
            gasto = float(sal.get()) * 1.2
        elif str(fact.get().strip()) == "Factor 2":
            gasto = float(sal.get()) * 1.3
        elif str(fact.get().strip()) == "Factor 3":
            gasto = float(sal.get()) * 1.4

    else:
        gasto = "Selecciona el factor de actividad"

    return sal2.set(gasto)


###----------------CREANDO LA VENTANA###---------------------
ventana = tk.Tk()
ventana.title("Programa dietas")
ventana.geometry("500x700")
ventana.configure(bg="lavender")


###----------------------------------CREAR UN MENÚ DESPLEGABLE-------------------------------------------


# TODO  CREAR UN MENÚ DESPLEGABLE

barraMenu = tk.Menu(ventana)
menuArchivo = tk.Menu(barraMenu)
menuOpciones = tk.Menu(barraMenu)
menuAyuda = tk.Menu(barraMenu)


menuArchivo.add_command(label="Salir", command=ventana.destroy)


barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
barraMenu.add_cascade(label="Opciones", menu=menuOpciones)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)


ventana.config(menu=barraMenu)

#####---------------CREANDO ETIQUETAS Y ENTRADAS DE DATOS
#######ETIQUETA DE EDAD
e1 = tk.Label(ventana, text="Ingresa tu edad:", bg="gray", fg="black")
e1.place(x=0, y=40, height=20, width=100)

edad = tk.Entry(ventana)
edad.place(x=100, y=40, height=20, width=100)
e11 = tk.Label(ventana, text="años", fg="black", bg="lavender")
e11.place(x=200, y=40)
#######ETIQUETA DE PESO
e2 = tk.Label(ventana, text="Ingresa tu peso:", bg="gray", fg="black")
e2.place(x=0, y=65, height=20, width=100)
peso = tk.Entry(ventana)
peso.place(x=100, y=65, height=20, width=100)
e22 = tk.Label(ventana, text="kg", fg="black", bg="lavender")
e22.place(x=200, y=65)

#######ETIQUETA DE ESTATURA
e3 = tk.Label(ventana, text="Ingresa tu estatura:", bg="gray", fg="black")
e3.place(x=0, y=90, height=20, width=100)

estatura = tk.Entry(ventana)
estatura.place(x=100, y=90, height=20, width=100)
e33 = tk.Label(ventana, text="cm", fg="black", bg="lavender")
e33.place(x=200, y=90)

#######ETIQUETA DE GÉNERO

var = tk.StringVar(ventana)
var.set("Selecciona tu género")
opciones = [
    "                   Hombre                 ",
    "                   Mujer                 ",
]

entrada4 = tk.OptionMenu(ventana, var, *opciones)
entrada4.place(x=0, y=115, height=30, width=200)
entrada4.configure(bg="snow", fg="black")


#####--------------------------------SALIDA DE TMB---------------------------
sal = tk.StringVar(ventana)
e4 = tk.Label(ventana, text="Tu tasa metabólica basal es:", bg="gray", fg="black")
e4.place(x=0, y=200, height=20, width=200)

salida = tk.Label(ventana, textvariable=sal, bg="white", fg="red")
salida.place(x=220, y=200, height=20, width=250)

######---------------------------------CALCULAR LA TMB-----------------

imb = tk.Button(ventana, text="TMB", command=ec_miffin, bg="light salmon", fg="black")
imb.place(x=300, y=40, height=100, width=100)

# ----------------------------------------------------CÁLCULO DEL GASTO CALÓRICO------------------------------------------

e5 = tk.Label(
    ventana,
    text="Ahora vamos a calcular tu gasto calórico",
    bg="lavender",
    font=("Amaranth", 15),
    fg="black",
)
e5.place(width=500, y=240)

####---------LISTA DE FACTOR DE ACTIVIDAD
fact = tk.StringVar(ventana)
fact.set("Selecciona tu nivel de actividad")
opt_fact = ["Factor 1", "Factor 2", "Factor 3", "Factor 4", "Factor 5"]

entrada5 = tk.OptionMenu(ventana, fact, *opt_fact)
entrada5.place(x=0, y=280, height=30, width=200)
entrada5.configure(bg="snow", fg="black")

sal2 = tk.StringVar(ventana)
e6 = tk.Label(ventana, text="Tu gasto calórico diario es: ", bg="gray", fg="black")
e6.place(x=0, y=510, height=20, width=200)

salida2 = tk.Label(ventana, textvariable=sal2, bg="white", fg="red")
salida2.place(x=220, y=510, height=20, width=250)

gasto = tk.Button(ventana, text="Gasto", command=gasto, bg="light salmon", fg="black")
gasto.place(x=300, y=340, height=100, width=100)


ventana.mainloop()
