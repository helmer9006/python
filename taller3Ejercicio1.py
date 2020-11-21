salarioMensual = 5000000

def calcularValorHora(salario):
    salarioDiario = 0
    salarioHora = 0
    salarioDiario = salario / 30
    salarioHora = salarioDiario / 8
    res = 'Mi salario mensual en 5 años quiero que sea de {0:.2f}'.format(
        salarioMensual),
    ' mi salario diario será de {0:.2f}'.format(salarioDiario),
    ' y mi salario por hora será de {0:.2f}'.format(salarioHora), '!'
    return res

print(calcularValorHora(salarioMensual))
