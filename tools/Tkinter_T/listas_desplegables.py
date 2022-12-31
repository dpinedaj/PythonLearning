import tkinter as tk

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Lista desplegable")
    ventana.geometry("380x300")
    ventana.configure(bg="gray")
    ##-------------------SE CREA UNA VARIABLE DE SALIDA
    var = tk.StringVar(ventana)
    ##-------------------SE DEFINE UN "PRESET"-----------------------
    var.set("Rojo")
    opciones = ["Azul", "Rosa", "Amarillo", "Verde"]

    ####-----------CREAMOS LA LISTA DESPLEGABLE OptionMenu
    opcion = tk.OptionMenu(ventana, var, *opciones)
    opcion.place(x=0, y=0, height=20, width=100)

    ventana.mainloop()
