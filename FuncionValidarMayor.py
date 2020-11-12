
def maximo(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return x, y


num1 = int(input("Ingresar numero 1: "))
num2 = int(input("Ingresar numero 2: "))

print(maximo(num1, num2))
