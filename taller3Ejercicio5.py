ingresos = {
    "salarioDependiente": 2400000,
    "administracionTienda": 300000,
}

gastosFijos = {
    "ortodoncia": 80000,
    "cursoIngles": 180000,
    "diversion": 150000,
    "planCelular": 33000,
    "aporteHogar": 450000
}
gastosVariables = {
    "diversion": 150000,
    "otras": 100000
}


def calcularIngresos(ingresos):
    suma = 0
    for _, valor in ingresos.items():
        suma += valor
    return(suma)


def calcularEgresos(gastosVariables, gastosFijos):
    sumaGastosVariables = 0
    sumaGastosFijos = 0
    totalGastos = 0
    for _, valor in gastosVariables.items():
        sumaGastosVariables += valor
    for _, valor in gastosFijos.items():
        sumaGastosFijos += valor
    totalGastos = sumaGastosFijos + sumaGastosVariables
    Egresos = {"variables": sumaGastosVariables,
               "fijos": sumaGastosFijos, "totalEgresos": totalGastos}
    return Egresos


ingresos = calcularIngresos(ingresos)
egresos = calcularEgresos(gastosVariables, gastosFijos)
SaldoTotal = ingresos - egresos['totalEgresos']
print('El total de mis ingresos es de $ {0:.2f}'.format(ingresos), " mis egresos son de $ {0:.2f}".format(
    egresos['totalEgresos']), " y mi saldo es de $ {0:.2f}".format(SaldoTotal))
