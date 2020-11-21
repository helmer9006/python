diccionario = {
    "nombre": "Helmer",
    "apellido": "Villarreal",
    "edad": 30,
    "nacimiento": "08/06/1990",
    "profesion": "Ingeniero de Sistemas"
}

#for llave in diccionario.keys(): #trae llaves
 #   print(llave)

#for llave in diccionario.keys(): #trae llaves
#    print(llave, ":", diccionario.get(llave))

#for llave, valor in diccionario.items():
#   print(llave, valor)
    
#print('Mi nombre es {nombre}, mi apellido es {apellido}, nací el {nacimiento}, y soy {profesion}'.format(**diccionario))            
#opcion 1
#print(diccionario.get('nombre'))  # opcion 2
# print(diccionario.values())
#diccionario.pop('edad') eliminar item opcion 1
#del diccionario['edad'] eliminar item opcion 2
#añadir un valor
diccionario['Hobby'] = 'Programación' # agregar elemento
print(diccionario['Hobby']) #
