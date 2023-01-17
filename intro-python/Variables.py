# Tipos de datos

# from re import M


palabra = 'Hola Mundo'
oracion = "Hola Mundo comilla doble "


# enteros 
entero = 20   #enteros
conDecimales = 20.2 #float
complejo = 1j

# print(palabra,oracion,entero, conDecimales, complejo)


#Listas 
lista = [1,2,3]  
print(lista)
lista.append('Hola chanchito')
print(lista)
# lista.clear() #Elimnar los elementos dentro de la lista

lista2 = lista.copy()
print(lista2)


#contar elementos dentro de una lista
print(lista.count(1))
# print("Numero de elementos de la lista: ", len(lista), len(lista2))

largoLista = len(lista)
largoLista2 = len(lista2)
print(largoLista,largoLista2)


