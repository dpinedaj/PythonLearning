from io import open

variable=open("archivo.txt","w")

for i in range(1000000):

	variable.write(f"{i}\n")

variable.close()

