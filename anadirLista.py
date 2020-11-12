lista = [0,2,4,6,8,6,0,2,4,6,8,6]

def eliminar6(lista):
    for indice in lista:
        if(indice == 6):
            lista.remove(6)
    return lista


print(eliminar6(lista))

##lista.append(6)
#lista.insert(0,200) #insertar en la posicion que indiquemos
#lista.remove(6)#elimina el elemento indicado en parentesis
#lista.pop(6)#eliminar el elemento del indice indicado
#sort ordenar lista de menor a mayor
#len devuelve el valor del tamaño de la lista





