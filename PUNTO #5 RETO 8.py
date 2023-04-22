n = int(input("Introduce un número entero al que desea elevar 2: ")) # pedimos al usuario que introduzca el valor de n
resultado = 1 # valor inicial del resultado

for i in range(n): # Iniciamos un ciclo for que se ejecuta n veces
    resultado *= 2 # En cada iteración, multiplicamos resultado por 2 y lo asignamos a resultado

print("El resultado de 2 elevado a la " + str(n)+ " es " + str(resultado)) # resultado final: 2 elevado a la potencia n
