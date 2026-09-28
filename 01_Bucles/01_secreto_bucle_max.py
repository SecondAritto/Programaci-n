print("Introduce un número")
introducir = int(input())
secreto = 4
if introducir == secreto :
	print("Has acertado!")
'''
else:
	print("No has acertado!")
	
'''
introducir = False
while introducir == False:
	if introducir != secreto:
		print("no has acertado")
		print("dame un numero")
	introducir =int(input())



'''
while True:
	if introducir == secreto:
		print("Has acertado")
	else:
		print("no has acertado")
	print("Dame un numero")
	introducir = int(input())
		
'''
		
		
'''
else :
	if introducir > secreto :
		print("El número es mayor que el introducido")
	
	else :
		print("El número es menor que el introducido")



if (introducir != secreto) :
	print("Venga! Dame otro número a ver si lo aciertas")
	numero2 = int(input())
	
 while numero2 != secreto :
	if (numero2 < introducir) and (introducir < secreto):
		print("Has introducido un nuúmero más pequeño todavía")
	if (numero2 > introducir) and (introducir > secreto):
		print("Has introducido un número todavía más grande!!!")
	if (numero2 > introducir) and (numero2 < secreto):
		print("Fallaste, pero has hecho caso. Has ido a más")
	if (numero2 < introducir) and (introducir > secreto):
		print("Fallo! pero has hecho caso y reducido")
'''
