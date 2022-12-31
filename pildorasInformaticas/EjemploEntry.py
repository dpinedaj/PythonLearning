from tkinter import *

root = Tk()

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()


cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=0, column=1)

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0)  # Al tener el mismo x, se mueve a la izq

root.mainloop()
