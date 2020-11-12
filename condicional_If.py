print("Programa de evaluacion de notas de alumnos")
nota_alumno= input("Ingresar nota del alummno \n ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota < 5:
		valoracion="reprobado"
	return valoracion	

print(evaluacion(int(nota_alumno))) #ejecutar funcion evaluacion