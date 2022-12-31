import argparse

description = """ Ejemplos de uso: 
                + Escaneo basico:
                    -target 127.0.0.1
                +Indica un puerto especifico:
                    -target 127.0.0.1 -port 21
                +Solo mostrar puertos abiertos:
                    -target 127.0.0.1 --open True """

parser = argparse.ArgumentParser(
    description="port_scanning",
    epilog=description,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "-target", metavar="TARGET", dest="target", help="target to scan", required=True
)
parser.add_argument(
    "-p", "--port", dest="port", type=int, help="port to scan. Default 80", default=80
)
parser.add_argument(
    "-v",
    dest="verbose",
    default=0,
    action="count",
    help="verbosity level -v, -vv, -vvv",
)

parser.add_argument(
    "--open",
    dest="only_open",
    action="store_true",
    help="only display open ports",
    default=False,
)

params = parser.parse_args().__dict__

print(params)
