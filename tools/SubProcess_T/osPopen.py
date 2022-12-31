import os

p = os.popen("dir")
with open("prueba.txt", "w") as f:
    f.write(p.read())
