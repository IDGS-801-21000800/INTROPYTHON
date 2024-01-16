#Tuplas
'''
    Son arreglos de python, 
    las tuplas son inmutables, es decir que no se pueden alterar
    pueden almacenar diferentes tipos de datos
'''

tupla=("uno", "dos", "tres")
print(tupla)

tuplaDatos=(12,True,24.5,"texto",12+3)
print(tuplaDatos)

print(tuplaDatos[2])
print(tuplaDatos[-1])
print(tuplaDatos[0:3])

sqrtTupla=(1,2,3,4,(1,2,3))
print(sqrtTupla)

a,b,c=tupla
print(a)
print(b)
print(c)

newTupla=tupla+tuplaDatos
print(newTupla)