import socket

funciones = (func for func in dir(socket) if func.islower() and not func.startswith('_'))
print("------FUNCIONES-----")
for i, fun in enumerate(funciones):
    print(i+1, fun)

constantes = (const for const in dir(socket) if const.isupper() and not const.startswith('_'))
print ("-----CONSTANTES-----")
for i, const in enumerate(constantes):
    print(i+1, const)

otras = (otra for otra in dir(socket) if otra.startswith('_'))
print("-----OTRAS----")
for i, otra in enumerate(otras):
    print(i+1, otra)
