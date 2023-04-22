n=int(input("Ingresar numero mayor igual que 2 del cual dese saber los numeros pares antes de el : "))  # Se pide un número entero cualquiera
def pares_hasta_el_numero(n): # Definimos unas función  para ir hasta s 
    p = [] # Hacemos una lista vacia 
    for i in range(1,n+1): # Establecemos el rango y lo unimos a la lista 
        if i%2==0: # Si el residuo es igual a cero es par, unirlo a la lista 
            p.insert(0,i) # Se inserte a la lista vacia el número par i que se encuentra en el rango de 1 a n. La posición en la que se inserta el elemento es el índice 0, es decir, al principio de la lista.
    return p #
print("Los numeros pares de " + str(n) + " hasta 2 son: "+ str(pares_hasta_el_numero(n)))  # Imprimimos los numeros pares que se encuentran en el rango