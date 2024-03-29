import socket
import sys


def checkPortSocket(ip, portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Puerto {}: \t Abierto".format(port))
            else:
                print("Puerto {}: \t Cerrado".format(port))
            sock.close()

    except socket.error as error:
        print(str(error))
        print("Error de conexion")
        sys.exit()


def testHost(host):
    try:
        print("gethostbyname")
        print(socket.gethostbyname_ex(host))

        print("\ngethostbyaddr")
        print(socket.gethostbyaddr("216.58.211.228"))

        print("\ngetfqdn")
        print(socket.getfqdn(host))

    except socket.error as error:
        print(str(error))
        print("Error de conexion")
        sys.exit()


checkPortSocket("localhost", [80, 8080, 443])

testHost("www.google.com")
