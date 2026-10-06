print("Introduce un número y mostraré su tabla")
multiplicando = int(input())

multiplicador = 0
diez = 10

print("Tabla del número", multiplicando)
while multiplicador<=diez:
	print(multiplicando, "  x  ", multiplicador, "   =   ", multiplicando * multiplicador)
	multiplicador = (multiplicador + 1)

print("listo")

