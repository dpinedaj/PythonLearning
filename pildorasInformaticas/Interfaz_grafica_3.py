from tkinter import *

raiz = Tk()

miFrame = Frame(raiz,width = 1200, height = 600)
miFrame.pack()

minombre = StringVar()

cuadroNombre = Entry (miFrame,textvariable=minombre)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="red",justify="center")

cuadroPassword = Entry(miFrame)
cuadroPassword.grid (row=1,column=1)
cuadroPassword.config(show = "*")

cuadroApellido = Entry (miFrame)
cuadroApellido.grid(row=2,column=1)

cuadroDireccion = Entry (miFrame)
cuadroDireccion.grid(row=3,column=1)

textoComentario = Text(miFrame,width=16,height=5)
textoComentario.grid(row=4,column=1,padx=10,pady=10)

scrollVert =Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4,column=2, sticky = "nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

nombreLabel = Label(miFrame,text="Nombre: ")
nombreLabel.grid(row = 0,column = 0, sticky = "e", pady = 10)

ApellidoLabel = Label(miFrame,text="Apellido: ")
ApellidoLabel.grid(row = 2, column = 0, sticky = "e", pady = 10)

DireccionLabel = Label(miFrame,text="Dirección de la casa: ")
DireccionLabel.grid(row = 3, column = 0, sticky = "e", pady = 10)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row = 1, column = 0, sticky = "e", pady = 10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

def codigoBoton():
    minombre.set("Daniel")

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()
raiz.mainloop()



