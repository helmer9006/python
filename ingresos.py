cont = 0
ingresos = 0
numIngresos = int(input("Digite la cantidad Ingresos"))
repetir = True
while repetir:
    valorIngreso = int(input("ingresar Monto Ingreso"))
    ingresos += valorIngreso
    cont += 1
    if cont == numIngresos:
        repetir = False
print("El Total de Ingresos es de: ", ingresos/(cont))
