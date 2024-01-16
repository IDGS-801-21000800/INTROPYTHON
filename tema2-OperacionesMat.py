#Operaciones básicas en python
num1=20
num2=30

print("la suma es", (num1+num2))
print("la resta es", (num1-num2))
print("el producto es", (num1*num2))
print("la división es", (num1/num2)) #con decimales
print("la división exacta es", (num1//num2)) #sin decimales
print("la potencia es", (num1**num2))

#Concatenacion en python
textoUno = "Hola"
textoDos = "Mundo"
textoFinal=textoUno+" "+ textoDos
print(textoFinal)

print("El saludo es %s %s" %(textoUno, textoDos))

saludoFinal="Saludo {} {}".format(textoUno, textoDos)
print(saludoFinal)

saludoFinal="Saludo {x} {y}".format(x=textoUno, y=textoDos)
print(saludoFinal)