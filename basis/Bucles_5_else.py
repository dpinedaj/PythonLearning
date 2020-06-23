

email =input("Introduce tu email, por favor: ")

for i in email:
	if i=="@":
		arroba=True

		break

else:

	arroba=False

print(arroba)