from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import sys


def salir():
		exit()
def abrir():
		global archi1

		nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo",
		                             filetypes=(("Jpg files", "*.JPG"),
		                              ("todos los archivos", "*.*")))

		if nombrearch != '':
			archi1 = PIL.Image.open(nombrearch,"r")
			reducida = archi1.resize((500,300))
			muestra = ImageTk.PhotoImage(reducida)

			label=Label(Frame1,image=muestra)
			label.image=muestra
			label.pack()
			
def guardar():
	global im
	nombrearch = fd.asksaveasfilename(initialdir="/", title="Guardar como",
		                                  filetypes=(("Jpg files", "*.JPG"), 
		                                  	("todos los archivos", "*.*")))
	if nombrearch != '':
		im.save(nombrearch,format="JPEG")

	mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    ###TODO----------------------------------Aún no se soluciona------------------------------------------------------

def escala_de_grises():

	global archi1
	global im

	try:
		while True:

			valor=sd.askfloat("Input","Inserta un valor de qué tan gris lo quieres >=2: ")
			if valor<2:
				mb.showinfo("Error","Debe ser mayor o igual a 2")
			else:
				numero = valor
				break

		im = archi1
		i = 0
		while i < im.size[0]:
			j = 0
			while j < im.size[1]:
				r, g, b = im.getpixel((i,j))
				g = (r + g + b) / numero
				gris = int(g)
				pixel = tuple([gris,gris,gris])
				im.putpixel((i,j),pixel)
				j+=1
			i+=1
		reducida = im.resize((500, 300))
		salida = ImageTk.PhotoImage(reducida)
		label2=Label(Frame2,image=salida)
		label2.image = salida
		label2.pack()

	except NameError:
		mb.showerror(title="Alerta",message="Primero debe abrir la imagen")
	

def pixeles_imagen(im):

	im = abrir_imagen(im)
	pixeles = tuple(im.getdata())

	return(pixeles)

#comentarios que puedan ser legibles



	
#*----------------------------------------------------------Generar ventana----------------------------------------
ventana1= Tk()
ventana1.title("Procesador de imágenes")
ventana1.config(bg="black")
ventana1.geometry("1200x1000")


menubarra = Menu(ventana1)
ventana1.config(menu = menubarra)


menuarchivo = Menu(menubarra)
menuarchivo.add_command(label="Abrir", command= abrir)
menuarchivo.add_command(label="Guardar", command= guardar)
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command= salir)
menubarra.add_cascade(label="Archivo", menu=menuarchivo)

Frame1= Frame(ventana1,width=540,height=340)
Frame1.place(x=50,y=200)
Frame1.config(bd=20,relief="groove",cursor="hand2")

Frame2= Frame(ventana1,width=540,height=340)
Frame2.place(x=610,y=200)
Frame2.config(bd=20,relief="sunken",cursor="hand2")


Botongris = Button(ventana1,command=escala_de_grises,bg="gray",text="GRISES")
Botongris.place(x=50,y=50,height=100,width=100)
	





ventana1.mainloop()

