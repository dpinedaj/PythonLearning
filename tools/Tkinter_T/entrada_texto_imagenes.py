import tkinter as tk

ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("800x500")
ventana.configure(bg="slate gray")


# ---------------------------INSERTAR IMÁGENES DEBEN SER FORMATO GIF-----------
# -----CONVERSOR DE IMÁGENES A GIF----------------- https://image.online-convert.com/convert-to-gif

imagen = tk.PhotoImage(file="Proyectos\programaMtto\gear.gif")
###--------Para reducir el tamaño de la imágen, a mayor número, menor tamaño de imagen
imagen = imagen.subsample(2, 2)

label = tk.Label(image=imagen)

#####Con esta instrucción le asigno lugar a la imagen (Si quisiera ponerla de fondo)
label.place(x=0, y=0, relwidth=1.0, relheight=1.0)
# label.pack()    #######Se usa place o pack para variar

# ------------------------------------------------ENTRADA NOMBRE---------------------------------------------
###Creamos la etiqueta 1
e1 = tk.Label(ventana, text="Nombre: ", bg="firebrick", fg="white")
e1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

###Con esto se crea una entrada de texto justo después de la etiqueta 1 CON EL ORGANIZADOR "PACK"
entrada1 = tk.Entry(ventana)
entrada1.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

# -----------------------------------------------ENTRADA APELLIDOS-------------------------------------------
###Creamos la etiqueta 2
e2 = tk.Label(ventana, text="Apellidos: ", bg="firebrick", fg="white")
e2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

###Con esto se crea una entrada de texto justo después de la etiqueta 2 CON EL ORGANIZADOR "PACK"
entrada2 = tk.Entry(ventana)
entrada2.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)


ventana.mainloop()
