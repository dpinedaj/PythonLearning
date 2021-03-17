import tkinter as tk


def suma():

    suma = int(entrada1.get()) + int(entrada2.get()) ### con get() se obtiene el valor de la entrada
    return var.set(suma)  #Se almacena el resultado en "var"
def cerrar():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Sumadora")
ventana.geometry('300x300')
ventana.configure(bg = "rosy brown")

var = tk.StringVar()


##-------------------------------CREAR LA ENTRADA 1------------------------
e1 = tk.Label(ventana,text = "Numero 1: ",bg = "black", fg = "white")
e1.pack(padx = 5, pady = 5, ipadx =5, ipady = 5)

entrada1 = tk.Entry(ventana)
entrada1.pack(padx= 5, pady = 5, ipadx = 5, ipady = 5)


##--------------------------------CREAR LA ENTRADA  2-------------------
e2 = tk.Label(ventana,text = "Numero 2: ",bg = "black", fg = "white")
e2.pack(padx = 5, pady = 5, ipadx =5, ipady = 5)

entrada2 = tk.Entry(ventana)
entrada2.pack(padx= 5, pady = 5, ipadx = 5, ipady = 5)


##_-----------------------------CREAR EL BOTÓN PARA SUMAR-----------------------------
botonsuma = tk.Button(ventana, text = "Suma", fg = "indian red",command = suma)
botonsuma.pack(side = tk.TOP, pady = 10)

##-------------------------------CREAR CASILLA DEL RESULTADO----------------------
####### Con textvariable permito que se modifique según el valor que se obtenga de var
res = tk.Label(ventana, bg = "snow", textvariable = var, padx = 5, pady = 5, width = 10)
res.pack(pady = 10)

##_-----------------------------CREAR EL BOTÓN PARA CERRAR-----------------------------
botonsuma = tk.Button(ventana, text = "Cerrar", fg = "black",bg = "red", command = cerrar)
botonsuma.pack(pady = 10)



ventana.mainloop()