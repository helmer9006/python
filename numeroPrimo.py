lista = []
primos = []

for i in range(1,100):
    lista.append(i)


def primo(lista):
    cont = 0
    for num in lista:
        for i range(i, a):
            if num % i == 0:
                cont += 1
        if cont >= 2:
            primos.append(num)

    return primos
#print(lista)
print(primo(lista))