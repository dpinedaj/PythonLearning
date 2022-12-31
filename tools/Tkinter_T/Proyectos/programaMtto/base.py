import sqlite3 as lite
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import simpledialog as sd


def salir():
    tk._exit()


def entrarBase(url):
    global Conexion

    Conexion = lite.connect(url)


def crearBase():
    ventana2 = tk.Tk()
    ventana2.mainloop()


def crearTabla(nombre, columnas=(), tipos=()):
    global Conexion
    global Cursor
    entradas = ""
    for i, j in zip(columnas, tipos):
        entradas += i + " " + j + ","
    Cursor = Conexion.cursor()
    Cursor.execute("CREATE TABLE nombre(entradas )")
    Conexion.commit()


def ingresarDatos(tabla, datos):
    global Conexion
    global Cursor
    datos = ""
    Cursor.execute("INSERT INTO tabla VALUES(datos)")
    Conexion.commit()


def abrirurl():
    global url
    url = fd.askopenfilename(
        initialdir="/",
        title="Seleccione archivo",
        filetypes=(("csv files", "*."), ("todos los archivos", "*.*")),
    )


def mostrarbase():
    pass


#!----------------------------------------------VENTANA PRINCIPAL--------------------------------------


root = tk.Tk()
root.title("Programa")
root.iconbitmap("Proyectos/programaMtto/gear.ico")
root.geometry("800x800")
root.configure(background="RosyBrown4")
fondo = tk.PhotoImage(file="Proyectos\programaMtto\gear.gif")
fondo = fondo.subsample(2, 2)
fondolabel = tk.Label(root, image=fondo)
fondolabel.place(x=0, y=0, relwidth=1.0, relheight=1.0)


#!---------------------------------------------MENUBAR----------------------------------------------

menubarra = tk.Menu(root)
root.config(menu=menubarra)


menuarchivo = tk.Menu(menubarra)
menuarchivo.add_command(label="Nueva", command=crearBase)
menuarchivo.add_command(label="Abrir", command=abrirurl)
# //menuarchivo.add_command(label="Guardar", command= guardar)
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=salir)
menubarra.add_cascade(label="Archivo", menu=menuarchivo)


#!-----------------------------------------------TOOLBOX------------------------------------------------
toolbox = tk.Frame(root, bg="white", width=150)
toolbox.config(bd=10, relief="groove")
toolbox.pack(fill="y", side="right")
boton1 = tk.Button(toolbox, text="boton", width=15).pack(padx=10, pady=20)
boton2 = tk.Button(toolbox, text="boton", width=15).pack(padx=10, pady=20)
boton3 = tk.Button(toolbox, text="boton", width=15).pack(padx=10, pady=20)
boton4 = tk.Button(toolbox, text="boton", width=15).pack(padx=10, pady=20)
boton5 = tk.Button(toolbox, text="boton", width=15).pack(padx=10, pady=20)
boton6 = tk.Button(toolbox, text="boton", width=15).pack(padx=10, pady=20)


#!-------------------------------------------------EXPLORADOR DE DOCUMENTOS--------------------------------
explorer = tk.Frame(root, bg="sky blue", width=150)
explorer.config(bd=10, relief="raised", cursor="hand2")
explorer.pack(fill="y", side="left")


root.mainloop()
# //Conexion.close()
