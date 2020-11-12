array=[1, "mama", 2, "pedro", 250, 21.5] #declaracion de arreglo o lista
array.append("Helmer")#append agregar nuevo valor al final del array
array.insert(2, "Sandra")#insert agrega elemento al array en la posicion que queramos, recibo primer parametro indice donde agregar el valor y segundo el valor
array.extend(["juan", "luisa",500])#extend permite crear otro array que se anexará al original
print(array.index(1))#index permite buscar un elemento en el arreglo devolviendo el indice donde se encuentra, solo se debe pasar el valor a ser buscado
print("Helmer" in array)# funcion in permite buscar un valor en un array y devuelve true si se encuentra o false caso contrario
array.remove("Helmer")#remove permite eliminar el elementeo especificado por su valor
array.pop()#pop permite eliminar el ultimo elemento agregado al array o lista
print(array[:])#imprimir toda la lista o array
print(array[0])#imprimir posicion 0 del array
print(array[1])#imprimir posicion 1 del array
print(array[2])#imprimir posicion 2 del array
print(array[0:4])#imprimir un rango que inicia en la posicion 0 y excluye a partir de la posicion 4
print(array[:4])#imprimir un rango que inicia en la posicion 0(sino se coloca se asume que ese cero) y excluye a partir de la posicion 4 
print(array[3:])#accede a todos los dos elementos a partir de la posicion 3
#las listas se pueden sumar y funciona como concatenacion, el resultado es igual a extend 

