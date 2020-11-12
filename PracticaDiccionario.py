#diccionarios son como los objetos en javascripts
miDiccionario = {
	"nombre": "Helmer",
	"apellido":"Villarreal",
	"edad":30,
	"nacimiento": "08/06/1990",
	"estado": "soltero"
}
miDiccionario['correo']="helmer@gmail.com" #añadir nuevo elemento al final del diccionario
print(miDiccionario)#imprimiendo todo el diccionario
print(miDiccionario['nombre'], miDiccionario['apellido']) #imprimiendo algunos valores del diccionario
miDiccionario['correo'] = 'helmer90@outlook.com' #modificar el atributo correo del diccionario
print(miDiccionario)#imprimiendo todo el diccionario
del miDiccionario['correo'] #eliminar la propiedad correo del diccionario
print(miDiccionario)#imprimiendo todo el diccionario

#####################################################
#otro diccionario con otro diccionario dentro
miDiccionario2 = {23: "jordan", "nombre": "Michael", "Equipo":"chicago", "anillos": {"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario2.keys())#funcion keys devuelve todas las claves del diccionario
print(miDiccionario2['anillos'])
print(miDiccionario2.values())# funcion values devuelove los valores de todas las llaves
print(len(miDiccionario2)) #devuelve la longitud o cantidad de atributos del diccionario