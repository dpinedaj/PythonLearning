import argparse

parser = argparse.ArgumentParser(description='Paso de parametros')
parser.add_argument('-p1', dest='param1', help="parametro1")
parser.add_argument('-p2', dest='param2', help="parametro2")

parser.add_argument('-param', dest='param', type=int)

params = parser.parse_args()

print(params.param1)
print(params.param2)
print(params.param)
print(type(params.param))