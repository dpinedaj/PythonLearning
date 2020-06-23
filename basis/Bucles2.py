contador=0
miemail=input("Introduce tu dirección de email: ")
for i in miemail:
	if i=="@" or i==".":

		contador=contador+1

if contador>=2:
	print("Email es correcto")
else:
	print("El email no es correcto")




