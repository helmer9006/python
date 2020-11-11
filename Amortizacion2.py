print("Ejercicio de Amortización")
deuda = float(input("Ingrese el monto a prestar: "))
# periodos = int(input("Digite el tiempo del crédito: "))
interes = 0.01   # Equivalente a 10%
cuota = 1000000
totalPagado = 0
deudaInicial = deuda
cont = 1
intereses = (interes * deudaInicial)
pago = cuota - intereses
deuda_final = deudaInicial + intereses - cuota
while deuda_final > 0:
    print("Periodo", cont, "Deuda Inicial $ {0:.2f}".format(deudaInicial), " La tasa es de $ {0:.2f}".format(interes), " Los intereses son $ {0:.2f}".format(
        intereses), " El pago es de $ {0:.2f}".format(pago), " El saldo final es  {0:.2f}".format(deuda_final))
    intereses = (interes * deuda_final)
    pago = cuota - intereses

    # if pago > deudaInicial:
    #    print(pago, " ", deudaInicial, " ", intereses)
    #    cuota = deuda_final - intereses
    cont = cont + 1

    if (cuota - intereses) > deuda_final:
        pago = deuda_final - intereses
        #print('es menor aqui')
    deudaInicial = deuda_final
    deuda_final = deuda_final + intereses - cuota
    totalPagado = totalPagado + pago
    print("Periodo", cont, "Deuda Inicial $ {0:.2f}".format(deudaInicial), " La tasa es de $ {0:.2f}".format(interes), " Los intereses son $ {0:.2f}".format(
    intereses), "El Pago es de $ {0:.2f}".format(pago), " El saldo final es  {0:.2f}".format(deuda_final))
print("El total pagado fue $ {0:.2f}".format(totalPagado))
