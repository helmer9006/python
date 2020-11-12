print("************************************:")
print("Seleccionar el tipo de operación a realizar:(Escribir el Núnero de la opción)")
print("************************************:")
print("Tipo de producto financiero.")
print("Compra de Cartera: 1")
print("Crédito de libre inversión: : 2")
print("Crédito hipotecario: 3")
print("Tarjeta Crédito: 4")
print("Para salir opcion : 0")

repetir = True

while repetir:
    opcion = int(input("Ingresar número Opción: \n"))
    if opcion == 1:
        montoCredito = int(input("Ingresar Monto: \n"))
        tiempo = int(input("Ingresar cant meses: \n"))
        interes = montoCredito * 0.8 * tiempo / 100
        valorTotal = montoCredito + interes
        print("El interes es de", interes,
            "El valor total a pagar", valorTotal)

    elif opcion == 2:

        montoCredito = int(input("Ingresar Monto:: \n"))
        tiempo = int(input("Ingresar cant en meses: \n"))
        interes = montoCredito * 1.5 * tiempo / 100
        valorTotal = montoCredito + interes
        print("El interes es de", interes, "El valor total a pagar", valorTotal)

    elif opcion == 3:
        montoCredito = int(input("Ingresar Monto:: \n"))
        tiempo = int(input("Ingresar cant en meses: \n"))
        interes = montoCredito * 0.4 * tiempo / 100
        valorTotal = montoCredito + 6
        print("El interes es de", interes, "El valor total a pagar", valorTotal)

    elif opcion == 4:
        montoCredito = int(input("Ingresar Monto:: \n"))
        tiempo = int(input("Ingresar cant meses: \n"))
        interes = montoCredito * 2.16 * tiempo / 100
        valorTotal = montoCredito + interes
        print("El interes es de", interes, "El valor total a pagar", valorTotal)
    elif opcion == 0:
        repetir = False

    else:
        print("opcion invalida")
        
    print("\n\n\n Nuevo Ciclo")        
 print("Gracias...")