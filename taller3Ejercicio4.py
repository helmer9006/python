comprasSemanales = {
    'leche': 26000,
    'pan': 10000,
    'huevo': 16000,
    'arroz': 45000,
    'carne': 60000,
    'mecatos': 35000,
    'aseo': 80000
}


def calcularGastoMes(comprasSemanales):
    suma = 0
    for llave, valor in comprasSemanales.items():
        suma += valor
    return(suma)

def calcularGastoAnuales(comprasAnuales):
    suma = 0
    for llave, valor in comprasSemanales.items():
        suma += valor
    suma = suma * 12
    return(suma)


print('El total de gastos mensuales es de {0:.2f}'.format(calcularGastoMes(comprasSemanales)))
print('El total de gastos anuales es de {0:.2f}'.format(calcularGastoAnuales(comprasSemanales)))
