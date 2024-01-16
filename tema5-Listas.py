#listas
'''
    es una secuencia de elementos
    son mutables, es decir que se pueden modificar
    pueden almacenar diferentes tipos de datos
'''

lista=["Texto", 33, 6.5, False]
print(lista)
print(lista[:])
print(lista[2])
print(lista[-1])
print(lista[0:2])

lista.append("nuevo elemento")
print(lista)

lista.insert(2,"Cambio elemento")
print(lista)

lista.extend(["arreglo", 99, 45.5])
print(lista)

lista.remove(99) #Elimina según el valor del objeto, no por índice
print(lista)

lista.pop()
print(lista)

addLista=["Segundo", "Extra"]
newLista=lista+addLista
print(newLista)

print(addLista*2)

lista4=[2,5,9,6,1]
print(lista4)

lista4.sort()
print(lista4)

del lista4[0]
print(lista4)