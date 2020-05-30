from socket import *

def escaner():
    ip = input('Introduce IP: ')

    start = int(input("Introduce el puerto de inicio: "))

    end = int(input("Introduce el puerto de fin: "))

    print("Escaneando IP {}". format(ip))

    for port in range(start, end):
        print("Probando puerto {}".format(port))
        s = socket(AF_INET, SOCK_STREAM)

        s.settimeout(5)

        if s.connect_ex((ip, port)) == 0:
            print("Puerto {} abierto".format(port))

        s.close()

    print("Escaneo Finalizado")


def server():
    size = 512
    host = 'localhost'
    port = 5000
    #Family = Internet, type = stream socket means TCP
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    print("Listening in port {}".format(port))

    c, addr = sock.accept()

    data = c.recv(size)
    if data:
        print("Connection from : {}".format(sock[0]))

    sock.close()