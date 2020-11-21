horasTrabajadasDia = 8
valorHora = 40000
diasTrabajados = 20
salario = {}


def calcularSalarioDeseado(horas, valorHora, dias):
    salarioDiario = horas * valorHora
    salarioMensual = 20 * salarioDiario
    salarioAño = salarioMensual * 12
    salario = {
        "salarioDiario": salarioDiario,
        "salarioMensual": salarioMensual,
        "salarioAño": salarioAño
        }
    return salario


res = calcularSalarioDeseado(horasTrabajadasDia, valorHora, diasTrabajados)
for llave, valor in res.items():
    print(llave, valor)
    
#print('mi salario diario es ', res.salario['salarioDiario'], ' mi salario mensual es ', res.salario['salarioMensual'], 'mi salario anual es de ', res.salario['salarioAnual'])
