print("Verificación de Acceso")
edad_usuario = int(input("Ingresar tu Edad: \n"))
nota_alumno = int(input("Ingresar nota: \n"))

if edad_usuario < 18:
	print("No puedes ingresar, eres menor de edad")
elif edad_usuario >100:
	print("Edad invalida")	
else:
	print("Si puedes ingresar, eres mayor de edad")


##################################
#nota alumo

#nota_alumno = int(input("Ingresar nota: \n"))

if nota_alumno < 5:
	print('Tu calificacion es insuficiente')
elif nota_alumno < 6:
	print('Tu calificacion es suficinete')
elif nota_alumno < 7:
	print('Tu calificacion es Bien')
elif nota_alumno < 9:
	print('Tu calificacion es Notable')	
else:
	print('Tu calificacion es Sobesaliente')	
	
print("El programa ha finalizado")	