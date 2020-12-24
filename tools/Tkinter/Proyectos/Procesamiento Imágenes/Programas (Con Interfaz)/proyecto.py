# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:38:45 2016

@author: CkriZz
"""
############################################################################################
from tkinter import messagebox
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import Menu
from tkinter import Tk
from tkinter import NW
from PIL import Image
import numpy as np
############################################################################################
def abrir():
    ventana.filename = filedialog.askopenfilename(initialdir = "C:/Users/CkriZz/Pictures/PROYECTOFINAL",title = "Elige Tu Archivo De Imagen:", filetypes = (("Imagenes PNG", "*.png"),("Imagenes GIF ", "*.gif")))    
    global ruta    
    ruta = ventana.filename
    imagenL = PhotoImage(file = ruta)
    global abrirImagen
    abrirImagen = canvas.create_image(130, 150, anchor=NW, image=imagenL)
    ventana.mainloop()
############################################################################################
def grises():
    im = Image.open(ruta)
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i, j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i, j), pixel)
            j+=1
        i+=1
    g = im2.convert('L')
    g.save('C:/Users/CkriZz/Pictures/PROYECTOFINAL/RESULTADOS/grises.gif') 
    imagenL = PhotoImage(file = 'C:/Users/CkriZz/Pictures/PROYECTOFINAL/RESULTADOS/grises.gif')
    global grisesito
    grisesito = canvas.create_image(600, 150, anchor=NW, image=imagenL)
    ventana.mainloop()
############################################################################################
def otsu():
    canvas.delete(grises)    
    nombre = 'grises.gif'
    im = Image.open("C:/Users/CkriZz/Pictures/PROYECTOFINAL/RESULTADOS/" + nombre)
    ima = im
    col, ren = ima.size
    img = np.array(ima.getdata())
    thr = entrada.get()
    if thr==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        #Se Aplica la umbralización al "array" de la imagen
        #limites de procesado en x
        x_min, x_max = 0, col
        #limites de procesado en y
        y_min, y_max = 0, ren
        #imagen de salida
        img_out = np.zeros(col * ren)
        #procesado de la imagen
        loc = 0 #posicin del "pixel" actual
        for y in range (y_min, y_max):
            for x in range(x_min, x_max):
                loc = y * col + x
                if img[loc] > thr:
                    img_out[loc] = 255
                else:
                    img_out[loc] = 0
        img_thr = img_out
    im_otsu = img_thr.reshape(ren, col)
    im_otsu = Image.fromarray(im_otsu)
    im_otsu.save('C:/Users/CkriZz/Pictures/PROYECTOFINAL/RESULTADOS/otsu.gif') 
    imagenL = PhotoImage(file = 'C:/Users/CkriZz/Pictures/PROYECTOFINAL/RESULTADOS/otsu.gif')
    global Otsu    
    Otsu = canvas.create_image(600, 150, anchor=NW, image=imagenL)
    ventana.mainloop()
############################################################################################
def fondo():
    nombre = 'otsu.gif'
    im = Image.open("C:/Users/CkriZz/Pictures/PROYECTOFINAL/RESULTADOS/" + nombre)
    im3 = Image.open(ruta)
    im_otsu = im
    ren, col = im_otsu.size
    i = 0
    while i<ren:
        j = 0
        while j<col:
            if(im_otsu.getpixel((i,j))!=0):
                im3.putpixel((i,j),(255,0,0))
            j+=1
        i+=1
    im3.save('C:/Users/CkriZz/Pictures/PROYECTOFINAL/RESULTADOS/fondo.gif') 
    imagenL = PhotoImage(file = 'C:/Users/CkriZz/Pictures/PROYECTOFINAL/RESULTADOS/fondo.gif')
    global Otsu    
    Otsu = canvas.create_image(600, 150, anchor=NW, image=imagenL)
    ventana.mainloop()
############################################################################################
def limpiar():
    canvas.delete('all')
############################################################################################
"""Creacion De Ventana Y Lienzo (Canvas)"""
ventana = Tk()
w = 1000
h = 650
extraW=ventana.winfo_screenwidth() - w
extraH=ventana.winfo_screenheight() - h
ventana.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))
canvas = Canvas(ventana, width=1000, height=650)
canvas.pack()
ventana.title("Reconocimiento De Tumores")
entrada = IntVar()
Entry(ventana, textvariable = entrada, width = 8).place(x=110, y=60)
Label(text = "IMAGEN ORIGINAL", font= ("Times New Roman",14)).place(x=180, y=120)
Label(text = "IMAGEN PROCESADA", font= ("Times New Roman",14)).place(x=640, y=120)
Label(text = "INGRESE EL UMBRAL OPTIMO ", font= ("Times New Roman",9)).place(x=4, y=20)
Label(text = "PARA SEGMENTAR LA IMAGEN ", font= ("Times New Roman",9)).place(x=0, y=40)
Label(text = "EN ENTEROS ", font= ("Times New Roman",9)).place(x=20, y=60)
############################################################################################
"""Creacion De Los Menus"""
barraMenu = Menu(ventana)
mnuOpciones = Menu(barraMenu)
mnuInicio = Menu(barraMenu)
############################################################################################
"""Menu Unidad I"""
mnuInicio.add_command(label = "Abrir Imagen", command = abrir)
mnuInicio.add_separator()
mnuInicio.add_command(label = "Escala De Grises", command = grises)
mnuInicio.add_separator()
mnuInicio.add_command(label = "Segmentacion (Otsu)", command = otsu)
mnuInicio.add_separator()
mnuInicio.add_command(label = "Quitar Fondo Y Poner Tumor En Color Rojo", command = fondo)
############################################################################################
"""Menu Opciones"""
mnuOpciones.add_command(label = "Limpiar", command = limpiar)
mnuOpciones.add_separator()
mnuOpciones.add_command(label = "Salir", command = ventana.destroy)
############################################################################################
barraMenu.add_cascade(label = "Inicio", menu = mnuInicio)
barraMenu.add_cascade(label = "Opciones", menu = mnuOpciones)
ventana.config(menu = barraMenu)
ventana.mainloop()
############################################################################################