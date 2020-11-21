res = 0
salario = 3500000
baseCotizacion = 877803
porcentajeSalud = 12.5
transporte = 102854
porcentajePension = 16
tipoContrato = 'dependiente'


def calcularSalarioDependiente(salario, baseCotizacion, porcentajePension, porcentajeSalud, transporte):
    salud = (baseCotizacion * porcentajeSalud / 100)
    pension = (baseCotizacion * porcentajePension / 100)
    if salario < (baseCotizacion ** 2):
        totalaPagar = salario - salud - pension + transporte
        return totalaPagar
    else:
        totalaPagar = salario - salud - pension
        return totalaPagar

def calcularSalario(tipoContrato):
    if tipoContrato == 'dependiente':
        total = calcularSalarioDependiente(salario, baseCotizacion, porcentajePension, porcentajeSalud, transporte)
        return total
    else:
        salud = (salario * porcentajeSalud / 100)
        pension = (salario * porcentajePension / 100)
        total = salario - salud - pension
        return total
res = calcularSalario(tipoContrato)
print('salario es de ', salario, ' total a pagar es ', res, ' tipo contrato ', tipoContrato)

