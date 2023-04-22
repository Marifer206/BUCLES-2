Pares=[] # Crear una lista vacia para los numeros pares
Impares=[] # Crear una lista vacia para los numeros impares
for i in range(1,1001): # Bucle for con la coleccion range
    if i%2==0: # Si el residuo de la divison es cero es par
        Pares.append(i) # Metodo append para ingresar el numero par
    else:
        Impares.append(i) # Metodo append para ingresar el numero impar
print("Los numeros pares en el rango de 0 a 1000 son " + str(Pares)) # Imprimir lita de pares 
print("\n")
print("Los numeros impares en el rango de 0 a 1000 son " + str(Impares))  # Imprimir lita de impares 