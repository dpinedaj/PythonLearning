from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

ventana = Tk()


def abrirfichero():
    file = fd.askopenfilename(title="Abrir", initialdir="C:")


def mensaje():
    mb.showinfo(title="mensaje", message="HOLAAA")


Button(ventana, text="abrir", command=abrirfichero).pack()
Button(ventana, text="mensaje", command=mensaje).pack()


ventana.mainloop()
