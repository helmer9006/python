monto = float(input("Ingrese el monto a prestar: "))
tiempo = int(input("Digite el tiempo del crédito: "))
opcionProducto = int(input("""Seleccionar el producto financiero a validar:
1. Crédito Hipotecario
2. Tarjeta Crédito
3. Crédito Libre Inversión
4. Compra de Cartera
\n\n
"""))
# region SELECCIONANDO PRODUCTO FINANCIERO
if(opcionProducto == 1):
    interes = 0.4
elif(opcionProducto == 2):
    interes = 2.16
elif(opcionProducto == 3):
    interes = 1.5
elif(opcionProducto == 4):
    interes = 0.8
else:
    print("Opción Invalida...")
# endregion

montoInicial = monto 

# region FUNCION PARA CALCULAR INTERES COMPUESTO
def InteresCompuesto(monto, tiempo, interes):

    for i in range(tiempo):
        ValorPorIntereses = (monto * (interes/100))
        monto = monto + ValorPorIntereses
    return monto
# endregion

# region FUNCION PARA CALCULAR INTERES SIMPLE

def InteresSimple(monto, tiempo, interes):
    res = 0
    for i in range(tiempo):
        ValorPorIntereses = monto * (interes/100)
        res = res + ValorPorIntereses
    return res
# endregion

# INVOCANDO FUNCION INTERES COMPUESTO
IntComp = InteresCompuesto(monto, tiempo, interes)
print("El Interes compuesto es: {0:.2f}".format(
      IntComp - montoInicial), " y el valor total a pagar  es: ""{0:.2f}".format(IntComp))

# INVOCANDO FUNCION INTERES SIMPLE
IntSimple = InteresSimple(monto, tiempo, interes)
print("El Interes simple es: {0:.2f}".format(IntSimple), "y el el valor total a pagar es: {0:.2f}".format(IntSimple + monto))
