print("Introduce un número")
introducir = int(input())
secreto = 4

if introducir == secreto :
	print("Has acertado!")

else :
	if introducir > secreto :
		print("El número es mayor que el introducido")
	
	else :
		print("El número es menor que el introducido")

while (secreto != 4):
	print("Venga! Dame otro número a ver si lo aciertas")
	numero2 = int(input())
