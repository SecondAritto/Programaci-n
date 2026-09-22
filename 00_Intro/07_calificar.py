print("Introduce las tres notas correspondientes a cada evaluación")
print("Indica tu nota de la primera evaluación")
primera = int(input())

print("Tiene evaluación continua?")
evaluacion1 = input()

print("Has entregado y aprobado el trabajo voluntario de la asignatura?")
trabajo1 = input()


print("Indica tu nota de la segunda evaluación")
segunda = int(input())

print("Tiene evaluación continua?")
evaluacion2 = input()

print("Has entregado y aprobado el trabajo voluntario de la asignatura?")
trabajo2 = input()


print("Indica tu nota de la tercera evaluación")
tercera = int(input())
print("Tiene evaluación continua?")
evaluacion3 = input()

print("Has entregado y aprobado el trabajo voluntario de la asignatura?")
trabajo3 = input()

notafinal = (evaluacion1 + evaluacion2 + evaluacion3) /3

print(notafinal)
