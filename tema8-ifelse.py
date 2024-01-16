print("Comparación de dos numeros")
a=int(input("Primer numero: "))
b=int(input("Segundo numero: "))

if a>b:
    print("{} es mayor a {}".format(a,b))
else: 
    if b>a:
        print("{} es mayor a {}".format(b,a))
    else: 
        if a==b:
            print("los valores son iguales")


print("\n\n Pedir una edad")
edad=int(input("Ingresa tu edad: "))

if edad>18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")