"""
Programa que cree una lista de cuatro elementos y solicite al usuario cumplimentarlos uno a uno.
Pueden ser direcciones IP (192.168.1.1) o números de puerto (21,22,80). Tras rellenar todos los campos, estos deberán mostrarse en pantalla
"""


class Prueba1:
    def __init__(self):
        self.lista = []

    def rellenar_lista(self):
        for i in range(4):
            self.lista.append(input("Ingrese un elemento: "))


a = Prueba1()

a.rellenar_lista()

print(a.lista)
