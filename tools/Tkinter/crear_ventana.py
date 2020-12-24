import tkinter as tk

ventana = tk.Tk()
ventana.title("Primera ventana")

##Ancho x Alto
ventana.geometry('380x300')
ventana.configure(bg="dim gray")

etiqueta1 = tk.Label(ventana,text="Etiqueta 1",bg="red",fg="white")
etiqueta1.pack(padx = 20, pady = 20, side = tk.LEFT,fill = tk.Y)
### Pone la etiqueta pegada a la izquierda y rellena toda la zona izquierda
etiqueta2 = tk.Label(ventana,text="Etiqueta 2",bg="cadet blue",fg="black")
etiqueta2.pack(padx = 20, pady = 20) ####Deja espacio en el eje X y Y

etiqueta3 = tk.Label(ventana,text="Etiqueta 3",bg="medium sea green",fg="dark orange")
etiqueta3.pack(fill = tk.X)   ###Pone la etiqueta a lo largo del eje X

etiqueta4 = tk.Label(ventana,text="Etiqueta 4",bg="violet red",fg="snow2")
etiqueta4.pack(padx = 20, pady= 20, ipadx =20, ipady = 20)  ##Cambia el tamaño de la etiqueta en ipadx y y

##Crea un ciclo infinito (Mientras no se cierre la ventana
##T'odo lo que esté antes de esta línea se seguirá ejecutando...
##
ventana.mainloop()

