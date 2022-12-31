import socket


def cliente():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Adress = ("ip", "puerto")
    s.connect(Adress)


def socket_bins():
    # Para conexiones desde la misma maquina
    socket.bind(("localhost", 5000))

    # Para conexiones desde toda la red
    socket.bind((socket.gethostname(), 5000))

    # El socket es alcanzable por cualquier conexion que tenga la maquina
    socket.bind(("", 5000))


def server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((socket.gethostname(), 5000))

    # Listen especifica cuantos clientes va a permitir.
    s.listen(5)
