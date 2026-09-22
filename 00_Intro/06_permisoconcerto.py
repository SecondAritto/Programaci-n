print("Introduce tu fecha de nacimiento")
nacimiento = int(input())
anyo_actual = 2026
edad = anyo_actual - nacimiento
mayor = 18
menor = 14

if edad >= mayor:
    print("Se te permite la asistencia")

else:

    if edad >= menor and edad < mayor:
        print("Tienes autorización de tus padres?")
        autorizacion = input()
        
        if autorizacion == "si":
            
            print("Se te permite la asistencia")
            
        else:
            print("No se te permite la asistencia")
    else:
        print("No se te permite la entrada por ser menor de 18 años")
