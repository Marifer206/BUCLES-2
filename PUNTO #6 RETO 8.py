n = float(input("Ingresa el numero: ")) #Solicitar número que se quiere elevar 
e = int(input("Ingresa el exponente del numero: ")) # Solicitar el exponente del numero

resultado = 1 #Inicializar la variable resultado en 1

# Se utiliza un ciclo for para multiplicar x por sí mismo n veces
for i in range(e):
    resultado *= n

print(" El resultado de " + str(n) + " elevado a la " + str(e) + " es " + str(resultado) ) # Se imprime el resultado obtenido de la última iteración del ciclo for