lista = []
pares = []
reversePares = []

for i in range(1, 101):
    lista.append(i)

def calPares(lista):
    for i in lista:
        if(i % 2 == 0):
            pares.append(i)
    return [pares]

def reversePar(pares):
    for i in reversed(pares):
        reversePares.append(i)
    return [reversePares]


print("pares",calPares(lista))
print('Reverso pares', reversePar(pares))
print(pares[3:11])
