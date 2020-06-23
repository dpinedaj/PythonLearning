from tkinter import *

root = Tk()

miFrame = Frame(root,width=500,height=400)
miFrame.pack()

miLabel=Label(miFrame,text="Texto a mostrar",fg="red",
font=("Comic Sans MS", 18)).place(x=100,y=200)####Permite ubicar el texto en cualquier lugar de la interfaz


root.mainloop()