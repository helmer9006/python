promedio = 0
suma = 0
cont = 0
repetir = True
cantNotas = int(input("Ingrese la cantidad de notas a promediar"))
while repetir:
        nota = int(input("ingresar nota"))
        suma += nota
        cont += 1
        if cantNotas < cont:
            repetir = False
print("El promedio es: ", suma/cont)
