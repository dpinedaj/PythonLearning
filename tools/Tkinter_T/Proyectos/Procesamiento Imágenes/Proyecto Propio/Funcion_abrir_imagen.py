##Esta librería tiene todas las herramientas para manipular imágenes###
from PIL import Image
import numpy as np


def abrir_imagen(im):

    ruta = "C:/Users/user/Desktop/Programación/Imagen/" + im
    im = Image.open(ruta)
    return im
    im.close()


def escala_de_grises(im):

    im = abrir_imagen(im)
    im.show()

    i = 0

    while i < im.size[0]:
        j = 0
        while j < im.size[1]:
            r, g, b = im.getpixel((i, j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im.putpixel((i, j), pixel)
            j += 1
        i += 1
    im.save("imagen.jpg")
    im.show()


def pixeles_imagen(im):

    im = abrir_imagen(im)
    pixeles = tuple(im.getdata())

    return pixeles


#####Inserte el nombre de la imagen###

escala_de_grises("grafica.jpg")
