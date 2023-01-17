palabra = 'Hola Mundo';
oracion = "Hola Mundo comilla doble"

entero = 20
decimales = 12.3
complejo = 1j

# print(palabra, oracion, entero, decimales, complejo)

lista = ['Hola Chancho', 'Hola', 'Chanchito feliz']
# print(lista)

lista.append('Mateo Rodriguez'); ##Agregar elementos a la lista
# lista.clear() ##Eliminar los elementos dentro de la lista

lista2 = lista.copy()
# print('Lista 2 : ',  lista2)
# print('Lista de valores: ', lista)

# print(lista.count('Chanchito feliz')) ## Saber las veces que se repite un dato
# print('Total de valores de la lista:', len(lista),'Lista 2:', len(lista2))

# Accediendo a elementos de la lista
# print(lista[0])

# Eliminando elementos de una lista
# lista.pop()
# lista.pop()
# print(lista)

 # lista.remove('Hola Chancho')
# print(lista)

#Ordenar la lista
lista.reverse()
lista.sort()
print(lista)

#==============================
#Tuplas 
#==============================
tupla = (12,34,'Hola Mundo', 'Mateo Rodriguez')
print(tupla)
listaDeTupla = list(tupla)
# print(listaDeTupla.append('chanchito'))
# print(tupla[0])
# print(listaDeTupla)

rango = range(6)
# print(rango)

##Diccionario

diccionario = {
    "nombre": 'Mateo R',
    "edad": 20,
    "sexo": 'Masculino'
}

# print(diccionario)

# print(diccionario['nombre'])

diccionario ['Mardow'] = 'Super'
# print(diccionario)

del diccionario['nombre']
# print(diccionario)



flufly = {
    "nombre": "Flufly", 
    "edad": 4
}

mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Flufly": flufly,
    "Mamba": mamba
}
print(gatitos)


persona = dict(nombre="Mateo", apellido="Rodriguez",edad=19)
print(persona)

#Booleanos 
verdadero = True
falso = False

if(verdadero == True):
    print('el dato es verdadero')
else:
    print("No es falso")


