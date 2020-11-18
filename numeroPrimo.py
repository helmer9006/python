import math
def validaPrimo(limite):
    numeros = list(range(2, limite+1))
    indice = 0
    while numeros[indice]**2 <= limite:
        for numero in numeros:
            if numero != numeros[indice]:
                if numero % numeros[indice] ==0:
                    numeros.remove(numero)
        indice+=1
    return numeros


def primo(numero):
    if numero < 2:
        return "El numero es Primo"
    elif numero == 2:
        return "El numero es Primo"
    else:
        raiz = int(math.sqrt(numero))+1
        for i in range(2, raiz):
            if numero % i == 0:
                return "El numero no es Primo"       
        return "El numero es Primo"     

print(validaPrimo(100))
print(primo(4))