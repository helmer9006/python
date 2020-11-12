#las tuplas no se puede modificar, eliminar o agregar, solo listar
#no es necesario usar parentesis
tuplaUnitaria=("valor",)
mitupla=("Juan", 13,1,1995)
nombre, dia, mes, año = mitupla #asignando nombre a los valores de la tupla o campos - se denomina desempaquetado 



print(mitupla[0])#imprimir posicion 0 de la dupla 
milista=list(mitupla) # list sirve para convertir tupla en lista
nuevaTupla=tuple(milista)# tuple sirve para convertir lista en tupla
print(milista) #imprimir nueva lista creada de la tupla
print(nuevaTupla)#imprimiendo nueva dupla creada de la lista milista 
print("Juan" in nuevaTupla)#buscar Juan en la tupla
print(nuevaTupla.count(13))#count permite identificar cuantas veces esta un valor dentro de la tupla el numero 13 esta una sola vez en la tupla
print(len(nuevaTupla)) #len me permite identificar cuantos elementos tiene una tupla
print(len(tuplaUnitaria))#imprimiendo la cantidad de elementos de la dupla unitaria(1)
print(nombre) #imprimiendo valor de variable nombre de la tupla
print(año)#imprimiendo valor de variable año de la tupla
print(dia)#imprimiendo valor de variable dia de la tupla
print(mes)#imprimiendo valor de variable mes de la tupla