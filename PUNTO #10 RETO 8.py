import math

def arctan_approx(x, n): # Definr la función arctan_approx que toma dos argumentos: x y n
    if x < -1 or x > 1: # Asegurse que el valor de x está en el rango [-1, 1]
        print("Error: el valor de x debe estar en el rango [-1, 1].")
        return

    approx = 0  # Inicializa la variable approx en 0
    for i in range(n): # Itera n veces, sumando cada término de la serie de Maclaurin para la arcotangente
        term = ((-1)**i * x**(2*i + 1)) / (2*i + 1) # Calcula cada término de la serie de Maclaurin utilizando la fórmula correspondiente
        approx += term # Suma el término actual a la aproximación acumulada

    error = abs(math.atan(x) - approx)# Calcula el error absoluto entre la aproximación y el valor real de la función arcotangente
    real = math.atan(x) # Calcula el valor real
    p_error = error / real * 100 # Calcula el porcentaje de error

    print(f"Aproximación: {approx:.6f}")  # Imprimime la aproximación
    print(f"Valor real: {math.atan(x):.6f}")  # Imprimime el valor real
    print(f"Error: {error:.6f}")  # Imprimime el error
    print(f"Porciento de error: {p_error:.6f}%")  # Imprime la diferencia entre ambos


    # Condicion para que el porcentaje de error sea mayor o menor a 0.1 %
    if p_error <= 0.1:
        print (f"El porcentaje de error es menor a 0.1%: {p_error:.6f}") 
    else:
        print (f"El porcentaje de error es mayor a 0.1%: {p_error:.6f}") 



x = float(input("Ingrese el valor de x para aproximar la función arcotangente: ")) #Solicitar el valor x
n = int(input("Ingrese el número de términos de la serie de Maclaurin que desea utilizar: ")) #solicitar el valor de n 


arctan_approx(x, n) # Llamar a la función arctan_approx para utilizarla con los valores dados por el usuario