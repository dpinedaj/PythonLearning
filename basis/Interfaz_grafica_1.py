from tkinter import *
#-------------------------------------CREAR RAIZ O VENTANA PPAL------
raiz = Tk()
raiz.title("Ventana de pruebas")


#raiz.resizable(True,False) ##Limita la "redimensión" de la ventana

raiz.iconbitmap("Comida.ico")####Para cambiar la imágen de la plumita se debe ingresar una imagen.ico
raiz.geometry("650x350")##Asigna tamaño a la ventana "AnchoxAlto"
raiz.config(bg="blue",)##Varias configuraciones, color fondo o algunos más
raiz.config(bd = 45,relief="groove",cursor="hand2")

#---------------------CREAR EL PRIMER FRAME-------------------------
miFrame = Frame()
###-------combinando side y anchor se puede asignar posición---------
###------con fill se rellena toda una posición
###----para y, hay que usar fill="y", expand = True-----
miFrame.pack()
miFrame.config(bg="red",width = 650, height = 350)
miFrame.config(bd=35)##Tamaño de borde
miFrame.config(relief="sunken")#Asigna un relieve"sunken","groove"
miFrame.config(cursor="pirate")#Transforma el cursor cuando se pasa por le frame



raiz.mainloop()