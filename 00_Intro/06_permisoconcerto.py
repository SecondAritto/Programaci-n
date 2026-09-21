print("Introduce tu fecha de nacimiento")
nacimiento = int(input())
edad = 18

if nacimiento == edad:
	print("Se te permite la asistencia")

else:
	if nacimiento > edad:
		print("Se te permite la asistencia")
	else:
		print("No se te permite la asistencia")
		
	 
