def sumar(a, b):
    return (a+b)


num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
res = sumar(num1, num2)
print("La suma de {0} y {1} es ".format(num1, num2), res)
