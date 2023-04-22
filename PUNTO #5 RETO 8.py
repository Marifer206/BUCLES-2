n = int(input("Introduce un número entero al que desea elevar n: ")) # solicitar al usuario que introduzca el valor de n
resultado = 1 # valor inicial del resultado

for i in range(n): # Iniciar un ciclo for que se ejecuta n veces
    resultado *= 2 # En cada iteración, multiplica el resultado por 2 y lo asigna a resultado

print("El resultado de 2 elevado a la " + str(n)+ " es " + str(resultado)) # imprime el resultado final de 2 elevado a n 
