#!/usr/bin/env python3

import socket

HOST = ""  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
try:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  # socker.AF_INET needs a 2-tuple (host, port)
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print("Connected by", addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print("Received msg: ", repr(data))
                    conn.sendall(b"msg delivered")


except Exception as ex:
    print("ERROR")
    print(str(ex))
