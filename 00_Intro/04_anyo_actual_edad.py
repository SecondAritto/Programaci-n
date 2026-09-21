print("Introduce tu año de nacimiento, por favor")
nacimiento = int(input())

print("Indica el año actual ")
anyo_actual = int(input())

edad = anyo_actual - nacimiento
print(edad)
if edad >= 18 :
	print("Eres mayor de edad")
else:
	print("Eres menor de edad")


print("llevas", edad - 3, "años estudiando")
