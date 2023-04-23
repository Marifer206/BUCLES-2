import math
n=int(input("Ingresar el numero hasta el cual quiera saber su respectivo factorial: ")) # Declarar n e inicializarla con el valor dado por el usario 
for i in range(1, n+1): # Bucle for con la coleccion range
    print(i, "! =", math.factorial(i)) # imprimir el numero con su respectivo factorial