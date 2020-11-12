
print("""
***************************************************
*******************MENÚ CALCULADORA****************
***************************************************\n
SELECCIONAR OPERACIÓN A REALIZAR
1 - SUMA
2 - RESTA
3 - MULTIPLICACION
4 - DIVISIÓN
5 - SALIR

A continuación debe digitar el numero de la operación a realizar...
""")

# region TODAS LAS FUNCIONES


def suma(num1, num2):
    resultado = num1+num2
    return resultado


def resta(num1, num2):
    resultado = num1-num2
    return resultado


def multiplicacion(num1, num2):
    resultado = num1*num2
    return resultado


def division(num1, num2):
    resultado = num1/num2
    return resultado


def PedirNumeros():
    num1 = int(input("Ingresar primer número :"))
    num2 = int(input("Ingresar segundo número :"))
    return [num1, num2]


# endregion

# region BUCLE

while True:
    opcion = int(input("\nIngresar Opción : "))

    if(opcion == 1):
        num1, num2 = PedirNumeros()
        res = suma(num1, num2)
        print("La suma de {0} y {1} es ".format(num1, num2), res)
    elif(opcion == 2):
        num1, num2 = PedirNumeros()
        res = resta(num1, num2)
        print("La resta de {0} y {1} es ".format(num1, num2), res)
    elif(opcion == 3):
        num1, num2 = PedirNumeros()
        res = multiplicacion(num1, num2)
        print("La multiplicación entre {0} y {1} es ".format(num1, num2), res)
    elif(opcion == 4):
        num1, num2 = PedirNumeros()
        res = division(num1, num2)
        print("La división entre {0} y {1}".format(
            num1, num2), "es {0:.2f}".format(res))
    elif(opcion == 5):
        print("Has Finalizado.. Gracias.")
        break
    else:
        print("Opción Invalida")

# endregion
