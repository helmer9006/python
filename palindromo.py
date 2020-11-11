
def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    palabra = palabra.replace('á', 'a').lower()
    palabra = palabra.replace('é', 'e').lower()
    palabra = palabra.replace('í', 'i').lower()
    palabra = palabra.replace('ó', 'o').lower()
    palabra = palabra.replace('ú', 'u').lower()
    palabra = palabra.replace(':', '').lower()
    palabra = palabra.replace(',', '').lower()
    print(palabra)
    if palabra[::] == palabra[::-1]:
        return True

    else:
        return False


def run():
    palabra = input('Ingrese una palabra: ')
    if es_palindromo(palabra):
        print('Es palindromo')

    else:
        print('No es palindromo')

run()

