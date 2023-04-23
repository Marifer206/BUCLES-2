def factorial(num): # definir funcion para función calcular el factorial de un número.
    fact = 1
    for i in range(1, num+1): # Bucle for con la coleccion range
        fact *= i # multiplica fact por cada numero del rango en cada iteracion
    return fact # retorna el nuevo valoe de fact

def numeros_con_factorial(n): # funcion para imprimir los numeros desde 1 has n, junto con su respectivo factorial 
    for i in range(1, n+1): # Bucle for con la coleccion range
        print(i, "! =", factorial(i)) # imprimir el numero con su respectivo factorial

n=int(input("Ingresar el numero hasta el cual quiera saber su respectivo factorial: ")) # solicitar al usuario el numero
numeros_con_factorial(n)